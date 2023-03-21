
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
readme-ai
</h1>
<h3 align="center">📍 The future of documentation is here.</h3>
<h3 align="center">🚀 Developed with the software and tools below.</h3>
<p align="center">


<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white" alt="black" />
<img src="https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="colorlog" />
<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=for-the-badge&logo=Pytest&logoColor=white" alt="coverage" />
<img src="https://img.shields.io/badge/spaCy-09A3D5.svg?style=for-the-badge&logo=spaCy&logoColor=white" alt="dacite" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="GitPython" />

<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=for-the-badge&logo=GNU-Bash&logoColor=white" alt="GNU Bash" />
<img src="https://img.shields.io/badge/Anaconda-44A833.svg?style=for-the-badge&logo=Anaconda&logoColor=white" alt="Anaconda" />
<img src="https://img.shields.io/badge/ZeroMQ-DF0000.svg?style=for-the-badge&logo=ZeroMQ&logoColor=white" alt="isort" />
<img src="https://img.shields.io/badge/OpenSSL-721412.svg?style=for-the-badge&logo=OpenSSL&logoColor=white" alt="flake8" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white" alt="JSON" />
</p>

</div>


---
## 📍 Table of Contents
- [📍 Table of Contents](#-table-of-contents)
- [👋 Introdcution](#-introdcution)
- [🔮 Feautres](#-feautres)
- [⚙️ Project Structure](#️-project-structure)
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

## 👋 Introdcution

The Readme AI codebase allows for the conversion of Readme files into other formats such as PDF, HTML, and Markdown. This is done using a natural language processing approach that analyzes the Readme

## 🔮 Feautres

> `[📌  INSERT-PROJECT-FEATURES]`

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## ⚙️ Project Structure

```bash
.
├── LICENSE
├── Makefile
├── README.md
├── conf
│   ├── badges.json
│   ├── conf.toml
│   ├── file_extensions_map.toml
│   └── language_instructions.toml
├── docs
│   ├── README_EX_1.md
│   ├── README_EX_2.md
│   ├── README_EX_3.md
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

8 directories, 40 files
```
---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 🧩 Modules
<details closed><summary>Scripts</summary>

| File     | Summary                                                                                                                                                                                                         |
|:---------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| clean.sh | This bash script is used to clean up Python cache files, remove build artifacts, remove Jupyter notebook checkpoints, and remove pytest cache.                                                                  |
| run.sh   | This Bash script activates a Conda environment and runs a Python script. It begins by setting the "-eo pipefail" flag, which causes the script to exit immediately if any command returns a non-zero exit code. |

</details>

<details closed><summary>Src</summary>

| File         | Summary                                                                                                                                                                                                                                              |
|:-------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| builder.py   | format. py is a Python file that contains functions to build a markdown file from a configuration object, a list of badges, an introduction string, a name, and a URL.                                                                               |
| conf.py      | This file contains the configuration constants for the project. It contains five dataclasses: OpenAI, GitHub, Markdown, Paths, and AppConfig.                                                                                                        |
| logger.py    | Logger is a class that provides logging functionality with colored output. It is initialized with a name and a logging level (defaults to INFO).                                                                                                     |
| main.py      | This file contains the main function for the README-AI application. It is responsible for loading the configuration file, parsing command line arguments, fetching project dependencies, and generating the README. md file.                         |
| model.py     | This file contains the model class for the OpenAI API. It provides functions for converting code to text, generating readme features, and summarizing text.                                                                                          |
| processor.py | This file contains the source code for the processor module. It contains functions for cloning a GitHub repository, detecting the primary language of the repository, extracting dependencies from the repository, and generating user instructions. |
| utils.py     | This file contains the FileFactory class and several FileHandler subclasses. The FileFactory class is used to create a FileHandler object based on the file type of the file path passed to it.                                                      |

</details>
<hr />

## 🏎💨 Getting Started

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

### 🤖 Running readme-ai

```sh
python main.py
```

### 🧪 Running Tests
```sh
#run tests
```

<hr />

## 🗺 Roadmap

- [X] [📌  INSERT-TASK-TODO]
- [X] [📌  INSERT-TASK-TODO]
- [ ] [📌  INSERT-TASK-TODO]
- [ ] [📌  INSERT-TASK-TODO]


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

If you have any questions or concerns, please open an issue on GitHub or contact the repo owner at `[📌  INSERT-EMAIL-ADDRESS]`

---

## 🙏 Acknowledgments
> `[📌  INSERT-DESCRIPTION]`


---

