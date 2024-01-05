<p align="left">
  <img src="https://cdn-icons-png.flaticon.com/512/6295/6295417.png" width="100" />
</p>
<p align="left">
    <h1 align="left">BUENAVISTA</h1>
</p>
<p align="left">
    <em>Unleash the Power of Programmable Proxies!</em>
</p>
<p align="left">
	<img src="https://img.shields.io/github/license/jwills/buenavista?style=flat-square&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/jwills/buenavista?style=flat-square&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/jwills/buenavista?style=flat-square&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/jwills/buenavista?style=flat-square&color=0080ff" alt="repo-language-count">
<p>
<p align="left">
		<em>Developed with the software and tools below.</em>
</p>
<p align="left">
	<img src="https://img.shields.io/badge/DuckDB-FFF000.svg?style=flat-square&logo=DuckDB&logoColor=black" alt="DuckDB">
	<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat-square&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
	<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat-square&logo=YAML&logoColor=white" alt="YAML">
	<img src="https://img.shields.io/badge/PostgreSQL-4169E1.svg?style=flat-square&logo=PostgreSQL&logoColor=white" alt="PostgreSQL">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python">
	<br>
	<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat-square&logo=Docker&logoColor=white" alt="Docker">
	<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=flat-square&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions">
	<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat-square&logo=Pytest&logoColor=white" alt="Pytest">
	<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=flat-square&logo=FastAPI&logoColor=white" alt="FastAPI">
</p>
<hr>

## 🔗 Quick Links

