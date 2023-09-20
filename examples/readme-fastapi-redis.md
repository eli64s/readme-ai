<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>async-ml-inference
</h1>
<h3>◦ Fast, Reliable AI: async-ml-inference</h3>
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
<img src="https://img.shields.io/github/languages/top/FerrariDG/async-ml-inference?style&color=5D6D7E" alt="GitHub top language" />
<img src="https://img.shields.io/github/languages/code-size/FerrariDG/async-ml-inference?style&color=5D6D7E" alt="GitHub code size in bytes" />
<img src="https://img.shields.io/github/commit-activity/m/FerrariDG/async-ml-inference?style&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/license/FerrariDG/async-ml-inference?style&color=5D6D7E" alt="GitHub license" />
</div>

---

## 📖 Table of Contents
- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [⚙️ Modules](#modules)
- [🚀 Getting Started](#-getting-started)
    - [🔧 Installation](#-installation)
    - [🤖 Running async-ml-inference](#-running-async-ml-inference)
    - [🧪 Tests](#-tests)
- [🛣 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The project aims to provide an asynchronous machine learning inference system using distributed task management and a web API. It includes components for processing audio lengths and scraping EuroMillions results. The system offers the ability to handle background tasks, retrieve task results, and supports parallel processing for increased efficiency. Its value lies in enabling efficient and scalable inference, making it suitable for applications that require real-time processing of audio data and retrieval of scraped information.

---

## 📦 Features

| Feature                | Description                           |
| ---------------------- | ------------------------------------- |
| **⚙️ Architecture**     | The codebase follows a microservices architecture, with separate services for RabbitMQ message broker, Redis backend, Celery workers, API service, and client service. The services are connected via a network. The use of Docker Compose allows for easy setup and management of the multi-container environment.
| **📃 Documentation**   | The codebase lacks comprehensive documentation. While some files contain brief descriptions of their purpose, there is no central documentation or README file providing an overview of the project's features and usage. Further documentation would benefit developers trying to understand and contribute to the project.
| **🔗 Dependencies**    | The codebase relies on various external libraries and systems. Some notable dependencies include BeautifulSoup, Celery, FastAPI, RabbitMQ, Redis, and Uvicorn. These libraries provide functionality for web scraping, distributed task management, API development, message queuing, and backend storage. The dependencies are specified in the Pipfile and Pipfile.lock files.
| **🧩 Modularity**      | The codebase demonstrates modularity by organizing components into separate directories (api and workers), each containing their own set of files. This separation allows for easy understanding and maintenance of each component. The code also makes use of modular libraries like Celery and FastAPI, enabling the creation of interchangeable components.
| **🧪 Testing**          | The codebase does not include explicit testing strategies and tools. However, the modular design of the components allows for easier testing and isolation of functionality. Developers can implement unit tests for individual components by mocking dependencies and using test frameworks like pytest.
| **⚡️ Performance**      | The performance of the system depends on the efficiency of the individual components. The use of Celery for distributed task management and Redis for backend storage helps improve the system's speed and resource usage. However, specific performance benchmarks or optimization techniques are not mentioned in the codebase.
| **🔐 Security**        | The codebase does not explicitly address security measures. However, potential security concerns include the handling of user credentials for RabbitMQ and Redis connections, as well as the validation and sanitization of user inputs in the API endpoints. The code could benefit from the implementation of authentication and authorization mechanisms to protect sensitive data.
| **🔀 Version Control** | The codebase uses Git for version control, as evidenced by the presence of a .gitignore file and the GitHub repository itself. However, the code lacks versioning information, such as tags or release notes, to indicate the progression and history of the project. Proper use of branching and pull requests would facilitate collaborative development and code review processes.
| **🔌 Integrations**    | The system interacts with external systems like RabbitMQ and Redis for message queuing and backend storage, respectively. It also utilizes external libraries like BeautifulSoup for web scraping and requests for making HTTP requests. The modular design of the codebase allows for easy integration with other services or APIs as needed.
| **📶 Scalability**     | The use of a microservices architecture with separate components allows for scalability by adding or removing services based on demand. The codebase shows potential for horizontal scalability by replicating and load balancing the worker services. However, the code does not incorporate explicit scalability features, such as auto-scaling or dynamic resource allocation.

---


## 📂 Repository Structure


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

## ⚙️ Modules

<details closed><summary>Root</summary>

| File                                                                                                 | Summary                                                                                                                                                                                                                                                                                                                                                                                   |
| ---                                                                                                  | ---                                                                                                                                                                                                                                                                                                                                                                                       |
| [docker-compose.yaml](https://github.com/FerrariDG/async-ml-inference/blob/main/docker-compose.yaml) | This code sets up a multi-container environment using Docker Compose. It includes a RabbitMQ message broker, a Redis backend, Celery workers for audio and euro tasks, an API service, and a client service. The services are connected via a network.                                                                                                                                    |
| [Pipfile](https://github.com/FerrariDG/async-ml-inference/blob/main/Pipfile)                         | This code defines package dependencies, scripts for running various components, and their versions. It includes libraries like BeautifulSoup, Celery, FastAPI, and others, with corresponding versions specified. It also sets up scripts for running components like RabbitMQ, Redis, Flower, and Celery workers. Finally, it includes a script for running the API and a client script. |
| [Pipfile.lock](https://github.com/FerrariDG/async-ml-inference/blob/main/Pipfile.lock)               | HTTPStatus Exception: 400                                                                                                                                                                                                                                                                                                                                                                 |

</details>

<details closed><summary>Api</summary>

| File                                                                                                   | Summary                                                                                                                                                                                                                                                                                      |
| ---                                                                                                    | ---                                                                                                                                                                                                                                                                                          |
| [requirements.txt](https://github.com/FerrariDG/async-ml-inference/blob/main/src/api/requirements.txt) | The code utilizes Celery for distributed task management, FastAPI for building APIs, and Uvicorn as the ASGI server. Pydantic is used for data validation and serialization.                                                                                                                 |
| [Dockerfile](https://github.com/FerrariDG/async-ml-inference/blob/main/src/api/Dockerfile)             | This code sets up a Python web API using the FastAPI framework. It installs required dependencies, copies the API code, and exposes ports for communication. Finally, it runs the API using Uvicorn with specific host and port configurations.                                              |
| [api.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/api/api.py)                     | This code sets up a FastAPI server that interacts with Celery to handle background tasks. It defines two endpoints for creating tasks, and a third endpoint to get the result of a task by its ID. The code also includes a helper function to send task results to an external destination. |

</details>

<details closed><summary>Workers</summary>

| File                                                                                                       | Summary                                                                                                                                                                                                                                                                                                         |
| ---                                                                                                        | ---                                                                                                                                                                                                                                                                                                             |
| [backend.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/backend.py)             | The code includes functions to retrieve Redis connection details from environment variables, construct a Redis connection URL, and check if the Redis backend is running by attempting a connection. The code promotes flexibility and reusability by allowing easy customization of Redis connection settings. |
| [requirements.txt](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/requirements.txt) | The code utilizes the BeautifulSoup4 library for web scraping, Celery with Redis for task management, Librosa for audio analysis, and Numba for just-in-time compilation.                                                                                                                                       |
| [Dockerfile](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/Dockerfile)             | This code sets up a Python environment, installs required dependencies, and copies the code into a working directory. It also exposes ports 6379 and 5672.                                                                                                                                                      |
| [broker.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/broker.py)               | This code provides functions to get the RabbitMQ connection URL, check if the RabbitMQ broker is running, and handle connection errors. It uses environment variables for user credentials, host, port, and vhost.                                                                                              |

</details>

<details closed><summary>Audio</summary>

| File                                                                                               | Summary                                                                                                                                                                                                                                                                                        |
| ---                                                                                                | ---                                                                                                                                                                                                                                                                                            |
| [worker.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/audio/worker.py) | This code defines a Celery worker for extracting the length of an audio file from a given URL. It validates the running status of the backend and broker, retrieves the audio data, and calculates the length using librosa. The task is executed asynchronously.                              |
| [config.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/audio/config.py) | This module configures the Celery worker for processing audio lengths. It sets the worker to acknowledge tasks only when they complete or fail, allows the worker to process only one task at a time, creates a queue for the worker, and sets the expiration time for Redis keys to 48 hours. |

</details>

<details closed><summary>Euro</summary>

| File                                                                                              | Summary                                                                                                                                                                                                                                                                                   |
| ---                                                                                               | ---                                                                                                                                                                                                                                                                                       |
| [worker.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/euro/worker.py) | This code is a Celery worker that scrapes the Euromillions website for results. It checks if the backend and broker services are running, then defines a task to scrape the results for a given draw date. It handles exceptions and returns the numbers and stars from the scraped page. |
| [config.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/euro/config.py) | This module sets up Celery configurations for the Euromillions Results worker, including task acknowledgements, prefetching, queue name, and result expiration time. It ensures efficient task processing and result management.                                                          |

</details>

<details closed><summary>Client</summary>

| File                                                                                                      | Summary                                                                                                                                                                                                  |
| ---                                                                                                       | ---                                                                                                                                                                                                      |
| [requirements.txt](https://github.com/FerrariDG/async-ml-inference/blob/main/src/client/requirements.txt) | This code uses the requests library to make HTTP requests, retrying library to handle retry logic, and joblib library for parallel processing.                                                           |
| [Dockerfile](https://github.com/FerrariDG/async-ml-inference/blob/main/src/client/Dockerfile)             | This code sets up a Python environment, installs project dependencies, and copies a Python script. It then exposes port 5000 and runs the script when the container starts.                              |
| [client.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/client/client.py)               | This code sends audio URLs and dates to an API, retrieves task IDs, and then retrieves the results of those tasks using parallel processing. It also handles retrying requests and printing the results. |

</details>

---

## 🚀 Getting Started

***Dependencies***

Before you begin, ensure that you have the following prerequisites installed:
> - `ℹ️ Requirement 1`
> - `ℹ️ Requirement 2`
> - `ℹ️ ...`

### 🔧 Installation

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

### 🤖 Running async-ml-inference

```sh
python main.py
```

### 🧪 Tests
```sh
pytest
```

---


## 🛣 Roadmap

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
