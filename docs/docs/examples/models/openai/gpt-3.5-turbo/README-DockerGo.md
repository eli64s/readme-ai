<div id="top">

<!-- HEADER STYLE: CLASSIC -->
<div align="center">

<img src="../../../../../../readmeai/assets/logos/purple.svg" width="30%" style="position: relative; top: 0; right: 0;" alt="Project Logo"/>

# DOCKER-GS-PING

<em>Optimize Go app performance effortlessly with Docker-Gs-Ping.</em>

<!-- BADGES -->
<img src="https://img.shields.io/github/license/olliefr/docker-gs-ping?style=flat&logo=opensourceinitiative&logoColor=white&color=0d47a1" alt="license">
<img src="https://img.shields.io/github/last-commit/olliefr/docker-gs-ping?style=flat&logo=git&logoColor=white&color=0d47a1" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/olliefr/docker-gs-ping?style=flat&color=0d47a1" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/olliefr/docker-gs-ping?style=flat&color=0d47a1" alt="repo-language-count">

<em>Technology Stack:</em>

<img src="https://img.shields.io/badge/Go-00ADD8.svg?style=flat&logo=Go&logoColor=white" alt="Go">
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white" alt="Docker">
<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=flat&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions">

</div>
<br>

---

## 🔵 Table of Contents

<details>
<summary>Table of Contents</summary>

- [🔵 Table of Contents](#-table-of-contents)
- [🟢 Overview](#-overview)
- [🟡 Features](#-features)
- [🟠 Project Structure](#-project-structure)
    - [🔴 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
    - [🟣 Prerequisites](#-prerequisites)
    - [🟤 Installation](#-installation)
    - [⚫ Usage](#-usage)
    - [⚪ Testing](#-testing)
- [🌈 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)
- [✨ Acknowledgments](#-acknowledgments)

</details>

---

## 🟢 Overview

docker-gs-ping is a comprehensive tool designed to streamline Docker image management and enhance Go application deployment processes.

**Why docker-gs-ping?**

This project excels at simplifying Docker image building and Go application deployment. Key features include:

- 📦 Efficient dependency management for seamless integration
- 🚀 Automated CI/CD workflows for Docker Hub releases and smoke testing
- 🛠️ Multi-stage Docker builds for optimized deployment

---

## 🟡 Features

|      | Component       | Details                              |
| :--- | :-------------- | :----------------------------------- |
| ⚙️  | **Architecture**  | <ul><li>Follows a **multistage Dockerfile** pattern</li><li>**Separation of concerns** between build and runtime stages</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Consistent **Go coding conventions**</li><li>Use of **Go modules** for dependency management</li></ul> |
| 📄 | **Documentation** | <ul><li>Includes detailed **Dockerfile** and **Dockerfile.multistage** documentation</li></ul> |
| 🔌 | **Integrations**  | <ul><li>**GitHub Actions** for CI/CD in `.github/workflows/ci-cd.yml` and `ci-smoketest.yml`</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Well-structured codebase with **modular components**</li></ul> |
| 🧪 | **Testing**       | <ul><li>Presence of **smoke tests** in the CI pipeline</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Efficient use of **Go standard libraries** for performance optimization</li></ul> |
| 🛡️ | **Security**      | <ul><li>Utilizes **secure coding practices** in Go</li></ul> |
| 📦 | **Dependencies**  | <ul><li>Relies on dependencies like `bytebufferpool`, `crypto`, `fasttemplate`, etc., managed via **Go modules**</li></ul> |

---

## 🟠 Project Structure

```sh
└── docker-gs-ping/
    ├── .github
    ├── Dockerfile
    ├── Dockerfile.multistage
    ├── LICENSE
    ├── README.md
    ├── go.mod
    ├── go.sum
    ├── main.go
    └── main_test.go
```

### 🔴 Project Index

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
					<td style='padding: 8px;'>Define project dependencies and version constraints in the go.mod file for seamless integration and package management within the Docker-Gs-Ping module.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/olliefr/docker-gs-ping/blob/master/Dockerfile'>Dockerfile</a></b></td>
					<td style='padding: 8px;'>- Build a Docker image for a Go application, defining dependencies, setting up the working directory, copying source files, and exposing port 8080<br>- Use the provided Dockerfile to streamline the setup process and ensure the application runs smoothly within the container environment.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/olliefr/docker-gs-ping/blob/master/go.sum'>go.sum</a></b></td>
					<td style='padding: 8px;'>- Manage third-party dependencies and versions using the go.sum file within the project structure<br>- This file lists the exact versions of external packages required for the codebase, ensuring reliable and consistent functionality across different environments.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/olliefr/docker-gs-ping/blob/master/Dockerfile.multistage'>Dockerfile.multistage</a></b></td>
					<td style='padding: 8px;'>- Builds, tests, and deploys a Go application in a multi-stage Docker build<br>- Initializes a base image for building the app, runs tests, and generates a slim deployment image using a distroless base<br>- Hosts the application on port 8080 with a non-root user.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/olliefr/docker-gs-ping/blob/master/main.go'>main.go</a></b></td>
					<td style='padding: 8px;'>- Define a web server using Echo framework, handling root and health endpoints<br>- The server listens on a specified port, defaulting to 8080<br>- Additionally, includes a basic function to calculate the minimum of two integers.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/olliefr/docker-gs-ping/blob/master/main_test.go'>main_test.go</a></b></td>
					<td style='padding: 8px;'>- Defines unit tests for the <code>IntMin</code> function, covering basic and table-driven scenarios<br>- Validates expected outputs against inputs<br>- Improves code reliability by ensuring correct functionality under various conditions<br>- Facilitates identifying and fixing potential issues early in development.</td>
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
							<td style='padding: 8px;'>- Automates Docker Hub releases based on successful tests for the projects main branch and version tags<br>- Handles Docker image metadata, caching, building, testing, and pushing to Docker Hub<br>- Configured to trigger on push events to main' branch and v* tags, as well as pull requests to main.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/olliefr/docker-gs-ping/blob/master/.github/workflows/ci-smoketest.yml'>ci-smoketest.yml</a></b></td>
							<td style='padding: 8px;'>- Define a GitHub workflow for running smoke tests on every push or manual trigger<br>- The workflow checks out code, installs Go, fetches required modules, builds, and runs tests using the Go toolchain on an Ubuntu runner<br>- This ensures code quality and functionality with each update.</td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---

## 🚀 Getting Started

### 🟣 Prerequisites

This project requires the following dependencies:

- **Programming Language:** Go
- **Package Manager:** Go modules
- **Container Runtime:** Docker

### 🟤 Installation

Build docker-gs-ping from the source and install dependencies:

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


### ⚫ Usage

Run the project with:

**Using [docker](https://www.docker.com/):**
```sh
docker run -it {image_name}
```
**Using [go modules](https://golang.org/):**
```sh
go run {entrypoint}
```

### ⚪ Testing

Docker-gs-ping uses the {__test_framework__} test framework. Run the test suite with:

**Using [go modules](https://golang.org/):**
```sh
go test ./...
```


---

## 🌈 Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🤝 Contributing

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

## 📜 License

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
    --output 'docs/docs/examples/generated/tmp/readme-docker-gs-ping.md' \
    --badge-style 'flat' \
    --badge-color '0d47a1' \
    --logo 'PURPLE' \
    --header-style 'CLASSIC' \
    --navigation-style 'ACCORDION' \
    --emojis 'gradient' \
    --temperature 0.814 \
    --tree-max-depth 1 \
    --api openai
```
-->
