<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100">
<p>PydocsAI</p></h1><b>Automate README Markdown creation and codebase documentation for your projects!</b><br><br>

![OpenAI](https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Anaconda](https://img.shields.io/badge/Anaconda-44A833.svg?style=for-the-badge&logo=Anaconda&logoColor=white)
![Bash](https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=for-the-badge&logo=GNU-Bash&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26.svg?style=for-the-badge&logo=HTML5&logoColor=white)
![GitHub](https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white)

</div>

---

## Overview

PydocsAI is a Python package that provides an automated way to generate a README.md file and documentation for a codebase. This package leverages OpenAI's GPT Davinci model to translate the codebase into documentation, and then generates a structured output Markdown template that contains the project documentation. PydocsAI also generates automated header badge icons related to your project dependencies and creates a repository file directory tree.

The project is still under development and is very opinionated in its setup, but it can be used as a starting point for projects that require documentation. The current version of PyDocsAI is limited to codebases written in Python.
## Use-Case

Software, data, machine learning, or any project that requires documentation!

## Feautres

### Badges

Analyzes your project repository to create a list of software and packages used, displayed as badges in the README header section.

<div><details closed><summary>Example - Badges</a></summary>

![header](docs/gpt/head.png)

</detais></div>

### Code Summary

This project leverages the base GPT Davinci model from OpenAI to translate a repository of Python code to documentaion.

<div><details closed><summary>Example - Docoumentation</a></summary>

![body](docs/gpt/body.png)</detais>

</div>

### Repository Tree

Creates a directory tree to display in your readme.

<div><details closed><summary>Example - Tree</a></summary>

![body](docs/gpt/tree.png)</detais>

</div>

### README Generation

See this [Sample Markdown](docs/markdown/readme.md) for the README.md file generated running this script on this repository.

---

## Getting Started

### GitHub Repository

Copy the url of your project's GitHub repository and update the code below from `conf/conf.toml` below.

```bash
# GitHub
[github]
url = "https://github.com/eli64s/PydocsAI"
```

### OpenAI API Key

<details closed>
<summary><a href="https://platform.openai.com/docs/introduction">OpenAI API Setup</a></summary>

Here are the steps to create an OpenAI API key:

1. Go to the OpenAI website.
2. Click the "Sign up for free" button.
3. Fill out the registration form with your information and agree to the terms of service.
4. Once logged in, click on the "API" tab.
5. Follow the instructions to create a new API key.
6. Copy the API key and keep it in a secure place.

You can now use the OpenAI API key to integrate with OpenAI's language models in your projects.
</details>

Copy your your OpenAI API key and update the code below from `scripts/run_main.sh` below.

```bash
#!/bin/bash
set +x

export OPENAI_API_KEY="<OPENAI-API-KEY>"

```

---

### Usage

```Bash
# 1. Clone GitHub repository.
git clone https://github.com/eli64s/PydocsAI && cd PydocsAI

# 2. Setup conda virtual environment.
make conda

# 3. Run the model.
bash scripts/run_model.sh
```

---

## Contribute

Contributions and suggestions welcome!

---

## Roadmap

- Add compatability for additional file types.
- Extend capabilities beyond codebase documentation

---

## References

- [Profile Badges - Aveek-Saha/GitHub-Profile-Badges](https://github.com/Aveek-Saha/GitHub-Profile-Badges)
- [Automated Docstrings - cdesarmeaux/autodocstrings](https://github.com/cdesarmeaux/autodocstrings)

---
