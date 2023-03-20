
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
README-AI
</h1>

> <h3 align="center">
>
> `[📌  INSERT-PROJECT-SUMMARY]`
>
> </h3>
> <h3 align="center">🚀 Developed using OpenAI's language model API and the software tools below.</h3>
> <p align="center">
> 
> ![openai](https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white)
> ![pandas](https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
> ![py](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)
> ![pytest](https://img.shields.io/badge/Pytest-0A9EDC.svg?style=for-the-badge&logo=Pytest&logoColor=white)
> ![sh](https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=for-the-badge&logo=GNU-Bash&logoColor=white)
> ![json](https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white)
> ![markdown](https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white)
> </p>

</div>


---

## 📦 Table of Contents


- [📦 Table of Contents](#-table-of-contents)
- [👋 Introduction](#-introduction)
- [🔮 Feautres](#-feautres)
- [⚙️ Repository Structure](#️-repository-structure)
- [🧩 Modules](#-modules)
- [🏎💨 Getting Started](#-getting-started)
  - [✅ Prerequisites](#-prerequisites)
  - [💻 Installation](#-installation)
  - [🤖 Running readme-ai](#-running-readme-ai)
  - [🧪 Running Tests](#-running-tests)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [🪪 License](#-license)
- [📫 Contact](#-contact)
- [🙏 Acknowledgments](#-acknowledgments)

---
## 👋 Introduction

Open source project written in Python
* Uses natural language processing to automatically generate a README.md file for a given codebase
* Can be run from the command line
* Supports English and Spanish
* Generates a report of the most important keywords in the codebase
* Includes a link to the original codebase repository

## 🔮 Feautres

> `[📌  INSERT-DESCRIPTION]`

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## ⚙️ Repository Structure
```bash
.
├── LICENSE
├── Makefile
├── README.md
├── conf
│   ├── badges.json
│   ├── conf.toml
│   └── templates
│       └── base_py.toml
├── docs
│   ├── README_EX_1.md
│   ├── README_EX_2.md
│   ├── README_EX_3.md
│   ├── imgs
│   │   ├── docs.png
│   │   ├── head.png
│   │   ├── misc.png
│   │   ├── overview.png
│   │   ├── tree.png
│   │   └── usage.png
│   └── raw_data.csv
├── pyproject.toml
├── requirements.txt
├── scripts
│   ├── run_main.sh
│   └── test.sh
├── setup
│   ├── environment.yaml
│   └── setup.sh
├── setup.py
├── src
│   ├── __init__.py
│   ├── builder.py
│   ├── conf.py
│   ├── logger.py
│   ├── main.py
│   ├── model.py
│   ├── processor.py
│   └── utils.py
└── tests
    ├── conftest.py
    ├── test_builder.py
    ├── test_conf.py
    ├── test_logger.py
    ├── test_main.py
    ├── test_model.py
    ├── test_processor.py
    └── test_utils.py

9 directories, 39 files
```
---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 🧩 Modules


<details closed><summary>Scripts</summary>

| File Name   | Summary                                                                                                                                                      |
|:------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| run_main.sh | This code is a Bash script that downloads the English language model for the spaCy library and then runs the main. py file from the src directory.           |
| test.sh     | This code activates a conda environment called "myenv", runs a pytest command with verbose and junitxml options, and then deactivates the conda environment. |

</details>

<details closed><summary>Src</summary>

| File Name    | Summary                                                                                                                                                                                                                                                                  |
|:-------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| builder.py   | This code is a Python script that builds a Markdown file from a configuration object, a list of features, an introduction, a list of packages, a name, and a URL.                                                                                                        |
| conf.py      | This code defines a configuration constants object, AppConfig, which contains five dataclasses: OpenAI, GitHub, Markdown, Paths, and AppConfig.                                                                                                                          |
| logger.py    | This code creates a Logger class which provides methods for logging messages with different levels of severity. The messages are printed to the console with different colors depending on the severity.                                                                 |
| main.py      | This code is a Python script that uses the OpenAI API to generate a README. md file for a given project. It loads a configuration file, clones the project's codebase, and uses the OpenAI API to generate features, an introduction, and documentation for the project. |
| model.py     | This code is a Python module that provides functions for summarizing code and generating readme features. It uses the OpenAI API and the Spacy library to process text.                                                                                                  |
| processor.py | This code is a Python script that clones a Git repository and retrieves its contents. It also creates a conda environment file and parses the codebase to get the contents of each file with a specific file type.                                                       |
| utils.py     | This code creates a FileFactory class that can be used to read and write data from different file types, such as CSV, JSON, HTML, MD, and TOML.                                                                                                                          |

</details>
<hr />

## 🏎💨 Getting Started
    
### ✅ Prerequisites
    
Before you begin, ensure that you have the following prerequisites installed:
    
- `[📌  INSERT-PREREQUISITES-IF-NEEDED]`

    
### 💻 Installation
    
1. Clone the readme-ai repository:
    
```sh
git clone https://github.com/eli64s/readme-ai
```
    
2. Change to the project directory:
    
```sh
cd readme-ai
```
    
3. Install the dependencies:
    
```sh
pip install -r requirements.txt
```
    
### 🤖 Running readme-ai
    
```sh
python main.py
```
    
### 🧪 Running Tests
    
```sh
# INSERT-HOW-TO-RUN-UNIT-TESTS
```
    
---

    
## 🗺 Roadmap

- [X] `[📌  INSERT-TASK-TODO]`
- [ ] `[📌  INSERT-TASK-TODO]`
- [ ] `[📌  INSERT-TASK-TODO]`

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

## 📫 Contact

If you have any questions or concerns, please open an issue on GitHub or contact the repo owner at `[📌  your-email@example.com]`


---

## 🙏 Acknowledgments

 `[📌  INSERT-DESCRIPTION]`

---
