# Basic Usage Examples

This page provides simple examples of using readme-ai with different LLM services and basic configurations.

## Generate README with OpenAI

```sh
readmeai --repository https://github.com/username/project \
         --api openai \
         --model gpt-3.5-turbo
```

## Generate README with Ollama

```sh
readmeai --repository https://github.com/username/project \
         --api ollama \
         --model mistral
```

## Generate README with Google Gemini

```sh
readmeai --repository https://github.com/username/project \
         --api gemini
```

## Generate README in Offline Mode

```sh
readmeai --repository https://github.com/username/project \
         --api offline
```

## Customize Badge Style and Color

```sh
readmeai --repository https://github.com/username/project \
         --api openai \
         --badge-style flat-square \
         --badge-color "#FF5733"
```

## Use Custom Project Logo

```sh
readmeai --repository https://github.com/username/project \
         --api openai \
         --image custom
```

When prompted, enter the path or URL to your custom logo image.

## Generate README with Emojis

```sh
readmeai --repository https://github.com/username/project \
         --api openai \
         --emojis
```

These examples demonstrate basic usage of readme-ai. For more advanced configurations and options, see the [Advanced Configurations](advanced-configurations.md) page.
