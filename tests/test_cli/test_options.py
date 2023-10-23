"""Unit tests for the CLI options module."""

from readmeai.cli import options


def test_api_key_default():
    assert options.api_key.default is None


def test_badges_choices():
    assert options.badges.type.choices == [
        "flat",
        "flat-square",
        "for-the-badge",
        "plastic",
        "social",
        "apps",
        "apps-light",
    ]


def test_badges_default():
    assert options.badges.default == "flat-square"


def test_emojis_default():
    assert options.emojis.default is True


def test_emojis_type():
    assert options.emojis.type == bool


def test_model_default():
    assert options.model.default == "gpt-3.5-turbo"


def test_offline_default():
    assert options.offline.default is False


def test_offline_type():
    assert options.offline.type == bool


def test_output_default():
    assert options.output.default == "readme-ai.md"


def test_repository_required():
    assert options.repository.required is True


def test_temperature_default():
    assert options.temperature.default == 1.0


def test_temperature_type():
    assert options.temperature.type == float
