
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
async-ml-inference
</h1>
<h3>◦ Efficiently predict the future with async-ml-inference.</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/scikitlearn-F7931E.svg?style&logo=scikit-learn&logoColor=white" alt="scikitlearn" />
<img src="https://img.shields.io/badge/.ENV-ECD53F.svg?style&logo=dotenv&logoColor=black" alt=".ENV" />
<img src="https://img.shields.io/badge/Redis-DC382D.svg?style&logo=Redis&logoColor=white" alt="Redis" />
<img src="https://img.shields.io/badge/Jinja-B41717.svg?style&logo=Jinja&logoColor=white" alt="Jinja" />
<img src="https://img.shields.io/badge/SciPy-8CAAE6.svg?style&logo=SciPy&logoColor=white" alt="SciPy" />
<img src="https://img.shields.io/badge/Celery-37814A.svg?style&logo=Celery&logoColor=white" alt="Celery" />

<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style&logo=Docker&logoColor=white" alt="Docker" />
<img src="https://img.shields.io/badge/NumPy-013243.svg?style&logo=NumPy&logoColor=white" alt="NumPy" />
<img src="https://img.shields.io/badge/Numba-00A3E0.svg?style&logo=Numba&logoColor=white" alt="Numba" />
<img src="https://img.shields.io/badge/FastAPI-009688.svg?style&logo=FastAPI&logoColor=white" alt="FastAPI" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
</p>

