# Ollama Integration

Ollama is a privacy-focused, open-source Large Language Model (LLM) that can be run locally to generate high-quality README content. Readme-ai integrates seamlessly with Ollama to provide a fast and privacy-friendly option for generating README files.

<sub>See more about Ollama on [GitHub](https://github.com/ollama/ollama).</sub>

## Configuration

```sh
readmeai --repository <REPO_URL_OR_PATH> --api ollama --model llama3
```

## Available Models

You can pull any model from the Ollama repository. Some recommended models include:
- `llama2`
- `mistral`
- `gemma2`

## Best Practices

- Ensure Ollama is running locally before using this option.
- Ollama models run offline, providing privacy and speed benefits.
