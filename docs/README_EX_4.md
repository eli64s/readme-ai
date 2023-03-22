
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
readme-ai
</h1>
<h3 align="center">📍 The future of documentation is here.</h3>
<h3 align="center">🚀 Developed with the software and tools below.</h3>
<p align="center">

<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white" alt="toml" />
<img src="https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="python-dateutil" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="pygments" />
<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=for-the-badge&logo=Pytest&logoColor=white" alt="pandas" />
<img src="https://img.shields.io/badge/ZeroMQ-DF0000.svg?style=for-the-badge&logo=ZeroMQ&logoColor=white" alt="matplotlib-inline" />

<img src="https://img.shields.io/badge/NumPy-013243.svg?style=for-the-badge&logo=NumPy&logoColor=white" alt="pre-commit" />
<img src="https://img.shields.io/badge/SciPy-8CAAE6.svg?style=for-the-badge&logo=SciPy&logoColor=white" alt="platformdirs" />
<img src="https://img.shields.io/badge/scikitlearn-F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="dvc-s3" />
<img src="https://img.shields.io/badge/spaCy-09A3D5.svg?style=for-the-badge&logo=spaCy&logoColor=white" alt="executing" />
<img src="https://img.shields.io/badge/DVC-13ADC7.svg?style=for-the-badge&logo=DVC&logoColor=white" alt="sphinx" />

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
  - [🤖 Using readme-ai](#-using-readme-ai)
  - [🧪 Running Tests](#-running-tests)
- [🛠 Future Development](#-future-development)
- [🤝 Contributing](#-contributing)
- [🪪 License](#-license)
- [🙏 Acknowledgments](#-acknowledgments)

---

## 📍Overview

The Readme AI codebase allows for the conversion of Readme files into other formats such as PDF, HTML, and Markdown. This is done using a natural language processing approach that analyzes the Readme

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
│   ├── README_EX_1_new.md
│   ├── README_EX_2.md
│   ├── README_EX_3.md
│   ├── README_EX_4.md
│   ├── imgs
│   │   ├── docs.png
│   │   ├── header.png
│   │   ├── misc.png
│   │   ├── setup.png
│   │   ├── toc.png
│   │   └── tree.png
│   └── raw_data.csv
├── requirements.txt
├── scripts
│   ├── clean.sh
│   ├── py_script_header.sh
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
│   ├── file_parser.py
│   ├── logger.py
│   ├── main.py
│   ├── model.py
│   └── processor.py
└── tests
    ├── conftest.py
    ├── test_builder.py
    ├── test_conf.py
    ├── test_file_factory.py
    ├── test_logger.py
    ├── test_main.py
    ├── test_model.py
    └── test_processor.py

9 directories, 47 files
```
---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 💻 Modules
<details closed><summary>Scripts</summary>

| File                | Summary                                                                                                                                                                  |
|:--------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| py_script_header.sh | This code is a Bash script that iterates through all the . py files in a specified folder and adds a header to each file with the script name, author, and date updated. |
| run.sh              | This code is a Bash script that activates a Conda environment and runs a Python script. It also allows for the exporting of environment variables.                       |
| clean.sh            | This code is a Bash script that cleans up Python cache files, removes build artifacts, Jupyter notebook checkpoints, and pytest cache.                                   |

</details>

<details closed><summary>Src</summary>

| File            | Summary                                                                                                                                                                                                                                                                                                                                                                      |
|:----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| file_parser.py  | This is a file parser module that can be used to parse files in various formats and extract dependencies from them. It supports formats such as requirements. txt, conda. yml, Pipfile, Gemfile, Cargo. lock, Cargo. toml, build. gradle, build. sbt, composer. json, composer. lock, conda. yml, dependencies. yml, environment. yml, snapcraft. yaml, snap/snapcraft. yaml |
| conf.py         | This code creates configuration constants for an application, including OpenAI API details, GitHub repository details, Markdown template code, and project file paths.                                                                                                                                                                                                       |
| processor.py    | This code provides methods to process a GitHub repository. It clones the repository to a temporary directory, gets the file contents, creates a temporary directory, and gets the project dependencies.                                                                                                                                                                      |
| logger.py       | Logger is a class for the project that provides logging capabilities with colored output. It supports logging levels such as DEBUG, INFO, WARNING, ERROR, and CRITICAL.                                                                                                                                                                                                      |
| file_factory.py | This FileHandler class is a file factory module that provides methods to read and write files in markdown, toml, and json formats.                                                                                                                                                                                                                                           |
| model.py        | This code uses OpenAI's GPT-3 model to generate summary text from code. It uses the text-davinci-003 model to create a prompt from the code, and then uses the text-davinci-002 model to generate a summary of the code.                                                                                                                                                     |
| builder.py      | This code builds a README. md file from a template and data. It uses the pandas library to parse the data, the git library to clone a repository, and the subprocess library to create a directory tree.                                                                                                                                                                     |
| main.py         | This code is a Python script that generates a README. md file for a given repository using OpenAI. It reads in configuration files, parses command line arguments, and uses the GitHub and OpenAI APIs to generate a summary of the codebase and a slogan for the repository.                                                                                                |

</details>
<hr />

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> `[📌  INSERT-PROJECT-PREREQUISITES]`

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

### 🤖 Using readme-ai

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

