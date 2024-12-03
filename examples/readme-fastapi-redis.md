<p align="center">
  <img src="https://img.icons8.com/external-tal-revivo-filled-tal-revivo/96/external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-filled-tal-revivo.png" width="20%" />
</p>
<p align="center">
    <h1 align="center">ASYNC-ML-INFERENCE</h1>
</p>
<p align="center">
    <em>Empowering ML with Async Magic!</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/FerrariDG/async-ml-inference?style=flat-square&logo=opensourceinitiative&logoColor=white&color=009688" alt="license">
	<img src="https://img.shields.io/github/last-commit/FerrariDG/async-ml-inference?style=flat-square&logo=git&logoColor=white&color=009688" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/FerrariDG/async-ml-inference?style=flat-square&color=009688" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/FerrariDG/async-ml-inference?style=flat-square&color=009688" alt="repo-language-count">
</p>
<p align="center">
		<em>Tech Stack</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Redis-DC382D.svg?style=flat-square&logo=Redis&logoColor=white" alt="Redis">
	<img src="https://img.shields.io/badge/Celery-37814A.svg?style=flat-square&logo=Celery&logoColor=white" alt="Celery">
	<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=flat-square&logo=FastAPI&logoColor=white" alt="FastAPI">
	<img src="https://img.shields.io/badge/Numba-00A3E0.svg?style=flat-square&logo=Numba&logoColor=white" alt="Numba">
	<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat-square&logo=Docker&logoColor=white" alt="Docker">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/Pydantic-E92063.svg?style=flat-square&logo=Pydantic&logoColor=white" alt="Pydantic">
</p>
<br>

##  Table of Contents

