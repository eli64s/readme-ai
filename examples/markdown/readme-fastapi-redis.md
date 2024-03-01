<p align="center">
  <img src="https://img.icons8.com/external-tal-revivo-duo-tal-revivo/100/external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-duo-tal-revivo.png" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">ASYNC-ML-INFERENCE</h1>
</p>
<p align="center">
    <em>Empower ML Inference with Asynchronous Efficiency!</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/FerrariDG/async-ml-inference?style=flat&logo=opensourceinitiative&logoColor=white&color=blueviolet" alt="license">
	<img src="https://img.shields.io/github/last-commit/FerrariDG/async-ml-inference?style=flat&logo=git&logoColor=white&color=blueviolet" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/FerrariDG/async-ml-inference?style=flat&color=blueviolet" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/FerrariDG/async-ml-inference?style=flat&color=blueviolet" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Pydantic-E92063.svg?style=flat&logo=Pydantic&logoColor=white" alt="Pydantic">
	<img src="https://img.shields.io/badge/Redis-DC382D.svg?style=flat&logo=Redis&logoColor=white" alt="Redis">
	<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat&logo=YAML&logoColor=white" alt="YAML">
	<img src="https://img.shields.io/badge/Celery-37814A.svg?style=flat&logo=Celery&logoColor=white" alt="Celery">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white" alt="Docker">
	<img src="https://img.shields.io/badge/Numba-00A3E0.svg?style=flat&logo=Numba&logoColor=white" alt="Numba">
	<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=flat&logo=FastAPI&logoColor=white" alt="FastAPI">
</p>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>

