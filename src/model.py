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


# os.environ["OPENAI_API_KEY"] = ""
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
    ignore = ["__init__", "setup.py"]
    try:
        for file_name, raw_code in files.items():
            if any(substr in file_name for substr in ignore):
                continue

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


def generate_readme_intro(url):
    match = re.search(r"github.com/([^/]*)/([^/]*)", url)
    if not match:
        raise ValueError("Invalid GitHub URL")

    owner = match.group(1)
    repo = match.group(2)
    model_engine = "text-davinci-002"
    prompt = (
        f"Generate a 'Usage' section for the {repo} repository on GitHub.\n\n"
        f"## Repository\n\n"
        f"Owner: {owner}\n"
        f"Name: {repo}\n\n"
        "## Usage\n\n"
        "### How to install\n\n"
        "### How to use\n\n"
        "### Example usage\n\n"
        "### API Reference\n\n"
        "### Parameters\n\n"
        "### Return Values\n\n"
        "### Exceptions\n\n"
        "### Contributing\n\n"
        "### License\n\n"
        "## Acknowledgments\n\n"
        "## References\n\n"
    )
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    text = response.choices[0].text.strip()
    return text.split("\n")[0]


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
