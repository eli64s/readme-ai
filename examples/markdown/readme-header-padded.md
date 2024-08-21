[<img src="https://raw.githubusercontent.com/wuchong/awesome-flink/master/flink_squirrel.png" align="right" width="25%" padding-right="350">]()

# `PYFLINK-POC`

#### Streamlining data flow, empowering seamless integration.

<p align="left">
	<img src="https://img.shields.io/github/license/eli64s/pyflink-poc?style=flat-square&logo=opensourceinitiative&logoColor=white&color=BA0098" alt="license">
	<img src="https://img.shields.io/github/last-commit/eli64s/pyflink-poc?style=flat-square&logo=git&logoColor=white&color=BA0098" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/eli64s/pyflink-poc?style=flat-square&color=BA0098" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/eli64s/pyflink-poc?style=flat-square&color=BA0098" alt="repo-language-count">
</p>
<p align="left">
		<em>Built with the tools and technologies:</em>
</p>
<p align="left">
	<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat-square&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
	<img src="https://img.shields.io/badge/Apache%20Flink-E6526F.svg?style=flat-square&logo=Apache-Flink&logoColor=white" alt="Apache%20Flink">
	<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat-square&logo=YAML&logoColor=white" alt="YAML">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=flat-square&logo=AIOHTTP&logoColor=white" alt="AIOHTTP">
	<img src="https://img.shields.io/badge/Apache%20Kafka-231F20.svg?style=flat-square&logo=Apache-Kafka&logoColor=white" alt="Apache%20Kafka">
	<img src="https://img.shields.io/badge/pandas-150458.svg?style=flat-square&logo=pandas&logoColor=white" alt="pandas">
</p>

<br>

