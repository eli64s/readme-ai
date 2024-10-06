from readmeai.config.constants import (
    BadgeStyleOptions,
    ImageOptions,
    LLMService,
    ServiceAuthKeys,
)


def test_badge_options():
    assert BadgeStyleOptions.DEFAULT == "default"
    assert BadgeStyleOptions.FLAT == "flat"
    assert BadgeStyleOptions.FLAT_SQUARE == "flat-square"
    assert BadgeStyleOptions.FOR_THE_BADGE == "for-the-badge"
    assert BadgeStyleOptions.PLASTIC == "plastic"
    assert BadgeStyleOptions.SKILLS == "skills"
    assert BadgeStyleOptions.SKILLS_LIGHT == "skills-light"
    assert BadgeStyleOptions.SOCIAL == "social"


def test_image_options():
    assert ImageOptions.CUSTOM == "CUSTOM"
    assert ImageOptions.LLM == "LLM"
    assert (
        ImageOptions.BLACK
        == "https://img.icons8.com/external-tal-revivo-regular-tal-revivo/96/external-readme-is-a-easy-to-build-a-developer-hub-that-adapts-to-the-user-logo-regular-tal-revivo.png"
    )
    assert (
        ImageOptions.BLUE
        == "https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg"
    )
    assert (
        ImageOptions.CLOUD
        == "https://cdn-icons-png.flaticon.com/512/6295/6295417.png"
    )
    assert (
        ImageOptions.GRADIENT
        == "https://img.icons8.com/?size=512&id=55494&format=png"
    )
    assert (
        ImageOptions.GREY
        == "https://img.icons8.com/external-tal-revivo-filled-tal-revivo/96/external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-filled-tal-revivo.png"
    )
    assert (
        ImageOptions.PURPLE
        == "https://img.icons8.com/external-tal-revivo-duo-tal-revivo/100/external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-duo-tal-revivo.png"
    )


def test_model_options():
    assert LLMService.ANTHROPIC == "ANTHROPIC"
    assert LLMService.GEMINI == "GEMINI"
    assert LLMService.OLLAMA == "OLLAMA"
    assert LLMService.OPENAI == "OPENAI"
    assert LLMService.OFFLINE == "OFFLINE"


def test_secret_keys():
    assert ServiceAuthKeys.ANTHROPIC_API_KEY == "ANTHROPIC_API_KEY"
    assert ServiceAuthKeys.GOOGLE_API_KEY == "GOOGLE_API_KEY"
    assert ServiceAuthKeys.OLLAMA_HOST == "OLLAMA_HOST"
    assert ServiceAuthKeys.OPENAI_API_KEY == "OPENAI_API_KEY"
