"""OpenAI GPT3.5 model for generating summary text."""

import asyncio
import os
import re
from typing import Dict, Tuple

import httpx
import openai
import spacy
from spacy.lang.en import English

import preprocess
from logger import Logger

LOGGER = Logger("readmeai_logger")

openai.api_key = os.getenv("OPENAI_API_KEY")
nlp = spacy.load("en_core_web_sm")
parser = English()

# Use connection pooling
http_client = httpx.AsyncClient(
    http2=True,
    timeout=30,
    limits=httpx.Limits(max_keepalive_connections=10, max_connections=100),
)


class OpenAIError(Exception):
    """
    Custom exception class for OpenAI errors.

    Attributes
    ----------
    Exception : str
        The error message for the OpenAI API error.
    """


async def code_to_text(
    ignore_files: list,
    files: Dict[str, str],
) -> Dict[str, str]:
    """
    Generate summary text for code files using OpenAI's GPT-3.

    Parameters
    ----------
    files : Dict[str, str]
        A dictionary where the keys are file paths and values are raw code.

    Returns
    -------
    Dict[str, str]
        A dictionary where the keys are file paths and values are summary text.
    """

    tasks = []
    for file_path, raw_code in files.items():
        if any(fn in str(file_path) for fn in ignore_files):
            LOGGER.debug(f"File skipped: {file_path}")
            continue

        LOGGER.debug(f"Davinci processing: {file_path}")

        prompt = f"Create a summary description for this code: {raw_code}"
        prompt_length = len(prompt.split())
        if prompt_length > 4096:
            LOGGER.warning(f"Prompt too long: {file_path}")
            tasks.append(
                asyncio.create_task(
                    dummy_summary(file_path, "Prompt too long to generate summary.")
                )
            )
            continue

        # Use async client with connection pooling
        tasks.append(asyncio.create_task(fetch_summary(file_path, prompt)))

    results = await asyncio.gather(*tasks)

    return results


async def dummy_summary(file_path: str, summary: str) -> Tuple[str, str]:
    """
    Create a dummy summary for a given file path.

    Parameters
    ----------
    file_path : str
        The file path for which to create a dummy summary.
    summary : str
        The dummy summary to be returned.

    Returns
    -------
    Tuple[str, str]
        A tuple containing the file path and the dummy summary.
    """

    return (file_path, summary)


async def fetch_summary(file_path: str, prompt: str) -> Tuple[str, str]:
    """
    Fetch summary text for a given file path using OpenAI's GPT-3 API.

    Parameters
    ----------
    file_path : str
        The file path for which to fetch summary text.
    prompt : str
        The prompt to send to OpenAI's GPT-3 API.

    Returns
    -------
    Tuple[str, str]
        A tuple containing the file path and the generated summary text.
    """

    # Use async client with connection pooling
    response = await http_client.post(
        "https://api.openai.com/v1/engines/text-davinci-003/completions",
        json={
            "prompt": prompt,
            "temperature": 0,
            "max_tokens": 99,
            "top_p": 1,
            "frequency_penalty": 0.0,
            "presence_penalty": 0.0,
        },
        headers={"Authorization": f"Bearer {openai.api_key}"},
    )

    response.raise_for_status()
    data = response.json()

    if "choices" not in data or len(data["choices"]) == 0:
        raise OpenAIError("OpenAI response missing 'choices' field")

    file_summary = data["choices"][0]["text"]
    summary = re.sub(r"^[^a-zA-Z]*", "", file_summary)
    summary_spacy = summarize_text_spacy(summary)
    summary_spacy = preprocess.add_space_between_sentences(summary_spacy)
    return (file_path, summary_spacy)


def generate_summary_text(prompt: str) -> str:
    """
    Generate summary text from a given prompt using OpenAI's GPT-3 API.

    Parameters
    ----------
    prompt : str
        The prompt to send to OpenAI's GPT-3 API.

    Returns
    -------
    str
        The generated summary text.
    """

    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=44,
    )
    generated_text = completions.choices[0].text
    return generated_text.lstrip()


def summarize_text_spacy(summary: str) -> str:
    """
    Summarize text using the SpaCy library.

    Parameters
    ----------
    summary : str
        The text to be summarized.

    Returns
    -------
    str
        The summarized text.
    """

    summaries = nlp(summary)
    summary_text = ""
    for sent in summaries.sents:
        summary_text += sent.text.strip()
        if len(summary_text) > 120:
            break
    return summary_text
