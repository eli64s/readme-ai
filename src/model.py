"""
src/model.py
"""
import os
from typing import Dict

import openai


openai.api_key = os.getenv("OPENAI_API_KEY")


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
            if "__init__" in file or ".py" not in file:
                continue

            prompt = f"Summarize the Python code provided below: {code}"

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

            file_summary = response["choices"][0]["text"].strip()
            doc_list.append((file, file_summary))

    except openai.error.APIError as api_err:
        raise OpenAIError(f"OpenAI error: {api_err}") from api_err

    return doc_list
