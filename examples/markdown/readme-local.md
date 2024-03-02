<p align="left">
  <img src="https://flink.apache.org/img/logo/png/1000/flink_squirrel_1000.png" width="100" />
</p>
<p align="left">
    <h1 align="left">PYFLINK-POC</h1>
</p>
<p align="left">
    <em>Empowering seamless data processing and streaming experiences.</em>
</p>
<p align="left">
	<!-- local repository, no metadata badges. -->
<p>
<p align="left">
		<em>Developed with the software and tools below.</em>
</p>
<p align="left">
	<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=default&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
	<img src="https://img.shields.io/badge/Apache%20Flink-E6526F.svg?style=default&logo=Apache-Flink&logoColor=white" alt="Apache%20Flink">
	<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=default&logo=YAML&logoColor=white" alt="YAML">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=default&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=default&logo=AIOHTTP&logoColor=white" alt="AIOHTTP">
	<img src="https://img.shields.io/badge/Apache%20Kafka-231F20.svg?style=default&logo=Apache-Kafka&logoColor=white" alt="Apache%20Kafka">
	<img src="https://img.shields.io/badge/pandas-150458.svg?style=default&logo=pandas&logoColor=white" alt="pandas">
</p>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>

- [📍 Overview](#-overview)
- [🧩 Features](#-features)
- [🗂️ Repository Structure](#️-repository-structure)
- [📦 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
  - [⚙️ Installation](#️-installation)
  - [🤖 Usage](#-usage)
  - [🧪 Tests](#-tests)
- [🛠 Project Roadmap](#-project-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)
</details>
<hr>

## 📍 Overview

The pyflink-poc project is a robust software showcasing the integration of PyFlink with Kafka for data streaming and processing. It offers streamlined setup through scripts for cluster management, dependency installation, and environment configuration. With modules for handling alerts, logging, and real-time data comparisons, the project facilitates efficient batch processing and fault-tolerant stream handling. Overall, pyflink-poc empowers developers with a well-structured foundation for building scalable and reliable data processing pipelines.

---

## 🧩 Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | The project has a modular architecture that separates data processing components from stream processing. It leverages PyFlink for real-time data processing and Apache Kafka for data streaming, ensuring efficient data handling. |
| 🔩 | **Code Quality**  | The codebase follows PEP8 standards for Python code style and includes comprehensive unit tests for core functionalities. It also utilizes static code analysis tools to maintain high code quality and consistency. |
| 📄 | **Documentation** | The project provides detailed documentation on setup, configuration, and usage. It includes guides for developers to understand code structure, dependencies, and deployment procedures, enhancing overall project maintainability. |
| 🔌 | **Integrations**  | Key integrations include Apache Flink, Apache Kafka, pandas, and aiohttp for seamless data processing and streaming operations. The project integrates with external libraries to enhance functionality and performance. |
| 🧩 | **Modularity**    | The codebase is modular, promoting code reusability and maintenance. Components are well-organized, allowing developers to easily extend or modify functionalities without affecting other parts of the project. |
| 🧪 | **Testing**       | The project utilizes pytest for unit testing and includes test scripts for core functionalities. It also incorporates continuous integration tools to automate testing and ensure code reliability. |
| ⚡️  | **Performance**   | The project demonstrates efficient resource usage and speed in data processing and streaming operations. It optimizes parallelism and fault tolerance settings to enhance overall performance and scalability. |
| 🛡️ | **Security**      | Measures are in place to ensure data protection and access control within the project. Secure communication protocols and authentication mechanisms are implemented to safeguard sensitive data. |
| 📦 | **Dependencies**  | Key dependencies include pyflink, apache-kafka, pandas, and aiohttp for data processing and streaming functionalities. External libraries are managed through requirements.txt and setup.py for streamlined dependency management. |

---

## 🗂️ Repository Structure

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

## 📦 Modules

<details closed><summary>.</summary>

| File                                 | Summary                                                                                                                                                                                                                                                            |
| ---                                  | ---                                                                                                                                                                                                                                                                |
| [requirements.txt](requirements.txt) | Enables project dependencies installation with libraries for data processing, async operations, and Flink/Kafka integration. Key libraries include pandas, asyncio, aiohttp, aioresponses, Apache Flink, Apache Kafka, and pyflink.                                |
| [setup.py](setup.py)                 | Sets up dependencies for the project through package management. Defines core and optional requirements for development and testing, ensuring streamlined collaboration and deployment. Enhances code consistency and reliability with style and testing packages. |

</details>

<details closed><summary>setup</summary>

| File                       | Summary                                                                                                                                                                                                  |
| ---                        | ---                                                                                                                                                                                                      |
| [setup.sh](setup/setup.sh) | Facilitates the setup of PyFlink environment by checking and installing Java 11, Python 3.7, Conda, and PyFlink. Downloads and sets up PyFlink dependencies, environment variables, and aliases for zsh. |

</details>

<details closed><summary>scripts</summary>

| File                         | Summary                                                                                                                                                                                                                         |
| ---                          | ---                                                                                                                                                                                                                             |
| [run.sh](scripts/run.sh)     | Initiates Flink cluster, runs PyFlink job, and stops the cluster. Manages cluster operations for executing PyFlink jobs. Essential script in repository architecture for job execution.                                         |
| [clean.sh](scripts/clean.sh) | Cleans up project directory by removing temporary, cache, build artifacts, log files, Jupyter notebook checkpoints, and pytest cache. Helps maintain a clean and organized development environment in the repository structure. |

</details>

<details closed><summary>conf</summary>

| File                                        | Summary                                                                                                                                                                 |
| ---                                         | ---                                                                                                                                                                     |
| [flink-config.yaml](conf/flink-config.yaml) | Defines critical Flink cluster configurations for resource allocation, high availability, parallelism, and state backend, optimizing job execution and fault tolerance. |
| [conf.toml](conf/conf.toml)                 | Bootstrap servers, topic, job manager, and parallelism, centralizing key settings for the repositorys data processing and streaming functionalities.                    |

</details>

<details closed><summary>src</summary>

| File                                       | Summary                                                                                                                                                                                                                                                       |
| ---                                        | ---                                                                                                                                                                                                                                                           |
| [alerts_handler.py](src/alerts_handler.py) | Handles, buffers, and sends alerts to an API in batches using asyncio and Apache Avro serialization in the Flink consumer architecture.                                                                                                                       |
| [logger.py](src/logger.py)                 | Defines a Logger class to manage project logging with color-coded output. Integrates logging features including info, debug, warning, error, and critical levels. Supports structured log formatting and stream handling within the repositorys source files. |
| [consumer.py](src/consumer.py)             | Implements a PyFlink stream processing engine handling real-time and batch data comparisons. Orchestrates alerts for flagged data discrepancies. Manages fault tolerance and parallel processing for data streaming.                                          |

</details>

---

## 🚀 Getting Started

**System Requirements:**

* **Python**: `version x.y.z`

### ⚙️ Installation

<h4>From <code>source</code></h4>

> 1. Clone the pyflink-poc repository:
>
> ```console
> $ git clone ../pyflink-poc
> ```
>
> 2. Change to the project directory:
> ```console
> $ cd pyflink-poc
> ```
>
> 3. Install the dependencies:
> ```console
> $ pip install -r requirements.txt
> ```

### 🤖 Usage

<h4>From <code>source</code></h4>

> Run pyflink-poc using the command below:
> ```console
> $ python main.py
> ```

### 🧪 Tests

> Run the test suite using the command below:
> ```console
> $ pytest
> ```

---

## 🛠 Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://local/pyflink-poc/issues)**: Submit bugs found or log feature requests for the `pyflink-poc` project.
- **[Submit Pull Requests](https://local/pyflink-poc/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://local/pyflink-poc/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your local account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone ../pyflink-poc
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
6. **Push to local**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="center">
   <a href="https://local{/pyflink-poc/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=pyflink-poc">
   </a>
</p>
</details>

---

## 📄 License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 👏 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-overview)

---
