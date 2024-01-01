<div align="center">
   <h1>
      <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" alt="Markdown" width="100" height="100" id="markdown">
      <br>
      MLOPS-COURSE
   </h1>
   <h3>◦ Transforming ML Ops with MLOps Course+</h3>
   <h3>◦ Developed with the software and tools below.</h3>

<p align="center">
      <img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat-square&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
<img src="https://img.shields.io/badge/precommit-FAB040.svg?style=flat-square&logo=pre-commit&logoColor=black" alt="precommit">
<img src="https://img.shields.io/badge/scikitlearn-F7931E.svg?style=flat-square&logo=scikit-learn&logoColor=white" alt="scikitlearn">
<img src="https://img.shields.io/badge/Jupyter-F37626.svg?style=flat-square&logo=Jupyter&logoColor=white" alt="Jupyter">
<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat-square&logo=YAML&logoColor=white" alt="YAML">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=flat-square&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions">

<img src="https://img.shields.io/badge/pandas-150458.svg?style=flat-square&logo=pandas&logoColor=white" alt="pandas">
<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat-square&logo=Pytest&logoColor=white" alt="Pytest">
<img src="https://img.shields.io/badge/Ray-028CF0.svg?style=flat-square&logo=Ray&logoColor=white" alt="Ray">
<img src="https://img.shields.io/badge/MLflow-0194E2.svg?style=flat-square&logo=MLflow&logoColor=white" alt="MLflow">
<img src="https://img.shields.io/badge/NumPy-013243.svg?style=flat-square&logo=NumPy&logoColor=white" alt="NumPy">
<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=flat-square&logo=FastAPI&logoColor=white" alt="FastAPI">
   </p>
   <img src="https://img.shields.io/github/license/GokuMohandas/mlops-course?style=flat-square&color=blue" alt="license">
   <img src="https://img.shields.io/github/last-commit/GokuMohandas/mlops-course?style=flat-square&color=blue" alt="last-commit">
   <img src="https://img.shields.io/github/stars/GokuMohandas/mlops-course?style=flat-square&color=blue" alt="stars">
   <img src="https://img.shields.io/github/v/release/GokuMohandas/mlops-course?style=flat-square&color=blue" alt="release-version">
</div>

---

