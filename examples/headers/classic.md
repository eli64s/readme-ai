<p align="center">
    <img src="https://cdn-icons-png.flaticon.com/512/6295/6295417.png" align="center" width="30%">
</p>
<p align="center"><h1 align="center">BUENAVISTA</h1></p>
<p align="center">
	<em>Elevating data processing and API excellence.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/jwills/buenavista?style=flat-square&logo=opensourceinitiative&logoColor=white&color=skyblue" alt="license">
	<img src="https://img.shields.io/github/last-commit/jwills/buenavista?style=flat-square&logo=git&logoColor=white&color=skyblue" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/jwills/buenavista?style=flat-square&color=skyblue" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/jwills/buenavista?style=flat-square&color=skyblue" alt="repo-language-count">
</p>
<p align="center">Tech Stack</p>
<p align="center">
	<img src="https://img.shields.io/badge/DuckDB-FFF000.svg?style=flat-square&logo=DuckDB&logoColor=black" alt="DuckDB">
	<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat-square&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
	<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=flat-square&logo=FastAPI&logoColor=white" alt="FastAPI">
	<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat-square&logo=Pytest&logoColor=white" alt="Pytest">
	<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat-square&logo=Docker&logoColor=white" alt="Docker">
	<br>
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=flat-square&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions">
	<img src="https://img.shields.io/badge/PostgreSQL-4169E1.svg?style=flat-square&logo=PostgreSQL&logoColor=white" alt="PostgreSQL">
	<img src="https://img.shields.io/badge/Pydantic-E92063.svg?style=flat-square&logo=Pydantic&logoColor=white" alt="Pydantic">
</p>
<br>

##  Table of Contents

