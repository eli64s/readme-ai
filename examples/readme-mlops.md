
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
mlops-course
</h1>
<h3>◦ Revolutionize your ML workflow with MLOps Course.</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=for-the-badge&logo=Streamlit&logoColor=white" alt="Streamlit" />
<img src="https://img.shields.io/badge/scikitlearn-F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikitlearn" />
<img src="https://img.shields.io/badge/Jupyter-F37626.svg?style=for-the-badge&logo=Jupyter&logoColor=white" alt="Jupyter" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=for-the-badge&logo=Docker&logoColor=white" alt="Docker" />
<img src="https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="pandas" />

<img src="https://img.shields.io/badge/DVC-13ADC7.svg?style=for-the-badge&logo=DVC&logoColor=white" alt="DVC" />
<img src="https://img.shields.io/badge/MLflow-0194E2.svg?style=for-the-badge&logo=MLflow&logoColor=white" alt="MLflow" />
<img src="https://img.shields.io/badge/NumPy-013243.svg?style=for-the-badge&logo=NumPy&logoColor=white" alt="NumPy" />
<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=for-the-badge&logo=FastAPI&logoColor=white" alt="FastAPI" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white" alt="JSON" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="Markdown" />
</p>
</div>

---

## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [⚙️ Features](#-features)
- [📂 Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🚀 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The project is a comprehensive machine learning pipeline for text classification that includes training models, preprocessing data, and predicting tags for input texts. Its core functionalities include training models using stochastic gradient descent, performing hyperparameter optimization with Optuna, preprocessing text data using TF-IDF and oversampling, and predicting tags for input texts using a pre-trained model. The pipeline aims to simplify the process of developing and deploying machine learning models for text classification tasks, making it easier for developers to integrate ML into their applications.

---

## ⚙️ Features

Feature | Description |
|-----|-----|
| **🏗 Architecture** | The codebase follows a modular architecture, where there are distinct components for data preprocessing, training, and inference. The training pipeline uses Optuna for hyper-parameter optimization, and the trained models are saved and loaded using MLflow. There is also an Airflow DAG for orchestrating MLOps workflows. Furthermore, the codebase includes a Streamlit web app and FastAPI API for deploying models. |
| **📑 Documentation** | The codebase has extensive documentation, including docstrings, README files, and comments throughout the code. The README files provide details on how to set up the project for development and production, while the docstrings provide guidance on the functions and classes. |
| **🧩 Dependencies** | The codebase has dependencies on widely used packages such as Pandas, NumPy, Scikit-learn, and TensorFlow. It also uses FastAPI, Streamlit, MLflow, Optuna, and DVC for deployment, experimentation, and version control, respectively. |
| **♻️ Modularity** | The codebase is divided into different modules for data processing, training, and evaluation, with distinct functions for specific tasks such as preprocessing data, training models, and generating performance metrics. The different parts of the pipelines are clearly separated, facilitating testing, experimentation, and maintenance. |
| **✔️ Testing** | The codebase includes tests across different components, including the training pipeline, data preprocessing, and data splitting. Furthermore, the tests include both unit tests and integration tests. The tests are run using `pytest` and can be executed using the `make test` command. |
| **⚡️ Performance** | The codebase appears to have some optimization for speed, such as using TF-IDF for feature extraction and Uvicorn worker for Gunicorn. However, no extensive performance evaluations or profiling appear to have been conducted. |
| **🔒 Security** | There is no explicit focus on security in the codebase. However, some measures are taken to ensure data privacy, such as renaming columns in a labeled dataset. Authentication and validation can be included in the FastAPI and Streamlit apps. |
| **🔀 Version Control** | The codebase includes support for version control using DVC, which is used to version data files. Performing experiments and training new models are explicitly separated to enable reproducibility. Experiment results are logged using MLflow, further enabling model tracking and versioning. |
| **🔌 Integrations** | The codebase supports integration with several external tools, including Airflow, DVC, Optuna, and MLflow. These tools can be used for hyperparameter tuning, version control, experiment logging, and pipeline orchestration. |
| **📈 Scalability** | The codebase appears to have some potential for scalability, such as using distributed processing for hyperparameter tuning using Opt

---


## 📂 Project Structure


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

## 🧩 Modules

<details closed><summary>Airflow</summary>

| File                | Summary                                                                                                                                                                                                                                                                       | Module                      |
|:--------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------|
| webserver_config.py | The provided code snippet contains the default configuration for the Airflow webserver. It includes authentication type and registration options, as well as theme configurations. The authentication types supported include database, LDAP, OAuth, OpenID, and REMOTE_USER. | airflow/webserver_config.py |

</details>

<details closed><summary>App</summary>

| File        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                   | Module          |
|:------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------|
| api.py      | This code snippet defines an API using FastAPI to serve a machine learning model's predictions. It includes functions to check the API's health, retrieve model performance metrics and corresponding arguments, and predict tags for a list of texts. The code also loads artifacts during application startup and constructs JSON responses for each endpoint.                                                                          | app/api.py      |
| gunicorn.py | The provided code snippet is a Gunicorn configuration file that defines settings for a Python WSGI HTTP server such as the server socket, worker processes, logging, and server hooks. It allows for customization of server behavior, including setting the number of worker processes, timeout duration, and log granularity. The file also includes various callback functions for server events, such as post-fork and pre-execution. | app/gunicorn.py |
| schemas.py  | The code defines two Pydantic models-Text and PredictPayload-to be used for validating JSON payloads in a FastAPI endpoint. The Text model ensures that a'text' field is present and has a minimum length of 1. The PredictPayload model is used for a list of Text objects, and includes a validator to ensure that the list is not empty. The Config class includes an example JSON payload for documentation purposes.                 | app/schemas.py  |
| data.py     | This code snippet provides functions for preprocessing text data, replacing out of scope and minority labels, and generating balanced data splits. It also includes a LabelEncoder class to encode labels into unique indices, which can be saved and loaded from a JSON file. Overall, these functionalities can be helpful for preparing text data for machine learning models.                                                         | app/data.py     |

</details>

<details closed><summary>Config</summary>

| File      | Summary                                                                                                                                                                                   | Module           |
|:----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| config.py | The code initializes a logger and various directories for storing data and logs. It also sets up a MLFlow model registry and defines a list of stopwords for natural language processing. | config/config.py |

</details>

<details closed><summary>Dags</summary>

| File         | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Module                    |
|:-------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------|
| workflows.py | This code defines a DAG for MLOps workflows using Airflow. The DAG has four tasks: `extract_from_dwh` extracts labeled data from a BigQuery data warehouse, `validate` validates the extracted data using Great Expectations, `optimize` performs hyperparameter optimization, and `train` trains a machine learning model. The tasks are executed in a sequential order with `extract_from_dwh` as the first task, followed by `validate`, `optimize`, and `train`. | airflow/dags/workflows.py |

</details>

<details closed><summary>Notebooks</summary>

| File          | Summary                                 | Module                  |
|:--------------|:----------------------------------------|:------------------------|
| tagifai.ipynb | Prompt exceeds max token limit: 214676. | notebooks/tagifai.ipynb |

</details>

<details closed><summary>Root</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                                                                                                         | Module     |
|:-----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------|
| Dockerfile | The provided code snippet is for creating a Docker image for a Python application. It installs dependencies, copies the required files and directories, and pulls assets from a remote storage. It exposes port 8000 and starts the app using gunicorn with Uvicorn worker.                                                                                                                     | Dockerfile |
| Makefile   | The provided Makefile defines several commands for maintaining a Python project. The "venv" command creates a virtual environment and installs dependencies, "style" command executes styling formatting, "clean" command removes unnecessary files, and "test" command runs tests on code, data, and models. Lastly, there is a "dvc" command for adding and pushing data to a DVC repository. | Makefile   |
| setup.py   | This code snippet is a Python script that defines the package "tagifai". It loads required packages from a "requirements.txt" file, and sets up additional packages for development, documentation, and testing. The script also specifies the package name, version, author, description, and URL.                                                                                             | setup.py   |

</details>

<details closed><summary>Streamlit</summary>

| File   | Summary                                                                                                                                                                                                                                                                                                                                      | Module           |
|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| app.py | The provided code snippet imports necessary libraries and modules, including pandas and Streamlit, to create a web app. It loads and displays data from a labeled CSV file, shows performance metrics from a JSON file, and allows users to enter text for inference using a pretrained model. The app is configured using a config.py file. | streamlit/app.py |

</details>

<details closed><summary>Tagifai</summary>

| File        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Module              |
|:------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------|
| predict.py  | The provided code snippet includes two functions, `custom_predict` and `predict`, which are used to predict labels for input texts. `custom_predict` generates predicted label indices by comparing given probability scores to a threshold value, and defaulting to a specified index if the conditions are not met. `predict` uses `custom_predict` and various artifacts to predict tags for a list of input texts and returns a list of dictionaries containing the input text and predicted tag for each text.                                                                               | tagifai/predict.py  |
| utils.py    | This code snippet contains three functions. "load_dict" loads a dictionary from a JSON file. "save_dict" saves a dictionary to a specific file location in JSON format. "set_seeds" sets a seed for reproducibility using the NumPy and random libraries.                                                                                                                                                                                                                                                                                                                                         | tagifai/utils.py    |
| train.py    | The code defines a function to train a machine learning model to classify text data using stochastic gradient descent. Preprocessing and data splitting steps are performed, followed by feature extraction with TF-IDF and oversampling to handle class imbalance. The model is trained for a specified number of epochs with early stopping using Optuna for hyperparameter tuning. The evaluation metrics for the model are logged using MLflow.                                                                                                                                               | tagifai/train.py    |
| evaluate.py | The code defines two slicing functions for data analysis and a function to compute performance metrics such as precision, recall, and f1 score. The `get_metrics` function can be used to obtain overall and per-class metrics using ground truth and predicted labels. Additionally, it can provide slice metrics if a dataframe is provided with columns to slice by using the slicing functions. The generated metrics are returned in a dictionary format.                                                                                                                                    | tagifai/evaluate.py |
| main.py     | The provided code snippet contains a command-line interface (CLI) application for training, optimizing, and predicting tags for projects using machine learning models. The application uses MLflow to manage experiments, Optuna for hyperparameter optimization, and Pandas for data manipulation. The trained model's performance and artifacts are logged and saved for future use.                                                                                                                                                                                                           | tagifai/main.py     |
| data.py     | The provided code snippet contains functions and a class for preprocessing text data, encoding labels, and generating balanced data splits for a machine learning model. The preprocessing functions include replacing out of scope and minority labels, and cleaning text by lowercasing, stemming, and removing stopwords and non-alphanumeric characters. The LabelEncoder class allows for encoding and decoding labels, as well as saving and loading class instances to JSON files. The get_data_splits function generates balanced data splits for training, validation, and testing sets. | tagifai/data.py     |

</details>

---

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - [ℹ️ Requirement 1]
> - [ℹ️ Requirement 2]
> - [...]

### 🖥 Installation

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
pytest
```

---


## 🗺 Roadmap

> - [X] [ℹ️  Task 1: Implement X]
> - [ ] [ℹ️  Task 2: Refactor Y]
> - [ ] [...]


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

This project is licensed under the `[ℹ️  INSERT-LICENSE-TYPE]` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 👏 Acknowledgments

> - [ℹ️  List any resources, contributors, inspiration, etc.]

---
