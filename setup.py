"""Setup script for the readme-ai package."""

from pathlib import Path

from setuptools import find_namespace_packages, setup

BASE_DIR = Path(__file__).parent

with open(BASE_DIR / "requirements.txt") as file:
    required_packages = [line.strip() for line in file]

style_packages = ["black==21.9b0", "flake8", "isort"]
test_packages = ["pytest", "pytest-cov"]

setup(
    name="readme-ai",
    version="0.0.1",
    description="""🚀 Generate awesome README markdown files from the terminal, powered by OpenAI's GPT language model APIs 💫""",
    author="eli64s",
    author_email="zeroxeli@gmail.com",
    url="https://github.com/eli64s/readme-ai",
    python_requires=">=3.7",
    packages=find_namespace_packages(),
    install_requires=required_packages,
    extras_require={
        "dev": style_packages + test_packages + ["pre-commit==2.15.0"],
        "test": test_packages,
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=[
        "readme",
        "readme-badges",
        "readme-template",
        "autodoc",
        "readme-boilerplate",
        "awesome-readme",
        "readme-generator",
        "gpt-3",
        "readme-stats",
        "openai-api",
        "auto-readme",
        "ai-tools",
        "shieldsio-badges",
        "gpt-4",
        "llms",
        "openai-python",
        "chatgpt-python",
        "llmops",
        "openai-chatbot",
        "gpt-35-turbo",
    ],
    project_urls={
        "Documentation": "https://github.com/eli64s/readme-ai/blob/main/README.md",
        "Source Code": "https://github.com/eli64s/readme-ai",
    },
)
