<div id="top">

<!-- HEADER STYLE: CLASSIC -->
<div align="center">

<img src="../../../../../../readmeai/assets/logos/blue.svg" width="30%" style="position: relative; top: 0; right: 0;" alt="Project Logo"/>

# BUENAVISTA

<em>Transforming data access with seamless query rewriting.</em>

<!-- BADGES -->
<img src="https://img.shields.io/github/license/jwills/buenavista?style=flat&logo=opensourceinitiative&logoColor=white&color=0d47a1" alt="license">
<img src="https://img.shields.io/github/last-commit/jwills/buenavista?style=flat&logo=git&logoColor=white&color=0d47a1" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/jwills/buenavista?style=flat&color=0d47a1" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/jwills/buenavista?style=flat&color=0d47a1" alt="repo-language-count">

<em>Technology Stack:</em>

<img src="https://img.shields.io/badge/DuckDB-FFF000.svg?style=flat&logo=DuckDB&logoColor=black" alt="DuckDB">
<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=flat&logo=FastAPI&logoColor=white" alt="FastAPI">
<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat&logo=Pytest&logoColor=white" alt="Pytest">
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white" alt="Docker">
<br>
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=flat&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions">
<img src="https://img.shields.io/badge/PostgreSQL-4169E1.svg?style=flat&logo=PostgreSQL&logoColor=white" alt="PostgreSQL">
<img src="https://img.shields.io/badge/Pydantic-E92063.svg?style=flat&logo=Pydantic&logoColor=white" alt="Pydantic">
<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat&logo=YAML&logoColor=white" alt="YAML">

</div>
<br>

---

## ⚛️ Table of Contents

