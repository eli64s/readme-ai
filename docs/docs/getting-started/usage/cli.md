---
title: Command Line Interface (CLI)
---

# Command Line Interface

The readme-ai CLI supports multiple ways to generate documentation, from cloud LLM providers to local models. Choose your preferred method below.

## Cloud LLM Providers

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

=== "![anthropic][anthropic-svg]{ width="12px" height="12px" }&emsp13;Anthropic"

    Use Anthropic's Claude models:

    ```sh
    readmeai \
        --api anthropic \
        --model claude-3-5-sonnet-20240620 \
        --output readmeai-anthropic.md \
        --repository https://github.com/eli64s/readme-ai
    ```

=== "![gemini][gemini-svg]{ width="12px" height="12px" }&emsp13;Google Gemini"

    Generate with Google's Gemini models:

    ```sh
    readmeai \
        --api gemini \
        --model gemini-1.5-flash \
        --output readmeai-gemini.md \
        --repository https://github.com/eli64s/readme-ai
    ```

## Local Options

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

## Advanced Usage

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

## Command Options

For a complete list of available options, use the `--help` flag:

```sh
readmeai --help
```

You should see output similar to the following:

```console
Usage: readmeai [OPTIONS]

  Entry point for the readme-ai CLI application.

Options:
  -V, --version                   Show the version and exit.
  -a, --align [center|left|right]
                                  align for the README.md file header
                                  sections.
  --api [anthropic|gemini|ollama|openai|offline]
                                  LLM API service provider to power the README
                                  file generation.
  -bc, --badge-color TEXT         Primary color (hex code or name) to use for
                                  the badge icons.
  -bs, --badge-style [default|flat|flat-square|for-the-badge|plastic|skills|skills-light|social]
                                  Visual style of the badge icons used in the
                                  README file.
  --base-url TEXT                 Base URL for the LLM API service.
  -cw, --context-window INTEGER   Maximum number of tokens to use for the
                                  model's context window.
  -e, --emojis [default|minimal|ascension|fibonacci|harmony|prism|quantum|monochrome|unicode|atomic|cosmic|crystal|earth|fire|forest|nature|water|gradient|rainbow|solar|fun|vintage|zen|random]
                                  Emoji theme 'packs' for customizing header
                                  section titles.
  -hs, --header-style [ASCII|ASCII_BOX|BANNER|CLASSIC|CLEAN|COMPACT|CONSOLE|MODERN]
                                  README header style template options.
  -l, --logo [ANIMATED|BLACK|BLUE|GRADIENT|ORANGE|METALLIC|PURPLE|RAINBOW|TERMINAL|CUSTOM|LLM]
                                  Project logo for the README file.
  -ls, --logo-size TEXT           Project logo size.
  -m, --model TEXT                LLM API model to power the README file
                                  generation.
  -ns, --navigation-style [ACCORDION|BULLET|NUMBER|ROMAN]
                                  Navigation menu styles for the README table
                                  of contents.
  -o, --output TEXT               Output file path for the generated README
                                  file.
  -rl, --rate-limit INTEGER RANGE
                                  Number of requests per minute for the LLM
                                  API service.  [1<=x<=25]
  -r, --repository TEXT           Provide a repository URL (GitHub, GitLab,
                                  BitBucket) or local path.  [required]
  -sm, --system-message TEXT      System message to display in the README
                                  file.
  -t, --temperature FLOAT RANGE   Increasing temperature yields more
                                  randomness in text generation.  [x<=2.0]
  --top-p FLOAT RANGE             Top-p sampling probability for the model's
                                  generation.  [0.0<=x<=1.0]
  -td, --tree-max-depth INTEGER   Maximum depth of the directory tree
                                  generated for the README file.
  --help                          Show this message and exit.
```

See the [CLI Reference](../cli-reference.md) for the full list of options and their descriptions.

<!--
## Troubleshooting

1. **Permission Issues**
   - Use `sudo` for system-wide installation on Unix systems
   - Use a virtual environment to avoid permission issues
   - Ensure Python is properly added to your system's PATH

2. **Package Installation Problems**
   - Update pip: `python -m pip install --upgrade pip`
   - Try installing in a fresh virtual environment
   - Check Python version compatibility (3.9+ required)

3. **API Key Issues**
   - Verify API key is correctly set in environment variables
   - Check API key permissions and quotas
   - Ensure no leading/trailing whitespace in API key

4. **Execution Errors**
   - Check internet connectivity for API calls
   - Verify repository URL/path is accessible
   - Ensure sufficient disk space for output

For additional help:
- Check the [GitHub Issues](https://github.com/eli64s/readme-ai/issues)
- Visit the [Official Documentation](https://eli64s.github.io/readme-ai/)
- Start a [Discussion](https://github.com/eli64s/readme-ai/discussions)
-->

---

<!-- REFERENCE LINKS -->
<!--
[anthropic-svg]: https://simpleicons.org/icons/anthropic.svg
[bash-svg]: https://simpleicons.org/icons/bash.svg
[docker-svg]: https://simpleicons.org/icons/docker.svg
[gemini-svg]: https://simpleicons.org/icons/googlegemini.svg
[git-svg]: https://simpleicons.org/icons/git.svg
[markdown-svg]: https://simpleicons.org/icons/markdown.svg
[ollama-svg]: https://simpleicons.org/icons/ollama.svg
[openai-svg]: https://simpleicons.org/icons/openai.svg
[poetry-svg]: https://simpleicons.org/icons/poetry.svg
[streamlit-svg]: https://simpleicons.org/icons/streamlit.svg
-->

<!-- ICONS (https://simpleicons.org/) -->
--8<-- "references.md:simple-icons"
