<div id="top">

<!-- HEADER STYLE: CLASSIC -->
<div align="center">

![logo](../../../../../../../../../../../readmeai/assets/logos/metallic.svg){ width="35%" style=position: relative; top: 0; right: 0; }

# README-AI-STREAMLIT

<em>AI-powered READMEs: Effortless, brilliant documentation.</em>

<!-- BADGES -->
<img src="https://img.shields.io/github/license/eli64s/readme-ai-streamlit?style=flat&logo=opensourceinitiative&logoColor=white&color=pink" alt="license">
<img src="https://img.shields.io/github/last-commit/eli64s/readme-ai-streamlit?style=flat&logo=git&logoColor=white&color=pink" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/eli64s/readme-ai-streamlit?style=flat&color=pink" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/eli64s/readme-ai-streamlit?style=flat&color=pink" alt="repo-language-count">

<em>Technology Stack:</em>

<img src="https://img.shields.io/badge/Jinja-B41717.svg?style=flat&logo=Jinja&logoColor=white" alt="Jinja">
<img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=flat&logo=Streamlit&logoColor=white" alt="Streamlit">
<img src="https://img.shields.io/badge/TOML-9C4121.svg?style=flat&logo=TOML&logoColor=white" alt="TOML">
<img src="https://img.shields.io/badge/precommit-FAB040.svg?style=flat&logo=pre-commit&logoColor=black" alt="precommit">
<img src="https://img.shields.io/badge/Ruff-FCC21B.svg?style=flat&logo=Ruff&logoColor=black" alt="Ruff">
<img src="https://img.shields.io/badge/tqdm-FFC107.svg?style=flat&logo=tqdm&logoColor=black" alt="tqdm">
<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
<img src="https://img.shields.io/badge/NumPy-013243.svg?style=flat&logo=NumPy&logoColor=white" alt="NumPy">
<br>
<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat&logo=Pytest&logoColor=white" alt="Pytest">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=flat&logo=AIOHTTP&logoColor=white" alt="AIOHTTP">
<img src="https://img.shields.io/badge/pandas-150458.svg?style=flat&logo=pandas&logoColor=white" alt="pandas">
<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=flat&logo=OpenAI&logoColor=white" alt="OpenAI">
<img src="https://img.shields.io/badge/uv-DE5FE9.svg?style=flat&logo=uv&logoColor=white" alt="uv">
<img src="https://img.shields.io/badge/Pydantic-E92063.svg?style=flat&logo=Pydantic&logoColor=white" alt="Pydantic">

</div>
<br>

---

## ⬜ Table of Contents

