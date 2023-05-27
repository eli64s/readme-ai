
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
contacts-cli
</h1>
<h3 align="center">📍 GitHub project contacts-cli: Command line interface for your GitHub project contacts.</h3>
<h3 align="center">🚀 Developed with the software and tools below.</h3>
<p align="center">

<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="" />
<img src="https://img.shields.io/badge/Rust-000000.svg?style=for-the-badge&logo=Rust&logoColor=white" alt="markdown" />
</p>

</div>

---
## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍Overview](#-introdcution)
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

The GitHub project is a powerful collaboration and code-sharing tool that enables developers to work together on software projects. The project also provides a platform for developers to share their code with others, and to create and manage

## 🔮 Features

> `[📌  INSERT-PROJECT-FEATURES]`

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## ⚙️ Project Structure

```bash
.
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
<details closed><summary>.</summary>

| File   | Summary                                                                                                                        |
|:-------|:-------------------------------------------------------------------------------------------------------------------------------|
| .env   | This code sets up the environment variables for a Redis server, with the hostname set to 'localhost' and the port set to 7480. |

</details>

<details closed><summary>Src</summary>

| File    | Summary                                                                                                                                                         |
|:--------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| main.rs | This code is a command line application for managing contacts. It provides commands for adding, viewing, updating, deleting, exporting, and importing contacts. |

</details>

<details closed><summary>Src/models</summary>

| File       | Summary                                                                                                                                                                                                                                                         |
|:-----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| mod.rs     | This code creates a public module called "contact" which can be used to store and manage contact information.                                                                                                                                                   |
| contact.rs | This code creates a struct called Contact which contains three fields: name (String), phone_no (u64) and email (String). The struct is derived from the Serialize and Deserialize traits from the serde library, allowing it to be serialized and deserialized. |

</details>

<details closed><summary>Src/repositories</summary>

| File                 | Summary                                                                                                                                                                                                                                                                                                      |
|:---------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| contacts.rs          | This code provides a trait for a ContactsRepository, which provides methods for adding, updating, deleting, getting, listing, exporting to JSON, importing from JSON, and counting contacts.                                                                                                                 |
| db_contacts.rs       | This code implements a ContactsRepository trait for a database-backed contacts repository. It provides methods for adding, updating, deleting, getting, listing, exporting to JSON, and importing from JSON contacts.                                                                                        |
| mod.rs               | This code creates three modules: contacts, db_contacts, and inmemory_contacts. The contacts module provides a general interface for managing contacts, while the db_contacts and inmemory_contacts modules provide specific implementations for managing contacts in a database and in memory, respectively. |
| inmemory_contacts.rs | This code implements an InMemoryContactsRepository struct which provides methods to add, update, delete, get, list, and count contacts, as well as export and import contacts from/to a JSON file.                                                                                                           |

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
#run tests
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

[📌  INSERT-DESCRIPTION]


---
