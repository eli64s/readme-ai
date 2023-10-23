<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>DOCKER-GS-PING</h1>
<h3>◦ Instantly ping and stay connected!</h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=for-the-badge&logo=YAML&logoColor=white" alt="YAML" />
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=for-the-badge&logo=Docker&logoColor=white" alt="Docker" />
<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=for-the-badge&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions" />
<img src="https://img.shields.io/badge/Go-00ADD8.svg?style=for-the-badge&logo=Go&logoColor=white" alt="Go" />
</p>
<img src="https://img.shields.io/github/license/olliefr/docker-gs-ping?style=for-the-badge&color=5D6D7E" alt="GitHub license" />
<img src="https://img.shields.io/github/last-commit/olliefr/docker-gs-ping?style=for-the-badge&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/olliefr/docker-gs-ping?style=for-the-badge&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/languages/top/olliefr/docker-gs-ping?style=for-the-badge&color=5D6D7E" alt="GitHub top language" />
</div>

---

##  Table of Contents
- [Table of Contents](#table-of-contents)
- [Overview](#overview)
- [Features](#features)
- [Repository Structure](#repository-structure)
- [Modules](#modules)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Running docker-gs-ping](#running-docker-gs-ping)
  - [Tests](#tests)
- [Project Roadmap](#project-roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---


##  Overview

The repository is a Dockerized Go application that serves as a ping service. It uses the Echo framework to implement a simple web server with two routes ("/" and "/health"). The code includes unit tests for the main function and follows a multi-stage Docker build process. It also includes GitHub Actions workflow files for CI/CD and smoke testing, enabling automated build, test, and release processes. The repository's value proposition lies in its ability to easily containerize and deploy a Go application with built-in CI/CD and testing capabilities.

---

##  Features

|    | Feature            | Description                                                                                                        |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The codebase follows a modular design pattern, with separate files for the Dockerfile, main application code, and test code. The application is built as a Go module, using the Echo framework for the web server. This architecture allows for easy maintenance and scalability.|
| 📄 | **Documentation**  | The codebase includes a README.md file that provides basic information about the project and how to run it. The individual files also have comments explaining their purpose and functionality. However, the documentation could be more comprehensive, especially regarding the choice of architectural patterns and design decisions.|
| 🔗 | **Dependencies**   | The codebase has several external dependencies, such as GitHub Actions for CI/CD workflows, the Echo framework for the web server, and various Go packages for testing and other functionalities. The dependencies are managed using a go.sum file, which ensures reproducible builds and version control. |
| 🧩 | **Modularity**     | The codebase is well-organized into separate files for different components, such as Dockerfile, main application code, and test code. This modular structure allows for easier code maintenance, testing, and code reuse. |
| 🧪 | **Testing**        | The codebase includes unit tests for the main application code, implemented in the main_test.go file. The tests cover different scenarios, including basic functionality and table-driven tests. The testing framework used is the standard Go testing package. |
| ⚡️  | **Performance**    | The codebase does not have any explicit performance optimizations. However, being built in Go, it benefits from the language's inherent performance advantages, such as efficient concurrency handling and memory management. The lightweight Echo framework also contributes to the overall performance of the application.|
| 🔐 | **Security**       | The codebase uses secure coding practices, such as validating user inputs and using encryption libraries like golang.org/x/crypto. However, without further analysis, it's challenging to determine the full extent of security measures implemented in the system. Proper access controls and other security measures should be added as required. |
| 🔀 | **Version Control**| The codebase is hosted on GitHub and uses GitHub Actions for Continuous Integration and Continuous Deployment (CI/CD) workflows. The codebase follows standard Git version control practices and includes a .gitignore file to exclude unnecessary files from version control. |
| 🔌 | **Integrations**   | The codebase integrates with external services like Docker Hub and GitHub Actions. Docker Hub is used to store and distribute the Docker images created from the codebase, while GitHub Actions automates the build, test, and release processes. These integrations enhance the development workflow and enable seamless deployment of the application. |
| 📶 | **Scalability**    | The codebase exhibits potential for scalability. The modular design and use of a lightweight framework like Echo make it easier to scale the application horizontally by deploying multiple instances. However, to achieve true scalability, additional factors such as data storage and load balancing need to be considered. |

---


##  Repository Structure

```sh
└── ./
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


##  Modules

<details closed><summary>Root</summary>

| File                                                                                               | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---                                                                                                | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [go.mod](https://github.com/olliefr/docker-gs-ping/blob/main/go.mod)                               | The code is a Go module with the module name "github.com/olliefr/docker-gs-ping" and requires the package "github.com/labstack/echo/v4" version 4.10.2. It also has several other indirect dependencies such as "github.com/golang-jwt/jwt" and "golang.org/x/crypto". The code exists within a directory structure that includes various files like Dockerfiles, a main.go file, and a main_test.go file.                                                                                       |
| [Dockerfile](https://github.com/olliefr/docker-gs-ping/blob/main/Dockerfile)                       | The Dockerfile is used to create a Docker image for a Go application. It starts with a base image of golang:1.19. It sets the working directory to /app and downloads Go modules. It then copies the source code and builds the application using CGO_ENABLED=0 to disable CGO and GOOS=linux to build for Linux. It exposes port 8080 and specifies the command to run the application as "/docker-gs-ping".                                                                                    |
| [go.sum](https://github.com/olliefr/docker-gs-ping/blob/main/go.sum)                               | The code is a go.sum file that lists the specific versions of external packages that are used in a project. It includes versions of packages like go-spew, golang-jwt/jwt, labstack/echo/v4, and many others. Each line specifies the package name, version, and a unique identifier (h1). This file ensures that the project uses the specified versions of these packages for reproducible builds and to avoid breaking changes.                                                               |
| [Dockerfile.multistage](https://github.com/olliefr/docker-gs-ping/blob/main/Dockerfile.multistage) | The code consists of a Docker multi-stage build process. The first stage builds the application from source, utilizing a Golang image, while the second stage runs the tests within the container. The final stage deploys the application binary into a lean image, utilizing the `gcr.io/distroless/base-debian11` image. The resulting image exposes port 8080 and runs the application as the `nonroot` user. The application is a ping service that will be executed when the image is run. |
| [main.go](https://github.com/olliefr/docker-gs-ping/blob/main/main.go)                             | The code consists of a simple web server implemented using the Echo framework in Go. It initializes a new Echo instance, sets up middleware for logging and error recovery, and defines two routes-"/" and "/health"-that return HTTP responses. It also includes a main function that starts the server on a specified port (defaulting to 8080) and an auxiliary function that calculates the minimum of two integers.                                                                         |
| [main_test.go](https://github.com/olliefr/docker-gs-ping/blob/main/main_test.go)                   | The code contains unit tests for the `IntMin` function. The first test, `TestIntMinBasic`, checks if the function correctly returns the minimum value between two integers. The second test, `TestIntMinTableDriven`, includes a table of test cases with inputs and expected outputs. Each test case is executed, and the function's output is compared against the expected result. Any mismatches are reported as errors.                                                                     |

</details>

<details closed><summary>Workflows</summary>

| File                                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---                                                                                                        | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [ci-cd.yml](https://github.com/olliefr/docker-gs-ping/blob/main/.github/workflows/ci-cd.yml)               | The code is a GitHub Actions workflow file that automates the build, test, and release process for a Dockerized application. The workflow runs on push events for the'main' branch and tags starting with'v'. It includes steps to checkout code, retrieve Docker metadata, set up Docker Buildx, cache Docker layers, build the application and run tests in Docker, login to Docker Hub, and push the release to Docker Hub. The workflow ensures that the release is only pushed if the event is not a pull request. |
| [ci-smoketest.yml](https://github.com/olliefr/docker-gs-ping/blob/main/.github/workflows/ci-smoketest.yml) | The code above represents a GitHub workflow file ("ci-smoketest.yml") that runs a smoke test for a Go project. The workflow is triggered on any push to the repository or manually. It runs on an Ubuntu environment and consists of several steps: checking out the code, installing Go using the version specified in the "go.mod" file, fetching required Go modules, building the project, and then running tests on it.                                                                                            |

</details>

---

##  Getting Started

***Dependencies***

Please ensure you have the following dependencies installed on your system:

`- ℹ️ Dependency 1`

`- ℹ️ Dependency 2`

`- ℹ️ ...`

###  Installation

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

###  Running docker-gs-ping

```sh
./myapp
```

###  Tests
```sh
go test
```

---


##  Project Roadmap

> - [X] `ℹ️  Task 1: Implement X`
> - [ ] `ℹ️  Task 2: Implement Y`
> - [ ] `ℹ️ ...`


---

##  Contributing

[**Discussions**](https://github.com/olliefr/docker-gs-ping/discussions)
  - Join the discussion here.

[**New Issue**](https://github.com/olliefr/docker-gs-ping/issues)
  - Report a bug or request a feature here.

[**Contributing Guidelines**](https://github.com/olliefr/docker-gs-ping/blob/main/CONTRIBUTING.md)

- Contributions are welcome! Please follow these steps:

1. Fork the project repository to your GitHub account.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive such as `new-feature-x` or `bugfix-issue-x`.
```sh
git checkout -b new-feature-x
```
4. Develop your changes locally.
5. Commit your updates with a clear explanation of the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub.
```sh
git push origin new-feature-x
```
7. Create a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
8. Once your pull request is reviewed, it will be merged into the main branch of the project repository.

---

##  License


This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#Top)

---
