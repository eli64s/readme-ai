# 🚧 Language Model Integrations

*🚧 WIP*

Readme-ai integrates seamlessly with various Large Language Model (LLM) services to generate high-quality README content. This page provides an overview of the supported LLM services and links to detailed information about each.

## Supported LLM Services

1. [OpenAI](openai.md)
2. [Ollama](ollama.md)
3. [Anthropic](anthropic.md)
4. [Google Gemini](google_gemini.md)
5. [Offline Mode](offline_mode.md)

## Comparing LLM Services

| Service | Pros | Cons |
|---------|------|------|
| OpenAI  | High-quality output, Versatile | Requires API key, Costs associated |
| Ollama  | Free, Privacy-focused, Offline | May be slower, Requires local setup |
| Anthropic | Privacy-focused, Offline | May be slower, Requires local setup |
| Gemini  | Strong performance, Google integration | Requires API key |
| Offline | No internet required, Fast | Basic output, Limited customization |

---

<!-- ## Tips for Optimal Results

1. **Experiment with different models**: Try various LLM services and models to find the best fit for your project.
2. **Provide clear context**: Ensure your repository has well-organized code and documentation to help the LLM generate more accurate content.
3. **Fine-tune with CLI options**: Use readme-ai's CLI options to customize the output further after choosing your LLM service.
4. **Review and edit**: Always review the generated README and make necessary edits to ensure accuracy and relevance to your project.

By leveraging these LLM integrations effectively, you can generate comprehensive and accurate README files for your projects with minimal effort.
Here is a structured content tab implementation for integrating multiple APIs in README-AI, based on the detailed API integration information you provided:

---

## 🚀 API Integrations

README-AI supports multiple large language model (LLM) APIs for generating README files. The following tabs explain how to configure and use each supported API.

### API Configuration Tabs

<div class="grid" markdown>

=== "Anthropic"

        ```sh
        readmeai --api anthropic --model claude-3-opus-20240229 --repository <REPO_URL_OR_PATH>
        ```


=== "Gemini"

        ```sh
        readmeai --api gemini --model gemini-1.5-flash --repository <REPO_URL_OR_PATH>
        ```

=== "Ollama"

        ```sh
        readmeai --api ollama --model llama3 --repository <REPO_URL_OR_PATH>
        ```

=== "OpenAI"

        ```sh
        readmeai --api openai --model gpt-3.5-turbo --repository <REPO_URL_OR_PATH>
        ```

=== "OfflineMode"

        ```sh
        readmeai --api offline --repository <REPO_URL_OR_PATH>
        ```

```

</div> -->
