<p align="center">
  <img src="/examples/assets/image-generation/readme-streamlit-v0.5.88.png" width="60%" alt="README-AI-STREAMLIT-logo">
</p>
<p align="center">
    <h1 align="center">README-AI-STREAMLIT</h1>
</p>
<p align="center">
    <em>Craft READMEs with AI magic!</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/eli64s/readme-ai-streamlit?style=flat-square&logo=opensourceinitiative&logoColor=white&color=60A5FA" alt="license">
	<img src="https://img.shields.io/github/last-commit/eli64s/readme-ai-streamlit?style=flat-square&logo=git&logoColor=white&color=60A5FA" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/eli64s/readme-ai-streamlit?style=flat-square&color=60A5FA" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/eli64s/readme-ai-streamlit?style=flat-square&color=60A5FA" alt="repo-language-count">
</p>
<p align="center">
		<em>Built with the tools and technologies:</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=flat-square&logo=Streamlit&logoColor=white" alt="Streamlit">
	<img src="https://img.shields.io/badge/precommit-FAB040.svg?style=flat-square&logo=pre-commit&logoColor=black" alt="precommit">
	<img src="https://img.shields.io/badge/Ruff-FCC21B.svg?style=flat-square&logo=Ruff&logoColor=black" alt="Ruff">
	<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat-square&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
	<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat-square&logo=Pytest&logoColor=white" alt="Pytest">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/Poetry-60A5FA.svg?style=flat-square&logo=Poetry&logoColor=white" alt="Poetry">
</p>
<br>

<details><summary>Table of Contents</summary>

