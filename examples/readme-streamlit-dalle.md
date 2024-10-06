<p align="center">
  <img src="/examples/assets/image-generation/readme-streamlit-dalle.png" width="60%" alt="README-AI-STREAMLIT-logo">
</p>
<p align="center">
    <h1 align="center">README-AI-STREAMLIT</h1>
</p>
<p align="center">
    <em>Empower READMEs with AI magic, effortlessly.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/eli64s/readme-ai-streamlit?style=plastic&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/eli64s/readme-ai-streamlit?style=plastic&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/eli64s/readme-ai-streamlit?style=plastic&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/eli64s/readme-ai-streamlit?style=plastic&color=0080ff" alt="repo-language-count">
</p>
<p align="center">
		<em>Built with the tools and technologies:</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=plastic&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
	<img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=plastic&logo=Streamlit&logoColor=white" alt="Streamlit">
	<img src="https://img.shields.io/badge/Poetry-60A5FA.svg?style=plastic&logo=Poetry&logoColor=white" alt="Poetry">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=plastic&logo=Python&logoColor=white" alt="Python">
</p>

<br>

##### 🔗 Table of Contents

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [🧩 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
    - [🔖 Prerequisites](#-prerequisites)
    - [📦 Installation](#-installation)
    - [🤖 Usage](#-usage)
    - [🧪 Tests](#-tests)
- [📌 Project Roadmap](#-project-roadmap)
- [🔰 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

The readme-ai-streamlit project automates README generation for Streamlit apps using AI. It streamlines the process by collecting user inputs, enhancing customization with badges and emojis, and providing a web app interface for generating README files. The project's core functionalities include cleaning artifacts, managing dependencies with Poetry, and facilitating efficient development workflows. By leveraging AI in a Streamlit web app, readme-ai-streamlit adds value by simplifying README creation, improving user experience, and enhancing project documentation.

---

## 👾 Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | The project follows a modular architecture with a CLI tool for README generation and a Streamlit web app for AI-based README generation. It uses Python for backend logic and Streamlit for the frontend. |
| 🔩 | **Code Quality**  | The codebase maintains high code quality standards with consistent formatting and linting using tools like Ruff. It follows best practices for Python development and includes a Makefile for automation tasks. |
| 📄 | **Documentation** | The project has detailed documentation in the form of comments in the codebase and a README file. It explains the project structure, setup instructions, and usage guidelines for developers. |
| 🔌 | **Integrations**  | Key integrations include README AI library for AI-based README generation, Streamlit for web app development, and Poetry for dependency management. External dependencies like Ruff are used for code formatting and linting. |
| 🧩 | **Modularity**    | The codebase is modular and reusable, with separate modules for CLI functionality, utility functions, and the Streamlit web app. This design allows for easy maintenance and extension of the project. |
| 🧪 | **Testing**       | Testing frameworks and tools are not explicitly mentioned in the repository contents. However, the project can benefit from incorporating testing frameworks like pytest for automated testing. |
| ⚡️  | **Performance**   | The project's efficiency is enhanced by using AI for README generation and Streamlit for interactive web app development. Resource usage is optimized for generating README files based on user inputs. |
| 🛡️ | **Security**      | Security measures for data protection and access control are not explicitly mentioned in the repository contents. Implementing secure coding practices and data encryption can enhance the project's security. |
| 📦 | **Dependencies**  | Key external libraries and dependencies include README AI, Streamlit, Poetry for dependency management, and Ruff for code formatting and linting. These dependencies streamline development and enhance project functionality. |
| 🚀 | **Scalability**   | The project's architecture and design support scalability for handling increased traffic and load. The use of Streamlit for web app development allows for easy scaling of the AI-based README generation functionality. |

---

## 📂 Repository Structure

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
    │   └── utils.py
    └── tests
        ├── __init__.py
        └── conftest.py
```

---

## 🧩 Modules

<details closed><summary>.</summary>

| File | Summary |
| --- | --- |
| [Makefile](https://github.com/eli64s/readme-ai-streamlit/blob/main/Makefile) | Orchestrates code formatting, linting, testing, and application execution.-Facilitates repository cleanup, Conda package building, and word search functionality.-Enhances development workflow efficiency and maintenance. |
| [pyproject.toml](https://github.com/eli64s/readme-ai-streamlit/blob/main/pyproject.toml) | Generates READMEs automatically on Streamlit using the README AI library. Manages dependencies and project metadata with Poetry. Maintains code formatting and linting standards with Ruff. Supports development with additional dependencies like Ruff. |

</details>

<details closed><summary>scripts</summary>

| File | Summary |
| --- | --- |
| [clean.sh](https://github.com/eli64s/readme-ai-streamlit/blob/main/scripts/clean.sh) | Cleans build, test, and Python artifacts. Removes files and directories related to builds, tests, coverage, backups, and caches. Provides commands for specific cleaning tasks. |

</details>

<details closed><summary>src</summary>

| File | Summary |
| --- | --- |
| [cli.py](https://github.com/eli64s/readme-ai-streamlit/blob/main/src/cli.py) | Collects user inputs for configuring a README generation web app.-Builds a command to execute a CLI tool for generating README files based on user settings.-Enhances README customization with badges, emojis, and project logo options. |
| [utils.py](https://github.com/eli64s/readme-ai-streamlit/blob/main/src/utils.py) | Provides utility functions for the Streamlit app, enhancing functionality and improving user experience. |
| [app.py](https://github.com/eli64s/readme-ai-streamlit/blob/main/src/app.py) | Generates README files using AI in a Streamlit web app. Initializes session state, executes commands, and displays output. Handles README generation settings, previews, downloads, and markdown copying. Logs errors if generation fails. |

</details>

---

## 🚀 Getting Started

### 🔖 Prerequisites

**Python**: `version x.y.z`

### 📦 Installation

Build the project from source:

1. Clone the readme-ai-streamlit repository:
```sh
❯ git clone https://github.com/eli64s/readme-ai-streamlit
```

2. Navigate to the project directory:
```sh
❯ cd readme-ai-streamlit
```

3. Install the required dependencies:
```sh
❯ pip install -r requirements.txt
```

### 🤖 Usage

To run the project, execute the following command:

```sh
❯ python main.py
```

### 🧪 Tests

Execute the test suite using the following command:

```sh
❯ pytest
```

---

## 📌 Project Roadmap

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
