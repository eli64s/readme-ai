
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
go-docker-example
</h1>
<h3 align="center">📍 Go Docker, Unleash the Power of the Cloud!</h3>
<h3 align="center">🚀 Developed with the software and tools below.</h3>
<p align="center">

<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=for-the-badge&logo=GNU-Bash&logoColor=white" alt="" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="yaml" />
<img src="https://img.shields.io/badge/Go-00ADD8.svg?style=for-the-badge&logo=Go&logoColor=white" alt="sample" />
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

go-docker-example is an open source Go-based project that demonstrates how to create a modern and fully featured web application using Docker containers. The project tooling provides out of the box support for deploying and

## 🔮 Feautres

> `[📌  INSERT-PROJECT-FEATURES]`

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## ⚙️ Project Structure

```bash
.
├── Dockerfile
├── README.md
├── cmd
│   └── example
│       ├── main.go
│       └── main_test.go
├── go.mod
├── go.sum
├── travis.sh
└── user
    ├── user.go
    └── user_test.go

4 directories, 9 files
```
---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 💻 Modules
<details closed><summary>Example</summary>

| File         | Summary                                                                                                                                                                                                                            | Module                   |
|:-------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------|
| main.go      | This code is a Go program that creates a user object and prints a greeting to the console using the user's full name.                                                                                                              | cmd/example/main.go      |
| main_test.go | This code is a test for the main() function, which is used to check if the output contains a specific string. It uses the "testing" package, "assert" package, and "log" package to test the main() function and check the output. | cmd/example/main_test.go |

</details>

<details closed><summary>Top Level</summary>

| File      | Summary                                                                                                                                                                                                   | Module    |
|:----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------|
| go.mod    | This module provides an example of how to use Docker with Go. It requires several packages, including go-spew, color, go-colorable, go-isatty, go-difflib, testify, and golang. org/x/sys.                | go.mod    |
| go.sum    | go-spew v1. 1. 0 is a debugging package for Go that provides a deep pretty printer for Go data structures to aid in debugging.                                                                            | go.sum    |
| travis.sh | This code builds a Docker image called "example-builder" with the target "builder", runs unit tests and publishes test coverage to Coveralls, and then builds and runs an app container called "example". | travis.sh |

</details>

<details closed><summary>User</summary>

| File         | Summary                                                                                                                                              | Module            |
|:-------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------|:------------------|
| user.go      | This code creates a User struct with two fields, NameFirst and NameLast, and a GetFullName method which returns the first and last name of the user. | user/user.go      |
| user_test.go | This code tests the GetFullName() function of the User package, which combines the NameFirst and NameLast fields to create a full name.              | user/user_test.go |

</details>
<hr />

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> `[📌  INSERT-PROJECT-PREREQUISITES]`

### 💻 Installation

1. Clone the go-docker-example repository:
```sh
git clone https://github.com/fterrag/go-docker-example
```

2. Change to the project directory:
```sh
cd go-docker-example
```

3. Install the dependencies:
```sh
go build -o myapp
```

### 🤖 Using go-docker-example

```sh
./myapp
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
