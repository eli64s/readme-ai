<!--
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
``` -->
