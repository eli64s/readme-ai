<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
</p>
<p align="center">
    <h1 align="center">MLOPS-COURSE</h1>
</p>
<p align="center">
    <em>MLOps mastery made simple with mlops-course!</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/GokuMohandas/mlops-course?style=flat&color=orange" alt="license">
	<img src="https://img.shields.io/github/last-commit/GokuMohandas/mlops-course?style=flat&logo=git&logoColor=white&color=orange" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/GokuMohandas/mlops-course?style=flat&color=orange" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/GokuMohandas/mlops-course?style=flat&color=orange" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
	<img src="https://img.shields.io/badge/precommit-FAB040.svg?style=flat&logo=pre-commit&logoColor=black" alt="precommit">
	<img src="https://img.shields.io/badge/scikitlearn-F7931E.svg?style=flat&logo=scikit-learn&logoColor=white" alt="scikitlearn">
	<img src="https://img.shields.io/badge/Jupyter-F37626.svg?style=flat&logo=Jupyter&logoColor=white" alt="Jupyter">
	<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat&logo=YAML&logoColor=white" alt="YAML">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=flat&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions">
	<br>
	<img src="https://img.shields.io/badge/pandas-150458.svg?style=flat&logo=pandas&logoColor=white" alt="pandas">
	<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat&logo=Pytest&logoColor=white" alt="Pytest">
	<img src="https://img.shields.io/badge/Ray-028CF0.svg?style=flat&logo=Ray&logoColor=white" alt="Ray">
	<img src="https://img.shields.io/badge/MLflow-0194E2.svg?style=flat&logo=MLflow&logoColor=white" alt="MLflow">
	<img src="https://img.shields.io/badge/NumPy-013243.svg?style=flat&logo=NumPy&logoColor=white" alt="NumPy">
	<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=flat&logo=FastAPI&logoColor=white" alt="FastAPI">
</p>
<hr>

## 🔗 Quick Links

