# LLM Configuration Snippets

This file contains reusable LLM configuration snippets for MkDocs documentation.

<!-- --8<-- [start:openai] -->
## OpenAI Configuration

Example configuration for OpenAI models:

```bash
readmeai -r https://github.com/eli64s/readme-ai \
  --api openai \
  --model gpt-4o-mini \
  --temperature 0.7
```
<!-- --8<-- [end:openai] -->

<!-- --8<-- [start:anthropic] -->
## Anthropic Configuration

Example configuration for Anthropic models:

```bash
readmeai -r https://github.com/eli64s/readme-ai \
  --api anthropic \
  --model claude-3-haiku-20240307 \
  --temperature 0.7
```
<!-- --8<-- [end:anthropic] -->

<!-- --8<-- [start:gemini] -->
## Google Gemini Configuration

Example configuration for Google Gemini models:

```bash
readmeai -r https://github.com/eli64s/readme-ai \
  --api gemini \
  --model gemini-1.5-flash \
  --temperature 0.7
```
<!-- --8<-- [end:gemini] -->

<!-- --8<-- [start:ollama] -->
## Ollama Configuration

Example configuration for Ollama models:

```bash
readmeai -r https://github.com/eli64s/readme-ai \
  --api ollama \
  --model llama3.2 \
  --temperature 0.7
```
<!-- --8<-- [end:ollama] -->
