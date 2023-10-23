<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>ASYNC-ML-INFERENCE</h1>
<h3>◦ Boost ML with Async Speed!</h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/scikitlearn-F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikitlearn" />
<img src="https://img.shields.io/badge/.ENV-ECD53F.svg?style=for-the-badge&logo=dotenv&logoColor=black" alt=".ENV" />
<img src="https://img.shields.io/badge/Redis-DC382D.svg?style=for-the-badge&logo=Redis&logoColor=white" alt="Redis" />
<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=for-the-badge&logo=YAML&logoColor=white" alt="YAML" />
<img src="https://img.shields.io/badge/Jinja-B41717.svg?style=for-the-badge&logo=Jinja&logoColor=white" alt="Jinja" />
<img src="https://img.shields.io/badge/SciPy-8CAAE6.svg?style=for-the-badge&logo=SciPy&logoColor=white" alt="SciPy" />

<img src="https://img.shields.io/badge/Celery-37814A.svg?style=for-the-badge&logo=Celery&logoColor=white" alt="Celery" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=for-the-badge&logo=Docker&logoColor=white" alt="Docker" />
<img src="https://img.shields.io/badge/NumPy-013243.svg?style=for-the-badge&logo=NumPy&logoColor=white" alt="NumPy" />
<img src="https://img.shields.io/badge/Numba-00A3E0.svg?style=for-the-badge&logo=Numba&logoColor=white" alt="Numba" />
<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=for-the-badge&logo=FastAPI&logoColor=white" alt="FastAPI" />
</p>
<img src="https://img.shields.io/github/license/FerrariDG/async-ml-inference?style=for-the-badge&color=5D6D7E" alt="GitHub license" />
<img src="https://img.shields.io/github/last-commit/FerrariDG/async-ml-inference?style=for-the-badge&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/FerrariDG/async-ml-inference?style=for-the-badge&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/languages/top/FerrariDG/async-ml-inference?style=for-the-badge&color=5D6D7E" alt="GitHub top language" />
</div>

---

