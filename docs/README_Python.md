
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
README-AI
</h1>
<h3 align="center">📍 See the Future of README Writing with README-AI!</h3>
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
<img src="https://img.shields.io/badge/precommit-FAB040.svg?style=for-the-badge&logo=pre-commit&logoColor=black" alt="spacy" />
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

README-AI is a machine learning project that generates template-based README files for GitHub repositories. It automates the process of creating a README and reduces the time needed to write a README.

## 🔮 Feautres

> `[📌  INSERT-PROJECT-FEATURES]`

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## ⚙️ Project Structure


```bash
repo
├── CONTRIBUTING.md
├── Dockerfile
├── LICENSE
├── Makefile
├── README.md
├── conf
│   ├── badges.json
│   ├── conf.toml
│   ├── file_extensions.toml
│   ├── file_names.toml
│   ├── ignore_files.toml
│   └── setup_guide.toml
├── docs
│   ├── README_EX_1.md
│   ├── README_EX_2.md
│   ├── README_EX_3.md
│   ├── README_EX_3_FastAPI.md
│   ├── README_EX_4_PY.md
│   ├── README_EX_5_GO.md
│   ├── README_EX_6_JAVA.md
│   ├── README_EX_GO.md
│   ├── README_EX_JS.md
│   ├── README_EX_RUST.md
│   ├── README_EX_RUST_GITLAB.md
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
│   ├── preprocess_helper.py
│   └── utils.py
└── tests
    ├── __init__.py
    ├── conftest.py
    ├── test_builder.py
    ├── test_conf.py
    ├── test_file_factory.py
    ├── test_logger.py
    ├── test_main.py
    ├── test_model.py
    ├── test_preprocess.py
    ├── test_preprocess_helper.py
    └── test_utils.py

8 directories, 56 files
```

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 💻 Modules

<details closed><summary>Scripts</summary>

| File     | Summary                                                                                                                                                                                                                    | Module           |
|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| run.sh   | This code is a Bash script that activates a Conda environment and runs a Python script. It also allows for the exporting of environment variables.                                                                         | scripts/run.sh   |
| clean.sh | This bash script removes unwanted files and directories, such as backup files, Python cache files and directories, build artifacts, Jupyter notebook checkpoints, pytest cache, benchmarks, raw data files, and log files. | scripts/clean.sh |
| test.sh  | This code is a Bash script that activates a conda environment, sets the directories to include and exclude in a coverage report, generates the coverage report and saves it to a file, and then removes files and folders. | scripts/test.sh  |

</details>

<details closed><summary>Src</summary>

| File                 | Summary                                                                                                                                                                                                                                                                                                             | Module                   |
|:---------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------|
| preprocess.py        | This code handles preprocessing of the input codebase, including cloning or copying a repository from a URL or local path, getting the contents of all the files, and getting the dependencies of a project.                                                                                                        | src/preprocess.py        |
| conf.py              | This code provides configuration constants for an application, including OpenAI, Git, Markdown, and Paths. It also includes a helper function to read configuration files and update the helper configurations.                                                                                                     | src/conf.py              |
| preprocess_helper.py | This code provides helper functions for dependency parsing for README-AI. It includes functions for parsing files in Python, Rust, Javascript, and Java, such as Conda environment files, Pipfiles, Pyproject TOML files, Cargo TOML files, Cargo lock files, package.json files, Yarn lock files, Go module files | src/preprocess_helper.py |
| logger.py            | This code is a custom logger module using loguru for README-AI. It provides functions for logging messages at different levels, such as info, debug, warning, error, critical, trace, success, and exception. It also allows for custom logging levels.                                                            | src/logger.py            |
| file_factory.py      | This module provides a FileHandler class for reading and writing different file types, such as Markdown, TOML, and JSON. It includes methods for reading and writing files, as well as a cache for storing file contents.                                                                                           | src/file_factory.py      |
| model.py             | This code is an OpenAI API handler for generating text for the README.md file. It uses connection pooling to make requests to the OpenAI API, and uses Spacy's NLP pipeline to process the generated text. It also includes a custom exception class for OpenAI errors.                                             | src/model.py             |
| builder.py           | This code builds a README.md file for a codebase using a configuration Markdown template, OpenAI API language models, and project dependencies. It parses project files, generates badge icons, creates a setup guide, and creates a directory tree structure for the README.md file.                               | src/builder.py           |
| utils.py             | This code provides utility methods for a project, including a function to reformat a sentence by removing extra white space and a function to check if a given string is a valid URL.                                                                                                                               | src/utils.py             |
| main.py              | This code automates the generation of a README.md file for a codebase using OpenAI's API. It takes in an API key, local codebase directory, output path, and remote GitHub repository as arguments, and generates a summary of the codebase using OpenAI's API.                                                     | src/main.py              |

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
