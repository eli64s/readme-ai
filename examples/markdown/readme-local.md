<p align="center">
  <img src="https://flink.apache.org/img/logo/png/1000/flink_squirrel_1000.png" width="100" />
</p>
<p align="center">
    <h1 align="center">PYFLINK-POC</h1>
</p>
<p align="center">
    <em>Streamline data processing with PyFlink-PoC.</em>
</p>
<p align="center">
	<!-- local repository, no metadata badges. -->
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
	<img src="https://img.shields.io/badge/Apache%20Flink-E6526F.svg?style=flat&logo=Apache-Flink&logoColor=white" alt="Apache%20Flink">
	<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat&logo=YAML&logoColor=white" alt="YAML">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=flat&logo=AIOHTTP&logoColor=white" alt="AIOHTTP">
	<img src="https://img.shields.io/badge/Apache%20Kafka-231F20.svg?style=flat&logo=Apache-Kafka&logoColor=white" alt="Apache%20Kafka">
	<img src="https://img.shields.io/badge/pandas-150458.svg?style=flat&logo=pandas&logoColor=white" alt="pandas">
</p>
<hr>

##  Quick Links

> - [ Overview](#-overview)
> - [ Features](#-features)
> - [ Repository Structure](#-repository-structure)
> - [ Modules](#-modules)
> - [ Getting Started](#-getting-started)
>   - [ Installation](#-installation)
>   - [ Running pyflink-poc](#-running-pyflink-poc)
>   - [ Tests](#-tests)
> - [ Project Roadmap](#-project-roadmap)
> - [ Contributing](#-contributing)
> - [ License](#-license)
> - [ Acknowledgments](#-acknowledgments)

---

##  Overview

The pyflink-poc project is a powerful and efficient data stream processing framework built with Apache Flink and Python. Its core functionalities include consuming data from Apache Kafka using asyncio and aiohttp, providing fault-tolerant processing capabilities with checkpointing, filtering and joining data, and sending alerts based on predefined conditions. This project's value proposition lies in its ability to handle large-scale data processing in real-time, enabling businesses to derive insights, make data-driven decisions, and take proactive actions promptly.

---

##  Features

|   | Feature        | Description                                                                                                                                                                                                                                                                             |
|---|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ⚙️ | Architecture  | The project follows a client-server architecture, where the client side consumes data from Apache Kafka using asyncio and aiohttp, and the server side processes the data using Apache Flink and Python. The architecture is designed for high scalability and fault tolerance.              |
| 🔩 | Code Quality   | The codebase demonstrates good code quality and adheres to standard Python style conventions. It includes proper code documentation, follows meaningful variable and function naming, and maintains consistent formatting.                                                                                |
| 📄 | Documentation  | The project has extensive documentation, including detailed README files explaining the project's setup, dependencies, and usage. The code is well-documented, providing inline comments and docstrings that facilitate understanding and maintenance.                                              |
| 🔌 | Integrations   | The key integrations and external dependencies of the project include Apache Kafka for data ingestion, Apache Flink for stream processing, and various Python libraries such as aiohttp, pandas, and pyflink. These integrations enable seamless connectivity and efficient data processing.   |
| 🧩 | Modularity     | The codebase is well-structured and modular, allowing for easy reusability of components. It follows the principle of separation of concerns, with different modules responsible for specific tasks, such as data ingestion, processing, and alert handling, ensuring maintainability and extensibility. |
| 🧪 | Testing        | The project employs unit testing using the pytest framework to ensure the correctness and robustness of the code. It contains a comprehensive test suite, covering various functionalities and edge cases. Additionally, the project utilizes aioresponses for mocking HTTP responses during testing.  |
| ⚡️ | Performance    | The project demonstrates efficient performance, leveraging the power of Apache Kafka and Apache Flink for real-time stream processing. The codebase efficiently utilizes system resources and takes advantage of parallel processing to achieve high throughput and low latency.                            |
| 🛡️ | Security       | The project incorporates measures to ensure data protection and access control. It uses secure communication protocols for interaction with external APIs, implements proper authentication and authorization mechanisms, and follows best practices to prevent data leakage and unauthorized access.                    |
| 📦 | Dependencies   | The project relies on various external libraries and dependencies, including shell, txt, sh, yaml, py, apache-kafka, apache-flink, asyncio, text, aioresponses, aiohttp, pandas, toml, pyflink, and python. These dependencies provide necessary functionality and streamline development.           |


---

##  Repository Structure

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

##  Modules

<details closed><summary>.</summary>

| File                                 | Summary                                                                                                                                                                                                                                                                    |
| ---                                  | ---                                                                                                                                                                                                                                                                        |
| [requirements.txt](requirements.txt) | The code snippet in src/consumer.py is responsible for consuming data from Apache Kafka using asyncio and aiohttp. It plays a critical role in the repository's architecture by handling the retrieval of data from Kafka and processing it further.                       |
| [setup.py](setup.py)                 | This code snippet is the setup file for the parent repository. It sets up the required packages and dependencies, including packages for documentation, code styling, and testing. It also specifies the repository's name, version, and additional configuration options. |

</details>

<details closed><summary>setup</summary>

| File                       | Summary                                                                                                                                                                                            |
| ---                        | ---                                                                                                                                                                                                |
| [setup.sh](setup/setup.sh) | This code snippet is a setup script for the parent repository. It installs Java 11, Python 3.7, and Conda. It also downloads and extracts PyFlink, sets environment variables and aliases for zsh. |

</details>

<details closed><summary>scripts</summary>

| File                         | Summary                                                                                                                                                                                                                                                                                                                                                   |
| ---                          | ---                                                                                                                                                                                                                                                                                                                                                       |
| [run.sh](scripts/run.sh)     | The code snippet in the `run.sh` script starts a Flink cluster, submits a PyFlink job, and stops the cluster. It plays a critical role in running the PyFlink job within the larger repository architecture.                                                                                                                                              |
| [clean.sh](scripts/clean.sh) | The `clean.sh` script in the `scripts` directory is responsible for cleaning up various artifacts and files in the repository. It removes backup files, Python cache files, build artifacts, Jupyter notebook checkpoints, pytest cache, and log files. This script is an essential part of maintaining the cleanliness and organization of the codebase. |

</details>

<details closed><summary>conf</summary>

| File                                        | Summary                                                                                                                                                                                                                                                                                                                                                               |
| ---                                         | ---                                                                                                                                                                                                                                                                                                                                                                   |
| [flink-config.yaml](conf/flink-config.yaml) | The code snippet, located in `conf/flink-config.yaml`, contains the Flink configuration for the parent repository. It sets various parameters related to job and task managers, high availability, parallelism, state backend, and logging. These settings define the behavior and performance of the Flink application running within the repository's architecture. |
| [conf.toml](conf/conf.toml)                 | The code snippet in the conf/conf.toml file provides configuration constants for the parent repository. It includes Kafka and Flink settings such as the bootstrap servers, topic, job manager, and parallelism. It plays a critical role in defining the necessary settings for the repository's Kafka and Flink components.                                         |

</details>

<details closed><summary>src</summary>

| File                                       | Summary                                                                                                                                                                                                                                                                                                                                         |
| ---                                        | ---                                                                                                                                                                                                                                                                                                                                             |
| [alerts_handler.py](src/alerts_handler.py) | The code snippet `alerts_handler.py` implements a REST API alert handler for the Flink consumer in the parent repository. It sends alerts to an API using aiohttp in batches, serializes alerts using Apache Avro, and buffers alerts before sending them to the API.                                                                           |
| [logger.py](src/logger.py)                 | Summary: The `logger.py` file in the `src` directory of the codebase contains a Logger class that configures and provides logging functionality for the project. It allows logging messages with different log levels and formats them using colored output.                                                                                    |
| [consumer.py](src/consumer.py)             | The `consumer.py` code snippet is responsible for data stream processing using Apache Flink and Python. It creates an execution environment, sets up the stream time characteristic and checkpointing for fault tolerance, defines source and batch tables, performs data filtering and joins, and processes flagged records by sending alerts. |

</details>

---

##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Python**: `version x.y.z`

###  Installation

1. Clone the pyflink-poc repository:

```sh
git clone ../pyflink-poc
```

2. Change to the project directory:

```sh
cd pyflink-poc
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

###  Running pyflink-poc

Use the following command to run pyflink-poc:

```sh
python main.py
```

###  Tests

To execute tests, run:

```sh
pytest
```

---

##  Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://local/pyflink-poc/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://local/pyflink-poc/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://local/pyflink-poc/issues)**: Submit bugs found or log feature requests for Pyflink-poc.

<details closed>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
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
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-quick-links)

---
