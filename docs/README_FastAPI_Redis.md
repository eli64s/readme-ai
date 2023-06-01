
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
async-ml-inference
</h1>
<h3 align="center">📍 Revolutionize your ML with lightning-fast async inference on GitHub!</h3>
<h3 align="center">🚀 Developed with the software and tools below:</h3>

<p align="center">
<img src="https://img.shields.io/badge/Redis-DC382D.svg?style=for-the-badge&logo=Redis&logoColor=white" alt="Redis" />
<img src="https://img.shields.io/badge/Celery-37814A.svg?style=for-the-badge&logo=Celery&logoColor=white" alt="Celery" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=for-the-badge&logo=Docker&logoColor=white" alt="Docker" />
<img src="https://img.shields.io/badge/Numba-00A3E0.svg?style=for-the-badge&logo=Numba&logoColor=white" alt="Numba" />
<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=for-the-badge&logo=FastAPI&logoColor=white" alt="FastAPI" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="Markdown" />
</p>
</div>

---

## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍Overview](#-overview)
- [🔮 Features](#-features)
- [⚙️ Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🏎💨 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [🪪 License](#-license)
- [📫 Contact](#-contact)
- [🙏 Acknowledgments](#-acknowledgments)

---


## 📍Overview

The async-ml-inference project is a distributed task queue system that utilizes Celery, RabbitMQ, and Redis to perform audio length extraction and lottery result scraping tasks. The project includes an API server and client for submitting and retrieving task results, as well as Docker containers for deploying the system. The value proposition of this project is that it provides an efficient and scalable solution for performing machine learning inference tasks asynchronously.

---

## 🔮 Features

Feature | Description |
|---|---|
| **🏗 Overall Structure and Organization** | The repository has a clear and modular design, with separate directories for the API, workers, and client. The use of Celery for task distribution and Redis for task persistence allows for efficient and scalable processing. |
| **📝 Code Documentation** | The codebase has adequate inline documentation for most modules and functions, but some modules lack clear explanations or examples of usage. |
| **🧩 Dependency Management** | Dependencies are clearly defined in the Pipfile, with separate sections for production and development dependencies. The use of Docker containers ensures consistent environments across development and deployment. |
| **♻️ Code Modularity and Reusability** | The codebase is well-organized into separate modules, with clear separation of concerns between the API, workers, and client. Functions and classes are generally well-designed and reusable, but some modules have overlapping functionality. |
| **✅ Testing and Quality Assurance** | The codebase lacks automated tests, but includes some manual testing scripts in the client directory. The use of Docker containers and Celery task retries helps ensure fault tolerance and reliable processing. |
| **⚡️ Performance and Optimization** | The use of Celery for task distribution allows for efficient processing, but some tasks may be CPU-bound and could benefit from parallelization or optimization. |
| **🔒 Security Measures** | The codebase does not include any explicit security measures, such as authentication or data encryption. However, the use of Docker containers and Celery task queues may provide some inherent security benefits. |
| **🔄 Version Control and Collaboration** | The repository is well-organized and includes clear commit messages, but lacks documentation on contribution guidelines or issue tracking. |
| **🔌 External Integrations** | The codebase includes external integrations with RabbitMQ and Redis for task distribution and persistence, and with Beautifulsoup4 for web scraping. |
| **📈 Scalability and Extensibility** | The use of Celery and Redis allows for efficient and scalable task processing, and the codebase is designed to be easily extended with new tasks or modules. However, some modules may require significant modification to add new functionality. |

---


<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## ⚙️ Project Structure


```bash
repo
├── Pipfile
├── Pipfile.lock
├── README.md
├── docker-compose.yaml
├── docs
│   └── diagram
│       ├── architecture.png
│       └── diagram.py
├── src
│   ├── api
│   │   ├── Dockerfile
│   │   ├── api.py
│   │   └── requirements.txt
│   ├── client
│   │   ├── Dockerfile
│   │   ├── client.py
│   │   └── requirements.txt
│   └── workers
│       ├── Dockerfile
│       ├── audio
│       │   ├── config.py
│       │   └── worker.py
│       ├── backend.py
│       ├── broker.py
│       ├── euro
│       │   ├── config.py
│       │   └── worker.py
│       └── requirements.txt
└── tests
    └── README.md

10 directories, 21 files
```

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 💻 Modules

<details closed><summary>Api</summary>

| File       | Summary                                                                                                                                                                                                                                                           | Module             |
|:-----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
| Dockerfile | The provided code snippet sets up a Docker container based on Python 3.7. It installs the required dependencies specified in requirements.txt, copies the api.py file to the working directory, exposes three ports, and runs the API using Uvicorn on port 5000. | src/api/Dockerfile |
| api.py     | HTTP 429 error when fetching summary.                                                                                                                                                                                                                             | src/api/api.py     |

</details>

<details closed><summary>Audio</summary>

| File      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Module                      |
|:----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------|
| worker.py | This code snippet defines a Celery worker for audio length extraction. It imports necessary libraries and functions, checks if the backend and broker are running, and defines a task called "audio_length" that takes an audio URL as input and returns the length of the audio file. The task loads the audio file using the librosa library, simulates a long task processing, and returns the audio length. If an error occurs during the task, it updates the state of the task and raises an exception. | src/workers/audio/worker.py |
| config.py | This code snippet configures a Celery worker for processing audio tasks. The worker will only handle one task at a time and will acknowledge the task only after completion or if it fails due to an unhandled exception. A queue named "audio" is created for the worker to fetch tasks from, and the result of each task will expire after 48 hours.                                                                                                                                                        | src/workers/audio/config.py |

</details>

<details closed><summary>Client</summary>

| File       | Summary                                                                                                                                                                                                                                      | Module                |
|:-----------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
| Dockerfile | HTTP 429 error when fetching summary.                                                                                                                                                                                                        | src/client/Dockerfile |
| client.py  | The code sends HTTP POST requests to API endpoints to process audio files and dates. It uses parallel processing to improve efficiency and includes retry logic for failed requests. The results of the requests are printed to the console. | src/client/client.py  |

</details>

<details closed><summary>Euro</summary>

| File      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Module                     |
|:----------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------|
| worker.py | This code snippet creates a Celery worker that scrapes the results of the Euromillions lottery from a specified URL using Beautiful Soup. The worker is initiated with a broker and backend URL, and includes functions to check if the backend and broker are running. The "scrappy_result" function is a Celery task that takes a draw date as input and returns a tuple of integers representing the lottery numbers and stars. If the scraping fails, the task updates its state and raises an Ignore exception. | src/workers/euro/worker.py |
| config.py | This module contains Celery configurations for the Euromillions Results worker. It sets the task acknowledgement to be late, the worker prefetch multiplier to be 1, and defines a single task queue named "euro". Additionally, the expiration time for results is set to 48 hours.                                                                                                                                                                                                                                 | src/workers/euro/config.py |

</details>

<details closed><summary>Root</summary>

| File                | Summary                                                                                                                                                                                                                                                                                                                                                                 | Module              |
|:--------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------|
| docker-compose.yaml | The code snippet provides a Docker Compose file to deploy a Celery distributed task queue system. The system consists of a RabbitMQ message broker, a Redis backend, two Celery workers for audio and euro tasks, an API server, and a client. The Compose file also sets up the necessary environment variables and network connections between the services.          | docker-compose.yaml |
| Pipfile             | The provided code snippet is a configuration file for a Python project that specifies dependencies, development packages, and scripts to be executed. It includes packages such as Celery, FastAPI, and Beautifulsoup4, and scripts for running a broker, backend, and workers. Additionally, it includes scripts for generating diagrams and running a client and API. | Pipfile             |
| Pipfile.lock        | HTTP 400 error when fetching summary.                                                                                                                                                                                                                                                                                                                                   | Pipfile.lock        |

</details>

<details closed><summary>Workers</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                                                                                                 | Module                 |
|:-----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------|
| backend.py | The provided code snippet defines functions for retrieving Redis connection details from environment variables and constructing a Redis URL. It also includes a function for checking if a Redis instance is running by attempting to connect to it. If the connection fails, an error message is printed and the function returns False.                                               | src/workers/backend.py |
| Dockerfile | The code snippet sets up a Python 3.7 environment, installs the necessary dependencies specified in requirements.txt, and exposes ports 6379 and 5672. It also copies the current directory into the /workers directory and cleans up unnecessary files after installation.                                                                                                             | src/workers/Dockerfile |
| broker.py  | This code provides functions to retrieve the necessary information to establish a connection with a RabbitMQ instance, such as the username, password, port, and virtual host. It also includes a function to check if the broker is running by attempting to establish a connection with retries. If the connection fails, an error message is printed and the function returns False. | src/workers/broker.py  |

</details>

<hr />

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> `[📌  INSERT-PROJECT-PREREQUISITES]`

### 💻 Installation

1. Clone the async-ml-inference repository:
```sh
git clone https://github.com/FerrariDG/async-ml-inference
```

2. Change to the project directory:
```sh
cd async-ml-inference
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

### 🤖 Using async-ml-inference

```sh
python main.py
```

### 🧪 Running Tests
```sh
# [INSERT-COMMAND-FOR-TESTS]
```

<hr />


## 🛠 Future Development
- [X] [📌  COMPLETED-TASK]
- [ ] [📌  INSERT-TASK]
- [ ] [📌  INSERT-TASK]


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
7. Create a pull request to the original repository.
Open a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 🪪 License

This project is licensed under the `[📌  INSERT-LICENSE-TYPE]` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 🙏 Acknowledgments

[📌  INSERT-DESCRIPTION]


---

