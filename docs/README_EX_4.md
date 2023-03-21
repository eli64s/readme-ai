
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
pyflink_scripts
</h1>
<h3 align="center">📍 Make your data pipeline great again!</h3>
<h3 align="center">🚀 Developed with the software and tools below.</h3>
<p align="center">

<img src="https://img.shields.io/badge/scikitlearn-F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="xz" />
<img src="https://img.shields.io/badge/DVC-13ADC7.svg?style=for-the-badge&logo=DVC&logoColor=white" alt="libsodium" />
<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=for-the-badge&logo=Pytest&logoColor=white" alt="pyaml" />
<img src="https://img.shields.io/badge/SciPy-8CAAE6.svg?style=for-the-badge&logo=SciPy&logoColor=white" alt="platformdirs" />
<img src="https://img.shields.io/badge/spaCy-09A3D5.svg?style=for-the-badge&logo=spaCy&logoColor=white" alt="decorator" />
<img src="https://img.shields.io/badge/precommit-FAB040.svg?style=for-the-badge&logo=pre-commit&logoColor=black" alt="dacite" />

<img src="https://img.shields.io/badge/OpenSSL-721412.svg?style=for-the-badge&logo=OpenSSL&logoColor=white" alt="libsqlite" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="coverage" />
<img src="https://img.shields.io/badge/ZeroMQ-DF0000.svg?style=for-the-badge&logo=ZeroMQ&logoColor=white" alt="ncurses" />
<img src="https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="scikit-learn" />
<img src="https://img.shields.io/badge/NumPy-013243.svg?style=for-the-badge&logo=NumPy&logoColor=white" alt="fastparquet" />
<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white" alt="python-dateutil" />
</p>

</div>

---
## 📍 Table of Contents
- [📍 Table of Contents](#-table-of-contents)
- [👋 Introdcution](#-introdcution)
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

## 👋 Introdcution

This codebase includes scripts for interacting with the Apache Flink Python API. With these scripts, users can submit and manage Flink jobs, as well as query the state of Flink clusters.

## 🔮 Feautres

> `[📌  INSERT-PROJECT-FEATURES]`

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## ⚙️ Project Structure

```bash
.
├── conf
│   ├── conf.toml
│   ├── flink-config.yaml
│   └── my_flink_job.yaml
├── scripts
│   ├── project_setup.sh
│   └── run.sh
├── setup
│   └── setup.sh
└── src
    ├── consumer.py
    ├── kafka_snowflake_match.py
    ├── main.py
    ├── my_flink_consumer.py
    ├── nrt_alerts.py
    ├── send_alerts.py
    └── sink.py

5 directories, 13 files
```
---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 🧩 Modules
<details closed><summary>Scripts</summary>

| File   | Summary                                                                                                          |
|:-------|:-----------------------------------------------------------------------------------------------------------------|
| run.sh | This code is a Bash script that starts a Flink cluster, submits a PyFlink job, and then stops the Flink cluster. |

</details>

<details closed><summary>Src</summary>

| File                     | Summary                                                                                                                                                                                                  |
|:-------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| sink.py                  | This code creates a PyFlink application that consumes messages from a Kafka topic, checks if the data matches a Snowflake table, and then inserts the data into the Snowflake table if a match is found. |
| my_flink_consumer.py     | This code sets up a Flink job pipeline to process XML data from a Kafka source and send alerts via an API call if the customer age is below a specified threshold.                                       |
| nrt_alerts.py            | This code sets up a Flink job pipeline to process XML data from a Kafka source and send alerts via an API call if the customer age is below a specified threshold.                                       |
| kafka_snowflake_match.py | This code creates a Flink job that reads messages from a Kafka topic, checks if the data matches a Snowflake table, and prints the results to the console.                                               |
| send_alerts.py           | This code creates a stream pipeline that consumes data from a Kafka topic, processes it, and sends alerts via an API when a new booking is made for a hotel at a price below $100.                       |
| consumer.py              | This code is a Flink-Kafka consumer script that reads messages from a Kafka topic, applies a custom mapper function to the messages, and prints the results to the console.                              |
| main.py                  | This example uses Flink State to maintain a count of incoming Kafka messages. The `MyMapper` class is defined as a separate mapper function, which is invoked for each message in the stream.            |

</details>
<hr />

## 🏎💨 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> `[📌  INSERT-PROJECT-PREREQUISITES]`

### 💻 Installation

1. Clone the pyflink_scripts repository:
```sh
git clone https://github.com/eli64s/pyflink_scripts
```

2. Change to the project directory:
```sh
cd pyflink_scripts
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

### 🤖 Running pyflink_scripts

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

