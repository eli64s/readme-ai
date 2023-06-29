"""Setup script for the readme-ai package."""

from pathlib import Path

from setuptools import find_packages, setup


BASE_DIR = Path(__file__).parent / "requirements.txt"
with open(BASE_DIR) as file:
    required_packages = [line.strip() for line in file]

setup(
    name="readme-ai",
    version="0.0.3",
    description="🚀 Generate awesome README.md files from the terminal, powered by OpenAI's GPT language model APIs 💫",
    author="eli64s",
    author_email="0x.eli.64s@gmail.com",
    url="https://github.com/eli64s/readme-ai",
    python_requires=">=3.8.1",
    packages=find_packages(exclude=["tests"]),
    install_requires=required_packages,
    extras_require={
        "dev": [
            "black",
            "flake8",
            "isort",
            "pytest",
            "pytest-cov",
            "pre-commit",
        ],
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
    entry_points={
        "console_scripts": [
            "readme-ai = src.__main__:main",
        ],
    },
)
