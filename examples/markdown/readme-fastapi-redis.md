<div align="center">
<h1><img src=https://img.icons8.com/external-tal-revivo-regular-tal-revivo/96/external-readme-is-a-easy-to-build-a-developer-hub-that-adapts-to-the-user-logo-regular-tal-revivo.png width="100" />
<br>ASYNC-ML-INFERENCE</h1>
<h3>◦ Unlocking code potential with powerful README creation.</h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/.ENV-ECD53F.svg?style=flat&logo=dotenv&logoColor=black" alt=".ENV" />
<img src="https://img.shields.io/badge/Redis-DC382D.svg?style=flat&logo=Redis&logoColor=white" alt="Redis" />
<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat&logo=YAML&logoColor=white" alt="YAML" />
<img src="https://img.shields.io/badge/Celery-37814A.svg?style=flat&logo=Celery&logoColor=white" alt="Celery" />

<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white" alt="Docker" />
<img src="https://img.shields.io/badge/Numba-00A3E0.svg?style=flat&logo=Numba&logoColor=white" alt="Numba" />
<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=flat&logo=FastAPI&logoColor=white" alt="FastAPI" />
</p>
<img src="https://img.shields.io/github/license/FerrariDG/async-ml-inference?style=flat&color=5D6D7E" alt="GitHub license" />
<img src="https://img.shields.io/github/last-commit/FerrariDG/async-ml-inference?style=flat&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/FerrariDG/async-ml-inference?style=flat&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/languages/top/FerrariDG/async-ml-inference?style=flat&color=5D6D7E" alt="GitHub top language" />
</div>
<hr>

