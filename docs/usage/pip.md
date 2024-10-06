---
title: Pip
---

# Using `pip` <p align="left"><a href="https://pypi.org/project/readmeai"><img src="https://img.shields.io/pypi/v/readmeai?color=3775A9&logo=pypi&label=PyPI&labelColor=3775A9&logoColor=white" alt="pypi-version"> &nbsp;</a><a href="https://github.com/eli64s/readme-ai"><img src="https://img.shields.io/github/stars/eli64s/readme-ai?color=3775A9&label=GitHub%20Stars&labelColor=3775A9&logo=github&logoColor=white" alt="github-stars"></a></p>

## Installation

To install `readmeai` from PyPI, simply run:

```sh
pip install readmeai
```

`pip` is the default Python package manager, and this command will download and install the latest version of `readmeai` from the Python Package Index (PyPI).

## With `pipx`

To install `readmeai` in an isolated environment using `pipx`, run:

```sh
pipx install readmeai
```
#### Using `pip`

[![pip](https://img.shields.io/badge/PyPI-3775A9.svg?style=flat&logo=PyPI&logoColor=white)](https://pypi.org/project/readmeai/)

???+ note "Python Version Requirement"
        Ensure you have Python version 3.9 or higher before installing readme-ai. For the latest Python installation guide, visit the

## Installation Using Pip

To install readme-ai from PyPI, simply run:

```sh
pipx install readmeai
```

`pip` is the default Python package manager, and this command will download and install the latest version of readme-ai from the Python Package Index (PyPI).

## Using `pip`

To install readme-ai in an isolated environment using `pipx`, run:

```sh
pipx install readmeai
```

???+ info "Why Use Pipx?"
        `pipx` allows you to install and run Python command-line applications in isolated environments, preventing conflicts with other Python projects.


## Running readme-ai

After installation, you can run readme-ai with:

```sh
readmeai --api openai --repository https://github.com/eli64s/readme-ai
```

Explanation of common arguments:

| Argument      | Description                           |
| ----------- | ------------------------------------ |
| `--api`       | Specifies the LLM API service to use (e.g., OpenAI, Ollama, Anthropic). |
| `--repository` | Specifies the GitHub repository or local directory path to analyze. |

## Building from Source

To build readme-ai from the source code, follow these steps:

1. Clone the repository from GitHub:

```sh
git clone https://github.com/eli64s/readme-ai
```

2. Navigate to the `readme-ai` directory:

```sh
cd readme-ai
```

3. Install dependencies:

```sh
pip install .
```

Alternatively, use `poetry` to build the project:

```sh
poetry install
```

## Optional Dependencies

To use additional LLM providers like **Anthropic** or **Google Gemini**, install the optional dependencies:

**Anthropic**:

```sh
pip install readmeai[anthropic]
```

**Google Gemini**:

```sh
pip install readmeai[gemini]
```

## Usage

### Setting Environment Variables

**OpenAI API Key**

Generate an OpenAI API key and set it as an environment variable:

```sh
export OPENAI_API_KEY=<your_api_key>
```

For Windows users, use:

```sh
set OPENAI_API_KEY=<your_api_key>
```

**Anthropic API Key**

To use the Anthropic API, set your API key:

```sh
export ANTHROPIC_API_KEY=<your_api_key>
```

### Running readme-ai

Run readme-ai with OpenAI:

```sh
readmeai --api openai --repository https://github.com/eli64s/readme-ai
```

Run readme-ai with Anthropic:

```sh
readmeai --api anthropic --repository https://github.com/eli64s/readme-ai
```

For a list of all available options, run:

```sh
readmeai --help
```

## Troubleshooting

1. **Permission Issues**: Ensure you have the necessary permissions to install Python packages. You may need to use `sudo` on Unix-based systems.
2. **Pipx Not Found**: Make sure `pipx` is properly installed and available in your PATH. You can find installation instructions [here](https://pipxproject.github.io/pipx/installation/).
3. **Missing Dependencies**: Some advanced features require additional Python packages. Check the [official documentation](https://github.com/eli64s/readme-ai) for a list of optional dependencies.

For further help, you can [open an issue](https://github.com/eli64s/readme-ai/issues) on GitHub or refer to the [official documentation](https://eli64s.github.io/readme-ai/).

## With Pip <p align="left">

<a href="https://pypi.org/project/readmeai"><img src="https://img.shields.io/pypi/v/readmeai?color=3775A9&logo=pypi&label=PyPI&labelColor=3775A9&logoColor=white" alt="pypi-version">

&nbsp;</a><a href="https://github.com/eli64s/readme-ai"><img src="https://img.shields.io/github/stars/eli64s/readme-ai?color=3775A9&label=GitHub%20Stars&labelColor=3775A9&logo=github&logoColor=white" alt="github-stars"></a></p>

Installing readme-ai using `pip` or `pipx` makes it easy to get started with the tool, allowing you to directly use the CLI in your local environment. This section details how to install readme-ai using `pip`, `pipx`, and additional methods like building from source or using Docker.

???+ note "Python Version Requirement"
        Ensure you have Python version 3.9 or higher before installing readme-ai. For the latest Python installation guide, visit the [official Python documentation](https://www.python.org/downloads/).

## Installation with Pip

Install readme-ai from PyPI with a single command:

```sh
pip install readmeai
```

Pip is the standard package manager for Python, and this command will download and install the latest version of readme-ai from the Python Package Index (PyPI).

## Installation with Pipx

Install readme-ai in an isolated environment using `pipx` to avoid conflicts between package dependencies:

```sh
pipx install readmeai
```

???+ info "Why Pipx?"
    Using `pipx` allows you to install and run Python command-line applications in isolated environments, which helps prevent dependency conflicts with other Python projects.

## Running the CLI

Run readme-ai directly after installation:

```sh
readmeai --api openai --repository https://github.com/eli64s/readme-ai
```

Explanation of common arguments:

| Argument      | Function                           |
| ----------- | ------------------------------------ |
| `--api`       | Specifies the LLM API service to use (e.g., OpenAI, Ollama, Anthropic). |
| `--repository` | Specifies the GitHub repository or local directory path to analyze. |


## Building from Source

To build readme-ai from the source code, follow these steps:

1. Clone the repository from GitHub:

```sh
git clone https://github.com/eli64s/readme-ai
```

2. Navigate to the `readme-ai` directory:

```sh
cd readme-ai
```

3. Install dependencies:

```sh
pip install .
```

Alternatively, you can use `poetry` to build the project:

```sh
poetry install
```

## Optional Dependencies

To use additional LLM providers like **Anthropic** or **Google Gemini**, install the optional dependencies:

Anthropic:

```sh
pip install readmeai[anthropic]
```

Google Gemini:

```sh
pip install readmeai[gemini]
```

## Usage

### Setting Environment Variables

**OpenAI API Key**

Ensure you have generated an OpenAI API key and set it as an environment variable:

```sh
export OPENAI_API_KEY=<your_api_key>
```

For Windows users, use:

```sh
set OPENAI_API_KEY=<your_api_key>
```

**Anthropic API Key**

To use the Anthropic API, set your Anthropic API key:

```sh
export ANTHROPIC_API_KEY=<your_api_key>
```

### Example Usage

Run readme-ai with OpenAI:

```sh
readmeai --api openai --repository https://github.com/eli64s/readme-ai
```

Run readme-ai with Anthropic:

```sh
readmeai --api anthropic --repository https://github.com/eli64s/readme-ai
```

For a list of all available options, run:

```sh
readmeai --help
```

## Troubleshooting

1. **Permission Issues**: Ensure you have the necessary permissions to install Python packages. You may need to use `sudo` on Unix-based systems.
2. **Pipx Not Found**: Make sure pipx is properly installed and available in your PATH. You can find installation instructions [here](https://pipxproject.github.io/pipx/installation/).
3. **Missing Dependencies**: Some advanced features require additional Python packages. Check the [official documentation](https://github.com/eli64s/readme-ai) for a list of optional dependencies.

For further help, you can [open an issue](https://github.com/eli64s/readme-ai/issues) on GitHub or refer to the [official documentation](https://eli64s.github.io/readme-ai/).
