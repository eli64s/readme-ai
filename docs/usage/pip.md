---
hide:
  - title
---

<!--
<a href="https://pypi.org/project/readmeai">
	<img src="https://img.shields.io/pypi/v/readmeai?color=3775A9&logo=pypi&label=PyPI&labelColor=3775A9&logoColor=white" alt="pypi-version">
</a>
<a href="https://github.com/eli64s/readme-ai">
	<img src="https://img.shields.io/github/stars/eli64s/readme-ai?color=3775A9&label=GitHub%20Stars&labelColor=3775A9&logo=github&logoColor=white" alt="github-stars">
</a>
-->

After installation, you can run readme-ai with:

```sh
readmeai --api openai --repository https://github.com/eli64s/readme-ai
```

## Usage

### Setting Environment Variables

**OpenAI API Key**

Generate an OpenAI API key and set it as an environment variable:

```sh
export OPENAI_API_KEY=<your_api_key>
```

For Windows users, use:

```sh
set OPENAI_API_KEY=<your_api_key>
```

**Anthropic API Key**

To use the Anthropic API, set your API key:

```sh
export ANTHROPIC_API_KEY=<your_api_key>
```

### Running readme-ai

Run readme-ai with OpenAI:

```sh
readmeai --api openai --repository https://github.com/eli64s/readme-ai
```

Run readme-ai with Anthropic:

```sh
readmeai --api anthropic --repository https://github.com/eli64s/readme-ai
```

For a list of all available options, run:

```sh
readmeai --help
```

## Troubleshooting

1. **Permission Issues**: Ensure you have the necessary permissions to install Python packages. You may need to use `sudo` on Unix-based systems.
2. **Pipx Not Found**: Make sure `pipx` is properly installed and available in your PATH. You can find installation instructions [here](https://pipxproject.github.io/pipx/installation/).
3. **Missing Dependencies**: Some advanced features require additional Python packages. Check the [official documentation](https://github.com/eli64s/readme-ai) for a list of optional dependencies.

For further help, you can [open an issue](https://github.com/eli64s/readme-ai/issues) on GitHub or refer to the [official documentation](https://eli64s.github.io/readme-ai/).
