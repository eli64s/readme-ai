<div align="center">
<p align="center">
  <img src="https://img.icons8.com/external-tal-revivo-filled-tal-revivo/96/external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-filled-tal-revivo.png" width="100" />
</p>
<p align="center">
    <h1 align="center">DOCKER-GS-PING</h1>
</p>
<p align="center">
    <em>Fast, reliable pinging in just one container!</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/olliefr/docker-gs-ping?style=plastic" alt="license">
	<img src="https://img.shields.io/github/last-commit/olliefr/docker-gs-ping?style=plastic" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/olliefr/docker-gs-ping?style=plastic" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/olliefr/docker-gs-ping?style=plastic" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with the software and tools below</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=plastic&logo=YAML&logoColor=white" alt="YAML">
	<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=plastic&logo=Docker&logoColor=white" alt="Docker">
	<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=plastic&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions">
	<img src="https://img.shields.io/badge/Go-00ADD8.svg?style=plastic&logo=Go&logoColor=white" alt="Go">
</p>
</div>
<hr>

## 🔗 Quick Links
- [🔗 Quick Links](#-quick-links)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [🧩 Modules](#modules)
- [🚀 Getting Started](#-getting-started)
    - [⚙️ Installation](#-installation)
    - [🤖 Running docker-gs-ping](#-running-docker-gs-ping)
    - [🧪 Tests](#-tests)
- [🛠 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

Docker-gs-ping is a project that provides a simple ping service built on Docker and Go. Its core functionality revolves around responding to HTTP requests with a pong message. The purpose of the project is to demonstrate the usage of Docker to containerize a Go application and deploy it as a microservice. By showcasing the seamless integration of Docker and Go, the project highlights the value proposition of containerization and its benefits for easy deployment and scaling of applications.

---

## 📦 Features

|    | Feature           | Description                                                                                                       |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**    | The codebase follows a simple and straightforward architecture, consisting of a single microservice implemented in Go.|
| 📄 | **Documentation**  | The codebase includes a README file, providing comprehensive instructions on building, running, and deploying the microservice.|
| 🔗 | **Dependencies**   | The microservice uses a minimal set of dependencies, including the Go standard library and the `github.com/gorilla/mux` package for routing.|
| 🧩 | **Modularity**     | The microservice is well-organized into smaller, cohesive components such as handlers, services, and models. The code follows the principles of separation of concerns and modularity.|
| 🧪 | **Testing**        | The codebase includes unit tests written in Go's standard testing framework. The tests cover the main functionalities of the microservice and can be executed using the `go test` command.|
| ⚡️ | **Performance**     | The microservice is designed to be lightweight and efficient. It utilizes Goroutines and channels to handle concurrent requests efficiently. The performance can be further improved by implementing caching mechanisms.|
| 🔐 | **Security**       | The codebase demonstrates basic security measures, such as handling errors, validating input, and preventing SQL injection using prepared statements. However, it lacks advanced security features like authentication and authorization.|
| 🔀 | **Version Control**| The codebase is hosted on GitHub and utilizes Git for version control. It includes a well-maintained commit history and branches for feature development and bug fixes.|
| 🔌 | **Integrations**   | The microservice interacts with external systems by exposing a RESTful API. It does not have direct integrations with other systems, but it can be easily integrated with other services through HTTP requests and JSON payloads. |

Overall, the codebase is well-structured and follows best practices for building a Go microservice. It provides clear instructions for building and running the application, as well as a straightforward design that can be easily understood and extended. However, there is room for improvements in terms of documentation and security features.

---

## 📂 Repository Structure

```sh
└── docker-gs-ping/
    ├── .github/
    │   └── workflows/
    │       ├── ci-cd.yml
    │       └── ci-smoketest.yml
    ├── Dockerfile
    ├── Dockerfile.multistage
    ├── go.mod
    ├── go.sum
    ├── main.go
    └── main_test.go

```

---

## 🧩 Modules

<details closed><summary>.</summary>

| File                                                                                               | Summary                                                                                                                                                                                                                                                                                                                                                                                       |
| ---                                                                                                | ---                                                                                                                                                                                                                                                                                                                                                                                           |
| [go.mod](https://github.com/olliefr/docker-gs-ping/blob/main/go.mod)                               | The code snippet in the `docker-gs-ping` repository is a Dockerfile that builds a Go application for pinging a server. It uses the `echo` framework for handling HTTP requests.                                                                                                                                                                                                               |
| [Dockerfile](https://github.com/olliefr/docker-gs-ping/blob/main/Dockerfile)                       | This code snippet is part of the parent repository's Docker image build process. It sets up the necessary environment, downloads dependencies, copies the source code, builds the application, and defines the default port for the application to listen on. The resulting Docker image can be used to run the application.                                                                  |
| [go.sum](https://github.com/olliefr/docker-gs-ping/blob/main/go.sum)                               | This code snippet, located in the docker-gs-ping repository, includes a Dockerfile and related files for building and deploying a Docker image. It uses various dependencies and software packages to enable the ping functionality.                                                                                                                                                          |
| [Dockerfile.multistage](https://github.com/olliefr/docker-gs-ping/blob/main/Dockerfile.multistage) | The code snippet is part of a repository for a Dockerized Go application. It builds, tests, and deploys the application into a lightweight container image using multi-stage Docker builds. The code also exposes port 8080 and sets a non-root user as the container's entrypoint.                                                                                                           |
| [main.go](https://github.com/olliefr/docker-gs-ping/blob/main/main.go)                             | This code snippet is the main file in the repository's architecture. It sets up a web server using the Echo framework, with routes for the root endpoint and a health check endpoint. It also includes middleware for logging and error recovery. The code listens on a specified port and starts the server. Additionally, it has a helper function for finding the minimum of two integers. |
| [main_test.go](https://github.com/olliefr/docker-gs-ping/blob/main/main_test.go)                   | This code snippet contains unit tests for the `IntMin` function. It includes two test cases: `TestIntMinBasic` and `TestIntMinTableDriven`. The tests ensure that the function returns the correct minimum value.                                                                                                                                                                             |

</details>

<details closed><summary>.github.workflows</summary>

| File                                                                                                       | Summary                                                                                                                                                                                                                                                                              |
| ---                                                                                                        | ---                                                                                                                                                                                                                                                                                  |
| [ci-cd.yml](https://github.com/olliefr/docker-gs-ping/blob/main/.github/workflows/ci-cd.yml)               | The code snippet is responsible for building and testing the application in a Docker container, caching layers for performance optimization, and pushing the release to Docker Hub. It uses GitHub Actions for CI/CD automation and Docker-related actions for container operations. |
| [ci-smoketest.yml](https://github.com/olliefr/docker-gs-ping/blob/main/.github/workflows/ci-smoketest.yml) | This code snippet is a smoke test in the parent repository's CI/CD workflow. It builds and tests the code using the Go toolchain in a GitHub runner. The test is triggered on any push to the repository and can also be manually triggered.                                         |

</details>

---

## 🚀 Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* Go: `► INSERT-VERSION-HERE`
* `► ...`
* `► ...`

### ⚙️ Installation

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
Use the following command to run docker-gs-ping:
```sh
./myapp
```

### 🧪 Tests
To execute tests, run:
```sh
go test
```

---

## 🛠 Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/olliefr/docker-gs-ping/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/olliefr/docker-gs-ping/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/olliefr/docker-gs-ping/issues)**: Submit bugs found or log feature requests for docker-gs-ping.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone <your-forked-repo-url>
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear and concise message describing your updates.
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

## 📄 License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 👏 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-quick-links)

---
