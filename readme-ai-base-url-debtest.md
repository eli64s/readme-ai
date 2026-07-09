# DebTest: README-AI OpenAI-Compatible `base_url`

## Change
- Honor `llm.base_url` in the OpenAI handler for OpenAI-compatible endpoints.
- Preserve Ollama localhost fallback when no explicit compatible host is configured.
- Add deterministic handler tests for OpenAI, Ollama, OpenRouter-style, LM Studio-style, and custom Ollama-style endpoints.

## Risk Tier
- Medium

Why:
- Touches request transport construction for a core model handler.
- Incorrect normalization can break all OpenAI/Ollama requests or silently misroute them.

## Failure Modes Reviewed
- Bare host base URLs duplicate or omit `v1/chat/completions`.
- `/v1` base URLs duplicate `v1`.
- Full endpoint URLs get appended again.
- Ollama users lose the default localhost fallback.
- Focused tests fail for unrelated reasons because tokenization downloads leak into handler tests.

## Mitigations
- Normalize transport URLs with explicit handling for:
  - bare hosts
  - `/v1` bases
  - full endpoint URLs
- Keep Ollama fallback limited to OpenAI-default bases.
- Patch OpenAI handler tests to stub `token_handler`, matching the repo's Gemini test isolation pattern.

## Verification
- `python3 -m py_compile readmeai/models/openai.py tests/models/test_openai.py`
- `git diff --check`
- `poetry run pytest -o addopts='' tests/models/test_openai.py -n 0`

## Result
- Pass
- `11 passed`

## Residual Risk
- This PR does not add a new provider enum; it only makes the existing OpenAI-compatible path work correctly.
- I did not run the full repo test suite; I ran the closest focused handler slice that covers the changed behavior.
