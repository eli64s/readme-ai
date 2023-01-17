"""src/chatgpt_engine.py."""
import os
from typing import Dict

import openai

openai.api_key = os.getenv("API_SK")


def code_to_text(engine: str, files: Dict[str, str]) -> Dict[str, str]:
    """Summarize the code in the following Python script: file.

    Args:
        file (str): The name of the file to summarize

    Returns:
        str: The summary of the file
    """
    l = []
    for file, code in files.items():
        prompt = f"Summarize the code in the following Python script: {code}"
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
        l.append((file, file_summary))
    return l
