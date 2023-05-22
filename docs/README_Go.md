
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
docker-gs-ping
</h1>
<h3 align="center">📍 Ping up your Docker setup with docker-gs-ping!</h3>
<h3 align="center">🚀 Developed with the software and tools below.</h3>
<p align="center">

<img src="https://img.shields.io/badge/Go-00ADD8.svg?style=for-the-badge&logo=Go&logoColor=white" alt="Go" />
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=for-the-badge&logo=Docker&logoColor=white" alt="Docker" />
<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=for-the-badge&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="Markdown" />
</p>

</div>

---

## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍Overview](#overview)
- [🔮 Feautres](#-feautres)
  - [Distinctive Features](#distinctive-features)
- [⚙️ Project Structure](#️-project-structure)
- [💻 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
  - [✅ Prerequisites](#-prerequisites)
  - [💻 Installation](#-installation)
  - [🤖 Using docker-gs-ping](#-using-docker-gs-ping)
  - [🧪 Running Tests](#-running-tests)
- [🛠 Future Development](#-future-development)
- [🤝 Contributing](#-contributing)
- [🪪 License](#-license)
- [🙏 Acknowledgments](#-acknowledgments)

---


## 📍Overview

The docker-gs-ping GitHub project provides users with a tool to quickly and efficiently deploy and scale applications on Docker and Google Cloud Platform. It is a great resource for developers looking to quickly build and deploy applications in a streamlined manner. The project offers a robust set of features, such as basic routes, port configuration, and a unit testing function for the evaluation of an integer minimum. Overall, the docker-gs-ping GitHub project is a valuable resource for developers looking for an efficient tool to build and deploy applications.

---

## 🔮 Feautres

### Distinctive Features

1. **User-Centered Design:** The project focuses on the user's needs, by providing routes such as "/" and "/health" and setting the port to 8080 if one is not provided. 
2. **Dependency Management:** The project is written in Go 1.19 with various dependencies, including github.com/labstack/echo/v4 v4.10.2, jwt, gommon, bytebufferpool, fasttemplate, crypto, net, sys, text, and time. 
3. **Unit Testing:** The script main_test.go is a demonstration of unit testing a function using the Go language; it tests a function called IntMin with two input parameters and evaluates the returned result against a set of expected values included in a table. 
4. **Integration with Docker and Google Cloud Platform:** The project is designed for use with Docker and Google Cloud Platform. This enables users to take advantage of the scalability and flexibility of the cloud platform while using the powerful features of container technology.

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

| File         | Summary                                                                                                                                                                                                                                                     | Module       |
|:-------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------|
| go.mod       | This is a module written in Go 1.19 with various dependencies, including github.com/labstack/echo/v4 v4.10.2, jwt, gommon, bytebufferpool, fasttemplate, crypto, net, sys, text, and time. It is intended for use with Docker and Google Cloud Platform.    | go.mod       |
| main.go      | This code script implements a web server using the echo library, allowing for basic routes such as "/" and "/health" and setting the port to 8080 if one is not provided. Additionally, the code contains an implementation of an integer minimum function. | main.go      |
| main_test.go | This code script is a demonstration of unit testing a function using the Go language; it tests a function called IntMin with two input parameters and evaluates the returned result against a set of expected values included in a table.                   | main_test.go |

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
#run tests
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

