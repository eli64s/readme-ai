**Requirements**

* Python: 3.9+
* Package manager or container runtime: `pip` or `docker` recommended.
* OpenAI API account and API key (other providers coming soon)

**Repository**

A repository URL or local path to your codebase is required run readme-ai. The following are supported:

- [GitHub](https://github.com/)
- [GitLab](https://gitlab.com/)
- [Bitbucket](https://bitbucket.org/)
- [File System](https://en.wikipedia.org/wiki/File_system)

**OpenAI API Key**

An OpenAI API account and API key are needed to use *readme-ai*. The following steps outline the process.

<details closed>
  <summary>🔐 OpenAI API Account Setup</summary>
  <ol>
    <li>Go to the <a href="https://platform.openai.com/">OpenAI website</a>.</li>
    <li>Click the "Sign up for free" button.</li>
    <li>Fill out the registration form with your information and agree to the terms of service.</li>
    <li>Once logged in, click on the "API" tab.</li>
    <li>Follow the instructions to create a new API key.</li>
    <li>Copy the API key and keep it in a secure place.</li>
  </ol>
</details>


---

### Running *README-AI*

Before running the application, ensure you have an OpenAI API key and its set as an environment variable.

On `Linux` or `MacOS`
```console
$ export OPENAI_API_KEY=YOUR_API_KEY
```

On `Windows`
```console
$ set OPENAI_API_KEY=YOUR_API_KEY
```

Use one of the methods below to run the application (Pip, Docker, Conda, Streamlit, etc).

Using `pip`
```sh
readmeai --repository https://github.com/eli64s/readme-ai
```

Using `docker`

```sh
docker run -it \
-e OPENAI_API_KEY=$OPENAI_API_KEY \
-v "$(pwd)":/app zeroxeli/readme-ai:latest \
-r https://github.com/eli64s/readme-ai
```

Using `conda`
```sh
readmeai -r https://github.com/eli64s/readme-ai
```

Using `streamlit`

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://readmeai.streamlit.app/)

> [!NOTE]
>
> The web app is hosted on <a href="https://streamlit.io/">Streamlit Community Cloud</a>, a free service for sharing Streamlit apps. Thus, the app may be unstable or unavailable at times. See the <a href="https://github.com/eli64s/readme-ai-streamlit">readme-ai-streamlit</a> repository for more details.

<details closed><summary>Alternatively, run the application locally from the cloned repository.</summary><br>

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

</details>

---

### Tests

Use [`pytest`](https://docs.pytest.org/en/7.1.x/contents.html) to run the default test suite.
```sh
make test
```

Use [`nox`](https://nox.thea.codes/en/stable/) to run the test suite against multiple Python versions including `(3.9, 3.10, 3.11, 3.12)`.
```sh
nox -f noxfile.py
```

---
