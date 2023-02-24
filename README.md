<div align="center">
  <h1 align="center">
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
    <br />
    PydocsAI
  </h1>
  <h3 align="center">Automate README creation, code documentation, and more!</h3>
  <h4 align="center">🏎💨 Powered by OpenAI's language model API and the tools listed below.</h4>
  <p align="center">
    <img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="Markdown" />
    <img src="https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white" alt="OpenAI" />
    <img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/Pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
    <img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=for-the-badge&logo=HTML5&logoColor=white" alt="HTML5" />
    <img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=for-the-badge&logo=GNU-Bash&logoColor=white" alt="Bash" />
    <img src="https://img.shields.io/badge/Anaconda-44A833.svg?style=for-the-badge&logo=Anaconda&logoColor=white" alt="Anaconda" />
  </p>
</div>

---

## 🌊 Overview

PydocsAI is a Python package that provides an automated way to generate a README.md file and document your codebase. This package leverages OpenAI's GPT Davinci model to translate a given codebase to natural language, producing a structured project README template that includes codebase metadata and documentation.

The project is still under development and is opinionated in its setup, but it can be used as a starting point for projects that require documentation. The current version of PyDocsAI is limited to codebases written in Python.

---

## 🔮 Features

<h1 align="center">👇<br /><br />1. 🤖 Codebase Documentation</h1>
<p align="center">Have you met anyone who said they loved documenting code? That’s why we're building this project, hope you enjoy!
</p>

|   |   |
| --- | --- |
| <b>Codebase Documentation</b><br /><br />This project leverages OpenAI's GPT Davinci<br /> model to convert a given Python codebase into<br /> natural language, producing a well-structured<br /> project README template that includes codebase metadata, documentation<br /> and other essential details. | ![header](docs/imgs/docs.png) |

<h1 align="center">👇<br /><br />⒉ 🪪 Badges</h1>
<p align="center">Visualize project dependencies and components in your README's header section with badges.
</p>

|   |   |
| --- | --- |
| <br /><br/><b>Profile Badges</b><br /><br />Analyzes your project's dependencies and requirements, displaying them as badges<br /> in the README's header section. | ![badges](docs/imgs/head.png) |

<h1 align="center">👇<br /><br />⒊ 🌳 Project Tree</h1>
<p align="center">Why not a tree as well? Visualize your project's GitHub directories and files.
</p>

|   |   |
| --- | --- |
| <br /><b>Project Tree</b><br /><br />Creates a GitHub directory tree to display in your README.| ![tree](docs/imgs/tree.png) |

<h1 align="center">👇<br /><br />⒋ 🐍 Environment YAML</h1>
<p align="center">Creates the directory and file setup/environment.yaml if it does not already exit, and writes the README installion section.
</p>

|   |   |
| --- | --- |
| <br /><br/><b>Environment Yaml</b><br /><br />Creates your project's environment yaml<br /> file and generates an installation guide section for others can use your project easily! | ![badges](docs/imgs/usage.png) |

<br />
<h1 align="center">👇<br /><br /><a href="https://github.com/eli64s/PydocsAI/blob/main/docs/readme.md">Example Output README File</a></h1>

---

## 🚀 Getting Started

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

To use PydocsAI, you will need an API key for OpenAI. Follow the steps below to create an API key:

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

1. Clone the PydocsAI repository:

```sh
git clone https://github.com/eli64s/PydocsAI.git && cd PydocsAI
```

2. Create a new Conda environment and install the required dependencies:

```sh
conda env create -f setup/environment.yaml
conda activate pydocsai
```

3. Set up the OpenAI API key by creating an environment variable:

```sh
export OPENAI_API_KEY=<your-api-key>
```

Alternatively, you can set up the OpenAI API key in a .env file in the root directory of the project.

### Running PydocsAI

Once you have installed PydocsAI, you can generate a README file for your codebase by running the following command:

```sh
python src/main.py
```

---

## 📍 Roadmap

- [ ] Add compatability for additional file types.
- [ ] Extend capabilities beyond code documentation.
- [ ] Implement different configuration file templates.

---

## 🤝 Contributing

We welcome contributions to PydocsAI from the open-source community! If you would like to contribute, please see our contribution guidelines for more information.

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 📧 Contact

If you have any questions or feedback about PydocsAI, please feel free to reach out. We would be happy to hear from you!

---

## 🙏 Acknowledgments

- Badge Icons: [Aveek-Saha/GitHub-Profile-Badges](https://github.com/Aveek-Saha/GitHub-Profile-Badges)

---
