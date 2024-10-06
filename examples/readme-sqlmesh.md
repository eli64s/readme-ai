<p align="center">
  <img src="https://styles.redditmedia.com/t5_36en4/styles/communityIcon_t74nv7kttaz61.png" width="20%" alt="SQLMESH-TEST-TOOLS-logo">
</p>
<p align="center">
    <h1 align="center">SQLMESH-TEST-TOOLS</h1>
</p>
<p align="center">
    <em>Empower Your SQL, Automate with Confidence!</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/eli64s/sqlmesh-test-tools?style=flat-square&logo=opensourceinitiative&logoColor=white&color=00ffe9" alt="license">
	<img src="https://img.shields.io/github/last-commit/eli64s/sqlmesh-test-tools?style=flat-square&logo=git&logoColor=white&color=00ffe9" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/eli64s/sqlmesh-test-tools?style=flat-square&color=00ffe9" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/eli64s/sqlmesh-test-tools?style=flat-square&color=00ffe9" alt="repo-language-count">
</p>
<p align="center">
		<em>Built with the tools and technologies:</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/DuckDB-FFF000.svg?style=flat-square&logo=DuckDB&logoColor=black" alt="DuckDB">
	<img src="https://img.shields.io/badge/Jupyter-F37626.svg?style=flat-square&logo=Jupyter&logoColor=white" alt="Jupyter">
	<img src="https://img.shields.io/badge/Poetry-60A5FA.svg?style=flat-square&logo=Poetry&logoColor=white" alt="Poetry">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat-square&logo=Pytest&logoColor=white" alt="Pytest">
</p>

<br>

