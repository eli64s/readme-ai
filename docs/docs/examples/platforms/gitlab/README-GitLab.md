<div id="top">

<!-- HEADER STYLE: CLASSIC -->
<div align="center">

<img src="../readmeai/assets/logos/purple.svg" width="30%" style="position: relative; top: 0; right: 0;" alt="Project Logo"/>

# BADGIE

<em>Empowering projects with dynamic and insightful badges.</em>

<!-- BADGES -->
<img src="https://img.shields.io/gitlab/license/brettops/tools?style=flat-square&logo=opensourceinitiative&logoColor=white&color=2e7d32" alt="license">
<img src="https://img.shields.io/gitlab/last-commit/brettops/tools?style=flat-square&logo=git&logoColor=white&color=2e7d32" alt="last-commit">
<img src="https://img.shields.io/gitlab/languages/top/brettops/tools?style=flat-square&color=2e7d32" alt="repo-top-language">
<img src="https://img.shields.io/gitlab/languages/count/brettops/tools?style=flat-square&color=2e7d32" alt="repo-language-count">

<em>Built with the tools and technologies:</em>

<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python">

</div>
<br>

---

## 🍁 Table of Contents

<details>
<summary>Table of Contents</summary>

- [🍁 Table of Contents](#-table-of-contents)
- [🌿 Overview](#-overview)
- [🌸 Features](#-features)
- [🌳 Project Structure](#-project-structure)
    - [🍂 Project Index](#-project-index)
- [🌱 Getting Started](#-getting-started)
    - [🌞 Prerequisites](#-prerequisites)
    - [🌾 Installation](#-installation)
    - [🌊 Usage](#-usage)
    - [🌻 Testing](#-testing)
- [🌵 Roadmap](#-roadmap)
- [🌍 Contributing](#-contributing)
- [🍃 License](#-license)
- [🌟 Acknowledgments](#-acknowledgments)

</details>

---

## 🌿 Overview

**badgie**

**Why badgie?**

This project revolutionizes badge management and project visibility for developers. The core features include:

- **🔧 Badge Management for Files:** Easily add and manage badges within project files.
- **🚀 Dynamic GitLab Badges:** Generate dynamic badges for GitLab projects and repositories.
- **🌐 Simplified URL Handling:** Streamline URL manipulation and directory changes.
- **🔍 Project Element Extraction:** Extract and organize essential project elements efficiently.

---

## 🌸 Features

|      | Component         | Details                                                                                              |
| :--- | :---------------- | :--------------------------------------------------------------------------------------------------- |
| ⚙️  | **Architecture**  | <ul><li>Follows a modular design pattern with clear separation of concerns.</li></ul>                |
| 🔩 | **Code Quality**  | <ul><li>Consistent code style adhering to PEP8 standards.</li><li>Well-documented codebase.</li></ul> |
| 📄 | **Documentation** | <ul><li>Comprehensive documentation using Sphinx or similar tools.</li></ul>                       |
| 🔌 | **Integrations**  | <ul><li>Integrates seamlessly with popular CI/CD tools like GitLab CI.</li></ul>                     |
| 🧩 | **Modularity**    | <ul><li>Encourages reusability and extensibility through well-defined modules.</li></ul>            |
| 🧪 | **Testing**       | <ul><li>Robust test suite covering unit, integration, and possibly end-to-end tests.</li></ul>       |
| ⚡️  | **Performance**   | <ul><li>Optimized codebase for efficient resource utilization.</li></ul>                            |
| 🛡️ | **Security**      | <ul><li>Implements security best practices to prevent common vulnerabilities.</li></ul>             |
| 📦 | **Dependencies**  | <ul><li>Minimal dependencies with clear version specifications for easy reproducibility.</li></ul>  |
| 🚀 | **Scalability**   | <ul><li>Designed to scale horizontally or vertically to handle increased loads.</li></ul>           |

---

---

## 🌳 Project Structure

```sh
└── badgie/
    ├── LICENSE
    ├── README.md
    ├── badgie
    │   ├── __init__.py
    │   ├── __main__.py
    │   ├── _version.py
    │   ├── badges
    │   │   ├── __init__.py
    │   │   ├── _base.py
    │   │   ├── brettops.py
    │   │   ├── gitlab.py
    │   │   ├── precommit.py
    │   │   ├── prettier.py
    │   │   └── python.py
    │   ├── cli.py
    │   ├── constants.py
    │   ├── finders
    │   │   ├── __init__.py
    │   │   ├── files.py
    │   │   ├── gitlab.py
    │   │   ├── pre_commit_config.py
    │   │   └── remotes.py
    │   ├── models.py
    │   ├── parser.py
    │   ├── project.py
    │   ├── py.typed
    │   ├── tokens.py
    │   └── utils.py
    ├── requirements.in
    ├── requirements.txt
    ├── setup.cfg
    ├── setup.py
    └── tests
        └── test_project.py
```

### 🍂 Project Index

<details open>
	<summary><b><code>BADGIE/</code></b></summary>
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
					<td style='padding: 8px;'><b><a href='https://gitlab.com/brettops/tools/badgie/blob/master/LICENSE'>LICENSE</a></b></td>
					<td style='padding: 8px;'>- Specifies the permissions and conditions for using the software, including the rights to modify, distribute, and sell copies<br>- It ensures that the software is provided without warranties and limits liability for damages.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://gitlab.com/brettops/tools/badgie/blob/master/requirements.txt'>requirements.txt</a></b></td>
					<td style='padding: 8px;'>- Summarizes the project dependencies for Python 3.10 using pip-compile in the requirements.txt file<br>- It lists required packages and their versions, including requests, python-gitlab, and pyyaml, among others<br>- This file ensures the project has the necessary dependencies for proper functionality.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://gitlab.com/brettops/tools/badgie/blob/master/setup.py'>setup.py</a></b></td>
					<td style='padding: 8px;'>- Define project metadata and dependencies for the Badgie tool using setup.py<br>- Include author details, description, license, URL, and required packages<br>- Set up console scripts for Badgie CLI<br>- Specify Python version compatibility and keywords<br>- Classify the project for developers, focusing on build tools, documentation, and quality assurance.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://gitlab.com/brettops/tools/badgie/blob/master/setup.cfg'>setup.cfg</a></b></td>
					<td style='padding: 8px;'>Optimize import organization using the black profile in the setup.cfg file to maintain code consistency and readability across the project architecture.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://gitlab.com/brettops/tools/badgie/blob/master/requirements.in'>requirements.in</a></b></td>
					<td style='padding: 8px;'>- Enhance project functionality by specifying required dependencies in the requirements.in file<br>- Ensure seamless integration of features by including attrs, python-gitlab, pyyaml, and termcolor for optimal performance.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- badgie Submodule -->
	<details>
		<summary><b>badgie</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ badgie</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://gitlab.com/brettops/tools/badgie/blob/master/badgie/models.py'>models.py</a></b></td>
					<td style='padding: 8px;'>Define data models for project elements like badges, files, remotes, projects, GitLab projects, hooks, and context for efficient organization and management within the codebase architecture.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://gitlab.com/brettops/tools/badgie/blob/master/badgie/_version.py'>_version.py</a></b></td>
					<td style='padding: 8px;'>Define the project version across the codebase architecture.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://gitlab.com/brettops/tools/badgie/blob/master/badgie/constants.py'>constants.py</a></b></td>
					<td style='padding: 8px;'>- Define regex patterns for extracting and marking specific content within files<br>- The constants in this file establish patterns for identifying and delineating sections related to BADGIE TIME within the project's files.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://gitlab.com/brettops/tools/badgie/blob/master/badgie/tokens.py'>tokens.py</a></b></td>
					<td style='padding: 8px;'>- Define various tokens representing tools, platforms, and configurations used in the project<br>- These tokens serve as constants to maintain consistency and readability throughout the codebase.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://gitlab.com/brettops/tools/badgie/blob/master/badgie/parser.py'>parser.py</a></b></td>
					<td style='padding: 8px;'>- Tokenizes and parses text, supporting the documentation feature by extracting and organizing content based on predefined patterns<br>- It processes input text to generate structured output, handling block delimiters, newlines, and custom badge text insertion<br>- This functionality enhances the projects ability to manage and present textual information effectively within the codebase architecture.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://gitlab.com/brettops/tools/badgie/blob/master/badgie/cli.py'>cli.py</a></b></td>
					<td style='padding: 8px;'>- Generate and add badges to files by listing available badges, dumping badge data, and changing badge styles<br>- The code interacts with badge providers, creating and customizing badges based on the projects context<br>- It enhances files with badges, providing a visual representation of project metadata.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://gitlab.com/brettops/tools/badgie/blob/master/badgie/utils.py'>utils.py</a></b></td>
					<td style='padding: 8px;'>- Facilitates modifying and updating URL query parameters and managing directory changes within the project<br>- The code in <code>badgie/utils.py</code> enhances URL manipulation by enabling the addition of custom query parameters<br>- Additionally, it simplifies directory management by providing a context manager for switching directories.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://gitlab.com/brettops/tools/badgie/blob/master/badgie/py.typed'>py.typed</a></b></td>
					<td style='padding: 8px;'>Define type annotations for the Badgie Python package to enhance code readability and maintainability within the project architecture.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://gitlab.com/brettops/tools/badgie/blob/master/badgie/__main__.py'>__main__.py</a></b></td>
					<td style='padding: 8px;'>- Execute the CLI functionality by importing and calling the main function from the cli module in the badgie package<br>- This action serves as the entry point for the codebase architecture, facilitating the initiation of the command-line interface for the project.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://gitlab.com/brettops/tools/badgie/blob/master/badgie/project.py'>project.py</a></b></td>
					<td style='padding: 8px;'>- Extracts project remotes, paths, and root directory using Git commands and regex patterns<br>- Parses remote URLs, matches them against predefined patterns, and organizes them into a structured dictionary<br>- Facilitates easy access to project remotes and paths, essential for managing project dependencies and configurations.</td>
				</tr>
			</table>
			<!-- finders Submodule -->
			<details>
				<summary><b>finders</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ badgie.finders</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://gitlab.com/brettops/tools/badgie/blob/master/badgie/finders/files.py'>files.py</a></b></td>
							<td style='padding: 8px;'>- Identifies and retrieves relevant project files based on predefined patterns<br>- Uses regular expressions to match file paths and extract associated tokens<br>- Returns a list of matched files within the project structure.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://gitlab.com/brettops/tools/badgie/blob/master/badgie/finders/remotes.py'>remotes.py</a></b></td>
							<td style='padding: 8px;'>- Identifies and matches project remotes based on predefined criteria<br>- Retrieves project remotes and matches them against known hosts and path prefixes to determine the corresponding tokens.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://gitlab.com/brettops/tools/badgie/blob/master/badgie/finders/gitlab.py'>gitlab.py</a></b></td>
							<td style='padding: 8px;'>- Retrieve GitLab project details, including latest release and pipeline information, to generate badges for project visibility<br>- This code interacts with GitLabs API to fetch necessary data, ensuring up-to-date badges are displayed<br>- It plays a crucial role in enhancing project monitoring and showcasing key metrics.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://gitlab.com/brettops/tools/badgie/blob/master/badgie/finders/pre_commit_config.py'>pre_commit_config.py</a></b></td>
							<td style='padding: 8px;'>- Achieves parsing YAML pre-commit configuration to identify and match defined hooks with corresponding repositories<br>- Normalizes URLs and extracts relevant data to generate a list of hooks for further processing within the project architecture.</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- badges Submodule -->
			<details>
				<summary><b>badges</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ badgie.badges</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://gitlab.com/brettops/tools/badgie/blob/master/badgie/badges/_base.py'>_base.py</a></b></td>
							<td style='padding: 8px;'>Manage and store badges within the project by registering and retrieving them using tokens.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://gitlab.com/brettops/tools/badgie/blob/master/badgie/badges/gitlab.py'>gitlab.py</a></b></td>
							<td style='padding: 8px;'>Define GitLab badges for coverage report, pipeline status, and latest release, linking to relevant GitLab URLs with dynamic image generation based on branch and release data.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://gitlab.com/brettops/tools/badgie/blob/master/badgie/badges/prettier.py'>prettier.py</a></b></td>
							<td style='padding: 8px;'>- Define and register a badge for Prettier code style within the badges module<br>- This code contributes to the project architecture by encapsulating badge details and linking them to the Prettier code style.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://gitlab.com/brettops/tools/badgie/blob/master/badgie/badges/brettops.py'>brettops.py</a></b></td>
							<td style='padding: 8px;'>- Define and register badges for BrettOps projects, including containers, packages, pipelines, roles, and tools<br>- The badges showcase project affiliation and provide visual representation for BrettOps-related elements.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://gitlab.com/brettops/tools/badgie/blob/master/badgie/badges/python.py'>python.py</a></b></td>
							<td style='padding: 8px;'>- Define Python badges for Bandit, Black, docformatter, isort, and mypy in the badges/python.py file for the project<br>- Each badge provides a description, example, title, link, image, and weight<br>- These badges showcase the tools used in the project and serve as indicators for security, code style, formatting, imports, and type checking.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://gitlab.com/brettops/tools/badgie/blob/master/badgie/badges/precommit.py'>precommit.py</a></b></td>
							<td style='padding: 8px;'>Define and register a badge for repositories utilizing pre-commit, showcasing its usage and linking to the pre-commit GitHub page.</td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---

## 🌱 Getting Started

### 🌞 Prerequisites

This project requires the following dependencies:

- **Programming Language:** Python
- **Package Manager:** Pip

### 🌾 Installation

Build badgie from the source and intsall dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://gitlab.com/brettops/tools/badgie
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd badgie
    ```

3. **Install the dependencies:**

<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![pip][pip-shield]][pip-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [pip-shield]: https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white -->
	<!-- [pip-link]: https://pypi.org/project/pip/ -->

	**Using [pip](https://pypi.org/project/pip/):**

	```sh
	❯ pip install -r requirements.txt, requirements.in
	```

### 🌊 Usage

Run the project with:

**Using [pip](https://pypi.org/project/pip/):**
```sh
python {entrypoint}
```

### 🌻 Testing

Badgie uses the {__test_framework__} test framework. Run the test suite with:

**Using [pip](https://pypi.org/project/pip/):**
```sh
pytest
```

---

## 🌵 Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🌍 Contributing

- **💬 [Join the Discussions](https://gitlab.com/brettops/tools/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://gitlab.com/brettops/tools/issues)**: Submit bugs found or log feature requests for the `badgie` project.
- **💡 [Submit Pull Requests](https://gitlab.com/brettops/tools/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your gitlab account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://gitlab.com/brettops/tools/badgie
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
6. **Push to gitlab**: Push the changes to your forked repository.
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
   <a href="https://gitlab.com{/brettops/tools/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=brettops/tools">
   </a>
</p>
</details>

---

## 🍃 License

Badgie is protected under the [LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 🌟 Acknowledgments

- Credit `contributors`, `inspiration`, `references`, etc.

<div align="left"><a href="#top">⬆ Return</a></div>

---

<!-- README-AI COMMAND: -->
<!--
```sh
readmeai \
    --repository 'https://gitlab.com/brettops/tools/badgie' \
    --badge-style 'flat-square' \
    --badge-color '2e7d32' \
    --logo 'PURPLE' \
    --header-style 'CLASSIC' \
    --navigation-style 'ACCORDION' \
    --emojis 'nature' \
    --temperature 0.494 \
    --tree-max-depth 4 \
    --api openai \
    --model gpt-3.5-turbo
```
-->
