from enum import Enum


class LLMAuthKeys(str, Enum):
    """
    LLM API service environment variable keys.
    """

    ANTHROPIC_API_KEY = "ANTHROPIC_API_KEY"
    GOOGLE_API_KEY = "GOOGLE_API_KEY"
    OLLAMA_HOST = "OLLAMA_HOST"
    OPENAI_API_KEY = "OPENAI_API_KEY"


class LLMProviders(str, Enum):
    """
    LLM API services supported by readme-ai.
    """

    ANTHROPIC = "anthropic"
    GEMINI = "gemini"
    OLLAMA = "ollama"
    OPENAI = "openai"
    OFFLINE = "offline"


class AnthropicModels(str, Enum):
    """
    Enumerated list of supported Anthropic models.
    """

    CLAUDE3_HAIKU = "claude-3-haiku-20240307"
    CLAUDE3_OPUS = "claude-3-opus-20240229"
    CLAUDE3_SONNET = "claude-3-sonnet-20240229"
    CLAUDE35_SONNET = "claude-3-5-sonnet-20240620"


class GeminiModels(str, Enum):
    """
    Enumerated list of supported Gemini models.
    """

    GEMINI_FLASH_2 = "gemini-2.0-flash-exp"
    GEMINI_FLASH = "gemini-1.5-flash"
    GEMINI_PRO = "gemini-1.5-pro"


class OllamaModels(str, Enum):
    """
    Enumerated list of supported Ollama models.
    """

    LLAMA31 = "llama3.1"
    LLAMA32 = "llama3.2"
    GEMMA2 = "gemma2"
    MISTRAL = "mistral"
    QWEN = "qwen2.5-coder"


class OpenAIModels(str, Enum):
    """
    Enumerated list of supported OpenAI models.
    """

    GPT35_TURBO = "gpt-3.5-turbo"
    GPT4_TURBO = "gpt-4-turbo"
    GPT4O_MINI = "gpt-4o-mini"
    GPT4O = "gpt-4o"


class BaseURLs(str, Enum):
    """
    Enumerated list of supported API base URLs.
    """

    ANTHROPIC = "https://api.anthropic.com/"
    GEMINI = "https://generativelanguage.googleapis.com/"
    OLLAMA = "http://localhost:11434/"
    OPENAI = "https://api.openai.com/"
