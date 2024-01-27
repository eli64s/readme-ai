## LLM API Key

Before running the application, ensure you have an OpenAI API key and its set as an environment variable.

On `Linux` or `MacOS`
```console
$ export OPENAI_API_KEY=YOUR_API_KEY
```

On `Windows`
```console
$ set OPENAI_API_KEY=YOUR_API_KEY
```

---

## Command Line Interface

Use one of the methods below to run the application (Pip, Docker, Conda, Streamlit, etc).

### PyPI

```sh
readmeai --repository https://github.com/eli64s/readme-ai
```

### Docker

```sh
docker run -it \
-e OPENAI_API_KEY=$OPENAI_API_KEY \
-v "$(pwd)":/app zeroxeli/readme-ai:latest \
-r https://github.com/eli64s/readme-ai
```

### Conda

```sh
readmeai -r https://github.com/eli64s/readme-ai
```

### From Source

Alternatively, clone the repository and run the application from source.

Using `pipenv`
```sh
pipenv shell && \
python3 -m readmeai.cli.commands -o readme-ai.md -r https://github.com/eli64s/readme-ai
```

Using `poetry`
```sh
poetry shell && \
poetry run python3 -m readmeai.cli.commands -o readme-ai.md -r https://github.com/eli64s/readme-ai
```

---

## Web Application

### Streamlit

Use readme-ai directly in your browser via <a href="https://streamlit.io/">Streamlit Community Cloud</a>, no installation required!

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://readme-ai.streamlit.app/)

<sub>
    Web app may be unavailable at times as its hosted for free. See the <a href="https://github.com/eli64s/readme-ai-streamlit">readme-ai-streamlit</a> repository for more details.
</sub>

---

## Testing

Use [`pytest`](https://docs.pytest.org/en/7.1.x/contents.html) to run the default test suite.
```sh
make test
```

Use [`nox`](https://nox.thea.codes/en/stable/) to run the test suite against multiple Python versions including `(3.9, 3.10, 3.11, 3.12)`.
```sh
nox -f noxfile.py
```

---
