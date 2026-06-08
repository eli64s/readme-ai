"""OpenAI Codex OAuth helpers for readme-ai.

These helpers support an optional ChatGPT/Codex-backed OpenAI auth mode
without changing the existing standard OpenAI API-key workflow.
"""

from __future__ import annotations

import base64
import hashlib
import os
import secrets
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Any
from urllib.parse import urlencode, urlparse, parse_qs

import httpx

import click

CLIENT_ID = "app_EMoamEEZ73f0CkXaXp7hrann"
AUTHORIZE_URL = "https://auth.openai.com/oauth/authorize"
TOKEN_URL = "https://auth.openai.com/oauth/token"
REDIRECT_URI = "http://localhost:1455/auth/callback"
SCOPE = "openid profile email offline_access"
JWT_CLAIM_PATH = "https://api.openai.com/auth"


def _b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode().rstrip("=")


def generate_pkce() -> tuple[str, str]:
    verifier = _b64url(secrets.token_bytes(32))
    challenge = _b64url(hashlib.sha256(verifier.encode()).digest())
    return verifier, challenge


def create_state() -> str:
    return secrets.token_hex(16)


def decode_jwt_payload(token: str) -> dict[str, Any] | None:
    try:
        parts = token.split(".")
        if len(parts) != 3:
            return None
        payload = parts[1]
        padding = "=" * (-len(payload) % 4)
        decoded = base64.urlsafe_b64decode(payload + padding)
        import json
        return json.loads(decoded)
    except Exception:
        return None


def get_account_id(access_token: str) -> str | None:
    payload = decode_jwt_payload(access_token)
    if not payload:
        return None
    auth = payload.get(JWT_CLAIM_PATH)
    if isinstance(auth, dict):
        account_id = auth.get("chatgpt_account_id")
        if isinstance(account_id, str) and account_id:
            return account_id
    return None


def build_auth_url(verifier: str, state: str) -> str:
    _, challenge = verifier, _b64url(hashlib.sha256(verifier.encode()).digest())
    params = {
        "response_type": "code",
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "scope": SCOPE,
        "code_challenge": challenge,
        "code_challenge_method": "S256",
        "state": state,
        "id_token_add_organizations": "true",
        "codex_cli_simplified_flow": "true",
        "originator": "pi",
    }
    return f"{AUTHORIZE_URL}?{urlencode(params)}"


def _token_exchange(payload: dict[str, str]) -> dict[str, Any]:
    with httpx.Client(timeout=30.0, follow_redirects=True) as client:
        response = client.post(
            TOKEN_URL,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data=payload,
        )
    response.raise_for_status()
    data = response.json()
    access = data.get("access_token")
    refresh = data.get("refresh_token")
    expires_in = data.get("expires_in")
    if not access or not refresh or not isinstance(expires_in, int):
        raise RuntimeError("OAuth token response missing fields")
    account_id = get_account_id(access)
    if not account_id:
        raise RuntimeError("Failed to extract ChatGPT account ID from token")
    return {
        "access": access,
        "refresh": refresh,
        "expires": int(__import__('time').time() * 1000) + (expires_in * 1000),
        "accountId": account_id,
    }


def exchange_code(code: str, verifier: str) -> dict[str, Any]:
    return _token_exchange(
        {
            "grant_type": "authorization_code",
            "client_id": CLIENT_ID,
            "code": code,
            "code_verifier": verifier,
            "redirect_uri": REDIRECT_URI,
        }
    )


def refresh_openai_codex_oauth(refresh_token: str) -> dict[str, Any]:
    return _token_exchange(
        {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "client_id": CLIENT_ID,
        }
    )


def get_openai_codex_session_headers(access_token: str, account_id: str | None = None, session_id: str | None = None) -> dict[str, str]:
    account_id = account_id or get_account_id(access_token)
    if not account_id:
        raise RuntimeError("Failed to extract ChatGPT account ID from token")

    headers = {
        "Authorization": f"Bearer {access_token}",
        "chatgpt-account-id": account_id,
        "OpenAI-Beta": "responses=experimental",
        "originator": "pi",
        "User-Agent": "readme-ai",
        "accept": "application/json, text/event-stream",
        "content-type": "application/json",
    }
    if session_id:
        headers["session_id"] = session_id
    return headers


def probe_openai_codex_responses(access_token: str, model: str = "gpt-4o-mini") -> dict[str, Any]:
    account_id = get_account_id(access_token)
    url = "https://chatgpt.com/backend-api/codex/responses"
    payload = {
        "model": model,
        "instructions": "You are a precise assistant. Follow the user exactly.",
        "input": [{"role": "user", "content": [{"type": "input_text", "text": "Reply with exactly: pong"}]}],
        "reasoning": {"effort": "low", "summary": "auto"},
        "text": {"verbosity": "low"},
        "store": False,
        "stream": True,
        "tool_choice": "auto",
        "parallel_tool_calls": True,
    }
    headers = get_openai_codex_session_headers(access_token, account_id)
    with httpx.Client(timeout=30.0, follow_redirects=True) as client:
        resp = client.post(url, headers=headers, json=payload)
        try:
            body = resp.json()
        except Exception:
            body = resp.text
        return {"status": resp.status_code, "body": body, "headers": dict(resp.headers)}


def probe_openai_codex_candidates(access_token: str, models: list[str]) -> list[dict[str, Any]]:
    results = []
    for model in models:
        try:
            result = probe_openai_codex_responses(access_token, model=model)
            results.append({"model": model, **result})
        except Exception as e:
            results.append({"model": model, "status": "exception", "body": repr(e), "headers": {}})
    return results


def login_openai_codex_oauth(*, open_browser: bool = True) -> dict[str, Any]:
    verifier, _challenge = generate_pkce()
    state = create_state()
    auth_url = build_auth_url(verifier, state)

    code_holder: dict[str, str | None] = {"code": None}

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):  # noqa: N802
            parsed = urlparse(self.path)
            if parsed.path != "/auth/callback":
                self.send_response(404)
                self.end_headers()
                return
            params = parse_qs(parsed.query)
            if (params.get("state", [None])[0]) != state:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"State mismatch")
                return
            code = params.get("code", [None])[0]
            if not code:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"Missing code")
                return
            code_holder["code"] = code
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"<html><body><p>Authentication successful. Return to your terminal.</p></body></html>")

        def log_message(self, format, *args):
            return

    click.echo("Starting OpenAI Codex OAuth login for readme-ai...")
    click.echo(auth_url)
    if open_browser and not os.getenv("READMEAi_NO_BROWSER"):
        try:
            webbrowser.open(auth_url)
        except Exception:
            pass

    server = HTTPServer(("127.0.0.1", 1455), Handler)
    server.timeout = 120
    try:
        while not code_holder["code"]:
            server.handle_request()
            if not code_holder["code"]:
                pass
    finally:
        server.server_close()

    code = code_holder["code"]
    if not code:
        pasted = click.prompt("Paste the authorization code or full redirect URL", default="", show_default=False)
        if "code=" in pasted:
            parsed = urlparse(pasted)
            params = parse_qs(parsed.query)
            if (params.get("state", [None])[0]) not in (None, state):
                raise RuntimeError("State mismatch")
            code = params.get("code", [None])[0]
        else:
            code = pasted.strip() or None

    if not code:
        raise RuntimeError("Missing authorization code")

    return exchange_code(code, verifier)
