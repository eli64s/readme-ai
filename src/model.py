"""src/model.py."""
import os
from typing import Dict

import openai


openai.api_key = os.getenv("OPENAI_API_KEY")


def code_to_text(engine: str, files: Dict[str, str]) -> Dict[str, str]:
    """_summary_

    Parameters
    ----------
    engine
        _description_
    files
        _description_

    Returns
    -------
        _description_
    """
    doc_list = []

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
        file_summary = response["choices"][0]["text"].strip()
        doc_list.append((file, file_summary))
    return doc_list
