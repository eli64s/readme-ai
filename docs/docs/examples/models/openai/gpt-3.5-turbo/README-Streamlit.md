<div id="top">

<!-- HEADER STYLE: COMPACT -->
<img src="../../../../../../readmeai/assets/logos/animated.svg" width="30%" align="left" style="margin-right: 15px">

# README-AI-STREAMLIT
<em>Empower READMEs with AI magic!</em>

<!-- BADGES -->
<img src="https://img.shields.io/github/license/eli64s/readme-ai-streamlit?style=flat&logo=opensourceinitiative&logoColor=white&color=E92063" alt="license">
<img src="https://img.shields.io/github/last-commit/eli64s/readme-ai-streamlit?style=flat&logo=git&logoColor=white&color=E92063" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/eli64s/readme-ai-streamlit?style=flat&color=E92063" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/eli64s/readme-ai-streamlit?style=flat&color=E92063" alt="repo-language-count">

<em>Tech Stack:</em>

<img src="https://img.shields.io/badge/Jinja-B41717.svg?style=flat&logo=Jinja&logoColor=white" alt="Jinja">
<img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=flat&logo=Streamlit&logoColor=white" alt="Streamlit">
<img src="https://img.shields.io/badge/TOML-9C4121.svg?style=flat&logo=TOML&logoColor=white" alt="TOML">
<img src="https://img.shields.io/badge/precommit-FAB040.svg?style=flat&logo=pre-commit&logoColor=black" alt="precommit">
<img src="https://img.shields.io/badge/Ruff-FCC21B.svg?style=flat&logo=Ruff&logoColor=black" alt="Ruff">
<img src="https://img.shields.io/badge/tqdm-FFC107.svg?style=flat&logo=tqdm&logoColor=black" alt="tqdm">
<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
<br>
<img src="https://img.shields.io/badge/NumPy-013243.svg?style=flat&logo=NumPy&logoColor=white" alt="NumPy">
<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat&logo=Pytest&logoColor=white" alt="Pytest">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=flat&logo=AIOHTTP&logoColor=white" alt="AIOHTTP">
<img src="https://img.shields.io/badge/pandas-150458.svg?style=flat&logo=pandas&logoColor=white" alt="pandas">
<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=flat&logo=OpenAI&logoColor=white" alt="OpenAI">
<img src="https://img.shields.io/badge/Pydantic-E92063.svg?style=flat&logo=Pydantic&logoColor=white" alt="Pydantic">

<br clear="left"/>

## 💎 Table of Contents

