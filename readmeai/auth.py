"""Auth helpers for readme-ai.

Supports the existing OPENAI_API_KEY flow plus an optional local
OpenAI Codex OAuth credential file for bearer-token auth.
"""

from __future__ import annotations

import json
import os
import time
from pathlib import Path
from typing import Any

import click

OPENAI_CODEX_AUTH_PATH_ENV = "READMEAI_OPENAI_AUTH_FILE"
DEFAULT_OPENAI_CODEX_AUTH_PATH = Path.home() / ".config" / "readmeai" / "auth.json"


def _expand_auth_path(path: str | os.PathLike[str] | None = None) -> Path:
    raw = path or os.getenv(OPENAI_CODEX_AUTH_PATH_ENV) or str(DEFAULT_OPENAI_CODEX_AUTH_PATH)
    return Path(raw).expanduser()


def load_openai_codex_credentials(path: str | os.PathLike[str] | None = None) -> dict[str, Any] | None:
    auth_path = _expand_auth_path(path)
    if not auth_path.exists():
        return None

    data = json.loads(auth_path.read_text())
    if not isinstance(data, dict):
        return None

    creds = data.get("openai-codex")
    if not isinstance(creds, dict):
        return None

    if not creds.get("access"):
        return None

    return creds


def save_openai_codex_credentials(creds: dict[str, Any], path: str | os.PathLike[str] | None = None) -> Path:
    auth_path = _expand_auth_path(path)
    auth_path.parent.mkdir(parents=True, exist_ok=True)

    payload: dict[str, Any] = {}
    if auth_path.exists():
        try:
            existing = json.loads(auth_path.read_text())
            if isinstance(existing, dict):
                payload = existing
        except Exception:
            payload = {}

    payload["openai-codex"] = creds
    auth_path.write_text(json.dumps(payload, indent=2) + "\n")
    return auth_path


def refresh_openai_codex_credentials(path: str | os.PathLike[str] | None = None) -> dict[str, Any] | None:
    creds = load_openai_codex_credentials(path)
    if not creds:
        return None

    refresh = creds.get("refresh")
    if not isinstance(refresh, str) or not refresh:
        return None

    from readmeai.oauth_openai_codex import refresh_openai_codex_oauth

    refreshed = refresh_openai_codex_oauth(refresh)
    account_id = creds.get("accountId")
    if account_id and not refreshed.get("accountId"):
        refreshed["accountId"] = account_id
    save_openai_codex_credentials(refreshed, path)
    return refreshed


def get_openai_bearer_token() -> str | None:
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        return api_key

    creds = load_openai_codex_credentials()
    if creds:
        expires = creds.get("expires")
        if isinstance(expires, (int, float)) and time.time() * 1000 >= expires:
            try:
                creds = refresh_openai_codex_credentials() or creds
            except Exception:
                pass
        access = creds.get("access")
        if isinstance(access, str) and access:
            return access

    return None


def auth_source_label() -> str:
    if os.getenv("OPENAI_API_KEY"):
        return "OPENAI_API_KEY"
    if load_openai_codex_credentials():
        return f"OpenAI Codex OAuth file ({_expand_auth_path()})"
    return "none"


def login_openai_codex(
    path: str | os.PathLike[str] | None = None,
    *,
    open_browser: bool = True,
) -> Path:
    """Run the optional ChatGPT/Codex OAuth login flow.

    Stores credentials in a local JSON file for readme-ai to reuse.
    """

    from readmeai.oauth_openai_codex import login_openai_codex_oauth

    creds = login_openai_codex_oauth(open_browser=open_browser)
    return save_openai_codex_credentials(creds, path)


def print_login_success(auth_path: Path) -> None:
    click.echo(f"Saved OpenAI Codex OAuth credentials to {auth_path}")
