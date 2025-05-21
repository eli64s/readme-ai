<!-- --8<------ [start:cloud-openai] -->
=== "![openai][openai-svg]{ width="12px" height="12px" }&emsp13;OpenAI"

    Generate documentation using OpenAI's models:

    ```sh
    readmeai \
        --api openai \
        --output readmeai-openai.md \
        --repository https://github.com/eli64s/readme-ai
    ```

    !!! info "Default Model"
        The default model is `gpt-3.5-turbo`, offering the best balance between cost and performance. When using any model from the `gpt-4` series and up, please monitor your costs and usage to avoid unexpected charges.
<!-- --8<------ [end:cloud-openai] -->

<!-- --8<------ [start:cloud-anthropic] -->
=== "![anthropic][anthropic-svg]{ width="12px" height="12px" }&emsp13;Anthropic"

    Use Anthropic's Claude models:

    ```sh
    readmeai \
        --api anthropic \
        --model claude-3-5-sonnet-20240620 \
        --output readmeai-anthropic.md \
        --repository https://github.com/eli64s/readme-ai
    ```
<!-- --8<------ [end:cloud-anthropic] -->

<!-- --8<------ [start:cloud-gemini] -->
=== "![gemini][gemini-svg]{ width="12px" height="12px" }&emsp13;Google Gemini"

    Generate with Google's Gemini models:

    ```sh
    readmeai \
        --api gemini \
        --model gemini-1.5-flash \
        --output readmeai-gemini.md \
        --repository https://github.com/eli64s/readme-ai
    ```
<!-- --8<------ [end:cloud-gemini] -->

<!-- --8<------ [start:local-options] -->
=== "![ollama][ollama-svg]{ width="12px" height="12px" }&emsp13;Ollama"

    Use locally hosted models with Ollama:

    ```sh
    readmeai \
        --api ollama \
        --model llama3.2 \
        --repository https://github.com/eli64s/readme-ai
    ```

=== "![git][git-svg]{ width="12px" height="12px" }&emsp13;Local Repository"

    Generate documentation for a local codebase:

    ```sh
    readmeai \
        --api openai \
        --repository /users/username/projects/myproject
    ```

=== "![markdown][markdown-svg]{ width="12px" height="12px" }&emsp13;Offline Mode"

    Generate without using any LLM services:

    ```sh
    readmeai \
        --api offline \
        --output readmeai-offline.md \
        --repository https://github.com/eli64s/readme-ai
    ```
<!-- --8<------ [end:local-options] -->

<!-- --8<------ [start:advanced] -->
=== "Customization"

    ```sh
    readmeai \
        --repository https://github.com/eli64s/readme-ai \
        --output readmeai.md \
        --api openai \
        --model gpt-4 \
        --badge-color A931EC \
        --badge-style flat-square \
        --header-style compact \
        --navigation-style fold \
        --temperature 0.9 \
        --tree-depth 2 \
        --logo LLM \
        --emojis solar
    ```
<!-- --8<------ [end:advanced] -->
