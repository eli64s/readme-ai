<p align="center">
  <img src="https://img.icons8.com/external-tal-revivo-filled-tal-revivo/96/external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-filled-tal-revivo.png" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">DOCKER-GS-PING</h1>
</p>
<p align="center">
    <em>Deploy. Ping. Simplified. Docker-gs-ping.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/olliefr/docker-gs-ping?style=for-the-badge&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/olliefr/docker-gs-ping?style=for-the-badge&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/olliefr/docker-gs-ping?style=for-the-badge&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/olliefr/docker-gs-ping?style=for-the-badge&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=for-the-badge&logo=Docker&logoColor=white" alt="Docker">
	<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=for-the-badge&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions">
	<img src="https://img.shields.io/badge/Go-00ADD8.svg?style=for-the-badge&logo=Go&logoColor=white" alt="Go">
</p>

<!-- TABLE OF CONTENTS -->
<details>
   <summary>Table of Contents</summary>

- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [🧩 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
  - [⚙️ Install](#️-install)
  - [► Using docker-gs-ping](#-using-docker-gs-ping)
  - [🧪 Tests](#-tests)
- [🛠 Project Roadmap](#-project-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)
</details>
<hr>

## 📍 Overview

The **docker-gs-ping** project is a Dockerized Go application that leverages the Echo framework to create an HTTP server with basic endpoints. The project's core functionality includes building, testing, and deploying the application using multistage Dockerfiles. It incorporates middleware for logging and recovery, along with a custom integer minimum function. The repository includes automated CI/CD workflows for testing and deployment, ensuring the application's integrity. With its streamlined Docker container deployment and robust testing processes, docker-gs-ping offers a reliable solution for building and scaling Go web applications efficiently.

---

## 📦 Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | *The project follows a containerized architecture using Docker, with a focus on building and deploying a Go application with exposed port 8080 for listening. It includes a multistage Dockerfile for efficient image builds.* |
| 🔩 | **Code Quality**  | *The codebase maintains good quality and style with unit tests for basic and table-driven scenarios. Includes middleware setup for logging and recovery and a focus on accurate functionality.* |
| 📄 | **Documentation** | *The project provides good documentation, including a detailed go.mod file defining dependencies, Dockerfile descriptions, test scenarios, and automated CI/CD workflows using GitHub Actions.* |
| 🔌 | **Integrations**  | *Key integrations and dependencies include Echo v4, jwt, gommon, and more for building an HTTP server. External integrations like GitHub Actions streamline testing and deployment processes.* |
| 🧩 | **Modularity**    | *The codebase is modular and reusable, evident from the structured setup of endpoints, middleware, and the integer minimum function implementation. Promotes code reusability and scalability.* |
| 🧪 | **Testing**       | *Unit tests are implemented for ensuring accurate functionality of the codebase. Testing frameworks and tools used for validating the IntMin function and overall system integrity.* |
| ⚡️  | **Performance**   | *Efficiently handles resource usage with a multistage Dockerfile for building, testing, and deploying. Employs middleware for logging and recovery, ensuring a fast and reliable HTTP server setup.* |
| 🛡️ | **Security**      | *Security measures include dependency checksums generated from go.sum for Docker image builds, ensuring secure and reliable deployment. Integrations like jwt provide additional security features.* |
| 📦 | **Dependencies**  | *Key external libraries and dependencies include Echo v4, jwt, gommon, crypto packages, among others. Dependency management via go.mod and go.sum files for streamlined builds.* |

---

## 📂 Repository Structure

```sh
└── docker-gs-ping/
    ├── .github
    │   └── workflows
    ├── Dockerfile
    ├── Dockerfile.multistage
    ├── LICENSE
    ├── README.md
    ├── go.mod
    ├── go.sum
    ├── main.go
    └── main_test.go
```

---

## 🧩 Modules

<details closed><summary>.</summary>

| File                                                                                                 | Summary                                                                                                                                                         |
| ---                                                                                                  | ---                                                                                                                                                             |
| [go.mod](https://github.com/olliefr/docker-gs-ping/blob/master/go.mod)                               | Docker-gs-ping's go.mod defines dependencies for Echo v4, jwt, gommon, and more.                                                                                |
| [Dockerfile](https://github.com/olliefr/docker-gs-ping/blob/master/Dockerfile)                       | Builds a Go application in a Docker container, enabling easy deployment with exposed port 8080 for listening.                                                   |
| [go.sum](https://github.com/olliefr/docker-gs-ping/blob/master/go.sum)                               | Generates dependencies checksums from go.sum for Docker image builds in the parent repository.                                                                  |
| [Dockerfile.multistage](https://github.com/olliefr/docker-gs-ping/blob/master/Dockerfile.multistage) | Multistage Dockerfile for building, testing, and deploying Go application into a minimal image with distroless base.                                            |
| [main.go](https://github.com/olliefr/docker-gs-ping/blob/master/main.go)                             | Implements an HTTP server using Echo framework with basic endpoints. Includes middleware setup for logging and recovery. Incorporated integer minimum function. |
| [main_test.go](https://github.com/olliefr/docker-gs-ping/blob/master/main_test.go)                   | Unit tests for basic and table-driven scenarios, ensuring accurate functionality of the IntMin function within the repository's architecture.                   |

</details>

<details closed><summary>.github.workflows</summary>

| File                                                                                                         | Summary                                                                                                                                    |
| ---                                                                                                          | ---                                                                                                                                        |
| [ci-cd.yml](https://github.com/olliefr/docker-gs-ping/blob/master/.github/workflows/ci-cd.yml)               | Automated CI/CD workflows configured for the Dockerized Go application using GitHub Actions. Streamlines testing and deployment processes. |
| [ci-smoketest.yml](https://github.com/olliefr/docker-gs-ping/blob/master/.github/workflows/ci-smoketest.yml) | Automated CI smoketest workflow ensures the Dockerized Go application's functionality and integrity.                                       |

</details>

---

## 🚀 Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Go**: `version x.y.z`

### ⚙️ Install

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

### ► Using `docker-gs-ping`

Use the following command to run docker-gs-ping:

```sh
./myapp
```

### 🧪 Tests

Use the following command to run tests:

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

- **[Report Issues](https://github.com/olliefr/docker-gs-ping/issues)**: Submit bugs found or log feature requests for the `docker-gs-ping` project.
- **[Submit Pull Requests](https://github.com/olliefr/docker-gs-ping/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/olliefr/docker-gs-ping/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/olliefr/docker-gs-ping
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/olliefr/docker-gs-ping/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=olliefr/docker-gs-ping">
   </a>
</p>
</details>

---

## 📄 License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 👏 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-overview)

---