- [📍 Overview](#overview)
- [👾 Features](#features)
- [📁 Project Structure](#project-structure)
  - [📂 Project Index](#project-index)
- [🚀 Getting Started](#getting-started)
  - [📋 Prerequisites](#prerequisites)
  - [⚙️ Installation](#installation)
  - [🤖 Usage](#-usage)
  - [🧪 Tests](#-tests)
- [📌 Roadmap](#roadmap)
- [🔰 Contributing](#-contributing)
- [🎗 License](#license)
- [🙌 Acknowledgments](#acknowledgments)

</details>
<hr>

## 📍 Overview

README-AI Streamlit is a tool that simplifies README file creation for software projects. It offers customizable templates and AI-generated content to enhance project presentation. Ideal for developers seeking efficient and polished project documentation.

---

## 👾 Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Utilizes a modular design with separate components for CLI settings, Streamlit web app, and command generation.</li><li>Employs Streamlit for the web app interface and Python for backend logic.</li><li>Integrates AI for generating README files dynamically based on user input.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Follows PEP 8 coding standards for Python codebase.</li><li>Includes automated tests using `pytest` for ensuring code reliability.</li><li>Utilizes pre-commit hooks for code formatting and linting.</li></ul> |
| 📄 | **Documentation** | <ul><li>Comprehensive documentation in the form of README files, inline comments, and docstrings.</li><li>Provides usage instructions and installation guides using `poetry` package manager.</li><li>Includes script files for managing project tasks and maintaining code hygiene.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integrates with `Streamlit` for creating interactive web applications.</li><li>Uses `poetry` for managing project dependencies.</li><li>Includes `pre-commit` hooks for automated code checks.</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Separates functionality into distinct modules for CLI, web app, and command generation.</li><li>Allows for easy extension and customization of features.</li><li>Encourages code reusability and maintainability.</li></ul> |
| 🧪 | **Testing**       | <ul><li>Implements unit tests using `pytest` to validate code functionality.</li><li>Uses `pytest-cov` for code coverage analysis.</li><li>Includes `mypy` for static type checking.</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Optimizes codebase for efficient generation and display of README content.</li><li>Utilizes caching mechanisms for improved performance.</li><li>Regularly monitors and optimizes performance metrics.</li></ul> |
| 🛡️ | **Security**      | <ul><li>Follows best practices for handling sensitive data like API keys.</li><li>Implements secure coding practices to prevent vulnerabilities.</li><li>Regularly updates dependencies to address security issues.</li></ul> |
| 📦 | **Dependencies**  | <ul><li>Manages dependencies using `poetry` package manager.</li><li>Includes a `poetry.lock` file for version control.</li><li>Ensures dependency compatibility and stability.</li></ul> |
| 🚀 | **Scalability**   | <ul><li>Designed to scale by separating concerns and components.</li><li>Supports handling increased traffic and user interactions.</li><li>Utilizes cloud services for scalability and resource management.</li></ul> |

---

## 📁 Project Structure

```sh
└── readme-ai-streamlit/
    ├── LICENSE
    ├── Makefile
    ├── README.md
    ├── poetry.lock
    ├── pyproject.toml
    ├── scripts
    │   └── clean.sh
    ├── src
    │   ├── __init__.py
    │   ├── app.py
    │   ├── cli.py
    │   └── commands.py
    └── tests
        ├── __init__.py
        ├── conftest.py
        └── src
```

### 📂 Project Index

<details open>
	<summary><b><code>README-AI-STREAMLIT/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/eli64s/readme-ai-streamlit/blob/master/Makefile'>Makefile</a></b></td>
				<td>Facilitates project management and development tasks including cleaning artifacts, displaying git logs, removing cached files, managing dependencies, formatting codebase, running tests, and providing a help menu.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/eli64s/readme-ai-streamlit/blob/master/pyproject.toml'>pyproject.toml</a></b></td>
				<td>Generates automated README files for a Python project using the provided project structure and dependencies.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- scripts Submodule -->
		<summary><b>scripts</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/eli64s/readme-ai-streamlit/blob/master/scripts/clean.sh'>clean.sh</a></b></td>
				<td>- The clean.sh script file provides functions to remove various artifacts such as build, test, and Python files from the project directory<br>- It helps maintain a clean project structure by deleting unnecessary files and directories, enhancing the overall codebase hygiene.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- src Submodule -->
		<summary><b>src</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/eli64s/readme-ai-streamlit/blob/master/src/cli.py'>cli.py</a></b></td>
				<td>- Configure CLI settings for the README-AI Streamlit web app, allowing users to customize various aspects such as repository link, API key, badge style, and project logo<br>- The settings enable users to generate README files with specific language models, header styles, and table of contents formatting, enhancing the overall presentation of their projects.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/eli64s/readme-ai-streamlit/blob/master/src/app.py'>app.py</a></b></td>
				<td>- The code in src/app.py serves as the main function for a Streamlit web app that generates README files using AI<br>- It initializes session state variables, configures the app layout, and handles the generation and display of README content<br>- Users can preview, download, and copy the generated README file.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/eli64s/readme-ai-streamlit/blob/master/src/commands.py'>commands.py</a></b></td>
				<td>- Generates CLI commands for the README-AI Streamlit web app, facilitating the execution of commands and handling output<br>- The code file in src/commands.py constructs commands for processing repositories, incorporating various parameters like API key, emojis, badge styling, and model options<br>- It executes the commands, displaying logs and handling errors effectively.</td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---

## 🚀 Getting Started

### 📋 Prerequisites

Before getting started with readme-ai-streamlit, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Poetry


### 📦 Installation

Install readme-ai-streamlit using one of the following methods:

**Build from source:**

1. Clone the readme-ai-streamlit repository:
```sh
❯ git clone https://github.com/eli64s/readme-ai-streamlit
```

2. Navigate to the project directory:
```sh
❯ cd readme-ai-streamlit
```

3. Install the project dependencies:


**Using `poetry`** &nbsp; [<img align="center" src="https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json" />](https://python-poetry.org/)

```sh
❯ poetry install
```




### 🤖 Usage

Run readme-ai-streamlit using the following command:

**Using `poetry`** &nbsp; [<img align="center" src="https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json" />](https://python-poetry.org/)

```sh
❯ poetry run python {entrypoint}
```



### 🧪 Testing

Run the test suite using the following command:

**Using `poetry`** &nbsp; [<img align="center" src="https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json" />](https://python-poetry.org/)

```sh
❯ poetry run pytest
```



## 📌 Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🔰 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/eli64s/readme-ai-streamlit/issues)**: Submit bugs found or log feature requests for the `readme-ai-streamlit` project.
- **[Submit Pull Requests](https://github.com/eli64s/readme-ai-streamlit/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/eli64s/readme-ai-streamlit/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/eli64s/readme-ai-streamlit
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
   <a href="https://github.com{/eli64s/readme-ai-streamlit/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=eli64s/readme-ai-streamlit">
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
