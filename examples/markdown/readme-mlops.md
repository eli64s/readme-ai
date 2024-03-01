<p align="center">
  <img src="https://img.icons8.com/?size=512&id=55494&format=png" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">MLOPS-COURSE</h1>
</p>
<p align="center">
    <em>Streamline Your MLOps Journey with Automation</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/GokuMohandas/mlops-course?style=flat&logo=opensourceinitiative&logoColor=white&color=blueviolet" alt="license">
	<img src="https://img.shields.io/github/last-commit/GokuMohandas/mlops-course?style=flat&logo=git&logoColor=white&color=blueviolet" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/GokuMohandas/mlops-course?style=flat&color=blueviolet" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/GokuMohandas/mlops-course?style=flat&color=blueviolet" alt="repo-language-count">
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

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>

- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [🧩 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
  - [⚙️ Install](#️-install)
  - [► Using mlops-course](#-using-mlops-course)
  - [🧪 Tests](#-tests)
- [🛠 Project Roadmap](#-project-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)
</details>
<hr>

## 📍 Overview

The mlops-course project automates model training and hyperparameter tuning for optimizing machine learning models. It enhances model performance reliably by utilizing hyperopt. The repository includes styling and cleaning tasks for code consistency, cluster computing environment configurations, and deployment scripts for managing workloads and serving models using FastAPI. Key components such as logging configurations, data handling utilities, and distributed model training with PyTorch and BERT are integrated into the project. The deployment is facilitated on Kubernetes clusters with YAML configurations, making model deployment and serving scalable and efficient.

---

## 📦 Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | The project follows a modular architecture with components for model training, evaluation, and serving using Ray, PyTorch, and FastAPI. It supports distributed computing for adaptive training and deployment.|
| 🔩 | **Code Quality**  | The codebase maintains high code quality standards with automated formatting (Black, iSort), linting (Flake8), and testing (Pytest). Pre-commit hooks enforce code consistency, ensuring clean and reliable code.|
| 📄 | **Documentation** | Extensive documentation covering setup, usage, and codebase details is available. README files, inline comments, and docs generation using MkDocs ensure clear and comprehensive documentation.|
| 🔌 | **Integrations**  | Key integrations include MLflow for experiment tracking, GitHub Actions for CI/CD automation, and deployment with Ray for distributed computing. External dependencies like Transformers and Snorkel enhance model capabilities.|
| 🧩 | **Modularity**    | The codebase is highly modular, facilitating code reusability and maintainability. Various modules handle tasks such as data loading, model training, evaluation, and serving, allowing for easy extension and customization.|
| 🧪 | **Testing**       | Testing is thorough with Pytest covering unit and integration tests. Code coverage is tracked using pytest-cov ensuring reliable software quality.|
| ⚡️  | **Performance**   | The project emphasizes efficiency and speed with distributed training capabilities using Ray and optimized model architectures with PyTorch. It focuses on resource utilization to enhance performance.|
| 🛡️ | **Security**      | Security measures include secure user authentication and adherence to best practices for data protection. The project maintains data integrity and access control for sensitive information.|
| 📦 | **Dependencies**  | Key external libraries such as scikit-learn, transformers, and mlflow are utilized for machine learning tasks. Tools like Flask and FastAPI support web server functionalities.|

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

| File                                                                                          | Summary                                                                                                                                                                                 |
| ---                                                                                           | ---                                                                                                                                                                                     |
| [requirements.txt](https://github.com/GokuMohandas/mlops-course/blob/master/requirements.txt) | Automate model training hyperparameter tuning using hyperopt for optimizing ML models. Helps enhance model performance reliably in the MLOps course project.                            |
| [Makefile](https://github.com/GokuMohandas/mlops-course/blob/master/Makefile)                 | Styling and cleaning tasks for the repository, ensuring code consistency, and removing unnecessary files for efficient maintenance.                                                     |
| [pyproject.toml](https://github.com/GokuMohandas/mlops-course/blob/master/pyproject.toml)     | Manages code formatting with Black, iSort, and Flake8, ensuring clean, consistent code across the repository while excluding common directories and specific files for Pytest coverage. |

</details>

<details closed><summary>deploy</summary>

| File                                                                                                         | Summary                                                                                                                                                                              |
| ---                                                                                                          | ---                                                                                                                                                                                  |
| [cluster_env.yaml](https://github.com/GokuMohandas/mlops-course/blob/master/deploy/cluster_env.yaml)         | Configure cluster computing environment for Ray with post-build Python package installations.                                                                                        |
| [cluster_compute.yaml](https://github.com/GokuMohandas/mlops-course/blob/master/deploy/cluster_compute.yaml) | Manages cloud resources for madewithml deployment in us-east2, specifying head and worker node types with their configurations.Intialized BlockDeviceMappings and TagSpecifications. |

</details>

<details closed><summary>deploy.jobs</summary>

| File                                                                                                  | Summary                                                                                                                         |
| ---                                                                                                   | ---                                                                                                                             |
| [workloads.yaml](https://github.com/GokuMohandas/mlops-course/blob/master/deploy/jobs/workloads.yaml) | Manages workloads in the cluster environment for a specific project, handling configurations and runtime environment variables. |
| [workloads.sh](https://github.com/GokuMohandas/mlops-course/blob/master/deploy/jobs/workloads.sh)     | Automates testing, training, evaluating, and deploying machine learning models on MadeWithML platform.                          |

</details>

<details closed><summary>deploy.services</summary>

| File                                                                                                          | Summary                                                                                                                          |
| ---                                                                                                           | ---                                                                                                                              |
| [serve_model.yaml](https://github.com/GokuMohandas/mlops-course/blob/master/deploy/services/serve_model.yaml) | Serve a Machine Learning model with Ray for madewithml project, defining runtime environment, upload path, and rollout strategy. |
| [serve_model.py](https://github.com/GokuMohandas/mlops-course/blob/master/deploy/services/serve_model.py)     | Serves model deployment by fetching artifacts from S3 and configuring the entrypoint based on run ID and threshold.              |

</details>

<details closed><summary>madewithml</summary>

| File                                                                                           | Summary                                                                                                                                                                                                                                                                            |
| ---                                                                                            | ---                                                                                                                                                                                                                                                                                |
| [config.py](https://github.com/GokuMohandas/mlops-course/blob/master/madewithml/config.py)     | Manages logging configuration and MLflow setup within the project, sets up directories, logger, and constraints for effective tracking and monitoring.                                                                                                                             |
| [models.py](https://github.com/GokuMohandas/mlops-course/blob/master/madewithml/models.py)     | Defines a finetuned Large Language Model (LLM) module for fine-tuning. Inherits LLM and adds dropout and classification layers.                                                                                                                                                    |
| [predict.py](https://github.com/GokuMohandas/mlops-course/blob/master/madewithml/predict.py)   | Predict tags and probabilities for project titles and descriptions using MLflow experiments and TorchPredictor.                                                                                                                                                                    |
| [serve.py](https://github.com/GokuMohandas/mlops-course/blob/master/madewithml/serve.py)       | FastAPI application serving a machine learning model for project classification with health check, run ID retrieval, evaluation, and prediction endpoints.                                                                                                                         |
| [utils.py](https://github.com/GokuMohandas/mlops-course/blob/master/madewithml/utils.py)       | Utility functions for reproducible experimentation, data handling, array padding, and tensor conversion within the AI/ML workflow. Includes setting seeds, loading/saving dictionaries, array padding, collating batch data, converting dict to list, and fetching MLflow run IDs. |
| [tune.py](https://github.com/GokuMohandas/mlops-course/blob/master/madewithml/tune.py)         | defines CLI, configures tuning workload, conducts training, and logs results.                                                                                                                                                                                                      |
| [train.py](https://github.com/GokuMohandas/mlops-course/blob/master/madewithml/train.py)       | Train a distributed model using Ray for adaptive training and evaluation, leveraging PyTorch and BERT.CLI app enables training config setup and result saving.                                                                                                                     |
| [evaluate.py](https://github.com/GokuMohandas/mlops-course/blob/master/madewithml/evaluate.py) | CLI script to evaluate model performance metrics on datasets, showcasing overall and per-class results alongside slice metrics for NLP projects.                                                                                                                                   |
| [data.py](https://github.com/GokuMohandas/mlops-course/blob/master/madewithml/data.py)         | Handles dataset loading, stratified split, text cleaning, and tokenization. Includes a custom preprocessor for data transformation.                                                                                                                                                |

</details>

<details closed><summary>.github.workflows</summary>

| File                                                                                                                | Summary                                                                                                                                                         |
| ---                                                                                                                 | ---                                                                                                                                                             |
| [serve.yaml](https://github.com/GokuMohandas/mlops-course/blob/master/.github/workflows/serve.yaml)                 | GitHub Actions workflow** for serving model predictions using API endpoints. Implements fast and scalable prediction serving infrastructure.                    |
| [json_to_md.py](https://github.com/GokuMohandas/mlops-course/blob/master/.github/workflows/json_to_md.py)           | Converts JSON data to Markdown format for project documentation.                                                                                                |
| [workloads.yaml](https://github.com/GokuMohandas/mlops-course/blob/master/.github/workflows/workloads.yaml)         | CI/CD workflows for model training, evaluation, and deployment using GitHub Actions. Automates the pipeline to build, test, and deploy machine learning models. |
| [documentation.yaml](https://github.com/GokuMohandas/mlops-course/blob/master/.github/workflows/documentation.yaml) | Generates documentation for the MLOps course repository using GitHub Actions workflow.                                                                          |

</details>

<details closed><summary>notebooks</summary>

| File                                                                                                    | Summary                                                                                                                                                                |
| ---                                                                                                     | ---                                                                                                                                                                    |
| [benchmarks.ipynb](https://github.com/GokuMohandas/mlops-course/blob/master/notebooks/benchmarks.ipynb) | This code snippet facilitates secure user authentication within the parent repository's system architecture, enhancing overall system reliability and data protection. |
| [madewithml.ipynb](https://github.com/GokuMohandas/mlops-course/blob/master/notebooks/madewithml.ipynb) | Code SummaryManages deployment for ML model training on Kubernetes cluster using YAML configurations in the `deploy` directory.                                        |

</details>

---

## 🚀 Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Python**: `version x.y.z`

### ⚙️ Install

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

### ► Using `mlops-course`

Use the following command to run mlops-course:

```sh
python main.py
```

### 🧪 Tests

Use the following command to run tests:

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

- **[Report Issues](https://github.com/GokuMohandas/mlops-course/issues)**: Submit bugs found or log feature requests for the `mlops-course` project.
- **[Submit Pull Requests](https://github.com/GokuMohandas/mlops-course/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/GokuMohandas/mlops-course/discussions)**: Share your insights, provide feedback, or ask questions.

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
<p align="center">
   <a href="https://github.com{/GokuMohandas/mlops-course/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=GokuMohandas/mlops-course">
   </a>
</p>
</details>

---

## 📄 License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 👏 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-overview)

---
