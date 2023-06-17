
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
docker-gs-ping
</h1>
<h3 align="center">📍 Stay connected with docker-gs-ping on GitHub, the ultimate ping tester!</h3>
<h3 align="center">🚀 Developed with the software and tools below:</h3>

<p align="center">
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=for-the-badge&logo=Docker&logoColor=white" alt="Docker" />
<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=for-the-badge&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions" />
<img src="https://img.shields.io/badge/Go-00ADD8.svg?style=for-the-badge&logo=Go&logoColor=white" alt="Go" />
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

The docker-gs-ping project is a Golang application that can be built into a Docker image using one of two provided Dockerfiles. The application serves as a basic HTTP server that responds to GET requests with a "pong" message. The value proposition of the project is its ease of use and portability, allowing developers to quickly spin up a simple HTTP server in a Docker container. Additionally, the project includes automated testing and deployment workflows using GitHub Actions.

---

## 🔮 Features

Feature | Description |
|---|---|
| **🏗 Overall Structure and Organization** | The codebase follows the standard organization structure for a Golang application, with separate directories for the main package, tests, and Dockerfiles. |
| **📝 Code Documentation** | The codebase lacks comprehensive documentation, with only basic comments explaining the purpose of some functions. |
| **🧩 Dependency Management** | The codebase uses Go modules for dependency management, with explicit version requirements for each package. |
| **♻️ Code Modularity and Reusability** | The codebase demonstrates modularity and reusability, with separate functions for handling HTTP requests and responses, and reusable functions for error handling and logging. |
| **✅ Testing and Quality Assurance** | The codebase includes unit tests for some functions and uses GitHub Actions for continuous integration and deployment. |
| **⚡️ Performance and Optimization** | The codebase does not include any explicit performance optimization techniques, but using a lean distroless base image in the multistage Dockerfile can improve performance and reduce image size. |
| **🔒 Security Measures** | The codebase does not include any explicit security measures, such as input validation or encryption, but using the distroless base image can improve security by reducing the attack surface. |
| **🔄 Version Control and Collaboration** | The codebase uses Git for version control and GitHub for collaboration, with clear commit messages and pull request descriptions. |
| **🔌 External Integrations** | The codebase integrates with Docker Hub for image hosting and uses the Echo framework for handling HTTP requests. |
| **📈 Scalability and Extensibility** | The codebase demonstrates extensibility, with separate functions for handling different HTTP requests, and scalability, with the ability to deploy the application as a Docker container. |

---


<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## ⚙️ Project Structure


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

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 💻 Modules

<details closed><summary>Root</summary>

| File                  | Summary                                                                                                                                                                                                                                                                                                                                                                                                                      | Module                |
|:----------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
| go.mod                | The code snippet is a Go module with a requirement for the Echo framework version 4.10.2. It also has indirect requirements for various other packages such as JWT, byte buffer pool, and crypto. The purpose and functionality of the module is not evident from the provided code.                                                                                                                                         | go.mod                |
| Dockerfile            | This code snippet is a Dockerfile that builds a Docker image for a Golang application. It sets the working directory, downloads Go modules, copies the source code, builds the application, exposes a default TCP port, and sets the default command to run the application.                                                                                                                                                 | Dockerfile            |
| Dockerfile.multistage | The code snippet is a Dockerfile that builds a Go application from source, runs tests in a container, and deploys the application binary into a lean image using distroless base image. The final image exposes port 8080 and sets a non-root user as the entrypoint for the application.                                                                                                                                    | Dockerfile.multistage |
| main.go               | HTTP 429 error when fetching summary.                                                                                                                                                                                                                                                                                                                                                                                        | main.go               |
| main_test.go          | The code snippet provides two functions for unit testing a function called IntMin. The first TestIntMinBasic function tests the IntMin function with specific inputs and checks if the output is as expected. The second TestIntMinTableDriven function uses a table-driven approach to test multiple inputs and expected outputs using a loop and the t.Run function. The testing package is imported to execute the tests. | main_test.go          |

</details>

<details closed><summary>Workflows</summary>

| File             | Summary                                                                                                                                                                                                                                                                                                                                                                  | Module                             |
|:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------|
| ci-cd.yml        | The provided code snippet is a GitHub Actions workflow that executes when code is pushed to the main branch or a tag starting with "v". The workflow builds and tests a Docker image using a multistage Dockerfile and caches the layers for faster builds. If the tests pass, the workflow logs in to Docker Hub and pushes the image with appropriate labels and tags. | .github/workflows/ci-cd.yml        |
| ci-smoketest.yml | The code snippet provides a GitHub Actions workflow that runs a smoke test on any push to the repository, or can be manually triggered. This workflow builds and tests a Go application directly in the GitHub runner. It includes steps for checking out the code, installing Go, fetching required Go modules, building, and testing the application.                  | .github/workflows/ci-smoketest.yml |

</details>

<hr />

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> `[📌  INSERT-PROJECT-PREREQUISITES]`

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

### 🤖 Using docker-gs-ping

```sh
./myapp
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

[📌  INSERT-DESCRIPTION]


---

