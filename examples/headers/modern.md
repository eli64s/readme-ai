<div align="left" style="position: relative;">
<img src="https://flink.apache.org/img/logo/png/1000/flink_squirrel_1000.png" align="right" width="30%" style="margin: -20px 0 0 20px;">
<h1>PYFLINK-POC</h1>
<p align="left">
	<em>Streamlining data flow with PyFlink power!</em>
</p>
<p align="left">
	<img src="https://img.shields.io/github/license/eli64s/pyflink-poc?style=flat&logo=opensourceinitiative&logoColor=white&color=E30B5C" alt="license">
	<img src="https://img.shields.io/github/last-commit/eli64s/pyflink-poc?style=flat&logo=git&logoColor=white&color=E30B5C" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/eli64s/pyflink-poc?style=flat&color=E30B5C" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/eli64s/pyflink-poc?style=flat&color=E30B5C" alt="repo-language-count">
</p>
<p align="left">Built with the tools and technologies:</p>
<p align="left">
	<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=flat&logo=AIOHTTP&logoColor=white" alt="AIOHTTP">
	<img src="https://img.shields.io/badge/pandas-150458.svg?style=flat&logo=pandas&logoColor=white" alt="pandas">
	<img src="https://img.shields.io/badge/Apache%20Kafka-231F20.svg?style=flat&logo=Apache-Kafka&logoColor=white" alt="Apache%20Kafka">
	<img src="https://img.shields.io/badge/Apache%20Flink-E6526F.svg?style=flat&logo=Apache-Flink&logoColor=white" alt="Apache%20Flink">
</p>
</div>
<br clear="right">

