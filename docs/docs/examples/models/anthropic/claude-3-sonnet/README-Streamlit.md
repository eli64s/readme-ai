<div id="top">

<!-- HEADER STYLE: COMPACT -->
<img src="../../../../../../readmeai/assets/logos/ice.svg" width="200px" align="left" style="margin-right: 15px">

# README-AI-STREAMLIT
<em>Supercharge Your Docs: AI-Powered README Generation Unleashed</em>

<!-- BADGES -->
<img src="https://img.shields.io/github/license/eli64s/readme-ai-streamlit?style=flat-square&logo=opensourceinitiative&logoColor=white&color=E92063" alt="license">
<img src="https://img.shields.io/github/last-commit/eli64s/readme-ai-streamlit?style=flat-square&logo=git&logoColor=white&color=E92063" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/eli64s/readme-ai-streamlit?style=flat-square&color=E92063" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/eli64s/readme-ai-streamlit?style=flat-square&color=E92063" alt="repo-language-count">

<em>Built with the tools and technologies:</em>

<img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=flat-square&logo=Streamlit&logoColor=white" alt="Streamlit">
<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat-square&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat-square&logo=Pytest&logoColor=white" alt="Pytest">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=flat-square&logo=AIOHTTP&logoColor=white" alt="AIOHTTP">
<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=flat-square&logo=OpenAI&logoColor=white" alt="OpenAI">
<img src="https://img.shields.io/badge/uv-DE5FE9.svg?style=flat-square&logo=uv&logoColor=white" alt="uv">
<img src="https://img.shields.io/badge/Pydantic-E92063.svg?style=flat-square&logo=Pydantic&logoColor=white" alt="Pydantic">

<br clear="left"/>

<details><summary><b>Table of Contents</b></summary>

