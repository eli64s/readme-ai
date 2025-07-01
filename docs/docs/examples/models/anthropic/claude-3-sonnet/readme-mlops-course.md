<div id="top">

<!-- HEADER STYLE: COMPACT -->
<img src="readmeai/assets/logos/terminal.svg" width="30%" align="left" style="margin-right: 15px">

# MLOPS-COURSE
<em>Mastering ML Lifecycle: From Concept to Production Powerhouse</em>

<!-- BADGES -->
<img src="https://img.shields.io/github/license/GokuMohandas/mlops-course?style=flat-square&logo=opensourceinitiative&logoColor=white&color=2e7d32" alt="license">
<img src="https://img.shields.io/github/last-commit/GokuMohandas/mlops-course?style=flat-square&logo=git&logoColor=white&color=2e7d32" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/GokuMohandas/mlops-course?style=flat-square&color=2e7d32" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/GokuMohandas/mlops-course?style=flat-square&color=2e7d32" alt="repo-language-count">

<em>Built with the tools and technologies:</em>

<img src="https://img.shields.io/badge/SQLAlchemy-D71F00.svg?style=flat-square&logo=SQLAlchemy&logoColor=white" alt="SQLAlchemy">
<img src="https://img.shields.io/badge/TOML-9C4121.svg?style=flat-square&logo=TOML&logoColor=white" alt="TOML">
<img src="https://img.shields.io/badge/Jupyter-F37626.svg?style=flat-square&logo=Jupyter&logoColor=white" alt="Jupyter">
<img src="https://img.shields.io/badge/scikitlearn-F7931E.svg?style=flat-square&logo=scikit-learn&logoColor=white" alt="scikitlearn">
<img src="https://img.shields.io/badge/precommit-FAB040.svg?style=flat-square&logo=pre-commit&logoColor=black" alt="precommit">
<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat-square&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=flat-square&logo=FastAPI&logoColor=white" alt="FastAPI">
<img src="https://img.shields.io/badge/NumPy-013243.svg?style=flat-square&logo=NumPy&logoColor=white" alt="NumPy">
<br>
<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat-square&logo=Pytest&logoColor=white" alt="Pytest">
<img src="https://img.shields.io/badge/MLflow-0194E2.svg?style=flat-square&logo=MLflow&logoColor=white" alt="MLflow">
<img src="https://img.shields.io/badge/Ray-028CF0.svg?style=flat-square&logo=Ray&logoColor=white" alt="Ray">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=flat-square&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions">
<img src="https://img.shields.io/badge/pandas-150458.svg?style=flat-square&logo=pandas&logoColor=white" alt="pandas">
<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat-square&logo=YAML&logoColor=white" alt="YAML">

<br clear="left"/>

## 💧 Table of Contents

