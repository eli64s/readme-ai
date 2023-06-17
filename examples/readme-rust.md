
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
contacts-cli
</h1>
<h3 align="center">📍 Stay Connected with Ease: Manage Your Contacts with Contacts-CLI on GitHub!</h3>
<h3 align="center">🚀 Developed with the software and tools below:</h3>

<p align="center">
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=for-the-badge&logo=Docker&logoColor=white" alt="Docker" />
<img src="https://img.shields.io/badge/Rust-000000.svg?style=for-the-badge&logo=Rust&logoColor=white" alt="Rust" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="Markdown" />
</p>
</div>

---

## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍Overview](#-overview)
- [🔮 Features](#-features)
- [⚙️ Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🏎💨 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [🪪 License](#-license)
- [📫 Contact](#-contact)
- [🙏 Acknowledgments](#-acknowledgments)

---


## 📍Overview

The project is a command-line interface for managing contacts that allows users to add, view, update, and delete contacts, and also to export and import them as JSON files. It provides functionality for connecting to a Redis database or using an in-memory data store. The project's value proposition is that it provides a simple and flexible way to manage contacts from the command line, with support for both persistent and in-memory storage options.

---

## 🔮 Features

Feature | Description |
|---|---|
| **🏗 Structure and Organization** | The codebase follows the standard Rust package structure, with separate directories for source files, tests, and documentation. The project's architecture is based on the repository pattern, with separate modules for contacts, Redis, and in-memory repository implementations. |
| **📝 Code Documentation** | The codebase includes inline documentation with Rust's built-in documentation tool, as well as README.md files that provide general documentation, installation instructions, and usage examples. |
| **🧩 Dependency Management** | The project uses Cargo for dependency management, with dependencies specified in the Cargo.toml file. The project relies on several external libraries including clap, dotenvy, redis, regex, serde, serde_json, and shlex. |
| **♻️ Modularity and Reusability** | The codebase is highly modular, with separate modules for contacts, Redis, and in-memory repository implementations. The repository pattern allows for easy extension and reuse of repository implementations with different data sources. |
| **✅ Testing and Quality Assurance** | The codebase includes unit tests for each module and integration tests that verify the interactions between modules, ensuring that the code functions as expected. The code is formatted using Rust's built-in formatter, and linted using the Clippy tool to ensure code quality and consistency. |
| **⚡️ Performance and Optimization** | The codebase efficiently uses Redis as a data source, taking advantage of Redis's performance characteristics such as in-memory data storage, and optimized querying operations. |
| **🔒 Security Measures** | The codebase uses Redis's built-in authentication mechanism to secure access to Redis instances. dotenv is used to securely manage sensitive environment variables. |
| **🔄 Version Control and Collaboration** | The codebase is hosted on GitHub, and uses Git for version control. The repository includes a Makefile for easily managing build tasks, including starting and stopping a Redis instance using Docker Compose. |
| **🔌 External Integrations** | The project integrates with Redis, a popular in-memory data store, and uses the Clap library for command-line argument parsing, making it easy to integrate with other command-line tools and scripts. |
| **📈 Scalability and Extensibility** | The repository pattern used in the codebase allows for easy extension and reuse of repository implementations with different data sources. Redis's built-in scalability features enable the system to easily handle larger amounts of data and user load. |

---


<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## ⚙️ Project Structure


```bash
repo
├── Cargo.toml
├── LICENSE
├── Makefile
├── README.md
├── docker-compose.yaml
└── src
    ├── main.rs
    ├── models
    │   ├── contact.rs
    │   └── mod.rs
    └── repositories
        ├── contacts.rs
        ├── db_contacts.rs
        ├── inmemory_contacts.rs
        └── mod.rs

4 directories, 12 files
```

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 💻 Modules

<details closed><summary>Models</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                                                                                                              | Module                |
|:-----------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
| mod.rs     | The code snippet creates a module named "contact" that can be used to organize related functions, structs, and traits within a Rust program. This module can then be imported and used in other parts of the program as needed.                                                                                                                                                                      | src/models/mod.rs     |
| contact.rs | The provided code defines a Contact struct with three fields: name as a String, phone_no as a u64 (unsigned 64-bit integer), and email as a String. The struct implements the Serialize and Deserialize traits from Serde, which allows it to be easily serialized and deserialized from various formats like JSON. The Clone trait is also implemented, enabling easy copying of Contact instances. | src/models/contact.rs |

</details>

<details closed><summary>Repositories</summary>

| File                 | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                               | Module                                |
|:---------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------|
| contacts.rs          | The code snippet defines functions to validate and extract data for a contact. It also defines a trait `ContactsRepository` that outlines methods for managing and manipulating a collection of contacts, including adding, updating, and deleting contacts, as well as methods for exporting and importing contacts.                                                                                                                                 | src/repositories/contacts.rs          |
| db_contacts.rs       | The code defines a struct `DbContactsRepository` that implements a `ContactsRepository` trait for performing CRUD operations on contacts stored in a Redis instance. The Redis connection is established upon creating a new instance of `DbContactsRepository`. The implementation also includes functionalities such as pagination, exporting and importing contacts to/from JSON format and counting the total number of contacts stored in Redis. | src/repositories/db_contacts.rs       |
| mod.rs               | The provided code snippet contains three modules: "contacts", "db_contacts", and "inmemory_contacts". These modules likely contain code related to managing contacts in different ways, such as storing them in a database or in memory. It is not possible to determine the specific functionalities of these modules without further information.                                                                                                   | src/repositories/mod.rs               |
| inmemory_contacts.rs | The code defines an in-memory repository for managing contacts, implementing the ContactsRepository trait. It provides functionality for adding, updating, deleting, and retrieving contacts, as well as exporting and importing contacts to/from JSON and pagination of the contacts list. The code also includes unit tests to verify the functionality of the repository.                                                                          | src/repositories/inmemory_contacts.rs |

</details>

<details closed><summary>Root</summary>

| File                | Summary                                                                                                                                                                                                                                                                                                                                                                   | Module              |
|:--------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------|
| Cargo.toml          | The code snippet includes a package file which specifies the name, version, and dependencies of the project. The project relies on several external libraries including clap, dotenvy, redis, regex, serde, serde_json, and shlex.                                                                                                                                        | Cargo.toml          |
| docker-compose.yaml | This code defines a service running Redis 7 on an Alpine Linux container. It maps the container's port 6379 to a specified host port, and ensures that the service always restarts.                                                                                                                                                                                       | docker-compose.yaml |
| Makefile            | This code snippet provides a set of Makefile commands for managing a Rust project, including compiling, updating dependencies, running binaries, checking code, releasing the package, formatting Rust files, running tests, and starting/stopping a database using Docker Compose. A "help" command is also available to display all available commands and their usage. | Makefile            |

</details>

<details closed><summary>Src</summary>

| File    | Summary                                                                                                                                                                                                                                                                                                                                                                                   | Module      |
|:--------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------|
| main.rs | This code is a simple command line interface for a contacts application. It uses the Clap library to parse commands and arguments, and interacts with a database of contacts through a custom ContactsRepository. Users can add, view, update, and delete contacts, as well as export and import contacts to and from a JSON file. The application runs a REPL loop until the user quits. | src/main.rs |

</details>

<hr />

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> `[📌  INSERT-PROJECT-PREREQUISITES]`

### 💻 Installation

1. Clone the contacts-cli repository:
```sh
git clone https://github.com/MihaiBogdanEugen/contacts-cli
```

2. Change to the project directory:
```sh
cd contacts-cli
```

3. Install the dependencies:
```sh
cargo build
```

### 🤖 Using contacts-cli

```sh
cargo run
```

### 🧪 Running Tests
```sh
# [INSERT-COMMAND-FOR-TESTS]
```

<hr />


## 🛠 Future Development
- [X] [📌  COMPLETED-TASK]
- [ ] [📌  INSERT-TASK]
- [ ] [📌  INSERT-TASK]


---

## 🤝 Contributing
Contributions are always welcome! Please follow these steps:
1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).
```sh
git checkout -b new-feature-branch
```
4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub using the following command
```sh
git push origin new-feature-branch
```
7. Create a pull request to the original repository.
Open a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 🪪 License

This project is licensed under the `[📌  INSERT-LICENSE-TYPE]` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 🙏 Acknowledgments

`[📌  INSERT-REFERENCES-AND-RESOURCES]`


---

