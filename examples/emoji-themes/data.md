<p align="center">
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="30%">
</p>

<p align="center">
	<h1 align="center">BUENAVISTA</h1>
</p>

<p align="center">
	<em>BuenaVista: Where Data Dances with Ease!</em>
</p>

<p align="center">
	<img src="https://img.shields.io/github/license/jwills/buenavista?style=plastic&logo=opensourceinitiative&logoColor=white&color=white" alt="license">
	<img src="https://img.shields.io/github/last-commit/jwills/buenavista?style=plastic&logo=git&logoColor=white&color=white" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/jwills/buenavista?style=plastic&color=white" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/jwills/buenavista?style=plastic&color=white" alt="repo-language-count">
</p>

<p align="center">
	Tech Stack
</p>

<p align="center">
	<img src="https://img.shields.io/badge/DuckDB-FFF000.svg?style=plastic&logo=DuckDB&logoColor=black" alt="DuckDB">
	<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=plastic&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
	<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=plastic&logo=FastAPI&logoColor=white" alt="FastAPI">
	<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=plastic&logo=Pytest&logoColor=white" alt="Pytest">
	<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=plastic&logo=Docker&logoColor=white" alt="Docker">
	<br>
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=plastic&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=plastic&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions">
	<img src="https://img.shields.io/badge/PostgreSQL-4169E1.svg?style=plastic&logo=PostgreSQL&logoColor=white" alt="PostgreSQL">
	<img src="https://img.shields.io/badge/Pydantic-E92063.svg?style=plastic&logo=Pydantic&logoColor=white" alt="Pydantic">
</p>

<br>

### 📚 Table of Contents

