
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
mlops-course
</h1>
<h3 align="center">📍 Revolutionize your workflow with MLOps-Course on GitHub!</h3>
<h3 align="center">🚀 Developed with the software and tools below:</h3>

<p align="center">
<img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=for-the-badge&logo=Streamlit&logoColor=white" alt="Streamlit" />
<img src="https://img.shields.io/badge/scikitlearn-F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikitlearn" />
<img src="https://img.shields.io/badge/Jupyter-F37626.svg?style=for-the-badge&logo=Jupyter&logoColor=white" alt="Jupyter" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=for-the-badge&logo=Docker&logoColor=white" alt="Docker" />
<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=for-the-badge&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions" />
<img src="https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="pandas" />

<img src="https://img.shields.io/badge/DVC-13ADC7.svg?style=for-the-badge&logo=DVC&logoColor=white" alt="DVC" />
<img src="https://img.shields.io/badge/MLflow-0194E2.svg?style=for-the-badge&logo=MLflow&logoColor=white" alt="MLflow" />
<img src="https://img.shields.io/badge/NumPy-013243.svg?style=for-the-badge&logo=NumPy&logoColor=white" alt="NumPy" />
<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=for-the-badge&logo=FastAPI&logoColor=white" alt="FastAPI" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="Markdown" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white" alt="JSON" />
</p>
</div>

---

## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍Overview](#-overview)
- [🔮 Features](#-features)
- [⚙️ Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🏎💨 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [🪪 License](#-license)
- [📫 Contact](#-contact)
- [🙏 Acknowledgments](#-acknowledgments)

---


## 📍Overview

The project is a comprehensive machine learning operations (MLOps) framework for text classification tasks. It includes tools for data preprocessing, model training and optimization, prediction, and evaluation. It leverages various Python libraries and frameworks such as FastAPI, MLflow, Optuna, and Airflow to streamline the MLOps workflow. The project aims to facilitate the creation and deployment of text classification models for various use cases, such as content tagging and document categorization.

---

## 🔮 Features

Feature | Description |
|---|---|
| **🏗 Structure and Organization** | The codebase is well-structured and organized, with clear separation of concerns and modular design patterns. The use of Makefiles and Dockerfiles streamlines the setup process and facilitates reproducibility. |
| **📝 Code Documentation** | The code includes good documentation, with comprehensive README files, docstrings for functions and modules, and comments throughout the codebase. |
| **🧩 Dependency Management** | The code utilizes clear and concise dependency management, with requirements.txt, PyProject.toml, and setup.py files for package installation, and pre-commit hooks for code quality and consistency. |
| **♻️ Modularity and Reusability** | The codebase is highly modular and reusable, with well-defined functions and classes, and clearly separated concerns. The code also incorporates inheritance and polymorphism in certain areas. |
| **✅ Testing and Quality Assurance** | The code includes comprehensive unit tests and integration tests, as well as continuous integration and deployment using GitHub Actions. Pre-commit hooks are also used for code quality and consistency checks. |
| **⚡️ Performance and Optimization** | The code makes use of various performance and optimization techniques, such as caching, parallelization, and hyperparameter optimization, with clear logging and monitoring of performance metrics. |
| **🔒 Security Measures** | The code incorporates custom configuration files and secure storage of sensitive information such as AWS credentials and private keys. The code also includes options for LDAP, OAuth, and database authentication in Airflow. |
| **🔄 Version Control and Collaboration** | The codebase is well-managed using Git version control, with clear commit messages and pull request reviews, and integration with GitHub Actions for continuous integration and deployment. |
| **🔌 External Integrations** | The codebase incorporates various external integrations, such as MLflow for experiment tracking, Optuna for hyperparameter optimization, and BigQuery for data extraction and validation. |
| **📈 Scalability and Extensibility** | The codebase is designed for scalability and extensibility, with clearly separated concerns, modular design patterns, and use of cloud services such as S3 and Docker for deployment. The use of Airflow also facilitates scheduling and orchestration of complex workflows. |

---


<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## ⚙️ Project Structure


```bash
repo
├── Dockerfile
├── Makefile
├── README.md
├── airflow
│   ├── airflow.cfg
│   ├── dags
│   │   └── workflows.py
│   └── webserver_config.py
├── app
│   ├── api.py
│   ├── data.py
│   ├── gunicorn.py
│   └── schemas.py
├── config
│   ├── args.json
│   ├── config.py
│   ├── performance.json
│   └── run_id.txt
├── data
│   ├── labeled_projects.csv.dvc
│   ├── projects.csv.dvc
│   └── tags.csv.dvc
├── docs
│   ├── index.md
│   └── tagifai
│       ├── data.md
│       ├── evaluate.md
│       ├── main.md
│       ├── predict.md
│       ├── train.md
│       └── utils.md
├── mkdocs.yml
├── notebooks
│   └── tagifai.ipynb
├── pyproject.toml
├── requirements.txt
├── setup.py
├── streamlit
│   └── app.py
├── tagifai
│   ├── data.py
│   ├── evaluate.py
│   ├── main.py
│   ├── predict.py
│   ├── train.py
│   └── utils.py
└── tests
    ├── code
    │   ├── test_args.json
    │   ├── test_data.py
    │   ├── test_evaluate.py
    │   ├── test_main.py
    │   ├── test_predict.py
    │   └── test_utils.py
    ├── great_expectations
    │   ├── checkpoints
    │   │   ├── labeled_projects.yml
    │   │   ├── projects.yml
    │   │   └── tags.yml
    │   ├── expectations
    │   │   ├── labeled_projects.json
    │   │   ├── projects.json
    │   │   └── tags.json
    │   ├── great_expectations.yml
    │   └── plugins
    │       └── custom_data_docs
    │           └── styles
    │               └── data_docs_custom_styles.css
    └── model
        └── test_behavioral.py

20 directories, 51 files
```

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 💻 Modules

<details closed><summary>Airflow</summary>

| File                | Summary                                                                                                                                                                                                                                                                                                                                                                    | Module                      |
|:--------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------|
| webserver_config.py | The provided code snippet contains default configuration settings for the Airflow webserver, including authentication options such as LDAP, OAuth, and database authentication. It also includes options for self-registration, recaptcha, and email configuration. Additionally, it includes options for theme customization using Flask App Builder's predefined themes. | airflow/webserver_config.py |
| airflow.cfg         | Prompt exceeds max token limit: 7314                                                                                                                                                                                                                                                                                                                                       | airflow/airflow.cfg         |

</details>

<details closed><summary>App</summary>

| File        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Module          |
|:------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------|
| api.py      | The provided code snippet is a FastAPI application for a machine learning project classifier called TagIfAI. It includes functionality such as loading artifacts upon startup, constructing JSON responses for different endpoints, retrieving performance metrics and arguments used for the run, and predicting tags for a list of texts. The code leverages various Python libraries such as datetime, functools, and HTTPStatus.                                                               | app/api.py      |
| gunicorn.py | The provided code snippet is a configuration file for Gunicorn (a Python WSGI HTTP Server for UNIX), with various settings for server socket, worker processes, server mechanics, logging, process naming, and server hooks. It includes settings for port, workers, timeout, errorlog, accesslog, proc_name, and functions for post_fork, pre_fork, pre_exec, when_ready, worker_int, and worker_abort. Some settings are commented out by default and require manual configuration.              | app/gunicorn.py |
| schemas.py  | This code snippet defines a Text model with a string attribute and a PredictPayload model with a list of Text objects. It also includes a validator to ensure that the list of texts to classify is not empty. The Config class includes an example schema for the PredictPayload model. Overall, this code enables input validation and defines data models for use with FastAPI.                                                                                                                 | app/schemas.py  |
| data.py     | The provided code snippet includes functions and a class for preprocessing textual data for machine learning tasks. It includes functionality to replace out-of-scope and minority labels, clean text by removing stopwords and non-alphanumeric characters, and encode labels as unique indices. Additionally, it provides a function for generating balanced data splits for training, validation, and testing. These tools can be used to build and train machine learning models on text data. | app/data.py     |

</details>

<details closed><summary>Config</summary>

| File      | Summary                                                                                                                                                                                                                                                                                                                                                               | Module           |
|:----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| config.py | The provided code snippet sets up various directories and stores for a machine learning project, including creating directories, defining logging configuration, setting up MLFlow model registry, and defining stop words. It also imports necessary modules such as logging, sys, pathlib, and mlflow, and utilizes existing module RichHandler for logging format. | config/config.py |

</details>

<details closed><summary>Dags</summary>

| File         | Summary                                                                                                                                                                                                                                                                                                                      | Module                    |
|:-------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------|
| workflows.py | This code sets up a DAG (Directed Acyclic Graph) for MLOps tasks in Airflow. It includes tasks to extract labeled data from a BigQuery data warehouse, validate it using Great Expectations, optimize hyperparameters, and train a model. The DAG is scheduled to run with a start date of two days ago and no set interval. | airflow/dags/workflows.py |

</details>

<details closed><summary>Notebooks</summary>

| File          | Summary                                | Module                  |
|:--------------|:---------------------------------------|:------------------------|
| tagifai.ipynb | Prompt exceeds max token limit: 214676 | notebooks/tagifai.ipynb |

</details>

<details closed><summary>Root</summary>

| File                    | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Module                  |
|:------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------|
| mkdocs.yml              | The provided code snippet is a configuration file for a website called "Made With ML" with a specific URL and repository link. It includes a navigation menu with links to various pages, a chosen theme, and plugins for generating documentation. It also includes a watch command to reload the documentation for any file changes.                                                                                                                                                           | mkdocs.yml              |
| .pre-commit-config.yaml | The code snippet provides a configuration file for pre-commit hooks, which are tools that ensure code quality and consistency. The file includes hooks for checking for trailing whitespace, fixing end-of-file issues, checking YAML and JSON syntax, detecting AWS credentials and private keys, and updating Python syntax. It also includes hooks for running flake8, isort, and black for style consistency. Additionally, it includes custom hooks for running DVC, testing, and cleaning. | .pre-commit-config.yaml |
| Dockerfile              | The provided code snippet is a Dockerfile that sets up a Python 3.7 environment with necessary dependencies and installs a Python package called "tagifai". It additionally copies various directories and files, initializes a DVC repository and pulls assets from an S3 bucket. Finally, it exposes port 8000 and starts the app using Gunicorn and UvicornWorker.                                                                                                                            | Dockerfile              |
| Makefile                | This code snippet is a Makefile with several commands for managing a Python project. The'venv' command creates a virtual environment and installs necessary packages.'style' formats the code using black, flake8, and isort.'clean' removes unnecessary files and directories.'test' runs pytest and great_expectations tests. There is also a'dvc' command for Data Version Control tasks. The Makefile also includes a'help' command to show available commands.                              | Makefile                |
| pyproject.toml          | The provided code snippet contains configurations for formatting, sorting, testing, and coverage in a Python project. It uses Black for code formatting, iSort for import sorting, Pytest for running tests with markers, and Pytest coverage for measuring code coverage while excluding certain files.                                                                                                                                                                                         | pyproject.toml          |
| setup.py                | The code snippet imports the necessary packages and reads in required packages from a requirements.txt file. It then defines a package called "tagifai" with its name, version, description, author, email, and URL. It also defines the required Python version, the packages to be installed, and additional packages for development, documentation, and testing.                                                                                                                             | setup.py                |

</details>

<details closed><summary>Streamlit</summary>

| File   | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                              | Module           |
|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| app.py | The provided code snippet uses the Path, pandas, and streamlit libraries, as well as custom modules, to display data, performance metrics, and run inference for a text classification model. The code loads and displays data from a CSV file, performance metrics from a JSON file, and allows users to input text for classification using a trained model. The code also uses a custom configuration file to set file paths and other variables. | streamlit/app.py |

</details>

<details closed><summary>Tagifai</summary>

| File        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Module              |
|:------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------|
| predict.py  | The provided code snippet includes functions for predicting text tags using a trained model and vectorizer. The custom_predict function allows for custom conditions to be set when predicting tags, while the predict function uses the vectorizer and model artifacts to make predictions for input texts. The output is a list of dictionaries that include the input text and predicted tag for each.                                                                                                                                                                                                | tagifai/predict.py  |
| utils.py    | The code snippet provides three functions. The first function loads a dictionary from a JSON file path, while the second saves a dictionary to a specific location in JSON format. The third function sets a seed for reproducibility by setting seeds for numpy and random. The code snippet makes use of the json, random, and numpy modules.                                                                                                                                                                                                                                                          | tagifai/utils.py    |
| train.py    | The code implements a machine learning model to predict tags for text input using Natural Language Processing techniques such as Tf-idf vectorization and stochastic gradient descent classifier. The model is trained and evaluated using various metrics, including precision, recall and f1 score. Additionally, the code provides options for hyperparameter optimization using Optuna and logs the results using MLflow.                                                                                                                                                                            | tagifai/train.py    |
| evaluate.py | The code snippet provides slicing functions for natural language processing (NLP) and short text, and metrics functions for generating performance metrics using ground truths and predictions, as well as slice metrics based on the generated slices from the slicing functions. It imports necessary libraries such as numpy, pandas, and sklearn.metrics, and uses the PandasSFApplier function from the snorkel.slicing library to apply slicing functions to a dataframe. The goal is to provide a tool for evaluating performance of models on specific slices of data based on certain criteria. | tagifai/evaluate.py |
| main.py     | The code provides a CLI for data extraction and transformation, model training, hyperparameter optimization, and prediction. It uses MLflow for experiment tracking, Optuna for hyperparameter optimization, joblib for serialization, and pandas for data manipulation. The trained model's artifacts are saved and later loaded for prediction using the `load_artifacts` and `predict` functions.                                                                                                                                                                                                     | tagifai/main.py     |
| data.py     | The code snippet provides functions for cleaning and preprocessing text data, replacing OOS and minority labels, generating balanced data splits, and encoding labels into unique indices. The `LabelEncoder` class can be used to fit and encode labels, as well as save and load label mappings to/from a JSON file. Overall, the code aims to facilitate text classification tasks by providing efficient pre-processing and encoding models.                                                                                                                                                         | tagifai/data.py     |

</details>

<details closed><summary>Workflows</summary>

| File              | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Module                              |
|:------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------|
| testing.yml       | The provided code snippet sets up a continuous integration testing workflow for Python code. The workflow triggers on push and pull request events in the "master" and "main" branches. The workflow runs on Ubuntu and includes steps to checkout the repository, set up Python 3.9, cache dependencies, install dependencies, and execute tests using pytest. Tests in the "test/code" directory are executed, excluding test_main.py and test_data.py. | .github/workflows/testing.yml       |
| documentation.yml | This code snippet defines a GitHub Action that builds and deploys documentation. It runs on push and pull_request events on the master and main branches, and uses Ubuntu, Python 3.9, and MKDocs. The script checks out the repository, sets up Python, installs dependencies, and deploys the documentation via the mkdocs gh-deploy command. Caching is also used to speed up the process.                                                             | .github/workflows/documentation.yml |

</details>

<hr />

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> `[📌  INSERT-PROJECT-PREREQUISITES]`

### 💻 Installation

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

### 🤖 Using mlops-course

```sh
python main.py
```

### 🧪 Running Tests
```sh
# [INSERT-COMMAND-FOR-TESTS]
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

`[📌  INSERT-REFERENCES-AND-RESOURCES]`


---

