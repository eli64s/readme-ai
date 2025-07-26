<div id="top">

<!-- HEADER STYLE: COMPACT -->
<img src="../../../../../../readmeai/assets/logos/midnight.svg" width="30%" align="left" style="margin-right: 15px">

# README-AI
<em></em>

<!-- BADGES -->
<img src="https://img.shields.io/github/license/eli64s/readme-ai?style=flat&logo=opensourceinitiative&logoColor=white&color=b19cd9" alt="license">
<img src="https://img.shields.io/github/last-commit/eli64s/readme-ai?style=flat&logo=git&logoColor=white&color=b19cd9" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/eli64s/readme-ai?style=flat&color=b19cd9" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/eli64s/readme-ai?style=flat&color=b19cd9" alt="repo-language-count">

<em>Technology Stack:</em>

<img src="https://img.shields.io/badge/Anthropic-191919.svg?style=flat&logo=Anthropic&logoColor=white" alt="Anthropic">
<img src="https://img.shields.io/badge/TOML-9C4121.svg?style=flat&logo=TOML&logoColor=white" alt="TOML">
<img src="https://img.shields.io/badge/precommit-FAB040.svg?style=flat&logo=pre-commit&logoColor=black" alt="precommit">
<img src="https://img.shields.io/badge/Ruff-FCC21B.svg?style=flat&logo=Ruff&logoColor=black" alt="Ruff">
<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat&logo=Pytest&logoColor=white" alt="Pytest">
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white" alt="Docker">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
<br>
<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=flat&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions">
<img src="https://img.shields.io/badge/Poetry-60A5FA.svg?style=flat&logo=Poetry&logoColor=white" alt="Poetry">
<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=flat&logo=AIOHTTP&logoColor=white" alt="AIOHTTP">
<img src="https://img.shields.io/badge/Material%20for%20MkDocs-526CFE.svg?style=flat&logo=Material-for-MkDocs&logoColor=white" alt="Material%20for%20MkDocs">
<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=flat&logo=OpenAI&logoColor=white" alt="OpenAI">
<img src="https://img.shields.io/badge/Google%20Gemini-8E75B2.svg?style=flat&logo=Google-Gemini&logoColor=white" alt="Google%20Gemini">
<img src="https://img.shields.io/badge/Pydantic-E92063.svg?style=flat&logo=Pydantic&logoColor=white" alt="Pydantic">
<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat&logo=YAML&logoColor=white" alt="YAML">

<br clear="left"/>

## 🔵 Table of Contents

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

---

## 🟢 Overview



---

## 🟡 Features

|      | Component       | Details                              |
| :--- | :-------------- | :----------------------------------- |
| ⚙️  | **Architecture**  | <ul><li>Follows clean architecture principles with separate layers for business logic, data access, and presentation.</li><li>Utilizes dependency injection for decoupling components.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Consistent code style enforced using tools like *pre-commit* for linting and formatting.</li><li>Comprehensive test suite covering both unit and integration tests.</li></ul> |
| 📄 | **Documentation** | <ul><li>Well-structured README with clear setup instructions and usage examples.</li><li>Inline code documentation using Python docstrings for functions and classes.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integrates with various CI/CD tools such as *GitHub Actions* for automated testing and deployment.</li><li>Uses *Poetry* for managing dependencies and packaging.</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Codebase is modular with reusable components and services.</li><li>Follows the Single Responsibility Principle for classes and functions.</li></ul> |
| 🧪 | **Testing**       | <ul><li>Uses *Pytest* for test automation with fixtures and parameterized tests.</li><li>Includes test coverage reports and test data generation for thorough testing.</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Optimized code for performance using async programming with *Aiohttp* for HTTP requests.</li><li>Caches data where appropriate to reduce processing time.</li></ul> |
| 🛡️ | **Security**      | <ul><li>Implements secure coding practices to prevent common vulnerabilities like input validation and SQL injection.</li><li>Uses *Pydantic* for data validation and type checking.</li></ul> |
| 📦 | **Dependencies**  | <ul><li>Manages dependencies using *Poetry* and *Conda* for Python packages.</li><li>Includes a detailed list of project dependencies in the README.</li></ul> |

---

## 🟠 Project Structure

