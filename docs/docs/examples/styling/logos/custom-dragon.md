<p align="center">
  <img src="https://img.freepik.com/premium-vector/cute-baby-dragon-smile-cartoon-vector-illustration_295036-2054.jpg" width="30%" alt="README-AI-STREAMLIT-logo">
</p>
<p align="center">
    <h1 align="center">README-AI-STREAMLIT</h1>
</p>
<p align="center">
    <em>Craft READMEs with AI magic!</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/eli64s/readme-ai-streamlit?style=flat-square&logo=opensourceinitiative&logoColor=white&color=FF4B4B" alt="license">
	<img src="https://img.shields.io/github/last-commit/eli64s/readme-ai-streamlit?style=flat-square&logo=git&logoColor=white&color=FF4B4B" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/eli64s/readme-ai-streamlit?style=flat-square&color=FF4B4B" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/eli64s/readme-ai-streamlit?style=flat-square&color=FF4B4B" alt="repo-language-count">
</p>
<p align="center">
		<em>_Built with:_</em>
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

##  Table of Contents

- [ Overview](#-overview)
- [ Features](#-features)
- [ Project Structure](#-project-structure)
  - [ Project Index](#-project-index)
- [ Getting Started](#-getting-started)
  - [ Prerequisites](#-prerequisites)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Testing](#-testing)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

---

##  Overview

README-AI Streamlit is a user-friendly tool that automates README file creation for software projects. It simplifies the process of generating project documentation, enhancing productivity for developers. Ideal for individuals and teams seeking efficient project management and streamlined documentation workflows.

---

##  Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Utilizes a modular architecture with separate components for CLI settings, web app functionality, and command generation.</li><li>Employs a Streamlit web app (<em>app.py<em>) as the main function for generating README files using AI.</li><li>Integration of environment variables and subprocesses to streamline repository processing.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Consistent code formatting and style enforced through tools like <em>mypy<em> and <em>pre-commit<em>.</li><li>Comprehensive test coverage using <em>pytest<em> and test automation for efficiency.</li><li>Codebase includes Makefile commands for maintaining project tasks and enhancing organization.</li></ul> |
| 📄 | **Documentation** | <ul><li>Clear and detailed documentation provided for setting up and using the project.</li><li>Extensive code comments and docstrings for improved code understanding.</li><li>Automated README generation using Streamlit AI for project documentation.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integration with <em>poetry<em> for managing dependencies and packaging.</li><li>Utilizes <em>streamlit<em> for building interactive web applications.</li><li>Integrates with various testing tools like <em>pytest<em> for automated testing.</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Separation of concerns with distinct modules for CLI commands, web app functionality, and command generation.</li><li>Encapsulation of functionality within classes and functions for reusability and maintainability.</li><li>Modular structure enables easy extension and customization of features.</li></ul> |
| 🧪 | **Testing**       | <ul><li>Comprehensive test suite using <em>pytest<em> with plugins like <em>pytest-sugar<em> and <em>pytest-cov<em> for enhanced testing capabilities.</li><li>Includes type checking with <em>mypy<em> for static analysis and type safety.</li><li>Testing automation integrated with CI/CD pipelines for continuous validation.</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Efficient generation of README files using AI-powered algorithms.</li><li>Optimized codebase for fast execution and response times.</li><li>Performance monitoring and profiling integrated for identifying bottlenecks.</li></ul> |
| 🛡️ | **Security**      | <ul><li>Secure handling of user inputs and sensitive information within the application.</li><li>Regular security audits and updates to address vulnerabilities.</li><li>Secure coding practices followed to prevent common security threats.</li></ul> |
| 📦 | **Dependencies**  | <ul><li>Dependency management handled through <em>poetry<em> for consistent and reproducible environments.</li><li>Project dependencies listed in <em>pyproject.toml<em> and locked in <em>poetry.lock<em> for version control.</li><li>Dependency badges included to showcase project dependencies and versions.</li></ul> |

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
            ├── __init__.py
            ├── test_app.py
            ├── test_cli.py
            └── test_commands.py
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
				<td>- Facilitates project maintenance and development tasks through Makefile commands<br>- Enables cleaning artifacts, managing dependencies, formatting code, running tests, and more<br>- Enhances project efficiency and organization.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/eli64s/readme-ai-streamlit/blob/master/pyproject.toml'>pyproject.toml</a></b></td>
				<td>Generates automated README files for a Python project using Streamlit AI.</td>
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
				<td>- The <em>clean.sh<em> script file in the <em>scripts<em> directory provides functionality to remove various artifacts such as build files, Python file artifacts, test and coverage artifacts, backup files, and cache files<br>- It helps maintain a clean project environment by removing unnecessary files and directories.</td>
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
				<td>- Configure CLI settings for the README-AI Streamlit web app, allowing users to customize various aspects such as repository link, API key, badge style, and more<br>- The CLI provides an interactive interface for users to input preferences and generate a README file tailored to their specifications.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/eli64s/readme-ai-streamlit/blob/master/src/app.py'>app.py</a></b></td>
				<td>- The code file <em>app.py<em> serves as the main function for a Streamlit web app that generates README files using AI<br>- It initializes session state variables, configures the web app layout, and handles the generation and display of README files based on user settings<br>- The app provides functionality to preview, download, and copy the generated README content.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/eli64s/readme-ai-streamlit/blob/master/src/commands.py'>commands.py</a></b></td>
				<td>- Generates CLI commands for the README-AI Streamlit web app, facilitating the building and execution of commands for processing repositories<br>- Handles the command execution and output, including error handling and logging<br>- Integrates with environment variables and subprocesses to streamline the processing of repositories with specified configurations.</td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
##  Getting Started

###  Prerequisites

Before getting started with readme-ai-streamlit, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Poetry


###  Installation

Install readme-ai-streamlit using one of the following methods:

**Build from source:**

1. Clone the readme-ai-streamlit repository:
<em><em><em>sh
❯ git clone https://github.com/eli64s/readme-ai-streamlit
<em><em><em>

2. Navigate to the project directory:
<em><em><em>sh
❯ cd readme-ai-streamlit
<em><em><em>

3. Install the project dependencies:


**Using <em>poetry<em>** &nbsp; [<img align="center" src="https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json" />](https://python-poetry.org/)

<em><em><em>sh
❯ poetry install
<em><em><em>




###  Usage
Run readme-ai-streamlit using the following command:
**Using <em>poetry<em>** &nbsp; [<img align="center" src="https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json" />](https://python-poetry.org/)

<em><em><em>sh
❯ poetry run python {entrypoint}
<em><em><em>


###  Testing
Run the test suite using the following command:
**Using <em>poetry<em>** &nbsp; [<img align="center" src="https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json" />](https://python-poetry.org/)

<em><em><em>sh
❯ poetry run pytest
<em><em><em>


##  Project Roadmap
- [X] **<em>Task 1<em>**: <strike>Implement feature one.</strike>
- [ ] **<em>Task 2<em>**: Implement feature two.
- [ ] **<em>Task 3<em>**: Implement feature three.

---

##  Contributing

- **💬 [Join the Discussions](https://github.com/eli64s/readme-ai-streamlit/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/eli64s/readme-ai-streamlit/issues)**: Submit bugs found or log feature requests for the <em>readme-ai-streamlit<em> project.
- **💡 [Submit Pull Requests](https://github.com/eli64s/readme-ai-streamlit/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   <em><em><em>sh
   git clone https://github.com/eli64s/readme-ai-streamlit
   <em><em><em>
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   <em><em><em>sh
   git checkout -b new-feature-x
   <em><em><em>
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   <em><em><em>sh
   git commit -m 'Implemented new feature x.'
   <em><em><em>
6. **Push to github**: Push the changes to your forked repository.
   <em><em><em>sh
   git push origin new-feature-x
   <em><em><em>
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

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---
