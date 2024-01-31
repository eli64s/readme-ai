<p align="left">
  <img src="https://cdn-icons-png.flaticon.com/512/6295/6295417.png" width="100" />
</p>
<p align="left">
    <h1 align="left">ASYNC-ML-INFERENCE</h1>
</p>
<p align="left">
    <em>Async ML Inference: Empowering Distributed Machine Learning</em>
</p>
<p align="left">
	<img src="https://img.shields.io/github/license/FerrariDG/async-ml-inference?style=flat&color=white" alt="license">
	<img src="https://img.shields.io/github/last-commit/FerrariDG/async-ml-inference?style=flat&logo=git&logoColor=white&color=white" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/FerrariDG/async-ml-inference?style=flat&color=white" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/FerrariDG/async-ml-inference?style=flat&color=white" alt="repo-language-count">
<p>
<p align="left">
		<em>Developed with the software and tools below.</em>
</p>
<p align="left">
	<img src="https://img.shields.io/badge/Pydantic-E92063.svg?style=flat&logo=Pydantic&logoColor=white" alt="Pydantic">
	<img src="https://img.shields.io/badge/Redis-DC382D.svg?style=flat&logo=Redis&logoColor=white" alt="Redis">
	<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat&logo=YAML&logoColor=white" alt="YAML">
	<img src="https://img.shields.io/badge/Celery-37814A.svg?style=flat&logo=Celery&logoColor=white" alt="Celery">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white" alt="Docker">
	<img src="https://img.shields.io/badge/Numba-00A3E0.svg?style=flat&logo=Numba&logoColor=white" alt="Numba">
	<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=flat&logo=FastAPI&logoColor=white" alt="FastAPI">
</p>
<hr>

##  Quick Links

