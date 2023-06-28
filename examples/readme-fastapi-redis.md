
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
async-ml-inference
</h1>
<h3>◦ Real-time ML magic, with async-ml-inference!</h3>
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

## 📒 Table of Contents
- [📒 Table of Contents](#-table-of-contents)
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

The project is a complete end-to-end solution for asynchronous machine learning inference, including an API for task creation and retrieval, workers for processing tasks, and a client for interacting with the API. It supports task processing for audio file length extraction and EuroMillions results scraping. The project leverages the capabilities of Celery and Redis for efficient background task processing and deploys the components using Docker containers for easy deployment and scalability. It enables users to offload computationally expensive tasks to workers, improving the performance and efficiency of machine learning inference tasks.

---

## ⚙️ Features

| Feature                | Description                                                                                                                                                                                                                                                           |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **⚙️ Architecture**    | The codebase follows a microservices architecture with separate components for the API, workers, and client. The API uses FastAPI for handling HTTP requests and Celery for background task processing. The workers are responsible for executing specific tasks asynchronously.                            |
| **📖 Documentation**   | The codebase lacks comprehensive documentation. While there are some comments in the code, there is no overall documentation describing the system's architecture, design patterns, or usage instructions. A more thorough explanation of the code and its components would be helpful for understanding and maintaining the system. |
| **🔗 Dependencies**    | The system relies on several external libraries, including FastAPI, Redis, RabbitMQ, Celery, Beautiful Soup, and Kombu. These dependencies provide functionality for handling HTTP requests, background task processing, handling data from Redis, and scraping data from websites.                                                |
| **🧩 Modularity**      | The codebase is organized into smaller components with separate directories for the API, workers, and client. Each directory contains code specific to its functionality, making it relatively easy to modify or replace individual components without impacting the overall system.                                                          |
| **✔️ Testing**         | The codebase does not include any tests. The lack of tests makes it difficult to ensure the correctness and reliability of the system. Implementing a testing strategy, including unit and integration tests, would greatly improve the codebase's stability and maintainability.                                  |
| **⚡️ Performance**     | The performance of the system highly depends on external systems like Redis and RabbitMQ for task queuing and message passing. The codebase itself does not have significant performance bottlenecks. However, the presence of long task processing times in the workers could impact overall performance.                        |
| **🔐 Security**        | The codebase does not include any explicit security measures. It is important to harden the system components, such as Redis and RabbitMQ, with appropriate access controls and authentication mechanisms to protect the data and ensure the system's security.                                           |
| **🔀 Version Control** | The codebase is hosted on GitHub, utilizing Git for version control. This allows for collaboration, tracking changes, and maintaining different branches for development and releases.                                                                                   |
| **🔌 Integrations**    | The system integrates with Redis and RabbitMQ for efficient task processing, Celery for executing background tasks, and Beautiful Soup and Kombu for scraping website data and handling message passing. Additional integrations could be added to expand the system's functionality.                          |
| **📶 Scalability**     | The system's architecture allows for horizontal scalability by adding more instances of the API, workers, or client components. The use of queue-based task processing and microservices architecture enables scaling the different components independently to handle increased

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

<details closed><summary>Root</summary>

| File                                                                         | Summary                                                                                                                                                                                                                                                                                     |
| ---                                                                          | ---                                                                                                                                                                                                                                                                                         |
| [Pipfile](https://github.com/FerrariDG/async-ml-inference/blob/main/Pipfile) | The provided code snippet is a configuration file that specifies dependencies, scripts, and URLs for a project. It includes package versions, development packages, script commands for running various components (e.g., brokers, workers), and URLs for accessing resources (e.g., PyPI). |

</details>

<details closed><summary>Api</summary>

| File                                                                                       | Summary                                                                                                                                                                                                                                                                                                       |
| ---                                                                                        | ---                                                                                                                                                                                                                                                                                                           |
| [Dockerfile](https://github.com/FerrariDG/async-ml-inference/blob/main/src/api/Dockerfile) | This code sets up the environment for a Python API. It installs the required dependencies, copies the API code, exposes the necessary ports, and starts the API server using Uvicorn.                                                                                                                         |
| [api.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/api/api.py)         | This code snippet sets up a FastAPI application with Celery and Redis for background task processing. It defines two API routes for creating and retrieving tasks. The tasks are sent to the Celery worker and their results are stored in Redis. The code also includes a function to send the task results. |

</details>

<details closed><summary>Workers</summary>

| File                                                                                           | Summary                                                                                                                                                                                                                                                     |
| ---                                                                                            | ---                                                                                                                                                                                                                                                         |
| [backend.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/backend.py) | The code snippet provides functions to retrieve Redis connection details (host, port, password, and database) from environment variables, construct a Redis URL, and check if a Redis instance is running.                                                  |
| [Dockerfile](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/Dockerfile) | This code snippet sets up a Python environment for workers. It installs necessary dependencies, upgrades pip, and installs packages from a requirements.txt file. It copies the code into the workers directory, exposes ports 6379 and 5672.               |
| [broker.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/broker.py)   | The code snippet provides functions to retrieve the RabbitMQ connection details, construct the broker URL, and check if the broker is running. It retrieves environment variables for customization and utilizes the kombu library for connection handling. |

</details>

<details closed><summary>Audio</summary>

| File                                                                                               | Summary                                                                                                                                                                                                                                                                                                                       |
| ---                                                                                                | ---                                                                                                                                                                                                                                                                                                                           |
| [worker.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/audio/worker.py) | This code snippet defines a Celery worker that extracts the length of an audio file. It checks if the backend and broker are running, then fetches the audio file from a URL. It loads the audio data, calculates the length, and simulates a long task processing time. Finally, it returns the audio length.                |
| [config.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/audio/config.py) | This code snippet includes configuration settings for a Celery worker that processes audio files. It sets the worker to acknowledge tasks only when they are returned or fail, limits the worker to handle only one task at a time, creates a queue for audio tasks, and sets the expiration time for Redis keys to 48 hours. |

</details>

<details closed><summary>Euro</summary>

| File                                                                                              | Summary                                                                                                                                                                                                                                                                                                                                                         |
| ---                                                                                               | ---                                                                                                                                                                                                                                                                                                                                                             |
| [worker.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/euro/worker.py) | This code snippet is a Celery worker that scrapes Euromillions results from a website. It checks the status of the backend and broker services, then defines a task called "scrappy_result" that takes a draw date as input. It opens the corresponding URL, parses the HTML using Beautiful Soup, extracts the numbers and stars, and returns them as a tuple. |
| [config.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/euro/config.py) | The code snippet configures Celery for a EuroMillions Results worker. It enables late task acknowledgements, sets worker prefetch multiplier to 1, creates a single queue named "euro", and sets the result expiration time to 48 hours.                                                                                                                        |

</details>

<details closed><summary>Client</summary>

| File                                                                                          | Summary                                                                                                                                                                                                           |
| ---                                                                                           | ---                                                                                                                                                                                                               |
| [Dockerfile](https://github.com/FerrariDG/async-ml-inference/blob/main/src/client/Dockerfile) | The given code creates a Docker container for a Python client application. It installs required dependencies, copies the application files, exposes port 5000, and sets the startup command as'python client.py'. |
| [client.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/client/client.py)   | This code snippet sends requests to an API with audio URLs and dates, retrieves task IDs, and then retrieves the corresponding results. It uses parallel processing for efficiency.                               |

</details>

---

## 🚀 Getting Started

### ✔️ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - `ℹ️ Requirement 1`
> - `ℹ️ Requirement 2`
> - `ℹ️ ...`

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

### 🎮 Using async-ml-inference

```sh
python main.py
```

### 🧪 Running Tests
```sh
pytest
```

---


## 🗺 Roadmap

> - [X] `ℹ️  Task 1: Implement X`
> - [ ] `ℹ️  Task 2: Refactor Y`
> - [ ] `ℹ️ ...`


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

This project is licensed under the `ℹ️  INSERT-LICENSE-TYPE` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 👏 Acknowledgments

> - `ℹ️  List any resources, contributors, inspiration, etc.`

---
