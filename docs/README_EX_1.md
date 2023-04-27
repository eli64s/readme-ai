<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
README-AI
</h1>
<h3 align="center">📍 Making your READMEs smarter, one commit at a time.</h3>
<h3 align="center">🚀 Developed with the software and tools below.</h3>
<p align="center">

<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white" alt="" />
<img src="https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="dacite" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="sample" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white" alt="flake8" />

<img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="idx" />
<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=for-the-badge&logo=Pytest&logoColor=white" alt="pandas" />
<img src="https://img.shields.io/badge/spaCy-09A3D5.svg?style=for-the-badge&logo=spaCy&logoColor=white" alt="colorlog" />
<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=for-the-badge&logo=GNU-Bash&logoColor=white" alt="json" />
</p>

</div>

---
## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍Overview](#overview)
- [🔮 Feautres](#-feautres)
- [⚙️ Project Structure](#️-project-structure)
- [💻 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
  - [✅ Prerequisites](#-prerequisites)
  - [💻 Installation](#-installation)
  - [🤖 Using README-AI](#-using-readme-ai)
  - [🧪 Running Tests](#-running-tests)
- [🛠 Future Development](#-future-development)
- [🤝 Contributing](#-contributing)
- [🪪 License](#-license)
- [🙏 Acknowledgments](#-acknowledgments)

---

## 📍Overview

README-AI is a project that aims to improve the quality of README files on GitHub. It does this by using machine learning to automatically generate high-quality READMEs for new projects,

## 🔮 Feautres

> `[📌  INSERT-PROJECT-FEATURES]`

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## ⚙️ Project Structure

```bash
.
├── CONTRIBUTING.md
├── LICENSE
├── Makefile
├── README.md
├── conf
│   ├── badges.json
│   ├── conf.toml
│   ├── file_extensions.toml
│   ├── file_names.toml
│   ├── setup_guide.toml
│   └── templates
│       └── general.toml
├── docs
│   ├── README_EX_1.md
│   ├── README_EX_2.md
│   ├── README_EX_3.md
│   ├── README_EX_4.md
│   ├── README_EX_JS.md
│   ├── README_EX_RUST.md
│   └── imgs
│       ├── docs.png
│       ├── header.png
│       ├── misc.png
│       ├── setup.png
│       ├── toc.png
│       └── tree.png
├── requirements.txt
├── scripts
│   ├── clean.sh
│   ├── run.sh
│   └── test.sh
├── setup
│   ├── environment.yaml
│   └── setup.sh
├── setup.py
├── src
│   ├── __init__.py
│   ├── builder.py
│   ├── conf.py
│   ├── file_factory.py
│   ├── logger.py
│   ├── main.py
│   ├── model.py
│   ├── preprocess.py
│   └── preprocess_helper.py
└── tests
    ├── conftest.py
    ├── test_builder.py
    ├── test_conf.py
    ├── test_file_factory.py
    ├── test_logger.py
    ├── test_main.py
    ├── test_model.py
    └── test_processor.py

9 directories, 46 files
```
---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 💻 Modules
<details closed><summary>Scripts</summary>

| File     | Summary                                                                                                                                            |
|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------|
| run.sh   | This code is a Bash script that activates a Conda environment and runs a Python script. It also allows for the exporting of environment variables. |
| clean.sh | This code is a Bash script that cleans up files and directories related to Python, Jupyter notebooks, pytest, benchmarks, and a CSV file.          |

</details>

<details closed><summary>Src</summary>

| File                 | Summary                                                                                                                                                                                                                                              |
|:---------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| preprocess.py        | This code provides methods to process a GitHub repository, such as cloning the repository to a temporary directory, getting the file contents, and getting the project dependencies.                                                                 |
| conf.py              | This code defines configuration constants for an application, including OpenAI API details, GitHub repository details, Markdown template strings, and project paths.                                                                                 |
| preprocess_helper.py | This code provides helper functions for dependency parsing for readme. ai. It includes functions for parsing Conda environment files, Pipfiles, pyproject. toml, requirements files, Cargo. toml, Cargo. lock, package. json, and yarn. lock.        |
| logger.py            | Logger is a class for the project that provides logging capabilities with colored output. It supports logging levels such as DEBUG, INFO, WARNING, ERROR, and CRITICAL.                                                                              |
| file_factory.py      | This File Factory module provides a class, FileHandler, which allows for the reading and writing of files in markdown, toml, and json formats.                                                                                                       |
| model.py             | This code uses the OpenAI GPT-3 model to generate summary text from code. It uses the OpenAI API to access the GPT-3 model, and the Spacy library to summarize the generated text.                                                                   |
| builder.py           | This code builds a README. md file from a template and data, such as a pandas DataFrame, a configuration object, and a list of dependencies.                                                                                                         |
| main.py              | README-AI is a tool that generates a README. md file for your repository using OpenAI's API. It takes in a repository URL or local directory path, and outputs a README. md file with a summary of the codebase, project dependencies, and a slogan. |

</details>
<hr />

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> `[📌  INSERT-PROJECT-PREREQUISITES]`

### 💻 Installation

1. Clone the README-AI repository:
```sh
git clone https://github.com/eli64s/README-AI
```

2. Change to the project directory:
```sh
cd README-AI
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

### 🤖 Using README-AI

```sh
python main.py
```

### 🧪 Running Tests
```sh
#run tests
```

<hr />

## 🛠 Future Development
- [X] [📌  COMPLETED-TASK]
- [ ] [📌  INSERT-TASK]
- [ ] [📌  INSERT-TASK]


---

## 🤝 Contributing
Contributions are always welcome! Please follow these steps:
1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).
```sh
git checkout -b new-feature-branch
```
4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub using the following command
```sh
git push origin new-feature-branch
```
7. Create a pull request to the original repository.
Open a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary. 
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 🪪 License

This project is licensed under the `[📌  INSERT-LICENSE-TYPE]` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 🙏 Acknowledgments

[📌  INSERT-DESCRIPTION]


---