> - [📍 Overview](#-overview)
> - [📦 Features](#-features)
> - [📂 Repository Structure](#-repository-structure)
> - [🧩 Modules](#-modules)
> - [🚀 Getting Started](#-getting-started)
>   - [⚙️ Installation](#️-installation)
>   - [🤖 Running mlops-course](#-running-mlops-course)
>   - [🧪 Tests](#-tests)
> - [🛠 Project Roadmap](#-project-roadmap)
> - [🤝 Contributing](#-contributing)
> - [📄 License](#-license)
> - [👏 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

The mlops-course project is a comprehensive codebase that aims to provide an end-to-end solution for implementing and managing machine learning operations (MLOps) pipelines. It offers functionalities for data preprocessing, model training, evaluation, and deployment. The project utilizes tools like Ray Serve, PyTorch, and MLflow to serve and deploy trained models, perform hyperparameter tuning experiments, train models on distributed workloads, evaluate model performance, and handle data processing tasks. By combining these features, the project simplifies and streamlines the process of developing and managing machine learning models, enabling practitioners to focus on the core aspects of their projects.

---

## 📦 Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | The project's architecture is based on a distributed workload using Ray and PyTorch. It includes components for data preprocessing, model training, evaluation, and deployment. The architecture also utilizes Ray Serve and FastAPI for serving the trained machine learning model. |
| 🔩 | **Code Quality**  | The codebase follows consistent formatting rules with tools like Black, iSort, Flake8, and Pytest configured in the `pyproject.toml` file. The presence of pre-commit hooks and Makefile for formatting and linting tasks suggests a focus on code quality and style. |
| 📄 | **Documentation** | The project includes extensive documentation, with Markdown files organized in a structured manner. The repository contains a `mkdocs` configuration and GitHub Actions workflow for automating the documentation generation and deployment process. |
| 🔌 | **Integrations**  | Key integrations include MLflow for experiment tracking, Ray for distributed workload orchestration, and GitHub Actions for CI/CD pipelines. The project also integrates with external libraries such as Transformers, Snorkel, Cleanlab, and Hyperopt for various machine learning tasks. |
| 🧩 | **Modularity**    | The codebase demonstrates modularity and reusability with separate modules for data processing, model training, evaluation, and deployment. Utility functions in the `madewithml/utils.py` module support data processing tasks. The use of Ray and PyTorch allows for scalable and adaptable architecture. |
| 🧪 | **Testing**       | The project utilizes Pytest for testing, with coverage reporting through pytest-cov. The presence of the `tests` directory suggests a focused approach to testing. |
| ⚡️  | **Performance**   | The project benefits from distributed workload execution using Ray, which can improve efficiency and resource utilization. However, a detailed assessment of performance would require benchmarking and analysis of the actual code. |
| 🛡️ | **Security**      | The repository does not explicitly specify security measures, but the use of GitHub Actions and integration with external tools suggests a focus on secure software delivery practices. Additional measures can potentially be implemented, depending on the specific deployment and runtime environment. |
| 📦 | **Dependencies**  | Key external libraries and dependencies include Ray, PyTorch, Transformers, Snorkel, Cleanlab, and Hyperopt. The `requirements.txt` file specifies the necessary packages for various purposes such as data preprocessing, model training, evaluation, and deployment. |


---

## 📂 Repository Structure

```sh
└── mlops-course/
    ├── .github
    │   └── workflows
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
    │   └── services
    ├── docs
    │   ├── index.md
    │   └── madewithml
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
        ├── data
        └── model
```

---

## 🧩 Modules

<details closed><summary>.</summary>

| File                                                                                          | Summary                                                                                                                                                                                                                                                                                                                                                                                      |
| ---                                                                                           | ---                                                                                                                                                                                                                                                                                                                                                                                          |
| [requirements.txt](https://github.com/GokuMohandas/mlops-course/blob/master/requirements.txt) | The code snippet in the `requirements.txt` file specifies the necessary dependencies for the parent repository. It lists various packages for different purposes such as data preprocessing, model training, evaluation, and deployment.                                                                                                                                                     |
| [Makefile](https://github.com/GokuMohandas/mlops-course/blob/master/Makefile)                 | The Makefile in the repository is responsible for executing styling and cleaning tasks. It provides commands for code formatting, linting, and removing unnecessary files.                                                                                                                                                                                                                   |
| [pyproject.toml](https://github.com/GokuMohandas/mlops-course/blob/master/pyproject.toml)     | This code snippet is located in the `pyproject.toml` file of the repository. It sets up linting, formatting, and testing configurations for the project, including tools like Black, iSort, Flake8, and Pytest. It defines the file formatting rules and excludes certain directories from linting. The code ensures that the codebase follows consistent formatting and is properly tested. |

</details>

<details closed><summary>deploy</summary>

| File                                                                                                         | Summary                                                                                                                                                                                                                                                                                            |
| ---                                                                                                          | ---                                                                                                                                                                                                                                                                                                |
| [cluster_env.yaml](https://github.com/GokuMohandas/mlops-course/blob/master/deploy/cluster_env.yaml)         | The code snippet in `deploy/cluster_env.yaml` defines the environment configuration for the parent repository. It specifies the base image, environment variables, Debian packages, Python packages, and post-build commands.                                                                      |
| [cluster_compute.yaml](https://github.com/GokuMohandas/mlops-course/blob/master/deploy/cluster_compute.yaml) | The code snippet `deploy/cluster_compute.yaml` contains the configuration settings for the cluster computation in the parent repository's architecture. It specifies the cloud provider, region, instance types, minimum and maximum workers, storage volume size, and tags for the cluster nodes. |

</details>

<details closed><summary>deploy.jobs</summary>

| File                                                                                                  | Summary                                                                                                                                                                                                                                                                                                  |
| ---                                                                                                   | ---                                                                                                                                                                                                                                                                                                      |
| [workloads.yaml](https://github.com/GokuMohandas/mlops-course/blob/master/deploy/jobs/workloads.yaml) | This code snippet, located in `deploy/jobs/workloads.yaml`, defines the configuration for a workload in the parent repository's architecture. It specifies the project ID, cluster environment, compute configuration, runtime environment, and other parameters necessary for the workload's execution. |
| [workloads.sh](https://github.com/GokuMohandas/mlops-course/blob/master/deploy/jobs/workloads.sh)     | This code snippet is responsible for executing different tasks, such as testing data/code, training a model, evaluating performance, and saving results to S3. It sets up necessary environment variables, runs pytest, executes training and evaluation scripts, and performs S3 uploads.               |

</details>

<details closed><summary>deploy.services</summary>

| File                                                                                                          | Summary                                                                                                                                                                                                                                                                                                                             |
| ---                                                                                                           | ---                                                                                                                                                                                                                                                                                                                                 |
| [serve_model.yaml](https://github.com/GokuMohandas/mlops-course/blob/master/deploy/services/serve_model.yaml) | The code snippet in `deploy/services/serve_model.yaml` is responsible for serving the madewithml project using Ray Serve, specifying the project ID, cluster environment, compute configuration, and other runtime environment variables. It enables the deployment of the madewithml project with the specified rollout strategy.  |
| [serve_model.py](https://github.com/GokuMohandas/mlops-course/blob/master/deploy/services/serve_model.py)     | This code snippet serves to copy files from an S3 bucket, sets the model registry path, and binds the entrypoint for model deployment. It is located in the `deploy/services/serve_model.py` file of the repository. The key activities include copying files from S3, setting the model registry path, and binding the entrypoint. |

</details>

<details closed><summary>madewithml</summary>

| File                                                                                           | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---                                                                                            | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [config.py](https://github.com/GokuMohandas/mlops-course/blob/master/madewithml/config.py)     | The code snippet in `madewithml/config.py` sets up logging and configuration for the parent repository. It creates directories, configures MLflow, and defines a logger. Additional constraints for stopwords are also included.                                                                                                                                                                                                                                                                                             |
| [models.py](https://github.com/GokuMohandas/mlops-course/blob/master/madewithml/models.py)     | The `models.py` file in the `madewithml` directory contains the `FinetunedLLM` class, which defines the architecture for a Large Language Model (LLM) that can be fine-tuned. It takes in various parameters, including the LLM itself, and implements the forward pass method for processing batches of data.                                                                                                                                                                                                               |
| [predict.py](https://github.com/GokuMohandas/mlops-course/blob/master/madewithml/predict.py)   | The `predict.py` code snippet in the `madewithml` module is responsible for predicting project tags based on project title and description. It uses MLflow to retrieve the best checkpoint from a specific run, loads the checkpoint, and performs the prediction. The results are then logged and returned.                                                                                                                                                                                                                 |
| [serve.py](https://github.com/GokuMohandas/mlops-course/blob/master/madewithml/serve.py)       | This `serve.py` code snippet in the `madewithml` module is responsible for deploying and serving a trained machine learning model. It uses FastAPI and Ray Serve to expose endpoints for health check, model evaluation, and prediction. The code initializes the model and provides methods for handling requests and returning results.                                                                                                                                                                                    |
| [utils.py](https://github.com/GokuMohandas/mlops-course/blob/master/madewithml/utils.py)       | The `utils.py` code snippet in the `madewithml` module of the parent repository provides utility functions for reproducibility, data processing, and data conversion. It includes functions to set seeds for reproducibility, load and save dictionaries to JSON files, pad arrays, collate batches of data, retrieve the MLflow run ID for a Ray trial ID, and convert dictionaries to lists of dictionaries. These functions are critical for various data processing tasks in the repository's machine learning pipeline. |
| [tune.py](https://github.com/GokuMohandas/mlops-course/blob/master/madewithml/tune.py)         | This code snippet is part of the madewithml repository and is responsible for performing hyperparameter tuning experiments. It uses Ray Tune to search for the best hyperparameters by training and evaluating multiple models. The results of the tuning experiment are returned as a grid of results. The code also provides options for specifying the dataset, initial parameters, number of workers, and other tuning configurations.                                                                                   |
| [train.py](https://github.com/GokuMohandas/mlops-course/blob/master/madewithml/train.py)       | The `madewithml/train.py` file in the repository is responsible for training a model using distributed workload. It uses the Ray library and PyTorch to train the model on multiple workers with customizable hyperparameters. The code has functions for training and evaluation steps, a training loop for each worker, and a main function for training the model.                                                                                                                                                        |
| [evaluate.py](https://github.com/GokuMohandas/mlops-course/blob/master/madewithml/evaluate.py) | The `evaluate.py` file in the `madewithml` module of the codebase is responsible for evaluating the performance of a model on a holdout dataset. It contains functions for calculating overall performance metrics, per class metrics, and metrics for different slices of the data. The code also includes a CLI command for running the evaluation and saving the results.                                                                                                                                                 |
| [data.py](https://github.com/GokuMohandas/mlops-course/blob/master/madewithml/data.py)         | The `madewithml/data.py` code snippet in the `mlops-course` repository is responsible for loading data from a source into a Ray Dataset, splitting the dataset into train and test sets with equal amounts of data points from each class, cleaning raw text, tokenizing text inputs, and preprocessing a raw dataframe. This snippet facilitates the data handling and preprocessing aspects of the parent repository's architecture.                                                                                       |

</details>

<details closed><summary>.github.workflows</summary>

| File                                                                                                                | Summary                                                                                                                                                                                                                                                                                                             |
| ---                                                                                                                 | ---                                                                                                                                                                                                                                                                                                                 |
| [serve.yaml](https://github.com/GokuMohandas/mlops-course/blob/master/.github/workflows/serve.yaml)                 | This code snippet defines a GitHub Actions workflow called serve.yaml in the.github/workflows directory of the repository. It is responsible for deploying and serving the trained machine learning model.                                                                                                          |
| [json_to_md.py](https://github.com/GokuMohandas/mlops-course/blob/master/.github/workflows/json_to_md.py)           | This code snippet, located at `.github/workflows/json_to_md.py`, is responsible for converting JSON files to Markdown format. It is an essential part of the repository's architecture, providing a critical feature for transforming data into a human-readable format.                                            |
| [workloads.yaml](https://github.com/GokuMohandas/mlops-course/blob/master/.github/workflows/workloads.yaml)         | This code snippet is located in the.github/workflows/workloads.yaml file. It likely defines the workflows and tasks that need to be executed in the repository's CI/CD pipeline. Its critical features include automation of the build and deployment processes, ensuring efficient and reliable software delivery. |
| [documentation.yaml](https://github.com/GokuMohandas/mlops-course/blob/master/.github/workflows/documentation.yaml) | The code snippet in `documentation.yaml` is responsible for automating the documentation workflow in the `mlops-course` repository. It defines the steps and triggers for generating and deploying documentation using `mkdocs` and GitHub Actions.                                                                 |

</details>

<details closed><summary>notebooks</summary>

| File                                                                                                    | Summary                                                                                                                                                                                                                                                                                                                       |
| ---                                                                                                     | ---                                                                                                                                                                                                                                                                                                                           |
| [benchmarks.ipynb](https://github.com/GokuMohandas/mlops-course/blob/master/notebooks/benchmarks.ipynb) | The code snippet plays a critical role in the parent repository's architecture by achieving specific functionalities. It is not possible to generate a summary without looking at the actual code snippet and understanding its implementation details. Please provide the relevant code snippet for a more accurate summary. |
| [madewithml.ipynb](https://github.com/GokuMohandas/mlops-course/blob/master/notebooks/madewithml.ipynb) | The code snippet is part of the parent repository's architecture and performs critical features. Its main role includes data preprocessing and feature engineering for machine learning models. It contributes to the overall MLOps course and is linked to datasets and deployment configurations.                           |

</details>

---

## 🚀 Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Python**: `version x.y.z`

### ⚙️ Installation

1. Clone the mlops-course repository:

```sh
git clone https://github.com/GokuMohandas/mlops-course
```

2. Change to the project directory:

```sh
cd mlops-course
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

### 🤖 Running mlops-course

Use the following command to run mlops-course:

```sh
python main.py
```

### 🧪 Tests

To execute tests, run:

```sh
pytest
```

---

## 🛠 Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/GokuMohandas/mlops-course/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/GokuMohandas/mlops-course/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/GokuMohandas/mlops-course/issues)**: Submit bugs found or log feature requests for Mlops-course.

<details closed>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
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

[**Return**](#-quick-links)

---
