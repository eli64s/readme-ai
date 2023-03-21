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
IGNORE = ["__init__", "requirements", "setup", "test", "README", "LICENSE"]

openai.api_key = os.getenv("OPENAI_API_KEY")
nlp = spacy.load("en_core_web_sm")
parser = English()


class OpenAIError(Exception):
    """Raised when an error occurs with the OpenAI API."""


def code_to_text(files: Dict[str, str]) -> Dict[str, str]:
    repo_contents = []
    prompt = "Generate summary documentation for code file: {}"
    try:
        for file_path, file_contents in files.items():
            if any(fn in file_path for fn in IGNORE):
                continue
            if file_path.startswith("."):
                continue

            LOGGER.info(f"Generating summary text for file: {file_path}")

            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt.format(file_contents),
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

            text_tuned = summarize_text_spacy(summary)

            text_cleaned = processor.add_space_between_sentences(text_tuned)

            if "\n" in text_cleaned:
                text_cleaned = text_cleaned.split("\n")[1]

            repo_contents.append((file_path, text_cleaned))

    except openai.error.APIError as api_err:
        raise OpenAIError(f"OpenAI error: {api_err}") from api_err

    return repo_contents


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
