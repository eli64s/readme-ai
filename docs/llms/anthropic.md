---
title: Ollama Installation Guide
---

# Installation Guide for readme-ai with Ollama <p align="left"><a href="https://github.com/eli64s/readme-ai"><img src="https://img.shields.io/github/stars/eli64s/readme-ai?color=3775A9&label=GitHub%20Stars&labelColor=3775A9&logo=github&logoColor=white" alt="github-stars"></a></p>

Get started with readme-ai using Ollama. This guide will show you how to install and run readme-ai using Ollama in your local environment.

???+ note "Ollama Requirement"
    Ensure you have Ollama installed and running on your system. For the latest installation guide, visit the [Ollama GitHub repository](https://github.com/ollama/ollama).

## Installation Using Ollama

To use readme-ai with Ollama, follow these steps:

1. **Install Ollama**

   Ensure you have installed Ollama on your system. You can find detailed installation instructions on the [Ollama GitHub page](https://github.com/ollama/ollama).

2. **Pull the LLM Model**

   Pull the required LLM model to use with Ollama:

   ```sh
   ollama pull llama3:latest
   ```

3. **Start the Ollama Server**

   Start the Ollama server locally:

   ```sh
   export OLLAMA_HOST=127.0.0.1 && ollama serve
   ```

4. **Run readme-ai with Ollama**

   After starting the server, run readme-ai with Ollama:

   ```sh
   readmeai --api ollama --model llama3 --repository https://github.com/eli64s/readme-ai
   ```

Explanation of common arguments:

| Argument      | Description                           |
| ----------- | ------------------------------------ |
| `--api`       | Specifies the LLM API service to use (in this case, Ollama). |
| `--model`     | Specifies the model to use with Ollama (e.g., llama3). |
| `--repository` | Specifies the GitHub repository or local directory path to analyze. |

## Optional Dependencies

To use additional LLM providers like **Anthropic** or **Google Gemini** in addition to Ollama, install the optional dependencies:

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

**Ollama Host**

Set the Ollama host to enable the local server:

```sh
export OLLAMA_HOST=127.0.0.1
```

For Windows users, use:

```sh
set OLLAMA_HOST=127.0.0.1
```

### Running readme-ai with Ollama

Run readme-ai with the Ollama model:

```sh
readmeai --api ollama --model llama3 --repository https://github.com/eli64s/readme-ai
```

For a list of all available options, run:

```sh
readmeai --help
```

## Troubleshooting

1. **Server Connection Issues**: Ensure that the Ollama server is running and accessible. Verify that the host address is set correctly.
2. **Model Not Found**: Make sure that the required LLM model is properly pulled using the `ollama pull` command.
3. **Permission Issues**: Ensure you have the necessary permissions to run commands with Ollama. You may need administrative rights on your system.

For further help, you can [open an issue](https://github.com/eli64s/readme-ai/issues) on GitHub or refer to the [official documentation](https://eli64s.github.io/readme-ai/).