##  Quick Links
- [ Quick Links](#-quick-links)
- [ Overview](#-overview)
- [ Features](#-features)
- [ Repository Structure](#-repository-structure)
- [ Modules](#modules)
- [ Getting Started](#-getting-started)
    - [ Installation](#-installation)
    - [ Running mlops-course](#-running-mlops-course)
    - [ Tests](#-tests)
- [ Roadmap](#-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

---

##  Overview

The mlops-course codebase is a comprehensive project that aims to provide a hands-on learning experience for mastering Machine Learning Operations (MLOps) concepts. This project emphasizes the seamless integration of ML workflows and deployment pipelines. With a focus on reproducibility and scalability, it incorporates various tools and libraries such as hyperopt, mlflow, snorkel, and transformers. The codebase enables users to efficiently experiment with different ML models, optimize hyperparameters, track experiments, and deploy models in a production-ready manner. By providing a step-by-step guide and examples, this project equips users with the necessary skills to implement end-to-end MLOps pipelines effectively.

---

##  Features

|    | Feature           | Description                                                                                                       |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**    | The codebase follows a modular, component-based architecture using Python's Flask framework. The system is loosely coupled and follows the Model-View-Controller (MVC) design pattern. |
| 📄 | **Documentation**  | The codebase has comprehensive documentation, including README files for each project component, providing information on installation, usage, and configuration. |
| 🔗 | **Dependencies**   | The system relies on several external libraries, such as Flask, NumPy, Pandas, scikit-learn, SQLAlchemy, and Docker, among others. It also utilizes Docker containers for deployment. |
| 🧩 | **Modularity**     | The system is well-organized into smaller, reusable components, such as data preprocessing, model training, serving predictions, and monitoring. Each component has its own designated folder and files. |
| 🧪 | **Testing**        | The codebase includes unit tests and integration tests using the pytest framework. It also utilizes continuous integration (CI) with GitHub Actions for automated testing. |
| ⚡️ | **Performance**     | The system's performance is optimized through the use of efficient algorithms, caching mechanisms, and parallel processing for data transformations. It also utilizes GPU acceleration for model training. |
| 🔐 | **Security**       | The codebase implements secure practices, such as input validation, authentication, and authorization. It also leverages environment variables for sensitive information and follows data encryption standards. |
| 🔀 | **Version Control**| The system utilizes Git and GitHub for version control, allowing for easy collaboration, code review, and tracking of code changes. It follows a branching strategy and includes clear commit messages. |


---

##  Repository Structure

```sh
└── mlops-course/
    ├── .github/
    │   └── workflows/
    │       ├── documentation.yaml
    │       ├── json_to_md.py
    │       ├── serve.yaml
    │       └── workloads.yaml
    ├── Makefile
    ├── datasets/
    ├── deploy/
    │   ├── cluster_compute.yaml
    │   ├── cluster_env.yaml
    │   ├── jobs/
    │   │   ├── workloads.sh
    │   │   └── workloads.yaml
    │   └── services/
    │       ├── serve_model.py
    │       └── serve_model.yaml
    ├── madewithml/
    │   ├── config.py
    │   ├── data.py
    │   ├── evaluate.py
    │   ├── models.py
    │   ├── predict.py
    │   ├── serve.py
    │   ├── train.py
    │   ├── tune.py
    │   └── utils.py
    ├── notebooks/
    │   ├── benchmarks.ipynb
    │   └── madewithml.ipynb
    ├── pyproject.toml
    ├── requirements.txt

```

---

##  Modules

<details closed><summary>.</summary>

| File                                                                                        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---                                                                                         | ---                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [requirements.txt](https://github.com/GokuMohandas/mlops-course/blob/main/requirements.txt) | The code snippet in the `serve.py` file within the `madewithml` directory is responsible for serving a trained machine learning model. It utilizes the `fastapi` library to create a web API endpoint that accepts input data and returns predictions from the model. This file plays a critical role in the repository's architecture as it enables the deployment and usage of the trained model in a production environment. |
| [Makefile](https://github.com/GokuMohandas/mlops-course/blob/main/Makefile)                 | The Makefile in the codebase is responsible for styling and cleaning operations. It uses tools like black, flake8, and isort for code formatting and removes unnecessary files like.DS_Store and.pyc.                                                                                                                                                                                                                           |
| [pyproject.toml](https://github.com/GokuMohandas/mlops-course/blob/main/pyproject.toml)     | This code snippet is part of a larger repository with a specific directory structure. It includes key files for code formatting, dependency management, and testing. The codebase utilizes various tools and software for development and testing purposes.                                                                                                                                                                     |

</details>

<details closed><summary>deploy</summary>

| File                                                                                                       | Summary                                                                                                                                                                                                                                               |
| ---                                                                                                        | ---                                                                                                                                                                                                                                                   |
| [cluster_env.yaml](https://github.com/GokuMohandas/mlops-course/blob/main/deploy/cluster_env.yaml)         | This code snippet is part of the MLOps course repository and is responsible for setting up the necessary environment for deploying the cluster. It installs required packages and dependencies for the deployment process.                            |
| [cluster_compute.yaml](https://github.com/GokuMohandas/mlops-course/blob/main/deploy/cluster_compute.yaml) | This code snippet, located in the `deploy/cluster_compute.yaml` file, defines the configuration for the cluster compute resources used in the software's deployment. It specifies the instance types, storage volume, and tags for the compute nodes. |

</details>

<details closed><summary>deploy.jobs</summary>

| File                                                                                                | Summary                                                                                                                                                                                                                                                                                                                                             |
| ---                                                                                                 | ---                                                                                                                                                                                                                                                                                                                                                 |
| [workloads.yaml](https://github.com/GokuMohandas/mlops-course/blob/main/deploy/jobs/workloads.yaml) | This code snippet, located in the `deploy/jobs/workloads.yaml` file, defines the configuration for executing the `workloads.sh` script within the parent repository's deployment environment. It specifies the project ID, cluster environment, compute configuration, runtime environment, and other parameters required for successful execution. |
| [workloads.sh](https://github.com/GokuMohandas/mlops-course/blob/main/deploy/jobs/workloads.sh)     | The code snippet in `deploy/jobs/workloads.sh` is responsible for executing various tasks such as testing data and code, training models, evaluating and testing models, and saving results to S3. It sets up environment variables and runs commands using `pytest` and Python scripts from the `madewithml` directory.                            |

</details>

<details closed><summary>deploy.services</summary>

| File                                                                                                        | Summary                                                                                                                                                                                                                                                                     |
| ---                                                                                                         | ---                                                                                                                                                                                                                                                                         |
| [serve_model.yaml](https://github.com/GokuMohandas/mlops-course/blob/main/deploy/services/serve_model.yaml) | This code snippet, found in the `deploy/services/serve_model.yaml` file, sets up the configuration for serving the model in the `madewithml` project. It specifies the import path, runtime environment, upload path, and other parameters necessary for serving the model. |
| [serve_model.py](https://github.com/GokuMohandas/mlops-course/blob/main/deploy/services/serve_model.py)     | The code snippet in the `serve_model.py` file is responsible for copying ML models and results from an S3 bucket and setting the entrypoint for model deployment. It uses the AWS CLI and the `ModelDeployment` class from the `madewithml` module.                         |

</details>

<details closed><summary>madewithml</summary>

| File                                                                                         | Summary                                                                                                                                                                                                                                                                                                                                                                      |
| ---                                                                                          | ---                                                                                                                                                                                                                                                                                                                                                                          |
| [config.py](https://github.com/GokuMohandas/mlops-course/blob/main/madewithml/config.py)     | This code snippet is the `config.py` file in the `madewithml` directory of the repository. It configures logging and sets up the MLflow tracking URI. It also defines a list of stopwords.                                                                                                                                                                                   |
| [models.py](https://github.com/GokuMohandas/mlops-course/blob/main/madewithml/models.py)     | This code snippet defines a finetuned Large Language Model (LLM) architecture using PyTorch. It takes in input data, passes it through the LLM model, applies dropout, and outputs predictions. It is part of the madewithml repository, which contains various modules and functionalities related to machine learning.                                                     |
| [predict.py](https://github.com/GokuMohandas/mlops-course/blob/main/madewithml/predict.py)   | This code snippet is a command-line tool that uses MLflow to predict tags for projects based on their title and description. It loads the best checkpoint from a specific MLflow run and uses it to make predictions using a pre-trained Torch model. The results are logged and returned as a dictionary.                                                                   |
| [serve.py](https://github.com/GokuMohandas/mlops-course/blob/main/madewithml/serve.py)       | The code snippet in `madewithml/serve.py` implements a FastAPI application for serving a machine learning model. It provides endpoints for health checks, evaluating data, and making predictions. The model is loaded from a saved checkpoint and applied on incoming data. It uses Ray's serving framework for deployment.                                                 |
| [utils.py](https://github.com/GokuMohandas/mlops-course/blob/main/madewithml/utils.py)       | This code snippet provides utility functions for data preprocessing and manipulation in the parent repository. It includes functions for setting seeds, loading and saving dictionaries, padding arrays, and converting data structures. These functions are used in various modules for data preparation and handling.                                                      |
| [tune.py](https://github.com/GokuMohandas/mlops-course/blob/main/madewithml/tune.py)         | The code snippet is a CLI command for running a hyperparameter tuning experiment using the Tune library. It loads a dataset, defines a search space for hyperparameters, sets up a trainer, and runs the tuning process using the specified configuration. The results are logged and optionally saved to a file.                                                            |
| [train.py](https://github.com/GokuMohandas/mlops-course/blob/main/madewithml/train.py)       | The `train.py` file in the `madewithml` directory of the repository is responsible for training a model using distributed computing. It defines functions for training and evaluating the model, as well as a command-line interface for starting the training process. The file also includes functionality for setting up the training environment and saving the results. |
| [evaluate.py](https://github.com/GokuMohandas/mlops-course/blob/main/madewithml/evaluate.py) | The `evaluate.py` file in the `madewithml` directory provides functions for evaluating the performance of a machine learning model. It calculates overall metrics, per class metrics, and slice metrics using precision, recall, and F1 score. It takes in a dataset with labels, loads a trained model, and returns the evaluation results.                                 |
| [data.py](https://github.com/GokuMohandas/mlops-course/blob/main/madewithml/data.py)         | The code snippet is responsible for loading, splitting, cleaning, and preprocessing data for a machine learning model. It includes functions for loading data from a source, stratified splitting, cleaning and tokenizing text, and preprocessing a dataframe. These functions are crucial for data preparation in the parent repository's machine learning workflow.       |

</details>

<details closed><summary>.github.workflows</summary>

| File                                                                                                              | Summary                                                                                                                                                                                                                                                                                                                    |
| ---                                                                                                               | ---                                                                                                                                                                                                                                                                                                                        |
| [serve.yaml](https://github.com/GokuMohandas/mlops-course/blob/main/.github/workflows/serve.yaml)                 | The code snippet is part of the parent repository's architecture and its main role is to serve a machine learning model. It configures AWS credentials, sets up dependencies, and uses Anyscale to rollout the model as a service.                                                                                         |
| [json_to_md.py](https://github.com/GokuMohandas/mlops-course/blob/main/.github/workflows/json_to_md.py)           | This code snippet converts a JSON file into Markdown format. It takes a JSON file as input and outputs the converted Markdown file. The Markdown file includes the key-value pairs from the JSON data in a readable format. The code achieves this by iterating over the JSON data and formatting it into Markdown syntax. |
| [workloads.yaml](https://github.com/GokuMohandas/mlops-course/blob/main/.github/workflows/workloads.yaml)         | The code snippet workloads.yaml in the.github/workflows directory is responsible for running various workloads in the parent repository. It configures AWS credentials, sets up dependencies, runs workloads, reads results from S3, and comments the results on the pull request.                                         |
| [documentation.yaml](https://github.com/GokuMohandas/mlops-course/blob/main/.github/workflows/documentation.yaml) | The code snippet is part of the repository's documentation workflow. It sets up dependencies, installs required packages, and deploys documentation using MkDocs. It ensures that the documentation is built and deployed correctly whenever there is a push to the main branch.                                           |

</details>

<details closed><summary>notebooks</summary>

| File                                                                                                  | Summary                                                                                                                                                                                                                                                                                |
| ---                                                                                                   | ---                                                                                                                                                                                                                                                                                    |
| [benchmarks.ipynb](https://github.com/GokuMohandas/mlops-course/blob/main/notebooks/benchmarks.ipynb) | This code snippet focuses on the repository's documentation and CI/CD workflows. It includes a script to convert JSON to Markdown and a workflow to serve the documentation.                                                                                                           |
| [madewithml.ipynb](https://github.com/GokuMohandas/mlops-course/blob/main/notebooks/madewithml.ipynb) | This code snippet, located in the `deploy/services` directory, serves a machine learning model. It includes a YAML file defining the service and a Python script to serve the model. It is part of a larger MLOps repository structure aimed at automating machine learning workflows. |

</details>

---

##  Getting Started

***Prerequisites***

Ensure you have the following dependencies installed on your system:

- `► INSERT-DEPENDENCY-1`
- `► INSERT-DEPENDENCY-2`
- `► INSERT-DEPENDENCY-3`
- `► ...`

###  Installation

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

###  Running mlops-course
Use the following command to run mlops-course:
```sh
python main.py
```

###  Tests
To execute tests, run:
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

- **[Submit Pull Requests](https://github.com/GokuMohandas/mlops-course/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/GokuMohandas/mlops-course/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/GokuMohandas/mlops-course/issues)**: Submit bugs found or log feature requests for mlops-course.

<details closed>
<summary>Contributing Guidelines</summary>

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

##  License


This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-quick-links)

---
