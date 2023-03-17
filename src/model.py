"""
src/model.py
"""
import os
import re
from typing import Dict

import openai
import spacy
from spacy.lang.en import English


openai.api_key = os.getenv("OPENAI_API_KEY")
nlp = spacy.load("en_core_web_sm")
parser = English()


class OpenAIError(Exception):
    """Raised when an error occurs with the OpenAI API."""


def code_to_text(engine: str, files: Dict[str, str]) -> Dict[str, str]:
    """Summarize Python code using OpenAI's Codex API.

    Parameters
    ----------
    engine : str
        The name of the OpenAI Codex engine to use.
    files : Dict[str, str]
        A dictionary of file names and code contents.

    Returns
    -------
    Dict[str, str]
        A dictionary of file names and code summaries.
    """
    doc_list = []

    try:
        for file, code in files.items():
            if "__init__" in file:
                continue

            prompt = f"Summarize the code provided below: {code}"

            response = openai.Completion.create(
                model=engine,
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
            _summary = summarize_text(summary)
            doc_list.append((file, _summary))

    except openai.error.APIError as api_err:
        raise OpenAIError(f"OpenAI error: {api_err}") from api_err

    return doc_list


def summarize_text(summary: str) -> str:
    """_summary_

    Parameters
    ----------
    summary
        _description_

    Returns
    -------
        _description_
    """
    doc = nlp(summary)
    summary_text = ""
    for sent in doc.sents:
        summary_text += sent.text.strip()
        if len(summary_text) > 120:
            break
    return summary_text
