<div align="center">
  <h1 align="center">
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
    <br>
    README-AI
  </h1>

> <h3 align="center">Automate README creation, code documentation, and more!</h3>
> <h3 align="center">🚀 Powered by OpenAI's language model API and the software below.</h3>
>  <p align="center">
>   <img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="Markdown" />
>   <img src="https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white" alt="OpenAI" />
>   <img src="https://img.shields.io/badge/Pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
>   <img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="Python" />
>   <img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=for-the-badge&logo=HTML5&logoColor=white" alt="HTML5" />
>   <img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=for-the-badge&logo=GNU-Bash&logoColor=white" alt="Bash" />
>   <img src="https://img.shields.io/badge/Anaconda-44A833.svg?style=for-the-badge&logo=Anaconda&logoColor=white" alt="Anaconda" />
> </p>

</div>

---

## 🧩 Table of Contents

- [🧩 Table of Contents](#-table-of-contents)
- [👋 Introdcution](#-introdcution)
- [🔮 Features](#-features)
- [🏎💨 Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [GitHub Repository](#github-repository)
  - [OpenAI API Setup](#openai-api-setup)
  - [Installation](#installation)
  - [Running README-AI](#running-readme-ai)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [🪪 License](#-license)
- [📫 Contact](#-contact)
- [🙏 Acknowledgments](#-acknowledgments)

---

## 👋 Introdcution

README-AI provides an automated way to generate a README Markdown files and create boilerplate documentation for your codebase. This project leverages OpenAI's GPT Davinci model to translate a given codebase to natural language, producing a structured project README template, including your codebase's metadata and boilerplate documentation.

<style>
    .warning {
        border: 2px solid #ffa500;
        border-radius: 10px;
        padding: 10px;
        background-color: #ffefd5;
        color: #ff8c00;
    }
</style>

<div class="warning">
    <p><strong>🚧 Note:</strong><br>This project is still under development and is opinionated in it's setup, but can be used as a starting point for any project that requires documentation. The current version of README-AI works best on codebases written in Python.
    </p>
</div>


---

## 🔮 Features

<h1 align="center">1.<br>👇<br><br>🤖 Codebase Documentation</h1>
<p align="center">Have you met anyone who said they loved writing documentation? That’s why we're building this project, enjoy!
</p>

|                                                                                                                                                                                                                                                                                         |                                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| <br><br/><b>📍 Codebase Documentation</b><br><br>This project leverages OpenAI's GPT Davinci<br> model to convert a given Python codebase into natural language, producing a well-structured<br>README template that includes repo metadata, documentation and other essential details. | ![header](https://github.com/eli64s/README-AI/blob/main/docs/imgs/docs.png?raw=true) |

<h1 align="center">⒉<br>👇<br><br>🪪 Project Badges</h1>
<p align="center">Visualize project dependencies and components in your README's header section with badges.
</p>

|                                                                                                                                                               |                                                                                      |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| <br><br/><b>📍 Project Badges </b><br><br>Analyzes your project's dependencies and requirements, displaying them as badges<br> in the README's header section. <br><br/><b>📍 Table of Contents </b><br><br>Creates table of contents section for your README file. | ![badges](https://github.com/eli64s/README-AI/blob/main/docs/imgs/head.png?raw=true) |

<h1 align="center">⒊<br>👇<br><br>🌲 Repository Tree</h1>
<p align="center">Why not a tree as well? Visualize your project's GitHub directories and files.
</p>

|                                                                                                             |                                                                                    |
|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| <br><br/><b>📍 GitHub Repository Tree</b><br><br>Creates a GitHub directory tree to display in your README. | ![tree](https://github.com/eli64s/README-AI/blob/main/docs/imgs/tree.png?raw=true) |

<h1 align="center">⒋<br>👇<br><br>🐍 Environment Yaml</h1>
<p align="center">Creates directory and file setup/environment.yaml if missing, and writes the README installion guide.
</p>

|                                                                                                                                                                                      |                                                                                                |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| <br><br/><b>📍 Environment Yaml File</b><br><br>Creates your project's environment yaml<br> file and generates an installation guide section for others can use your project easily! | ![getting_started](https://github.com/eli64s/README-AI/blob/main/docs/imgs/usage.png?raw=true) |

<h1 align="center">5.<br>👇<br><br>🧩 Additional Sections</h1>
<p align="center">Additional sections to build a robust README template for your project!
</p>

|                                                                                                                                                                                      |                                                                                                |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| <br><br/><b>📍 Automated Introduction and Features section</b><br><br>Additional boilerplate documentation generated by the OpenAI API.    | ![header](https://github.com/eli64s/README-AI/blob/main/docs/imgs/overview.png?raw=true) 
| <br><br/><b>📍 Contributing section and more!</b><br><br>Generates multiple additional sections to complete your README template. | ![header](https://github.com/eli64s/README-AI/blob/main/docs/imgs/misc.png?raw=true) |


<h1 align="center">⒍<br>👇<br><br>🪄 Example Output Files</h1>
<h2 align="center">
  <a href="https://github.com/eli64s/README-AI/blob/main/docs/README_EX_1.md">1️⃣ README.md - Small Codebase</a>
  <br>
  <a href="https://github.com/eli64s/README-AI/blob/main/docs/README_EX_2.md">2️⃣ README.md - Large Codebase</a>
</h2>

---

## 🏎💨 Getting Started

### Prerequisites

Before you begin, ensure that you have the following prerequisites installed:

- Python 3.6 or higher
- Conda package manager (recommended)
- Access to the OpenAI API (see OpenAI API Setup below)

### GitHub Repository

Copy the url of your project's GitHub repository and update the code below in the [conf/conf.toml](conf/conf.toml) file.

```bash
# GitHub
[github]
url = "<INSERT-GITHUB-REPO>"
```

### OpenAI API Setup

To use README-AI, you will need an API key for OpenAI. Follow the steps below to create an API key:

<details closed>
<summary>User Guide</summary>

1. Go to the OpenAI website.
2. Click the "Sign up for free" button.
3. Fill out the registration form with your information and agree to the terms of service.
4. Once logged in, click on the "API" tab.
5. Follow the instructions to create a new API key.
6. Copy the API key and keep it in a secure place.

</details>

### Installation

1. Clone the README-AI repository:

```sh
git clone https://github.com/eli64s/README-AI.git && cd README-AI
```

2. Create a new Conda environment and install the required dependencies:

```sh
conda env create -f setup/environment.yaml
conda activate README-AI
```

3. Set up the OpenAI API key by creating an environment variable:

```sh
export OPENAI_API_KEY=<your-api-key>
```

Alternatively, you can set up the OpenAI API key in a .env file in the root directory of the project.

### Running README-AI

Once you have installed README-AI, you can generate a README file for your codebase by running the following command:

```sh
python src/main.py
```

---

## 🗺 Roadmap

- [ ] Add additional language models on top of OpenAI's to fine tune text.
- [ ] Add compatability for multiple additional languages.
- [ ] Implement different configuration README templates.

---

## 🤝 Contributing

Contributions are always welcome! Please follow these steps:

1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).
   ```sh
   git checkout -b new-feature-branch
   ```
4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.
   ```sh
   git commit -m 'Implemented new feature.'
   ```
6. Push your changes to your forked repository on GitHub using the following command
   ```sh
   git push origin new-feature-branch
   ```
7. Create a [pull request](https://github.com/eli64s/README-AI/pulls) to the original repository.

Open a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary. 
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 🪪 License

This project is licensed under the MIT License. See [README-AI's LICENSE](LICENSE) file for additional details.

---

## 📫 Contact

- If you have any questions or feedback about README-AI, feel free to start a [discussion!](https://github.com/eli64s/README-AI/discussions)
- If you have identified a bug, open a [new issue!](https://github.com/eli64s/README-AI/issues)

---

## 🙏 Acknowledgments

- Badge Icons: [Aveek-Saha/GitHub-Profile-Badges](https://github.com/Aveek-Saha/GitHub-Profile-Badges)

---
