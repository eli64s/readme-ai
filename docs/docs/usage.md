# Usage

This guide covers the basic usage of readme-ai and provides examples for different LLM services.

## Basic Usage

The general syntax for using readme-ai is:

```sh
readmeai --repository <REPO_URL_OR_PATH> --api <LLM_SERVICE> [OPTIONS]
```

Replace `<REPO_URL_OR_PATH>` with your repository URL or local path, and `<LLM_SERVICE>` with your chosen LLM service (openai, ollama, gemini, or offline).

## Examples

### Using OpenAI

```sh
readmeai --repository https://github.com/eli64s/readme-ai \
         --api openai \
         --model gpt-3.5-turbo
```

### Using Ollama

```sh
readmeai --repository https://github.com/eli64s/readme-ai \
         --api ollama \
         --model llama3
```

### Using Google Gemini

```sh
readmeai --repository https://github.com/eli64s/readme-ai \
         --api gemini \
         --model gemini-1.5-flash
```

### Offline Mode

```sh
readmeai --repository https://github.com/eli64s/readme-ai \
         --api offline
```

## Advanced Usage

You can customize the output using various options:

```sh
readmeai --repository https://github.com/eli64s/readme-ai \
         --api openai \
         --model gpt-4-turbo \
         --badge-color blueviolet \
         --badge-style flat-square \
         --header-style compact \
         --toc-style fold \
         --temperature 0.1 \
         --tree-depth 2 \
         --image LLM \
         --emojis
```

For a full list of options, run:

```sh
readmeai --help
```

See the [Configuration](configuration.md) page for detailed information on all available options.