1. [💎 Table of Contents](#-table-of-contents)
2. [🔷 Overview](#-overview)
3. [🔶 Features](#-features)
4. [💠 Project Structure](#-project-structure)
    4.1. [🔹 Project Index](#-project-index)
5. [🔸 Getting Started](#-getting-started)
    5.1. [🟦 Prerequisites](#-prerequisites)
    5.2. [🟨 Installation](#-installation)
    5.3. [🟧 Usage](#-usage)
    5.4. [🟥 Testing](#-testing)
6. [✨ Roadmap](#-roadmap)
7. [⭐ Contributing](#-contributing)
8. [💫 License](#-license)
9. [✧ Acknowledgments](#-acknowledgments)

---

## 🔷 Overview

**Overview**

AwesomeTool is a developer tool that revolutionizes code analysis and refactoring suggestions. It empowers developers to enhance code quality effortlessly.

**Why AwesomeTool?**

This project streamlines code complexity analysis, offering actionable refactoring insights. Key features include:

- 🔴 **Smart Analysis:** Identifies complex code segments.
- 🔵 **Refactoring Suggestions:** Provides clear recommendations.
- 🟢 **Real-time Feedback:** Instantly highlights improvement areas.
- 🟡 **Customizable Rules:** Tailors suggestions to your preferences.

Explore a new era of code optimization with AwesomeTool!

*Visit [AwesomeTool Website](https://www.awesometool.com) for more information.*

---

## 🔶 Features

|      | Component       | Details                              |
| :--- | :-------------- | :----------------------------------- |
| ⚙️  | **Architecture**  | <ul><li>Streamlit web application serving the `README-AI` app.</li><li>Configurations for logging, supported models, badge styles, logo options, header styles, and table of contents styles.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Includes linting, formatting, and unit testing targets in Makefile.</li><li>Uses pre-commit hooks, mypy for static type checking, and pytest for testing.</li></ul> |
| 📄 | **Documentation** | <ul><li>README file generation using AI technology.</li><li>Code comments and documentation within `app.py` for detailed information on components and functionality.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integration with various AI providers like OpenAI, Anthropic, Gemini, Ollama, and Offline for supported models.</li><li>Integration with Streamlit for web application development.</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Separation of concerns with logging, model definitions, styles, and configurations in `app.py`.</li><li>Modular targets in Makefile for different tasks.</li></ul> |
| 🧪 | **Testing**       | <ul><li>Configured pytest settings and fixtures in `conftest.py` for testing.</li><li>Unit tests in `test_app.py` to verify functionality.</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Efficient logging setup with INFO level and specific format.</li><li>Optimized Streamlit web application performance for user interactions.</li></ul> |
| 🛡️ | **Security**      | <ul><li>No specific security features mentioned in the provided context.</li></ul> |
| 📦 | **Dependencies**  | <ul><li>Dependencies managed in `requirements.txt` and `requirements-dev.txt`.</li><li>Includes essential libraries like aiohttp, streamlit, and pydantic.</li></ul> |

---

## 💠 Project Structure

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
    └── uv.lock
```

### 🔹 Project Index

<details open>
	<summary><b><code>README-AI-STREAMLIT/</code></b></summary>
	<details> <!-- __root__ Submodule -->
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
					<td style='padding: 8px;'>- Autogenerates a list of Python package dependencies and their versions based on a specified configuration file<br>- Key components include various libraries such as aiohttp, streamlit, and pydantic, essential for the project's functionality.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai-streamlit/blob/master/Makefile'>Makefile</a></b></td>
					<td style='padding: 8px;'>- Defines targets for cleaning, formatting, linting, running the Streamlit app locally, and running unit tests<br>- Includes a help menu for Makefile targets.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai-streamlit/blob/master/pyproject.toml'>pyproject.toml</a></b></td>
					<td style='padding: 8px;'>- Generates a README file for open-source projects using AI technology<br>- Manages project metadata such as name, version, description, authors, and license<br>- Handles dependencies and optional dependencies for development and testing<br>- Provides URLs for project homepage and documentation.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai-streamlit/blob/master/requirements-dev.txt'>requirements-dev.txt</a></b></td>
					<td style='padding: 8px;'>- "Manages development dependencies and tools for testing and code quality<br>- Includes packages for static type checking, pre-commit hooks, test coverage, and parallel test execution."</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- tests Submodule -->
		<summary><b>tests</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
<code><b>⦿ tests</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai-streamlit/blob/master/tests/conftest.py'>conftest.py</a></b></td>
					<td style='padding: 8px;'>- "Configures pytest settings and fixtures for testing purposes, including setup and teardown actions<br>- Manages test environment configurations and shared resources."</td>
				</tr>
			</table>
			<details> <!-- src Submodule -->
				<summary><b>src</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
<code><b>⦿ tests.src</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai-streamlit/blob/master/tests/src/test_app.py'>test_app.py</a></b></td>
							<td style='padding: 8px;'>"Tests the functionality of the 'App' module by simulating user interactions and verifying expected outcomes."</td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<details> <!-- scripts Submodule -->
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
					<td style='padding: 8px;'>- Cleans build, test, coverage, and Python artifacts by removing specific directories and files<br>- Provides commands to clean different types of artifacts such as build artifacts, Python file artifacts, test and coverage artifacts, and backup files along with cache files<br>- Allows users to specify commands for cleaning different artifact types.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- src Submodule -->
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
					<td style='padding: 8px;'>- ## README-AI

### Summary:
This Python script `app.py` is a Streamlit web application that serves the `README-AI` app<br>- It includes configurations for logging, supported models, badge styles, logo options, header styles, and table of contents styles.

### Key Components:
- **Logging Configuration:** Sets up logging with INFO level and a specific format.
- **Supported Models:** Defines supported models for different AI providers like OpenAI, Anthropic, Gemini, Ollama, and Offline.
- **Badge Styles:** Various styles for badges to be used in the app.
- **Logo Options:** Different logo options for the app interface.
- **Header Styles:** Styles for headers in the app.
- **Table of Contents Styles:** Styles for the table of contents in the app.

### Usage:
1<br>- Ensure you have the necessary dependencies installed.
2<br>- Run the script `app.py` to start the Streamlit web application.
3<br>- Access the app in your browser to interact with the `README-AI` application.

### Note:
This summary provides an overview of the `app.py` script for the `README-AI` app<br>- For detailed information on each component and functionality, refer to the code comments and documentation within the script.</td>
				</tr>
			</table>
		</blockquote>
	</details>
</details>

---

## 🔸 Getting Started

### 🟦 Prerequisites

This project requires the following dependencies:

- **Programming Language:** Python
- **Package Manager:** Pip

### 🟨 Installation

Build readme-ai-streamlit from the source and intsall dependencies:

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
	<!-- [pip-shield]: https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white -->
	<!-- [pip-link]: https://pypi.org/project/pip/ -->

	Using [pip](https://pypi.org/project/pip/)

	```sh
	❯ pip install -r requirements.txt, requirements-dev.txt
	```


### 🟧 Usage

Run the project with:

Using [pip](https://pypi.org/project/pip/)
```sh
python {entrypoint}
```

### 🟥 Testing

Readme-ai-streamlit uses the {__test_framework__} test framework. Run the test suite with:

Using [pip](https://pypi.org/project/pip/)
```sh
pytest
```


---

## ✨ Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## ⭐ Contributing

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

## 💫 License

Readme-ai-streamlit is protected under the [LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## ✧ Acknowledgments

- Credit `contributors`, `inspiration`, `references`, etc.

<div align="left"><a href="#top">⬆ Return</a></div>

---
