import asyncio
import json
import unicodedata
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Literal
from urllib.parse import parse_qs, urlparse

import aiohttp
from readmeai.core.logger import get_logger
from readmeai.utilities.file_handler import FileHandler

_logger = get_logger(__name__)

GITHUB_URLS = {
    "icons": "https://raw.githubusercontent.com/Aveek-Saha/GitHub-Profile-Badges/main/data/icons.json",
    "icons_backup": "https://raw.githubusercontent.com/Aveek-Saha/GitHub-Profile-Badges/master/data/icons.json",
}


def extract_logo_name(url: str) -> str:
    """Extract the logo name from the badge URL."""
    parsed = urlparse(url)
    query_params = parse_qs(parsed.query)
    if "logo" in query_params:
        return query_params["logo"][0].lower()
    return ""


def normalize_name(name: str) -> str:
    """Normalize badge key names to lowercase ASCII format."""
    try:
        name = bytes(name, "utf-8").decode("unicode-escape")
    except UnicodeError as e:
        _logger.warning(f"Error decoding Unicode escape sequences: {e}")
    name = normalize_unicode(name)
    name = name.lower()
    name = name.replace(" ", "_")
    # name = re.sub(r"[.\s\-]+", "_", name)
    # name = re.sub(r"[^a-z0-9_]", "", name)
    # name = re.sub(r"_+", "_", name)
    # name = name.strip("_")
    return name


def normalize_unicode(
    text: str, normalization: Literal["NFC", "NFKC", "NFD", "NFKD"] = "NFKD"
) -> str:
    """Decompose unicode characters and remove non-ASCII characters."""
    normalized = unicodedata.normalize(normalization, text)
    ascii_text = normalized.encode("ASCII", "ignore").decode("ASCII")
    return ascii_text


def transform_badge_data(data: Dict[str, Any]) -> Dict[str, list]:
    """Transform badge data from original format to new format."""
    transformed = {}

    if "icons" in data and isinstance(data["icons"], list):
        icons = data["icons"]
    elif "icons" in data and isinstance(data["icons"]["icons"], list):
        icons = data["icons"]["icons"]
    else:
        icons = []

    for icon in icons:
        badge_url = icon["src"].replace("style=for-the-badge", "style={0}")
        badge_data = [badge_url, icon["hex"]]
        name = normalize_name(icon["name"])
        transformed[name] = badge_data

        logo_name = extract_logo_name(badge_url)
        if logo_name and logo_name != name:
            transformed[logo_name] = badge_data
            _logger.debug(
                f"Added additional entry for logo name: {logo_name} (original: {name})"
            )

        unicode_name = normalize_unicode(icon["name"])
        if unicode_name != name:
            transformed[unicode_name] = badge_data
            _logger.debug(
                f"Added additional entry for Unicode name: {unicode_name} (original: {name})"
            )

    return transformed


def merge_badge_data(
    existing_data: Dict[str, list], new_data: Dict[str, list]
) -> Dict[str, list]:
    """
    Merge existing and new badge data, ensuring:
    - All keys are lowercase
    - No duplicate keys exist
    - Preserving unique entries
    """
    normalized_existing = {}
    for key, value in existing_data.items():
        if isinstance(value, list) and len(value) == 2:
            norm_key = normalize_name(key)
            value[0] = value[0].replace("style=for-the-badge", "style={0}")
            normalized_existing[norm_key] = value
            logo_name = extract_logo_name(value[0])
            if logo_name and logo_name != norm_key:
                logo_norm_key = normalize_name(logo_name)
                normalized_existing[logo_norm_key] = value

    normalized_new = {}
    for key, value in new_data.items():
        if isinstance(value, list) and len(value) == 2:
            norm_key = normalize_name(key)
            value[0] = value[0].replace("style=for-the-badge", "style={0}")
            normalized_new[norm_key] = value
            logo_name = extract_logo_name(value[0])
            if logo_name and logo_name != norm_key:
                logo_norm_key = normalize_name(logo_name)
                normalized_new[logo_norm_key] = value

    merged = {}
    for k, v in {**normalized_existing, **normalized_new}.items():
        if k not in merged:
            merged[k] = v

    return dict(sorted(merged.items()))


async def fetch_json(session: aiohttp.ClientSession, url: str) -> Dict[str, Any]:
    """Fetch JSON data from a URL, handling text/plain responses."""
    async with session.get(url) as response:
        response.raise_for_status()
        text_content = await response.text()
        try:
            return json.loads(text_content)
        except json.JSONDecodeError as e:
            _logger.debug(f"Error decoding JSON from {url}: {e!r}")
            _logger.debug(f"Response content: {text_content}")
            raise e


async def update_external_data(
    output_path: Path, raw_output_path: Path | None = None
) -> None:
    """Update the shields data from external GitHub repository."""
    existing_data = {}
    file_handler = FileHandler()
    url_main = GITHUB_URLS["icons"]

    if output_path.exists():
        try:
            existing_data = file_handler.read(output_path)
        except Exception as e:
            _logger.debug(f"Error reading existing shields data: {e!r}")

    async with aiohttp.ClientSession() as session:
        try:
            try:
                icons_data = await fetch_json(session, url_main)
            except (aiohttp.ClientError, json.JSONDecodeError):
                _logger.debug("Primary URL failed, trying backup...")
                icons_data = await fetch_json(session, GITHUB_URLS["icons_backup"])

            if raw_output_path:
                raw_output_path.parent.mkdir(parents=True, exist_ok=True)
                file_handler.write(raw_output_path, icons_data)
                _logger.debug(f"Saved raw shields data to {raw_output_path}")

            transformed_data = transform_badge_data(icons_data)
            merged_data = merge_badge_data(existing_data, transformed_data)

            output_path.parent.mkdir(parents=True, exist_ok=True)
            file_handler.write(output_path, merged_data)
            _logger.debug(f"Successfully updated shields data to {output_path}")
            _logger.debug(f"Total number of shields badges: {len(merged_data)}")

        except aiohttp.ClientError as e:
            _logger.debug(f"Error fetching shields data from {url_main}: {e!r}")
            raise e
        except Exception as e:
            _logger.debug(
                f"Unexpected error updating shields data from {url_main}: {e!r}"
            )
            raise e


if __name__ == "__main__":
    current_date = datetime.today().strftime("%Y%m%d")
    base_path = Path(__file__).parent.parent / "assets" / "badges"
    output_path = base_path / f"shields_{current_date}.json"
    raw_output_path = base_path / f"shields_raw_{current_date}.json"

    try:
        asyncio.run(
            update_external_data(
                output_path=output_path, raw_output_path=raw_output_path
            )
        )
    except KeyboardInterrupt:
        _logger.debug("\nOperation cancelled by user")
    except Exception as e:
        _logger.debug(f"Failed to update badge data: {e}")
        exit(1)
