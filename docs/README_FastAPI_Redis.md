
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
async-ml-inference
</h1>
<h3 align="center">📍 Instantly power up your ML with Async-ML-Inference on GitHub!</h3>
<h3 align="center">🚀 Developed with the software and tools below:</h3>

<p align="center">
<img src="https://img.shields.io/badge/scikitlearn-F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikitlearn" />
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

This project provides a distributed system for asynchronous machine learning inference, using a combination of message queue, backend, and API services. The system can handle tasks related to audio processing and lottery result scraping, with the ability to add more tasks as needed. The purpose of the project is to allow for efficient, scalable inference, and can be used for various ML applications. Its value proposition is its ability to handle large-scale inference tasks asynchronously, with support for task management and result logging.

---

## 🔮 Features

Feature | Description |
|---|---|
| **🏗 Structure and Organization** | The codebase has a well-organized folder structure with separate directories for workers, API, and client code. The use of Docker Compose for defining the setup of different services in a distributed system is also a well-thought-out architectural decision. |
| **📝 Code Documentation** | The code has clear and concise docstrings for functions, and comments are present where necessary. Overall, the code documentation is of good quality and is helpful for understanding the purpose of each component. |
| **🧩 Dependency Management** | Dependencies are well-managed through the use of Pipfiles and Pipfile.lock to specify package versions for development and runtime environments. |
| **♻️ Modularity and Reusability** | The code is highly modular and reusable, with individual workers for specific tasks, a separate API service for handling requests, and a client application for interacting with the API. |
| **✅ Testing and Quality Assurance** | Directories for testing are present in the repository, but tests are lacking or incomplete for some of the components. Nonetheless, test-driven development (TDD) practice is encouraged in the code documentation. |
| **⚡️ Performance and Optimization** | The codebase uses Celery for asynchronous task processing, which allows for efficient and parallel processing of tasks in a distributed system. However, bottlenecks may still arise due to limited resources, which can be mitigated by scaling the number of workers. |
| **🔒 Security Measures** | The use of environment variables to store sensitive information such as passwords, and the inclusion of a.gitignore file to prevent sensitive data from being pushed to the repository, is a good security practice. However, more security measures such as HTTPS can be added to the API endpoint for secure communication. |
| **🔄 Version Control and Collaboration** | The use of Git for version control and Github for collaboration is evident in the repository, with clear commit messages and branches. However, a lack of collaboration beyond a single contributor is evident. |
| **🔌 External Integrations** | The codebase integrates with external libraries such as librosa for audio processing and BeautifulSoup for web scraping. It also integrates with external services such as RabbitMQ and Redis for backend and broker functionality. |
| **📈 Scalability and Extensibility** | The use of Docker Compose and Celery allows for easy scaling of the system by adding more containers and workers as needed. The well-organized and modular codebase also allows for easy addition of new workers and APIs to the system. |

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

| File       | Summary                                                                                                                                                                                                                                                                                                                                                                                                                         | Module             |
|:-----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
| Dockerfile | The provided code snippet creates a Docker image for a Python API. It copies the requirements.txt and api.py files to the image, installs the dependencies, exposes three ports (5000, 6379, 5672), and runs the API on port 5000 using the Uvicorn server.                                                                                                                                                                     | src/api/Dockerfile |
| api.py     | The provided code snippet defines a Python application using FastAPI and Celery for asynchronous task processing, with Redis and RabbitMQ as backend and broker respectively. The application defines two endpoints for creating and querying task results, and supports optional callback functionality for sending results to remote servers. It also includes a function for handling task result serialization and logging. | src/api/api.py     |

</details>

<details closed><summary>Audio</summary>