- [ Overview](#-overview)
- [ Features](#-features)
- [ Repository Structure](#-repository-structure)
- [ Modules](#-modules)
- [ Getting Started](#-getting-started)
  - [ Install](#-install)
  - [ Using async-ml-inference](#-using-async-ml-inference)
  - [ Tests](#-tests)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)
</details>
<hr>

##  Overview

The async-ml-inference project offers a comprehensive solution for asynchronous machine learning inference operations. Through a Dockerized environment, it orchestrates services for API, backend, audio, and Euro tasks using Celery, FastAPI, and related technologies. The project's core functionalities include handling audio length extraction, Euro millions results scraping, and managing ML model inference tasks efficiently. By structuring tasks as background processes, the project optimizes performance and scalability while ensuring real-time monitoring and result handling capabilities. Overall, async-ml-inference simplifies asynchronous ML inference workflows, streamlining the deployment and execution of complex machine learning tasks.

---

##  Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | Asynchronous ML inference system with separate components for API, workers, and client. Utilizes FastAPI, Celery, Redis, RabbitMQ for task handling. Dockerized environment for services like audio processing and Euro scraping. Scalable and efficient architecture. |
| 🔩 | **Code Quality**  | Well-structured codebase with adherence to PEP 8 guidelines. Utilizes tools like flake8, mypy, and pydocstyle for linting and typing. Consistent naming conventions and clear documentation within the code. |
| 📄 | **Documentation** | Extensive documentation with detailed explanations of components, dependencies, and configuration. README, inline comments, and docstrings are present. Helps developers understand the project quickly. |
| 🔌 | **Integrations**  | Integrates with external dependencies like BeautifulSoup, librosa, and numba for specific tasks. Uses Docker Compose for managing service connections and configurations. Relies on external data sources for Euro scraping. |
| 🧩 | **Modularity**    | Highly modular design with separate components for API, workers, and client. Each component is self-contained and can be easily reused or extended. Encourages code encapsulation and separation of concerns. |
| 🧪 | **Testing**       | Testing frameworks include pytest for unit testing. Uses Pydantic for data validation. Tests cover functionality of API endpoints, worker tasks, and client interactions. Encourages test-driven development practices. |
| ⚡️  | **Performance**   | Efficient handling of asynchronous tasks with Celery and Redis. FastAPI ensures low latency for API requests. Parallel processing in the client for improved performance. Resource-friendly architecture for ML inference operations. |
| 🛡️ | **Security**      | Secure communication among services using Redis and RabbitMQ. Implements access control and authentication mechanisms for API endpoints. Follows secure coding practices to prevent vulnerabilities. |
| 📦 | **Dependencies**  | Key dependencies include FastAPI, Celery, Redis, RabbitMQ for task handling. Utilizes libraries like BeautifulSoup, librosa, and numba for specific functionalities. Manages dependencies via Pipfile and requirements files. |
| 🚀 | **Scalability**   | Designed for scalability with Celery for distributed task processing. Dockerized components allow easy scaling and deployment. Utilizes asynchronous processing for handling increased traffic and load. |

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

| File                                                                                                   | Summary                                                                                                                                                                                             |
| ---                                                                                                    | ---                                                                                                                                                                                                 |
| [docker-compose.yaml](https://github.com/FerrariDG/async-ml-inference/blob/master/docker-compose.yaml) | Compose services for broker, backend, audio, euro, api, and client components, setting up network connections and configurations within a Dockerized environment for async ML inference operations. |
| [Pipfile](https://github.com/FerrariDG/async-ml-inference/blob/master/Pipfile)                         | Pipfile ensures proper package management for the project, defining required packages and scripts for development and execution.                                                                    |

</details>

<details closed><summary>src.api</summary>

| File                                                                                                     | Summary                                                                                                                                                                                                   |
| ---                                                                                                      | ---                                                                                                                                                                                                       |
| [requirements.txt](https://github.com/FerrariDG/async-ml-inference/blob/master/src/api/requirements.txt) | Responsible for defining dependencies for the API services, including Celery, FastAPI, Uvicorn, and Pydantic within the async-ml-inference repository's architecture.                                     |
| [Dockerfile](https://github.com/FerrariDG/async-ml-inference/blob/master/src/api/Dockerfile)             | Enables deployment of API service using Python 3.7, installing dependencies, exposing ports, and running a Uvicorn server on port 5000.                                                                   |
| [api.py](https://github.com/FerrariDG/async-ml-inference/blob/master/src/api/api.py)                     | Handles asynchronous ML inference tasks using FastAPI, Celery, Redis, and RabbitMQ. Allows creation and monitoring of audio length and Euro results tasks. Background tasks for result handling included. |

</details>

<details closed><summary>src.workers</summary>

| File                                                                                                         | Summary                                                                                                                                                 |
| ---                                                                                                          | ---                                                                                                                                                     |
| [backend.py](https://github.com/FerrariDG/async-ml-inference/blob/master/src/workers/backend.py)             | Fetches Redis backend configuration parameters, constructs backend URL, and verifies Redis connection status based on given details.                    |
| [requirements.txt](https://github.com/FerrariDG/async-ml-inference/blob/master/src/workers/requirements.txt) | Asynchronous ML inference workers with Celery, leveraging libraries like BeautifulSoup, librosa, and numba for processing tasks.                        |
| [Dockerfile](https://github.com/FerrariDG/async-ml-inference/blob/master/src/workers/Dockerfile)             | Enables efficient setup of worker environment for async ML inference in the repository. Incorporates necessary dependencies and exposes required ports. |
| [broker.py](https://github.com/FerrariDG/async-ml-inference/blob/master/src/workers/broker.py)               | Manages connection to RabbitMQ broker, checks its status, and constructs the broker URL dynamically based on environmental variables.                   |

</details>

<details closed><summary>src.workers.audio</summary>

| File                                                                                                 | Summary                                                                                                                                                                                |
| ---                                                                                                  | ---                                                                                                                                                                                    |
| [worker.py](https://github.com/FerrariDG/async-ml-inference/blob/master/src/workers/audio/worker.py) | Celery worker for audio length extraction, ensuring backend and broker availability before task execution. Handles audio file loading and simulates task processing.                   |
| [config.py](https://github.com/FerrariDG/async-ml-inference/blob/master/src/workers/audio/config.py) | Configures Celery's Audio Length worker with task acknowledgements delayed until completion or failure, single task processing, dedicated queue, and result expiration after 48 hours. |

</details>

<details closed><summary>src.workers.euro</summary>

| File                                                                                                | Summary                                                                                                                                                      |
| ---                                                                                                 | ---                                                                                                                                                          |
| [worker.py](https://github.com/FerrariDG/async-ml-inference/blob/master/src/workers/euro/worker.py) | Celery worker for scraping Euromillions results using BeautifulSoup from a specified draw date URL, ensuring backend and broker connection before execution. |
| [config.py](https://github.com/FerrariDG/async-ml-inference/blob/master/src/workers/euro/config.py) | Configurations for Celery worker handling Euromillions Results with task acknowledgments, queue settings, result expiration of 48 hours.                     |

</details>

<details closed><summary>src.client</summary>

| File                                                                                                        | Summary                                                                                                                                                                               |
| ---                                                                                                         | ---                                                                                                                                                                                   |
| [requirements.txt](https://github.com/FerrariDG/async-ml-inference/blob/master/src/client/requirements.txt) | Handles client-side API requests, including retrying and joblib dependencies.                                                                                                         |
| [Dockerfile](https://github.com/FerrariDG/async-ml-inference/blob/master/src/client/Dockerfile)             | Client Dockerfile for async ML inference service to build and run Python client, handling communication with the ML model.                                                            |
| [client.py](https://github.com/FerrariDG/async-ml-inference/blob/master/src/client/client.py)               | Perform asynchronous ML inference by sending audio and date requests to an external API, handling task statuses and retrieving results, utilizing parallel processing for efficiency. |

</details>

---

##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Python**: `version x.y.z`

###  Install

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

###  Using `async-ml-inference`

Use the following command to run async-ml-inference:

```sh
python main.py
```

###  Tests

Use the following command to run tests:

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

- **[Report Issues](https://github.com/FerrariDG/async-ml-inference/issues)**: Submit bugs found or log feature requests for the `async-ml-inference` project.
- **[Submit Pull Requests](https://github.com/FerrariDG/async-ml-inference/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/FerrariDG/async-ml-inference/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
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
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/FerrariDG/async-ml-inference/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=FerrariDG/async-ml-inference">
   </a>
</p>
</details>

---

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-overview)

---
