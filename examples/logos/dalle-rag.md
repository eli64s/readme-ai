<p align="center">
    <img src="/examples/logos/dalle-rag.png" align="center" width="30%">
</p>
<p align="center"><h1 align="center">THEPIPE</h1></p>
<p align="center"><em>Unleash Efficiency, Embrace Innovation!</em></p>
<p align="center">
	<img src="https://img.shields.io/github/license/emcf/thepipe?style=flat-square&logo=opensourceinitiative&logoColor=white&color=FFA500" alt="license">
	<img src="https://img.shields.io/github/last-commit/emcf/thepipe?style=flat-square&logo=git&logoColor=white&color=FFA500" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/emcf/thepipe?style=flat-square&color=FFA500" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/emcf/thepipe?style=flat-square&color=FFA500" alt="repo-language-count">
</p>
<p align="center">Tech Stack</p>
<p align="center">
	<img src="https://img.shields.io/badge/scikitlearn-F7931E.svg?style=flat-square&logo=scikit-learn&logoColor=white" alt="scikitlearn">
	<img src="https://img.shields.io/badge/Supabase-3FCF8E.svg?style=flat-square&logo=Supabase&logoColor=white" alt="Supabase">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=flat-square&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions">
	<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=flat-square&logo=AIOHTTP&logoColor=white" alt="AIOHTTP">
	<img src="https://img.shields.io/badge/Pydantic-E92063.svg?style=flat-square&logo=Pydantic&logoColor=white" alt="Pydantic">
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
- [ Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

---

##  Overview

**thepipe** is an open-source project designed to streamline data extraction, processing, and management tasks within AI-native applications. It simplifies web scraping, document processing, and multimedia manipulation, catering to developers working on AI-powered solutions.

With **thepipe**, you can:
🚀 **Efficient Web Scraping**: Seamlessly extract data from various sources using concurrent processing and chunking algorithms.
🔧 **Document Processing**: Organize and group text chunks for enhanced readability and analysis in document processing tasks.
🌐 **AI Text Extraction**: Utilize AI models for data extraction from URLs and files, providing structured JSON output.
🔒 **Compression Capabilities**: Compress project files into context prompts for efficient management and processing.
⚡ **Automation**: Automate Python package publishing, testing, and code coverage for streamlined development workflows.

---

##  Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Utilizes **`aiohttp`** for asynchronous HTTP requests handling.</li><li>Employs **concurrent processing** and **chunking algorithms** for efficient data extraction and organization.</li><li>Interacts with **external APIs** and services to enhance project functionality.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Maintains a stable and efficient codebase architecture through **seamless integration** of essential libraries like **`llama-index`**, **`scikit-learn`**, and others.</li><li>Defines project dependencies and configurations using **`setup.py`** for clear management.</li><li>Utilizes **`flake8`** linting and **unittest** for code quality assurance.</li></ul> |
| 📄 | **Documentation** | <ul><li>Facilitates project dependencies management through the **`requirements.txt`** file.</li><li>Provides clear installation and usage commands for the project.</li><li>Automates Python package publishing and testing with **`.github/workflows/python-publish.yml`** and **`.github/workflows/python-ci.yml`** respectively.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integrates with **external APIs** for enhanced functionality.</li><li>Automates Python package publishing on GitHub releases using **`.github/workflows/python-publish.yml`**.</li><li>Automates Python testing and code coverage with **Playwright setup** and **Codecov report upload** in **`.github/workflows/python-ci.yml`**.</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Facilitates seamless integration of essential libraries for document processing and multimedia manipulation within the project architecture through **`local.txt`**.</li><li>Organizes text chunks efficiently for readability and analysis using **`thepipe/chunker.py`**.</li><li>Supports various extraction configurations and data processing capabilities through **`thepipe/extract.py`**.</li></ul> |
| 🧪 | **Testing**       | <ul><li>Ensures code quality through **`pytest`** testing.</li><li>Automates Python testing and code coverage with **Playwright setup** and **Codecov report upload** in **`.github/workflows/python-ci.yml`**.</li><li>Integrates **unittest** for comprehensive testing coverage.</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Utilizes **asynchronous HTTP requests handling** with **`aiohttp`** for improved performance.</li><li>Employs **concurrent processing** and **chunking algorithms** for efficient data extraction.</li><li>Supports **local execution** for efficient project management.</li></ul> |

---

##  Project Structure

```sh
└── thepipe/
    ├── .github
    │   └── workflows
    ├── LICENSE
    ├── README.md
    ├── local.txt
    ├── requirements.txt
    ├── setup.py
    ├── tests
    │   ├── __init__.py
    │   ├── files
    │   ├── test_api.py
    │   ├── test_chunker.py
    │   ├── test_core.py
    │   ├── test_extractor.py
    │   └── test_scraper.py
    └── thepipe
        ├── __init__.py
        ├── chunker.py
        ├── core.py
        ├── extract.py
        └── scraper.py
```


###  Project Index
<details open>
	<summary><b><code>THEPIPE/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/emcf/thepipe/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td>- Facilitates project dependencies management by specifying required packages and versions in the 'requirements.txt' file<br>- This ensures seamless integration of essential libraries like 'llama-index', 'aiohttp', 'scikit-learn', and others, maintaining a stable and efficient codebase architecture.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/emcf/thepipe/blob/master/setup.py'>setup.py</a></b></td>
				<td>- Define project dependencies and configurations using setup.py for 'thepipe_api', an AI-native extractor powered by multimodal LLMs<br>- Include author details, description, version, and entry points for console scripts<br>- Utilize requirements.txt and local.txt for install and extra dependencies, respectively.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/emcf/thepipe/blob/master/local.txt'>local.txt</a></b></td>
				<td>Facilitates seamless integration of essential libraries for document processing and multimedia manipulation within the project architecture.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- thepipe Submodule -->
		<summary><b>thepipe</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/emcf/thepipe/blob/master/thepipe/scraper.py'>scraper.py</a></b></td>
				<td>- The `scraper.py` file in the `thepipe` directory is responsible for handling web scraping tasks, extracting data from various sources, and processing it for further analysis within the codebase architecture<br>- It utilizes concurrent processing, image manipulation, and chunking algorithms to efficiently gather and organize information<br>- Additionally, it interacts with external APIs and services to enhance the functionality of the project.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/emcf/thepipe/blob/master/thepipe/chunker.py'>chunker.py</a></b></td>
				<td>- Chunking functions in the code file segment text data into meaningful sections based on document structure, pages, sections, semantics, or keywords<br>- These functions organize and group text chunks to enhance readability and analysis, supporting various document processing tasks within the codebase architecture.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/emcf/thepipe/blob/master/thepipe/core.py'>core.py</a></b></td>
				<td>- Enables compression of project files into a context prompt by processing text and images, generating tokens, and saving outputs<br>- Parses arguments for source files, regex patterns, AI text extraction, and verbosity<br>- Supports local execution and facilitates efficient project management.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/emcf/thepipe/blob/master/thepipe/extract.py'>extract.py</a></b></td>
				<td>- The code file `extract.py` facilitates data extraction from URLs and files using AI models, providing structured JSON output<br>- It handles multiple extraction scenarios, error handling, and token calculation<br>- The file integrates with external APIs and supports various extraction configurations, contributing to the project's data processing capabilities.</td>
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
						<td><b><a href='https://github.com/emcf/thepipe/blob/master/.github/workflows/python-publish.yml'>python-publish.yml</a></b></td>
						<td>Automates Python package publishing on GitHub releases by building and uploading the package to PyPI.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/emcf/thepipe/blob/master/.github/workflows/python-ci.yml'>python-ci.yml</a></b></td>
						<td>- Automates Python testing and code coverage with Playwright setup, Tesseract OCR installation, and Codecov report upload<br>- Integrates flake8 linting, unittest, and coverage generation for the project.</td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---
##  Getting Started

###  Prerequisites

Before getting started with thepipe, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip


###  Installation

Install thepipe using one of the following methods:

**Build from source:**

1. Clone the thepipe repository:
```sh
❯ git clone https://github.com/emcf/thepipe
```

2. Navigate to the project directory:
```sh
❯ cd thepipe
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```




###  Usage
Run thepipe using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```


###  Testing
Run the test suite using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```


---
##  Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

##  Contributing

- **💬 [Join the Discussions](https://github.com/emcf/thepipe/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/emcf/thepipe/issues)**: Submit bugs found or log feature requests for the `thepipe` project.
- **💡 [Submit Pull Requests](https://github.com/emcf/thepipe/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/emcf/thepipe
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
   <a href="https://github.com{/emcf/thepipe/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=emcf/thepipe">
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