<details><summary>Table of Contents</summary>

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🤖 Usage](#🤖-usage)
  - [🧪 Testing](#🧪-testing)
- [📌 Project Roadmap](#-project-roadmap)
- [🔰 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

</details>
<hr>

## 📍 Overview

Pyflink-poc enables real-time data streaming and processing, seamlessly integrating Apache Flink and Apache Kafka. It empowers users to handle data efficiently with Pandas and asyncio, emphasizing scalability and performance. Ideal for developers seeking lightweight, responsive architectures for large dataset management and concurrent operations in their projects.

---

## 👾 Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Combines the power of `PyFlink`, `Apache Kafka`, and `asyncio` for real-time data streaming and processing.</li><li>Utilizes lightweight and responsive architecture for efficient data handling and scalability.</li><li>Implements batch processing for anomaly detection and alert handling.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Well-structured codebase with clear separation of concerns.</li><li>Follows PEP 8 guidelines for Python code style.</li><li>Includes unit tests for critical components ensuring robustness.</li></ul> |
| 📄 | **Documentation** | <ul><li>Comprehensive documentation in multiple formats like `txt`, `py`, `sh`, `yaml`, and `toml`.</li><li>Includes setup instructions, usage guidelines, and project overview.</li><li>Enhances project management and onboarding of new contributors.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integrates seamlessly with `Apache Kafka` for data ingestion and `aiohttp` for asynchronous HTTP requests.</li><li>Utilizes `PyFlink` for distributed data processing.</li><li>Facilitates integration with external systems through APIs.</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Follows modular design principles for easy extensibility and maintenance.</li><li>Encapsulates functionalities into separate modules for better organization.</li><li>Promotes reusability of components across the codebase.</li></ul> |
| 🧪 | **Testing**       | <ul><li>Includes unit tests using `pytest` to ensure functionality and reliability.</li><li>Tests cover critical paths, edge cases, and integration scenarios.</li><li>Facilitates continuous integration and deployment pipelines.</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Emphasizes performance optimization for handling large datasets.</li><li>Utilizes asynchronous processing with `asyncio` for improved efficiency.</li><li>Fine-tunes configurations for optimal resource allocation and fault tolerance.</li></ul> |
| 🛡️ | **Security**      | <ul><li>Implements secure data transmission with serialization using `Apache Avro`.</li><li>Follows best practices for handling sensitive data and authentication.</li><li>Ensures data integrity and confidentiality in communication with external systems.</li></ul> |
| 📦 | **Dependencies**  | <ul><li>Utilizes dependencies like `PyFlink`, `Apache Kafka`, `Pandas`, and `aiohttp` for core functionality.</li><li>Manages dependencies using `pip` via `requirements.txt` for easy installation.</li><li>Ensures compatibility and version consistency across dependencies.</li></ul> |

---

## 📁 Project Structure

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


### 📂 Project Index
<details open>
	<summary><b><code>PYFLINK-POC/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/eli64s/pyflink-poc/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td>- Enables real-time data streaming and processing by integrating Apache Flink and Apache Kafka with asynchronous HTTP requests<br>- Facilitates efficient data handling and manipulation using Pandas library while leveraging asyncio for concurrent operations<br>- The codebase emphasizes scalability and performance in handling large datasets through its lightweight and responsive architecture.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/eli64s/pyflink-poc/blob/master/setup.py'>setup.py</a></b></td>
				<td>- Configures project dependencies and packages for STREAM-ON through setup.py<br>- Sets up various packages for documentation, style checking, and testing, enhancing the overall project structure and management.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- setup Submodule -->
		<summary><b>setup</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/eli64s/pyflink-poc/blob/master/setup/setup.sh'>setup.sh</a></b></td>
				<td>- Facilitates setup and configuration of project dependencies and environment variables<br>- Installs Java 11, Python 3.7, and PyFlink, sets environment variables, and creates aliases for zsh<br>- Enables seamless integration and execution of PyFlink within the development environment.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- scripts Submodule -->
		<summary><b>scripts</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/eli64s/pyflink-poc/blob/master/scripts/run.sh'>run.sh</a></b></td>
				<td>Initiate Flink cluster, execute PyFlink job, and terminate Flink cluster using the provided run.sh script.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/eli64s/pyflink-poc/blob/master/scripts/clean.sh'>clean.sh</a></b></td>
				<td>- Clean script file removes backup files, Python caches, build artifacts, Jupyter notebook checkpoints, and pytest cache from the project directory<br>- It ensures the project remains clutter-free by deleting unnecessary files and directories to streamline development and maintenance processes.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- conf Submodule -->
		<summary><b>conf</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/eli64s/pyflink-poc/blob/master/conf/flink-config.yaml'>flink-config.yaml</a></b></td>
				<td>Define Flink cluster configuration parameters in the provided YAML file to ensure optimal resource allocation, fault tolerance, and scalability for distributed data processing.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/eli64s/pyflink-poc/blob/master/conf/conf.toml'>conf.toml</a></b></td>
				<td>Define project-wide configuration constants for Kafka and Flink services in the conf.toml file.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- src Submodule -->
		<summary><b>src</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/eli64s/pyflink-poc/blob/master/src/alerts_handler.py'>alerts_handler.py</a></b></td>
				<td>- Handles the sending of alerts to an API in batches using asyncio and aiohttp<br>- The code serializes alerts using Apache Avro before sending them to the designated API endpoint<br>- Additionally, it includes functionality to buffer alerts and send them in batches when a certain threshold is reached.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/eli64s/pyflink-poc/blob/master/src/logger.py'>logger.py</a></b></td>
				<td>- The Logger class provides structured logging capabilities for the project, enabling different log levels and colored output<br>- It enhances the codebase architecture by ensuring effective logging of critical information, warnings, and errors, thereby facilitating debugging and monitoring activities across the system.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/eli64s/pyflink-poc/blob/master/src/consumer.py'>consumer.py</a></b></td>
				<td>- Implements data stream processing with Apache Flink and Python, orchestrating streaming and batch data comparisons for anomaly detection<br>- Manages state and fault tolerance through checkpointing and processes flagged records to trigger alerts, enhancing the real-time monitoring system.</td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with pyflink-poc, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip


### ⚙️ Installation

Install pyflink-poc using one of the following methods:

**Build from source:**

1. Clone the pyflink-poc repository:
```sh
❯ git clone https://github.com/eli64s/pyflink-poc
```

2. Navigate to the project directory:
```sh
❯ cd pyflink-poc
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```




### 🤖 Usage
Run pyflink-poc using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```


### 🧪 Testing
Run the test suite using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```


---
## 📌 Project Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/eli64s/pyflink-poc/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/eli64s/pyflink-poc/issues)**: Submit bugs found or log feature requests for the `pyflink-poc` project.
- **💡 [Submit Pull Requests](https://github.com/eli64s/pyflink-poc/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

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
