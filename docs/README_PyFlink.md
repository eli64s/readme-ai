
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
STREAM-ON
</h1>
<h3 align="center">📍 Powering Your Projects With STREAM-ON: Keep It Flowing!</h3>
<h3 align="center">🚀 Developed with the software and tools below.</h3>
<p align="center">

<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=for-the-badge&logo=GNU-Bash&logoColor=white" alt="" />
<img src="https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="shell" />
<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=for-the-badge&logo=AIOHTTP&logoColor=white" alt="pandas" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="toml" />
<img src="https://img.shields.io/badge/Apache%20Flink-E6526F.svg?style=for-the-badge&logo=Apache-Flink&logoColor=white" alt="pyc" />
<img src="https://img.shields.io/badge/Apache%20Kafka-231F20.svg?style=for-the-badge&logo=Apache-Kafka&logoColor=white" alt="yaml" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="py" />
</p>

</div>

---

## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍Overview](#-introdcution)
- [🔮 Features](#-features)
- [⚙️ Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🏎💨 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [🪪 License](#-license)
- [📫 Contact](#-contact)
- [🙏 Acknowledgments](#-acknowledgments)

---


## 📍Overview

STREAM-ON is a GitHub project that enables a developer to quickly and easily build and deploy streaming applications in the cloud. It allows developers to access comprehensive tools for creating applications and managing data streams without having to manage any underlying cloud infrastructure. It provides performance monitoring and operational visibility, as well as log analysis and debugging capabilities.

## 🔮 Feautres

> `[📌  INSERT-PROJECT-FEATURES]`

---


<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## ⚙️ Project Structure


```bash
repo
├── README.md
├── conf
│   ├── conf.toml
│   └── flink-config.yaml
├── data
│   └── data.csv
├── requirements.txt
├── scripts
│   ├── clean.sh
│   └── run.sh
├── setup
│   └── setup.sh
├── setup.py
└── src
    ├── alerts_handler.py
    ├── consumer.py
    └── logger.py

6 directories, 12 files
```

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 💻 Modules

<details closed><summary>Root</summary>

| File      | Summary                                                                                                           | Module    |
|:----------|:------------------------------------------------------------------------------------------------------------------|:----------|
| .DS_Store | This code is an error message indicating that a file could not be decoded because it is not a text or UTF-8 file. | .DS_Store |

</details>

<details closed><summary>Scripts</summary>

| File     | Summary                                                                                                                                                                                                        | Module           |
|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| run.sh   | This code is a Bash script that starts a Flink cluster, submits a PyFlink job, and then stops the Flink cluster.                                                                                               | scripts/run.sh   |
| clean.sh | This code is a Bash script that cleans up files and directories related to Python, Jupyter Notebooks, and pytest. It deletes Python cache files, build artifacts, Jupyter notebook checkpoints, and log files. | scripts/clean.sh |

</details>

<details closed><summary>Src</summary>

| File              | Summary                                                                                                                                                                                                                                                                                                                                           | Module                |
|:------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
| alerts_handler.py | This code is a REST API alert handler for the Flink consumer. It buffers alerts and sends them to the API in batches using aiohttp, and serializes them using Apache Avro.                                                                                                                                                                        | src/alerts_handler.py |
| logger.py         | Logger is a class for the project that provides logging capabilities with colored output and different log levels.                                                                                                                                                                                                                                | src/logger.py         |
| consumer.py       | This code is a Python script that uses Apache Flink to process streaming data. It creates a StreamExecutionEnvironment, sets the parallelism, time characteristic, and checkpointing mode, and creates a StreamTableEnvironment. It then creates a source table and a batch view in the Flink table environment, and uses SQL queries to join the | src/consumer.py       |

</details>

<hr />

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> `[📌  INSERT-PROJECT-PREREQUISITES]`

### 💻 Installation

1. Clone the STREAM-ON repository:
```sh
git clone /Users/k01101011/Documents/GitHub/STREAM-ON
```

2. Change to the project directory:
```sh
cd STREAM-ON
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

### 🤖 Using STREAM-ON

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