- [ Overview](#-overview)
- [ Features](#-features)
- [ Project Structure](#-project-structure)
  - [ Project Index](#-project-index)
- [ Getting Started](#-getting-started)
  - [ Prerequisites](#-prerequisites)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Testing](#-testing)
- [ Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

---

##  Overview

BuenaVista is a versatile open-source project that streamlines fast data processing and API development. With enhanced SQL dialects for DuckDB, Postgres, and Trino, it enables seamless integration and efficient query handling. Targeting developers seeking efficient data querying and web service creation, BuenaVista offers a robust solution for building scalable data-driven applications.

---

##  Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Enables **FastAPI** for efficient API development.</li><li>Utilizes **DuckDB** for fast data processing.</li><li>Custom SQL dialect support for **Postgres** and **Trino**.</li><li>Facilitates seamless integration with **Python** and **SQL** technologies.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Follows PEP 8 standards for Python code.</li><li>Includes comprehensive unit tests using **pytest**.</li><li>Uses **pydantic** for data validation and schema creation.</li><li>Maintains clear and concise code documentation.</li></ul> |
| 📄 | **Documentation** | <ul><li>Well-documented codebase with inline comments and docstrings.</li><li>Includes a detailed **`dev-requirements.txt`** file specifying project dependencies.</li><li>Provides installation instructions using **`pip`** and **`docker`** with clear commands.</li><li>Documentation available for Docker setup and usage.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integrates seamlessly with **GitHub Actions** for CI/CD workflows.</li><li>Supports integration with **PostgreSQL** and **Trino** databases.</li><li>Utilizes **FastAPI** for handling HTTP requests and responses.</li><li>Implements **Docker** for containerization and deployment.</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Modular structure with separate files for different functionalities.</li><li>Encapsulates backend logic in **`buenavista/backends`** package.</li><li>Defines clear interfaces for handling sessions, query results, and data sources.</li><li>Separates HTTP endpoints logic in **`buenavista/http`** package.</li></ul> |
| 🧪 | **Testing**       | <ul><li>Comprehensive unit tests covering core functionalities.</li><li>Includes test fixtures for setup and teardown operations.</li><li>Utilizes **pytest** for running tests and generating reports.</li><li>Tests HTTP endpoints, SQL query execution, and data conversion.</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Leverages **DuckDB** for fast in-memory data processing.</li><li>Optimizes SQL query execution for efficient data retrieval.</li><li>Utilizes connection pooling for improved database performance.</li><li>Ensures minimal latency in handling HTTP requests.</li></ul> |
| 🛡️ | **Security**      | <ul><li>Implements secure database connections with **Postgres** and **DuckDB**.</li><li>Handles user input validation to prevent SQL injection attacks.</li><li>Follows best practices for securing Docker containers.</li><li>Ensures data privacy and integrity during HTTP transactions.</li></ul> |

---

##  Project Structure

```sh
└── buenavista/
    ├── .github
    │   └── workflows
    ├── LICENSE
    ├── README.md
    ├── buenavista
    │   ├── __init__.py
    │   ├── backends
    │   ├── bv_dialects.py
    │   ├── core.py
    │   ├── examples
    │   ├── http
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
        └── unit
```


###  Project Index
<details open>
	<summary><b><code>BUENAVISTA/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/jwills/buenavista/blob/master/dev-requirements.txt'>dev-requirements.txt</a></b></td>
				<td>- Enables fast data processing and API development by specifying necessary dependencies<br>- It facilitates seamless integration of DuckDB, FastAPI, psycopg, psycopg-pool, and others for efficient data querying and web service creation within the project architecture.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/jwills/buenavista/blob/master/setup.py'>setup.py</a></b></td>
				<td>- Define and configure project metadata for Buenavista, including package name, version, description, authorship details, and dependencies<br>- This setup file enables seamless integration and distribution of the project, ensuring correct attribution, documentation, and installation of required components.</td>
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
				<td>Download example data (iris.parquet and chinook.db) to the ./data directory using curl commands.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/jwills/buenavista/blob/master/docker/Dockerfile'>Dockerfile</a></b></td>
				<td>- Facilitates building and running Python applications within a Docker container<br>- Sets up necessary environment variables, installs dependencies, configures time zone, and specifies entry point for the application<br>- This file aids in creating a consistent and reproducible environment for deploying the project.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/jwills/buenavista/blob/master/docker/Makefile'>Makefile</a></b></td>
				<td>- The Makefile in the docker directory facilitates building the Docker image for the project and orchestrating Docker containers<br>- It streamlines tasks like building the image, starting containers, and downloading example data<br>- This file plays a crucial role in managing the project's Docker-related operations.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/jwills/buenavista/blob/master/docker/docker-compose.yml'>docker-compose.yml</a></b></td>
				<td>Define Docker services for cloud-based development environment with CloudBeaver and Buenavista, ensuring seamless integration and accessibility.</td>
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
				<td>- Enhances SQL dialects for DuckDB, Postgres, and Trino, enabling custom functions, token handling, and command transformations<br>- Modifies Trino with keywords and functions, extends Postgres, and tailors DuckDB command handling<br>- Improves DuckDB's generator with custom transforms for expressions like CurrentTimestamp and ToISO8601, ensuring accurate SQL generation.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/jwills/buenavista/blob/master/buenavista/core.py'>core.py</a></b></td>
				<td>- Defines core classes for representing query results, managing sessions, and translating data sources<br>- Implements methods for executing SQL queries, handling sessions, and checking JSON validity<br>- Facilitates interaction between data sources and query results within the project architecture.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/jwills/buenavista/blob/master/buenavista/postgres.py'>postgres.py</a></b></td>
				<td>- The code file buenavista/postgres.py provides functionality for handling server responses in the PG wire protocol<br>- It includes byte codes for various responses such as authentication requests, data rows, error responses, and more<br>- This code file plays a crucial role in managing communication between the project and a PostgreSQL database server, ensuring smooth interaction and data exchange.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/jwills/buenavista/blob/master/buenavista/rewrite.py'>rewrite.py</a></b></td>
				<td>- Enables SQL query rewriting based on defined relations<br>- Parses and transforms SQL expressions using specified dialects for reading and writing<br>- Supports custom relation definitions for subquery generation<br>- Allows for seamless integration with Presto and DuckDB dialects.</td>
			</tr>
			</table>
			<details>
				<summary><b>backends</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/jwills/buenavista/blob/master/buenavista/backends/postgres.py'>postgres.py</a></b></td>
						<td>- Facilitates PostgreSQL interactions, defining QueryResult and Session classes for managing data retrieval and connections<br>- Implements functions for executing SQL queries, loading data into DataFrames, and handling transactions within the database<br>- The PGConnection class manages connection pooling and session creation, ensuring efficient communication with the PostgreSQL server.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/jwills/buenavista/blob/master/buenavista/backends/duckdb.py'>duckdb.py</a></b></td>
						<td>- The code file in buenavista/backends/duckdb.py handles DuckDB data types, query results, and session management for the project's DuckDB connection<br>- It converts Arrow data types to Buenavista types, processes query results, and manages SQL execution within a transactional context.</td>
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
						<td>- Defines type mappings and converters for different data types in the Buenavista project, facilitating the conversion of types to Trino-compatible formats<br>- The code file `type_mapping.py` contains functions to handle various data types and their representations in the project, ensuring seamless data type conversion within the codebase architecture.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/jwills/buenavista/blob/master/buenavista/http/context.py'>context.py</a></b></td>
						<td>- Facilitates request handling, session management, and SQL execution within the project context<br>- Manages headers, session pools, and transaction IDs for efficient interaction with external data sources<br>- Enables execution of SQL queries and handles transaction lifecycle while maintaining session integrity.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/jwills/buenavista/blob/master/buenavista/http/schemas.py'>schemas.py</a></b></td>
						<td>- Defines data models for handling HTTP responses in a camel-case format, enhancing readability and consistency across the codebase<br>- This schema file organizes structures for client types, columns, statement statistics, query errors, warnings, and result handling for efficient data processing and error management in the project architecture.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/jwills/buenavista/blob/master/buenavista/http/main.py'>main.py</a></b></td>
						<td>- Implements HTTP endpoints to execute SQL queries, returning results in Buenavista's backend system<br>- Handles query execution, result conversion, and error handling<br>- Enables clients to interact with the system through a RESTful API, providing information on the system's status and executing SQL statements.</td>
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
						<td>- Rewrite SQL queries for PostgreSQL compatibility using DuckDB, enabling seamless integration with BuenaVista servers<br>- This code file creates a server instance with rewriter support, allowing users to interact with DuckDB databases via the BuenaVista platform effortlessly.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/jwills/buenavista/blob/master/buenavista/examples/duckdb_http.py'>duckdb_http.py</a></b></td>
						<td>- Enables rewriting and serving HTTP queries using FastAPI, DuckDB, and Buenavista's custom dialects<br>- Handles requests for JDBC metadata like tables, schemas, and columns<br>- Supports running DuckDB in-memory or from a file<br>- Integrates with Buenavista's Presto API for query processing.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/jwills/buenavista/blob/master/buenavista/examples/postgres_proxy.py'>postgres_proxy.py</a></b></td>
						<td>- The code file establishes a proxy server to handle PostgreSQL connections<br>- It configures a BuenaVista server to listen on a specific address and port, forwarding requests to a PostgreSQL database<br>- The file plays a critical role in the project's architecture by enabling communication between clients and the database through a proxy mechanism.</td>
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
						<td>Automate the Docker image build and push process to ghcr.io based on branch updates.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/jwills/buenavista/blob/master/.github/workflows/main.yml'>main.yml</a></b></td>
						<td>- Automates unit testing for Buena Vista app on GitHub<br>- Runs tests on PRs to main branch using multiple Python versions<br>- Installs dependencies, sets up Python environment, and executes tests with pytest.</td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---
##  Getting Started

###  Prerequisites

Before getting started with buenavista, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip
- **Container Runtime:** Docker


###  Installation

Install buenavista using one of the following methods:

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


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r dev-requirements.txt
```


**Using `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker build -t jwills/buenavista .
```




###  Usage
Run buenavista using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```


**Using `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker run -it {image_name}
```


###  Testing
Run the test suite using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```


---
##  Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

##  Contributing

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

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---
