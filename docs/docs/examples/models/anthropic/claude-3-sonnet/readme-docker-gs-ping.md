<div id="top">

<!-- HEADER STYLE: COMPACT -->
<img src="readmeai/assets/logos/rainbow.svg" width="30%" align="left" style="margin-right: 15px">

# DOCKER-GS-PING
<em>Containerize, Ping, Conquer: Mastering Docker's Heartbeat</em>

<!-- BADGES -->
<img src="https://img.shields.io/github/license/olliefr/docker-gs-ping?style=flat-square&logo=opensourceinitiative&logoColor=white&color=4169e1" alt="license">
<img src="https://img.shields.io/github/last-commit/olliefr/docker-gs-ping?style=flat-square&logo=git&logoColor=white&color=4169e1" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/olliefr/docker-gs-ping?style=flat-square&color=4169e1" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/olliefr/docker-gs-ping?style=flat-square&color=4169e1" alt="repo-language-count">

<em>Built with the tools and technologies:</em>

<img src="https://img.shields.io/badge/Go-00ADD8.svg?style=flat-square&logo=Go&logoColor=white" alt="Go">
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat-square&logo=Docker&logoColor=white" alt="Docker">
<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=flat-square&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions">

<br clear="left"/>

## 🟢 Table of Contents

1. [🟢 Table of Contents](#-table-of-contents)
2. [🟩 Overview](#-overview)
3. [💚 Features](#-features)
4. [🌿 Project Structure](#-project-structure)
    4.1. [🍃 Project Index](#-project-index)
5. [🌱 Getting Started](#-getting-started)
    5.1. [🌲 Prerequisites](#-prerequisites)
    5.2. [🎋 Installation](#-installation)
    5.3. [🎍 Usage](#-usage)
    5.4. [🌳 Testing](#-testing)
6. [🌴 Roadmap](#-roadmap)
7. [🌵 Contributing](#-contributing)
8. [🎄 License](#-license)
9. [✨ Acknowledgments](#-acknowledgments)

---

## 🟩 Overview

docker-gs-ping is a Go-based web application demonstrating containerization, testing, and deployment automation using Docker. It serves as a comprehensive Getting Started project for developers looking to master Docker best practices.

**Why docker-gs-ping?**

This project simplifies the process of containerizing Go applications while showcasing modern DevOps practices. The core features include:

- **🐳 Docker-compatible Go application:** Built with the Echo framework for easy containerization
- **🏗️ Multi-stage build process:** Optimizes image size for efficient deployment
- **🔄 Automated CI/CD workflow:** Streamlines testing and deployment to Docker Hub
- **🌐 Consistent deployment:** Ensures uniform execution across different environments
- **🔬 Quick integrity checks:** Implements smoke testing for rapid code verification

---

## 💚 Features

|      | Component       | Details                              |
| :--- | :-------------- | :----------------------------------- |
| ⚙️  | **Architecture**  | <ul><li>Go-based microservice</li><li>Containerized application</li><li>Multi-stage Docker build</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Go modules for dependency management</li><li>GitHub Actions for CI/CD</li></ul> |
| 📄 | **Documentation** | <ul><li>`Dockerfile` for container instructions</li><li>`Dockerfile.multistage` for optimized builds</li></ul> |
| 🔌 | **Integrations**  | <ul><li>GitHub Actions for automated workflows</li><li>Docker for containerization</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Go modules (`go.mod`, `go.sum`)</li><li>Separate Dockerfiles for different build strategies</li></ul> |
| 🧪 | **Testing**       | <ul><li>CI smoke tests (`ci-smoketest.yml`)</li><li>Automated testing in CI/CD pipeline</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Multi-stage Docker builds for smaller images</li><li>Use of `bytebufferpool` for efficient memory management</li></ul> |
| 🛡️ | **Security**      | <ul><li>JWT implementation</li><li>Use of `crypto` package</li></ul> |
| 📦 | **Dependencies**  | <ul><li>`github.com/labstack/echo/v4`</li><li>`golang.org/x/net`</li><li>`github.com/mattn/go-colorable`</li></ul> |

---

## 🌿 Project Structure

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

### 🍃 Project Index

<details open>
	<summary><b><code>DOCKER-GS-PING/</code></b></summary>
	<!-- __root__ Submodule -->
	<details>
		<summary><b>__root__</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ __root__</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/olliefr/docker-gs-ping/blob/master/go.mod'>go.mod</a></b></td>
					<td style='padding: 8px;'>- Defines module dependencies for the Docker Getting Started Ping project<br>- Specifies Go version 1.19 and lists required packages, including the primary dependency on Echo web framework<br>- Outlines indirect dependencies necessary for the projects functionality<br>- Ensures consistent package versions across development environments and facilitates reproducible builds for this containerized web application demonstrating Docker usage.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/olliefr/docker-gs-ping/blob/master/Dockerfile'>Dockerfile</a></b></td>
					<td style='padding: 8px;'>- Dockerfile defines the container environment for a Go application<br>- It sets up the Go runtime, copies necessary files, builds the application, and specifies the command to run<br>- The container exposes port 8080 for network communication<br>- This configuration ensures consistent deployment across different environments, encapsulating the application and its dependencies for easy distribution and execution.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/olliefr/docker-gs-ping/blob/master/go.sum'>go.sum</a></b></td>
					<td style='padding: 8px;'>- Manages dependencies and their versions for the Go project<br>- Lists required packages, including Echo web framework, JWT authentication, and various utility libraries<br>- Ensures consistent and reproducible builds by specifying exact versions of each dependency<br>- Facilitates easy project setup and maintenance by providing a comprehensive record of all external code used in the application.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/olliefr/docker-gs-ping/blob/master/Dockerfile.multistage'>Dockerfile.multistage</a></b></td>
					<td style='padding: 8px;'>- Dockerfile.multistage defines a multi-stage build process for a Go application<br>- It compiles the source code, runs tests, and creates a lean production image using a distroless base<br>- The final stage exposes port 8080 and sets up a non-root user for enhanced security<br>- This approach optimizes the build process and minimizes the final image size for efficient deployment.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/olliefr/docker-gs-ping/blob/master/main.go'>main.go</a></b></td>
					<td style='padding: 8px;'>- Serves as the entry point for a Docker-compatible web application using the Echo framework<br>- Configures routes for a root endpoint and a health check, sets up middleware for logging and recovery, and starts the server on a specified port<br>- Includes a utility function for finding the minimum of two integers, potentially for future use or testing purposes.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/olliefr/docker-gs-ping/blob/master/main_test.go'>main_test.go</a></b></td>
					<td style='padding: 8px;'>- Tests the IntMin function using unit tests in Go<br>- Includes a basic test case and a table-driven test with multiple scenarios<br>- Verifies that the function correctly returns the minimum of two integers across various input combinations<br>- Ensures the reliability and correctness of the IntMin function within the projects codebase.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- .github Submodule -->
	<details>
		<summary><b>.github</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ .github</b></code>
			<!-- workflows Submodule -->
			<details>
				<summary><b>workflows</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ .github.workflows</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/olliefr/docker-gs-ping/blob/master/.github/workflows/ci-cd.yml'>ci-cd.yml</a></b></td>
							<td style='padding: 8px;'>- Implements CI/CD workflow for automated testing and Docker image deployment<br>- Triggers on pushes to main branch and pull requests<br>- Builds the application, runs tests in a Docker container, and if successful, pushes the image to Docker Hub<br>- Utilizes caching for efficient builds and applies semantic versioning for image tagging<br>- Ensures code quality and streamlines release process for the project.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/olliefr/docker-gs-ping/blob/master/.github/workflows/ci-smoketest.yml'>ci-smoketest.yml</a></b></td>
							<td style='padding: 8px;'>- Defines a GitHub Actions workflow for continuous integration smoke testing<br>- Triggers on any push to the repository or manual activation<br>- Executes a basic build and test process using the Go toolchain directly in the GitHub runner<br>- Ensures code integrity by performing a quick check of the projects buildability and test suite functionality after each code change or on-demand.</td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---

## 🌱 Getting Started

### 🌲 Prerequisites

This project requires the following dependencies:

- **Programming Language:** Go
- **Package Manager:** Go modules
- **Container Runtime:** Docker

### 🎋 Installation

Build docker-gs-ping from the source and intsall dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/olliefr/docker-gs-ping
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd docker-gs-ping
    ```

3. **Install the dependencies:**

<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![docker][docker-shield]][docker-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [docker-shield]: https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white -->
	<!-- [docker-link]: https://www.docker.com/ -->

	**Using [docker](https://www.docker.com/):**

	```sh
	❯ docker build -t olliefr/docker-gs-ping .
	```
<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![go modules][go modules-shield]][go modules-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [go modules-shield]: https://img.shields.io/badge/Go-00ADD8.svg?style={badge_style}&logo=go&logoColor=white -->
	<!-- [go modules-link]: https://golang.org/ -->

	**Using [go modules](https://golang.org/):**

	```sh
	❯ go build
	```

### 🎍 Usage

Run the project with:

**Using [docker](https://www.docker.com/):**
```sh
docker run -it {image_name}
```
**Using [go modules](https://golang.org/):**
```sh
go run {entrypoint}
```

### 🌳 Testing

Docker-gs-ping uses the {__test_framework__} test framework. Run the test suite with:

**Using [go modules](https://golang.org/):**
```sh
go test ./...
```

---

## 🌴 Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🌵 Contributing

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

## 🎄 License

Docker-gs-ping is protected under the [LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## ✨ Acknowledgments

- Credit `contributors`, `inspiration`, `references`, etc.

<div align="left"><a href="#top">⬆ Return</a></div>

---

<!-- README-AI COMMAND: -->
<!--
```sh
readmeai \
    --repository 'https://github.com/olliefr/docker-gs-ping' \
    --output 'docs/docs/examples/ai-providers/anthropic/claude-3-sonnet/readme-docker-gs-ping.md' \
    --badge-style 'flat-square' \
    --badge-color '4169e1' \
    --logo 'RAINBOW' \
    --header-style 'COMPACT' \
    --navigation-style 'NUMBER' \
    --emojis 'forest' \
    --temperature 0.131 \
    --tree-max-depth 5 \
    --api anthropic \
    --model claude-3-5-sonnet-20240620
```
-->
