"""Setup script for the README-AI package."""

from pathlib import Path

from setuptools import find_namespace_packages, setup

BASE_DIR = Path(__file__).parent

with open(BASE_DIR / "requirements.txt") as file:
    required_packages = [line.strip() for line in file]

docs_packages = ["mkdocs", "mkdocstrings"]
style_packages = ["black==21.9b0", "flake8", "isort"]
test_packages = [
    "pytest",
    "pytest-cov",
    "great-expectations",
]

setup(
    name="readme_ai",
    version="1.0.0",
    description="""
        CLI tool that generates comprehensive README Markdown
        files, powered by OpenAI's GPT language model APIs.""",
    author="eli64s",
    author_email="",
    url="https://github.com/eli64s/README-AI",
    python_requires=">=3.7",
    packages=find_namespace_packages(),
    install_requires=required_packages,
    extras_require={
        "dev": docs_packages + style_packages + test_packages + ["pre-commit==2.15.0"],
        "test": test_packages,
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=[
        "ai",
        "auto-documentation",
        "auto-readme",
        "automated-readme",
        "badges",
        "chatgpt-python",
        "command-line-tool",
        "documentation",
        "gpt-3",
        "gpt-4",
        "nlp",
        "openai",
        "openai-api",
        "openai-gpt3",
        "python",
        "readme",
        "readme-automation",
        "readme-generator",
        "readme-generator-template",
        "readme-template",
    ],
    project_urls={
        "Documentation": "https://github.com/eli64s/README-AI/blob/main/README.md",
        "Source Code": "https://github.com/eli64s/README-AI",
    },
)
