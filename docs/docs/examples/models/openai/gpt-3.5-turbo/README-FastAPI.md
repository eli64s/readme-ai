<div id="top">

<!-- HEADER STYLE: BANNER -->
<div align="center">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 100">
	<defs>
		<linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
			<stop offset="0%" style="stop-color:#c9e52d;stop-opacity:1" />
			<stop offset="50%" style="stop-color:#5be52d;stop-opacity:1" />
			<stop offset="100%" style="stop-color:#2de56e;stop-opacity:1" />
		</linearGradient>
		<filter id="shadow">
			<feDropShadow dx="2.5" dy="2.5" stdDeviation="10" flood-opacity="0.5" />
		</filter>
		<pattern id="dots" width="20" height="20" patternUnits="userSpaceOnUse">
			<circle cx="3" cy="3" r="1.5" fill="rgba(255,255,255,0.1)" />
		</pattern>
	</defs>
	<rect width="100%" height="100%" fill="url(#bg)" rx="10" />
	<rect width="100%" height="100%" fill="url(#dots)" />
	<circle cx="16.0" cy="25.0" r="15.0" fill="rgba(255,255,255,0.2)" />
	<circle cx="184.0" cy="75.0" r="20.0" fill="rgba(255,255,255,0.2)" />
	<path d="M 100.0 12.5
             L 125.0 37.5
             L 75.0 37.5 Z" fill="rgba(255,255,255,0.2)" />
	<text x="100.0" y="50.0" font-family="Arial, sans-serif" font-size="24" font-weight="bold" text-anchor="middle" fill="#ffffff" filter="url(#shadow)">
		ML-INFERENCE
	</text>
	<text x="100.0" y="75.0" font-family="Arial, sans-serif" font-size="8" text-anchor="middle" fill="rgba(255,255,255,0.9)">
Harvesting ML insights with async precision and speed.</text></svg>

<!-- BADGES -->
<img src="https://img.shields.io/github/license/FerrariDG/async-ml-inference?style=plastic&logo=opensourceinitiative&logoColor=white&color=43a047" alt="license">
<img src="https://img.shields.io/github/last-commit/FerrariDG/async-ml-inference?style=plastic&logo=git&logoColor=white&color=43a047" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/FerrariDG/async-ml-inference?style=plastic&color=43a047" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/FerrariDG/async-ml-inference?style=plastic&color=43a047" alt="repo-language-count">

<em>Technology Stack:</em>

<img src="https://img.shields.io/badge/Redis-DC382D.svg?style=plastic&logo=Redis&logoColor=white" alt="Redis">
<img src="https://img.shields.io/badge/Celery-37814A.svg?style=plastic&logo=Celery&logoColor=white" alt="Celery">
<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=plastic&logo=FastAPI&logoColor=white" alt="FastAPI">
<img src="https://img.shields.io/badge/Numba-00A3E0.svg?style=plastic&logo=Numba&logoColor=white" alt="Numba">
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=plastic&logo=Docker&logoColor=white" alt="Docker">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=plastic&logo=Python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Pydantic-E92063.svg?style=plastic&logo=Pydantic&logoColor=white" alt="Pydantic">
<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=plastic&logo=YAML&logoColor=white" alt="YAML">

</div>
<br>

---

## 📜 Table of Contents

