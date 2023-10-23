<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>ASYNC-ML-INFERENCE</h1>
<h3>◦ Faster ML, Smarter Results!</h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/scikitlearn-F7931E.svg?style=flat&logo=scikit-learn&logoColor=white" alt="scikitlearn" />
<img src="https://img.shields.io/badge/.ENV-ECD53F.svg?style=flat&logo=dotenv&logoColor=black" alt=".ENV" />
<img src="https://img.shields.io/badge/Redis-DC382D.svg?style=flat&logo=Redis&logoColor=white" alt="Redis" />
<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat&logo=YAML&logoColor=white" alt="YAML" />
<img src="https://img.shields.io/badge/Jinja-B41717.svg?style=flat&logo=Jinja&logoColor=white" alt="Jinja" />
<img src="https://img.shields.io/badge/SciPy-8CAAE6.svg?style=flat&logo=SciPy&logoColor=white" alt="SciPy" />

<img src="https://img.shields.io/badge/Celery-37814A.svg?style=flat&logo=Celery&logoColor=white" alt="Celery" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white" alt="Docker" />
<img src="https://img.shields.io/badge/NumPy-013243.svg?style=flat&logo=NumPy&logoColor=white" alt="NumPy" />
<img src="https://img.shields.io/badge/Numba-00A3E0.svg?style=flat&logo=Numba&logoColor=white" alt="Numba" />
<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=flat&logo=FastAPI&logoColor=white" alt="FastAPI" />
</p>
<img src="https://img.shields.io/github/license/FerrariDG/async-ml-inference?style=flat&color=5D6D7E" alt="GitHub license" />
<img src="https://img.shields.io/github/last-commit/FerrariDG/async-ml-inference?style=flat&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/FerrariDG/async-ml-inference?style=flat&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/languages/top/FerrariDG/async-ml-inference?style=flat&color=5D6D7E" alt="GitHub top language" />
</div>

---