## 🔗 Quick Links
- [🔗 Quick Links](#-quick-links)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [🧩 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
  - [⚙️ Installation](#️-installation)
  - [🤖 Running async-ml-inference](#-running-async-ml-inference)
  - [🧪 Tests](#-tests)
- [🚧 Project Roadmap](#-project-roadmap)
- [🤝 Contributing](#-contributing)
    - [*Contributing Guidelines*](#contributing-guidelines)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

The code repository, async-ml-inference, is a comprehensive system for asynchronous machine learning inference. It utilizes a Celery-based architecture to handle audio file processing and Euro lottery result scraping. The repository includes services for the backend, API, client, and workers. The API endpoints allow users to create and retrieve audio processing tasks and Euro results. The workers include an audio worker that calculates audio file durations and a Euro worker that scrapes Euromillions results. Dependencies such as FastAPI, Celery, librosa, and requests are managed using Pipenv and Docker. The repository structure ensures efficient and scalable execution of machine learning inference tasks with high reliability and performance.

---

## 📦 Features

|    | Feature            | Description                                                                                                        |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The system follows a microservices architecture. It consists of various components/services, including an API, client, backend, audio worker, and euro worker. The system utilizes Celery for task management and RabbitMQ for message queuing. Each service is built and deployed as a separate Docker container. |
| 📄 | **Documentation**  | The documentation for the codebase is not explicitly mentioned in the repository structure or file summaries. Further analysis is required to assess the quality and comprehensiveness of the documentation. |
| 🔗 | **Dependencies**   | The system relies on several external libraries and tools. Some notable dependencies include Celery, FastAPI, uvicorn, pydantic, Redis, RabbitMQ, NumPy, and Beautiful Soup. The complete list of dependencies can be found in the Pipfile and requirements.txt files within the repository. |
| 🧩 | **Modularity**     | The system is organized into smaller, interchangeable components/services. Each component has its own directory within the src folder, and they can be developed, deployed, and scaled independently. The modular design enables easy maintenance, testing, and extensibility. |
| 🧪 | **Testing**        | The testing strategies and tools used in the system are not explicitly mentioned in the provided information. Further analysis is required to evaluate the system's testing practices. |
| ⚡️  | **Performance**    | The performance characteristics of the system are not explicitly mentioned in the provided information. Further analysis is required to assess the system's performance in terms of speed, efficiency, and resource usage. |
| 🔐 | **Security**       | The security measures implemented in the system are not explicitly mentioned in the provided information. Further analysis is required to evaluate the security features and practices employed by the codebase. |
| 🔀 | **Version Control**| The version control strategies and tools used in the system are not explicitly mentioned in the provided information. Further analysis is required to assess the system's version control practices. |
| 🔌 | **Integrations**   | The system interacts with other systems and services such as RabbitMQ and Redis for message queuing and backend storage, respectively. The integration with these services allows for scalable and distributed architecture. |
| 📶 | **Scalability**    | The system's ability to handle growth is supported by its microservices architecture and the use of Celery for task management. Each component can be scaled independently, allowing for horizontal scalability. Additionally, the use of Docker containers simplifies deployment and scaling processes. |

---

## 📂 Repository Structure

```sh
└── async-ml-inference/
    ├── .env
    ├── Pipfile
    ├── Pipfile.lock
    ├── docker-compose.yaml
    ├── src/
    │   ├── api/
    │   │   ├── Dockerfile
    │   │   ├── api.py
    │   │   └── requirements.txt
    │   ├── client/
    │   │   ├── Dockerfile
    │   │   ├── client.py
    │   │   └── requirements.txt
    │   └── workers/
    │       ├── Dockerfile
    │       ├── audio/
    │       ├── backend.py
    │       ├── broker.py
    │       ├── euro/
    │       └── requirements.txt

```

---


## 🧩 Modules

<details closed><summary>.</summary>

| File                                                                                                 | Summary                                                                                                                                                                                                                                                                                                                     |
| ---                                                                                                  | ---                                                                                                                                                                                                                                                                                                                         |
| [docker-compose.yaml](https://github.com/FerrariDG/async-ml-inference/blob/main/docker-compose.yaml) | The code snippet is a docker-compose.yaml file in the async-ml-inference repository. It defines services for a Celery-based system, including a broker, backend, audio worker, euro worker, API, and client. Each service is built from a specific directory and has its own set of environment variables and dependencies. |
| [Pipfile](https://github.com/FerrariDG/async-ml-inference/blob/main/Pipfile)                         | The code snippet in the Pipfile file provides a list of packages and their versions required for the repository. It also includes scripts for running various components of the system, such as the API, workers, and client.                                                                                               |
| [.env](https://github.com/FerrariDG/async-ml-inference/blob/main/.env)                               | The code in the `.env` file sets the PYTHONPATH environment variable to include the current directory, the `src` directory, and the `src/workers` directory.                                                                                                                                                                |
| [Pipfile.lock](https://github.com/FerrariDG/async-ml-inference/blob/main/Pipfile.lock)               | Code snippet summary: The code in this snippet is responsible for handling the asynchronous machine learning inference process within the repository.                                                                                                                                                                       |

</details>

<details closed><summary>src/api</summary>

| File                                                                                                   | Summary                                                                                                                                                                                                                                                           |
| ---                                                                                                    | ---                                                                                                                                                                                                                                                               |
| [requirements.txt](https://github.com/FerrariDG/async-ml-inference/blob/main/src/api/requirements.txt) | The code snippet is located at `src/api/requirements.txt` in the repository structure. It includes the dependencies `celery[redis, librabbitmq]`, `fastapi`, `uvicorn`, and `pydantic`.                                                                           |
| [Dockerfile](https://github.com/FerrariDG/async-ml-inference/blob/main/src/api/Dockerfile)             | This code snippet builds and configures a Docker image for the API service in the async-ml-inference repository. It installs required dependencies, copies the API script, exposes necessary ports, and starts the API server.                                    |
| [api.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/api/api.py)                     | The code snippet defines the API endpoints for creating and retrieving tasks related to audio processing and Euro results. It utilizes Celery for task management and communicates with RabbitMQ and Redis for message queuing and backend storage, respectively. |

</details>

<details closed><summary>src/workers</summary>

| File                                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                                            |
| ---                                                                                                        | ---                                                                                                                                                                                                                                                                                                                                                                |
| [backend.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/backend.py)             | The code snippet in `backend.py` provides functions for managing the connection to a Redis instance. It retrieves the Redis host, port, password, and database number from environment variables and uses them to establish a connection. It also includes a function to check if the backend is running by making a connection and performing an operation on it. |
| [requirements.txt](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/requirements.txt) | This code snippet specifies the dependencies required for the workers functionality in the async-ml-inference repository. It includes beautifulsoup4, celery with redis, librosa, and numba.                                                                                                                                                                       |
| [Dockerfile](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/Dockerfile)             | This code snippet provides the Dockerfile configuration for the workers module in the async-ml-inference repository.                                                                                                                                                                                                                                               |
| [broker.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/broker.py)               | This code snippet provides functions to retrieve RabbitMQ connection details and check if the RabbitMQ broker is running.                                                                                                                                                                                                                                          |

</details>

<details closed><summary>src/workers/audio</summary>

| File                                                                                               | Summary                                                                                                                                                                                                                                                          |
| ---                                                                                                | ---                                                                                                                                                                                                                                                              |
| [worker.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/audio/worker.py) | This code snippet defines a Celery worker that extracts the length of an audio file. It checks if the backend and broker services are running, then downloads and loads the audio file, calculates its duration, and returns the length as a result.             |
| [config.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/audio/config.py) | The code snippet in `src/workers/audio/config.py` sets up the configuration for the Audio Length worker in the repository's architecture. It includes settings for task acknowledgement, worker prefetching, task queue creation, and setting the Redis key TTL. |

</details>

<details closed><summary>src/workers/euro</summary>

| File                                                                                              | Summary                                                                                                                                                                                                                                                                                                                    |
| ---                                                                                               | ---                                                                                                                                                                                                                                                                                                                        |
| [worker.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/euro/worker.py) | This code snippet contains a Celery worker that scrapes Euromillions results from a website. It checks if the backend and broker are running before executing the task. The worker opens a URL, parses the HTML, and extracts the numbers and stars drawn in a specific draw. It returns a tuple of the numbers and stars. |
| [config.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/euro/config.py) | This code snippet provides Celery configurations for the Euromillions Results worker in the async-ml-inference repository. It sets task acknowledgements to be late, configures worker prefetch multiplier, defines a task queue, and sets the result expiration time to 48 hours.                                         |

</details>

<details closed><summary>src/client</summary>

| File                                                                                                      | Summary                                                                                                                                                                                                                                                          |
| ---                                                                                                       | ---                                                                                                                                                                                                                                                              |
| [requirements.txt](https://github.com/FerrariDG/async-ml-inference/blob/main/src/client/requirements.txt) | This code snippet specifies the dependencies required by the client module of the async-ml-inference repository. It includes requests, retrying, and joblib libraries.                                                                                           |
| [Dockerfile](https://github.com/FerrariDG/async-ml-inference/blob/main/src/client/Dockerfile)             | The code snippet is a Dockerfile located at src/client/Dockerfile within the repository. It sets up a containerized environment for a Python client application, installs dependencies, copies the client code, exposes a port, and runs the client application. |
| [client.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/client/client.py)               | The code snippet in `src/client/client.py` sends audio URLs and dates to specified endpoints, retrieves task results, and prints the results.                                                                                                                    |

</details>

---

## 🚀 Getting Started

***Prerequisites***

Ensure you have the following dependencies installed on your system:

- `► INSERT-DEPENDENCY-1`
- `► INSERT-DEPENDENCY-2`
- `► INSERT-DEPENDENCY-3`

### ⚙️ Installation

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


## 🚧 Project Roadmap

> - [X] `ℹ️  Task 1: Implement X`
> - [ ] `ℹ️  Task 2: Implement Y`
> - [ ] `ℹ️ ...`


---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/FerrariDG/async-ml-inference/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/FerrariDG/async-ml-inference/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/FerrariDG/async-ml-inference/issues)**: Submit bugs found or log feature requests for FERRARIDG.

#### *Contributing Guidelines*

<details closed>
<summary>Click to expand</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone <your-forked-repo-url>
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear and concise message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

## 📄 License


This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 👏 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#Top)

---