- [📜 Table of Contents](#-table-of-contents)
- [📖 Overview](#-overview)
- [🖋️ Features](#-features)
- [📚 Project Structure](#-project-structure)
    - [📜 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
    - [🔖 Prerequisites](#-prerequisites)
    - [🛠️ Installation](#-installation)
    - [📺 Usage](#-usage)
    - [🧪 Testing](#-testing)
- [🎞️ Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)
- [🎩 Acknowledgments](#-acknowledgments)

---

## 📖 Overview

Introducing async-ml-inference, a comprehensive tool tailored for managing asynchronous machine learning inference tasks efficiently.

**Why async-ml-inference?**

This project revolutionizes asynchronous task processing by offering:
- **🚀 Orchestrate Celery Tasks:** Execute tasks asynchronously for optimal performance.
- **🔧 Streamlined Environment Setup:** Simplify project setup and management with Pipfile.
- **💻 FastAPI Integration:** Create efficient API endpoints and client interactions effortlessly.
- **🐳 Dockerized Deployment:** Ensure consistent deployment across services with Dockerfile configurations.

---

## 🖋️ Features

|       | Component         | Details                                          |
| :---  | :---------------- | :----------------------------------------------- |
| ⚙️   | **Architecture**  | <ul><li>Async ML inference using FastAPI & Celery</li><li>Uses Redis as broker for asynchronous processing</li><li>Separation of concerns between API, workers, and client components</li></ul> |
| 🔩  | **Code Quality**    | <ul><li>Consistent code styling enforced with Flake8 & Pycodestyle</li><li>Type checking with MyPy to catch potential errors</li><li>Packages are imported within specific modules only, promoting encapsulation</li></ul> |
| 📄  | **Documentation**   | <ul><li>Detailed Docker setup with multiple Dockerfiles</li><li>API endpoints documented with Pydantic models</li><li>Codebase includes README, comments, and docstrings</li></ul> |
| 🔌   | **Integrations**   | <ul><li>Integration with FastAPI for creating RESTful APIs</li><li>Celery integration for task queuing and processing</li><li>Redis integration as a message broker</li></ul> |
| 🧩  | **Modularity**     | <ul><li>Modular structure with separate components for API, workers, and client</li><li>Each component has its own requirements.txt file for easy management</li><li>Encapsulated functions for specific tasks</li></ul> |
| 🧪   | **Testing**        | <ul><li>Testing modules for API endpoints with Pytest</li><li>Worker functions tested for expected behavior</li><li>Unit tests cover key functionalities</li></ul> |
| ⚡️   | **Performance**    | <ul><li>Numba library used for optimizing performance in numerical computations</li><li>Async processing with Celery enhances scalability and responsiveness</li><li>Librosa for audio processing efficiency</li></ul> |
| 🛡️  | **Security**       | <ul><li>Secure incoming requests with Pydantic validation</li><li>API endpoints sanitized using input validation</li><li>Use of auth tokens for authentication and authorization</li></ul> |
| 📦  | **Dependencies**   | <ul><li>Packages managed with Pipenv & Pip for version control</li><li>Docker-based setup simplifies dependency management</li><li>Requirements.txt files for individual components specify dependencies</li></ul> |

---

## 📚 Project Structure

```sh
└── async-ml-inference/
    ├── Pipfile
    ├── Pipfile.lock
    ├── README.md
    ├── docker-compose.yaml
    ├── docs
    │   └── diagram
    │       ├── architecture.png
    │       └── diagram.py
    ├── src
    │   ├── api
    │   │   ├── Dockerfile
    │   │   ├── api.py
    │   │   └── requirements.txt
    │   ├── client
    │   │   ├── Dockerfile
    │   │   ├── client.py
    │   │   └── requirements.txt
    │   └── workers
    │       ├── Dockerfile
    │       ├── audio
    │       │   ├── config.py
    │       │   └── worker.py
    │       ├── backend.py
    │       ├── broker.py
    │       ├── euro
    │       │   ├── config.py
    │       │   └── worker.py
    │       └── requirements.txt
    └── tests
        └── README.md
```

### 📜 Project Index

<details open>
	<summary><b><code>ASYNC-ML-INFERENCE/</code></b></summary>
	<!-- __root__ Submodule -->
	<details>
		<summary><b>__root__</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ __root__</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/FerrariDG/async-ml-inference/blob/master/docker-compose.yaml'>docker-compose.yaml</a></b></td>
					<td style='padding: 8px;'>Define the services configurations in the docker-compose.yaml file for running Celery tasks with RabbitMQ and Redis.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/FerrariDG/async-ml-inference/blob/master/Pipfile'>Pipfile</a></b></td>
					<td style='padding: 8px;'>- Detailing dependencies and scripts for the projects environment setup and management, the Pipfile streamlines package installation and project execution<br>- It defines packages including Beautiful Soup, FastAPI, and Celery, along with tooling like Flake8 and MyPy<br>- Script definitions for running Celery workers, API endpoints, and client interactions are also specified for operational clarity.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- src Submodule -->
	<details>
		<summary><b>src</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ src</b></code>
			<!-- api Submodule -->
			<details>
				<summary><b>api</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ src.api</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/FerrariDG/async-ml-inference/blob/master/src/api/requirements.txt'>requirements.txt</a></b></td>
							<td style='padding: 8px;'>Ensure asynchronous web framework and task queue compatibility with listed requirements.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/FerrariDG/async-ml-inference/blob/master/src/api/Dockerfile'>Dockerfile</a></b></td>
							<td style='padding: 8px;'>Define Dockerfile in src/api for Python 3.7, sets up API dependencies, exposes ports, and launches the API using uvicorn.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/FerrariDG/async-ml-inference/blob/master/src/api/api.py'>api.py</a></b></td>
							<td style='padding: 8px;'>- Define FastAPI routes for audio processing tasks with Celery for async execution<br>- Utilizes Redis and RabbitMQ as backend and broker, respectively<br>- Tasks include fetching audio length and Euro results, with async result retrieval for status updates<br>- Task details passed via POST requests, with callback option for result notification<br>- Allows querying task status via task ID.</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- workers Submodule -->
			<details>
				<summary><b>workers</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ src.workers</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/FerrariDG/async-ml-inference/blob/master/src/workers/backend.py'>backend.py</a></b></td>
							<td style='padding: 8px;'>Expose functions for retrieving Redis connection information and checking backend status, crucial for maintaining connectivity in the project architecture.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/FerrariDG/async-ml-inference/blob/master/src/workers/requirements.txt'>requirements.txt</a></b></td>
							<td style='padding: 8px;'>Analyze and manage project dependencies utilizing specified versions.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/FerrariDG/async-ml-inference/blob/master/src/workers/Dockerfile'>Dockerfile</a></b></td>
							<td style='padding: 8px;'>- Creates a streamlined Docker image in the workers directory, optimizing the environment for the Python application to run smoothly<br>- Handles dependencies, sets the working directory, and exposes necessary ports for communication, enhancing the project's deployment infrastructure.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/FerrariDG/async-ml-inference/blob/master/src/workers/broker.py'>broker.py</a></b></td>
							<td style='padding: 8px;'>- Enable checking RabbitMQ connection status and constructing the broker URL by retrieving environment variables<br>- The code in <code>src/workers/broker.py</code> focuses on managing RabbitMQ credentials and connection settings dynamically<br>- It offers functions to determine if the broker is running and to generate the appropriate broker URL for establishing connections.</td>
						</tr>
					</table>
					<!-- audio Submodule -->
					<details>
						<summary><b>audio</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ src.workers.audio</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/FerrariDG/async-ml-inference/blob/master/src/workers/audio/worker.py'>worker.py</a></b></td>
									<td style='padding: 8px;'>- Generates audio length by extracting and processing the duration of audio files<br>- Handles exceptions and simulates processing time based on the audio length<br>- Uses Celery for asynchronous task processing, ensuring reliable and efficient length extraction<br>- Critical for tasks requiring precise audio duration information within the projects worker architecture.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/FerrariDG/async-ml-inference/blob/master/src/workers/audio/config.py'>config.py</a></b></td>
									<td style='padding: 8px;'>Provide Celery configurations for the Audio Length worker, defining task acknowledgments, worker task limit, queue creation, and Redis key expiration time.</td>
								</tr>
							</table>
						</blockquote>
					</details>
					<!-- euro Submodule -->
					<details>
						<summary><b>euro</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ src.workers.euro</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/FerrariDG/async-ml-inference/blob/master/src/workers/euro/worker.py'>worker.py</a></b></td>
									<td style='padding: 8px;'>- Extracts Euromillions results from a designated URL using a Celery worker<br>- Validates backend and broker connections before scraping the page for numbers and stars relevant to the draw date<br>- Handles exceptions if data is not found, ensuring proper state updates along the way.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/FerrariDG/async-ml-inference/blob/master/src/workers/euro/config.py'>config.py</a></b></td>
									<td style='padding: 8px;'>- Configure Celery settings for the Euromillions Results worker in the project<br>- Set task acknowledgements to be late, prefetch multiplier to 1, and define a queue specifically for Euro tasks<br>- Results expire after 48 hours.</td>
								</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<!-- client Submodule -->
			<details>
				<summary><b>client</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ src.client</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/FerrariDG/async-ml-inference/blob/master/src/client/requirements.txt'>requirements.txt</a></b></td>
							<td style='padding: 8px;'>- Facilitates dependency management for the client module by defining required packages and versions in the <code>requirements.txt</code> file<br>- This ensures seamless integration with external libraries and tools as specified by the projects dependencies.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/FerrariDG/async-ml-inference/blob/master/src/client/Dockerfile'>Dockerfile</a></b></td>
							<td style='padding: 8px;'>- A Dockerfile sets up a Python environment for a client service in the project architecture<br>- It installs dependencies from requirements.txt, specifies the start command as python client.py, and exposes port 5000 for communication.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/FerrariDG/async-ml-inference/blob/master/src/client/client.py'>client.py</a></b></td>
							<td style='padding: 8px;'>Generate and send audio URLs, dates, and retrieve results concurrently to improve performance in the project for processing audio data.</td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---

## 🚀 Getting Started

### 🔖 Prerequisites

This project requires the following dependencies:

- **Programming Language:** Python
- **Package Manager:** Pipenv, Pip
- **Container Runtime:** Docker

### 🛠️ Installation

Build async-ml-inference from the source and install dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/FerrariDG/async-ml-inference
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd async-ml-inference
    ```

3. **Install the dependencies:**

<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![docker][docker-shield]][docker-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [docker-shield]: https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white -->
	<!-- [docker-link]: https://www.docker.com/ -->

	**Using [docker](https://www.docker.com/):**

	```sh
	❯ docker build -t FerrariDG/async-ml-inference .
	```
<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![pipenv][pipenv-shield]][pipenv-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [pipenv-shield]: https://img.shields.io/badge/Pipenv-3775A9.svg?style={badge_style}&logo=pypi&logoColor=white -->
	<!-- [pipenv-link]: https://pipenv.pypa.io/ -->

	**Using [pipenv](https://pipenv.pypa.io/):**

	```sh
	❯ pipenv install
	```
<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![pip][pip-shield]][pip-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [pip-shield]: https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white -->
	<!-- [pip-link]: https://pypi.org/project/pip/ -->

	**Using [pip](https://pypi.org/project/pip/):**

	```sh
	❯ pip install -r src/api/requirements.txt, src/workers/requirements.txt, src/client/requirements.txt
	```


### 📺 Usage

Run the project with:

**Using [docker](https://www.docker.com/):**
```sh
docker run -it {image_name}
```
**Using [pipenv](https://pipenv.pypa.io/):**
```sh
pipenv shell
❯ pipenv run python {entrypoint}
```
**Using [pip](https://pypi.org/project/pip/):**
```sh
python {entrypoint}
```

### 🧪 Testing

Async-ml-inference uses the {__test_framework__} test framework. Run the test suite with:

**Using [pipenv](https://pipenv.pypa.io/):**
```sh
pipenv shell
❯ pipenv run pytest
```
**Using [pip](https://pypi.org/project/pip/):**
```sh
pytest
```


---

## 🎞️ Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🤝 Contributing

- **💬 [Join the Discussions](https://github.com/FerrariDG/async-ml-inference/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/FerrariDG/async-ml-inference/issues)**: Submit bugs found or log feature requests for the `async-ml-inference` project.
- **💡 [Submit Pull Requests](https://github.com/FerrariDG/async-ml-inference/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

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

## 📜 License

Async-ml-inference is protected under the [LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 🎩 Acknowledgments

- Credit `contributors`, `inspiration`, `references`, etc.

<div align="left"><a href="#top">⬆ Return</a></div>

---

<!-- README-AI COMMAND: -->
<!--
```sh
readmeai \
    --repository 'https://github.com/FerrariDG/async-ml-inference' \
    --output 'docs/docs/examples/generated/tmp/readme-async-ml-inference.md' \
    --badge-style 'plastic' \
    --badge-color '43a047' \
    --logo 'BLUE' \
    --header-style 'BANNER' \
    --navigation-style 'BULLET' \
    --emojis 'vintage' \
    --temperature 1.005 \
    --tree-max-depth 4 \
    --api openai
```
-->
