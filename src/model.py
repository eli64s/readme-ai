"""
src/model.py
"""
import os
import re
from typing import Dict

import openai
import spacy
from spacy.lang.en import English

import processor

openai.api_key = os.getenv("OPENAI_API_KEY")
nlp = spacy.load("en_core_web_sm")
parser = English()


class OpenAIError(Exception):
    """Raised when an error occurs with the OpenAI API."""


def code_to_text(files: Dict[str, str]) -> Dict[str, str]:
    """_summary_

    Parameters
    ----------
    files
        _description_

    Returns
    -------
        _description_

    Raises
    ------
    OpenAIError
        _description_
    OpenAIError
        _description_
    """
    docs = []
    try:
        for file_name, raw_code in files.items():
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
            _summary = summarize_text(summary)
            _summary = processor.add_space_between_sentences(_summary)
            docs.append((file_name, _summary))

    except openai.error.APIError as api_err:
        raise OpenAIError(f"OpenAI error: {api_err}") from api_err

    return docs


def generate_readme_features(url: str, prompt: str) -> str:
    """_summary_

    Parameters
    ----------
    url
        _description_
    prompt
        _description_

    Returns
    -------
        _description_
    """
    model_engine = "text-davinci-002"
    prompt = prompt.format(url)
    completions = openai.Completion.create(
        engine=model_engine, prompt=prompt, max_tokens=1024
    )
    generated_text = completions.choices[0].text
    return generated_text.lstrip()


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
