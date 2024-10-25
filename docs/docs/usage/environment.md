# Environment Variables

Once you have installed `readmeai`, set up the required environment variables for the API key of your chosen language model provider. The following examples demonstrate how to set the environment variables for each provider supported by readme-ai:

## Setting API Keys

### <img width="2%" src="https://raw.githubusercontent.com/eli64s/readme-ai/ece59f6f523c8c0d831cee76f695632858091ca5/docs/assets/icons/openai.svg">&emsp13;OpenAI

```sh
export OPENAI_API_KEY=<your_api_key>
```

### <img width="2%" src="https://raw.githubusercontent.com/eli64s/readme-ai/ece59f6f523c8c0d831cee76f695632858091ca5/docs/assets/icons/anthropic.svg">&emsp13;Anthropic

```sh
export ANTHROPIC_API_KEY=<your_api_key>
```

### <img width="2%" src="https://raw.githubusercontent.com/eli64s/readme-ai/ece59f6f523c8c0d831cee76f695632858091ca5/docs/assets/icons/googlegemini.svg">&emsp13;Google Gemini

```sh
export GOOGLE_API_KEY=<your_api_key>
```

!!! info "Window Users"
	On Windows, use `set` instead of `export` to set environment variables.

	```cmd
	set OPENAI_API_KEY=<your_api_key>
	```

### <img width="2%" src="https://raw.githubusercontent.com/eli64s/readme-ai/ece59f6f523c8c0d831cee76f695632858091ca5/docs/assets/icons/ollama.svg">&emsp13;Ollama

**1. Pull your preferred language model from the Ollama server.**
    ```sh
    ollama pull <model_name>:<model_version>
    ```
    For example, to pull the `mistral` model:
    ```sh
    ollama pull mistral:latest
    ```
**2. Set the `OLLAMA_HOST` environment variable and start the Ollama server.**
    ```sh
    export OLLAMA_HOST=127.0.0.1 && ollama serve
    ```

!!! note "Unsupported Language Models"
    If your preferred LLM API is not supported, open an [issue](https://github.com/eli64s/readme-ai/issues) or submit a [pull request](https://github.com/eli64s/readme-ai/pulls) and we'll review the request!