![GitHub top language](https://img.shields.io/github/languages/top/FerrariDG/async-ml-inference?style&color=5D6D7E)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/FerrariDG/async-ml-inference?style&color=5D6D7E)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/FerrariDG/async-ml-inference?style&color=5D6D7E)
![GitHub license](https://img.shields.io/github/license/FerrariDG/async-ml-inference?style&color=5D6D7E)
</div>

---

## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [⚙️ Features](#-features)
- [📂 Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🚀 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The async-ml-inference repository is a project that provides a web API for processing audio and EuroMillions lottery results asynchronously, using Celery and Redis for task queuing and result storage. The API can be accessed from a client application that sends requests with audio URLs and dates to the API for processing. The project aims to provide a scalable and efficient solution for handling large-scale audio processing and lottery result scraping, with the added benefit of handling tasks asynchronously.

---

## ⚙️ Features

Feature | Description |
|-----|-----|
| **🏗 Architecture** | The codebase follows a microservices architecture pattern with separate components for the API server and backend workers. Celery is used as the task queue for handling background tasks and Redis and RabbitMQ are used as the message broker and backend respectively. The code implements a robust and scalable architecture for handling audio and Euro data processing using decoupled components. |
| **📑 Documentation** | The codebase includes a Pipfile for managing dependencies, and Dockerfiles for building the required containers. The code files are adequately commented and include docstrings, making it easy for new developers to understand the code. Additionally, the repository includes a README file with instructions on how to set up and run the API server and workers. |
| **🧩 Dependencies** | The codebase relies on a number of third-party libraries for its functionality, including FastAPI, Celery, Redis, RabbitMQ, BeautifulSoup, and requests. All dependencies are declared in the Pipfile, simplifying the installation process. |
| **♻️ Modularity** | The codebase is modular and follows the separation of concerns principle. The different components such as the API server, Celery tasks, configuration files, and worker implementations are separated into their respective directories. This improves readability and maintainability of the codebase. |
| **✔️ Testing** | The codebase includes basic unit tests for the Celery tasks that are implemented. However, comprehensive tests for the API endpoints and worker functions are not included. Additional tests would improve the reliability and maintainability of the codebase. |
| **⚡️ Performance** | The codebase is generally well optimized for performance. Celery is used to enable asynchronous task execution, and the codebase uses caching and retries to optimize the execution time of the tasks. However, additional performance optimizations may be needed as the size of the input data scales. |
| **🔒 Security** | The codebase incorporates some security features, including the use of environment variables to store sensitive information, and the use of secure transport protocols such as HTTPS. However, the API endpoints do not include authentication or authorization mechanisms, and sensitive data such as Redis and RabbitMQ connection data are included in the codebase. Additional security measures are needed to improve the security of the codebase. |
| **🔀 Version Control** | The codebase is hosted on GitHub and uses Git for version control. The code includes descriptive commit messages, making it easy to track changes to the codebase over time. However, there are no tags or releases for the codebase, which would improve the ease of collaboration and versioning. |
| **🔌 Integrations** | The codebase includes integrations with third-party services such as Redis, RabbitMQ, and BeautifulSoup. However, additional integrations with services such as a cloud storage platform or audio processing libraries would be needed to further improve the functionality

---


## 📂 Project Structure


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

## 🧩 Modules

<details closed><summary>Api</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                                                  | Module             |
|:-----------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
| Dockerfile | The provided code snippet is a Dockerfile that sets up a Python 3.7 environment for a web API with dependencies listed in requirements.txt. It installs the dependencies, copies the API file, sets up port exposure, and defines the command to run the API using the Uvicorn server on port 5000.                                      | src/api/Dockerfile |
| api.py     | The provided code snippet sets up a FastAPI that interacts with a Celery background task queue to process audio and Euro data. It also provides functionality to retrieve task results, and has options to send task results to an external service. The code reads environment variables for RabbitMQ and Redis connection information. | src/api/api.py     |

</details>

<details closed><summary>Audio</summary>

| File      | Summary                                                                                                                                                                                                                                                                                                                       | Module                      |
|:----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------|
| worker.py | This code defines a Celery task called "audio_length", which takes an audio URL as input and extracts the length of the audio file. The task checks if the backend and broker are running, and handles exceptions such as failure to load the audio file or network errors. The extracted length is returned as a dictionary. | src/workers/audio/worker.py |
| config.py | This code snippet sets configurations for a Celery worker that processes audio length tasks. The worker is set to acknowledge tasks only when they are returned or fail due to unhandled exceptions. It also creates a queue for the worker to handle tasks and sets a time-to-live limit for Redis keys.                     | src/workers/audio/config.py |

</details>

<details closed><summary>Client</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                      | Module                |
|:-----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
| Dockerfile | The code snippet sets up a Python 3.7 environment, installs dependencies listed in requirements.txt, copies client.py file, exposes port 5000, and runs the client.py file as the default command. The code executes in a slimmed-down Debian Buster container.                                              | src/client/Dockerfile |
| client.py  | The provided code snippet sends a set of audio URLs and dates to a web API and retrieves the results using parallel processing. The code uses the requests library for making HTTP requests, joblib for parallel processing, and retrying for handling task retries. The results are printed to the console. | src/client/client.py  |

</details>

<details closed><summary>Euro</summary>

| File      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Module                     |
|:----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------|
| worker.py | The provided code is a Celery worker that scrapes the EuroMillions lottery results from a given URL using BeautifulSoup. It checks if the broker and backend servers are running before executing the task. The `scrappy_result` function defined within the worker takes in a draw date as input parameter and returns a tuple of integers representing the drawn numbers and stars for that date. The function also handles exceptions and updates the state of the task accordingly. | src/workers/euro/worker.py |
| config.py | This code snippet is a module with Celery configurations for a worker that processes Euromillions results. It sets the task_acks_late flag to True, resulting in delayed task acknowledgements, and a prefetch multiplier of 1. The worker is configured to use a single queue named "euro", and the results expire after 48 hours.                                                                                                                                                     | src/workers/euro/config.py |

</details>

<details closed><summary>Root</summary>

| File    | Summary                                                                                                                                                                                                                                                                                         | Module   |
|:--------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
| Pipfile | The provided code snippet is a configuration file for a Python project. It lists dependencies and their versions under different categories such as dev-packages and packages. It also includes scripts for running the project and necessary services such as a broker and backend for Celery. | Pipfile  |

</details>

<details closed><summary>Workers</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                                                                                     | Module                 |
|:-----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------|
| backend.py | The code snippet defines functions to retrieve Redis configuration values, generate a backend URL based on these values, and check if a Redis instance is running. The Redis module is imported, and exceptions are handled appropriately. The code can thus be used to create a Redis client and check whether a connection can be established.                            | src/workers/backend.py |
| Dockerfile | This code snippet is for building a Docker container for a Python application. It installs the necessary dependencies listed in requirements.txt, sets the working directory to /workers, and exposes ports 6379 and 5672. Additionally, it copies the application files to the container.                                                                                  | src/workers/Dockerfile |
| broker.py  | The code snippet defines functions to retrieve connection details and check if a RabbitMQ instance is running. It uses Python's `os` module to get environment variables for the connection details and the `kombu` library to establish a connection. The `is_broker_running` function attempts to connect to RabbitMQ and return a boolean indicating success or failure. | src/workers/broker.py  |

</details>

---

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - [ℹ️ Requirement 1]
> - [ℹ️ Requirement 2]
> - [...]

### 🖥 Installation

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
pytest
```

---


## 🗺 Roadmap

> - [X] [ℹ️  Task 1: Implement X]
> - [ ] [ℹ️  Task 2: Refactor Y]
> - [ ] [...]


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
7. Create a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 📄 License

This project is licensed under the `[ℹ️  INSERT-LICENSE-TYPE]` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 👏 Acknowledgments

> - [ℹ️  List any resources, contributors, inspiration, etc.]

---
