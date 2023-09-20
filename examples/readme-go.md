<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>docker-gs-ping
</h1>
<h3>◦ Containerize the Ping!</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style&logo=Docker&logoColor=white" alt="Docker" />
<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions" />
<img src="https://img.shields.io/badge/Go-00ADD8.svg?style&logo=Go&logoColor=white" alt="Go" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
</p>
<img src="https://img.shields.io/github/languages/top/olliefr/docker-gs-ping?style&color=5D6D7E" alt="GitHub top language" />
<img src="https://img.shields.io/github/languages/code-size/olliefr/docker-gs-ping?style&color=5D6D7E" alt="GitHub code size in bytes" />
<img src="https://img.shields.io/github/commit-activity/m/olliefr/docker-gs-ping?style&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/license/olliefr/docker-gs-ping?style&color=5D6D7E" alt="GitHub license" />
</div>

---

## 📖 Table of Contents
- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [⚙️ Modules](#modules)
- [🚀 Getting Started](#-getting-started)
    - [🔧 Installation](#-installation)
    - [🤖 Running docker-gs-ping](#-running-docker-gs-ping)
    - [🧪 Tests](#-tests)
- [🛣 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The project is a Docker image that pings a server using a simple Go web application built with the Echo framework. It provides a lightweight and portable solution for checking the connectivity of a server. The Dockerization allows for easy deployment and scalability, making it convenient for monitoring multiple servers in a distributed environment. Additionally, the inclusion of automated tests and continuous integration workflows ensures the reliability and quality of the application.

---

## 📦 Features

| Feature                | Description                           |
| ---------------------- | ------------------------------------- |
| **⚙️ Architecture**     | The codebase follows a modular architecture with separate files for different components of the application. It uses the Echo framework to set up an HTTP server and handle routes. The Dockerfiles provide containerization for the application. Limit your response to a maximum of 250 characters.  |
| **📃 Documentation**   | The codebase is relatively well-documented, with each file providing a brief summary of its purpose. However, more detailed comments within the code could improve comprehensiveness. Limit your response to a maximum of 250 characters.  |
| **🔗 Dependencies**    | The project relies on the Echo framework, as well as several other Go modules that are specified in the `go.mod` file. These dependencies provide the necessary functionality for building the web application and running tests. Limit your response to a maximum of 250 characters.  |
| **🧩 Modularity**      | The codebase demonstrates good modularity by separating concerns into different files. The main functionality is contained in the `main.go` file, while testing logic resides in `main_test.go`. The Dockerfiles provide flexibility for building and deploying the application. Limit your response to a maximum of 250 characters.  |
| **🧪 Testing**          | The codebase includes test functions for the `IntMin` function using a basic scenario and a table-driven approach. This ensures that the function behaves as expected under different input conditions. The GitHub Actions workflows enable automated testing and provide visibility into the test results. Limit your response to a maximum of 250 characters.  |
| **⚡️ Performance**      | The codebase doesn't include explicit performance optimizations. However, being a simple web application, it is expected to have good performance. The use of the Echo framework and Go's concurrency features can contribute to efficient request handling. Limit your response to a maximum of 250 characters.  |
| **🔐 Security**        | The codebase does not explicitly address security measures. However, Go and Docker have built-in security features, and using frameworks like Echo can help mitigate common security vulnerabilities. Proper input validation and secure handling of sensitive data should be implemented if required. Limit your response to a maximum of 250 characters.  |
| **🔀 Version Control** | The codebase uses Git for version control, with the repository hosted on GitHub. The project follows a standard branching model, with CI/CD workflows triggered on push events and new tags. It leverages GitHub Actions for automated build, test, and release processes. Limit your response to a maximum of 250 characters.  |
| **🔌 Integrations**    | The codebase integrates with GitHub Actions for continuous integration and deployment. It builds and tests the application in containers, caches layers, and pushes releases to Docker Hub. The integration enables efficient development workflow and easy deployment. Limit your response to a maximum of 250 characters.  |
| **📶 Scalability**     | The codebase doesn't explicitly address scalability. However, being a containerized application, it can be easily deployed on scalable container orchestration platforms like Kubernetes. The modular design allows components to be scaled independently, and the use of Go can contribute to handling high loads. Limit your response to a maximum of 250 characters.  |

---


## 📂 Repository Structure


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

## ⚙️ Modules

<details closed><summary>Root</summary>

| File                                                                                               | Summary                                                                                                                                                                                                                                                        |
| ---                                                                                                | ---                                                                                                                                                                                                                                                            |
| [go.mod](https://github.com/olliefr/docker-gs-ping/blob/main/go.mod)                               | This code module is for a Docker image that pings a server. It requires the Echo framework and several other dependencies.                                                                                                                                     |
| [Dockerfile](https://github.com/olliefr/docker-gs-ping/blob/main/Dockerfile)                       | The code sets up a Docker environment for a Go application. It downloads Go modules, copies the source code, builds the application, exposes port 8080, and runs the application.                                                                              |
| [Dockerfile.multistage](https://github.com/olliefr/docker-gs-ping/blob/main/Dockerfile.multistage) | This Dockerfile builds a Go application from source, runs tests inside a container, and then deploys the application into a lean image based on the distroless base image. The final image exposes port 8080 and executes the application as the nonroot user. |
| [main.go](https://github.com/olliefr/docker-gs-ping/blob/main/main.go)                             | This code is a simple Go web application using the Echo framework. It sets up an HTTP server, handles routes for root and health endpoints, and starts the server on the specified port. It also includes a function to find the minimum of two integers.      |
| [main_test.go](https://github.com/olliefr/docker-gs-ping/blob/main/main_test.go)                   | This code includes two test functions for the IntMin function. The first test checks a basic scenario, while the second uses a table-driven approach to test multiple inputs and expected outputs.                                                             |

</details>

<details closed><summary>Workflows</summary>

| File                                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                                    |
| ---                                                                                                        | ---                                                                                                                                                                                                                                                                                                                                                        |
| [ci-cd.yml](https://github.com/olliefr/docker-gs-ping/blob/main/.github/workflows/ci-cd.yml)               | This code is for a GitHub Actions workflow that runs on push events to the main branch or when a new tag is created. It builds and tests an application in a Docker container, caches Docker layers, and pushes the release to Docker Hub if the event is not a pull request. It uses Docker Buildx and Docker login to handle the build and push process. |
| [ci-smoketest.yml](https://github.com/olliefr/docker-gs-ping/blob/main/.github/workflows/ci-smoketest.yml) | This code sets up a smoke test for a Go project. It runs automatically on every push to the repository or can be triggered manually. The test will build and test the project using Go toolchain in a GitHub runner.                                                                                                                                       |

</details>

---

## 🚀 Getting Started

***Dependencies***

Before you begin, ensure that you have the following prerequisites installed:
> - `ℹ️ Requirement 1`
> - `ℹ️ Requirement 2`
> - `ℹ️ ...`

### 🔧 Installation

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

### 🤖 Running docker-gs-ping

```sh
./myapp
```

### 🧪 Tests
```sh
go test
```

---


## 🛣 Roadmap

> - [X] `ℹ️  Task 1: Implement X`
> - [ ] `ℹ️  Task 2: Refactor Y`
> - [ ] `ℹ️ ...`


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

This project is licensed under the `ℹ️  INSERT-LICENSE-TYPE` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 👏 Acknowledgments

> - `ℹ️  List any resources, contributors, inspiration, etc.`

---
