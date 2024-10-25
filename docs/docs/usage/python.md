---
title: Python
---

## Running the CLI

Let's explore how to run readme-ai using Python with different configurations and options. We'll start with the basic usage and then move on to more advanced options.

```sh
readmeai --repository https://github.com/username/repository --api openai
```

### Usage with Different LLM Providers

#### OpenAI
```sh
readmeai --api openai --model gpt-3.5-turbo --repository https://github.com/username/repository
```

#### Anthropic
```sh
readmeai --api anthropic --model claude-3-5-sonnet-20240620 --repository https://github.com/username/repository
```

#### Google Gemini
```sh
readmeai --api gemini --model gemini-1.5-flash --repository https://github.com/username/repository
```

#### Ollama
```sh
readmeai --api ollama --model llama2 --repository https://github.com/username/repository
```

### Advanced Usage

Customize the README generation with additional options:

```sh
readmeai --repository https://github.com/username/repository \
         --output custom-readme.md \
         --api openai \
         --model gpt-4 \
         --badge-color A931EC \
         --badge-style flat-square \
         --header-style compact \
         --toc-style fold \
         --temperature 0.9 \
         --tree-depth 2 \
         --image LLM \
         --emojis
```

## Running from Source

<details><summary>Click to expand instructions</summary>

1. **Clone the repository:**
```sh
git clone https://github.com/eli64s/readme-ai
```

2. **Navigate to the directory:**
```sh
cd readme-ai
```

3. **Install dependencies:**
```sh
pip install -r setup/requirements.txt
```

4. **Run the application:**
```sh
python -m readmeai.cli.main --repository https://github.com/username/repository
```

</details>

## Troubleshooting

1. **Permission Issues**
   - Use `sudo` for system-wide installation on Unix systems
   - Use a virtual environment to avoid permission issues
   - Ensure Python is properly added to your system's PATH

2. **Package Installation Problems**
   - Update pip: `python -m pip install --upgrade pip`
   - Try installing in a fresh virtual environment
   - Check Python version compatibility (3.9+ required)

3. **API Key Issues**
   - Verify API key is correctly set in environment variables
   - Check API key permissions and quotas
   - Ensure no leading/trailing whitespace in API key

4. **Execution Errors**
   - Check internet connectivity for API calls
   - Verify repository URL/path is accessible
   - Ensure sufficient disk space for output

For additional help:
- Check the [GitHub Issues](https://github.com/eli64s/readme-ai/issues)
- Visit the [Official Documentation](https://eli64s.github.io/readme-ai/)
- Start a [Discussion](https://github.com/eli64s/readme-ai/discussions)
