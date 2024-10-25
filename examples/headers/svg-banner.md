<div align="center">
	<img src="./svg-banner.svg" width="100%" height="auto">
</div>
<p align="center">
	<em>README magic, AI-powered documentation made easy!</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/eli64s/readme-ai-streamlit?style=for-the-badge&logo=opensourceinitiative&logoColor=white&color=blueviolet" alt="license">
	<img src="https://img.shields.io/github/last-commit/eli64s/readme-ai-streamlit?style=for-the-badge&logo=git&logoColor=white&color=blueviolet" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/eli64s/readme-ai-streamlit?style=for-the-badge&color=blueviolet" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/eli64s/readme-ai-streamlit?style=for-the-badge&color=blueviolet" alt="repo-language-count">
</p>
<p align="center">Built with the tools and technologies:</p>
<p align="center">
	<img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=for-the-badge&logo=Streamlit&logoColor=white" alt="Streamlit">
	<img src="https://img.shields.io/badge/precommit-FAB040.svg?style=for-the-badge&logo=pre-commit&logoColor=black" alt="precommit">
	<img src="https://img.shields.io/badge/Ruff-FCC21B.svg?style=for-the-badge&logo=Ruff&logoColor=black" alt="Ruff">
	<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=for-the-badge&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
	<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=for-the-badge&logo=Pytest&logoColor=white" alt="Pytest">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/Poetry-60A5FA.svg?style=for-the-badge&logo=Poetry&logoColor=white" alt="Poetry">
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

**Readme-ai-streamlit** is a comprehensive toolset designed to streamline project documentation processes by automating README file generation using Streamlit and GPT models. It simplifies documentation maintenance, enhances consistency, and boosts project cleanliness for software development teams.

With **readme-ai-streamlit**, you can:
🚀 **Automate README Generation**: Easily create and customize README.md files powered by AI models.
🔧 **Enhance Documentation Efficiency**: Generate README files automatically, ensuring consistency across the codebase.
🌐 **Streamlit Web App Integration**: Utilize a user-friendly Streamlit web app for README generation and customization.
🔒 **Customizable Parameters**: Tailor README generation with adjustable language models, temperature, and tree depth.
⚡ **Utility Commands**: Access utility commands for project maintenance, version control tasks, and artifact cleaning.

---

## 👾 Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Utilizes Streamlit for interactive web app interface.</li><li>Integrates GPT models for automated README generation.</li><li>CLI configuration for user input and customization.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Includes Makefile for project maintenance tasks.</li><li>Linting and formatting using `pre-commit` for code consistency.</li><li>Test coverage with `pytest` and test parallelization with `pytest-xdist`.</li></ul> |
| 📄 | **Documentation** | <ul><li>Automated README generation using Streamlit and GPT models.</li><li>Clear documentation of install and usage commands with `poetry`.</li><li>Usage of `pyproject.toml` for project metadata.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integration with `Streamlit` for web app interface.</li><li>Utilizes `poetry` for managing Python dependencies.</li><li>Integration with `pre-commit` for automated code checks.</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Separate files for CLI configuration, app logic, and command generation.</li><li>Allows customization of README generation parameters.</li><li>Structured codebase for readability and maintainability.</li></ul> |
| 🧪 | **Testing**       | <ul><li>Test automation with `pytest`.</li><li>Randomized tests with `pytest-randomly` for diverse test coverage.</li><li>Test coverage reporting with `pytest-cov`.</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Efficient README generation powered by GPT models.</li><li>Streamlit web app provides fast and interactive user experience.</li><li>Optimized codebase for quick execution and response times.</li></ul> |
| 🛡️ | **Security**      | <ul><li>Secure handling of API keys and user inputs.</li><li>Regular code checks and linting for potential vulnerabilities.</li><li>Secure dependencies management using `poetry`.</li></ul> |
| 📦 | **Dependencies**  | <ul><li>Utilizes `poetry` for dependency management.</li><li>Defined dependencies include `Streamlit`, `pytest`, `pre-commit`, and `readmeai`.</li><li>Consistent dependency versions through `poetry.lock`.</li></ul> |

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
    ├── src
    └── tests
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
				<td>- Facilitates project maintenance and development tasks such as cleaning artifacts, managing dependencies with Poetry, formatting and linting codebase, running tests, and launching the Streamlit application locally<br>- Additionally, provides utility commands for version control tasks like displaying git logs, removing files from the cache, and exporting requirements.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/eli64s/readme-ai-streamlit/blob/master/pyproject.toml'>pyproject.toml</a></b></td>
				<td>Generates README files automatically for the project using Streamlit and GPT models, enhancing documentation efficiency and consistency across the codebase.</td>
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
				<td>- Cleans various artifacts like build files, Python artifacts, test and coverage artifacts, backup and cache files from the project directory<br>- It provides commands to remove specific types of files, enhancing the project's cleanliness and maintainability.</td>
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
				<td>- Defines CLI configuration settings for the README-AI Streamlit web app<br>- Presents a user-friendly interface to input repository details, API key, and various styling options for badge, project logo, and header<br>- Facilitates README generation with customizable parameters like language model, temperature, and tree depth<br>- Allows users to generate or reset the README file.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/eli64s/readme-ai-streamlit/blob/master/src/app.py'>app.py</a></b></td>
				<td>- The code file `app.py` serves as a Streamlit web app for the README-AI CLI Python package<br>- It enables users to generate README.md files powered by AI, providing a user-friendly interface to customize and download the generated content<br>- The app integrates with various settings and commands to facilitate seamless README generation.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/eli64s/readme-ai-streamlit/blob/master/src/commands.py'>commands.py</a></b></td>
				<td>- Generates CLI commands for the README-AI Streamlit web app, building and executing commands to process repository data<br>- Handles command execution, capturing and displaying output while processing repositories using specified parameters like API key, alignment, badge style, logo, and more.</td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with readme-ai-streamlit, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Poetry


### ⚙️ Installation

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


---
## 📌 Project Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🔰 Contributing

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

## 🎗 License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 🙌 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---