I. [🔵 Table of Contents](#-table-of-contents)<br>
[🟢 Overview](#overview)
III. [🟡 Features](#-features)<br>
IV. [🟠 Project Structure](#-project-structure)<br>
&nbsp;&nbsp;&nbsp;&nbsp;IV.a. [🔴 Project Index](#-project-index)<br>
V. [🚀 Getting Started](#-getting-started)<br>
&nbsp;&nbsp;&nbsp;&nbsp;V.a. [🟣 Prerequisites](#-prerequisites)<br>
&nbsp;&nbsp;&nbsp;&nbsp;V.b. [🟤 Installation](#-installation)<br>
&nbsp;&nbsp;&nbsp;&nbsp;V.c. [⚫ Usage](#-usage)<br>
&nbsp;&nbsp;&nbsp;&nbsp;V.d. [⚪ Testing](#-testing)<br>
VI. [🌈 Roadmap](#-roadmap)<br>
VII. [🤝 Contributing](#-contributing)<br>
VIII. [📜 License](#-license)<br>
IX. [✨ Acknowledgments](#-acknowledgments)<br>

</details>

---

## Overview

readme-ai-streamlit is an innovative tool that leverages AI to generate comprehensive README files for software projects. It combines the power of artificial intelligence with an intuitive Streamlit interface for effortless project documentation.

**Why readme-ai-streamlit?**

This project streamlines the creation of professional README files while ensuring consistency and quality. The core features include:

- **🧠 AI-powered generation:** Utilizes advanced AI models to create detailed README content.
- **🖥️ User-friendly interface:** Streamlit-based UI for easy interaction and customization.
- **🔄 Multi-model support:** Compatible with various AI providers like OpenAI, Anthropic, and Google.
- **🎨 Customization options:** Offers configurable badge styles and logo choices.
- **🔧 Development automation:** Includes tools for code formatting, linting, and testing.

---

## 🟡 Features

|      | Component       | Details                              |
| :--- | :-------------- | :----------------------------------- |
| ⚙️  | **Architecture**  | <ul><li>Python-based Streamlit web application</li><li>Utilizes OpenAI API for AI-powered README generation</li><li>Modular structure with separate requirements files</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Uses `ruff` for linting and formatting</li><li>`pre-commit` hooks for code quality checks</li><li>`mypy` for static type checking</li></ul> |
| 📄 | **Documentation** | <ul><li>README.md file (assumed)</li><li>Inline code comments (assumed)</li><li>Generated AI README files</li></ul> |
| 🔌 | **Integrations**  | <ul><li>OpenAI API integration</li><li>Streamlit for web interface</li><li>GitHub integration (via `gitpython`)</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Separate `requirements.txt` and `requirements-dev.txt`</li><li>Use of `pyproject.toml` for project configuration</li><li>Modular dependencies management</li></ul> |
| 🧪 | **Testing**       | <ul><li>`pytest` for unit testing</li><li>`pytest-xdist` for parallel test execution</li><li>`pytest-cov` for code coverage analysis</li><li>`pytest-randomly` for randomized test ordering</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Asynchronous HTTP requests with `aiohttp`</li><li>`cachetools` for caching mechanisms</li><li>`pyarrow` for efficient data processing</li></ul> |
| 🛡️ | **Security**      | <ul><li>`python-dotenv` for environment variable management</li><li>HTTPS requests with `urllib3` and `httpx`</li><li>Input validation with `pydantic`</li></ul> |
| 📦 | **Dependencies**  | <ul><li>`streamlit` for web app framework</li><li>`openai` for AI integration</li><li>`pandas` and `numpy` for data manipulation</li><li>`pydantic` for data validation</li><li>`tiktoken` for tokenization</li></ul> |

---

## 🟠 Project Structure

```sh
└── readme-ai-streamlit/
    ├── LICENSE
    ├── Makefile
    ├── README.md
    ├── assets
    │   ├── line.svg
    │   └── logo.svg
    ├── pyproject.toml
    ├── requirements-dev.txt
    ├── requirements.txt
    ├── scripts
    │   └── clean.sh
    ├── src
    │   ├── __init__.py
    │   └── app.py
    ├── tests
    │   ├── __init__.py
    │   ├── conftest.py
    │   └── src
    │       ├── __init__.py
    │       └── test_app.py
    └── uv.lock
```

### 🔴 Project Index

<details open>
	<summary><b><code>README-AI-STREAMLIT/</code></b></summary>
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
					<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai-streamlit/blob/master/requirements.txt'>requirements.txt</a></b></td>
					<td style='padding: 8px;'>- Requirements.txt specifies the projects dependencies and their versions, ensuring consistent environments across different setups<br>- It lists essential libraries like aiohttp, openai, pydantic, and streamlit, along with their respective dependencies<br>- This file is crucial for maintaining reproducibility and facilitating easy installation of all necessary packages for the project to function correctly.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai-streamlit/blob/master/Makefile'>Makefile</a></b></td>
					<td style='padding: 8px;'>- Makefile defines project automation tasks for the ReadmeAI project<br>- It includes commands for cleaning build artifacts, formatting and linting code, running the Streamlit app locally, executing unit tests, and displaying a help menu<br>- These targets streamline development workflows, ensuring code quality and consistency while facilitating easy project management and execution of common tasks.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai-streamlit/blob/master/pyproject.toml'>pyproject.toml</a></b></td>
					<td style='padding: 8px;'>- Defines project configuration for an AI-powered README generator<br>- Specifies metadata like name, version, description, and author details<br>- Outlines dependencies, including the core readmeai package and Streamlit for the user interface<br>- Sets Python version requirements and categorizes the project with relevant keywords<br>- Includes optional development and testing dependencies, along with project URLs for homepage and documentation.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai-streamlit/blob/master/requirements-dev.txt'>requirements-dev.txt</a></b></td>
					<td style='padding: 8px;'>- Specifies development dependencies for the project, focusing on testing, code quality, and static type checking tools<br>- Includes mypy for type checking, pre-commit for managing Git hooks, ruff for linting, and various pytest plugins for comprehensive testing<br>- These requirements ensure a robust development environment, enabling thorough code analysis, consistent formatting, and efficient test execution across the project.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- scripts Submodule -->
	<details>
		<summary><b>scripts</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ scripts</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai-streamlit/blob/master/scripts/clean.sh'>clean.sh</a></b></td>
					<td style='padding: 8px;'>- Provides a comprehensive cleaning utility for the projects development environment<br>- Offers functions to remove build artifacts, Python bytecode files, test and coverage data, backup files, and cache directories<br>- Allows selective cleaning of specific components or a complete cleanup<br>- Enhances project maintenance by eliminating unnecessary files and ensuring a clean workspace for developers.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- src Submodule -->
	<details>
		<summary><b>src</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ src</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai-streamlit/blob/master/src/app.py'>app.py</a></b></td>
					<td style='padding: 8px;'>- Configuration: It defines essential constants like the project title, supported AI models, badge styles, and logo options.2<br>- User Interface: The file likely uses Streamlit to create an interactive web interface for users to input project details and customize their README generation.3<br>- AI Integration: It prepares the groundwork for integrating various AI models (like OpenAI's GPT, Anthropic's Claude, Google's Gemini, and others) to assist in README generation.4<br>- Logging: Sets up logging to track the application's operations and potential issues.5<br>- File Handling: Includes utilities for temporary file creation and subprocess management, suggesting the app may interact with the local file system or external processes.Overall, this file acts as the central hub for the README-AI application, coordinating user inputs, AI processing, and output generation to create customized README files for software projects.</td>
				</tr>
			</table>
		</blockquote>
	</details>
</details>

---

## 🚀 Getting Started

### 🟣 Prerequisites

This project requires the following dependencies:

- **Programming Language:** unknown
- **Package Manager:** Pip, Uv

### 🟤 Installation

Build readme-ai-streamlit from the source and install dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/eli64s/readme-ai-streamlit
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd readme-ai-streamlit
    ```

3. **Install the dependencies:**

<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![pip][pip-shield]][pip-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [pip-shield]: None -->
	<!-- [pip-link]: None -->

	**Using [pip](None):**

	```sh
	❯ echo 'INSERT-INSTALL-COMMAND-HERE'
	```
<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![uv][uv-shield]][uv-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [uv-shield]: None -->
	<!-- [uv-link]: None -->

	**Using [uv](None):**

	```sh
	❯ echo 'INSERT-INSTALL-COMMAND-HERE'
	```

### ⚫ Usage

Run the project with:

**Using [pip](None):**
```sh
echo 'INSERT-RUN-COMMAND-HERE'
```
**Using [uv](None):**
```sh
echo 'INSERT-RUN-COMMAND-HERE'
```

### ⚪ Testing

Readme-ai-streamlit uses the {__test_framework__} test framework. Run the test suite with:

**Using [pip](None):**
```sh
echo 'INSERT-TEST-COMMAND-HERE'
```
**Using [uv](None):**
```sh
echo 'INSERT-TEST-COMMAND-HERE'
```

---

## 🌈 Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🤝 Contributing

- **💬 [Join the Discussions](https://github.com/eli64s/readme-ai-streamlit/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/eli64s/readme-ai-streamlit/issues)**: Submit bugs found or log feature requests for the `readme-ai-streamlit` project.
- **💡 [Submit Pull Requests](https://github.com/eli64s/readme-ai-streamlit/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

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

## 📜 License

Readme-ai-streamlit is protected under the [LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## ✨ Acknowledgments

- Credit `contributors`, `inspiration`, `references`, etc.

<div align="left"><a href="#top">⬆ Return</a></div>

---

<!-- README-AI COMMAND: -->
<!--
```sh
readmeai \
    --repository 'https://github.com/eli64s/readme-ai-streamlit' \
    --badge-style FLAT-SQUARE \
    --badge-color E92063 \
    --logo ICE \
    --header-style COMPACT \
    --navigation-style ACCORDION \
    --emojis RAINBOW
    --api anthropic \
    --model claude-3-5-sonnet-20240620
```
-->