```sh
└── readme-ai/
    ├── .github
    │   ├── release-drafter.yml
    │   └── workflows
    │       ├── coverage.yml
    │       ├── mkdocs.yml
    │       ├── release-drafter.yml
    │       └── release-pipeline.yml
    ├── CHANGELOG.md
    ├── CODE_OF_CONDUCT.md
    ├── CONTRIBUTING.md
    ├── Dockerfile
    ├── LICENSE
    ├── Makefile
    ├── README.md
    ├── docs
    │   ├── docs
    │   │   ├── assets
    │   │   ├── blog
    │   │   ├── cli.md
    │   │   ├── configuration
    │   │   ├── contributing.md
    │   │   ├── css
    │   │   ├── examples
    │   │   ├── faq.md
    │   │   ├── guides
    │   │   ├── index.md
    │   │   ├── js
    │   │   ├── llms
    │   │   ├── philosophy.md
    │   │   ├── troubleshooting.md
    │   │   ├── usage
    │   │   └── why.md
    │   ├── mkdocs.yml
    │   └── overrides
    │       └── main.html
    ├── examples
    │   ├── anthropic
    │   │   └── .gitkeep
    │   ├── gemini
    │   │   └── .gitkeep
    │   ├── headers
    │   │   ├── ascii.md
    │   │   ├── classic.md
    │   │   ├── compact.md
    │   │   ├── modern.md
    │   │   ├── svg-banner.md
    │   │   └── svg-banner.svg
    │   ├── local
    │   │   └── readme-local.md
    │   ├── logos
    │   │   ├── custom-balloon.md
    │   │   ├── custom-dragon.md
    │   │   ├── dalle-rag.md
    │   │   ├── dalle-rag.png
    │   │   ├── dalle.md
    │   │   └── dalle.png
    │   ├── offline-mode
    │   │   ├── readme-ai.md
    │   │   └── readme-litellm.md
    │   ├── ollama
    │   │   └── .gitkeep
    │   ├── openai
    │   │   └── .gitkeep
    │   ├── readme-ai.md
    │   ├── readme-docker-go.md
    │   ├── readme-fastapi-redis.md
    │   ├── readme-javascript.md
    │   ├── readme-kotlin.md
    │   ├── readme-litellm.md
    │   ├── readme-mlops.md
    │   ├── readme-ollama.md
    │   ├── readme-postgres.md
    │   ├── readme-python-v0.5.87.md
    │   ├── readme-python.md
    │   ├── readme-readmeai.md
    │   ├── readme-rust-c.md
    │   ├── readme-sqlmesh.md
    │   ├── readme-typescript.md
    │   └── toc
    │       ├── fold.png
    │       ├── links.png
    │       ├── number.png
    │       └── roman-numeral.png
    ├── noxfile.py
    ├── poetry.lock
    ├── pyproject.toml
    ├── readmeai
    │   ├── __init__.py
    │   ├── __main__.py
    │   ├── cli
    │   │   ├── __init__.py
    │   │   ├── main.py
    │   │   └── options.py
    │   ├── config
    │   │   ├── __init__.py
    │   │   ├── constants.py
    │   │   ├── settings
    │   │   └── settings.py
    │   ├── errors.py
    │   ├── generators
    │   │   ├── __init__.py
    │   │   ├── badges.py
    │   │   ├── banner.py
    │   │   ├── builder.py
    │   │   ├── emojis.py
    │   │   ├── quickstart.py
    │   │   ├── svg
    │   │   ├── tables.py
    │   │   └── tree.py
    │   ├── ingestion
    │   │   ├── __init__.py
    │   │   ├── file_processor.py
    │   │   ├── metadata_extractor.py
    │   │   ├── models.py
    │   │   └── pipeline.py
    │   ├── logger.py
    │   ├── models
    │   │   ├── __init__.py
    │   │   ├── anthropic.py
    │   │   ├── base.py
    │   │   ├── dalle.py
    │   │   ├── factory.py
    │   │   ├── gemini.py
    │   │   ├── offline.py
    │   │   ├── openai.py
    │   │   ├── prompts.py
    │   │   └── tokens.py
    │   ├── parsers
    │   │   ├── __init__.py
    │   │   ├── base.py
    │   │   ├── cpp.py
    │   │   ├── docker.py
    │   │   ├── factory.py
    │   │   ├── go.py
    │   │   ├── gradle.py
    │   │   ├── maven.py
    │   │   ├── npm.py
    │   │   ├── properties.py
    │   │   ├── python.py
    │   │   ├── rust.py
    │   │   └── swift.py
    │   ├── postprocessor
    │   │   ├── __init__.py
    │   │   ├── markdown_converter.py
    │   │   └── response_cleaner.py
    │   ├── preprocessor
    │   │   ├── __init__.py
    │   │   ├── directory_cleaner.py
    │   │   ├── document_cleaner.py
    │   │   └── file_filter.py
    │   ├── readers
    │   │   ├── __init__.py
    │   │   └── git
    │   ├── templates
    │   │   ├── __init__.py
    │   │   ├── base.py
    │   │   ├── header.py
    │   │   ├── quickstart.py
    │   │   └── table_of_contents.py
    │   └── utils
    │       ├── __init__.py
    │       ├── file_handler.py
    │       ├── file_resource.py
    │       └── helpers.py
    ├── scripts
    │   ├── clean.sh
    │   ├── docker.sh
    │   ├── pypi.sh
    │   ├── run_batch.sh
    │   └── run_batch_random.sh
    ├── setup
    │   ├── environment.yaml
    │   ├── requirements.txt
    │   └── setup.sh
    └── tests
        ├── __init__.py
        ├── cli
        │   ├── __init__.py
        │   ├── test_main.py
        │   └── test_options.py
        ├── config
        │   ├── __init__.py
        │   ├── test_constants.py
        │   └── test_settings.py
        ├── conftest.py
        ├── generators
        │   ├── __init__.py
        │   ├── conftest.py
        │   ├── test_badges.py
        │   ├── test_banner.py
        │   ├── test_builder.py
        │   ├── test_emojis.py
        │   ├── test_quickstart.py
        │   ├── test_tables.py
        │   └── test_tree.py
        ├── ingestion
        │   ├── __init__.py
        │   ├── test_file_processor.py
        │   ├── test_metadata_extractor.py
        │   ├── test_models.py
        │   └── test_pipeline.py
        ├── models
        │   ├── __init__.py
        │   ├── test_anthropic.py
        │   ├── test_base.py
        │   ├── test_dalle.py
        │   ├── test_factory.py
        │   ├── test_gemini.py
        │   ├── test_openai.py
        │   ├── test_prompts.py
        │   └── test_tokens.py
        ├── parsers
        │   ├── __init__.py
        │   ├── conftest.py
        │   ├── test_cpp.py
        │   ├── test_docker.py
        │   ├── test_factory.py
        │   ├── test_go.py
        │   ├── test_gradle.py
        │   ├── test_maven.py
        │   ├── test_npm.py
        │   ├── test_properties.py
        │   ├── test_python.py
        │   ├── test_rust.py
        │   └── test_swift.py
        ├── postprocessor
        │   ├── __init__.py
        │   ├── test_markdown_converter.py
        │   └── test_response_cleaner.py
        ├── preprocessor
        │   ├── __init__.py
        │   ├── test_directory_cleaner.py
        │   ├── test_document_cleaner.py
        │   └── test_file_filter.py
        ├── readers
        │   ├── __init__.py
        │   └── git
        ├── templates
        │   ├── __init__.py
        │   ├── test_header.py
        │   ├── test_quickstart.py
        │   └── test_table_of_contents.py
        ├── test_errors.py
        ├── test_logger.py
        ├── test_main.py
        └── utils
            ├── __init__.py
            ├── test_file_handler.py
            └── test_file_resource.py
```