> - [ Overview](#-overview)
> - [ Features](#-features)
> - [ Repository Structure](#-repository-structure)
> - [ Modules](#-modules)
> - [ Getting Started](#-getting-started)
>   - [ Installation](#-installation)
>   - [ Running async-ml-inference](#-running-async-ml-inference)
>   - [ Tests](#-tests)
> - [ Project Roadmap](#-project-roadmap)
> - [ Contributing](#-contributing)
> - [ License](#-license)
> - [ Acknowledgments](#-acknowledgments)

---

##  Overview

The async-ml-inference project is a distributed ML inference system that enables asynchronous machine learning inference using a combination of API, workers, and clients. The system's core functionalities include extracting the length of an audio file and scraping Euromillions results. The API component, built with FastAPI and Celery, exposes endpoints for creating tasks related to audio length and Euro results, as well as querying task results. The workers component consists of Celery workers responsible for performing the audio length extraction and Euromillions results scraping tasks. The client component interacts with the API, sending audio URLs and dates, and retrieving the results. With its distributed architecture and asynchronous nature, async-ml-inference offers a scalable and efficient solution for performing machine learning inference tasks.

---

##  Features

|    |   Feature         | Description                                                                                                                           |
|----|-------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| ⚙️  | **Architecture**  | The project's architecture is based on a distributed ML inference system. It includes services such as the Celery broker, backend, workers for audio and Euro prediction, an API, and a client. The docker-compose.yaml file orchestrates the deployment and configuration of these components. |
| 🔩 | **Code Quality**  | The codebase exhibits good code quality and style. It follows PEP8 standards, as indicated by the inclusion of flake8, pycodestyle, and pydocstyle in the dependencies.                                    |
| 📄 | **Documentation** | The project has a moderate level of documentation. The codebase includes comments and docstrings in key modules, but a comprehensive README or user guide is missing.                      |
| 🔌 | **Integrations**  | Key integrations and external dependencies include Celery, FastAPI, Uvicorn, Pydantic, Redis, and RabbitMQ. These integrations are essential for enabling asynchronous ML inference and communication between components. |
| 🧩 | **Modularity**    | The codebase demonstrates a good level of modularity and reusability. The services are organized into separate modules, allowing for independent development and testing.                                 |
| 🧪 | **Testing**       | The project does not explicitly mention testing frameworks or tools. However, the inclusion of flake8 and mypy in the dependencies suggests the presence of linting and static analysis.                   |
| ⚡️  | **Performance**   | The project's efficiency, speed, and resource usage depend on several factors such as the underlying machine and the performance of the ML models being used. No specific performance evaluation is mentioned. |
| 🛡️ | **Security**      | The project does not extensively discuss security measures. However, utilizing Docker containers, authentication mechanisms, and secure communication protocols would enhance security. |
| 📦 | **Dependencies**  | Key external libraries and dependencies include joblib, requests, librosa, NumPy, SQLAlchemy, Celery, FastAPI, Uvicorn, Redis, and RabbitMQ. These libraries contribute to the functionality and performance of the system. |


---

##  Repository Structure

```sh
└── async-ml-inference/
    ├── Pipfile
    ├── Pipfile.lock
    ├── README.md
    ├── docker-compose.yaml
    ├── docs
    │   └── diagram
    ├── src
    │   ├── api
    │   ├── client
    │   └── workers
    └── tests
        └── README.md
```

---

##  Modules

<details closed><summary>.</summary>

| File                                                                                                   | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---                                                                                                    | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [docker-compose.yaml](https://github.com/FerrariDG/async-ml-inference/blob/master/docker-compose.yaml) | Code Summary:The docker-compose.yaml file defines the services and their configurations for setting up a distributed ML inference system. It includes a Celery broker, backend, workers for audio and euro prediction, an API, and a client. Each service has specific environment variables and connection details to ensure communication and functionality within the distributed system. This code snippet plays a critical role in orchestrating the deployment and configuration of the various components of the ML inference system. It specifies the necessary services, their dependencies, and network configurations, enabling the seamless integration and interaction between different parts of the system. |
| [Pipfile](https://github.com/FerrariDG/async-ml-inference/blob/master/Pipfile)                         | This code snippet is part of the async-ml-inference repository. It's a Pipfile defining the project's dependencies and scripts for running various components of the architecture, including API, workers, and client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [Pipfile.lock](https://github.com/FerrariDG/async-ml-inference/blob/master/Pipfile.lock)               | This code snippet is a part of the async-ml-inference repository. It contributes to the overall architecture by defining the structure for APIs, clients, and workers, enabling asynchronous machine learning inference.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

</details>

<details closed><summary>src.api</summary>

| File                                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---                                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                                                                          |
| [requirements.txt](https://github.com/FerrariDG/async-ml-inference/blob/master/src/api/requirements.txt) | The code snippet in `src/api/requirements.txt` specifies the required dependencies for the API module of the `async-ml-inference` repository. It includes packages like Celery, FastAPI, Uvicorn, and Pydantic. These dependencies are critical for running the API and enabling asynchronous machine learning inference.                                                                                    |
| [Dockerfile](https://github.com/FerrariDG/async-ml-inference/blob/master/src/api/Dockerfile)             | The code snippet, located at `src/api/Dockerfile`, builds a Docker image for the API component of the `async-ml-inference` repository. It installs the required dependencies and sets up the environment for running the API with Uvicorn. The built image exposes ports 5000, 6379, and 5672.                                                                                                               |
| [api.py](https://github.com/FerrariDG/async-ml-inference/blob/master/src/api/api.py)                     | The `api.py` file in the `src/api` directory serves as the entry point for receiving API requests in the async-ml-inference repository. It defines endpoints for creating tasks related to audio length and Euro results, and also exposes an endpoint for querying task results. The file utilizes the FastAPI framework for handling HTTP requests and the Celery library for asynchronous task execution. |

</details>

<details closed><summary>src.workers</summary>

| File                                                                                                         | Summary                                                                                                                                                                                                                                                                                                     |
| ---                                                                                                          | ---                                                                                                                                                                                                                                                                                                         |
| [backend.py](https://github.com/FerrariDG/async-ml-inference/blob/master/src/workers/backend.py)             | The `backend.py` file in the `src/workers` directory contains functions related to accessing the backend for the ML inference system's Redis database. These functions enable retrieving the Redis connection URL, checking if the backend is running, and establishing a connection to the Redis instance. |
| [requirements.txt](https://github.com/FerrariDG/async-ml-inference/blob/master/src/workers/requirements.txt) | This code snippet, located at `src/workers/requirements.txt`, specifies the required dependencies for the workers component in the repository's architecture. It includes packages such as beautifulsoup4, celery with redis, librosa, and numba.                                                           |
| [Dockerfile](https://github.com/FerrariDG/async-ml-inference/blob/master/src/workers/Dockerfile)             | The Dockerfile in src/workers sets up a container for running workers in the async-ml-inference repository. It installs required dependencies, copies necessary files, and exposes ports for communication.                                                                                                 |
| [broker.py](https://github.com/FerrariDG/async-ml-inference/blob/master/src/workers/broker.py)               | The code in `src/workers/broker.py` is responsible for establishing a connection with a RabbitMQ broker. It retrieves the required connection configuration from environment variables and creates the broker URL. It also provides a function to check if the broker is running.                           |

</details>

<details closed><summary>src.workers.audio</summary>

| File                                                                                                 | Summary                                                                                                                                                                                                                                                                    |
| ---                                                                                                  | ---                                                                                                                                                                                                                                                                        |
| [worker.py](https://github.com/FerrariDG/async-ml-inference/blob/master/src/workers/audio/worker.py) | This code snippet, located at `src/workers/audio/worker.py`, is a Celery worker responsible for extracting the length of an audio file. It retrieves the audio data from a specified url, loads it using Librosa library, calculates the duration, and returns the result. |
| [config.py](https://github.com/FerrariDG/async-ml-inference/blob/master/src/workers/audio/config.py) | This code snippet is responsible for configuring the Celery worker for audio length calculation. It sets options for task acknowledgement, task prefetching, task queue creation, and Redis key time to live (TTL).                                                        |

</details>

<details closed><summary>src.workers.euro</summary>

| File                                                                                                | Summary                                                                                                                                                                                                                                                     |
| ---                                                                                                 | ---                                                                                                                                                                                                                                                         |
| [worker.py](https://github.com/FerrariDG/async-ml-inference/blob/master/src/workers/euro/worker.py) | This code snippet is a Celery worker responsible for scraping Euromillions results from a specified date. It validates the backend and broker connections, fetches the results page, extracts numbers and stars from the page, and returns them in a tuple. |
| [config.py](https://github.com/FerrariDG/async-ml-inference/blob/master/src/workers/euro/config.py) | This code snippet provides Celery configuration for the Euromillions Results worker in the async-ml-inference repository. Key features include task acknowledgement, prefetch multiplier, queue definition, and expiration time for results.                |

</details>

<details closed><summary>src.client</summary>

| File                                                                                                        | Summary                                                                                                                                                                                                                                                                                                                                  |
| ---                                                                                                         | ---                                                                                                                                                                                                                                                                                                                                      |
| [requirements.txt](https://github.com/FerrariDG/async-ml-inference/blob/master/src/client/requirements.txt) | This code snippet in `src/client/requirements.txt` specifies the required packages `requests`, `retrying`, and `joblib` for the client component of the `async-ml-inference` repository.                                                                                                                                                 |
| [Dockerfile](https://github.com/FerrariDG/async-ml-inference/blob/master/src/client/Dockerfile)             | This code snippet represents the Dockerfile for the client component of the async-ml-inference project. It sets up the client environment, installs the required dependencies, exposes port 5000, and runs the client.py script.                                                                                                         |
| [client.py](https://github.com/FerrariDG/async-ml-inference/blob/master/src/client/client.py)               | This code snippet, located at src/client/client.py, is responsible for sending audio URLs and dates to an API endpoint and retrieving the results. It utilizes parallel processing and retry mechanisms to handle network requests and wait for task completion. The main goal is to interact with the API and display the task results. |

</details>

---

##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Python**: `version x.y.z`

###  Installation

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

###  Running async-ml-inference

Use the following command to run async-ml-inference:

```sh
python main.py
```

###  Tests

To execute tests, run:

```sh
pytest
```

---

##  Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/FerrariDG/async-ml-inference/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/FerrariDG/async-ml-inference/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/FerrariDG/async-ml-inference/issues)**: Submit bugs found or log feature requests for Async-ml-inference.

<details closed>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone https://github.com/FerrariDG/async-ml-inference
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
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-quick-links)

---
