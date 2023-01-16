"""
src/chatgpt_engine.py
"""
import openai

openai.api_key = "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"


def get_file_summary(file_str: str) -> str:
    text = f"Summarize the code in the following Python script: {file_str}"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=text,
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    summary_text = response["choices"][0]["text"].strip()
    return summary_text
