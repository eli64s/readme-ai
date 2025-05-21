[<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="right" width="25%" padding-right="350">]()

# `DOCKER-GS-PING`

#### Containerize, Scale, and Thrive with Ease!

<p align="left">
	<img src="https://img.shields.io/github/license/olliefr/docker-gs-ping?style=for-the-badge&logo=opensourceinitiative&logoColor=white&color=00ADD8" alt="license">
	<img src="https://img.shields.io/github/last-commit/olliefr/docker-gs-ping?style=for-the-badge&logo=git&logoColor=white&color=00ADD8" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/olliefr/docker-gs-ping?style=for-the-badge&color=00ADD8" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/olliefr/docker-gs-ping?style=for-the-badge&color=00ADD8" alt="repo-language-count">
</p>
<p align="left">
		<em>_Built with:_</em>
</p>
<p align="left">
	<img src="https://img.shields.io/badge/Go-00ADD8.svg?style=for-the-badge&logo=Go&logoColor=white" alt="Go">
	<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=for-the-badge&logo=Docker&logoColor=white" alt="Docker">
	<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=for-the-badge&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions">

</p>
<br>

## 🔗 Table of Contents

I. [📍 Overview](#-overview)
II. [👾 Features](#-features)
III. [📁 Project Structure](#-project-structure)
IV. [🚀 Getting Started](#-getting-started)
V. [📌 Project Roadmap](#-project-roadmap)
VI. [🔰 Contributing](#-contributing)
VII. [🎗 License](#-license)
VIII. [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

docker-gs-ping is a project that simplifies deploying a Go application in a Docker container. It offers easy scalability and efficient testing. Ideal for developers seeking streamlined containerized application deployment.

---

## 👾 Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Uses a **multi-stage Docker** process for building, testing, and deploying the application</li><li>Implements an **HTTP server** using the Echo framework with middleware for logging and recovery</li><li>Follows a **modular structure** with defined routes for root and health endpoints</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Defines project dependencies and versions in the `go.mod` file for proper package management</li><li>Includes unit tests in `main_test.go` to ensure code correctness</li><li>Follows best practices for Go programming, such as error handling and code readability</li></ul> |
| 📄 | **Documentation** | <ul><li>Provides detailed **documentation** for installation, usage, and testing using `go modules` and `docker`</li><li>Includes **usage commands** for running the application locally with `go run` or `docker run`</li><li>Offers **test commands** for running tests using `go test`</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Automates Docker image release to Docker Hub using **GitHub Actions** in the `ci-cd.yml` workflow</li><li>Automates smoke testing with the `ci-smoketest.yml` workflow for every push or manual trigger</li><li>Ensures secure handling of Docker image metadata, caching, build, test, login, and push operations</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Organizes codebase into separate files like `main.go` and `main_test.go` for better maintainability</li><li>Utilizes middleware and routing to achieve **separation of concerns**</li><li>Encourages **code reusability** through functions like finding the minimum of two integers</li></ul> |
| 🧪 | **Testing**       | <ul><li>Includes unit tests in `main_test.go` to verify the correctness of functions like `IntMin`</li><li>Uses `go test` command for running tests across the codebase</li><li>Ensures code stability and reliability through comprehensive test coverage</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Optimizes performance by exposing port 8080 for runtime communication</li><li>Utilizes **non-root user** setup in the multi-stage Docker process for enhanced security and efficiency</li><li>Follows best practices for **Go application performance** tuning</li></ul> |
| 🛡️ | **Security**      | <ul><li>Implements a **non-root user** setup in the Dockerfile for enhanced container security</li><li>Follows **security best practices** for Go applications, such as input validation and secure error handling</li><li>Ensures secure handling of Docker image operations in the CI/CD workflows</li></ul> |

---

## 📁 Project Structure

```sh
└── docker-gs-ping/
    ├── .github
    │   └── workflows
    │       ├── ci-cd.yml
    │       └── ci-smoketest.yml
    ├── Dockerfile
    ├── Dockerfile.multistage
    ├── LICENSE
    ├── README.md
    ├── go.mod
    ├── go.sum
    ├── main.go
    └── main_test.go
```


### 📂 Project Index
<details open>
	<summary><b><code>DOCKER-GS-PING/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/olliefr/docker-gs-ping/blob/master/go.mod'>go.mod</a></b></td>
				<td>Define project dependencies and versions using the go.mod file, ensuring proper package management and compatibility within the codebase architecture.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/olliefr/docker-gs-ping/blob/master/Dockerfile'>Dockerfile</a></b></td>
				<td>- Facilitates building and running a Go application in a Docker container<br>- Downloads Go modules, copies source code, builds the application, and exposes port 8080 for runtime communication<br>- Allows easy deployment and scaling of the application within a containerized environment.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/olliefr/docker-gs-ping/blob/master/go.sum'>go.sum</a></b></td>
				<td>Manage project dependencies and versions using the provided go.sum file, ensuring compatibility and stability across the codebase architecture.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/olliefr/docker-gs-ping/blob/master/Dockerfile.multistage'>Dockerfile.multistage</a></b></td>
				<td>- Builds, tests, and deploys a Go application in a multi-stage Docker process<br>- Fetches dependencies, compiles the application, runs tests, and packages it into a minimal container image<br>- The resulting image exposes port 8080 and runs the application as a non-root user.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/olliefr/docker-gs-ping/blob/master/main.go'>main.go</a></b></td>
				<td>- Implements a basic HTTP server using the Echo framework with middleware for logging and recovery<br>- Defines routes for root and health endpoints<br>- Retrieves the port from the environment variable or defaults to 8080<br>- Starts the server on the specified port<br>- Includes a function for finding the minimum of two integers.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/olliefr/docker-gs-ping/blob/master/main_test.go'>main_test.go</a></b></td>
				<td>- Unit tests in main_test.go verify the correctness of the IntMin function through basic and table-driven scenarios<br>- These tests ensure that the function accurately determines the minimum value between two integers.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- .github Submodule -->
		<summary><b>.github</b></summary>
		<blockquote>
			<details>
				<summary><b>workflows</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/olliefr/docker-gs-ping/blob/master/.github/workflows/ci-cd.yml'>ci-cd.yml</a></b></td>
						<td>- Automates Docker image release to Docker Hub based on successful tests, following a CI/CD workflow triggered by pushes to the main branch or version tags<br>- Handles Docker image metadata, caching, build, test, login, and push operations securely using GitHub Actions.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/olliefr/docker-gs-ping/blob/master/.github/workflows/ci-smoketest.yml'>ci-smoketest.yml</a></b></td>
						<td>- Automates smoke testing for the project by building and testing Go code on every push or manual trigger<br>- Uses GitHub Actions to streamline the process in the CI pipeline.</td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---
## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with docker-gs-ping, ensure your runtime environment meets the following requirements:

- **Programming Language:** Go
- **Package Manager:** Go modules
- **Container Runtime:** Docker


### ⚙️ Installation

Install docker-gs-ping using one of the following methods:

**Build from source:**

1. Clone the docker-gs-ping repository:
```sh
❯ git clone https://github.com/olliefr/docker-gs-ping
```

2. Navigate to the project directory:
```sh
❯ cd docker-gs-ping
```

3. Install the project dependencies:


**Using `go modules`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Go-00ADD8.svg?style={badge_style}&logo=go&logoColor=white" />](https://golang.org/)

```sh
❯ go build
```


**Using `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker build -t olliefr/docker-gs-ping .
```




### 🤖 Usage
Run docker-gs-ping using the following command:
**Using `go modules`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Go-00ADD8.svg?style={badge_style}&logo=go&logoColor=white" />](https://golang.org/)

```sh
❯ go run {entrypoint}
```


**Using `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker run -it {image_name}
```


### 🧪 Testing
Run the test suite using the following command:
**Using `go modules`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Go-00ADD8.svg?style={badge_style}&logo=go&logoColor=white" />](https://golang.org/)

```sh
❯ go test ./...
```


## 📌 Project Roadmap
- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/olliefr/docker-gs-ping/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/olliefr/docker-gs-ping/issues)**: Submit bugs found or log feature requests for the `docker-gs-ping` project.
- **💡 [Submit Pull Requests](https://github.com/olliefr/docker-gs-ping/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

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

## 🎗 License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 🙌 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---
