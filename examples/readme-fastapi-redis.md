
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
async-ml-inference
</h1>
<h3>◦ Real-time predictions at lightning speed with async-ml-inference!</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/scikitlearn-F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikitlearn" />
<img src="https://img.shields.io/badge/.ENV-ECD53F.svg?style=for-the-badge&logo=dotenv&logoColor=black" alt=".ENV" />
<img src="https://img.shields.io/badge/Redis-DC382D.svg?style=for-the-badge&logo=Redis&logoColor=white" alt="Redis" />
<img src="https://img.shields.io/badge/Jinja-B41717.svg?style=for-the-badge&logo=Jinja&logoColor=white" alt="Jinja" />
<img src="https://img.shields.io/badge/SciPy-8CAAE6.svg?style=for-the-badge&logo=SciPy&logoColor=white" alt="SciPy" />
<img src="https://img.shields.io/badge/Celery-37814A.svg?style=for-the-badge&logo=Celery&logoColor=white" alt="Celery" />

<img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=for-the-badge&logo=Docker&logoColor=white" alt="Docker" />
<img src="https://img.shields.io/badge/NumPy-013243.svg?style=for-the-badge&logo=NumPy&logoColor=white" alt="NumPy" />
<img src="https://img.shields.io/badge/Numba-00A3E0.svg?style=for-the-badge&logo=Numba&logoColor=white" alt="Numba" />
<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=for-the-badge&logo=FastAPI&logoColor=white" alt="FastAPI" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="Markdown" />
</p>
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

The Async-ML-Inference project is a set of Python scripts that work together to provide an asynchronous machine learning inference API, allowing users to submit tasks for audio length extraction and EuroMillions lottery result scraping. The project is built using Celery and FastAPI, and utilizes RabbitMQ and Redis for message queuing and storage. The value proposition of the project is its ability to perform machine learning inference tasks asynchronously, allowing for greater scalability and efficiency.

---

## ⚙️ Features

Feature | Description |
|-----|-----|
| **🏗 Architecture** | The codebase follows a microservices architecture, with separate workers for audio processing and EuroMillions lottery results scraping, and a FastAPI-based API for receiving requests and distributing the tasks. Celery and Redis are used for message queuing and backend processing, and RabbitMQ is used as a broker. The codebase also includes a Dockerfile for building a container for the API and workers. |
| **📑 Documentation** | The codebase includes clear documentation, including README files in the root directory and the API and workers subdirectories, as well as comments throughout the code. The README files provide instructions for building and running the API and workers in a Docker environment, as well as descriptions of their functionality and configuration. |
| **🧩 Dependencies** | The codebase includes a number of dependencies, including libraries for audio processing (librosa), web scraping (beautifulsoup4), and message queuing (Celery, RabbitMQ, Redis). The codebase also includes several development packages for linting (flake8) and diagramming (diagrams). |
| **♻️ Modularity** | The codebase is modular, with separate subdirectories for the API and workers, and separate modules for task execution and configuration. The workers each have their own Dockerfile, and the API Dockerfile sets up the API separately from the workers. This modularity allows for easier maintenance and scaling. |
| **✔️ Testing** | The codebase includes some basic unit tests for the Celery tasks, but additional testing could be added to improve test coverage. |
| **⚡️ Performance** | The codebase is designed for high performance, utilizing asynchronous processing with Celery, RabbitMQ, and Redis to handle multiple tasks efficiently. The use of Docker containers also allows for easy scalability. |
| **🔒 Security** | The codebase includes some security measures, such as using Redis for storing task results rather than exposing them in API responses, and using Celery's late ack feature to avoid processing a task more than once. However, further security measures such as authentication and authorization could be added to the API. |
| **🔀 Version Control** | The codebase is version-controlled using git, with frequent commits and a clear commit history. The use of branches also allows for easier collaboration and development. |
| **🔌 Integrations** | The codebase integrates several technologies, including RabbitMQ and Redis for message queuing and backend processing, and joblib for parallel processing. It also includes endpoints for audio processing and EuroMillions lottery results scraping. |
| **📈 Scalability** | The codebase is designed for high scalability, with separate workers and an API that can be deployed in separate containers. The use of Celery, RabbitMQ, and Redis also allows for efficient handling of multiple tasks. However, further performance testing and

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

