"""Tests for the LiteLLM API handler."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest
import tenacity
from readmeai.config.settings import ConfigLoader, Settings
from readmeai.extractors.models import RepositoryContext
from readmeai.models.enums import LLMProviders


def _make_litellm_exception(name: str):
    """Create a fake litellm exception with the correct qualname for retry logic."""
    exc_type = type(name, (Exception,), {})
    exc_type.__module__ = "litellm.exceptions"
    exc_type.__qualname__ = name
    return exc_type


@pytest.fixture
def litellm_handler(
    mock_config_loader: ConfigLoader,
    mock_repository_context: RepositoryContext,
):
    """Fixture to provide a LiteLLMHandler instance."""
    mock_config_loader.config.llm.api = LLMProviders.LITELLM.value
    mock_config_loader.config.llm.model = "openai/gpt-4o-mini"

    with patch.dict("sys.modules", {"litellm": MagicMock()}):
        from readmeai.models.litellm import LiteLLMHandler

        with patch("readmeai.models.litellm.LITELLM_AVAILABLE", True):
            handler = LiteLLMHandler(
                config_loader=mock_config_loader,
                context=mock_repository_context,
            )
            yield handler


@pytest.fixture
def litellm_handler_with_mock(litellm_handler):
    """Fixture with mocked litellm.acompletion for request tests."""
    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message=MagicMock(content="test_response"))]
    mock_acompletion = AsyncMock(return_value=mock_response)

    with patch("readmeai.models.litellm.litellm") as mock_litellm:
        mock_litellm.acompletion = mock_acompletion
        litellm_handler._mock_litellm = mock_litellm
        litellm_handler._mock_acompletion = mock_acompletion
        yield litellm_handler


# --- Attribute and initialization tests ---


def test_litellm_handler_sets_attributes(litellm_handler):
    """Test that the LiteLLM handler sets the correct attributes."""
    assert hasattr(litellm_handler, "model")
    assert hasattr(litellm_handler, "max_tokens")
    assert hasattr(litellm_handler, "temperature")
    assert litellm_handler.model == "openai/gpt-4o-mini"


def test_litellm_not_installed():
    """Test that ImportError is raised when litellm is not installed."""
    with (
        patch("readmeai.models.litellm.LITELLM_AVAILABLE", False),
        pytest.raises(ImportError, match="LiteLLM is not installed"),
    ):
        from readmeai.models.litellm import LiteLLMHandler

        LiteLLMHandler(
            config_loader=ConfigLoader(),
            context=MagicMock(),
        )


# --- Payload build tests ---


@pytest.mark.asyncio
async def test_litellm_build_payload(litellm_handler):
    """Test that the LiteLLM handler builds the correct payload."""
    prompt = "test_prompt"
    payload = await litellm_handler._build_payload(prompt)
    assert isinstance(payload, dict)
    assert payload["model"] == "openai/gpt-4o-mini"
    assert payload["max_tokens"] == litellm_handler.max_tokens
    assert payload["temperature"] == litellm_handler.temperature
    assert len(payload["messages"]) == 2
    assert payload["messages"][0]["role"] == "system"
    assert payload["messages"][1]["role"] == "user"
    assert payload["messages"][1]["content"] == "test_prompt"


@pytest.mark.asyncio
async def test_litellm_build_payload_includes_drop_params(litellm_handler):
    """Test that drop_params=True is always included in the payload."""
    payload = await litellm_handler._build_payload("any prompt")
    assert payload["drop_params"] is True


# --- Successful request tests ---


@pytest.mark.asyncio
async def test_make_request_success(litellm_handler_with_mock):
    """Test _make_request with a successful response."""
    handler = litellm_handler_with_mock
    index, result = await handler._make_request(
        "test_index",
        "test_prompt",
        100,
        None,
    )
    assert index == "test_index"
    assert result == "test_response"
    handler._mock_acompletion.assert_called_once()


@pytest.mark.asyncio
async def test_make_request_file_summary_caps_tokens(litellm_handler_with_mock):
    """Test that file_summary index caps max_tokens to 100."""
    handler = litellm_handler_with_mock
    await handler._make_request("file_summary", "test_prompt", 100, None)
    assert handler.max_tokens == 100


# --- None/empty prompt handling ---


@pytest.mark.asyncio
async def test_make_request_none_prompt(mock_config: Settings, litellm_handler):
    """Test _make_request with None prompt returns placeholder."""
    index, result = await litellm_handler._make_request(
        "test_index",
        None,
        100,
        None,
    )
    assert index == "test_index"
    assert result == mock_config.md.placeholder


@pytest.mark.asyncio
async def test_make_request_empty_prompt_from_token_handler(
    mock_config: Settings, litellm_handler
):
    """Test _make_request when token_handler returns empty string."""
    with patch(
        "readmeai.models.litellm.token_handler",
        new_callable=AsyncMock,
        return_value="",
    ):
        index, result = await litellm_handler._make_request(
            "test_index",
            "some_prompt",
            100,
            None,
        )
        assert index == "test_index"
        assert result == mock_config.md.placeholder


# --- Empty/malformed response handling ---


@pytest.mark.asyncio
async def test_make_request_empty_content(mock_config: Settings, litellm_handler):
    """Test _make_request when provider returns empty content."""
    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message=MagicMock(content=""))]

    with patch("readmeai.models.litellm.litellm") as mock_litellm:
        mock_litellm.acompletion = AsyncMock(return_value=mock_response)
        index, result = await litellm_handler._make_request(
            "test_index",
            "test_prompt",
            100,
            None,
        )
        assert index == "test_index"
        assert result == mock_config.md.placeholder


@pytest.mark.asyncio
async def test_make_request_none_content(mock_config: Settings, litellm_handler):
    """Test _make_request when provider returns None content."""
    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message=MagicMock(content=None))]

    with patch("readmeai.models.litellm.litellm") as mock_litellm:
        mock_litellm.acompletion = AsyncMock(return_value=mock_response)
        index, result = await litellm_handler._make_request(
            "test_index",
            "test_prompt",
            100,
            None,
        )
        assert index == "test_index"
        assert result == mock_config.md.placeholder


# --- Transient error retry tests ---


@pytest.mark.asyncio
async def test_make_request_rate_limit_triggers_retry(litellm_handler):
    """Test that RateLimitError triggers retry via tenacity."""
    rate_limit_error = _make_litellm_exception("RateLimitError")

    with patch("readmeai.models.litellm.litellm") as mock_litellm:
        mock_litellm.acompletion = AsyncMock(side_effect=rate_limit_error("429"))
        with pytest.raises(tenacity.RetryError):
            await litellm_handler._make_request(
                "test_index",
                "test_prompt",
                100,
                None,
            )
        assert mock_litellm.acompletion.call_count == 3


@pytest.mark.asyncio
async def test_make_request_timeout_triggers_retry(litellm_handler):
    """Test that Timeout error triggers retry via tenacity."""
    timeout_err = _make_litellm_exception("Timeout")

    with patch("readmeai.models.litellm.litellm") as mock_litellm:
        mock_litellm.acompletion = AsyncMock(side_effect=timeout_err("timed out"))
        with pytest.raises(tenacity.RetryError):
            await litellm_handler._make_request(
                "test_index",
                "test_prompt",
                100,
                None,
            )
        assert mock_litellm.acompletion.call_count == 3


@pytest.mark.asyncio
async def test_make_request_connection_error_triggers_retry(litellm_handler):
    """Test that APIConnectionError triggers retry."""
    api_conn_error = _make_litellm_exception("APIConnectionError")

    with patch("readmeai.models.litellm.litellm") as mock_litellm:
        mock_litellm.acompletion = AsyncMock(
            side_effect=api_conn_error("connection refused")
        )
        with pytest.raises(tenacity.RetryError):
            await litellm_handler._make_request(
                "test_index",
                "test_prompt",
                100,
                None,
            )
        assert mock_litellm.acompletion.call_count == 3


# --- Non-transient error tests (should NOT retry) ---


@pytest.mark.asyncio
async def test_make_request_auth_error_no_retry(mock_config: Settings, litellm_handler):
    """Test that authentication errors do NOT trigger retry."""
    auth_error = _make_litellm_exception("AuthenticationError")
    auth_error.__module__ = "litellm.exceptions"

    with patch("readmeai.models.litellm.litellm") as mock_litellm:
        mock_litellm.acompletion = AsyncMock(side_effect=auth_error("invalid api key"))
        index, result = await litellm_handler._make_request(
            "test_index",
            "test_prompt",
            100,
            None,
        )
        assert index == "test_index"
        assert result == mock_config.md.placeholder
        assert mock_litellm.acompletion.call_count == 1


# --- Transient error predicate tests ---


def test_transient_error_predicate_rate_limit():
    """Test _is_transient_litellm_error recognizes RateLimitError."""
    from readmeai.models.litellm import _is_transient_litellm_error

    rate_limit_error = _make_litellm_exception("RateLimitError")
    assert _is_transient_litellm_error(rate_limit_error("test")) is True


def test_transient_error_predicate_timeout():
    """Test _is_transient_litellm_error recognizes Timeout."""
    from readmeai.models.litellm import _is_transient_litellm_error

    timeout_exc = _make_litellm_exception("Timeout")
    assert _is_transient_litellm_error(timeout_exc("test")) is True


def test_transient_error_predicate_rejects_value_error():
    """Test _is_transient_litellm_error rejects ValueError."""
    from readmeai.models.litellm import _is_transient_litellm_error

    assert _is_transient_litellm_error(ValueError("empty response")) is False


def test_transient_error_predicate_rejects_unknown():
    """Test _is_transient_litellm_error rejects non-transient errors."""
    from readmeai.models.litellm import _is_transient_litellm_error

    assert _is_transient_litellm_error(TypeError("bad type")) is False
    assert _is_transient_litellm_error(RuntimeError("something")) is False


def test_transient_error_predicate_rejects_auth_error():
    """Test _is_transient_litellm_error rejects AuthenticationError."""
    from readmeai.models.litellm import _is_transient_litellm_error

    auth_error = _make_litellm_exception("AuthenticationError")
    assert _is_transient_litellm_error(auth_error("bad key")) is False


# --- Non-transient error tests (model not found, bad request) ---


@pytest.mark.asyncio
async def test_make_request_not_found_error_no_retry(
    mock_config: Settings, litellm_handler
):
    """Test that NotFoundError (bad model name) does NOT retry."""
    not_found_error = _make_litellm_exception("NotFoundError")

    with patch("readmeai.models.litellm.litellm") as mock_litellm:
        mock_litellm.acompletion = AsyncMock(
            side_effect=not_found_error("model not found")
        )
        index, result = await litellm_handler._make_request(
            "test_index",
            "test_prompt",
            100,
            None,
        )
        assert index == "test_index"
        assert result == mock_config.md.placeholder
        assert mock_litellm.acompletion.call_count == 1


@pytest.mark.asyncio
async def test_make_request_bad_request_error_no_retry(
    mock_config: Settings, litellm_handler
):
    """Test that BadRequestError (e.g. context overflow) does NOT retry."""
    bad_request_error = _make_litellm_exception("BadRequestError")

    with patch("readmeai.models.litellm.litellm") as mock_litellm:
        mock_litellm.acompletion = AsyncMock(
            side_effect=bad_request_error("context length exceeded")
        )
        index, result = await litellm_handler._make_request(
            "test_index",
            "test_prompt",
            100,
            None,
        )
        assert index == "test_index"
        assert result == mock_config.md.placeholder
        assert mock_litellm.acompletion.call_count == 1


@pytest.mark.asyncio
async def test_make_request_passes_drop_params_to_acompletion(
    litellm_handler,
):
    """Test that drop_params=True is passed through to litellm.acompletion."""
    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message=MagicMock(content="ok"))]

    with patch("readmeai.models.litellm.litellm") as mock_litellm:
        mock_litellm.acompletion = AsyncMock(return_value=mock_response)
        await litellm_handler._make_request("test_index", "test_prompt", 100, None)
        call_kwargs = mock_litellm.acompletion.call_args[1]
        assert call_kwargs["drop_params"] is True


@pytest.mark.asyncio
async def test_make_request_uses_correct_model_string(
    litellm_handler,
):
    """Test that the litellm model string format is passed correctly."""
    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message=MagicMock(content="ok"))]

    with patch("readmeai.models.litellm.litellm") as mock_litellm:
        mock_litellm.acompletion = AsyncMock(return_value=mock_response)
        await litellm_handler._make_request("test_index", "test_prompt", 100, None)
        call_kwargs = mock_litellm.acompletion.call_args[1]
        assert call_kwargs["model"] == "openai/gpt-4o-mini"


# --- Error predicate: additional non-transient types ---


def test_transient_error_predicate_rejects_not_found():
    """Test _is_transient_litellm_error rejects NotFoundError."""
    from readmeai.models.litellm import _is_transient_litellm_error

    not_found = _make_litellm_exception("NotFoundError")
    assert _is_transient_litellm_error(not_found("model")) is False


def test_transient_error_predicate_rejects_bad_request():
    """Test _is_transient_litellm_error rejects BadRequestError."""
    from readmeai.models.litellm import _is_transient_litellm_error

    bad_req = _make_litellm_exception("BadRequestError")
    assert _is_transient_litellm_error(bad_req("context")) is False


def test_transient_error_predicate_service_unavailable():
    """Test _is_transient_litellm_error recognizes ServiceUnavailableError."""
    from readmeai.models.litellm import _is_transient_litellm_error

    svc_err = _make_litellm_exception("ServiceUnavailableError")
    assert _is_transient_litellm_error(svc_err("503")) is True


def test_transient_error_predicate_internal_server():
    """Test _is_transient_litellm_error recognizes InternalServerError."""
    from readmeai.models.litellm import _is_transient_litellm_error

    internal = _make_litellm_exception("InternalServerError")
    assert _is_transient_litellm_error(internal("500")) is True


# --- Factory registration tests ---


def test_litellm_in_provider_enum():
    """Test that LITELLM is registered in the LLMProviders enum."""
    assert LLMProviders.LITELLM.value == "litellm"


def test_litellm_in_model_factory():
    """Test that LiteLLM is registered in ModelFactory."""
    from readmeai.models.factory import ModelFactory

    assert LLMProviders.LITELLM.value in ModelFactory._model_map