I. [💧 Table of Contents](#-table-of-contents)<br>
II. [🌊 Overview](#-overview)<br>
III. [💦 Features](#-features)<br>
IV. [🔵 Project Structure](#-project-structure)<br>
&nbsp;&nbsp;&nbsp;&nbsp;IV.a. [🔷 Project Index](#-project-index)<br>
V. [💠 Getting Started](#-getting-started)<br>
&nbsp;&nbsp;&nbsp;&nbsp;V.a. [🅿️ Prerequisites](#-prerequisites)<br>
&nbsp;&nbsp;&nbsp;&nbsp;V.b. [🌀 Installation](#-installation)<br>
&nbsp;&nbsp;&nbsp;&nbsp;V.c. [🔹 Usage](#-usage)<br>
&nbsp;&nbsp;&nbsp;&nbsp;V.d. [❄ ️ Testing](#-testing)<br>
VI. [🧊 Roadmap](#-roadmap)<br>
VII. [⚪ Contributing](#-contributing)<br>
VIII. [⬜ License](#-license)<br>
IX. [✨ Acknowledgments](#-acknowledgments)<br>

---

## 🌊 Overview

MLOps Course is a comprehensive toolkit for building and deploying production-ready machine learning projects. It guides developers through the entire ML lifecycle, from data handling to model serving.

**Why mlops-course?**

This project streamlines the development of scalable and maintainable machine learning solutions. The core features include:

- **🔄 End-to-end ML pipeline:** Covers data processing, model creation, training, evaluation, and serving.
- **🚀 Automated deployment:** Integrates with GitHub Actions and Anyscale for seamless CI/CD workflows.
- **🎛️ Hyperparameter tuning:** Utilizes Ray Tune for efficient optimization of model parameters.
- **📊 Experiment tracking:** Incorporates MLflow for comprehensive logging and reproducibility.
- **🧹 Code quality maintenance:** Employs tools like Black, Flake8, and isort to ensure consistent, clean code.

---

## 💦 Features

|      | Component       | Details                              |
| :--- | :-------------- | :----------------------------------- |
| ⚙️  | **Architecture**  | <ul><li>MLOps-focused course structure</li><li>Jupyter notebooks for interactive learning</li><li>Modular Python codebase</li><li>Containerized deployments using GitHub Actions</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>`pre-commit` hooks for automated checks</li><li>`black` for code formatting</li><li>`flake8` for linting</li><li>`isort` for import sorting</li><li>`pyupgrade` for Python syntax upgrades</li></ul> |
| 📄 | **Documentation** | <ul><li>`mkdocs` for generating documentation</li><li>`mkdocstrings` for auto-generating API docs</li><li>Comprehensive `README.md` files</li><li>Jupyter notebooks as interactive documentation</li></ul> |
| 🔌 | **Integrations**  | <ul><li>`MLflow` for experiment tracking</li><li>`Ray` for distributed computing</li><li>`FastAPI` for serving models</li><li>`Anyscale` for cloud deployment</li><li>`Great Expectations` for data validation</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Separate YAML files for different environments</li><li>Modular Python package structure</li><li>`pyproject.toml` for project configuration</li></ul> |
| 🧪 | **Testing**       | <ul><li>`pytest` for unit testing</li><li>`pytest-cov` for code coverage</li><li>`cleanlab` and `snorkel` for data quality checks</li></ul> |
| ⚡️  | **Performance**   | <ul><li>`torch` for GPU-accelerated computations</li><li>`Ray` for distributed processing</li><li>`Hyperopt` for hyperparameter optimization</li></ul> |
| 🛡️ | **Security**      | <ul><li>GitHub Actions for CI/CD pipelines</li><li>Environment-specific YAML configurations</li><li>`pre-commit` hooks for security checks</li></ul> |
| 📦 | **Dependencies**  | <ul><li>`requirements.txt` for Python package management</li><li>`pip` as the package installer</li><li>Extensive use of data science libraries (e.g., `pandas`, `numpy`, `scikit-learn`)</li></ul> |

---

## 🔵 Project Structure

```sh
└── mlops-course/
    ├── .github
    │   └── workflows
    │       ├── documentation.yaml
    │       ├── json_to_md.py
    │       ├── serve.yaml
    │       └── workloads.yaml
    ├── LICENSE
    ├── Makefile
    ├── README.md
    ├── datasets
    │   ├── dataset.csv
    │   ├── holdout.csv
    │   ├── projects.csv
    │   └── tags.csv
    ├── deploy
    │   ├── cluster_compute.yaml
    │   ├── cluster_env.yaml
    │   ├── jobs
    │   │   ├── workloads.sh
    │   │   └── workloads.yaml
    │   └── services
    │       ├── serve_model.py
    │       └── serve_model.yaml
    ├── docs
    │   ├── index.md
    │   └── madewithml
    │       ├── data.md
    │       ├── evaluate.md
    │       ├── models.md
    │       ├── predict.md
    │       ├── serve.md
    │       ├── train.md
    │       ├── tune.md
    │       └── utils.md
    ├── madewithml
    │   ├── config.py
    │   ├── data.py
    │   ├── evaluate.py
    │   ├── models.py
    │   ├── predict.py
    │   ├── serve.py
    │   ├── train.py
    │   ├── tune.py
    │   └── utils.py
    ├── mkdocs.yml
    ├── notebooks
    │   ├── benchmarks.ipynb
    │   └── madewithml.ipynb
    ├── pyproject.toml
    ├── requirements.txt
    └── tests
        ├── code
        │   ├── conftest.py
        │   ├── test_data.py
        │   ├── test_predict.py
        │   ├── test_train.py
        │   ├── test_tune.py
        │   ├── test_utils.py
        │   └── utils.py
        ├── data
        │   ├── conftest.py
        │   └── test_dataset.py
        └── model
            ├── conftest.py
            ├── test_behavioral.py
            └── utils.py
```

### 🔷 Project Index

<details open>
	<summary><b><code>MLOPS-COURSE/</code></b></summary>
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
					<td style='padding: 8px;'><b><a href='https://github.com/GokuMohandas/mlops-course/blob/master/mkdocs.yml'>mkdocs.yml</a></b></td>
					<td style='padding: 8px;'>- Configures the MkDocs documentation structure for the Made With ML project<br>- Defines the site name, URL, repository link, and navigation hierarchy<br>- Organizes content into sections covering data handling, model creation, training, tuning, evaluation, prediction, serving, and utilities<br>- Utilizes the ReadTheDocs theme and enables automatic reloading for changes<br>- Sets up the mkdocstrings plugin to enhance documentation generation from source code.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/GokuMohandas/mlops-course/blob/master/requirements.txt'>requirements.txt</a></b></td>
					<td style='padding: 8px;'>- Requirements file specifies dependencies for a comprehensive machine learning project<br>- It includes libraries for data processing, model training, visualization, and deployment<br>- The project encompasses various aspects such as hyperparameter optimization, natural language processing, deep learning, and MLOps<br>- Additional sections cover documentation, code styling, testing, and development tools, indicating a well-structured and professionally managed codebase with emphasis on maintainability and reproducibility.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/GokuMohandas/mlops-course/blob/master/Makefile'>Makefile</a></b></td>
					<td style='padding: 8px;'>- Manages project maintenance tasks through a Makefile<br>- Automates code styling with tools like Black, Flake8, isort, and pyupgrade<br>- Implements cleaning operations to remove unnecessary files and caches, including.DS_Store, __pycache__,.pyc,.pyo,.pytest_cache,.ipynb_checkpoints, and coverage files<br>- Streamlines development workflow by providing easy-to-use commands for maintaining code quality and cleanliness across the project.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/GokuMohandas/mlops-course/blob/master/pyproject.toml'>pyproject.toml</a></b></td>
					<td style='padding: 8px;'>- Configures code formatting and testing tools for the project<br>- Specifies settings for Black, isort, flake8, pyupgrade, pytest, and coverage<br>- Defines line lengths, excluded directories, and ignored warnings<br>- Sets Python version compatibility and test file patterns<br>- Ensures consistent code style and facilitates efficient testing across the codebase, promoting maintainability and adherence to best practices in Python development.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- deploy Submodule -->
	<details>
		<summary><b>deploy</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ deploy</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/GokuMohandas/mlops-course/blob/master/deploy/cluster_env.yaml'>cluster_env.yaml</a></b></td>
					<td style='padding: 8px;'>- Defines the environment configuration for deploying the projects cluster<br>- Specifies the base Docker image, required Debian packages, and post-build commands<br>- Notably, it installs dependencies from the Made-With-ML projects requirements file, suggesting integration or utilization of that project's components<br>- Sets up a consistent and reproducible environment for running the application across different deployment instances.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/GokuMohandas/mlops-course/blob/master/deploy/cluster_compute.yaml'>cluster_compute.yaml</a></b></td>
					<td style='padding: 8px;'>- Defines cluster configuration for cloud deployment in the MadeWithML project<br>- Specifies cloud provider, region, and node types for both head and worker nodes<br>- Includes GPU-enabled worker nodes for computational tasks<br>- Sets AWS-specific configurations like block device mappings and instance tagging<br>- Enables scalable and flexible compute resources tailored for machine learning workflows in a cloud environment.</td>
				</tr>
			</table>
			<!-- jobs Submodule -->
			<details>
				<summary><b>jobs</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ deploy.jobs</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/GokuMohandas/mlops-course/blob/master/deploy/jobs/workloads.yaml'>workloads.yaml</a></b></td>
							<td style='padding: 8px;'>- Defines a job configuration for workloads in the projects deployment pipeline<br>- Specifies the project ID, cluster environment, compute settings, and runtime environment details<br>- Sets the working directory, upload path, and GitHub username as environment variables<br>- Utilizes a shell script for job execution and disables retries<br>- Essential for orchestrating and managing workload deployments within the project infrastructure.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/GokuMohandas/mlops-course/blob/master/deploy/jobs/workloads.sh'>workloads.sh</a></b></td>
							<td style='padding: 8px;'>- Executes a comprehensive pipeline for machine learning model development and evaluation<br>- Performs data testing, code testing, model training, evaluation on holdout data, and model testing<br>- Utilizes pytest for testing, trains a model with specified configurations, and saves results to files<br>- Finally, uploads model artifacts and results to an S3 bucket for storage and accessibility.</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- services Submodule -->
			<details>
				<summary><b>services</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ deploy.services</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/GokuMohandas/mlops-course/blob/master/deploy/services/serve_model.yaml'>serve_model.yaml</a></b></td>
							<td style='padding: 8px;'>- Configures deployment settings for the madewithml project using Ray Serve<br>- Specifies the project ID, cluster environment, and compute configuration<br>- Defines the import path for the model serving entrypoint and sets up the runtime environment, including working directory and S3 upload path<br>- Establishes environment variables and determines the rollout strategy for updates to the deployed service.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/GokuMohandas/mlops-course/blob/master/deploy/services/serve_model.py'>serve_model.py</a></b></td>
							<td style='padding: 8px;'>- Deploys the trained model for serving predictions<br>- Retrieves model artifacts and results from an S3 bucket, copying them to the local environment<br>- Sets up the ModelDeployment entrypoint using a specified run ID and prediction threshold<br>- Facilitates the transition from model training to deployment, enabling the serving of predictions in a production-ready environment.</td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<!-- madewithml Submodule -->
	<details>
		<summary><b>madewithml</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ madewithml</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/GokuMohandas/mlops-course/blob/master/madewithml/config.py'>config.py</a></b></td>
					<td style='padding: 8px;'>- Configures essential project settings and establishes logging mechanisms<br>- Defines directory structures, sets up MLflow tracking, and configures logging parameters for different output levels<br>- Initializes a root logger and specifies handlers for console, info, and error logs<br>- Includes a comprehensive list of stopwords for text processing tasks<br>- Serves as a central configuration hub for the entire project, ensuring consistent settings across modules.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/GokuMohandas/mlops-course/blob/master/madewithml/models.py'>models.py</a></b></td>
					<td style='padding: 8px;'>- Defines the FinetunedLLM class, a PyTorch module for fine-tuning large language models<br>- Implements a forward pass that processes input tokens through the LLM, applies dropout, and maps the output to the desired number of classes<br>- Serves as the core model architecture for the project, enabling customization of pre-trained language models for specific classification tasks.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/GokuMohandas/mlops-course/blob/master/madewithml/predict.py'>predict.py</a></b></td>
					<td style='padding: 8px;'>- Provides prediction functionality for a machine learning project using MLflow and Ray<br>- Implements methods to decode indices, format probabilities, and predict tags with probabilities<br>- Includes CLI commands to retrieve the best run ID from MLflow experiments and make predictions based on project titles and descriptions<br>- Utilizes TorchPredictor and preprocessor components for efficient inference on input data.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/GokuMohandas/mlops-course/blob/master/madewithml/serve.py'>serve.py</a></b></td>
					<td style='padding: 8px;'>- Serves as the entry point for deploying a machine learning model as a RESTful API using Ray Serve and FastAPI<br>- Defines endpoints for health checks, retrieving run IDs, evaluating models, and making predictions<br>- Implements custom logic for prediction thresholds and handles incoming requests asynchronously<br>- Initializes the model using MLflow and TorchPredictor, enabling seamless integration with the projects machine learning pipeline.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/GokuMohandas/mlops-course/blob/master/madewithml/utils.py'>utils.py</a></b></td>
					<td style='padding: 8px;'>- Provides utility functions for the madewithml project, supporting various operations across the codebase<br>- Includes methods for setting random seeds, loading and saving dictionaries, padding arrays, collating batches, retrieving MLflow run IDs, and converting dictionaries to lists<br>- These utilities enhance reproducibility, data handling, and experiment tracking, facilitating seamless integration with machine learning workflows and external libraries like Ray and MLflow.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/GokuMohandas/mlops-course/blob/master/madewithml/tune.py'>tune.py</a></b></td>
					<td style='padding: 8px;'>- Implements hyperparameter tuning functionality for machine learning models using Ray Tune<br>- Defines a command-line interface to configure and execute tuning experiments, including dataset handling, model training, and result logging<br>- Utilizes Rays distributed computing capabilities to efficiently search the parameter space, optimize model performance, and track experiments with MLflow integration<br>- Supports customizable tuning strategies and scaling configurations for flexible experimentation.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/GokuMohandas/mlops-course/blob/master/madewithml/train.py'>train.py</a></b></td>
					<td style='padding: 8px;'>- Implements the main training functionality for a machine learning model using Ray and PyTorch<br>- Defines training and evaluation steps, a distributed training loop, and a command-line interface for model training<br>- Handles data preprocessing, model initialization, and distributed training across multiple workers<br>- Integrates with MLflow for experiment tracking and supports customizable hyperparameters and training configurations.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/GokuMohandas/mlops-course/blob/master/madewithml/evaluate.py'>evaluate.py</a></b></td>
					<td style='padding: 8px;'>- Evaluates model performance on a holdout dataset using various metrics<br>- Calculates overall, per-class, and slice-specific metrics including precision, recall, and F1 score<br>- Supports loading a specific model run, processing datasets, and generating predictions<br>- Utilizes Ray for distributed computing and Typer for command-line interface<br>- Allows saving evaluation results to a specified location for further analysis or reporting.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/GokuMohandas/mlops-course/blob/master/madewithml/data.py'>data.py</a></b></td>
					<td style='padding: 8px;'>- Handles data processing and preparation for a machine learning project<br>- Implements functions to load data, perform stratified splits, clean text, tokenize input, and preprocess datasets<br>- Includes a custom preprocessor class for Ray datasets<br>- Focuses on preparing text data for natural language processing tasks, with specific attention to cleaning, tokenization, and encoding of textual inputs and their corresponding tags or labels.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- .github Submodule -->
	<details>
		<summary><b>.github</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ .github</b></code>
			<!-- workflows Submodule -->
			<details>
				<summary><b>workflows</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ .github.workflows</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/GokuMohandas/mlops-course/blob/master/.github/workflows/serve.yaml'>serve.yaml</a></b></td>
							<td style='padding: 8px;'>- Automates model deployment on Anyscale using GitHub Actions<br>- Triggered manually or by pushes to the main branch, this workflow configures AWS credentials, sets up Python dependencies, and rolls out the model service<br>- It utilizes secrets for Anyscale authentication and a predefined service configuration file, streamlining the process of serving the machine learning model in a production environment.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/GokuMohandas/mlops-course/blob/master/.github/workflows/json_to_md.py'>json_to_md.py</a></b></td>
							<td style='padding: 8px;'>- Converts JSON data to formatted Markdown, enhancing readability of complex data structures<br>- Processes nested dictionaries, lists, and handles numeric precision<br>- Designed for use in GitHub workflows, it takes input and output file paths as command-line arguments, facilitating automated documentation generation<br>- Supports the projects data presentation and reporting needs within the GitHub Actions environment.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/GokuMohandas/mlops-course/blob/master/.github/workflows/workloads.yaml'>workloads.yaml</a></b></td>
							<td style='padding: 8px;'>- Orchestrates workload execution for the project through GitHub Actions<br>- Triggered manually or on pull requests to the main branch, it configures AWS credentials, sets up dependencies, runs workloads using Anyscale, retrieves results from S3, and comments the training and evaluation outcomes on the pull request<br>- This workflow automates the testing and reporting process, ensuring consistent evaluation of changes before merging into the main branch.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/GokuMohandas/mlops-course/blob/master/.github/workflows/documentation.yaml'>documentation.yaml</a></b></td>
							<td style='padding: 8px;'>- Automates documentation deployment for the project using GitHub Actions<br>- Triggered by pushes to the main branch, the workflow sets up a Python environment, installs necessary dependencies, and deploys the documentation using MkDocs<br>- This process ensures that project documentation is consistently updated and published whenever changes are made to the main branch, maintaining up-to-date and accessible documentation for users and contributors.</td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<!-- notebooks Submodule -->
	<details>
		<summary><b>notebooks</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ notebooks</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/GokuMohandas/mlops-course/blob/master/notebooks/benchmarks.ipynb'>benchmarks.ipynb</a></b></td>
					<td style='padding: 8px;'>- Evaluate and compare the performance of different components or algorithms within the project.2<br>- Provide quantitative metrics to assess the efficiency and effectiveness of the codebase.3<br>- Help identify potential bottlenecks or areas for optimization in the project's implementation.The notebook is located in the notebooks directory, suggesting it's used for interactive analysis and experimentation<br>- As a benchmark file, it plays a crucial role in:-Measuring the speed, accuracy, or other relevant metrics of the project's core functionalities.-Comparing different versions or implementations of algorithms or models.-Establishing baseline performance metrics for future improvements.-Assisting developers in making data-driven decisions about code optimizations and enhancements.This benchmarking tool is essential for maintaining and improving the overall quality and performance of the project, ensuring that changes and updates to the codebase are thoroughly evaluated for their impact on system performance.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/GokuMohandas/mlops-course/blob/master/notebooks/madewithml.ipynb'>madewithml.ipynb</a></b></td>
					<td style='padding: 8px;'>- This Jupyter notebook file, located at <code>notebooks/madewithml.ipynb</code>, serves as the main entry point and interactive guide for the Made With ML project<br>- It provides an introduction to the project and likely contains a series of tutorials, code examples, and explanations that demonstrate how to use the various components of the Made With ML framework.The notebook appears to be designed with a focus on teaching machine learning concepts and practices to developers<br>- It likely covers the entire lifecycle of ML projects, from design and development to deployment and iteration, as indicated by the subtitle Design · Develop · Deploy · Iterate.Given its placement in the project structure, this notebook is probably intended to be the first point of interaction for users of the Made With ML project, offering a hands-on, guided experience through the projects capabilities and methodologies.</td>
				</tr>
			</table>
		</blockquote>
	</details>
</details>

---

## 💠 Getting Started

### 🅿️ Prerequisites

This project requires the following dependencies:

- **Programming Language:** Python
- **Package Manager:** Pip

### 🌀 Installation

Build mlops-course from the source and install dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/GokuMohandas/mlops-course
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd mlops-course
    ```

3. **Install the dependencies:**

<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![pip][pip-shield]][pip-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [pip-shield]: https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white -->
	<!-- [pip-link]: https://pypi.org/project/pip/ -->

	**Using [pip](https://pypi.org/project/pip/):**

	```sh
	❯ pip install -r requirements.txt
	```

### 🔹 Usage

Run the project with:

**Using [pip](https://pypi.org/project/pip/):**
```sh
python {entrypoint}
```

### ❄️ Testing

Mlops-course uses the {__test_framework__} test framework. Run the test suite with:

**Using [pip](https://pypi.org/project/pip/):**
```sh
pytest
```

---

## 🧊 Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## ⚪ Contributing

- **💬 [Join the Discussions](https://github.com/GokuMohandas/mlops-course/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/GokuMohandas/mlops-course/issues)**: Submit bugs found or log feature requests for the `mlops-course` project.
- **💡 [Submit Pull Requests](https://github.com/GokuMohandas/mlops-course/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/GokuMohandas/mlops-course
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
   <a href="https://github.com{/GokuMohandas/mlops-course/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=GokuMohandas/mlops-course">
   </a>
</p>
</details>

---

## ⬜ License

Mlops-course is protected under the [LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## ✨ Acknowledgments

- Credit `contributors`, `inspiration`, `references`, etc.

<div align="left"><a href="#top">⬆ Return</a></div>

---

<!-- README-AI COMMAND: -->
<!--
```sh
readmeai \
    --repository 'https://github.com/GokuMohandas/mlops-course' \
    --output 'docs/docs/examples/ai-providers/anthropic/claude-3-sonnet/readme-mlops-course.md' \
    --badge-style 'flat-square' \
    --badge-color '2e7d32' \
    --logo 'TERMINAL' \
    --header-style 'COMPACT' \
    --navigation-style 'ROMAN' \
    --emojis 'water' \
    --temperature 0.824 \
    --tree-max-depth 3 \
    --api anthropic \
    --model claude-3-5-sonnet-20240620
```
-->