1. [ Overview](#overview)
2. [ Features](#features)
3. [ Project Structure](#project-structure)
  3.1. [ Project Index](#project-index)
4. [ Getting Started](#getting-started)
  4.1. [ Prerequisites](#prerequisites)
  4.2. [ Installation](#installation)
  4.3. [ Usage](#-usage)
  4.4. [ Tests](#-tests)
5. [ Roadmap](#roadmap)
6. [ Contributing](#-contributing)
7. [ License](#license)
8. [ Acknowledgments](#acknowledgments)

---

##  Overview

async-ml-inference orchestrates distributed tasks for audio processing and Euro results retrieval. It streamlines asynchronous processing, enhancing efficiency and scalability. Ideal for developers seeking seamless task management in machine learning applications.

---

##  Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Orchestrates Docker services using `docker-compose.yaml` for a Celery-based distributed system.</li><li>Utilizes RabbitMQ and Redis containers for task queuing and backend storage.</li><li>Spins up Celery workers for audio and euro tasks, along with an API service and a client for interaction.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Defines FastAPI endpoints in `src/api/api.py` for creating and retrieving audio and Euro task results.</li><li>Implements Celery workers in `src/workers/audio/worker.py` and `src/workers/euro/worker.py` for efficient task processing.</li><li>Utilizes `flake8` for code linting and `pydocstyle` for docstring checking.</li></ul> |
| 📄 | **Documentation** | <ul><li>Primary language: Python</li><li>Package managers: `pipenv` and `pip`</li><li>Contains detailed documentation in various file formats like `.yaml`, `.lock`, `.txt`, and `.py`.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integrates with Redis and RabbitMQ for backend and broker connections.</li><li>Utilizes `requests` for making HTTP requests and `joblib` for parallel processing in the client module.</li><li>Uses `Celery` for asynchronous task execution.</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Separates concerns into API, workers, and client modules for clear functionality.</li><li>Configures Celery settings in separate files like `config.py` for Audio Length and Euromillions workers.</li><li>Ensures dependencies are managed separately for each module using `requirements.txt` files.</li></ul> |
| 🧪 | **Testing**       | <ul><li>Tests the project using `pytest` with commands provided for both `pipenv` and `pip` installations.</li><li>Includes unit tests for API endpoints, worker functions, and client interactions.</li><li>Ensures code quality with testing and linting tools like `mypy` and `pycodestyle`.</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Optimizes task processing efficiency by configuring Celery settings in `config.py` files.</li><li>Utilizes parallel processing in the client module for enhanced performance.</li><li>Calculates audio length efficiently using librosa in the audio worker.</li></ul> |
| 🛡️ | **Security**      | <ul><li>Secures backend and broker connections using environment variables and connection validation.</li><li>Ensures secure communication between components within the distributed system.</li><li>Follows best practices for handling sensitive data and user inputs.</li></ul> |

---

##  Project Structure

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

###  Project Index

<details open>
	<summary><b><code>Async-ml-inference Index</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/FerrariDG/async-ml-inference/blob/master/docker-compose.yaml'>docker-compose.yaml</a></b></td>
				<td>- Orchestrates Docker services for a Celery-based distributed system<br>- Manages RabbitMQ and Redis containers for task queuing and backend storage<br>- Spins up Celery workers for audio and euro tasks, along with an API service and a client for interaction<br>- Establishes network connections for seamless communication between components.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/FerrariDG/async-ml-inference/blob/master/Pipfile'>Pipfile</a></b></td>
				<td>Define project dependencies and scripts for development and deployment using the Pipfile.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- src Submodule -->
		<summary><b>src</b></summary>
		<blockquote>
			<details>
				<summary><b>api</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/FerrariDG/async-ml-inference/blob/master/src/api/requirements.txt'>requirements.txt</a></b></td>
						<td>- Facilitates dependency management for the project's API by specifying required packages and versions in the 'requirements.txt' file located at 'src/api/'<br>- This file ensures that the necessary libraries like Celery, FastAPI, uvicorn, and pydantic are installed to support the API functionality within the project architecture.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/FerrariDG/async-ml-inference/blob/master/src/api/Dockerfile'>Dockerfile</a></b></td>
						<td>- Facilitates containerized deployment of the API service by defining necessary dependencies and configurations<br>- Sets up a Python environment, installs required packages, exposes specified ports, and launches the API service using Uvicorn<br>- Streamlines the deployment process within the project architecture.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/FerrariDG/async-ml-inference/blob/master/src/api/api.py'>api.py</a></b></td>
						<td>- Defines FastAPI endpoints for creating and retrieving audio and Euro task results using Celery for asynchronous processing<br>- Handles task creation, status retrieval, and result sending<br>- Utilizes Redis and RabbitMQ for backend and broker connections<br>- Implements background tasks for result notifications.</td>
					</tr>
					</table>
				</blockquote>
			</details>
			<details>
				<summary><b>workers</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/FerrariDG/async-ml-inference/blob/master/src/workers/backend.py'>backend.py</a></b></td>
						<td>- Defines functions to retrieve Redis connection details and check if the backend is running<br>- The code constructs a Redis URL based on environment variables and attempts a connection to the Redis instance<br>- If successful, it confirms the backend is operational; otherwise, it logs an error.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/FerrariDG/async-ml-inference/blob/master/src/workers/requirements.txt'>requirements.txt</a></b></td>
						<td>- Manages project dependencies for the workers module, ensuring the required libraries are available for seamless execution<br>- This file specifies the versions of libraries like BeautifulSoup, Celery, librosa, and numba needed by the workers to perform tasks efficiently within the project architecture.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/FerrariDG/async-ml-inference/blob/master/src/workers/Dockerfile'>Dockerfile</a></b></td>
						<td>Builds a Docker image for worker processes, installing dependencies and exposing necessary ports.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/FerrariDG/async-ml-inference/blob/master/src/workers/broker.py'>broker.py</a></b></td>
						<td>- Defines functions to retrieve RabbitMQ connection details and check if the broker is running<br>- The code constructs a broker URL using environment variables and attempts to connect to RabbitMQ with retries<br>- If successful, it confirms the broker is running; otherwise, it logs an error.</td>
					</tr>
					</table>
					<details>
						<summary><b>audio</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/FerrariDG/async-ml-inference/blob/master/src/workers/audio/worker.py'>worker.py</a></b></td>
								<td>- Implements a Celery worker for extracting audio length<br>- Validates backend and broker connections before processing audio URL<br>- Downloads audio data, calculates duration using librosa, and simulates task processing time<br>- Handles exceptions and returns the audio length upon completion.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/FerrariDG/async-ml-inference/blob/master/src/workers/audio/config.py'>config.py</a></b></td>
								<td>Configure Celery settings for the Audio Length worker to optimize task processing efficiency and ensure reliable task handling within the project architecture.</td>
							</tr>
							</table>
						</blockquote>
					</details>
					<details>
						<summary><b>euro</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/FerrariDG/async-ml-inference/blob/master/src/workers/euro/worker.py'>worker.py</a></b></td>
								<td>- The code file in src/workers/euro/worker.py serves as a Celery worker for fetching Euromillions results<br>- It ensures the backend and broker services are running before scraping the results from a specified URL<br>- The worker extracts numbers and stars from the webpage based on the draw date provided, returning them as a tuple.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/FerrariDG/async-ml-inference/blob/master/src/workers/euro/config.py'>config.py</a></b></td>
								<td>- Configure Celery settings for the Euromillions Results worker, including task acknowledgements, prefetch multiplier, task queues, and result expiration time<br>- This module centralizes the configurations necessary for efficient task processing within the project's architecture.</td>
							</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<details>
				<summary><b>client</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/FerrariDG/async-ml-inference/blob/master/src/client/requirements.txt'>requirements.txt</a></b></td>
						<td>Manage external dependencies for the client-side application using the specified versions of requests, retrying, and joblib.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/FerrariDG/async-ml-inference/blob/master/src/client/Dockerfile'>Dockerfile</a></b></td>
						<td>Builds a lightweight Python container for the client module, installing dependencies and exposing port 5000.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/FerrariDG/async-ml-inference/blob/master/src/client/client.py'>client.py</a></b></td>
						<td>- Generates audio and date tasks, sends them to the API, retrieves results, and displays successful outputs<br>- Utilizes parallel processing for efficiency<br>- Key functionalities include posting audio URLs and dates, checking task statuses, and handling retries<br>- The script orchestrates the entire process seamlessly, enhancing performance through parallel execution.</td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---

##  Getting Started

###  Prerequisites

Before getting started with async-ml-inference, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pipenv, Pip
- **Container Runtime:** Docker


###  Installation

Install async-ml-inference using one of the following methods:

**Build from source:**

1. Clone the async-ml-inference repository:
```sh
❯ git clone https://github.com/FerrariDG/async-ml-inference
```

2. Navigate to the project directory:
```sh
❯ cd async-ml-inference
```

3. Install the project dependencies:


**Using `pipenv`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pipenv-3775A9.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pipenv.pypa.io/)

```sh
❯ pipenv install
```


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r src/api/requirements.txt, src/workers/requirements.txt, src/client/requirements.txt
```


**Using `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker build -t FerrariDG/async-ml-inference .
```




###  Usage

Run async-ml-inference using the following command:

**Using `pipenv`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pipenv-3775A9.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pipenv.pypa.io/)

```sh
❯ pipenv shell
❯ pipenv run python {entrypoint}
```


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```


**Using `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker run -it {image_name}
```



###  Testing

Run the test suite using the following command:

**Using `pipenv`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pipenv-3775A9.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pipenv.pypa.io/)

```sh
❯ pipenv shell
❯ pipenv run pytest
```


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```



##  Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

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

---