> - [📍 Overview](#-overview)
> - [📦 Features](#-features)
> - [📂 Repository Structure](#-repository-structure)
> - [🧩 Modules](#-modules)
> - [🚀 Getting Started](#-getting-started)
>     - [⚙️ Installation](#-installation)
>     - [🤖 Running buenavista](#-running-buenavista)
>     - [🧪 Tests](#-tests)
> - [🛠 Project Roadmap](#-project-roadmap)
> - [🤝 Contributing](#-contributing)
> - [📄 License](#-license)
> - [👏 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

Buenavista is a project that aims to provide a programmable proxy for Presto and Postgres. It allows users to enhance and customize the behavior of these database systems by intercepting and modifying queries in-flight. With its ability to programmatically transform queries, apply filtering and routing rules, and inject custom logic, Buenavista empowers developers to create flexible and efficient data access layers. Combining the power of FastAPI and the versatility of SQL, this project provides a valuable tool for optimizing and managing data pipelines.

---

##  Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | The project has a modular architecture that uses FastAPI and DuckDB to create programmable Presto and Postgres proxies. It leverages Python, SQL, and YAML to provide an efficient and flexible solution for data processing and analysis. |
| 🔩 | **Code Quality**  | The codebase follows good quality practices and adheres to PEP 8 style guidelines. It is well-structured, readable, and maintainable. |
| 📄 | **Documentation** | The project has comprehensive documentation, including a README file and a well-documented setup.py file. The documentation provides details about installation, usage, and configuration options. |
| 🔌 | **Integrations**  | Key integrations and external dependencies include FastAPI, DuckDB, Pydantic, PyArrow, and psycopg. These libraries are used to handle HTTP requests, execute SQL queries, validate and serialize data, and interact with databases. |
| 🧩 | **Modularity**    | The codebase is highly modular, allowing for easy extension and reuse of components. It follows the principles of separation of concerns and single responsibility, improving maintainability and scalability. |
| 🧪 | **Testing**       | The project uses pytest as the testing framework. It includes a set of tests that cover different functionalities and ensure the correctness of the code. |
| ⚡️  | **Performance**   | The project leverages DuckDB's in-memory columnar storage and vectorized query processing, resulting in excellent performance and low resource usage. |
| 🛡️ | **Security**      | The project does not explicitly mention security measures, but the use of authentication middleware in FastAPI and secure database connections can be implemented for data protection and access control. |
| 📦 | **Dependencies**  | Key external libraries and dependencies include FastAPI, DuckDB, Pydantic, PyArrow, and psycopg. These libraries provide essential functionality for handling HTTP requests, executing SQL queries, data serialization, and database interactions. |


---

##  Repository Structure

```sh
└── buenavista/
    ├── .github
    │   └── workflows
    │       ├── main.yml
    │       └── push.yaml
    ├── buenavista
    │   ├── backends
    │   │   ├── duckdb.py
    │   │   └── postgres.py
    │   ├── bv_dialects.py
    │   ├── core.py
    │   ├── examples
    │   │   ├── duckdb_http.py
    │   │   ├── duckdb_postgres.py
    │   │   └── postgres_proxy.py
    │   ├── http
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
    │   ├── docker-compose.yml
    │   └── download_data.sh
    └── setup.py
```

---

##  Modules

<details closed><summary>.</summary>

| File                                                                                          | Summary                                                                                                                                                                                                                                                                                               |
| ---                                                                                           | ---                                                                                                                                                                                                                                                                                                   |
| [dev-requirements.txt](https://github.com/jwills/buenavista/blob/master/dev-requirements.txt) | This code snippet, located in the `dev-requirements.txt` file, specifies the required development dependencies for the Buenavista repository. These dependencies include libraries and tools such as DuckDB, FastAPI, psycopg, PyArrow, Pydantic, pytest, and sqlglot.                                |
| [setup.py](https://github.com/jwills/buenavista/blob/master/setup.py)                         | This code snippet, located in the `setup.py` file, is responsible for setting up the configuration and dependencies for the Buenavista repository. It defines the package name, version, description, author, and other details. Additionally, it specifies the required packages and their versions. |

</details>

<details closed><summary>docker</summary>

| File                                                                                             | Summary                                                                                                                                                                                                                                                                                                                                  |
| ---                                                                                              | ---                                                                                                                                                                                                                                                                                                                                      |
| [download_data.sh](https://github.com/jwills/buenavista/blob/master/docker/download_data.sh)     | The code snippet `docker/download_data.sh` is responsible for downloading example data (specifically `iris.parquet` and `chinook.db`) to the `./data` directory. This script uses `curl` to fetch the files and `unzip` to extract the `chinook.db` file from a ZIP archive.                                                             |
| [Dockerfile](https://github.com/jwills/buenavista/blob/master/docker/Dockerfile)                 | This code snippet, located in the `docker/Dockerfile` file, sets up the Docker container for the Buenavista repository. It installs dependencies, builds and installs the repository, and exposes port 5433. The container's entry point runs the `duckdb_postgres` example.                                                             |
| [Makefile](https://github.com/jwills/buenavista/blob/master/docker/Makefile)                     | This code snippet, located in the docker/Makefile file, provides commands to build the buenavista Docker image, start the Docker container, and download example data. It is a part of the overall repository structure, contributing to the deployment and setup process of the buenavista project.                                     |
| [docker-compose.yml](https://github.com/jwills/buenavista/blob/master/docker/docker-compose.yml) | The code snippet in the docker-compose.yml file sets up and configures two services: cloudbeaver and buenavista. It specifies the Docker images to use for each service and defines their respective ports and environment variables. This code is critical for deploying and running the repository's services in a Docker environment. |

</details>

<details closed><summary>buenavista</summary>

| File                                                                                         | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---                                                                                          | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [bv_dialects.py](https://github.com/jwills/buenavista/blob/master/buenavista/bv_dialects.py) | The code snippet in `bv_dialects.py` adds additional expressions and custom modifications to dialects in the parent repository. It introduces a new expression `ToISO8601` and makes Trino and DuckDB specific modifications.                                                                                                                                                                                                                                          |
| [core.py](https://github.com/jwills/buenavista/blob/master/buenavista/core.py)               | The code snippet in core.py defines the main classes for the BV representation of a query result and the translation layer from an upstream data source. It also includes auxiliary classes for query results and extensions.                                                                                                                                                                                                                                          |
| [postgres.py](https://github.com/jwills/buenavista/blob/master/buenavista/postgres.py)       | The code snippet in `buenavista/postgres.py` is responsible for handling PostgreSQL database connections and executing queries. It includes functions for connecting to the database, executing queries, and handling query results. The code also imports necessary modules and defines logger.                                                                                                                                                                       |
| [rewrite.py](https://github.com/jwills/buenavista/blob/master/buenavista/rewrite.py)         | This code snippet contains a class called `Rewriter` that is responsible for rewriting SQL queries based on defined relations. It utilizes the `sqlglot` library to parse and generate SQL queries for different dialects. The `Rewriter` class has methods for defining relations and rewriting SQL queries by transforming the query expressions. The main function demonstrates the usage of the `Rewriter` class by defining a relation and rewriting a SQL query. |

</details>

<details closed><summary>buenavista.backends</summary>

| File                                                                                            | Summary                                                                                                                                                                                                                                                                                                                                                               |
| ---                                                                                             | ---                                                                                                                                                                                                                                                                                                                                                                   |
| [postgres.py](https://github.com/jwills/buenavista/blob/master/buenavista/backends/postgres.py) | This code snippet, located at `buenavista/backends/postgres.py`, provides a PostgreSQL implementation for Buenavista's backends. It defines classes for executing SQL queries, managing sessions, and converting query results.                                                                                                                                       |
| [duckdb.py](https://github.com/jwills/buenavista/blob/master/buenavista/backends/duckdb.py)     | The code snippet in `buenavista/backends/duckdb.py` defines classes and functions for interacting with a DuckDB database. It includes methods for converting data types, executing SQL queries, and managing sessions. The classes `DuckDBQueryResult`, `DuckDBSession`, and `DuckDBConnection` are the core components responsible for handling database operations. |

</details>

<details closed><summary>buenavista.http</summary>

| File                                                                                                | Summary                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ---                                                                                                 | ---                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [type_mapping.py](https://github.com/jwills/buenavista/blob/master/buenavista/http/type_mapping.py) | This code snippet in `buenavista/http/type_mapping.py` defines a type mapping dictionary and helper functions for converting data types between different systems. It provides mappings for various data types and allows converting types to Trino-specific formats. These mappings are used in the parent repository's HTTP module for type conversion and handling.                                                         |
| [context.py](https://github.com/jwills/buenavista/blob/master/buenavista/http/context.py)           | This code snippet defines the `Context` class, which manages the request context for HTTP API calls in the Buenavista repository. It handles request headers, manages session pooling for database connections, executes SQL queries, and manages transaction IDs.                                                                                                                                                             |
| [schemas.py](https://github.com/jwills/buenavista/blob/master/buenavista/http/schemas.py)           | This code snippet in schemas.py defines several Pydantic models and type annotations used for handling HTTP requests and responses in the Buenavista repository. It includes models for various query result structures, column definitions, statement statistics, and error handling. These models help ensure data consistency and facilitate communication between the backend and frontend components of the architecture. |
| [main.py](https://github.com/jwills/buenavista/blob/master/buenavista/http/main.py)                 | This code snippet is a part of the buenavista repository and contains the implementation for a FastAPI endpoint. It handles HTTP requests for executing SQL statements, converting the query results into a standardized format, and returning the results as JSON. The code also includes error handling and supports extensions for additional functionality.                                                                |

</details>

<details closed><summary>buenavista.examples</summary>

| File                                                                                                          | Summary                                                                                                                                                                                                                                                                                                                                                                                       |
| ---                                                                                                           | ---                                                                                                                                                                                                                                                                                                                                                                                           |
| [duckdb_postgres.py](https://github.com/jwills/buenavista/blob/master/buenavista/examples/duckdb_postgres.py) | This code snippet in duckdb_postgres.py is responsible for rewriting SQL queries in a DuckDB-PG compatibility layer. It creates a BuenaVista server that listens on a specified IP address and port, connects to a DuckDB database, and handles incoming queries. The rewriter modifies specific SQL queries, while the create function initializes the server with the necessary parameters. |
| [duckdb_http.py](https://github.com/jwills/buenavista/blob/master/buenavista/examples/duckdb_http.py)         | This code snippet is a part of the Buenavista repository and resides in the buenavista/examples/duckdb_http.py file. It sets up a FastAPI app with a DuckDB connection and rewriter for handling SQL queries. It also defines relations for various JDBC tables. The app runs on a specified host and port using uvicorn.                                                                     |
| [postgres_proxy.py](https://github.com/jwills/buenavista/blob/master/buenavista/examples/postgres_proxy.py)   | This code snippet in `buenavista/examples/postgres_proxy.py` sets up a proxy server to connect to a PostgreSQL database. It creates a `BuenaVistaServer` instance and listens on a specified address, forwarding requests to the PostgreSQL backend. The proxy server allows clients to interact with the database through a different interface.                                             |

</details>

<details closed><summary>.github.workflows</summary>

| File                                                                                      | Summary                                                                                                                                                                                                                                                                                                                     |
| ---                                                                                       | ---                                                                                                                                                                                                                                                                                                                         |
| [push.yaml](https://github.com/jwills/buenavista/blob/master/.github/workflows/push.yaml) | This code snippet is a GitHub Actions workflow file (.github/workflows/push.yaml) that is responsible for automating the process of building and pushing changes to the repository. It ensures that any changes made to the codebase are automatically built and deployed to the appropriate environment.                   |
| [main.yml](https://github.com/jwills/buenavista/blob/master/.github/workflows/main.yml)   | This code snippet is located in the `.github/workflows/main.yml` file. It plays a critical role in the repository's architecture as it defines the workflow automation for the repository. It specifies the steps to be executed whenever changes are pushed to the repository, ensuring efficient and automated processes. |

</details>

---

##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Python**: `version x.y.z`

###  Installation

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

###  Running buenavista

Use the following command to run buenavista:

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

- **[Submit Pull Requests](https://github/jwills/buenavista/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github/jwills/buenavista/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github/jwills/buenavista/issues)**: Submit bugs found or log feature requests for Buenavista.

<details closed>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
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