| File      | Summary                                                                                                                                                                                                                                                                                                                                                                                    | Module                      |
|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------|
| worker.py | The provided code snippet is a Celery worker for extracting the length of an audio file from a given URL. It uses the librosa library to load and process the audio data and returns the length in seconds. The code also includes error handling, logging, and simulation of a long task processing.                                                                                      | src/workers/audio/worker.py |
| config.py | This code snippet sets configurations for a Celery worker that handles tasks related to audio length. These configurations include having the worker acknowledge tasks only after they have been completed or have failed, limiting the worker to only one task at a time, creating a queue for the worker to pull tasks from, and setting the expiration time for Redis keys to 48 hours. | src/workers/audio/config.py |

</details>

<details closed><summary>Client</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                                              | Module                |
|:-----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
| Dockerfile | The provided code snippet is a Dockerfile that installs necessary dependencies for a Python app using pip, and copies the app's files into the container. It then exposes port 5000 and runs the app using the command "python client.py" when the container is started.                                                             | src/client/Dockerfile |
| client.py  | This code snippet sends audio URLs and draws dates to an API endpoint, retrieves task IDs, and uses them to get results via another endpoint. The results are printed to the console. It uses the joblib module for parallel execution, the requests module for HTTP requests, and the retrying module for retrying failed requests. | src/client/client.py  |

</details>

<details closed><summary>Euro</summary>

| File      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                          | Module                     |
|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------|
| worker.py | The provided code snippet is a Celery worker for scraping Euromillions lottery results from a designated URL. It contains functions for checking if the required backend and broker services are running, and for scraping lottery results based on a provided date. The results are returned as a tuple of integers representing the numbers drawn in the lottery. The function also handles exceptions and updates the task state accordingly. | src/workers/euro/worker.py |
| config.py | The provided code snippet configures a Celery worker for Euromillions Results using the kombu library to create a single queue called "euro". The worker is set to acknowledge tasks after they have finished processing, and prefetches one task at a time. Results are set to expire after 48 hours.                                                                                                                                           | src/workers/euro/config.py |

</details>

<details closed><summary>Root</summary>

| File                | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Module              |
|:--------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------|
| docker-compose.yaml | The code snippet is a Docker Compose configuration file that defines the setup for a distributed system consisting of different services. The services include a RabbitMQ message broker, a Redis database, Celery workers for audio and euro data processing, an API service that interacts with the workers, and a client application. The services are connected through a network and each service has its own container with specified configurations. | docker-compose.yaml |
| Pipfile             | The code snippet is a configuration file for a Python project that specifies dependencies and scripts for various tasks. It includes a list of development and runtime packages with specific version numbers, as well as scripts for running a Celery broker and backend, starting workers for different tasks, running a FastAPI server, and running a client script.                                                                                     | Pipfile             |
| Pipfile.lock        | HTTP 400 error when fetching summary.                                                                                                                                                                                                                                                                                                                                                                                                                       | Pipfile.lock        |

</details>

<details closed><summary>Workers</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                                                                                                                    | Module                 |
|:-----------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------|
| backend.py | This code snippet provides a set of functions to connect to a Redis database. The functions retrieve the required connection parameters (such as password and port) from environment variables or use default values. The "is_backend_running" function checks whether a connection to the Redis instance can be established, and returns a Boolean value indicating success or failure.                   | src/workers/backend.py |
| Dockerfile | This code snippet sets up a Python environment on Debian 10 "buster", installs required libraries and dependencies, and exposes specific ports. It copies a requirements file to a directory called "workers", sets the working directory to "workers", installs the requirements, and removes unnecessary files. Finally, it copies all files to the "workers" directory and exposes ports 6379 and 5672. | src/workers/Dockerfile |
| broker.py  | The provided code snippet sets up a connection to RabbitMQ message broker, using environmental variables to determine the credentials, port number, and virtual host. The "is_broker_running" function attempts to establish a connection to the broker, with a default of 3 retries, and returns a boolean indicating success. If unsuccessful, an error message is printed.                              | src/workers/broker.py  |

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

`[📌  INSERT-REFERENCES-AND-RESOURCES]`


---

