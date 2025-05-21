<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">BUENAVISTA</h1>
</p>
<p align="center">
    <em>Unlock Data Power with Buenavista-Dive Deeper!</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/jwills/buenavista?style=flat&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/jwills/buenavista?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/jwills/buenavista?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/jwills/buenavista?style=flat&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/DuckDB-FFF000.svg?style=flat&logo=DuckDB&logoColor=black" alt="DuckDB">
	<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
	<img src="https://img.shields.io/badge/Pydantic-E92063.svg?style=flat&logo=Pydantic&logoColor=white" alt="Pydantic">
	<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat&logo=YAML&logoColor=white" alt="YAML">
	<img src="https://img.shields.io/badge/PostgreSQL-4169E1.svg?style=flat&logo=PostgreSQL&logoColor=white" alt="PostgreSQL">
	<br>
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white" alt="Docker">
	<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=flat&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions">
	<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat&logo=Pytest&logoColor=white" alt="Pytest">
	<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=flat&logo=FastAPI&logoColor=white" alt="FastAPI">
</p>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>

- [ Overview](#-overview)
- [ Features](#-features)
- [ Repository Structure](#-repository-structure)
- [ Modules](#-modules)
- [ Getting Started](#-getting-started)
  - [ Install](#-install)
  - [ Using buenavista](#-using-buenavista)
  - [ Tests](#-tests)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)
</details>
<hr>

##  Overview

Buenavista is a versatile project offering programmable proxies for Presto and Postgres databases. With a focus on efficient database operations, it provides enhanced SQL dialects, data rewriting, and connection pooling capabilities. The project's core functionality includes querying and processing data, managing sessions, connections, and extensions. Buenavista simplifies SQL transformation between different databases, facilitates query execution via FastAPI endpoints, and supports DuckDB connections alongside PostgreSQL. Automated CI/CD workflows streamline development processes, ensuring code quality and deployment efficiency.

---

##  Features

|    |    Feature        | Description                                                                                                                 |
|----|-------------------|---------------------------------------------------------------                                                              |
| ⚙️  | **Architecture**  | Buenavista follows a modular architecture with core functionality in separate modules like `core`, `postgres`, and `duckdb`.  |
| 🔩 | **Code Quality**  | The codebase maintains high quality with detailed comments, consistent styling, and adherence to PEP standards.              |
| 📄 | **Documentation** | Extensive documentation is available, explaining core functionality, setup processes, and examples for easy understanding.  |
| 🔌 | **Integrations**  | Key dependencies include `pytest`, `psycopg-pool`, `fastapi`, and `pydantic`, enhancing functionality and performance.         |
| 🧩 | **Modularity**    | Buenavista codebase exhibits strong modularity, enabling easy reusability of components for different use cases.             |
| 🧪 | **Testing**       | Testing frameworks like `pytest` are used for comprehensive test coverage, ensuring code reliability and stability.          |
| ⚡️  | **Performance**   | Buenavista is designed for efficiency, ensuring fast query execution and optimized resource usage for improved performance.  |
| 🛡️ | **Security**      | Security measures include data protection via session management and access control through HTTP headers for connections. |
| 📦 | **Dependencies**  | Key dependencies include `psycopg-pool`, `fastapi`, `pyarrow`, and `sqlglot`, enhancing functionality and database interactions. |

---

##  Repository Structure

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

---

##  Modules

<details closed><summary>.</summary>

| File                                                                                          | Summary                                                                                                     |
| ---                                                                                           | ---                                                                                                         |
| [dev-requirements.txt](https://github.com/jwills/buenavista/blob/master/dev-requirements.txt) | Implements database connection pooling for Buenavista using psycopg-pool for efficient database operations. |
| [setup.py](https://github.com/jwills/buenavista/blob/master/setup.py)                         | Programmable Presto and Postgres proxies setup configuration for Buenavista repository.                     |

</details>

<details closed><summary>docker</summary>

| File                                                                                             | Summary                                                                                                                                                                    |
| ---                                                                                              | ---                                                                                                                                                                        |
| [download_data.sh](https://github.com/jwills/buenavista/blob/master/docker/download_data.sh)     | Download example data files (iris.parquet, chinook.db) into./data directory for Buenavista repository's docker environment setup.                                          |
| [Dockerfile](https://github.com/jwills/buenavista/blob/master/docker/Dockerfile)                 | Dockerfile setting up a Python environment for the Buenavista repository, installing dependencies, setting timezone, and launching a specific script on container startup. |
| [Makefile](https://github.com/jwills/buenavista/blob/master/docker/Makefile)                     | Build, start, and fetch data for Buenavista using Docker Compose with this Makefile within the repository's docker directory.                                              |
| [docker-compose.yml](https://github.com/jwills/buenavista/blob/master/docker/docker-compose.yml) | Compose services configuration for CloudBeaver and Buenavista images in docker-compose.yml, defining ports and environment variables.                                      |

</details>

<details closed><summary>buenavista</summary>

| File                                                                                         | Summary                                                                                                                                    |
| ---                                                                                          | ---                                                                                                                                        |
| [bv_dialects.py](https://github.com/jwills/buenavista/blob/master/buenavista/bv_dialects.py) | Enhances SQL dialects in the Buenavista project, including Trino and DuckDB customizations and additional expressions for Postgres.        |
| [core.py](https://github.com/jwills/buenavista/blob/master/buenavista/core.py)               | BV core functionality for querying and processing data, including result representation, sessions management, connections, and extensions. |
| [postgres.py](https://github.com/jwills/buenavista/blob/master/buenavista/postgres.py)       | buenavista/postgres.py` manages PostgreSQL connections, queries, and data rewriting within the `buenavista` repository architecture.       |
| [rewrite.py](https://github.com/jwills/buenavista/blob/master/buenavista/rewrite.py)         | Implements a SQL rewriter for abstracting table details, handling SQL transformation between different databases with relation mappings.   |

</details>

<details closed><summary>buenavista.backends</summary>

| File                                                                                            | Summary                                                                                                                                  |
| ---                                                                                             | ---                                                                                                                                      |
| [postgres.py](https://github.com/jwills/buenavista/blob/master/buenavista/backends/postgres.py) | Create PostgreSQL database connections and sessions, executing queries and fetching results with Buenavista-specific data types mapping. |
| [duckdb.py](https://github.com/jwills/buenavista/blob/master/buenavista/backends/duckdb.py)     | Convert DuckDB data types to Buenavista types and provide classes for querying and managing DuckDB connections and sessions.             |

</details>

<details closed><summary>buenavista.http</summary>

| File                                                                                                | Summary                                                                                                                                                                                                                             |
| ---                                                                                                 | ---                                                                                                                                                                                                                                 |
| [type_mapping.py](https://github.com/jwills/buenavista/blob/master/buenavista/http/type_mapping.py) | Defines type mappings and converters for translating Buenavista types to Trino, enhancing compatibility in the database interaction layer.                                                                                          |
| [context.py](https://github.com/jwills/buenavista/blob/master/buenavista/http/context.py)           | Manages session pools and HTTP headers for database connections based on incoming requests' metadata. Facilitates SQL execution and transaction handling efficiently.                                                               |
| [schemas.py](https://github.com/jwills/buenavista/blob/master/buenavista/http/schemas.py)           | Define Pydantic models for HTTP response schemas including Column, StatementStats, QueryError, and BaseResult with camel case aliasing.                                                                                             |
| [main.py](https://github.com/jwills/buenavista/blob/master/buenavista/http/main.py)                 | Code snippet `main.py` in `buenavista/http` provides FastAPI endpoints `info` and `statement` to handle HTTP requests for query execution and responses. It includes connection setup, query processing, and result transformation. |

</details>

<details closed><summary>buenavista.examples</summary>

| File                                                                                                          | Summary                                                                                                                                          |
| ---                                                                                                           | ---                                                                                                                                              |
| [duckdb_postgres.py](https://github.com/jwills/buenavista/blob/master/buenavista/examples/duckdb_postgres.py) | Rewriting SQL queries for DuckDB to emulate PostgreSQL behavior. Also, initializes a BuenaVista server to handle DuckDB connections.             |
| [duckdb_http.py](https://github.com/jwills/buenavista/blob/master/buenavista/examples/duckdb_http.py)         | Rewrites SQL queries with DuckDB connections. Configured FastAPI app with Presto API using DuckDB.                                               |
| [postgres_proxy.py](https://github.com/jwills/buenavista/blob/master/buenavista/examples/postgres_proxy.py)   | Postgres proxy enabling communication between servers. Establishes connection, listens on specified address, forwards requests to target server. |

</details>

<details closed><summary>.github.workflows</summary>

| File                                                                                      | Summary                                                                                                                                                           |
| ---                                                                                       | ---                                                                                                                                                               |
| [push.yaml](https://github.com/jwills/buenavista/blob/master/.github/workflows/push.yaml) | Automated CI workflows for push events. Incorporates linting, testing, and Docker image building. Streamlines development processes in the Buenavista repository. |
| [main.yml](https://github.com/jwills/buenavista/blob/master/.github/workflows/main.yml)   | Automated CI/CD pipeline for the Buenavista repository using GitHub Actions. Validates code changes, triggers builds, and deploys on merges to main branch.       |

</details>

---

##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Python**: `version x.y.z`

###  Install

1. Clone the buenavista repository:

```sh
git clone https://github.com/jwills/buenavista
```

2. Change to the project directory:

```sh
cd buenavista
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

###  Using `buenavista`

Use the following command to run buenavista:

```sh
python main.py
```

###  Tests

Use the following command to run tests:

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

- **[Report Issues](https://github.com/jwills/buenavista/issues)**: Submit bugs found or log feature requests for the `buenavista` project.
- **[Submit Pull Requests](https://github.com/jwills/buenavista/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/jwills/buenavista/discussions)**: Share your insights, provide feedback, or ask questions.

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

[**Return**](#-overview)

---
