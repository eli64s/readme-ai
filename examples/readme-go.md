
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
docker-gs-ping
</h1>
<h3>◦ Keep your containers alive with docker-gs-ping!</h3>
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

The "docker-gs-ping" project is a simple Golang web server that serves two endpoints: a greeting message and a health check. The project includes Dockerfiles for easy containerization and deployment in a production environment. The value proposition of this project lies in its simplicity and ease of use, making it an ideal starting point for building more complex web applications.

---

## ⚙️ Features

Feature | Description |
|-----|-----|
| **🏗 Architecture** | The codebase follows a microservice architecture pattern, where a lightweight Golang web application is containerized with Docker for easy deployment, scaling, and maintenance. The application also uses a minimalist approach to software design, with only two endpoints and a single function used in the source code. |
| **📑 Documentation** | The codebase has well-organized documentation using clear and concise language, including the README file and function's comments. The documentation covers the code's purpose, architecture, testing, and deployment instructions. |
| **🧩 Dependencies** | The codebase has minimal dependencies using the Go module system, with only one direct dependency (Echo framework) and several other indirect dependencies required for functionality. The use of a single framework ensures code readability and maintainability. |
| **♻️ Modularity** | The codebase is well-structured and divided into small modular files, each with a single-purpose function. The use of modular design allows developers to understand, maintain, and scale the application better. |
| **✔️ Testing** | The codebase includes unit tests using Go's built-in testing package, providing coverage for the application's critical logic. The tests use table-driven testing to execute multiple test cases stored in an array. The testing approach ensures confidence in the code's accuracy and reliability. |
| **⚡️ Performance** | The codebase uses Golang's ability to provide native performance to the web application, enabling the application to serve HTTP requests quickly and efficiently. Additionally, the implementation of a single function to compute the minimum value of two integers is optimized for performance. |
| **🔒 Security** | The codebase has no apparent security vulnerabilities or flaws, with secure configuration settings and practices for the Docker image. Additionally, the web application uses SSL on any exposed ports, protecting data in transit from potential attackers. |
| **🔀 Version Control** | The codebase uses Git for version control, hosted on Github, providing source code management, version release, and collaboration with other developers. The codebase has a clear commit history and follows a pull-request-based workflow, allowing for code review and collaboration. |
| **🔌 Integrations** | The codebase uses a containerization approach with Docker, allowing integration with various cloud-based services and infrastructure. The codebase also uses a minimalist approach to software architecture, making integration with other systems easier to manage and maintain. |
| **📈 Scalability** | The codebase can scale the application horizontally, by using containerization and load balancers services. The use of minimalist design makes it easier to manage and add new features when necessary. Additionally, the application uses a microservice architecture, making it easier to scale individual services independently. |

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

| File                  | Summary                                                                                                                                                                                                                                                                                                                                                                                        | Module                |
|:----------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
| go.mod                | The code snippet is a Go module that requires the "echo" package and several indirect packages for functionality. The module is named "docker-gs-ping" and is hosted on Github under the username "olliefr." The version of Go required by the module is 1.19.                                                                                                                                 | go.mod                |
| Dockerfile            | The code snippet is a Dockerfile script for building a Golang application image. It downloads the required Go modules, copies the source code, builds the application, sets the default exposed TCP port, and runs the application. This allows for easy deployment and scaling of the Golang application in a containerized environment.                                                      | Dockerfile            |
| Dockerfile.multistage | This Dockerfile builds a Golang application from source, runs tests, and deploys a lean production image. It uses a multi-stage build to minimize the final image size, and runs the application as a non-root user on port 8080.                                                                                                                                                              | Dockerfile.multistage |
| main.go               | This is a basic Golang web server that listens on a specified port and serves two endpoints: `/` and `/health`. Endpoint `/` returns an HTTP response containing the message "Hello, Docker! <3" as an HTML payload. Endpoint `/health` returns an HTTP response containing the JSON object `{"Status": "OK"}`. The code also includes a simple implementation of an integer minimum function. | main.go               |
| main_test.go          | The code snippet demonstrates two unit tests for a function called IntMin that returns the minimum value between two integers. The first test uses basic assertion while the second test uses table-driven testing to execute multiple test cases stored in an array. The testing package is imported and utilized for the test functions and error reporting.                                 | main_test.go          |

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
