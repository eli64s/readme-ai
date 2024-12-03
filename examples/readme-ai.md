[<img src="https://cdn-icons-png.flaticon.com/512/6295/6295417.png" align="left" width="20%" padding="20">]()

## &nbsp;&nbsp; README-AI

&nbsp;&nbsp;&nbsp;&nbsp; *Empowering Documentation with AI Brilliance*

<p align="left">&nbsp;&nbsp;
	<img src="https://img.shields.io/github/license/eli64s/readme-ai?style=flat&logo=opensourceinitiative&logoColor=white&color=526CFE" alt="license">
	<img src="https://img.shields.io/github/last-commit/eli64s/readme-ai?style=flat&logo=git&logoColor=white&color=526CFE" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/eli64s/readme-ai?style=flat&color=526CFE" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/eli64s/readme-ai?style=flat&color=526CFE" alt="repo-language-count">
</p>
<br>

<details><summary>Table of Contents</summary>

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🤖 Usage](#🤖-usage)
  - [🧪 Testing](#🧪-testing)
- [📌 Roadmap](#-project-roadmap)
- [🔰 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

</details>
<hr>

## 📍 Overview

README-AI is an open-source project that automates README generation for software repositories. It enhances developer productivity by creating structured documentation, including summaries, badges, and directory trees. Ideal for developers seeking efficient project onboarding and documentation maintenance.

---

## 👾 Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Modular design for scalability</li><li>Microservices architecture</li><li>Utilizes containerization with Docker</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Extensive testing with pytest and coverage reports</li><li>Linting and formatting with pre-commit hooks</li><li>Type checking with mypy</li></ul> |
| 📄 | **Documentation** | <ul><li>Rich documentation in various formats (YAML, TOML, Markdown)</li><li>Includes detailed installation commands for different package managers</li><li>Utilizes MkDocs for generating documentation</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integration with GitHub Actions for CI/CD</li><li>Uses various third-party libraries like OpenAI and requests</li><li>Includes shields.io badges for status indicators</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Well-structured codebase with clear separation of concerns</li><li>Encourages code reusability and maintainability</li><li>Utilizes dependency management with Poetry</li></ul> |
| 🧪 | **Testing**       | <ul><li>Comprehensive test suite with pytest and asyncio support</li><li>Includes coverage reports for test effectiveness</li><li>Randomized testing with pytest-randomly</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Optimized code for efficiency</li><li>Utilizes asynchronous programming with aiohttp</li><li>Scalable architecture for handling high loads</li></ul> |
| 🛡️ | **Security**      | <ul><li>Security measures with GitPython for version control</li><li>Utilizes secure communication with requests library</li><li>Includes security configurations in Dockerfile</li></ul> |
| 📦 | **Dependencies**  | <ul><li>Manages dependencies with Poetry and dependency lock files</li><li>Includes a variety of libraries for different functionalities</li><li>Dependency management with conda for environment setup</li></ul> |

---

## 📁 Project Structure

```sh
└── readme-ai/
    ├── .github
    ├── CHANGELOG.md
    ├── CODE_OF_CONDUCT.md
    ├── CONTRIBUTING.md
    ├── Dockerfile
    ├── LICENSE
    ├── Makefile
    ├── README.md
    ├── docs
    ├── examples
    ├── mkdocs.yml
    ├── noxfile.py
    ├── poetry.lock
    ├── pyproject.toml
    ├── readmeai
    ├── scripts
    ├── setup
    └── tests
```


### 📂 Project Index
<details open>
	<summary><b><code>README-AI/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/mkdocs.yml'>mkdocs.yml</a></b></td>
				<td>- Configure README-AI MkDocs site settings for documentation navigation, styling, and functionality<br>- Organize content, integrate with plugins, and apply custom CSS and JavaScript for enhanced user experience.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/Dockerfile'>Dockerfile</a></b></td>
				<td>- Facilitates the setup and configuration of a Docker container for the project, installing dependencies and setting up the necessary environment variables<br>- The Dockerfile defines the base image, sets up the working directory, installs required packages, creates a user, and configures the entry point and default command for running the application.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/Makefile'>Makefile</a></b></td>
				<td>Facilitates various project tasks such as cleaning build artifacts, creating Conda recipes, building Docker images, displaying git logs, managing dependencies with Poetry, formatting codebase with Ruff, running MkDocs server, conducting word searches in the codebase, and running unit tests using pytest and multiple Python versions with nox.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/pyproject.toml'>pyproject.toml</a></b></td>
				<td>- Generates README files using large language model APIs, facilitating developer documentation<br>- The code defines project metadata, dependencies, and scripts for the README file generator tool<br>- This file is crucial for managing project information and dependencies effectively.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/noxfile.py'>noxfile.py</a></b></td>
				<td>- Configures and executes tests across multiple Python versions using Nox<br>- Installs dependencies and runs the test suite with coverage reports for versions 3.9 to 3.12.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- setup Submodule -->
		<summary><b>setup</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/setup/setup.sh'>setup.sh</a></b></td>
				<td>- Facilitates environment setup by checking dependencies, creating a new conda environment, and installing required packages<br>- Ensures Python version compatibility and enhances user experience with informative messages<br>- Streamlines project onboarding by automating setup tasks.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/setup/requirements.txt'>requirements.txt</a></b></td>
				<td>Define project dependencies and versions using the requirements.txt file to ensure compatibility and manage package installations seamlessly across the codebase architecture.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/setup/environment.yaml'>environment.yaml</a></b></td>
				<td>Defines project dependencies and environment setup through a YAML file, specifying required Python version, package channels, and dependencies listed in a separate requirements file.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- scripts Submodule -->
		<summary><b>scripts</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/scripts/run_batch.sh'>run_batch.sh</a></b></td>
				<td>Generates markdown files with badges and images for various repositories based on predefined styles and settings.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/scripts/pypi.sh'>pypi.sh</a></b></td>
				<td>- Automates the PyPI deployment process by cleaning, building, and uploading distribution files for a specified package<br>- The script ensures seamless deployment to PyPI, enhancing the project's release workflow.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/scripts/clean.sh'>clean.sh</a></b></td>
				<td>- The clean.sh script removes various artifacts like build files, Python file artifacts, test and coverage files, backup files, and cache files<br>- It helps maintain a clean project directory by removing unnecessary files and directories<br>- This script is essential for ensuring a tidy and organized codebase.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/scripts/docker.sh'>docker.sh</a></b></td>
				<td>- Automates Docker image building, pushing, and multi-platform support<br>- Sets up Docker Buildx, builds and publishes the image, and completes the process by displaying the published image name.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- .github Submodule -->
		<summary><b>.github</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/.github/release-drafter.yml'>release-drafter.yml</a></b></td>
				<td>Define release drafter conventions and categorize changes based on labels for streamlined project versioning and changelog generation.</td>
			</tr>
			</table>
			<details>
				<summary><b>workflows</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/.github/workflows/coverage.yml'>coverage.yml</a></b></td>
						<td>- Automate Codecov coverage reporting for Python codebase using GitHub Actions<br>- Run tests, generate coverage reports, and upload to Codecov on push and pull requests<br>- Dependencies managed with Poetry.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/.github/workflows/mkdocs.yml'>mkdocs.yml</a></b></td>
						<td>- Automates deployment of MkDocs to GitHub Pages upon push or pull request<br>- Sets up Python, installs Poetry, dependencies, and builds the MkDocs site<br>- Utilizes the peaceiris/actions-gh-pages action for deployment, ensuring updates are published to the designated directory.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/.github/workflows/release-pipeline.yml'>release-pipeline.yml</a></b></td>
						<td>- Automates deployment to PyPI and Docker Hub upon main branch push/release<br>- Sets up Python environment, installs dependencies, builds and publishes to PyPI<br>- Builds and pushes Docker image, supporting multiple platforms<br>- Ensures smooth integration with PyPI and Docker Hub for efficient package and image deployment.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/.github/workflows/release-drafter.yml'>release-drafter.yml</a></b></td>
						<td>- Automates release notes drafting based on pull request events<br>- Supports PRs from forks and creates GitHub releases<br>- Configurable to disable autolabeler and specify custom config<br>- Uses GitHub token for authentication.</td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<details> <!-- readmeai Submodule -->
		<summary><b>readmeai</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/_exceptions.py'>_exceptions.py</a></b></td>
				<td>Define custom exceptions for readme-ai package, handling errors during README generation, CLI input, file system operations, and unsupported LLM services.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/__main__.py'>__main__.py</a></b></td>
				<td>- Generates README files by processing a repository and configuring settings for the README file generator agent<br>- Handles exceptions during the generation process and updates API and model settings accordingly<br>- Retrieves dependencies, analyzes files, and uses a model to generate the README content<br>- Saves the generated README.md file and provides completion notifications.</td>
			</tr>
			</table>
			<details>
				<summary><b>parsers</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/properties.py'>properties.py</a></b></td>
						<td>Parse .properties configuration files to extract jdbc connection strings and package names.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/factory.py'>factory.py</a></b></td>
						<td>- Define an abstract factory module for all project file parsers, providing a dictionary of callable file parser methods for various file types such as Python, C/C++, JavaScript/Node.js, Kotlin, Go, Java, Rust, Swift, and Docker<br>- This module facilitates the parsing of different file formats within the project architecture.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/docker.py'>docker.py</a></b></td>
						<td>Parse Docker configuration files to extract package names and services, contributing to the project's architecture by enabling efficient handling of dependencies and services specified in Dockerfiles and docker-compose.yaml files.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/npm.py'>npm.py</a></b></td>
						<td>Parse npm and yarn.lock files to extract dependency names for the project's architecture.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/cpp.py'>cpp.py</a></b></td>
						<td>- Parse C/C++ project dependency files using parsers for CMakeLists.txt, configure.ac, and Makefile.am<br>- Extract dependencies, libs, and software names from these files to facilitate project configuration and build processes<br>- The parsers help streamline the handling of different dependency file formats commonly found in C/C++ projects.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/gradle.py'>gradle.py</a></b></td>
						<td>- Parse Gradle and Gradle.kts dependency files to extract package names for the project's build configuration<br>- The code achieves this by implementing parsers for both types of dependency files, enabling seamless extraction of package names from the respective files.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/yarn.py'>yarn.py</a></b></td>
						<td>Extracts package names from a yarn.lock dependency file for the project's architecture.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/swift.py'>swift.py</a></b></td>
						<td>Parse Swift Package.swift files to extract package names for dependencies.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/python.py'>python.py</a></b></td>
						<td>- The provided code file contains parsers for extracting package names from various Python dependency files like requirements.txt, TOML, and YAML<br>- These parsers play a crucial role in analyzing and understanding the dependencies of the project, enabling efficient management and tracking of software dependencies across different build systems and environments.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/go.py'>go.py</a></b></td>
						<td>Parse go.mod files to extract package names for dependency management in the project architecture.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/maven.py'>maven.py</a></b></td>
						<td>Parse Maven pom.xml files to extract package names, adding 'spring' if dependencies contain it.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/rust.py'>rust.py</a></b></td>
						<td>Parse Rust cargo.toml dependency files to extract package names, handling errors gracefully.</td>
					</tr>
					</table>
				</blockquote>
			</details>
			<details>
				<summary><b>core</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/core/models.py'>models.py</a></b></td>
						<td>- The code file in readmeai/core/models.py orchestrates interactions with a Large Language Model API, handling requests and responses<br>- It abstracts the model settings, payload construction, and HTTP client management<br>- Additionally, it facilitates batch processing of prompts and code summaries generation for project files.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/core/preprocess.py'>preprocess.py</a></b></td>
						<td>Pre-processes repository files, extracts metadata, and generates file contexts for the project architecture.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/core/parsers.py'>parsers.py</a></b></td>
						<td>Defines an abstract base class for dependency file parsers, providing a standardized error handling mechanism and logging functionality for parsing exceptions.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/core/logger.py'>logger.py</a></b></td>
						<td>- Implements a custom logger with color and emoji support for the readme-ai package<br>- Allows logging messages at different levels with specified formatting and output to the console<br>- Manages multiple logger instances with configurable log levels.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/core/utils.py'>utils.py</a></b></td>
						<td>- Facilitates configuration of LLM API environments by setting variables based on specified LLM service<br>- Handles scenarios where necessary environment keys are missing, ensuring smooth operation or switching to offline mode<br>- Key functionality for seamless integration with LLM services in the project architecture.</td>
					</tr>
					</table>
				</blockquote>
			</details>
			<details>
				<summary><b>config</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings.py'>settings.py</a></b></td>
						<td>- The code file `settings.py` defines Pydantic models and settings for the `readme-ai` package<br>- It encapsulates configurations for API settings, file paths, Git repositories, Markdown templates, and LLM model parameters<br>- Additionally, it includes logic to validate and set Git repository attributes, generate file URLs, and load configuration settings for the package.</td>
					</tr>
					</table>
					<details>
						<summary><b>settings</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings/prompts.toml'>prompts.toml</a></b></td>
								<td>- **Summarize:**
Illustrate the key generative prompt templates for large language models in the project<br>- These templates offer a structured approach to analyze the project's technical capabilities and characteristics, aiding in the creation of a Markdown table<br>- The prompts cover essential aspects like architecture, code quality, documentation, integrations, modularity, testing, performance, security, dependencies, and scalability.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings/parsers.toml'>parsers.toml</a></b></td>
								<td>Parse and analyze project configuration and dependency files with the provided parsers.toml file.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings/quickstart.toml'>quickstart.toml</a></b></td>
								<td>- The provided code file, located at readmeai/config/settings/quickstart.toml, plays a crucial role in defining default configurations and settings for the project<br>- It specifies essential information such as the default tool, installation instructions, run commands, test instructions, shields for badges, and related website links<br>- This file serves as a central reference point for setting up and running the project, providing clarity on the tools and processes involved without delving into technical intricacies.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings/languages.toml'>languages.toml</a></b></td>
								<td>Define programming language extensions and their corresponding names for the project's configuration settings.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings/config.toml'>config.toml</a></b></td>
								<td>- The code file provides default settings and configurations for various aspects of the project, such as API settings, file resources, Git repository settings, and more<br>- It serves as a central configuration hub for defining key parameters that influence the behavior and functionality of the entire codebase architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings/markdown.toml'>markdown.toml</a></b></td>
								<td>Generate a Markdown template for constructing a README.md file, including header, badges, and directory structure.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings/ignore_list.toml'>ignore_list.toml</a></b></td>
								<td>Define exclusion criteria for preprocessing by specifying directories, file extensions, and file names to be ignored.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings/commands.toml'>commands.toml</a></b></td>
								<td>- Facilitates defining language-specific commands for installation, running, and testing in the project<br>- Supports various programming languages like Java, Python, and Go, ensuring streamlined development processes<br>- Enables easy execution of tasks across different languages, enhancing project efficiency and maintainability.</td>
							</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<details>
				<summary><b>utils</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/utils/file_handler.py'>file_handler.py</a></b></td>
						<td>Enables reading and writing various file formats using a unified interface, enhancing file I/O operations across the project.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/utils/text_cleaner.py'>text_cleaner.py</a></b></td>
						<td>- The code file in `text_cleaner.py` serves the purpose of post-processing responses from the LLM API in the open-source project<br>- It includes functions to clean and format text, such as removing specific patterns, correcting markdown table formatting, and ensuring consistent text structure<br>- This utility enhances the overall quality and readability of the generated text output.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/utils/file_resources.py'>file_resources.py</a></b></td>
						<td>- Retrieve the absolute path to a resource file within the package, prioritizing `importlib.resources` and falling back to `pkg_resources` for compatibility<br>- Handle errors with a custom exception to ensure successful resource file access.</td>
					</tr>
					</table>
				</blockquote>
			</details>
			<details>
				<summary><b>models</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/models/offline.py'>offline.py</a></b></td>
						<td>Handles offline mode for CLI operations when no LLM API service is available, setting default values and returning placeholder text in lieu of LLM API responses.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/models/gemini.py'>gemini.py</a></b></td>
						<td>- Handles Google Cloud's Gemini API requests by initializing the API settings, building payloads, and processing responses<br>- Utilizes Google's generative AI library for text generation<br>- Implements retry logic for robustness and logs response details.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/models/tokens.py'>tokens.py</a></b></td>
						<td>- Facilitates tokenizing and truncating text based on a specified maximum count, enhancing the language model's handling of prompts<br>- The code optimizes token count for prompts, ensuring they meet the defined context window while maintaining text integrity.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/models/dalle.py'>dalle.py</a></b></td>
						<td>- Generates and downloads images using OpenAI's DALL-E model, based on project configuration data<br>- Handles API sessions, formats prompt strings, generates images, and downloads them from provided URLs.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/models/factory.py'>factory.py</a></b></td>
						<td>- Selects appropriate LLM API service based on CLI input to return the corresponding handler<br>- The ModelRegistry class contains a mapping of CLI options to handler classes for different LLM API services, ensuring the correct handler is returned based on the input provided.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/models/prompts.py'>prompts.py</a></b></td>
						<td>- Generates and formats prompts for the LLM API based on provided context such as features, overview, and tagline<br>- Additionally, creates additional prompts like features, overview, and tagline for LLM using specific configurations and dependencies.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/models/openai.py'>openai.py</a></b></td>
						<td>- Implements an OpenAI API LLM handler with Ollama support, managing configuration settings and building payloads for requests<br>- Handles API calls, processes responses, and logs generated text<br>- Ensures robustness through retry logic for error handling.</td>
					</tr>
					</table>
				</blockquote>
			</details>
			<details>
				<summary><b>cli</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/cli/options.py'>options.py</a></b></td>
						<td>- Facilitates configuring command-line options for the readme-ai package, enabling users to customize image settings, API services, badges, and more for generating README.md files<br>- The options cover aspects like image selection, API backend, badge appearance, output file naming, and text generation parameters<br>- This module enhances user control over the content and styling of README files.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/cli/main.py'>main.py</a></b></td>
						<td>- Entrypoint function for the readme-ai CLI application, orchestrating the interaction between user input and the readme_agent function<br>- Handles CLI arguments for various options like alignment, API, and model configuration, facilitating the generation of README files using the readme-ai package.</td>
					</tr>
					</table>
				</blockquote>
			</details>
			<details>
				<summary><b>vcs</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/vcs/ingestor.py'>ingestor.py</a></b></td>
						<td>- The code file facilitates cloning, copying, and handling Git repositories within the project architecture<br>- It includes functions for cloning repositories, copying directories, removing temporary directories, and handling hidden files<br>- This code plays a crucial role in managing repository operations seamlessly within the project structure.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/vcs/metadata.py'>metadata.py</a></b></td>
						<td>- Retrieves metadata of a git repository from the host provider's API<br>- The code fetches GitHub repository details such as name, owner, statistics, URLs, languages, and license information<br>- It converts raw repository data into a structured data class, providing essential insights into the repository's characteristics and settings.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/vcs/url_builder.py'>url_builder.py</a></b></td>
						<td>- Implements Git repository URL validation, parsing, and API endpoint retrieval based on the provided URL<br>- Parses the URL to extract host, name, and full name attributes<br>- Supports creation of GitURL objects from string URLs and generates file URLs for remote repositories.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/vcs/providers.py'>providers.py</a></b></td>
						<td>- Defines GitHost Enum with supported services and URLs<br>- Parses Git repository URL to extract host, full name, and project name<br>- Generates the URL for a file in a remote repository based on the host and file path provided.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/vcs/errors.py'>errors.py</a></b></td>
						<td>- Define custom exceptions for Git repository validation: GitValidationError, GitCloneError, GitURLError, and UnsupportedGitHostError<br>- These exceptions handle errors related to cloning repositories, invalid URLs, and unsupported Git hosts within the utilities package.</td>
					</tr>
					</table>
				</blockquote>
			</details>
			<details>
				<summary><b>templates</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/templates/toc.py'>toc.py</a></b></td>
						<td>- Generates Table of Contents based on style and data, rendering a structured outline for README.md<br>- The code includes templates for different styles and items, allowing customization of the ToC appearance.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/templates/header.py'>header.py</a></b></td>
						<td>Defines header styles and renders README.md headers based on the chosen style, allowing customization through data input.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/templates/base_template.py'>base_template.py</a></b></td>
						<td>Defines a base template class with a method to render templates using provided data and a static method to sanitize input strings, mitigating XSS attacks.</td>
					</tr>
					</table>
				</blockquote>
			</details>
			<details>
				<summary><b>generators</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/generators/tree.py'>tree.py</a></b></td>
						<td>- Generates a directory tree structure for a code repository by formatting and organizing the project's file hierarchy<br>- The code classifies directories and files, presenting them in a structured tree format with specified depth levels.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/generators/builder.py'>builder.py</a></b></td>
						<td>- Generates various sections of the README Markdown file, including header, Table of Contents, code summaries, directory tree structure, Getting Started, and Contributing<br>- Integrates data from the project configuration to create a comprehensive README layout.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/generators/utils.py'>utils.py</a></b></td>
						<td>- Improve markdown content by removing emojis and splitting headings into sections for better readability and organization<br>- Update heading names by removing special characters for cleaner representation.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/generators/badges.py'>badges.py</a></b></td>
						<td>- Generates and formats SVG badges for the README file, using shields.io icons and skill icons from a specific repository<br>- Provides methods to build metadata badges for project dependencies and align them based on specified styles.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/generators/tables.py'>tables.py</a></b></td>
						<td>- Generates Markdown tables to store LLM text responses in README files by constructing formatted tables based on provided data<br>- This code facilitates organizing and displaying code summaries in a structured manner within project sub-directories, enhancing readability and accessibility for users navigating the project documentation.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/generators/quickstart.py'>quickstart.py</a></b></td>
						<td>- Generate dynamic 'Quickstart' guides for the README file based on the top language in the project<br>- Determine setup commands and prerequisites for the most prominent language, ensuring users have a smooth onboarding experience.</td>
					</tr>
					</table>
					<details>
						<summary><b>svg</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/generators/svg/skill_icons.json'>skill_icons.json</a></b></td>
								<td>- Generates a JSON file mapping skill icons to their names and a base URL for accessing them<br>- This file serves as a central repository for all available skill icons, facilitating easy access and retrieval within the project architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/generators/svg/shieldsio_icons.json'>shieldsio_icons.json</a></b></td>
								<td>- The code file `shieldsio_icons.json` in the `readmeai/generators/svg` directory serves the purpose of defining badge URLs and colors for various technologies used in the project<br>- It enables the generation of dynamic SVG badges for technologies like `.ENV` and `.NET` with customizable styles and logos, enhancing the visual representation of project documentation and status indicators.</td>
							</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---
## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with readme-ai, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Poetry, Pip, Conda
- **Container Runtime:** Docker


### ⚙️ Installation

Install readme-ai using one of the following methods:

**Build from source:**

1. Clone the readme-ai repository:
```sh
❯ git clone https://github.com/eli64s/readme-ai
```

2. Navigate to the project directory:
```sh
❯ cd readme-ai
```

3. Install the project dependencies:


**Using `poetry`** &nbsp; [<img align="center" src="https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json" />](https://python-poetry.org/)

```sh
❯ poetry install
```


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r setup/requirements.txt
```


**Using `conda`** &nbsp; [<img align="center" src="https://img.shields.io/badge/conda-342B029.svg?style={badge_style}&logo=anaconda&logoColor=white" />](https://docs.conda.io/)

```sh
❯ conda env create -f setup/environment.yaml
```


**Using `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker build -t eli64s/readme-ai .
```




### 🤖 Usage
Run readme-ai using the following command:
**Using `poetry`** &nbsp; [<img align="center" src="https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json" />](https://python-poetry.org/)

```sh
❯ poetry run python {entrypoint}
```


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```


**Using `conda`** &nbsp; [<img align="center" src="https://img.shields.io/badge/conda-342B029.svg?style={badge_style}&logo=anaconda&logoColor=white" />](https://docs.conda.io/)

```sh
❯ conda activate {venv}
❯ python {entrypoint}
```


**Using `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker run -it {image_name}
```


### 🧪 Testing
Run the test suite using the following command:
**Using `poetry`** &nbsp; [<img align="center" src="https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json" />](https://python-poetry.org/)

```sh
❯ poetry run pytest
```


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```


**Using `conda`** &nbsp; [<img align="center" src="https://img.shields.io/badge/conda-342B029.svg?style={badge_style}&logo=anaconda&logoColor=white" />](https://docs.conda.io/)

```sh
❯ conda activate {venv}
❯ pytest
```


## 📌 Roadmap
- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/eli64s/readme-ai/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/eli64s/readme-ai/issues)**: Submit bugs found or log feature requests for the `readme-ai` project.
- **💡 [Submit Pull Requests](https://github.com/eli64s/readme-ai/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/eli64s/readme-ai
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
   <a href="https://github.com{/eli64s/readme-ai/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=eli64s/readme-ai">
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
