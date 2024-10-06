# CLI Usage

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
         --model gpt-3.5-turbo # (1)
```

1.  :man_raising_hand: Model currently defaults to `gpt-3.5-turbo`


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
         --output readmeai.md \
         --api openai \
         --model gpt-4-turbo \
         --badge-color A931EC \
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

See the [Configuration Options](../configuration/cli_options.md) documentation for detailed explanations of each option.

## Tips for Effective Usage

1. **Choose the right LLM**: Different LLMs may produce varying results. Experiment to find the best fit for your project.
2. **Adjust temperature**: Lower values (e.g., 0.1) produce more focused output, while higher values (e.g., 0.8) increase creativity.
3. **Use custom prompts**: For specialized projects, consider using custom prompts to guide the AI's output.
4. **Review and edit**: Always review the generated README and make necessary adjustments to ensure accuracy and relevance.

## Troubleshooting

If you encounter any issues:

1. Ensure you have the latest version of readme-ai installed.
2. Check your API credentials if using OpenAI or Google Gemini.
3. For Ollama, make sure the Ollama service is running locally.
4. Consult the [FAQ](https://github.com/eli64s/readme-ai/issues) or [open an issue](https://github.com/eli64s/readme-ai/issues) for additional support.
