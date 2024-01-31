### ► Running `readme-ai`

Ensure your LLM API key is set as an environment variable.

`Linux / macOS:`
```console
$ export OPENAI_API_KEY=<your_api_key>
```

`Windows`
```console
$ set OPENAI_API_KEY=<your_api_key>
```

#### Using `pip`
[![pip](https://img.shields.io/badge/PyPI-3775A9.svg?style=flat&logo=PyPI&logoColor=white)](https://pypi.org/project/readmeai/)

```sh
readmeai --repository https://github.com/eli64s/readme-ai
```

#### Using `docker`
[![docker](https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white)](https://hub.docker.com/r/zeroxeli/readme-ai)

```sh
docker run -it \
-e OPENAI_API_KEY=$OPENAI_API_KEY \
-v "$(pwd)":/app zeroxeli/readme-ai:latest \
-r https://github.com/eli64s/readme-ai
```

#### Using `streamlit`

* [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://readme-ai.streamlit.app/)

Use the app directly in your browser on <a href="https://streamlit.io/">Streamlit</a>, no installation required! More details about the web app can be found <a href="https://github.com/eli64s/readme-ai-streamlit">here.</a>

<details closed>
<summary>
  <h4>From <code>source</code></h4>
</summary>

#### Using `bash`

[![bash](https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat&logo=GNU-Bash&logoColor=white)](https://www.gnu.org/software/bash/)

```console
$ conda activate readmeai
$ python3 -m readmeai.cli.commands -r https://github.com/eli64s/readme-ai
```

#### Using `poetry`
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)

```console
$ poetry shell
$ python3 -m readmeai.cli.commands -r https://github.com/eli64s/readme-ai
```

</details>

---

### 🧪 Tests

#### Using `pytest`
[![pytest](https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat&logo=Pytest&logoColor=white)](https://docs.pytest.org/en/7.1.x/contents.html)
```console
$ make pytest
```

#### Using `nox`
```console
$ nox -f noxfile.py
```

<sub>Use [nox](https://nox.thea.codes/en/stable/) to test application against multiple Python environments and dependencies!</sub>

---
