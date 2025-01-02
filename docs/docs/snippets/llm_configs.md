<!-- --8<------ [start:openai] -->
```yaml
openai:
  provider: openai
  models:
    default: gpt-3.5-turbo
    available:
      - gpt-3.5-turbo
      - gpt-4
      - gpt-4-turbo-preview
  parameters:
    temperature: 0.7
    top_p: 1.0
    max_tokens: 4096
    timeout: 30
```
<!-- --8<------ [end:openai] -->

<!-- --8<------ [start:anthropic] -->
```yaml
anthropic:
  provider: anthropic
  models:
    default: claude-3-sonnet
    available:
      - claude-3-opus
      - claude-3-sonnet
      - claude-3-haiku
  parameters:
    temperature: 0.7
    top_p: 1.0
    max_tokens: 4096
    timeout: 30
```
<!-- --8<------ [end:anthropic] -->

<!-- --8<------ [start:gemini] -->
```yaml
gemini:
  provider: google
  models:
    default: gemini-1.0-pro
    available:
      - gemini-1.0-pro
      - gemini-1.5-pro
  parameters:
    temperature: 0.7
    top_p: 1.0
    max_tokens: 2048
    timeout: 30
```
<!-- --8<------ [end:gemini] -->

<!-- --8<------ [start:ollama] -->
```yaml
ollama:
  provider: ollama
  models:
    default: llama2
    available:
      - mistral
      - llama2
      - codellama
  parameters:
    temperature: 0.7
    top_p: 1.0
    max_tokens: 4096
    timeout: 30
```
<!-- --8<------ [end:ollama] -->