## 📖 Table of Contents
- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [⚙️ Modules](#️-modules)
- [🚀 Getting Started](#-getting-started)
  - [🔧 Installation](#-installation)
  - [🤖 Running async-ml-inference](#-running-async-ml-inference)
  - [🧪 Tests](#-tests)
- [🛣 Project Roadmap](#-project-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The repository https://github.com/FerrariDG/async-ml-inference contains a project called readmeai. It is a Celery-based application that provides an API for creating and retrieving tasks related to audio length extraction and EuroMillions lottery results scraping. The project includes services such as a RabbitMQ message broker, a Redis backend, and workers for processing audio and EuroMillions tasks. It also includes an API service and a client service. The project aims to provide an efficient and scalable solution for performing these specific ML inference tasks asynchronously.

---

## 📦 Features

|    | Feature            | Description                                                                                                        |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The codebase follows a microservices architecture, with separate services for handling API requests, client requests, and workers for processing audio and euro tasks. The services are connected using Docker Compose and communicate through message brokers and backend systems.|
| 📄 | **Documentation**  | Limited information about the codebase is provided, and there is no dedicated documentation. It would be beneficial to have comprehensive documentation explaining the codebase's structure, architecture, and usage.|
| 🔗 | **Dependencies**   | The codebase relies on various external libraries and technologies, including Celery, RabbitMQ, Redis, FastAPI, and libraries such as BeautifulSoup4, Librosa, and NumPy. These dependencies provide functionality for task processing, web API development, data extraction, and more.|
| 🧩 | **Modularity**     | The codebase exhibits a good level of modularity with separate directories for API, client, and workers. Each component has its own Dockerfile and dependencies, allowing for flexibility and ease of maintenance. However, there could be more organization and separation within the workers directory.|
| 🧪 | **Testing**        | Limited information is provided about testing strategies and tools. It would be beneficial to have tests implemented for the different components, ensuring the stability and correctness of the code.|
| ⚡️  | **Performance**    | The codebase utilizes Celery and parallel processing to improve performance, allowing for efficient processing of audio and euro tasks. However, without specific performance benchmarks or metrics, it is challenging to evaluate the performance on speed, efficiency, and resource usage.|
| 🔐 | **Security**       | The codebase does not provide specific security measures, potentially leaving the system vulnerable to security attacks. It is crucial to implement appropriate security measures like input validation and authentication to protect data and maintain system functionality.|
| 🔀 | **Version Control**| No information is provided about the codebase's version control strategies and tools. It's recommended to use a version control system like Git to track changes, manage branches, and facilitate collaboration among team members.|
| 🔌 | **Integrations**   | The codebase integrates with external systems and services such as RabbitMQ and Redis for message brokering and backend storage, respectively. Integrations with libraries such as Celery and FastAPI enable task processing and API endpoint handling.|
| 📶 | **Scalability**    | The codebase's microservices architecture and usage of Celery allow for scalability by horizontally scaling the worker services based on demand. However, without further information about performance testing and specific scalability measures, it is challenging to assess the system's scalability capabilities.|

---


## 📂 Repository Structure

```sh
└── ./
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

| File                                                                                                 | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---                                                                                                  | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [docker-compose.yaml](https://github.com/FerrariDG/async-ml-inference/blob/main/docker-compose.yaml) | This code sets up a Docker-compose file that defines multiple services for a Celery-based application. The services include a RabbitMQ message broker, a Redis backend, workers for processing audio and euro tasks, an API service, and a client service. Each service has its own container with specific configurations and dependencies. The services are connected through a network, and the API service exposes port 5000 for communication with the client service. |
| [Pipfile](https://github.com/FerrariDG/async-ml-inference/blob/main/Pipfile)                         | This code represents the directory structure and dependencies for a project called readmeai. It includes a Pipfile that lists the packages required for the project, including libraries like BeautifulSoup4, Celery, FastAPI, and Redis. It also includes scripts for setting up a RabbitMQ broker, Redis backend, and running various workers and API/client components.                                                                                                  |
| [.env](https://github.com/FerrariDG/async-ml-inference/blob/main/.env)                               | The code sets the PYTHONPATH environment variable to include the current directory and the src directory, including the src/workers directory.                                                                                                                                                                                                                                                                                                                              |
| [Pipfile.lock](https://github.com/FerrariDG/async-ml-inference/blob/main/Pipfile.lock)               | The code represents the lock file for a Python project's dependencies. It contains the specific versions and checksums for packages such as amqp, audioread, and beautifulsoup4. This file ensures that the project will use consistent and compatible package versions, meeting its requirements.                                                                                                                                                                          |

</details>

<details closed><summary>Api</summary>

| File                                                                                                   | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---                                                                                                    | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [requirements.txt](https://github.com/FerrariDG/async-ml-inference/blob/main/src/api/requirements.txt) | The code in the given path (`src/api/requirements.txt`) specifies the dependencies required for the API module. It includes `celery` with Redis and librabbitmq plugins (version 4.4.0), `fastapi` (version 0.65.2), `uvicorn` (version 0.11.7), and `pydantic` (version 1.6.2). These dependencies are crucial for the proper functioning of the API module.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Dockerfile](https://github.com/FerrariDG/async-ml-inference/blob/main/src/api/Dockerfile)             | This code is a Dockerfile that defines the environment and runtime configuration for an API service. It sets up a Python 3.7 environment, installs the required dependencies specified in requirements.txt, and copies the API code into the container. The container exposes ports 5000, 6379, and 5672, and the API service is started using the uvicorn server with the specified API module and host/port configuration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [api.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/api/api.py)                     | The code above represents a FastAPI application that exposes several endpoints for creating and retrieving Celery tasks. The application uses RabbitMQ as a message broker and Redis as a backend for task results.The code defines two endpoint functions: `create_audio_task` and `create_euro_task`. These functions receive POST requests with specific data structures (`UrlItem` and `EuroDate`), create Celery tasks with corresponding parameters, and optionally add a background task to send the task result to a specified callback URL.The code also defines a `get_task_result` endpoint function that receives a GET request with a task ID, retrieves the task result from Celery, and returns it as a JSON response.The code utilizes the `Celery` class for creating a Celery instance and the `FastAPI` class for creating a FastAPI application. It also imports several modules and classes for handling request/response objects, task states, and data models. |

</details>

<details closed><summary>Workers</summary>

| File                                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---                                                                                                        | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [backend.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/backend.py)             | The code defines functions to retrieve configuration details for connecting to a Redis database and to check if the backend is running. It uses the `getenv` function to retrieve environment variables for the Redis host, port, password, and database number. The `get_backend_url` function constructs the URL for connecting to the Redis database. The `is_backend_running` function attempts to connect to the Redis database and returns a boolean value indicating if the connection was successful.                                                                                                                      |
| [requirements.txt](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/requirements.txt) | The code contains a requirements.txt file which specifies the dependencies for a worker component in a directory structure. The worker component requires the following dependencies: beautifulsoup4 version 4.9.0, celery with the redis backend version 4.4.0, librosa version 0.7.2, and numba version 0.48.0. These dependencies are needed for the worker to perform its tasks effectively.                                                                                                                                                                                                                                   |
| [Dockerfile](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/Dockerfile)             | This Dockerfile sets up a Python 3.7 environment based on the slim-buster image. It installs the libsndfile1 library, upgrades pip, and installs the requirements specified in requirements.txt. It then copies the current directory into the /workers directory in the Docker image. Finally, it exposes ports 6379 and 5672 for networking purposes.                                                                                                                                                                                                                                                                            |
| [broker.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/broker.py)               | This code defines functions to get the RabbitMQ credentials and broker URL, and checks if the RabbitMQ broker is running. The `get_rabbitmq_userpass()`, `get_rabbitmq_port()`, `get_rabbitmq_vhost()`, and `get_rabbitmq_host()` functions retrieve the RabbitMQ username, password, port, and host respectively from environment variables. The `get_broker_url()` function combines these values to construct the broker URL. The `is_broker_running()` function attempts to establish a connection with RabbitMQ and returns `True` if the connection is successful, otherwise it prints an error message and returns `False`. |

</details>

<details closed><summary>Audio</summary>

| File                                                                                               | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ---                                                                                                | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [worker.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/audio/worker.py) | This code defines a Celery worker for extracting the length of an audio file. The worker is responsible for downloading the file from a given URL, loading it using the librosa library, and calculating its duration. The worker checks if the backend and broker services are running before executing the task. If any exceptions occur during the process, the worker updates its state with relevant information and raises an Ignore exception. Finally, the worker returns the calculated audio length. |
| [config.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/audio/config.py) | This code defines the Celery configurations for the Audio Length worker. It sets the worker to acknowledge the task only when it returns or fails, ensures that the worker only handles one task at a time, creates a queue named "audio" for the worker, and sets the Redis key expiration time to 48 hours.                                                                                                                                                                                                  |

</details>

<details closed><summary>Euro</summary>

| File                                                                                              | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---                                                                                               | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [worker.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/euro/worker.py) | This code is a Celery worker that scrapes the Euromillions results from a website. It checks if the backend and broker services are running, then defines a Celery task called "euro.scrappy_result" that takes a draw date as input. The task scrapes the Euromillions results web page for the given draw date, extracting the numbers and stars drawn. If successful, it returns a tuple containing the numbers and stars. If any errors occur during scraping, appropriate exception handling and state updates are performed. |
| [config.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/euro/config.py) | This code configures a Celery worker for the Euromillions Results task. It sets the worker's prefetch multiplier to 1 and enables late task acknowledgments. The worker is configured to listen to a queue named "euro". Task results are set to expire after 48 hours.                                                                                                                                                                                                                                                            |

</details>

<details closed><summary>Client</summary>

| File                                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---                                                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                                                     |
| [requirements.txt](https://github.com/FerrariDG/async-ml-inference/blob/main/src/client/requirements.txt) | The code is a `requirements.txt` file located in the `src/client` directory. It specifies the dependencies required for the client module of a project. The dependencies listed are `requests==2.23.0`, `retrying==1.3.3`, and `joblib==0.14.1`. These dependencies are essential for the functionality and proper operation of the client module.                                                      |
| [Dockerfile](https://github.com/FerrariDG/async-ml-inference/blob/main/src/client/Dockerfile)             | The code is a Dockerfile that sets up a Python 3.7 slim-buster image with the client.py script. It copies the requirements.txt file to the /client directory, installs the required dependencies, and then copies the client.py script to the /client directory. Finally, it exposes port 5000 and runs the client.py script when the container is started.                                             |
| [client.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/client/client.py)               | This code retrieves audio lengths and euro lottery draw results using parallel processing. It sends audio URLs and dates to the specified API endpoints, gets task IDs in response, and then retrieves the results using the task IDs. The results contain either the audio length or the euro lottery results. The code utilizes threading to perform these tasks in parallel for improved efficiency. |

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

[**Discussions**](https://github.com/FerrariDG/async-ml-inference/discussions)
  - Join the discussion here.

[**New Issue**](https://github.com/FerrariDG/async-ml-inference/issues)
  - Report a bug or request a feature here.

[**Contributing Guidelines**](https://github.com/FerrariDG/async-ml-inference/blob/main/CONTRIBUTING.md)

- Contributions are welcome! Please follow these steps:

1. Fork the project repository to your GitHub account.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive such as `new-feature-x` or `bugfix-issue-x`.
```sh
git checkout -b new-feature-x
```
4. Develop your changes locally.
5. Commit your updates with a clear explanation of the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub.
```sh
git push origin new-feature-x
```
7. Create a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
8. Once your pull request is reviewed, it will be merged into the main branch of the project repository.

---

## 📄 License


This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 👏 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#Top)

---
