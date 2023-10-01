from unittest.mock import patch

import pytest

from readmeai.core import model


@pytest.fixture
def openai_handler():
    return model.OpenAIHandler(model.config)


@pytest.fixture
def code():
    return """
    def hello_world():
        print("Hello, world!")
    """


@pytest.fixture
def chat():
    return "What is the meaning of life?"


@pytest.mark.asyncio
async def test_code_to_text(openai_handler, code):
    with patch.object(openai_handler, "openai") as mock_openai:
        mock_openai.Completion.create.return_value.choices[
            0
        ].text = "This is some generated text."
        text = await openai_handler.code_to_text(code)
        mock_openai.Completion.create.assert_called_once_with(
            engine=model.config["openai_engine"],
            prompt=model.config["code_to_text_prompt"].format(code=code),
            max_tokens=model.config["openai_max_tokens"],
            n=model.config["openai_n"],
            stop=model.config["openai_stop"],
            temperature=model.config["openai_temperature"],
        )
        assert text == "This is some generated text."


@pytest.mark.asyncio
async def test_chat_to_text(openai_handler, chat):
    with patch.object(openai_handler, "openai") as mock_openai:
        mock_openai.Completion.create.return_value.choices[
            0
        ].text = "This is some generated text."
        text = await openai_handler.chat_to_text(chat)
        mock_openai.Completion.create.assert_called_once_with(
            engine=model.config["openai_engine"],
            prompt=model.config["chat_to_text_prompt"].format(chat=chat),
            max_tokens=model.config["openai_max_tokens"],
            n=model.config["openai_n"],
            stop=model.config["openai_stop"],
            temperature=model.config["openai_temperature"],
        )
        assert text == "This is some generated text."


def test_generate_code_from_text(openai_handler):
    text = "This is some generated text."
    code = openai_handler.generate_code_from_text(text)
    assert code.startswith("def ")
    assert "print(" in code
    assert "Hello, world!" in code


def test_generate_chat_response(openai_handler):
    text = "This is some generated text."
    response = openai_handler.generate_chat_response(text)
    assert isinstance(response, str)
