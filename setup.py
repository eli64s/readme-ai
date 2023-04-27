"""Setup file for the project."""

from pathlib import Path

from setuptools import find_namespace_packages, setup

BASE_DIR = Path(__file__).parent

with open(BASE_DIR / "requirements.txt") as file:
    required_packages = [line.strip() for line in file]

docs_packages = ["mkdocs==1.3.0", "mkdocstrings==0.18.1"]
style_packages = ["black==22.3.0", "flake8==3.9.2", "isort==5.10.1"]
test_packages = ["pytest==7.1.2", "pytest-cov==2.10.1", "great-expectations==0.15.15"]

setup(
    name="readmeai",
    version="0.1",
    description="Automated README generation using OpenAI's language model APIs.",
    author="eli64s",
    author_email="eli64s@example.com",
    url="https://github.com/eli64s/readme-ai",
    python_requires=">=3.7",
    packages=find_namespace_packages(),
    install_requires=required_packages,
    extras_require={
        "dev": docs_packages + style_packages + test_packages + ["pre-commit==2.19.0"],
        "test": test_packages,
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=[
        "readme",
        "readme-automation",
        "automated-readme",
        "openai",
        "openai-gpt3",
        "ai-tools",
    ],
    project_urls={
        "Documentation": "https://github.com/eli64s/readme-ai/blob/main/README.md",
        "Source Code": "https://github.com/eli64s/readme-ai",
    },
)