- [⬜ Table of Contents](#-table-of-contents)
- [◽ Overview](#-overview)
- [⚪ Features](#-features)
- [◻ ️ Project Structure](#-project-structure)
    - [⬚ Project Index](#-project-index)
- [▫ ️ Getting Started](#-getting-started)
    - [⬛ Prerequisites](#-prerequisites)
    - [◾ Installation](#-installation)
    - [⚫ Usage](#-usage)
    - [◼ ️ Testing](#-testing)
- [🔲 Roadmap](#-roadmap)
- [🔳 Contributing](#-contributing)
- [⬛ License](#-license)
- [✧ Acknowledgments](#-acknowledgments)

---

## ◽ Overview

Generate professional READMEs effortlessly with `readme-ai-streamlit`, a powerful tool leveraging the capabilities of multiple Large Language Models (LLMs).

**Why readme-ai-streamlit?**

This project automates README file generation, saving developers valuable time and ensuring consistent, high-quality documentation. The core features include:

- **🟢 Streamlit UI:**  Enjoy a user-friendly interface for seamless interaction and easy README generation.
- **🟡 Multiple LLM Support:** Choose from OpenAI, Anthropic, Gemini, and Ollama for optimal results.
- **🔵 Customizable Output:** Tailor the generated README to perfectly match your project's style and requirements.
- **🔴 Comprehensive Testing:** Benefit from a robust testing suite ensuring reliability and stability.
- **🟣 Automated Build Process:** Streamline your workflow with automated build, testing, and cleaning tasks.
- **🟠 Extensible and Maintainable Codebase:**  The well-structured codebase allows for easy extension and maintenance.

---

## ⚪ Features

|      | Component       | Details                              |
| :--- | :-------------- | :----------------------------------- |
| ⚙️  | **Architecture**  | <ul><li>Streamlit web application</li><li>Uses OpenAI API for text generation</li><li>Modular design with separate functions for different tasks</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Uses `pyproject.toml` for project management</li><li>Includes `pre-commit` hooks for code formatting and linting</li><li>`mypy` for static type checking</li><li>`pytest` for unit testing</li><li>`ruff` for code linting</li></ul> |
| 📄 | **Documentation** | <ul><li>README file provides basic instructions</li><li>Limited in-code documentation</li><li>No formal API documentation</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integrates with OpenAI API</li><li>Uses Streamlit for UI</li><li>Relies on several Python libraries (see Dependencies)</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Functions are relatively well-separated</li><li>Room for improvement in terms of larger-scale modularity</li></ul> |
| 🧪 | **Testing**       | <ul><li>Uses `pytest` framework</li><li>`pytest-cov` for coverage reporting</li><li>`pytest-xdist` for parallel testing</li><li>Test coverage could be improved</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Performance depends heavily on OpenAI API response times</li><li>No obvious performance optimizations implemented</li><li>Streamlit's caching mechanisms might help</li></ul> |
| 🛡️ | **Security**      | <ul><li>OpenAI API key handling needs careful consideration</li><li>No explicit security measures beyond standard Python practices</li></ul> |
| 📦 | **Dependencies**  | <ul><li>Many dependencies (see provided list)</li><li>Dependency management via `pip` and `pyproject.toml`</li></ul> |
| 🚀 | **Scalability**   | <ul><li>Scalability limited by OpenAI API usage limits</li><li>Streamlit's cloud deployment options could improve scalability</li></ul> |

---

## ◻️ Project Structure

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

### ⬚ Project Index

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
					<td style='padding: 8px;'>- The requirements file specifies all project dependencies<br>- It ensures that the application, built using Streamlit and ReadmeAI, has access to necessary libraries for tasks such as data processing, HTTP requests, OpenAI interaction, and UI rendering<br>- The listed packages cover a wide range of functionalities, from data manipulation and visualization to API communication and application structure.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai-streamlit/blob/master/Makefile'>Makefile</a></b></td>
					<td style='padding: 8px;'>- The Makefile orchestrates the projects build process<br>- It defines targets for cleaning, formatting, linting, running the Streamlit application, and executing unit tests<br>- These targets streamline development workflows, ensuring code quality and facilitating easy execution of common tasks within the <code>readmeai</code> source code directory and associated <code>tests</code> directory<br>- A help target provides a convenient overview of available commands.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai-streamlit/blob/master/pyproject.toml'>pyproject.toml</a></b></td>
					<td style='padding: 8px;'>- Pyproject.toml<code> configures the </code>src<code> project, an AI-powered README generator<br>- It specifies project metadata, including name, version, authors, and license<br>- Dependencies include </code>readmeai<code> and </code>streamlit`, indicating use of an external README generation library and a Streamlit-based user interface<br>- Development and testing dependencies are also defined for build and testing processes.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai-streamlit/blob/master/requirements-dev.txt'>requirements-dev.txt</a></b></td>
					<td style='padding: 8px;'>- Requirements-dev.txt` specifies the projects development dependencies<br>- It ensures consistent code quality through linters (mypy, ruff, pre-commit) and facilitates comprehensive testing using pytest and its extensions for coverage, randomized execution, enhanced output, and parallel processing<br>- These tools support the projects build and testing phases.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- tests Submodule -->
	<details>
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
					<td style='padding: 8px;'>- Conftest.py` provides pytest configuration for the projects test suite<br>- It sets up the testing environment, defining fixtures and other configurations used across multiple test modules<br>- This ensures consistent and reusable test setup, improving the efficiency and maintainability of the projects testing infrastructure<br>- The file contributes to a well-structured and robust testing process within the larger codebase.</td>
				</tr>
			</table>
			<!-- src Submodule -->
			<details>
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
							<td style='padding: 8px;'>- Unit tests for the applications core functionality are provided<br>- These tests verify the behavior of the applications components, ensuring correctness and stability<br>- Located within the project's test suite, it contributes to the overall quality assurance process by validating the application's adherence to specifications before deployment<br>- The tests cover key features, promoting robust software development.</td>
						</tr>
					</table>
				</blockquote>
			</details>
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
					<td style='padding: 8px;'>- The <code>clean.sh</code> script removes project artifacts<br>- It offers granular control, allowing selective removal of build files, Python bytecode, test results, and cache directories<br>- The script streamlines the development workflow by providing a centralized mechanism for cleaning up intermediate and temporary files, improving project organization and maintainability<br>- A comprehensive clean is performed when invoked without arguments.</td>
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
					<td style='padding: 8px;'>- The <code>src/app.py</code> file serves as the main entry point for the README-AI application<br>- It uses the Streamlit framework to create a user interface allowing users to select from various large language models (LLMs) and generate README files<br>- The application supports multiple LLM providers (OpenAI, Anthropic, Gemini, Ollama) and offers customization options for the generated READMEs appearance<br>- In essence, its the core application logic that ties together the different components of the project to provide a functional README generation tool.</td>
				</tr>
			</table>
		</blockquote>
	</details>
</details>

---

## ▫️ Getting Started

### ⬛ Prerequisites

This project requires the following dependencies:

- **Programming Language:** Python
- **Package Manager:** Pip, Uv

### ◾ Installation

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

	**Using [pip](https://pypi.org/project/pip/):**

	```sh
	❯ pip install -r requirements.txt, requirements-dev.txt
	```
<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![uv][uv-shield]][uv-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [uv-shield]: https://img.shields.io/badge/uv-DE5FE9.svg?style=for-the-badge&logo=uv&logoColor=white -->
	<!-- [uv-link]: https://docs.astral.sh/uv/ -->

	**Using [uv](https://docs.astral.sh/uv/):**

	```sh
	❯ uv sync --all-extras --dev
	```


### ⚫ Usage

Run the project with:

**Using [pip](https://pypi.org/project/pip/):**
```sh
python {entrypoint}
```
**Using [uv](https://docs.astral.sh/uv/):**
```sh
uv run python {entrypoint}
```

### ◼️ Testing

Readme-ai-streamlit uses the {__test_framework__} test framework. Run the test suite with:

**Using [pip](https://pypi.org/project/pip/):**
```sh
pytest
```
**Using [uv](https://docs.astral.sh/uv/):**
```sh
uv run pytest tests/
```


---

## 🔲 Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🔳 Contributing

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

## ⬛ License

Readme-ai-streamlit is protected under the [LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## ✧ Acknowledgments

- Credit `contributors`, `inspiration`, `references`, etc.

<div align="left"><a href="#top">⬆ Return</a></div>

---