##### 🔗 Table of Contents

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
- [🔰 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

The sqlmesh-test-tools project is designed to enhance the reliability and efficiency of SQL data models within the SQLMesh framework. It features tools for generating both synthetic datasets and YAML configuration files, which are crucial for automating SQL unit tests. By parsing and executing SQL queries, and then validating these against generated datasets, the project supports comprehensive testing workflows. This setup not only streamlines the development process but also ensures the accuracy and robustness of SQL queries and data models, making it an invaluable asset for developers working with complex data-driven applications.

---

## 👾 Features

|    | Feature            | Description |
|----|--------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**   | Modular design with separate components for dataset generation, YAML configuration, and SQL testing. Utilizes Jupyter notebooks for configuration and data generation scripts. |
| 🔩 | **Code Quality**   | Code is structured with clear separation of concerns. Uses Python best practices and adheres to PEP8 standards, facilitated by tools like `flake8` and `black`. |
| 📄 | **Documentation**  | Documentation is embedded within code and Jupyter notebooks, explaining functionalities and usage. Lacks a comprehensive README or external documentation. |
| 🔌 | **Integrations**   | Integrates with SQLMesh for SQL testing, DuckDB for database interactions, and Faker for data generation. |
| 🧩 | **Modularity**     | High modularity with distinct components for data generation, test file creation, and SQL execution. Facilitates reuse and maintenance. |
| 🧪 | **Testing**        | Uses `pytest` for testing. Specific tests for components are not detailed but likely integrated within the development workflow. |
| ⚡️ | **Performance**    | Performance specifics not detailed, but use of DuckDB suggests efficient handling of SQL queries and datasets. |
| 🛡️ | **Security**       | No explicit security measures detailed. Focus is on testing and data generation rather than secure deployment or data handling. |
| 📦 | **Dependencies**   | Key dependencies include `duckdb`, `pytest`, `Faker`, `typer`, `pyarrow`, `PyYAML`, `sqlglot`, and `black`. |
| 🚀 | **Scalability**    | Scalability is indirectly supported through the use of DuckDB and modular design, allowing for expansion in data size and complexity of SQL queries. |

---

## 📂 Repository Structure

```sh
└── sqlmesh-test-tools/
    ├── README.md
    ├── data
    │   └── seed_metric_loans.csv
    ├── docs
    │   ├── .gitkeep
    │   └── images
    │       └── project-logo.png
    ├── notebooks
    │   ├── faker_dataset_generator.ipynb
    │   └── sqlmesh_yml_generator.ipynb
    ├── poetry.lock
    ├── pyproject.toml
    ├── sql
    │   └── test_metric_loans_model.sql
    ├── src
    │   ├── __init__.py
    │   ├── data_generator.py
    │   └── test_generator.py
    └── tests
        └── test_metric_loans_model.yaml
```

---

## 🧩 Modules

<details closed><summary>.</summary>

| File | Summary |
| --- | --- |
| [pyproject.toml](https://github.com/eli64s/sqlmesh-test-tools/blob/main/pyproject.toml) | Defines the configuration for the SQL Unit Test Generator project, specifying dependencies essential for generating and testing SQL queries within the SQLMesh framework. It sets up the project environment and tooling for development, ensuring compatibility and streamlined project setup. |

</details>

<details closed><summary>notebooks</summary>

| File | Summary |
| --- | --- |
| [sqlmesh_yml_generator.ipynb](https://github.com/eli64s/sqlmesh-test-tools/blob/main/notebooks/sqlmesh_yml_generator.ipynb) | Generates YAML configuration files for SQL unit tests by parsing SQL queries, executing them against a dataset, and outputting the results in a structured format to facilitate automated testing within the SQLMesh testing framework. This enhances the reliability of SQL data models by automating test validations. |
| [faker_dataset_generator.ipynb](https://github.com/eli64s/sqlmesh-test-tools/blob/main/notebooks/faker_dataset_generator.ipynb) | Generates synthetic datasets for testing SQL queries by leveraging the Faker library to produce realistic loan and restaurant service data, which are then saved as CSV files for integration into automated testing workflows within the repositorys SQL testing framework. |

</details>

<details closed><summary>src</summary>

| File | Summary |
| --- | --- |
| [test_generator.py](https://github.com/eli64s/sqlmesh-test-tools/blob/main/src/test_generator.py) | Generates YAML test files for SQL models by extracting and testing SQL queries and Common Table Expressions (CTEs) against provided datasets, facilitating automated testing and validation within the SQLMesh test tools ecosystem. Integrates with a CLI for streamlined operations. |
| [data_generator.py](https://github.com/eli64s/sqlmesh-test-tools/blob/main/src/data_generator.py) | Generates synthetic datasets for testing within the sqlmesh-test-tools repository, supporting the validation of SQL queries and data models by providing customizable and scalable data inputs, crucial for ensuring the robustness and accuracy of data operations across different testing scenarios. |

</details>

<details closed><summary>sql</summary>

| File | Summary |
| --- | --- |
| [test_metric_loans_model.sql](https://github.com/eli64s/sqlmesh-test-tools/blob/main/sql/test_metric_loans_model.sql) | Analyzes loan data by computing metrics such as average loan amount, age demographics of applicants, and loan frequency within the year, integrating these insights through a series of joined SQL queries to facilitate comprehensive data-driven decision-making within the repositorys testing framework. |

</details>

---

## 🚀 Getting Started

### 🔖 Prerequisites

**JupyterNotebook**: `version x.y.z`

### 📦 Installation

Build the project from source:

1. Clone the sqlmesh-test-tools repository:
```sh
❯ git clone https://github.com/eli64s/sqlmesh-test-tools
```

2. Navigate to the project directory:
```sh
❯ cd sqlmesh-test-tools
```

3. Install the required dependencies:
```sh
❯ pip install -r requirements.txt
```

### 🤖 Usage

To run the project, execute the following command:

```sh
❯ jupyter nbconvert --execute notebook.ipynb
```

### 🧪 Tests

Execute the test suite using the following command:

```sh
❯ pytest notebook_test.py
```

---

## 📌 Project Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🔰 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/eli64s/sqlmesh-test-tools/issues)**: Submit bugs found or log feature requests for the `sqlmesh-test-tools` project.
- **[Submit Pull Requests](https://github.com/eli64s/sqlmesh-test-tools/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/eli64s/sqlmesh-test-tools/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/eli64s/sqlmesh-test-tools
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
   <a href="https://github.com{/eli64s/sqlmesh-test-tools/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=eli64s/sqlmesh-test-tools">
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