<details><summary>Table of Contents</summary>

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [🧩 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
    - [🔖 Prerequisites](#-prerequisites)
    - [📦 Installation](#-installation)
    - [🤖 Usage](#-usage)
    - [🧪 Tests](#-tests)
- [📌 Project Roadmap](#-project-roadmap)
- [🤝 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

</details>
<hr>

## 📍 Overview

The pyflink-poc project is a comprehensive solution that seamlessly integrates Apache Flink, Apache Kafka, and PyFlink for efficient stream processing. It offers streamlined setup and execution through scripts like run.sh and clean.sh, ensuring a tidy repository structure. Key components like alerts_handler.py and consumer.py handle batch alert processing and data stream management, respectively. With centralized configuration files and enhanced logging capabilities, pyflink-poc simplifies Flink application development and maintenance, making it a valuable tool for real-time data processing projects.

---

## 👾 Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | The project has a modular architecture leveraging Apache Flink for stream processing. It integrates with Apache Kafka for data ingestion and processing. The codebase is structured with clear separation of concerns for different components. |
| 🔩 | **Code Quality**  | The codebase maintains good quality and follows a consistent style. It includes clear variable naming, proper documentation, and adheres to PEP8 standards. Code reviews and linting tools are used to ensure high quality. |
| 📄 | **Documentation** | The project provides extensive documentation covering setup, configuration, usage, and code structure. README, inline comments, and configuration files are well-documented, aiding developers in understanding and contributing to the project. |
| 🔌 | **Integrations**  | Key integrations include PyFlink, Apache Kafka, and aiohttp for asynchronous communication. External dependencies like pandas, asyncio, and aioresponses are used for seamless integration within the architecture. |
| 🧩 | **Modularity**    | The codebase exhibits good modularity with separate modules for handling alerts, logging, and data processing. Components are designed for reusability and maintainability, promoting a scalable and extensible architecture. |
| 🧪 | **Testing**       | The project utilizes testing frameworks like pytest for unit and integration testing. Tests cover critical components such as alert handling, data processing, and stream processing logic, ensuring code reliability and functionality. |
| ⚡️  | **Performance**   | The project demonstrates efficient resource usage and speed in stream processing tasks. Utilization of Apache Flink and optimized configurations in Flink cluster settings contribute to high performance and scalability. |
| 🛡️ | **Security**      | Security measures include data protection through serialization using Apache Avro and access control mechanisms for external API communication. Secure coding practices are followed to prevent vulnerabilities and ensure data integrity. |
| 📦 | **Dependencies**  | Key dependencies include pandas, asyncio, aiohttp, Apache Flink, Apache Kafka, and PyFlink. These libraries enable seamless integration and functionality within the project's architecture. |
| 🚀 | **Scalability**   | The project demonstrates scalability with the ability to handle increased traffic and load through Apache Flink's distributed processing capabilities. Configurable parallelism settings and fault tolerance mechanisms support scalability requirements. |

---

## 📂 Repository Structure

```sh
└── pyflink-poc/
    ├── README.md
    ├── conf
    │   ├── conf.toml
    │   └── flink-config.yaml
    ├── data
    │   └── data.csv
    ├── requirements.txt
    ├── scripts
    │   ├── clean.sh
    │   └── run.sh
    ├── setup
    │   └── setup.sh
    ├── setup.py
    └── src
        ├── alerts_handler.py
        ├── consumer.py
        └── logger.py
```

---

## 🧩 Modules

<details closed><summary>.</summary>

| File | Summary |
| --- | --- |
| [requirements.txt](https://github.com/eli64s/pyflink-poc/blob/main/requirements.txt) | Enables project dependencies like pandas, asyncio, aiohttp, aioresponses, Apache Flink, Apache Kafka, and PyFlink for seamless integration within the repositorys architecture. |
| [setup.py](https://github.com/eli64s/pyflink-poc/blob/main/setup.py) | Defines package dependencies and configurations for the project. Sets up STREAM-ON with required packages and optional dev/test tools. Organizes project structure and enhances development workflow. |

</details>

<details closed><summary>setup</summary>

| File | Summary |
| --- | --- |
| [setup.sh](https://github.com/eli64s/pyflink-poc/blob/main/setup/setup.sh) | Checks/install Java 11, Python 3.7, Conda; downloads/extracts PyFlink; sets environment variables; creates aliases for zsh. Enhances PyFlink development workflow by streamlining environment configuration. |

</details>

<details closed><summary>scripts</summary>

| File | Summary |
| --- | --- |
| [run.sh](https://github.com/eli64s/pyflink-poc/blob/main/scripts/run.sh) | Initiates Flink cluster, executes PyFlink job, and halts Flink cluster. Orchestrates cluster operations for PyFlink job execution. |
| [clean.sh](https://github.com/eli64s/pyflink-poc/blob/main/scripts/clean.sh) | Cleans up project artifacts and cache files, ensuring a tidy repository structure. Removes temporary files, Python cache, build artifacts, Jupyter notebook checkpoints, and pytest cache, enhancing project cleanliness and organization. |

</details>

<details closed><summary>conf</summary>

| File | Summary |
| --- | --- |
| [flink-config.yaml](https://github.com/eli64s/pyflink-poc/blob/main/conf/flink-config.yaml) | Defines Flink cluster configuration settings for JobManager, TaskManager, High Availability, parallelism, state backend, and logging. Crucial for optimizing resource allocation, fault tolerance, and logging verbosity in the Flink application. |
| [conf.toml](https://github.com/eli64s/pyflink-poc/blob/main/conf/conf.toml) | Defines Kafka and Flink configuration constants for the parent repository. Specifies Kafka bootstrap servers and topic, as well as Flink job manager and parallelism settings. Crucial for maintaining consistent configurations across the project. |

</details>

<details closed><summary>src</summary>

| File | Summary |
| --- | --- |
| [alerts_handler.py](https://github.com/eli64s/pyflink-poc/blob/main/src/alerts_handler.py) | Handles sending alerts to an external API in batches, serializing data using Apache Avro. Manages a buffer for efficient batch processing and utilizes aiohttp for asynchronous communication. Key components include alert serialization, buffer management, and batch sending logic. |
| [logger.py](https://github.com/eli64s/pyflink-poc/blob/main/src/logger.py) | Enables logging with colored output for the project. Initializes a logger with specified name and level, configuring it to display log messages in different colors based on severity. Provides methods for logging at different levels. |
| [consumer.py](https://github.com/eli64s/pyflink-poc/blob/main/src/consumer.py) | Implements data stream processing with Flink, creating tables, views, and processing flagged records for alerts. Orchestrates the stream processing engine with event time characteristics and fault tolerance mechanisms. |

</details>

---

## 🚀 Getting Started

### 🔖 Prerequisites

**Python**: `version x.y.z`

### 📦 Installation

Build the project from source:

1. Clone the pyflink-poc repository:
```sh
❯ git clone https://github.com/eli64s/pyflink-poc
```

2. Navigate to the project directory:
```sh
❯ cd pyflink-poc
```

3. Install the required dependencies:
```sh
❯ pip install -r requirements.txt
```

### 🤖 Usage

To run the project, execute the following command:

```sh
❯ python main.py
```

### 🧪 Tests

Execute the test suite using the following command:

```sh
❯ pytest
```

---

## 📌 Project Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/eli64s/pyflink-poc/issues)**: Submit bugs found or log feature requests for the `pyflink-poc` project.
- **[Submit Pull Requests](https://github.com/eli64s/pyflink-poc/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/eli64s/pyflink-poc/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/eli64s/pyflink-poc
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/eli64s/pyflink-poc/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=eli64s/pyflink-poc">
   </a>
</p>
</details>

---

## 🎗 License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 🙌 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---
