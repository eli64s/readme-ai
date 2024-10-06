# CLI Reference

README-AI offers a wide range of configuration options to customize your README generation. This page provides a comprehensive list of all available options with detailed explanations.

## CLI Options

| Option | Description | Default | Impact |
|--------|-------------|---------|--------|
| `--align` | Text alignment in header | `center` | Affects the visual layout of the README header |
| `--api` | LLM API service | `offline` | Determines which AI service is used for content generation |
| `--badge-color` | Badge color (name or hex) | `0080ff` | Customizes the color of status badges in the README |
| `--badge-style` | Badge icon style type | `flat` | Changes the visual style of status badges |
| `--base-url` | Base URL for the repository | `v1/chat/completions` | Used for API requests to the chosen LLM service |
| `--context-window` | Max context window of LLM API | `3999` | Limits the amount of context provided to the LLM |
| `--emojis` | Add emojis to README sections | `False` | Adds visual flair to section headers |
| `--header-style` | Header template style | `classic` | Changes the overall look of the README header |
| `--image` | Project logo image | `blue` | Sets the main image displayed in the README |
| `--model` | Specific LLM model to use | `gpt-3.5-turbo` | Chooses the AI model for content generation |
| `--output` | Output filename | `readme-ai.md` | Specifies the name of the generated README file |
| `--rate-limit` | Max API requests per minute | `5` | Prevents exceeding API rate limits |
| `--repository` | Repository URL or local path | `None` | Specifies the project to analyze |
| `--temperature` | Creativity level for generation | `0.9` | Controls the randomness of the AI's output |
| `--toc-style` | Table of contents style | `bullet` | Changes the format of the table of contents |
| `--top-p` | Top-p sampling probability | `0.9` | Fine-tunes the AI's output diversity |
| `--tree-depth` | Max depth of directory tree | `2` | Controls the detail level of the project structure |

## CLI Usage Examples

### Using OpenAI

```sh
readmeai --api openai --model gpt-3.5-turbo --repository https://github.com/username/project \
```

### Using Ollama

```sh
ollama run llama3
```

```sh
readmeai --api ollama --model llama3 --repository https://github.com/username/project \
```

### Generate README with Google Gemini

```sh
readmeai --repository https://github.com/username/project \
        --api gemini \
        --model gemini-1.5-flash
```

### Generate README in Offline Mode

```sh
readmeai --repository https://github.com/username/project \
        --api offline
```

### Customize Badge Style and Color

```sh
readmeai --repository https://github.com/username/project \
        --api openai \
        --badge-style flat-square \
        --badge-color FF5733
```

### Use Custom Project Logo

```sh
readmeai --repository https://github.com/username/project \
        --api openai \
        --image custom
```

When prompted, enter the path or URL to your custom logo image.

### Generate README with Emojis

```sh
readmeai --repository https://github.com/username/project \
        --api openai \
        --emojis
```

These examples demonstrate basic usage of readme-ai. Lets take a look at some more advanced configurations and options next.

## Advanced Configurations

The following examples demonstrate advanced configurations and options for generating a README using readme-ai.

### Generate README with Custom OpenAI API Parameters

```sh
readmeai --repository /path/to/project \
        --api openai \
        --model gpt-4-turbo
        --context-window 9999
        --temperature 0.1
        --rate-limit 20
```

### Generate README with Specific Directory Depth

```sh
readmeai --repository /path/to/project \
        --api openai \
        --tree-depth 3
```

### Generate README with LLM API Parameters

```sh
readmeai --repository /path/to/project \
        --api openai \
        --model gpt-4-turbo
        --context-window 4999
        --temperature 0.7
        --top-p 0.8
```

### Generate README with Custom Table of Contents Style

```sh
readmeai --repository /path/to/project \
        --api openai \
        --toc-style fold
```
