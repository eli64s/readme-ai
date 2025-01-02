import pytest
from readmeai.generators.colors.converters import hex_to_hls


@pytest.mark.parametrize(
    "hex_color,expected_hls",
    [
        ("#000000", (0.0, 0.0, 0.0)),  # Black
        ("#FFFFFF", (0.0, 1.0, 0.0)),  # White
        ("#FF0000", (0.0, 0.5, 1.0)),  # Red
        ("#00FF00", (0.333, 0.5, 1.0)),  # Green
        ("#0000FF", (0.667, 0.5, 1.0)),  # Blue
    ],
)
def test_hex_to_hls(hex_color: str, expected_hls: tuple[float, float, float]):
    """Test hex to HLS color conversion."""
    assert hex_to_hls(hex_color) == pytest.approx(expected_hls, abs=0.001)
