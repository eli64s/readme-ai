"""OpenAI GPT-3 model for generating summary text."""
import os
import re
from typing import Dict

import openai
import spacy
from spacy.lang.en import English

import processor
from logger import Logger

LOGGER = Logger("readme_ai_logger")
IGNORE = [
    ".*"
    "badges",
    ".json",
    ".md",
    ".pyc",
    ".txt",
    ".yml",
    ".yaml",
    ".json",
    ".config",
    ".log",
    ".ini",
    ".cfg",
    ".xml",
    ".toml",
    ".git",
    ".idea",
    "__pycache__",
    "__init__",
    "requirements",
    "setup",
    "test",
    "README",
    "LICENSE",
    "Makefile",
    "CONTRIBUTING",
    "CODE_OF_CONDUCT",
]

openai.api_key = os.getenv("OPENAI_API_KEY")
nlp = spacy.load("en_core_web_sm")
parser = English()


class OpenAIError(Exception):
    """Raised when an error occurs with the OpenAI API."""


def code_to_text(files: Dict[str, str]) -> Dict[str, str]:
    docs = []
    try:
        for file_path, raw_code in files.items():
            
            if any(fn in str(file_path) for fn in IGNORE):
                LOGGER.debug(f"File skipped: {file_path}")
                continue

            LOGGER.debug(f"Davinci processing: {file_path}")

            model_engine = "text-davinci-003"
            prompt = f"Create a summary description for this code: {raw_code}"
            response = openai.Completion.create(
                model=model_engine,
                prompt=prompt,
                temperature=0,
                max_tokens=100,
                top_p=1,
                frequency_penalty=0.0,
                presence_penalty=0.0,
            )

            if "choices" not in response or len(response["choices"]) == 0:
                raise OpenAIError("OpenAI response missing 'choices' field")

            file_summary = response["choices"][0]["text"]
            summary = re.sub(r"^[^a-zA-Z]*", "", file_summary)
            _summary = summarize_text_spacy(summary)
            _summary = processor.add_space_between_sentences(_summary)
            docs.append((file_path, _summary))

    except openai.error.APIError as api_err:
        raise OpenAIError(f"OpenAI error: {api_err}") from api_err

    return docs


def generate_summary_text(prompt: str) -> str:
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=44,
    )
    generated_text = completions.choices[0].text
    return generated_text.lstrip()


def summarize_text_spacy(summary: str) -> str:
    summaries = nlp(summary)
    summary_text = ""
    for sent in summaries.sents:
        summary_text += sent.text.strip()
        if len(summary_text) > 120:
            break
    return summary_text