### 🔴 Project Index

<details open>
	<summary><b><code>README-AI/</code></b></summary>
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
					<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/Dockerfile'>Dockerfile</a></b></td>
					<td style='padding: 8px;'>- Create a Docker image for readmeai using Python 3.11-slim-buster<br>- Install necessary dependencies, set up a non-root user, and define the entry point and command to run readmeai with--help argument.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/Makefile'>Makefile</a></b></td>
					<td style='padding: 8px;'>- Define project tasks easily with this Makefile<br>- Clean project artifacts, build Docker images, run tests, format codebase, and more<br>- Simplify dependency management with Poetry<br>- Plus, explore a user-friendly help menu for smooth navigation.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/pyproject.toml'>pyproject.toml</a></b></td>
					<td style='padding: 8px;'>- Generate automated README files with AI using the provided codebase structure<br>- The code defines dependencies, scripts, and project metadata, enabling efficient markdown generation<br>- This tool streamlines documentation creation, enhancing developer productivity.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/noxfile.py'>noxfile.py</a></b></td>
					<td style='padding: 8px;'>- Execute tests across various Python versions using the provided noxfile.py to ensure codebase reliability<br>- The file orchestrates test suite execution, including installing dependencies and running tests with coverage reports<br>- It supports Python versions 3.9 to 3.12, enhancing code quality and compatibility.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- setup Submodule -->
	<details>
		<summary><b>setup</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ setup</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/setup/setup.sh'>setup.sh</a></b></td>
					<td style='padding: 8px;'>- Define and execute the environment setup process for the README-AI project, ensuring Python compatibility and installing necessary dependencies<br>- The script checks for existing environments and creates a new one if needed, streamlining the setup for users.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/setup/requirements.txt'>requirements.txt</a></b></td>
					<td style='padding: 8px;'>- Define project dependencies using Python package versions in setup/requirements.txt<br>- Ensure compatibility with Python versions 3.9 to 4.0<br>- Keep packages up-to-date and aligned with the projects requirements for seamless integration and functionality.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/setup/environment.yaml'>environment.yaml</a></b></td>
					<td style='padding: 8px;'>- Create the environment configuration for the project specifying dependencies and channels<br>- Ensure Python 3.9 or higher is required along with additional packages listed in the requirements.txt file<br>- This file is crucial for setting up the development environment and package dependencies.</td>
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
					<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/scripts/run_batch.sh'>run_batch.sh</a></b></td>
					<td style='padding: 8px;'>- Generate README markdown files for open-source projects by running the script <code>run_batch.sh</code><br>- The script utilizes <code>readmeai</code> to craft detailed project documentation with various styles, APIs, models, and customizations<br>- Improve project visibility and engagement by creating comprehensive READMEs effortlessly.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/scripts/pypi.sh'>pypi.sh</a></b></td>
					<td style='padding: 8px;'>- Automates the PyPI deployment process for the readmeai package<br>- Cleans previous builds, creates a new distribution, and uploads it to PyPI using twine<br>- Upon successful upload, confirms the deployment of a new package version.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/scripts/clean.sh'>clean.sh</a></b></td>
					<td style='padding: 8px;'>- Provide a script to clean various artifacts in the project, ensuring a tidy development environment<br>- The script simplifies the removal of build, test, coverage, and Python artifacts, enhancing project maintenance and organization<br>- It offers commands to clean specific artifact types, improving efficiency in managing project files.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/scripts/run_batch_random.sh'>run_batch_random.sh</a></b></td>
					<td style='padding: 8px;'>- Generate diverse README files for multiple repositories by executing the <code>run_batch_random.sh</code> script<br>- It automates the creation of markdown files with various styles and content, leveraging the <code>readmeai</code> tool<br>- The script configures badges, images, alignment, headers, and table of contents for each repository, ensuring a polished and distinctive README appearance.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/scripts/docker.sh'>docker.sh</a></b></td>
					<td style='padding: 8px;'>- Automates Docker image building and publishing<br>- Sets up Docker Buildx, builds the specified image, pushes it to the repository, and creates a multi-platform image<br>- Streamlines the process and ensures the successful publication of the image.</td>
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
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/.github/release-drafter.yml'>release-drafter.yml</a></b></td>
					<td style='padding: 8px;'>- Define versioning and categorization for release notes following changelog conventions<br>- Map labels to categories for features, bug fixes, etc<br>- Generate release notes from pull request titles<br>- Use semantic versioning with labels major, minor, patch<br>- Template captures change details.</td>
				</tr>
			</table>
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
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/.github/workflows/coverage.yml'>coverage.yml</a></b></td>
							<td style='padding: 8px;'>- Create a GitHub Actions workflow to run Python tests and measure code coverage<br>- The workflow sets up Python, installs dependencies using Poetry, runs tests with coverage analysis, and uploads reports to Codecov<br>- This ensures code quality is maintained through automated testing and coverage monitoring.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/.github/workflows/mkdocs.yml'>mkdocs.yml</a></b></td>
							<td style='padding: 8px;'>- Describe how this workflow automates the deployment of the MkDocs documentation site to GitHub Pages<br>- This action is triggered on push or pull requests to the main branch<br>- It sets up Python, installs Poetry dependencies, builds the MkDocs site, and deploys to GitHub Pages using the peaceiris/actions-gh-pages action.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/.github/workflows/release-pipeline.yml'>release-pipeline.yml</a></b></td>
							<td style='padding: 8px;'>- Automate PyPI and Docker Hub deployments, ensuring code reliability and availability<br>- Version-controlled releases trigger package publication to PyPI and Docker Hub, guaranteeing up-to-date packages and container images<br>- Optimize deployment processes for seamless integration and delivery.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/.github/workflows/release-drafter.yml'>release-drafter.yml</a></b></td>
							<td style='padding: 8px;'>- Automates release notes generation by utilizing the Release Drafter GitHub Action<br>- Triggers on main branch pushes and specific pull request events<br>- Manages permissions for content read/write operations<br>- Executes on the latest Ubuntu environment<br>- Integrates with GitHub Token for secure access.</td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<!-- readmeai Submodule -->
	<details>
		<summary><b>readmeai</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ readmeai</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/logger.py'>logger.py</a></b></td>
					<td style='padding: 8px;'>- Implement custom structured logging using structlog for the readme-ai package<br>- Configure the logger with specified processors and renderer, supporting JSON or Console output formats<br>- Include additional processors for context, log level, and stack information<br>- Extract and format messages to enhance log readability<br>- Provide a method to retrieve a logger instance by name.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/errors.py'>errors.py</a></b></td>
					<td style='padding: 8px;'>Summarize the purpose and use of the errors.py file in the projects architecture.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/__main__.py'>__main__.py</a></b></td>
					<td style='padding: 8px;'>- Orchestrates README.md generation by processing repository data, building the file with configurable features, overview, and image<br>- Logs repository info and completion status<br>- Handles errors during the generation process.</td>
				</tr>
			</table>
			<!-- parsers Submodule -->
			<details>
				<summary><b>parsers</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ readmeai.parsers</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/properties.py'>properties.py</a></b></td>
							<td style='padding: 8px;'>Parses *.properties configuration files-Extracts dependencies from file content-Cleans and filters extracted words-Splits camelCase and various text formats-Returns a list of sorted dependencies-Handles version-specific dependencies</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/factory.py'>factory.py</a></b></td>
							<td style='padding: 8px;'>- Create dependency file parser objects based on file names for various tech stacks<br>- Register and retrieve parsers using a predefined dictionary<br>- Centralize parser creation logic to simplify adding new parsers<br>- The ParserFactory manages the creation of specific parsers for different file types within the projects architecture.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/docker.py'>docker.py</a></b></td>
							<td style='padding: 8px;'>- Parse Docker configuration files to extract dependencies and service details<br>- The codebase includes parsers for Dockerfile and docker-compose.yaml files<br>- The DockerfileParser extracts package names, while the DockerComposeParser provides information on services, including environment variables, ports, commands, networks, and images.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/npm.py'>npm.py</a></b></td>
							<td style='padding: 8px;'>- Extracts npm package names from the package.json file for use in the project’s dependency management<br>- This parser simplifies identifying dependencies, devDependencies, and peerDependencies, aiding in efficient package handling and maintenance within the architecture.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/cpp.py'>cpp.py</a></b></td>
							<td style='padding: 8px;'>- Parse C/C++ project dependency files like CMakeLists.txt, configure.ac, and Makefile.am<br>- Extract dependencies, libraries, and software using specific regex patterns<br>- Implement parsers for each file type to ensure accurate extraction of required information.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/gradle.py'>gradle.py</a></b></td>
							<td style='padding: 8px;'>- Parse Gradle dependency files to extract package names, handling both <code>build.gradle</code> and <code>build.gradle.kts</code> formats<br>- Identify dependencies using regex patterns and split logic, returning a list of unique package names.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/swift.py'>swift.py</a></b></td>
							<td style='padding: 8px;'>Parse Swift Package.swift files to extract package names, handling various formats.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/python.py'>python.py</a></b></td>
							<td style='padding: 8px;'>- Parse Python dependency files to extract package names, excluding version specifiers and comments<br>- Handles various build systems like Pipenv, Poetry, Flit, and Rust<br>- Utilizes TOML and YAML parsers to extract all package dependencies efficiently<br>- Achieves clean extraction of package names from diverse dependency file formats, ensuring accurate and organized data retrieval.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/go.py'>go.py</a></b></td>
							<td style='padding: 8px;'>Parse go.mod dependency files to extract and return package names found within.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/maven.py'>maven.py</a></b></td>
							<td style='padding: 8px;'>- Extract Maven package names from pom.xml files, handling parsing errors<br>- Includes regex to match dependencies and identifies spring packages<br>- Inherits from BaseFileParser for modular functionality<br>- Use this for parsing Maven dependency files in the pom.xml format within the project architecture.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/base.py'>base.py</a></b></td>
							<td style='padding: 8px;'>- The BaseFileParser and DefaultParser classes provide a standardized approach for parsing dependency files within the project structure<br>- BaseFileParser serves as an abstract base class defining the parsing interface, while DefaultParser acts as a fallback for unknown file types, ensuring consistent error handling and returning an empty list when needed.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/parsers/rust.py'>rust.py</a></b></td>
							<td style='padding: 8px;'>Parse Rust cargo.toml dependency files to extract package names for the project architecture.</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- ingestion Submodule -->
			<details>
				<summary><b>ingestion</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ readmeai.ingestion</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/ingestion/models.py'>models.py</a></b></td>
							<td style='padding: 8px;'>Describe how the <code>models.py</code> file structures essential data models such as <code>QuickStart</code>, <code>FileContext</code>, and <code>RepositoryContext</code> to capture repository and file details, vital for managing and understanding project metadata effectively within the codebase architecture.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/ingestion/file_processor.py'>file_processor.py</a></b></td>
							<td style='padding: 8px;'>- Generates file information, counts languages occurrences, and extracts dependencies from given contexts<br>- Processes files within a repository path, creating context objects with cleaned content, language mapping, and parsed dependencies<br>- Handles error logging for dependency parsing.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/ingestion/metadata_extractor.py'>metadata_extractor.py</a></b></td>
							<td style='padding: 8px;'>- Extracts metadata from file contexts by detecting tools based on file patterns and converting them into string values<br>- The MetadataExtractor class processes a list of file contexts to categorize tools into predefined categories like CICD, containers, documentation, and package managers<br>- The outcome is a dictionary mapping each category to its corresponding tools as strings.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/ingestion/pipeline.py'>pipeline.py</a></b></td>
							<td style='padding: 8px;'>- Process repository to extract metadata, dependencies, and languages<br>- The code initializes processors for files, metadata, and quickstart generation, then executes the repository processing logic<br>- It leverages file processing, metadata extraction, and dependency extraction to create a context object containing files, dependencies, languages, metadata, and a quickstart guide.</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- config Submodule -->
			<details>
				<summary><b>config</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ readmeai.config</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/config/constants.py'>constants.py</a></b></td>
							<td style='padding: 8px;'>- Define enum classes in <code>constants.py</code> for badge, header, image, and table of contents styles, as well as LLM API service providers and auth keys<br>- This file centralizes settings for README customization, providing a structured approach to manage visual elements and service configurations.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings.py'>settings.py</a></b></td>
							<td style='padding: 8px;'>- Generate Pydantic models and settings for the readme-ai package, including API, file paths, Git repository, Markdown code templates, and LLM model configurations<br>- Load and parse configuration settings from TOML files to facilitate README.md generation and project setup.</td>
						</tr>
					</table>
					<!-- settings Submodule -->
					<details>
						<summary><b>settings</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ readmeai.config.settings</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings/prompts.toml'>prompts.toml</a></b></td>
									<td style='padding: 8px;'>- Generate compelling overview text summarizing the key features and benefits of the project without diving into technical details<br>- Ensure the overview encapsulates the core problem resolution, primary advantages, and target user base of the project.Innovative {0} project revolutionizes {1}, offering {2}<br>- Targeting {3}, it delivers {4}<br>- Experience {5} benefits with this cutting-edge solution.Remember, engaging phrasing is crucial to capture the project essence effectively.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings/parsers.toml'>parsers.toml</a></b></td>
									<td style='padding: 8px;'>- Outline how to configure and analyze project files, covering various CI/CD, configuration, infrastructure, monitoring, and orchestration aspects in a structured manner<br>- This allows easy parsing and understanding of diverse file types and frameworks used across the project, aiding in effective management and optimization of the codebase architecture.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings/quickstart.toml'>quickstart.toml</a></b></td>
									<td style='padding: 8px;'>- Default Tool:<strong> Specifies the default tool for quick start operations.-</strong>Installation:<strong> Provides commands for installing project dependencies.-</strong>Execution:<strong> Defines commands for running the project.-</strong>Testing:<strong> Includes commands for testing the project functionalities.-</strong>Tool-specific Configurations:<strong> Allows customization for different tools like Bash and Dockerfile.-</strong>Badges and References:** Supports the inclusion of shields and website links for relevant tools.This configuration file acts as a pivotal guide for users aiming to swiftly set up, run, and test the project across various environments and toolsets<br>- It streamlines the onboarding process and ensures a seamless experience for developers interacting with the codebase.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings/quickstart_config.toml'>quickstart_config.toml</a></b></td>
									<td style='padding: 8px;'>- Outline how the <code>quickstart_config.toml</code> file configures standardized project templates for a seamless onboarding experience<br>- It defines structured sections for prerequisites, installation, usage, and testing, streamlining the setup process<br>- The files structured format ensures consistency in project documentation, enhancing accessibility for users.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings/tooling.toml'>tooling.toml</a></b></td>
									<td style='padding: 8px;'>- Outline package manager configuration settings for various tech stacks in the provided tooling.toml file within the project<br>- Define standardized file structures for essential package managers like Pythons pip and JavaScripts npm<br>- Enforce consistency across development environments by specifying required configuration files for each technology, facilitating seamless package management.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings/languages.toml'>languages.toml</a></b></td>
									<td style='padding: 8px;'>Define programming language file extensions with corresponding names for the projects language settings configuration.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings/config.toml'>config.toml</a></b></td>
									<td style='padding: 8px;'>- The configuration file <code>config.toml</code> in <code>readmeai/config/settings</code> centralizes default API settings, file resources, Git repository settings, language model API configurations, and logging setup<br>- It plays a crucial role in defining key parameters and paths across the project architecture.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings/tool_config.toml'>tool_config.toml</a></b></td>
									<td style='padding: 8px;'>- The <code>tool_config.toml</code> file within the <code>readmeai/config/settings</code> directory serves as a comprehensive language and tool configuration document for the project<br>- It centralizes key information related to Docker setup and usage, offering guidelines on installation, running, and testing Docker containers within the projects architecture.### Features:-<strong>Default Configuration:</strong> Provides default commands for installation, usage, and testing.-<strong>Docker Container Settings:</strong> Specifies Docker-related configurations such as file extensions, installation commands, usage guidelines, and relevant URLs.-<strong>Docker Compose Settings:</strong> Outlines Docker Compose file details, including installation and usage instructions.### Usage:Developers can refer to this file to streamline the setup and utilization of Docker and Docker Compose within the project<br>- It acts as a quick reference guide for configuring and managing containers efficiently.### Additional Resources:-<strong>Docker Shield:</strong> Displays a badge with Docker-related information for visual identification.-<strong>Website Link:</strong> Directs users to the official Docker website for further information and resources.By leveraging the insights provided in this <code>tool_config.toml</code> file, developers can enhance their understanding of Docker integration within the projects ecosystem, facilitating smoother development and deployment processes.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings/ignore_list.toml'>ignore_list.toml</a></b></td>
									<td style='padding: 8px;'>- Define the exclusion criteria for preprocessing by listing directories, file extensions, and file names to be ignored<br>- This configuration ensures that specific items are excluded from processing, enhancing the efficiency of file handling within the project structure.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/config/settings/commands.toml'>commands.toml</a></b></td>
									<td style='padding: 8px;'>- Detailing programming language installation, execution, and testing commands, the file structures concise directives for various languages<br>- It serves as a vital guide for swiftly setting up, running, and testing code in diverse environments, enabling seamless development across different tech stacks within the projects architecture.</td>
								</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<!-- postprocessor Submodule -->
			<details>
				<summary><b>postprocessor</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ readmeai.postprocessor</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/postprocessor/markdown_converter.py'>markdown_converter.py</a></b></td>
							<td style='padding: 8px;'>- Converts markdown syntax to HTML elements for README-AIs HTML-based table content in README.md<br>- Supports bold, italic, links, headers, and lists<br>- Regular expressions precompiled to enhance performance<br>- Includes functions for processing inline elements and converting markdown text to HTML.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/postprocessor/response_cleaner.py'>response_cleaner.py</a></b></td>
							<td style='padding: 8px;'>- Clean and format LLM API responses by removing uneven Markdown syntax, preserving valid formatting, and extracting specific text patterns<br>- Remove quotes and unnecessary characters while ensuring proper capitalization<br>- This utility enhances the readability and consistency of generated text from the LLM.</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- utils Submodule -->
			<details>
				<summary><b>utils</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ readmeai.utils</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/utils/file_handler.py'>file_handler.py</a></b></td>
							<td style='padding: 8px;'>- Facilitates reading and writing operations for various file formats such as HTML, JSON, Markdown, TOML, TXT, and YAML<br>- Implements robust error handling to manage exceptions during file I/O operations<br>- Supports caching to enhance performance when reading JSON and TOML files.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/utils/file_resource.py'>file_resource.py</a></b></td>
							<td style='padding: 8px;'>Retrieve resource file paths within the package using importlib.resources and pkg_resources, handling fallback scenarios.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/utils/helpers.py'>helpers.py</a></b></td>
							<td style='padding: 8px;'>Verify module availability for import within the project architecture.</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- models Submodule -->
			<details>
				<summary><b>models</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ readmeai.models</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/models/offline.py'>offline.py</a></b></td>
							<td style='padding: 8px;'>- Describe how the Offline Mode model handler operates within the project's architecture<br>- It manages CLI operations independently of the LLM API connection<br>- The handler sets up model configurations, generates payloads for API requests, and simulates API responses with placeholder text.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/models/gemini.py'>gemini.py</a></b></td>
							<td style='padding: 8px;'>- Implement the Google Gemini LLM API service within the architecture<br>- Initialize and configure the Gemini model, handle API requests, and process responses for generating text<br>- Ensure graceful handling when the Generative AI library is unavailable<br>- Retry requests for resilience<br>- Safely access configurations and parameters, optimizing text generation functionality.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/models/tokens.py'>tokens.py</a></b></td>
							<td style='padding: 8px;'>- Enhances token handling for the LLM model by providing functions to count, truncate, and update token limits based on prompt input<br>- The utilities manage token encoding, handle truncation to specified token limits, and adjust token counts as needed<br>- These functions aid in optimizing token usage within the models context window.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/models/dalle.py'>dalle.py</a></b></td>
							<td style='padding: 8px;'>- Generate and download images using OpenAIs DALL-E model<br>- The image, saved as a PNG file, serves as the project logo in the README<br>- Currently, only OpenAI is supported for image generation within readme-ai.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/models/factory.py'>factory.py</a></b></td>
							<td style='padding: 8px;'>- Create LLM API handler instances based on configuration and context<br>- Map different LLM services to respective handler classes<br>- Get the suitable handler based on input, or raise an error for unsupported services<br>- Aims to facilitate the handling of various LLM services within the project architecture.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/models/prompts.py'>prompts.py</a></b></td>
							<td style='padding: 8px;'>- Generate prompts for LLM text generation with provided context to enhance text generation<br>- Retrieve and inject prompt templates based on the given prompt type and context<br>- Additionally, set additional and summary context for features, overview, and slogan prompts to optimize LLM API performance.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/models/openai.py'>openai.py</a></b></td>
							<td style='padding: 8px;'>- Detailing the OpenAI API model handler functionality, the <code>OpenAIHandler</code> class manages interactions with OpenAIs language models, supporting Ollama as well<br>- It configures model settings, constructs payloads, and processes API responses, generating text based on user prompts<br>- This component encapsulates the communication logic with the OpenAI service, facilitating text generation tasks within the projects architecture.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/models/anthropic.py'>anthropic.py</a></b></td>
							<td style='padding: 8px;'>- Implement Anthropic API service handling for generating text using Anthropics Claude LLM model<br>- Configure the model settings, build payload for API requests, handle API response processing, and retry on specific exceptions for reliable text generation.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/models/base.py'>base.py</a></b></td>
							<td style='padding: 8px;'>- The <code>BaseModelHandler</code> serves as the interface for handling requests to the Language Model API<br>- It manages the HTTP client lifecycle, initiates settings for the API, builds payloads for POST requests, and processes API responses to generate text<br>- Additionally, it facilitates batch requests, enabling the generation of summaries and additional context for files within the project.</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- cli Submodule -->
			<details>
				<summary><b>cli</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ readmeai.cli</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/cli/options.py'>options.py</a></b></td>
							<td style='padding: 8px;'>- Generate command-line interface options for the readme-ai package, enabling users to customize README.md files efficiently<br>- This module offers prompts for image selection, version display, badge customization, header alignment, API service choices, and various styling options to enhance the overall presentation of README files<br>- It simplifies the configuration process for creating engaging project documentation.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/cli/main.py'>main.py</a></b></td>
							<td style='padding: 8px;'>- Entrypoint function for the readme-ai CLI app configures settings and calls the readme_agent with provided inputs<br>- It initializes Git, LLM, and Markdown settings, sets API rate limit, and logs configuration details before invoking readme_agent for processing.</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- templates Submodule -->
			<details>
				<summary><b>templates</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ readmeai.templates</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/templates/table_of_contents.py'>table_of_contents.py</a></b></td>
							<td style='padding: 8px;'>- Generate README.md Table of Contents with customizable styles and anchor links<br>- Render based on user-defined data structures, providing flexibility for various formatting preferences.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/templates/header.py'>header.py</a></b></td>
							<td style='padding: 8px;'>- Describe how the HeaderTemplate class defines various header styles using pre-defined templates<br>- It allows users to specify a style and render headers with dynamic data<br>- The class provides flexibility for different visual representations in README.md files based on the chosen style.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/templates/base.py'>base.py</a></b></td>
							<td style='padding: 8px;'>- Define a base template for rendering Markdown content by extending an abstract class<br>- The template serves as the foundation for all Markdown templates in the project structure at readmeai/templates/base.py<br>- It outlines a method to render data into a string format, facilitating the generation of Markdown content.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/templates/quickstart.py'>quickstart.py</a></b></td>
							<td style='padding: 8px;'>- Generate the Quickstart section in the README, providing Installation, Usage, and Testing instructions based on the project's configuration<br>- The output includes system requirements, installation steps, usage commands, and testing procedures<br>- This code file constructs a structured guide for users to quickly get started with the project, enhancing their onboarding experience.</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- generators Submodule -->
			<details>
				<summary><b>generators</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ readmeai.generators</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/generators/tree.py'>tree.py</a></b></td>
							<td style='padding: 8px;'>- Generate a directory tree structure representation for a code repository, replacing the root directory name with the repository name<br>- The code constructs a string outlining the directory hierarchy up to a specified depth, facilitating visualizing the layout of files and folders within the repository.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/generators/emojis.py'>emojis.py</a></b></td>
							<td style='padding: 8px;'>- Remove emojis from default markdown template headers to enhance readability<br>- This utility, part of the projects generator module, ensures clean headers for better user experience<br>- The feature can be easily toggled via CLI flags.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/generators/builder.py'>builder.py</a></b></td>
							<td style='padding: 8px;'>- Generates various sections of a README.md file, including header, table of contents, file summaries, directory tree structure, quickstart guide, and contributing guide<br>- Integrates badges, emojis, and tables to provide a comprehensive overview of the project<br>- Handles dynamic content based on configuration settings and repository context to streamline README generation.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/generators/badges.py'>badges.py</a></b></td>
							<td style='padding: 8px;'>- Generate SVG badges for the README using shields.io icons<br>- Build metadata badges for project dependencies, sorting them by color and name<br>- Convert hex colors to HLS format for badge sorting<br>- Generate badges for the README using shields.io icons, including skill icons for the header section based on specified dependencies.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/generators/tables.py'>tables.py</a></b></td>
							<td style='padding: 8px;'>- Generate expandable sections for modules with nested submodules using HTML tables<br>- Handle root files separately and format code summaries for structured Markdown tables with nested submodules<br>- Group code summaries by their nested module structure to provide a comprehensive overview of the projects codebase architecture.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/generators/banner.py'>banner.py</a></b></td>
							<td style='padding: 8px;'>- Generate stylish banners and ASCII art for project titles and slogans<br>- Convert SVG to HTML for embedding in README files.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/generators/quickstart.py'>quickstart.py</a></b></td>
							<td style='padding: 8px;'>- Generates Quickstart instructions by building data models, determining primary language, and formatting install, usage, and test commands<br>- Handles exceptions and logs errors for robust error handling<br>- The code leverages configuration settings and metadata to provide relevant commands for different tools and languages, enhancing the user experience with clear instructions.</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- readers Submodule -->
			<details>
				<summary><b>readers</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ readmeai.readers</b></code>
					<!-- git Submodule -->
					<details>
						<summary><b>git</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ readmeai.readers.git</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/readers/git/metadata.py'>metadata.py</a></b></td>
									<td style='padding: 8px;'>- Retrieve metadata of a git repository from the host providers API<br>- The code fetches GitHub repository details like name, owner, description, statistics, URLs, programming languages, topics, and more<br>- It provides a structured way to store and access essential repository information for further analysis and usage within the project architecture.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/readers/git/providers.py'>providers.py</a></b></td>
									<td style='padding: 8px;'>- Define Git repository URL model and parsing methods, enabling validation and attribute setting<br>- Extract host, full name, and project name from the URL to create GitURL objects<br>- Facilitate API endpoint and file URL retrieval for remote repositories, supporting GitHub, GitLab, Bitbucket, and local repositories.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/readers/git/repository.py'>repository.py</a></b></td>
									<td style='padding: 8px;'>- Clone and copy Git repositories, handling errors elegantly<br>- Load data efficiently into a temporary directory<br>- This code facilitates seamless repository operations without compromising on error handling or performance.</td>
								</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<!-- preprocessor Submodule -->
			<details>
				<summary><b>preprocessor</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ readmeai.preprocessor</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/preprocessor/file_filter.py'>file_filter.py</a></b></td>
							<td style='padding: 8px;'>Filter files based on a default ignore list to determine if they should be excluded from processing within the codebase architecture.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/preprocessor/directory_cleaner.py'>directory_cleaner.py</a></b></td>
							<td style='padding: 8px;'>- Clean up temporary and hidden directories in the project structure using OS-specific methods<br>- Remove hidden files and directories, excluding those in.github<br>- This code file handles the removal of unwanted directory contents, contributing to maintaining a clean and organized project architecture.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/eli64s/readme-ai/blob/master/readmeai/preprocessor/document_cleaner.py'>document_cleaner.py</a></b></td>
							<td style='padding: 8px;'>- Enhances repository content by cleaning documents through removing empty lines, extra whitespaces, trailing whitespaces, and normalizing indentation<br>- The DocumentCleaner class provides methods to preprocess code strings effectively.</td>
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

