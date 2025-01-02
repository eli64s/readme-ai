import colorsys


def hex_to_hls(hex_color: str) -> tuple[float, float, float]:
    """Converts a hex color to HLS."""
    hex_color = hex_color.lstrip("#")
    rgb = tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))
    return colorsys.rgb_to_hls(rgb[0] / 255, rgb[1] / 255, rgb[2] / 255)
