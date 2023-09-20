<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>mlops-course
</h1>
<h3>◦ Master MLOps with mlops-course!</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash" />
<img src="https://img.shields.io/badge/precommit-FAB040.svg?style&logo=pre-commit&logoColor=black" alt="precommit" />
<img src="https://img.shields.io/badge/scikitlearn-F7931E.svg?style&logo=scikit-learn&logoColor=white" alt="scikitlearn" />
<img src="https://img.shields.io/badge/Jupyter-F37626.svg?style&logo=Jupyter&logoColor=white" alt="Jupyter" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions" />
<img src="https://img.shields.io/badge/pandas-150458.svg?style&logo=pandas&logoColor=white" alt="pandas" />

<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style&logo=Pytest&logoColor=white" alt="Pytest" />
<img src="https://img.shields.io/badge/Ray-028CF0.svg?style&logo=Ray&logoColor=white" alt="Ray" />
<img src="https://img.shields.io/badge/MLflow-0194E2.svg?style&logo=MLflow&logoColor=white" alt="MLflow" />
<img src="https://img.shields.io/badge/NumPy-013243.svg?style&logo=NumPy&logoColor=white" alt="NumPy" />
<img src="https://img.shields.io/badge/FastAPI-009688.svg?style&logo=FastAPI&logoColor=white" alt="FastAPI" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
</p>
<img src="https://img.shields.io/github/languages/top/GokuMohandas/mlops-course?style&color=5D6D7E" alt="GitHub top language" />
<img src="https://img.shields.io/github/languages/code-size/GokuMohandas/mlops-course?style&color=5D6D7E" alt="GitHub code size in bytes" />
<img src="https://img.shields.io/github/commit-activity/m/GokuMohandas/mlops-course?style&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/license/GokuMohandas/mlops-course?style&color=5D6D7E" alt="GitHub license" />
</div>

---

