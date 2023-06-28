
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
docker-gs-ping
</h1>
<h3>◦ Seamless pinging with docker-gs-ping!</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style&logo=Docker&logoColor=white" alt="Docker" />
<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions" />
<img src="https://img.shields.io/badge/Go-00ADD8.svg?style&logo=Go&logoColor=white" alt="Go" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
</p>

![GitHub top language](https://img.shields.io/github/languages/top/olliefr/docker-gs-ping?style&color=5D6D7E)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/olliefr/docker-gs-ping?style&color=5D6D7E)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/olliefr/docker-gs-ping?style&color=5D6D7E)
![GitHub license](https://img.shields.io/github/license/olliefr/docker-gs-ping?style&color=5D6D7E)
</div>

---

## 📒 Table of Contents
- [📒 Table of Contents](#-table-of-contents)
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

The project is a Dockerized Go server that responds to HTTP requests using the Echo framework. It serves as a basic web server with middleware setup, customizable routes, and the ability to handle different HTTP methods. The project's value proposition lies in providing a lightweight, scalable, and easily deployable server solution, allowing developers to quickly set up and handle HTTP requests with minimal configuration.

---

## ⚙️ Features

| Feature                | Description                                                                                                                             |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **⚙️ Architecture**    | The codebase follows a simple and straightforward architectural design, with a single web server using the Echo framework to handle HTTP requests.                                                  |
| **📖 Documentation**   | The documentation is limited, with only brief summaries of each file in the repository. It would be beneficial to have more detailed documentation, including instructions on setup and usage. |
| **🔗 Dependencies**    | The codebase relies on external libraries, such as Echo for the web framework, and other Go modules managed through the go.mod file.      |
| **🧩 Modularity**      | The system is organized into smaller components, with separate files for the main server, unit tests, Dockerfiles, and the go.mod file. The modularity allows for easy extensibility and maintenance. |
| **✔️ Testing**         | The code includes automated unit tests using Go's testing package, covering different scenarios and assertions for the main server and the IntMin function.                                         |
| **⚡️ Performance**     | The system's performance depends on the underlying Go framework and the hardware it is deployed on. The minimalistic Dockerfile ensures a lean image, minimizing resource usage.            |
| **🔐 Security**        | The codebase doesn't explicitly implement security measures. However, being a straightforward server, implementing additional security measures would depend on the deployment and specific requirements. |
| **🔀 Version Control** | The codebase is version-controlled using Git, hosted on GitHub. The repository can be cloned or forked, and any changes can be tracked and managed effectively using Git methodologies. |
| **🔌 Integrations**    | The system does not have explicit integrations, but it can be easily integrated with other systems or services through HTTP endpoints provided by the Echo framework.                |
| **📶 Scalability**     | The system's scalability depends on the underlying Go framework and the infrastructure it is deployed on. Being a simple web server, it can handle a moderate level of concurrent requests.   |

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

| File                                                                                               | Summary                                                                                                                                                                                                                                                                                                                                                                                                   |
| ---                                                                                                | ---                                                                                                                                                                                                                                                                                                                                                                                                       |
| [go.mod](https://github.com/olliefr/docker-gs-ping/blob/main/go.mod)                               | The code snippet is a Go module that uses the Echo framework to build a server that responds to HTTP requests. It has various dependencies managed with version requirements.                                                                                                                                                                                                                             |
| [Dockerfile](https://github.com/olliefr/docker-gs-ping/blob/main/Dockerfile)                       | The provided code snippet builds a Docker image for a Go application. It downloads Go modules, copies the source code, builds the application, and exposes port 8080. Finally, it sets the command to run the built application.                                                                                                                                                                          |
| [Dockerfile.multistage](https://github.com/olliefr/docker-gs-ping/blob/main/Dockerfile.multistage) | The provided code snippet is a Dockerfile that builds a Go application, runs tests, and creates a lean image for deployment. It first builds the application, downloads dependencies, and compiles the binary. Then, it runs tests in a separate stage. Finally, it creates an image using a minimal base, copies the binary, opens a port, sets a non-root user, and sets the entry point as the binary. |
| [main.go](https://github.com/olliefr/docker-gs-ping/blob/main/main.go)                             | This code snippet is a basic web server built with the Echo framework. It sets up middleware, defines two routes ("/" and "/health"), and starts the server on a specified port (defaulting to 8080). It also includes a simple function for finding the minimum of two integers.                                                                                                                         |
| [main_test.go](https://github.com/olliefr/docker-gs-ping/blob/main/main_test.go)                   | The code snippet is a demonstration of automated unit testing in Go. It includes two test functions, one using basic assertions and the other using table-driven testing. The functions test the IntMin function by comparing its output with expected values and reporting any mismatches.                                                                                                               |

</details>

---

## 🚀 Getting Started

### ✔️ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - `ℹ️ Requirement 1`
> - `ℹ️ Requirement 2`
> - `ℹ️ ...`

### 💻 Installation

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

### 🎮 Using docker-gs-ping

```sh
./myapp
```

### 🧪 Running Tests
```sh
go test
```

---


## 🗺 Roadmap

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
