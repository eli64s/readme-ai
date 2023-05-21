
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
async-ml-inference
</h1>
<h3 align="center">📍 Exploring ML Inference - Async Style!</h3>
<h3 align="center">🚀 Developed with the software and tools below.</h3>
<p align="center">

<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="flake8" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="" />
<img src="https://img.shields.io/badge/Redis-DC382D.svg?style=for-the-badge&logo=Redis&logoColor=white" alt="librosa" />
<img src="https://img.shields.io/badge/Celery-37814A.svg?style=for-the-badge&logo=Celery&logoColor=white" alt="requests" />
<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=for-the-badge&logo=FastAPI&logoColor=white" alt="markdown" />
<img src="https://img.shields.io/badge/Numba-00A3E0.svg?style=for-the-badge&logo=Numba&logoColor=white" alt="uvicorn" />
</p>

</div>

---

## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍Overview](#overview)
- [🔮 Feautres](#-feautres)
- [⚙️ Project Structure](#️-project-structure)
- [💻 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
  - [✅ Prerequisites](#-prerequisites)
  - [💻 Installation](#-installation)
  - [🤖 Using async-ml-inference](#-using-async-ml-inference)
  - [🧪 Running Tests](#-running-tests)
- [🛠 Future Development](#-future-development)
- [🤝 Contributing](#-contributing)
- [🪪 License](#-license)
- [🙏 Acknowledgments](#-acknowledgments)

---


## 📍Overview

Async-ml-inference is a library created by Microsoft that facilitates the deployment of lightweight Python models directly to existing servers or the cloud. This library provides an easy to use API that offers a range of data handling, batching and streaming capabilities from the cloud or any inference server.

## 🔮 Feautres

> `[📌  INSERT-PROJECT-FEATURES]`

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

| File   | Summary                                                                                                                                                                                                                                                                                                     | Module         |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|
| api.py | This code creates a FastAPI application that uses Celery to run tasks in the background. It sets up the connection strings for RabbitMQ and Redis, and defines two tasks,' length' and' results'. It also defines two endpoints,' /audio / length' and' /euro / results', which can be used to create tasks | src/api/api.py |

</details>

<details closed><summary>Audio</summary>

| File      | Summary                                                                                                                                                                                                                                                                         | Module                      |
|:----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------|
| worker.py | This code is a Celery worker for audio Length extraction. It uses the Celery library to connect to a broker and backend, and uses the librosa library to extract the audio length from a given audio URL. It also includes error handling and a simulated long task processing. | src/workers/audio/worker.py |
| config.py | This module contains Celery configurations for an Audio Length worker. It sets the worker to acknowledge tasks only when they are returned or fail, limits the worker to one task at a time, creates a queue for the worker, and sets the Redis key TTL to 48 hours.            | src/workers/audio/config.py |

</details>

<details closed><summary>Client</summary>

| File      | Summary                                                                                                                                                                                                                                                 | Module               |
|:----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------|
| client.py | This code sends audio URLs and dates to an API, and then retrieves the results of the tasks. It uses the Parallel library to send the tasks in parallel, and the Retry library to retry the tasks if they fail. The results are printed out in the end. | src/client/client.py |

</details>

<details closed><summary>Euro</summary>

| File      | Summary                                                                                                                                                                                                                                                                                          | Module                     |
|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------|
| worker.py | This code is a Celery worker for Euromillions results. It uses the BeautifulSoup library to scrape the results from the Euromillions website and returns the numbers and stars as a tuple. It also includes error handling to update the state and raise an Ignore exception if an error occurs. | src/workers/euro/worker.py |
| config.py | This module contains Celery configurations for a Euromillions Results worker. It sets task acknowledgements to be late, sets the worker prefetch multiplier to 1, and creates a queue called " euro ". It also sets the result expiration to 48 hours in seconds.                                | src/workers/euro/config.py |

</details>

<details closed><summary>Root</summary>

| File    | Summary                                                                                                                                                                                                                                                                | Module   |
|:--------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
| Pipfile | This code is a configuration file for a Python project. It contains the name and URL of the project, as well as the packages and scripts used. It includes packages such as BeautifulSoup4, Celery, FastAPI, Flower, Joblib, Librosa, Numba, Pydantic, Redis, Requests | Pipfile  |

</details>

<details closed><summary>Workers</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                                      | Module                 |
|:-----------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------|
| backend.py | This code imports the getenv function from the os module and imports the Redis and ConnectionError classes from the redis module. It then defines several functions to get the Redis password, port, database number, and host. The get_backend_url() function uses the other functions to create a URL string for the Redis | src/workers/backend.py |
| broker.py  | This code imports the getenv function from the os module, imports the Connection and OperationalError classes from the kombu module, and defines several functions to get the user, password, port, and virtual host of a RabbitMQ instance, as well as a function to check if the broker is running.                        | src/workers/broker.py  |

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
#run tests
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

[📌  INSERT-DESCRIPTION]


---