## 📖 Table of Contents
- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [⚙️ Modules](#modules)
- [🚀 Getting Started](#-getting-started)
    - [🔧 Installation](#-installation)
    - [🤖 Running mlops-course](#-running-mlops-course)
    - [🧪 Tests](#-tests)
- [🛣 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The project "Made With ML" is a comprehensive resource for machine learning practitioners. It offers functionalities for data preprocessing, model training and evaluation, hyperparameter tuning, prediction serving, and documentation generation. The project's core value proposition lies in providing a streamlined workflow, with distributed computing capabilities and integration with popular libraries like PyTorch and Transformers. It also offers easy deployment on cloud platforms like AWS and AnyScale, enhancing scalability and accessibility for machine learning projects.

---

## 📦 Features

| Feature                | Description                           |
| ---------------------- | ------------------------------------- |
| **⚙️ Architecture**     | The codebase follows a modular architecture, with separate files for different functionalities such as data loading/preprocessing, model training, evaluation, prediction, and serving. It also utilizes a distributed training approach using Ray, Torch, and Transformers. The codebase is designed to be scalable, allowing for easy addition of new features or updates. Limit your response to a maximum of 250 characters. |
| **📃 Documentation**   | The documentation in the codebase is comprehensive and well-structured. It includes a configuration file for the website, dependencies, Makefile for code styling and cleaning, and a pyproject.toml file for code consistency and quality. It also provides detailed explanations and examples for each file, function, and class. Limit your response to a maximum of 250 characters. |
| **🔗 Dependencies**    | The codebase has a wide range of dependencies tailored for different purposes such as core machine learning libraries, natural language processing, data analysis, documentation generation, code formatting, testing, web development, and deployment. These dependencies are listed in the requirements.txt file and are installed using pip. Limit your response to a maximum of 250 characters. |
| **🧩 Modularity**      | The codebase demonstrates good modularity, with separate files for different functionalities and separate directories for deployment, services, and models. Each file focuses on a specific task and can be easily reused or replaced. The use of functions and classes also contributes to the modularity, allowing for easy customization and extension. Limit your response to a maximum of 250 characters. |
| **🧪 Testing**          | The codebase includes testing as part of its development process. It uses pytest and pytest-cov for testing and capturing test coverage. The tests cover different aspects such as data loading, model training, evaluation, prediction, and serving. The testing strategy ensures that the code functions as expected and helps maintain code quality. Limit your response to a maximum of 250 characters. |
| **⚡️ Performance**      | The codebase leverages distributed training using Ray, Torch, and Transformers to improve performance and speed up training processes. It also includes optimizations like data preprocessing, batch processing, and GPU utilization for better resource usage and efficiency. The use of MLflow for logging and checkpointing helps monitor and improve performance. Limit your response to a maximum of 250 characters. |
| **🔐 Security**        | The codebase doesn't explicitly address security measures. However, it is worth noting that security is a broad and complex topic that may require additional considerations depending on the deployment environment and use case. Limit your response to a maximum of 250 characters. |
| **🔀 Version Control** | The codebase effectively utilizes Git for version control. It is hosted on GitHub, allowing collaborative development and easy tracking of changes. The use of meaningful commit messages, branches, and pull requests demonstrates good version control practices. Limit your response to a maximum of 250 characters. |
| **🔌 Integrations**    | The codebase integrates with several external systems and services. It uses Docker for environment setup, AWS for cloud deployment and cluster management, AnyScale for serving the machine learning model, and Ray for distributed training. It also interacts with MLflow for logging and checkpointing, and S3 for data and model

---


## 📂 Repository Structure


```bash
repo
├── LICENSE
├── Makefile
├── README.md
├── datasets
│   ├── dataset.csv
│   ├── holdout.csv
│   ├── projects.csv
│   └── tags.csv
├── deploy
│   ├── cluster_compute.yaml
│   ├── cluster_env.yaml
│   ├── jobs
│   │   ├── workloads.sh
│   │   └── workloads.yaml
│   └── services
│       ├── serve_model.py
│       └── serve_model.yaml
├── docs
│   ├── index.md
│   └── madewithml
│       ├── data.md
│       ├── evaluate.md
│       ├── models.md
│       ├── predict.md
│       ├── serve.md
│       ├── train.md
│       ├── tune.md
│       └── utils.md
├── madewithml
│   ├── config.py
│   ├── data.py
│   ├── evaluate.py
│   ├── models.py
│   ├── predict.py
│   ├── serve.py
│   ├── train.py
│   ├── tune.py
│   └── utils.py
├── mkdocs.yml
├── notebooks
│   ├── benchmarks.ipynb
│   └── madewithml.ipynb
├── pyproject.toml
├── requirements.txt
└── tests
    ├── code
    │   ├── conftest.py
    │   ├── test_data.py
    │   ├── test_predict.py
    │   ├── test_train.py
    │   ├── test_tune.py
    │   ├── test_utils.py
    │   └── utils.py
    ├── data
    │   ├── conftest.py
    │   └── test_dataset.py
    └── model
        ├── conftest.py
        ├── test_behavioral.py
        └── utils.py

13 directories, 48 files
```

---

## ⚙️ Modules

<details closed><summary>Root</summary>

| File                                                                                        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---                                                                                         | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [mkdocs.yml](https://github.com/GokuMohandas/mlops-course/blob/main/mkdocs.yml)             | This code defines the core functionalities of a website called "Made With ML." It includes navigation links, a theme, plugins, and a watch feature to reload the documentation for any file changes. The website provides resources related to machine learning, including data, models, training, tuning, evaluation, prediction, serving, and utilities. The code is hosted on GitHub.                                                                                                                                                                                                                |
| [requirements.txt](https://github.com/GokuMohandas/mlops-course/blob/main/requirements.txt) | This code includes a variety of dependencies for different purposes:-Default: Core libraries and frameworks for machine learning, natural language processing, and data analysis.-Notebook: Additional libraries for interactive notebooks and data visualization.-Documentation: Tools for generating documentation for the codebase.-Styling: Libraries for code formatting and style enforcement.-Testing: Libraries for testing and asserting expectations.-Development: Libraries for web development and command-line interface.-Deployment: Libraries for deploying code on distributed systems. |
| [Makefile](https://github.com/GokuMohandas/mlops-course/blob/main/Makefile)                 | The code is a Makefile that provides commands for code styling and cleaning. The "style" command formats the code using black, checks for linting errors with flake8, sorts imports with isort, and upgrades code with pyupgrade. The "clean" command removes unnecessary files and directories.                                                                                                                                                                                                                                                                                                        |
| [pyproject.toml](https://github.com/GokuMohandas/mlops-course/blob/main/pyproject.toml)     | The code includes configurations for formatting (black), import sorting (isort), linting (flake8), upgrading to Python 3.9+ compatibility (pyupgrade), and test coverage (pytest cov). It aims to ensure code consistency, readability, and quality.                                                                                                                                                                                                                                                                                                                                                    |

</details>

<details closed><summary>Deploy</summary>

| File                                                                                                       | Summary                                                                                                                                                                                                                  |
| ---                                                                                                        | ---                                                                                                                                                                                                                      |
| [cluster_env.yaml](https://github.com/GokuMohandas/mlops-course/blob/main/deploy/cluster_env.yaml)         | This code snippet sets up a Docker environment with a specific base image and necessary dependencies. It installs Python packages, updates pip and installs packages specified in a requirements.txt file.               |
| [cluster_compute.yaml](https://github.com/GokuMohandas/mlops-course/blob/main/deploy/cluster_compute.yaml) | The code defines the core functionalities for deploying a cluster on the AWS cloud. It specifies the region, instance types for head and worker nodes, and other AWS configurations like block device mappings and tags. |

</details>

<details closed><summary>Jobs</summary>

| File                                                                                                | Summary                                                                                                                                                                                                                                                                 |
| ---                                                                                                 | ---                                                                                                                                                                                                                                                                     |
| [workloads.yaml](https://github.com/GokuMohandas/mlops-course/blob/main/deploy/jobs/workloads.yaml) | The code defines a set of workloads to be executed on a specified cluster. It includes project details, cluster environment, compute configuration, runtime environment, and the entry point script. It also specifies the maximum number of retries for the workloads. |
| [workloads.sh](https://github.com/GokuMohandas/mlops-course/blob/main/deploy/jobs/workloads.sh)     | This code performs a series of tasks including testing data and code, training a model, evaluating the model, testing the trained model, and saving the model and results to S3.                                                                                        |

</details>

<details closed><summary>Services</summary>

| File                                                                                                        | Summary                                                                                                                          |
| ---                                                                                                         | ---                                                                                                                              |
| [serve_model.yaml](https://github.com/GokuMohandas/mlops-course/blob/main/deploy/services/serve_model.yaml) | HTTPStatus Exception: 503                                                                                                        |
| [serve_model.py](https://github.com/GokuMohandas/mlops-course/blob/main/deploy/services/serve_model.py)     | The code imports necessary modules, copies files from S3, and sets an entrypoint for model deployment based on given parameters. |

</details>

<details closed><summary>Madewithml</summary>

| File                                                                                         | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---                                                                                          | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [config.py](https://github.com/GokuMohandas/mlops-course/blob/main/madewithml/config.py)     | This code provides the core functionalities for configuration and logging in a Python project. It sets up directories, configures MLflow, initializes logging, and defines a list of stopwords. The logging configuration includes console and file handlers for different log levels.                                                                                                                                                                                                       |
| [models.py](https://github.com/GokuMohandas/mlops-course/blob/main/madewithml/models.py)     | This code defines a PyTorch model for fine-tuning a Large Language Model (LLM). The model takes input sequences and masks, passes them through the LLM, applies dropout regularization, and then passes the pooled output through a linear layer to obtain the final predictions.                                                                                                                                                                                                            |
| [predict.py](https://github.com/GokuMohandas/mlops-course/blob/main/madewithml/predict.py)   | This code provides functionalities for predicting tags based on input data using a pre-trained model. It includes methods for decoding indices to labels, formatting probabilities, and making predictions with probabilities. It also includes functions for retrieving the best run ID and best checkpoint from an MLflow experiment. The main predict() function takes a specific run ID, project title, and description as inputs and returns the prediction results for the input data. |
| [serve.py](https://github.com/GokuMohandas/mlops-course/blob/main/madewithml/serve.py)       | This code defines a FastAPI application for serving a machine learning model. It includes routes for health check, evaluation, and prediction. The model is loaded using a run ID and a threshold is applied to classify predictions. Ray is used for distributed serving.                                                                                                                                                                                                                   |
| [utils.py](https://github.com/GokuMohandas/mlops-course/blob/main/madewithml/utils.py)       | This code includes functions for setting seeds, loading and saving dictionaries as JSON files, padding arrays, converting batches of numpy arrays to tensors, retrieving MLflow run IDs, and converting dictionaries to a list of dictionaries.                                                                                                                                                                                                                                              |
| [tune.py](https://github.com/GokuMohandas/mlops-course/blob/main/madewithml/tune.py)         | This code defines a command-line interface (CLI) app for hyperparameter tuning experiments using Ray and Tune. It sets up the necessary configurations, datasets, trainers, and search algorithms for hyperparameter optimization. The results of the tuning experiment are logged using MLflow and saved to a file if specified. The code also includes a main function to initialize Ray and run the CLI app.                                                                              |
| [train.py](https://github.com/GokuMohandas/mlops-course/blob/main/madewithml/train.py)       | This code defines a distributed training workload using Ray, Torch, and Transformers for training a language model.The code implements functions for training and evaluating the model, as well as a distributed training loop.It also includes CLI options for configuring the training workload.The code uses MLflow for logging and checkpointing, and supports distributed training with multiple workers and GPUs.                                                                      |
| [evaluate.py](https://github.com/GokuMohandas/mlops-course/blob/main/madewithml/evaluate.py) | This code includes functions for evaluating the performance of a model on a dataset. It calculates overall metrics, per class metrics, and metrics for different slices of the data. The evaluation results can be saved to a file if specified.                                                                                                                                                                                                                                             |
| [data.py](https://github.com/GokuMohandas/mlops-course/blob/main/madewithml/data.py)         | This code contains several core functionalities. It includes functions for loading data into a Ray Dataset, stratified splitting of datasets, text cleaning, tokenization using a pre-trained BERT tokenizer, and data preprocessing. There is also a custom preprocessor class that fits and transforms the data.                                                                                                                                                                           |

</details>

<details closed><summary>Workflows</summary>

| File                                                                                                              | Summary                                                                                                                                                                                                                                                                                                              |
| ---                                                                                                               | ---                                                                                                                                                                                                                                                                                                                  |
| [serve.yaml](https://github.com/GokuMohandas/mlops-course/blob/main/.github/workflows/serve.yaml)                 | The code sets up AWS credentials, installs dependencies, and serves a machine learning model using AnyScale.                                                                                                                                                                                                         |
| [json_to_md.py](https://github.com/GokuMohandas/mlops-course/blob/main/.github/workflows/json_to_md.py)           | This code converts a JSON file to a formatted markdown file. It reads the JSON data, converts it to markdown format, and saves it to a file. The `to_markdown` function handles the conversion, and the `json_to_markdown` function orchestrates the process. The code also includes command-line argument handling. |
| [workloads.yaml](https://github.com/GokuMohandas/mlops-course/blob/main/.github/workflows/workloads.yaml)         | The code sets up AWS credentials, installs dependencies, runs workloads, reads results from S3, and comments them on a pull request.                                                                                                                                                                                 |
| [documentation.yaml](https://github.com/GokuMohandas/mlops-course/blob/main/.github/workflows/documentation.yaml) | The code is a GitHub Actions workflow that builds and deploys documentation using MkDocs. It sets up Python dependencies, installs MkDocs and mkdocstrings, and then deploys the documentation using the "mkdocs gh-deploy" command.                                                                                 |

</details>

<details closed><summary>Notebooks</summary>

| File                                                                                                  | Summary                                 |
| ---                                                                                                   | ---                                     |
| [benchmarks.ipynb](https://github.com/GokuMohandas/mlops-course/blob/main/notebooks/benchmarks.ipynb) | Prompt exceeds max token limit: 4000.   |
| [madewithml.ipynb](https://github.com/GokuMohandas/mlops-course/blob/main/notebooks/madewithml.ipynb) | Prompt exceeds max token limit: 218014. |

</details>

---

## 🚀 Getting Started

***Dependencies***

Before you begin, ensure that you have the following prerequisites installed:
> - `ℹ️ Requirement 1`
> - `ℹ️ Requirement 2`
> - `ℹ️ ...`

### 🔧 Installation

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

```sh
python main.py
```

### 🧪 Tests
```sh
pytest
```

---


## 🛣 Roadmap

> - [X] `ℹ️  Task 1: Implement X`
> - [ ] `ℹ️  Task 2: Refactor Y`
> - [ ] `ℹ️ ...`


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
7. Create a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 📄 License

This project is licensed under the `ℹ️  INSERT-LICENSE-TYPE` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 👏 Acknowledgments

> - `ℹ️  List any resources, contributors, inspiration, etc.`

---