## 📖 Table of Contents
- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 repository Structure](#-repository-structure)
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

The repository "async-ml-inference" is an ML inference project with async capabilities. It includes an API, client, and workers for audio and Euro tasks. The project uses Docker Compose to define and configure multiple services, such as RabbitMQ, Redis, and the API. The API receives requests to calculate the length of an audio file or retrieve Euro lottery results and assigns tasks to Celery workers. The workers perform the tasks asynchronously and provide endpoints to create tasks and retrieve their results. The project also includes Dockerfiles and scripts for running different components.

---

## 📦 Features

|    | Feature            | Description                                                                                                        |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The codebase follows a microservices architecture, with separate components for the API, client, and workers. It utilizes Docker containers to isolate and deploy each component. The components communicate with each other through a message broker (RabbitMQ) and a backend (Redis). This architecture enables scalability and fault tolerance. Limit your response to <= 65 words.             |
| 📄 | **Documentation**  | The codebase lacks comprehensive documentation. While some code files provide summaries of their purpose, there is no central documentation describing the overall functionality and instructions for setup or usage. Additional documentation would greatly improve the onboarding experience for developers and users. Limit your response to <= 65 words.|
| 🔗 | **Dependencies**   | The codebase relies on several external libraries for different functionalities, including FastAPI and Celery for the API, libsourcilla for audio processing, and BeautifulSoup for web scraping. Other dependencies include Docker and Python libraries such as requests and joblib. The code specifies these dependencies through the Pipenv and requirements.txt files. Limit your response to <= 65 words.|
| 🧩 | **Modularity**     | The codebase is organized into smaller, interchangeable components, namely the API, client, and workers. Each component has its own directory and Dockerfile, allowing for modularity and independent development. However, there are no explicit design patterns or architectural decisions in the codebase related to modularity. Limit your response to <= 65 words.|
| 🧪 | **Testing**        | The codebase does not include specific details or indications of testing strategies or tools. It would be beneficial to have unit tests for each component to ensure their individual functionality. The lack of testing information can make it difficult for developers to ensure code correctness and maintainability. Limit your response to <= 65 words.       |
| ⚡️  | **Performance**    | The performance of the system depends on the efficiency of each component. The asynchronous nature of FastAPI and Celery allows for parallel processing, improving response times. However, without specific performance benchmarks or optimization details, it is challenging to evaluate the system's overall performance. It would be beneficial to perform load testing and profiling to assess resource usage and identify potential bottlenecks. Limit your response to <= 65 words.|
| 🔐 | **Security**       | The codebase does not have explicit measures to protect data and maintain functionality. It lacks details regarding authentication, authorization, and secure data handling. Implementing secure communication protocols (e.g., TLS) and adding security measures such as input validation and authentication mechanisms would enhance the security of the system. Limit your response to <= 65 words.|
| 🔀 | **Version Control**| The codebase utilizes Git for version control, as evidenced by its presence on GitHub. However, the codebase does not provide details about specific version control strategies or tools used. It would be beneficial to include information about branching strategies, commit conventions, and code review processes to promote collaboration, reproducibility, and maintainability. Limit your response to <= 65 words.|
| 🔌 | **Integrations**   | The codebase interacts with other systems and services through the use of Docker containers, RabbitMQ as a message broker, and Redis as a backend.

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


## ⚙️ Modules

<details closed><summary>Root</summary>

| File                                                                                                 | Summary                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---                                                                                                  | ---                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [docker-compose.yaml](https://github.com/FerrariDG/async-ml-inference/blob/main/docker-compose.yaml) | The code sets up a Docker Compose file to define and configure a system with multiple services. It creates containers for a RabbitMQ broker, a Redis backend, an audio worker, a Euro conversion worker, an API, and a client. The containers are connected through a network. Each container has environment variables defining its dependencies and configurations. Ports are assigned for the API and the RabbitMQ management UI. |
| [Pipfile](https://github.com/FerrariDG/async-ml-inference/blob/main/Pipfile)                         | The code represents the directory structure and dependencies of an async ML inference project. It contains a Pipfile specifying various packages and their versions. The project includes a backend API, a client, and workers for audio and euro tasks. It also includes Dockerfiles for each component and scripts for running the broker, backend, flower, workers, API, and client.                                              |
| [.env](https://github.com/FerrariDG/async-ml-inference/blob/main/.env)                               | The given code represents the directory tree structure and a file named ".env" with the following content: "PYTHONPATH=.:src:src/workers". This code sets the Python path to include the current directory, "src", and "src/workers" directories, enabling the import of modules from these directories in Python code.                                                                                                              |
| [Pipfile.lock](https://github.com/FerrariDG/async-ml-inference/blob/main/Pipfile.lock)               | The code is a representation of the Pipfile.lock file, which contains information about the dependencies of the project. It specifies the versions and hashes of the packages required for the project. The code shows the versions and hashes for the "amqp" and "audioread" packages, which are dependencies for the project.                                                                                                      |

</details>

<details closed><summary>Api</summary>

| File                                                                                                   | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---                                                                                                    | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [requirements.txt](https://github.com/FerrariDG/async-ml-inference/blob/main/src/api/requirements.txt) | This code specifies the dependencies required for the API module of the async-ml-inference project. It includes the Celery library with Redis and librabbitmq as optional dependencies, FastAPI, Uvicorn, and Pydantic. These packages are necessary for running the API module and enable features such as asynchronous task handling, web framework, server, and data validation.                                                                                                                                 |
| [Dockerfile](https://github.com/FerrariDG/async-ml-inference/blob/main/src/api/Dockerfile)             | This Dockerfile sets up a container for the API component of an Async ML Inference application. It installs the necessary dependencies specified in `requirements.txt`, copies the `api.py` file to the container, and exposes ports 5000, 6379, and 5672. Finally, it runs the `uvicorn` command to start the API server on host 0.0.0.0 and port 5000.                                                                                                                                                            |
| [api.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/api/api.py)                     | This code defines an API using FastAPI for performing two tasks: calculating the length of an audio file and retrieving Euro lottery results. The API receives requests with audio URLs or Euro lottery draw dates and assigns tasks to a Celery worker. The worker calculates the length of the audio file or retrieves the Euro lottery results. The API provides endpoints to create these tasks and retrieve their results using task IDs. The code also includes functionality to send task results elsewhere. |

</details>

<details closed><summary>Workers</summary>

| File                                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---                                                                                                        | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [backend.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/backend.py)             | The code provides functions to get the Redis connection details and check if the Redis backend is running. The `get_redis_password()`, `get_redis_port()`, `get_redis_dbnum()`, and `get_redis_host()` functions retrieve the corresponding Redis connection parameters from environment variables or default values. The `get_backend_url()` function constructs the Redis connection URL based on the retrieved parameters. The `is_backend_running()` function attempts to connect to the Redis backend and returns a boolean indicating if the connection was successful. |
| [requirements.txt](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/requirements.txt) | The code in the `requirements.txt` file specifies the dependencies required for the workers module in an asynchronous machine learning inference project. It includes the following packages: BeautifulSoup version 4.9.0, Celery with the Redis broker version 4.4.0, librosa version 0.7.2, and numba version 0.48.0.                                                                                                                                                                                                                                                       |
| [Dockerfile](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/Dockerfile)             | This code is a Dockerfile that builds a Python 3.7 container image for the "workers" component in an ML inference application. It installs the necessary dependencies specified in requirements.txt, including libsndfile1 for audio processing. The code also exposes ports 6379 and 5672 for communication with other services.                                                                                                                                                                                                                                             |
| [broker.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/broker.py)               | The code in "broker.py" is responsible for connecting to a RabbitMQ instance and checking if it is running. It defines several helper functions to retrieve the necessary connection details from environment variables and constructs the broker URL using those details. Using the constructed URL, the code attempts to establish a connection to the RabbitMQ instance and ensure it is running. If successful, it returns True; otherwise, it returns False and prints an error message.                                                                                 |

</details>

<details closed><summary>Audio</summary>

| File                                                                                               | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---                                                                                                | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [worker.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/audio/worker.py) | The code is a Celery worker that calculates the length of an audio file. It retrieves the audio file from a given URL, loads it using the librosa library, and calculates its duration. The worker also simulates a long task processing by sleeping for a duration proportional to the audio length divided by 10. The result is returned as a dictionary with the key'audio_length'. The worker requires a running backend and broker to function properly. |
| [config.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/audio/config.py) | This code defines the Celery configurations for the Audio Length worker. It sets the worker to acknowledge tasks only when completed or failing, allows the worker to handle only one task at a time, creates a queue named "audio" for the worker, and specifies the expiration time for Redis keys as 48 hours.                                                                                                                                             |

</details>

<details closed><summary>Euro</summary>

| File                                                                                              | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---                                                                                               | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [worker.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/euro/worker.py) | The code represents a Celery worker for Euromillions results. It scrapes the results from a specified URL using BeautifulSoup. The worker checks if the backend and broker are running before connecting to them. It defines a task called `scrappy_result` that takes a draw date as input and returns a tuple of numbers and stars. If any errors occur during scraping or if the numbers and stars are not found on the page, the task raises an exception.                                                                                                                    |
| [config.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/euro/config.py) | The code in the "config.py" file is responsible for configuring the Celery worker that processes Euromillions Results. It sets the following configurations:-`task_acks_late = True`: The worker waits to acknowledge the task until after the task has been executed.-`worker_prefetch_multiplier = 1`: The worker retrieves 1 additional task for each task it is currently processing.-`task_queues = [Queue(name="euro")]`: The worker listens for tasks from the "euro" queue.-`result_expires = 60 * 60 * 48`: The results of the tasks expire after 48 hours (in seconds). |

</details>

<details closed><summary>Client</summary>

| File                                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---                                                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [requirements.txt](https://github.com/FerrariDG/async-ml-inference/blob/main/src/client/requirements.txt) | This code is a snippet of the requirements.txt file located at src/client/requirements.txt. It specifies the dependencies required for the client component of an async-ml-inference system. The required packages are requests 2.23.0, retrying 1.3.3, and joblib 0.14.1.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Dockerfile](https://github.com/FerrariDG/async-ml-inference/blob/main/src/client/Dockerfile)             | The code above is a Dockerfile used to build a client image for a Python application. It starts with a base image of python:3.7-slim-buster. It then copies the requirements.txt file to the /client/ directory, sets the working directory to /client/, and installs the necessary dependencies using pip.Next, it copies the client.py file to the /client/ directory.It exposes port 5000 and sets the command to run the client.py file using the python interpreter.                                                                                                                                                                                                                                        |
| [client.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/client/client.py)               | The code above is a Python script that performs parallel asynchronous ML inference tasks. It sends audio URLs and dates to an API endpoint for processing. The `make_post` function sends audio URLs to the `/audio/length` endpoint and the `make_date_post` function sends dates to the `/euro/results` endpoint. The script then retrieves the results using the `get_result` function, which makes a GET request to a task-specific endpoint. It retries the request up to 10 times with exponential waiting times if the status is pending. The results are printed to the console, showing the task ID, status, and output. The script utilizes parallel processing to improve performance and efficiency. |

</details>

---

## 🚀 Getting Started

***Dependencies***

Please ensure you have the following dependencies installed on your system:

`- ℹ️ Dependency 1`

`- ℹ️ Dependency 2`

`- ℹ️ ...`

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


## 🛣 Project Roadmap

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