| File       | Summary                                                                                                                                                                                                                                                                                                                                                                   | Module             |
|:-----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
| Dockerfile | The code snippet sets up a Docker container for a Python API using the 3.7-slim-buster image. It installs the Python packages listed in requirements.txt and exposes ports for the API, Redis and RabbitMQ. Finally, it runs the API using the uvicorn server.                                                                                                            | src/api/Dockerfile |
| api.py     | The provided code snippet is a Python program that utilizes Celery and FastAPI for asynchronous task processing and web API framework respectively. It includes functions to create audio and Euro results tasks, to get task results, and to send task results to somewhere. It also includes necessary configuration variables and Pydantic models for data validation. | src/api/api.py     |

</details>

<details closed><summary>Audio</summary>

| File      | Summary                                                                                                                                                                                                                                                                                                                                                                                               | Module                      |
|:----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------|
| worker.py | The provided code snippet is a Celery worker for extracting the length of an audio file using librosa library. The worker is initiated with a broker and backend and the audio length extraction task is defined as a Celery task. The task loads the audio URL, extracts the audio length, and returns the result. Any exception raised during the task is handled and the task is marked as failed. | src/workers/audio/worker.py |
| config.py | This code snippet sets configurations for a Celery worker responsible for Audio Length tasks. It enables the worker to acknowledge tasks only upon completion or failure, limits it to one task at a time and assigns a queue for those tasks. Additionally, it sets the Redis key time to live to 48 hours.                                                                                          | src/workers/audio/config.py |

</details>

<details closed><summary>Client</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                                                                                                                       | Module                |
|:-----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
| Dockerfile | The provided code snippet is a Dockerfile for a Python client that copies the requirements.txt and client.py files into a working directory, installs the necessary dependencies, and runs the client.py file on port 5000. The Docker image ensures that pip is upgraded and the requirements are compiled and cached for more efficient execution, then removes unnecessary files to reduce the image size. | src/client/Dockerfile |
| client.py  | The code sends requests to two endpoints in parallel using joblib, one for audio URL length and the other for Euro lottery results. The retrying module is used to handle cases where the API is still processing requests. The results are then printed for each task that completed successfully, otherwise, an error message is printed.                                                                   | src/client/client.py  |

</details>

<details closed><summary>Euro</summary>

| File      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                | Module                     |
|:----------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------|
| worker.py | This code is a Celery worker that scrapes Euromillions lottery results from a website using the Beautiful Soup library, and returns the numbers and stars for a given draw date as a tuple. The code includes error handling for cases where the website cannot be reached or if the numbers and stars are not found on the page. The Celery worker is connected to a broker and backend server through functions in external modules. | src/workers/euro/worker.py |
| config.py | This code snippet is setting configurations for a worker that handles tasks related to EuroMillions results using the Celery library. It enables late acks for tasks, sets a prefetch multiplier of 1, defines a single queue for the task, and sets a result expiration time of 48 hours.                                                                                                                                             | src/workers/euro/config.py |

</details>

<details closed><summary>Root</summary>

| File    | Summary                                                                                                                                                                                                                                                                                                                                                                                    | Module   |
|:--------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
| Pipfile | The provided code snippet contains a configuration file that specifies dependencies and scripts for a Python project. It includes development packages such as diagrams and flake8, as well as packages like beautifulsoup4 and celery. The scripts section includes commands for starting a RabbitMQ broker, a Redis backend, and various Celery workers and Flower for monitoring tasks. | Pipfile  |

</details>

<details closed><summary>Workers</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                            | Module                 |
|:-----------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------|
| backend.py | The provided code snippet defines several functions for retrieving configuration parameters related to connecting to Redis, and for checking if a Redis instance is running. The `get_backend_url()` function returns a Redis connection string based on the retrieved parameters. The `is_backend_running()` function attempts to connect to the Redis instance, and returns a boolean indicating whether the connection was successful.          | src/workers/backend.py |
| Dockerfile | This code snippet creates a Docker image based on Python 3.7, installs the necessary dependencies and libraries, copies the code into the image, and exposes ports 6379 and 5672. It uses a requirements.txt file to install the required Python packages and removes unnecessary files to optimize the image. The resulting image can be used to run workers for tasks like message queuing and audio processing.                                 | src/workers/Dockerfile |
| broker.py  | This code snippet provides functions for generating a broker URL and checking if the RabbitMQ instance is running. It uses the `os` and `kombu` modules to fetch environment variables and establish connections with the broker. The `get_broker_url()` function constructs a URL based on the retrieved variables and the `is_broker_running()` function attempts to establish a connection and returns a boolean indicating success or failure. | src/workers/broker.py  |

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
