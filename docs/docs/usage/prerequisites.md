# Prerequisites

### System Requirements

- **Python**: `3.9+`
- **Package Manager/Container**: `pip`, `pipx`, `uv`, or `docker`.

### Supported Sources

The following git hosting services are supported for source code retrieval, along with your local file system:

- [**GitHub**](https://github.com/)
- [**GitLab**](https://gitlab.com/)
- [**Bitbucket**](https://bitbucket.org/)
- [**File System**](https://en.wikipedia.org/wiki/File_system)

<sub>If your Git provider is not listed, open an [issue](https://github.com/eli64s/readme-ai/issues) or submit a [pull request](https://github.com/eli64s/readme-ai/pulls) to add support for additional platforms.</sub>

### Supported LLM APIs

To enable the full functionality of `readmeai`, an account and API key are required for one of the following providers:

- [**OpenAI**](https://platform.openai.com/docs/quickstart/account-setup): Recommended for general use. Requires an OpenAI account and API key.
- [**Ollama**](https://github.com/ollama/ollama): Free and open-source. No API key required.
- [**Anthropic**](https://www.anthropic.com/): Requires an Anthropic account and API key.
- [**Google Gemini**](https://ai.google.dev/tutorials/python_quickstart): Requires a Google Cloud account and API key.
- [**Offline Mode**](https://github.com/eli64s/readme-ai/blob/main/examples/offline-mode/readme-ai.md): Generates a boilerplate README without making API calls.

<sub>For more information on setting up an API key, refer to the provider's documentation.</sub>