- **Programming Language:** Python
- **Package Manager:** Poetry, Pip, Conda
- **Container Runtime:** Docker

### 🟤 Installation

Build readme-ai from the source and install dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/eli64s/readme-ai
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd readme-ai
    ```

3. **Install the dependencies:**

<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![docker][docker-shield]][docker-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [docker-shield]: https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white -->
	<!-- [docker-link]: https://www.docker.com/ -->

	**Using [docker](https://www.docker.com/):**

	```sh
	❯ docker build -t eli64s/readme-ai .
	```
<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![poetry][poetry-shield]][poetry-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [poetry-shield]: https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json -->
	<!-- [poetry-link]: https://python-poetry.org/ -->

	**Using [poetry](https://python-poetry.org/):**

	```sh
	❯ poetry install
	```
<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![pip][pip-shield]][pip-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [pip-shield]: https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white -->
	<!-- [pip-link]: https://pypi.org/project/pip/ -->

	**Using [pip](https://pypi.org/project/pip/):**

	```sh
	❯ pip install -r setup/requirements.txt
	```
<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![conda][conda-shield]][conda-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [conda-shield]: https://img.shields.io/badge/conda-342B029.svg?style={badge_style}&logo=anaconda&logoColor=white -->
	<!-- [conda-link]: https://docs.conda.io/ -->

	**Using [conda](https://docs.conda.io/):**

	```sh
	❯ conda env create -f setup/environment.yaml
	```


### ⚫ Usage

Run the project with:

**Using [docker](https://www.docker.com/):**
```sh
docker run -it {image_name}
```
**Using [poetry](https://python-poetry.org/):**
```sh
poetry run python {entrypoint}
```
**Using [pip](https://pypi.org/project/pip/):**
```sh
python {entrypoint}
```
**Using [conda](https://docs.conda.io/):**
```sh
conda activate {venv}
❯ python {entrypoint}
```

### ⚪ Testing

Readme-ai uses the {__test_framework__} test framework. Run the test suite with:

**Using [poetry](https://python-poetry.org/):**
```sh
poetry run pytest
```
**Using [pip](https://pypi.org/project/pip/):**
```sh
pytest
```
**Using [conda](https://docs.conda.io/):**
```sh
conda activate {venv}
❯ pytest
```


---

## 🌈 Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🤝 Contributing

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

## 📜 License

Readme-ai is protected under the [LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## ✨ Acknowledgments

- Credit `contributors`, `inspiration`, `references`, etc.

<div align="left"><a href="#top">⬆ Return</a></div>

---

<!-- README-AI COMMAND: -->
<!--
```sh
readmeai \
    --repository 'https://github.com/eli64s/readme-ai' \
    --output 'docs/docs/examples/generated/tmp/readme-readme-ai.md' \
    --badge-style 'flat' \
    --badge-color 'b19cd9' \
    --logo 'BLACK' \
    --header-style 'COMPACT' \
    --navigation-style 'BULLET' \
    --emojis 'gradient' \
    --temperature 0.774 \
    --tree-max-depth 3 \
    --api openai
```
-->
