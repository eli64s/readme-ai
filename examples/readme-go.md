
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
docker-gs-ping
</h1>
<h3>◦ Ping like a pro with Docker</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=for-the-badge&logo=Docker&logoColor=white" alt="Docker" />
<img src="https://img.shields.io/badge/Go-00ADD8.svg?style=for-the-badge&logo=Go&logoColor=white" alt="Go" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="Markdown" />
</p>
</div>

---

## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [⚙️ Features](#-features)
- [📂 Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🚀 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The docker-gs-ping project is a Golang-based web application that provides endpoints to ping a Docker container and check its health status. It uses the Echo framework for HTTP server implementation and can be built and deployed easily using Docker. The project's main value proposition is its simplicity, reliability, and ease of use when it comes to monitoring Docker containers.

---

## ⚙️ Features

Feature | Description |
|-----|-----|
| **🏗 Architecture** | The codebase follows a simple client-server architecture. It uses the Echo framework to create a lightweight HTTP server, which responds to GET requests on two endpoints. The endpoints return an HTML and JSON response, respectively. The Dockerfile(s) use a multistage build process to create a lean and efficient Docker image. |
| **📑 Documentation** | The repository contains a clear and concise README file that provides information about the application, how to build and run the Docker image, and the endpoints exposed by the server. The README also includes a section on how to contribute to the codebase and a license. |
| **🧩 Dependencies** | The Go module makes use of the Echo v4.10.2 framework, along with several other indirect dependencies such as jwt, crypto, and text. The Docker images are based on golang:1.17.1-alpine and debian:11, respectively. |
| **♻️ Modularity** | The codebase is modular and follows the standard Go project structure. It contains a single main package that sets up the HTTP server and handles requests, with an additional main_test.go file for unit tests. The multistage Dockerfile builds the application from source and runs tests in a separate stage before creating a lean image. |
| **✔️ Testing** | The codebase includes a single test file, main_test.go, with two unit tests for the IntMin function. The tests are well-written and cover basic functionality as well as a table-driven test for multiple inputs and expected outputs. The Dockerfile.multistage runs the tests before creating the image, ensuring that the binary deployed in the final image is tested and reliable. |
| **⚡️ Performance** | The codebase is lightweight and efficient, using the Echo framework for creating a fast and scalable HTTP server. The multistage Dockerfile ensures that the final image is lean and optimized, reducing startup time and memory usage. |
| **🔒 Security** | The Dockerfile.multistage creates a nonroot user and runs the application with the corresponding uid/gid to minimize security risks. The HTTP server has minimal attack surface, with just two simple endpoints, and doesn't handle any sensitive data. The Go modules used in the project are up-to-date and have no known security vulnerabilities. |
| **🔀 Version Control** | The repository is well-organized and follows standard Git conventions. It includes a clear commit history, with informative commit messages that explain changes made to the codebase. The repository follows a "main" branch protection approach, requiring pull requests to be reviewed before merging into the main branch. |
| **🔌 Integrations** | The codebase doesn't contain any external integrations or services. |
| **📈 Scalability** | The codebase is designed to be scalable, with the Echo

---


## 📂 Project Structure


```bash
repo
├── Dockerfile
├── Dockerfile.multistage
├── LICENSE
├── README.md
├── go.mod
├── go.sum
├── main.go
└── main_test.go

1 directory, 8 files
```

---

## 🧩 Modules

<details closed><summary>Root</summary>

| File                  | Summary                                                                                                                                                                                                                                                                                                                                                                                              | Module                |
|:----------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
| go.mod                | The provided code is a Go module with a dependency on the Echo v4.10.2 framework. It also has several indirect dependencies on various packages, including jwt, crypto, and text. The module is used for pinging a Docker container and is available on GitHub under the olliefr/docker-gs-ping repository.                                                                                          | go.mod                |
| Dockerfile            | This code snippet is a Dockerfile that sets up a Golang environment and builds an application. It copies the source code and Go modules, downloads dependencies, builds the application, exposes port 8080 for the application, and finally runs the application using CMD.                                                                                                                          | Dockerfile            |
| Dockerfile.multistage | The code snippet is a Dockerfile that builds a Go application from source code, runs tests, and deploys the compiled binary into a lean image based on Debian 11. The image exposes port 8080 and runs the binary with the entrypoint "/docker-gs-ping" as a nonroot user.                                                                                                                           | Dockerfile.multistage |
| main.go               | The code sets up a basic HTTP server using the Echo framework and listens on a default port "8080" or the port specified in the environment variable "PORT". It also includes two endpoints: "/" which returns an HTML response and "/health" which returns a JSON response with a status of "OK". Additionally, it includes a function to calculate the minimum integer value between two integers. | main.go               |
| main_test.go          | This Go code snippet illustrates two different unit tests for the IntMin function. The first test is basic and checks if the function returns the minimum of two integers. The second test is table-driven and uses a table to test multiple inputs and expected outputs. Both tests use the testing package to report any errors in the function's logic.                                           | main_test.go          |

</details>

---

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - [ℹ️ Requirement 1]
> - [ℹ️ Requirement 2]
> - [...]

### 🖥 Installation

1. Clone the docker-gs-ping repository:
```sh
git clone https://github.com/olliefr/docker-gs-ping
```

2. Change to the project directory:
```sh
cd docker-gs-ping
```

3. Install the dependencies:
```sh
go build -o myapp
```

### 🤖 Using docker-gs-ping

```sh
./myapp
```

### 🧪 Running Tests
```sh
go test
```

---


## 🗺 Roadmap

> - [X] [ℹ️  Task 1: Implement X]
> - [ ] [ℹ️  Task 2: Refactor Y]
> - [ ] [...]


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
7. Create a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 📄 License

This project is licensed under the `[ℹ️  INSERT-LICENSE-TYPE]` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 👏 Acknowledgments

> - [ℹ️  List any resources, contributors, inspiration, etc.]

---