- [📚 Table of Contents](#-table-of-contents)
- [📊 Overview](#-overview)
- [📈 Features](#-features)
- [📁 Project Structure](#-project-structure)
    - [📑 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
    - [🔧 Prerequisites](#-prerequisites)
    - [⚙️ Installation](#-installation)
    - [📓 Usage](#-usage)
    - [🧪 Testing](#testing)
- [🎯 Roadmap](#-roadmap)
- [🤝 Contributing](#contributing)
- [📜 License](#-license)
- [🌟 Acknowledgments](#-acknowledgments)

---

## 📊 Overview

**Buenavista** simplifies database interactions and query management for developers. With enhanced SQL dialects and seamless data handling, it streamlines querying across PostgreSQL, Trino, and DuckDB. Ideal for teams needing efficient data retrieval and transformation, Buenavista offers a robust solution for diverse database tasks.

---

## 📈 Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Structured around core classes for query results and database connections</li><li>Enhanced SQL dialects for Postgres, Trino, and DuckDB</li><li>Session-based approach for PostgreSQL and DuckDB interactions</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Defined package metadata and dependencies using `setup.py`</li><li>Custom functions and modifications for SQL dialects in `bv_dialects.py`</li><li>Pydantic models for query results and errors in `schemas.py`</li></ul> |
| 📄 | **Documentation** | <ul><li>Enables project dependencies with `dev-requirements.txt`</li><li>Usage of `docker-compose.yml` for defining services and configurations</li><li>Automated unit tests with GitHub Actions in `.github/workflows/main.yml`</li></ul> |
| 🔌 | **Integrations**  | <ul><li>HTTP endpoints for system information and SQL execution in `http/main.py`</li><li>Proxying PostgreSQL connections through Buenavista in `examples/postgres_proxy.py`</li><li>Automated Docker image building and pushing in `.github/workflows/push.yaml`</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Separate backends for PostgreSQL and DuckDB in `backends/` directory</li><li>Custom rewriter for DuckDB to PostgreSQL queries in `examples/duckdb_postgres.py`</li><li>HTTP context management in `http/context.py`</li></ul> |
| 🧪 | **Testing**       | <ul><li>Facilitates testing with `pytest`</li><li>Automated testing setup in `.github/workflows/main.yml`</li><li>Pydantic models for error handling in `http/schemas.py`</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Optimized query generation and transformation capabilities</li><li>Efficient handling of query results and session management</li><li>FastAPI server implementation for HTTP endpoints</li></ul> |
| 🛡️ | **Security**      | <ul><li>Secure communication between application and databases</li><li>Proper interpretation of server responses and data types</li><li>Session pooling and transaction handling for secure connections</li></ul> |
| 📦 | **Dependencies**  | <ul><li>Project dependencies managed with `pip` in `dev-requirements.txt`</li><li>Dependencies for database connectivity, API development, and testing</li><li>Installation commands provided for `pip` and `docker`</li></ul> |

---

## 📁 Project Structure

```sh
└── buenavista/
    ├── .github
    ├── LICENSE
    ├── README.md
    ├── buenavista
    ├── dev-requirements.txt
    ├── docker
    ├── setup.py
    └── tests
```

### 📑 Project Index

<details open>
	<summary><b><code>BUENAVISTA/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/jwills/buenavista/blob/master/dev-requirements.txt'>dev-requirements.txt</a></b></td>
				<td>Enables project dependencies for database connectivity, API development, and testing.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/jwills/buenavista/blob/master/setup.py'>setup.py</a></b></td>
				<td>Define package metadata and dependencies for the Buenavista project using setup.py.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- docker Submodule -->
		<summary><b>docker</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/jwills/buenavista/blob/master/docker/download_data.sh'>download_data.sh</a></b></td>
				<td>Download example data files (iris.parquet and chinook.db) to the ./data directory using curl commands.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/jwills/buenavista/blob/master/docker/Dockerfile'>Dockerfile</a></b></td>
				<td>- Builds a Docker image for a Python application, setting up necessary environment variables, dependencies, and configurations<br>- The Dockerfile defines the image's structure, installs dependencies, copies project files, and specifies the entry point to run the application.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/jwills/buenavista/blob/master/docker/Makefile'>Makefile</a></b></td>
				<td>Facilitates building, running, and setting up example data for the Buenavista project using Docker and Docker Compose.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/jwills/buenavista/blob/master/docker/docker-compose.yml'>docker-compose.yml</a></b></td>
				<td>Defines services and configurations for Docker containers in the project, specifying images and ports for CloudBeaver and Buenavista services.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- buenavista Submodule -->
		<summary><b>buenavista</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/jwills/buenavista/blob/master/buenavista/bv_dialects.py'>bv_dialects.py</a></b></td>
				<td>- Enhances SQL dialects in the codebase by introducing custom functions and modifications for Postgres, Trino, and DuckDB<br>- Includes a new function for ISO8601 conversion, Trino keyword additions, and DuckDB command handling<br>- Improves query generation and transformation capabilities for specific dialects.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/jwills/buenavista/blob/master/buenavista/core.py'>core.py</a></b></td>
				<td>- Defines core classes for representing query results and managing database connections, ensuring seamless interaction with upstream data sources<br>- The code establishes a structured framework for handling query results and session management within the project's architecture.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/jwills/buenavista/blob/master/buenavista/postgres.py'>postgres.py</a></b></td>
				<td>- The `buenavista/postgres.py` file in the project architecture defines server responses in the PG wire protocol and maps type OIDs to their corresponding data types<br>- This code file plays a crucial role in handling communication between the application and the PostgreSQL database, ensuring proper interpretation of server responses and data types.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/jwills/buenavista/blob/master/buenavista/rewrite.py'>rewrite.py</a></b></td>
				<td>Enables rewriting SQL queries based on defined relations, transforming expressions to match specified sources.</td>
			</tr>
			</table>
			<details>
				<summary><b>backends</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/jwills/buenavista/blob/master/buenavista/backends/postgres.py'>postgres.py</a></b></td>
						<td>- Enables PostgreSQL database interaction through a session-based approach, facilitating SQL execution, result handling, and DataFrame loading<br>- The code defines query result structures, session management, and connection handling for seamless database operations within the project's architecture.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/jwills/buenavista/blob/master/buenavista/backends/duckdb.py'>duckdb.py</a></b></td>
						<td>Converts DuckDB data types to Buenavista types and provides classes for handling query results and sessions within the DuckDB backend.</td>
					</tr>
					</table>
				</blockquote>
			</details>
			<details>
				<summary><b>http</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/jwills/buenavista/blob/master/buenavista/http/type_mapping.py'>type_mapping.py</a></b></td>
						<td>- Defines type mappings and converters for Buenavista data types, facilitating conversion to Trino-compatible types<br>- The code establishes mappings between Buenavista types and Trino types, along with conversion functions for specific types<br>- This enables seamless translation of Buenavista data types to Trino-compatible representations within the codebase architecture.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/jwills/buenavista/blob/master/buenavista/http/context.py'>context.py</a></b></td>
						<td>- Manages HTTP request context, handles session pooling, and executes SQL queries based on request headers<br>- Facilitates connection management and transaction handling within the codebase architecture.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/jwills/buenavista/blob/master/buenavista/http/schemas.py'>schemas.py</a></b></td>
						<td>- Defines Pydantic models for representing query results and errors in a Presto HTTP client<br>- The models handle data transformation and alias generation, ensuring compatibility with the Presto API.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/jwills/buenavista/blob/master/buenavista/http/main.py'>main.py</a></b></td>
						<td>- The code in buenavista/http/main.py defines endpoints for retrieving system information and executing SQL statements via HTTP requests<br>- It handles query execution, error handling, and response formatting, integrating with various extensions and a query rewriter<br>- The code contributes to the project's architecture by providing a crucial interface for interacting with the system.</td>
					</tr>
					</table>
				</blockquote>
			</details>
			<details>
				<summary><b>examples</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/jwills/buenavista/blob/master/buenavista/examples/duckdb_postgres.py'>duckdb_postgres.py</a></b></td>
						<td>- Implements a rewriter for DuckDB to PostgreSQL queries, enabling seamless compatibility between the two database systems<br>- The code establishes a BuenaVista server using DuckDB, with the ability to rewrite specific queries for PostgreSQL compatibility<br>- It also handles server setup and shutdown based on environment variables or user input.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/jwills/buenavista/blob/master/buenavista/examples/duckdb_http.py'>duckdb_http.py</a></b></td>
						<td>- Implements a FastAPI server using DuckDB for Buenavista, providing HTTP endpoints for JDBC metadata queries<br>- Handles DuckDB setup, connects to the database, and runs the FastAPI app on a specified host and port<br>- Rewrites SQL queries using a custom rewriter for DuckDB dialects.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/jwills/buenavista/blob/master/buenavista/examples/postgres_proxy.py'>postgres_proxy.py</a></b></td>
						<td>- Facilitates proxying PostgreSQL connections through Buenavista, enabling seamless communication with a PostgreSQL database<br>- The code establishes a BuenaVistaServer instance, connecting to a PostgreSQL database on localhost:5432, and listens for incoming connections on localhost:5433.</td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<details> <!-- .github Submodule -->
		<summary><b>.github</b></summary>
		<blockquote>
			<details>
				<summary><b>workflows</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/jwills/buenavista/blob/master/.github/workflows/push.yaml'>push.yaml</a></b></td>
						<td>- Automates Docker image building and pushing to ghcr.io upon push to the main branch<br>- Handles metadata, QEMU setup, Docker Buildx, and Container Registry login<br>- Uses GitHub Actions for seamless integration within the project's CI/CD pipeline.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/jwills/buenavista/blob/master/.github/workflows/main.yml'>main.yml</a></b></td>
						<td>- Automates running unit tests on pull requests for the Buena Vista project<br>- Uses GitHub Actions to set up Python environments, install dependencies, and execute tests across multiple Python versions<br>- Ensures code quality and functionality are maintained before merging changes into the main branch.</td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---

## 🚀 Getting Started

### 🔧 Prerequisites

Before you begin, ensure your system meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip
- **Container Runtime:** Docker


### ⚙️ Installation

Install `buenavista` using one of the following methods:

**Build from source:**

1. Clone the buenavista repository:

```sh
❯ git clone https://github.com/jwills/buenavista
```

2. Navigate to the project directory:

```sh
❯ cd buenavista
```

3. Install the project dependencies:

**With `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r dev-requirements.txt
```
**With `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker build -t <image_name> .
```



### 📓 Usage

**With `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python <entrypoint>
```
**With `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker run -it <image_name>
```

### 🧪 Testing

**With `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```

---

## 🎯 Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🤝 Contributing

- **💬 [Join the Discussions](https://github.com/jwills/buenavista/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/jwills/buenavista/issues)**: Submit bugs found or log feature requests for the `buenavista` project.
- **💡 [Submit Pull Requests](https://github.com/jwills/buenavista/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/jwills/buenavista
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
   <a href="https://github.com{/jwills/buenavista/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=jwills/buenavista">
   </a>
</p>
</details>

---

## 📜 License

Buenavista is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 🌟 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---
    