- [⚛ ️ Table of Contents](#-table-of-contents)
- [🔮 Overview](#-overview)
- [💫 Features](#-features)
- [⭐ Project Structure](#-project-structure)
    - [✨ Project Index](#-project-index)
- [🌟 Getting Started](#-getting-started)
    - [💠 Prerequisites](#-prerequisites)
    - [🔷 Installation](#-installation)
    - [🔸 Usage](#-usage)
    - [✴ ️ Testing](#-testing)
- [⚡ Roadmap](#-roadmap)
- [🌀 Contributing](#-contributing)
- [💫 License](#-license)
- [✧ Acknowledgments](#-acknowledgments)

---

## 🔮 Overview

Introducing Buenavista, a versatile developer tool designed to streamline SQL query management and enhance database interactions.

**Why Buenavista?**

This project simplifies project setup and maintenance, offering customizable proxy options for tailored database interactions. Key features include:

- **🔥 Seamless Dependency Management:** Simplify project setup and maintenance.
- **💡 Customizable Proxy Options:** Tailor database interactions to specific project needs.
- **🐳 Docker Support:** Effortlessly manage data, images, and services within containers.
- **⚙️ Enhanced SQL Dialects:** Optimize query generation and transformation capabilities.

---

## 💫 Features

|      | Component       | Details                              |
| :--- | :-------------- | :----------------------------------- |
| ⚙️  | **Architecture**  | <ul><li>Follows a modular microservices architecture.</li><li>Uses FastAPI for RESTful APIs.</li><li>Utilizes Docker for containerization.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Consistent code style and formatting.</li><li>Includes unit tests using Pytest.</li><li>Uses type hinting with Pydantic for data validation.</li></ul> |
| 📄 | **Documentation** | <ul><li>Comprehensive documentation using Python docstrings.</li><li>Includes Dockerfile and docker-compose.yml setup guides.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integrated with GitHub Actions for CI/CD workflows.</li><li>Uses psycopg for PostgreSQL database integration.</li><li>Utilizes pyarrow for efficient data serialization.</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Codebase organized into separate modules for clear separation of concerns.</li><li>Follows SOLID principles for maintainability.</li></ul> |
| 🧪 | **Testing**       | <ul><li>Includes unit tests covering core functionalities.</li><li>Uses fixtures and mocks for effective testing.</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Optimized performance using async/await with FastAPI.</li><li>Efficient data processing with pyarrow and duckdb.</li></ul> |
| 🛡️ | **Security**      | <ul><li>Follows best practices for secure coding.</li><li>Uses psycopg-pool for secure connection pooling.</li></ul> |
| 📦 | **Dependencies**  | <ul><li>Dependencies managed using pip and listed in dev-requirements.txt.</li><li>Includes libraries like pyarrow, pydantic, and fastapi.</li></ul> |

---

## ⭐ Project Structure

```sh
└── buenavista/
    ├── .github
    │   └── workflows
    │       ├── main.yml
    │       └── push.yaml
    ├── LICENSE
    ├── README.md
    ├── buenavista
    │   ├── __init__.py
    │   ├── backends
    │   │   ├── __init__.py
    │   │   ├── duckdb.py
    │   │   └── postgres.py
    │   ├── bv_dialects.py
    │   ├── core.py
    │   ├── examples
    │   │   ├── duckdb_http.py
    │   │   ├── duckdb_postgres.py
    │   │   └── postgres_proxy.py
    │   ├── http
    │   │   ├── __init__.py
    │   │   ├── context.py
    │   │   ├── main.py
    │   │   ├── schemas.py
    │   │   └── type_mapping.py
    │   ├── postgres.py
    │   └── rewrite.py
    ├── dev-requirements.txt
    ├── docker
    │   ├── Dockerfile
    │   ├── Makefile
    │   ├── README.md
    │   ├── connection.png
    │   ├── docker-compose.yml
    │   └── download_data.sh
    ├── setup.py
    └── tests
        ├── functional
        │   └── duckdb
        │       ├── test_http.py
        │       └── test_postgres.py
        └── unit
            ├── postgres
            │   ├── test_bv_buffer.py
            │   ├── test_bv_context.py
            │   └── test_handler.py
            ├── test_core.py
            └── test_rewrite.py
```

### ✨ Project Index

<details open>
	<summary><b><code>BUENAVISTA/</code></b></summary>
	<!-- __root__ Submodule -->
	<details>
		<summary><b>__root__</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ __root__</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jwills/buenavista/blob/master/dev-requirements.txt'>dev-requirements.txt</a></b></td>
					<td style='padding: 8px;'>Define and manage project dependencies for seamless integration.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jwills/buenavista/blob/master/setup.py'>setup.py</a></b></td>
					<td style='padding: 8px;'>- Define package metadata and dependencies for Buenavista, a programmable Presto and Postgres proxy<br>- Include author info, package version, description, and dependencies like FastAPI and Pydantic<br>- Additional options for DuckDB and Postgres are available<br>- Find and include Buenavista packages for installation.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- docker Submodule -->
	<details>
		<summary><b>docker</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ docker</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jwills/buenavista/blob/master/docker/download_data.sh'>download_data.sh</a></b></td>
					<td style='padding: 8px;'>- Download example data files (iris.parquet and chinook.db) to the./data directory using curl commands<br>- The script creates the data directory, downloads the files, and unzips the chinook.db file.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jwills/buenavista/blob/master/docker/Dockerfile'>Dockerfile</a></b></td>
					<td style='padding: 8px;'>- Create a Docker image for a Python application, setting up the environment, installing dependencies, and configuring the timezone<br>- The image exposes port 5433 and defines an entry point to run a specific Python module.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jwills/buenavista/blob/master/docker/Makefile'>Makefile</a></b></td>
					<td style='padding: 8px;'>Facilitates building, running, and setting up example data for the Buenavista project using Docker and Docker Compose.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jwills/buenavista/blob/master/docker/docker-compose.yml'>docker-compose.yml</a></b></td>
					<td style='padding: 8px;'>Define services and their configurations in the docker-compose.yml file to orchestrate cloudbeaver and buenavista containers for seamless deployment and management within the project architecture.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- buenavista Submodule -->
	<details>
		<summary><b>buenavista</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ buenavista</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jwills/buenavista/blob/master/buenavista/bv_dialects.py'>bv_dialects.py</a></b></td>
					<td style='padding: 8px;'>- Enhances SQL dialects for DuckDB, Postgres, and Trino by adding custom functions, tokenizers, parsers, and command handlers<br>- Provides additional expressions like <code>ToISO8601</code> and modifies Trino and DuckDB behaviors for specific commands<br>- Improves query generation and transformation capabilities within the SQL dialects.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jwills/buenavista/blob/master/buenavista/core.py'>core.py</a></b></td>
					<td style='padding: 8px;'>- Defines core classes for representing query results, sessions, and connections in the Buenavista project<br>- Handles translation between data sources and Buenavista query results<br>- Includes methods for creating sessions, executing SQL queries, and checking JSON payloads.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jwills/buenavista/blob/master/buenavista/postgres.py'>postgres.py</a></b></td>
					<td style='padding: 8px;'>- SummaryThe <code>buenavista/postgres.py</code> file in the project is responsible for handling server responses in the PG wire protocol<br>- It defines byte codes for various server responses and includes type mappings for different data types used in Postgres<br>- This file plays a crucial role in managing communication with the Postgres database server and interpreting the responses received, contributing to the overall functionality and reliability of the system.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jwills/buenavista/blob/master/buenavista/rewrite.py'>rewrite.py</a></b></td>
					<td style='padding: 8px;'>- Rewrite SQL queries by transforming table references into subqueries based on predefined relations<br>- The code in <code>buenavista/rewrite.py</code> defines a <code>Rewriter</code> class that parses and rewrites SQL statements using specified dialects<br>- It allows for customizing query transformations through decorators, enhancing query flexibility and modularity within the project architecture.</td>
				</tr>
			</table>
			<!-- backends Submodule -->
			<details>
				<summary><b>backends</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ buenavista.backends</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jwills/buenavista/blob/master/buenavista/backends/postgres.py'>postgres.py</a></b></td>
							<td style='padding: 8px;'>- Implement a PostgreSQL backend for Buenavista, offering query execution and DataFrame loading capabilities<br>- The code defines classes for query results, sessions, and connections, enabling seamless interaction with the database.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jwills/buenavista/blob/master/buenavista/backends/duckdb.py'>duckdb.py</a></b></td>
							<td style='padding: 8px;'>- Converts DuckDB data types to Buenavista types, provides an iterator for RecordBatch data, and defines classes for handling query results and sessions<br>- Implements SQL rewrites for compatibility and manages transactions<br>- The code enhances data type handling and query execution within the DuckDB backend, ensuring seamless integration with Buenavistas architecture.</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- http Submodule -->
			<details>
				<summary><b>http</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ buenavista.http</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jwills/buenavista/blob/master/buenavista/http/type_mapping.py'>type_mapping.py</a></b></td>
							<td style='padding: 8px;'>- Define type mappings and conversion functions for various data types in the projects architecture<br>- Map Buenavista types to Trino types and provide conversion functions for specific types<br>- This file plays a crucial role in ensuring seamless data type handling and compatibility within the codebase.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jwills/buenavista/blob/master/buenavista/http/context.py'>context.py</a></b></td>
							<td style='padding: 8px;'>- Manage HTTP request context, session pooling, and headers for connections<br>- Acquire and release sessions, execute SQL queries, and handle transaction IDs<br>- Ensure proper session closure and provide access to session and header information.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jwills/buenavista/blob/master/buenavista/http/schemas.py'>schemas.py</a></b></td>
							<td style='padding: 8px;'>- Define data models for HTTP schemas with camelCase aliasing and populate by name configuration<br>- Includes models for client type signatures, columns, statement stats, query errors, warnings, and query results with detailed stats and error handling.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jwills/buenavista/blob/master/buenavista/http/main.py'>main.py</a></b></td>
							<td style='padding: 8px;'>- Define an HTTP service with endpoints for retrieving system info and executing SQL statements<br>- It handles incoming requests, processes queries asynchronously, and returns results in a structured format<br>- The service manages connections, extensions, and query rewriting, ensuring efficient query execution and error handling.</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- examples Submodule -->
			<details>
				<summary><b>examples</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ buenavista.examples</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jwills/buenavista/blob/master/buenavista/examples/duckdb_postgres.py'>duckdb_postgres.py</a></b></td>
							<td style='padding: 8px;'>- Rewrite SQL queries for DuckDB to mimic PostgreSQL behavior<br>- Create a BuenaVista server using DuckDB as the backend, with a custom rewriter for specific queries<br>- The server listens on a specified host and port, utilizing environment variables if available.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jwills/buenavista/blob/master/buenavista/examples/duckdb_http.py'>duckdb_http.py</a></b></td>
							<td style='padding: 8px;'>- The code file <code>duckdb_http.py</code> sets up a FastAPI app with DuckDB connections for a Presto API<br>- It defines rewriters for various JDBC-related queries and runs the app using uvicorn<br>- The file facilitates querying and interacting with DuckDB databases via HTTP endpoints.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jwills/buenavista/blob/master/buenavista/examples/postgres_proxy.py'>postgres_proxy.py</a></b></td>
							<td style='padding: 8px;'>- Create a PostgreSQL proxy server that listens on a specified address and forwards requests to a PostgreSQL database<br>- The server utilizes BuenaVistaServer and PGConnection classes to handle connections and serve incoming requests.</td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<!-- .github Submodule -->
	<details>
		<summary><b>.github</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ .github</b></code>
			<!-- workflows Submodule -->
			<details>
				<summary><b>workflows</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ .github.workflows</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jwills/buenavista/blob/master/.github/workflows/push.yaml'>push.yaml</a></b></td>
							<td style='padding: 8px;'>- Automates Docker image pushing to ghcr.io upon workflow trigger<br>- Utilizes metadata for versioning and tagging<br>- Handles QEMU setup, Docker Buildx configuration, and Container Registry login<br>- Executes Docker build and push actions with caching optimizations<br>- Enhances CI/CD pipeline efficiency for the project.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jwills/buenavista/blob/master/.github/workflows/main.yml'>main.yml</a></b></td>
							<td style='padding: 8px;'>- Ensure Buena Vista Unit Tests run smoothly on pull requests to the main branch<br>- Set up Python versions 3.10, 3.11, and 3.12, install dependencies, and execute tests using pytest.</td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---

## 🌟 Getting Started

### 💠 Prerequisites

This project requires the following dependencies:

- **Programming Language:** Python
- **Package Manager:** Pip
- **Container Runtime:** Docker

### 🔷 Installation

Build buenavista from the source and intsall dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/jwills/buenavista
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd buenavista
    ```

3. **Install the dependencies:**

<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![docker][docker-shield]][docker-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [docker-shield]: https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white -->
	<!-- [docker-link]: https://www.docker.com/ -->

	**Using [docker](https://www.docker.com/):**

	```sh
	❯ docker build -t jwills/buenavista .
	```
<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![pip][pip-shield]][pip-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [pip-shield]: https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white -->
	<!-- [pip-link]: https://pypi.org/project/pip/ -->

	**Using [pip](https://pypi.org/project/pip/):**

	```sh
	❯ pip install -r dev-requirements.txt
	```


### 🔸 Usage

Run the project with:

**Using [docker](https://www.docker.com/):**
```sh
docker run -it {image_name}
```
**Using [pip](https://pypi.org/project/pip/):**
```sh
python {entrypoint}
```

### ✴️ Testing

Buenavista uses the {__test_framework__} test framework. Run the test suite with:

**Using [pip](https://pypi.org/project/pip/):**
```sh
pytest
```


---

## ⚡ Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🌀 Contributing

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

## 💫 License

Buenavista is protected under the [LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## ✧ Acknowledgments

- Credit `contributors`, `inspiration`, `references`, etc.

<div align="left"><a href="#top">⬆ Return</a></div>

---

<!-- README-AI COMMAND: -->
<!--
```sh
readmeai \
    --repository 'https://github.com/jwills/buenavista' \
    --output 'docs/docs/examples/generated/tmp/readme-buenavista.md' \
    --badge-style 'flat' \
    --badge-color '0d47a1' \
    --logo 'BLUE' \
    --header-style 'CLASSIC' \
    --navigation-style 'BULLET' \
    --emojis 'atomic' \
    --temperature 0.143 \
    --tree-max-depth 5 \
    --api openai
```
-->
