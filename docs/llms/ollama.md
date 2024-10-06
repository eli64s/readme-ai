# Ollama

Ollama is a privacy-focused, open-source tool for running open-source LLMs locally such as `Llama 3`, `Mistral`, and `Gemma 2`. Ollama can be used with readme-ai to generate README files with a variety of models and configurations from their [model library](https://github.com/ollama/ollama?tab=readme-ov-file#model-library).

## Usage

Start by downloading [Ollama](https://ollama.com/download), and then pull a model such as Llama 3 or Mistral.

```sh
ollama pull llama3
```

Once you have the model, run the ollama server.

```sh
ollama run llama3
```

Then, you can use the `readmeai` CLI to generate README files using the Ollama API.

```sh
readmeai --api ollama --model llama3 -r https//github.com/username/project
```

???+ note

    - Slower README generation times may be experienced when using Ollama compared to cloud-based services.
