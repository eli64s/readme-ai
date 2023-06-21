
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
mlops-course
</h1>
<h3>◦ MLOps made easy with mlops-course</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?style&logo=Streamlit&logoColor=white" alt="Streamlit" />
<img src="https://img.shields.io/badge/scikitlearn-F7931E.svg?style&logo=scikit-learn&logoColor=white" alt="scikitlearn" />
<img src="https://img.shields.io/badge/Jupyter-F37626.svg?style&logo=Jupyter&logoColor=white" alt="Jupyter" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style&logo=Docker&logoColor=white" alt="Docker" />
<img src="https://img.shields.io/badge/pandas-150458.svg?style&logo=pandas&logoColor=white" alt="pandas" />

<img src="https://img.shields.io/badge/DVC-13ADC7.svg?style&logo=DVC&logoColor=white" alt="DVC" />
<img src="https://img.shields.io/badge/MLflow-0194E2.svg?style&logo=MLflow&logoColor=white" alt="MLflow" />
<img src="https://img.shields.io/badge/NumPy-013243.svg?style&logo=NumPy&logoColor=white" alt="NumPy" />
<img src="https://img.shields.io/badge/FastAPI-009688.svg?style&logo=FastAPI&logoColor=white" alt="FastAPI" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style&logo=JSON&logoColor=white" alt="JSON" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
</p>

![GitHub top language](https://img.shields.io/github/languages/top/GokuMohandas/mlops-course?style&color=5D6D7E)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/GokuMohandas/mlops-course?style&color=5D6D7E)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/GokuMohandas/mlops-course?style&color=5D6D7E)
![GitHub license](https://img.shields.io/github/license/GokuMohandas/mlops-course?style&color=5D6D7E)
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

The git repository, mlops-course, contains a machine learning project called Tagifai that classifies machine learning projects. It offers a containerized environment using Docker, Makefile automation for common tasks, a FastAPI application and Streamlit web interface for text inference, and Python scripts for data preprocessing, model training, and artifact management. The project is valuable for structuring, logging, and automating machine learning workflows, as well as providing a streamlined machine learning pipeline for text classification tasks.

---

## ⚙️ Features

Feature | Description |
|-----|-----|
| **🏗 Architecture** | The codebase is structured following a modular architecture with clear separation of concerns between different components. The use of DVC for asset versioning and managing dependencies, as well as the use of Docker for containerizing the application, allows for easy reproducibility and portability. The architecture also incorporates MLFlow for tracking experiments and model performance. |
| **📑 Documentation** | The codebase includes comprehensive documentation in the form of README files detailing the purpose and functionality of each component, as well as instructions for setting up and running the application. Documentation is also provided in the codebase with clear and concise comments throughout the code. |
| **🧩 Dependencies** | The codebase includes a clearly defined set of dependencies listed in a requirements.txt file, which can be easily installed using pip. The Makefile includes a target to create and activate a virtual environment for the project to ensure consistent dependencies across different systems. |
| **♻️ Modularity** | The codebase follows a modular design pattern with separate components responsible for specific tasks, such as data preprocessing, training, and inference. This allows for easy maintenance, testing, and scaling of different parts of the application. The use of Pydantic models for validating and handling incoming requests in the FastAPI application adds an additional layer of modularity and validation. |
| **✔️ Testing** | The codebase includes a comprehensive suite of tests using Pytest and Great Expectations. Tests are included for code, data, and models, ensuring the entire application is rigorously tested. The Makefile includes a target for running tests, which can be integrated into a CI/CD pipeline. |
| **⚡️ Performance** | The codebase includes several optimizations for performance, such as using Stochastic Gradient Descent for training the model, using FastAPI for building a high-performance API, and using Gunicorn as a web server. Additionally, the use of MLFlow for tracking experiments and performance allows for easy comparison of different models and configurations. |
| **🔒 Security** | The codebase includes several security measures, such as using Pydantic models for input validation in the API, using a secure and random secret key for authentication in the Airflow webserver, and explicitly setting permissions for files and directories in the Dockerfile. However, additional security measures, such as input sanitization, password hashing, and using HTTPS for API endpoints, could be implemented depending on the specific use case. |
| **🔀 Version Control** | The codebase uses Git for version control and is hosted on GitHub. Clear commit messages and pull request descriptions are used to provide context and explain changes, making it easy for collaborators to review and contribute to the project. The use of DVC for versioning assets and dependencies further streamlines the version control process. |
| **🔌 Integrations** | The codebase includes

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

| File                | Summary                                                                                                                                                                                                                                                                                                                       | Module                      |
|:--------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------|
| webserver_config.py | The provided code snippet contains default configuration settings for the Airflow webserver, including authentication configuration options such as AUTH_DB and AUTH_REMOTE_USER, as well as theme configuration options. It also includes commented-out code for other authentication methods like AUTH_LDAP and AUTH_OAUTH. | airflow/webserver_config.py |

</details>

<details closed><summary>App</summary>

| File        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Module          |
|:------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------|
| api.py      | The provided code snippet is a FastAPI application that provides endpoints to classify machine learning projects using TagIfAI. The application loads artifacts on startup and includes endpoints for health check, retrieving performance metrics, getting arguments used for the run, and predicting tags for a list of texts. The responses are constructed in JSON format with metadata such as message, method, status code, timestamp, and URL.                                                                                                                    | app/api.py      |
| gunicorn.py | The provided code snippet is a Gunicorn config file that sets up the server socket, worker processes, server mechanics, logging, process naming, and server hooks for a Python web application. It allows customization of various parameters such as the number of worker processes, worker class, timeout, log level, and server hooks for users to optimize the application's performance and behavior. It also provides useful functions such as post_fork, pre_fork, and pre_exec for server customization.                                                         | app/gunicorn.py |
| schemas.py  | The provided code defines two Pydantic models-Text and PredictPayload-that are used for validating and handling incoming requests in a FastAPI application. The Text model includes a string field with a minimum length requirement and the PredictPayload model includes a list of Text objects, which must not be empty, along with an example request schema. The @validator decorator is used to add custom validation logic to the PredictPayload model.                                                                                                           | app/schemas.py  |
| data.py     | The provided code snippet offers various functions for preprocessing text and labels in a DataFrame, encoding labels into unique indices, and generating balanced data splits. The functions include replacing out of scope labels, replacing minority labels, cleaning text by removing non-alphanumeric characters, stop words, and stemming, and performing train-test splits on data. The code also includes a LabelEncoder class that can encode and decode labels, save and load label encodings from a JSON file, and provide useful meta-data about the encoder. | app/data.py     |

</details>

<details closed><summary>Config</summary>

| File      | Summary                                                                                                                                                                                                                                                                                                                                         | Module           |
|:----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| config.py | The code snippet defines several directories and stores for a machine learning project, sets up logging with rich output to console and rotating files, and defines a list of stopwords. It also sets up MLFlow tracking to a local directory. The provided code is useful for structuring a machine learning project and logging its progress. | config/config.py |

</details>

<details closed><summary>Dags</summary>

| File         | Summary                                                                                                                                                                                                                                                                                                     | Module                    |
|:-------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------|
| workflows.py | This code snippet sets up an Airflow DAG for MLOps workflows. It includes tasks for extracting labeled data from BigQuery, validating the data using Great Expectations, optimizing hyperparameters using Tagifai, and training a model using Tagifai. The tasks are linked using a simple linear pipeline. | airflow/dags/workflows.py |

</details>

<details closed><summary>Notebooks</summary>

| File          | Summary                                 | Module                  |
|:--------------|:----------------------------------------|:------------------------|
| tagifai.ipynb | Prompt exceeds max token limit: 214676. | notebooks/tagifai.ipynb |

</details>

<details closed><summary>Root</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Module     |
|:-----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------|
| Dockerfile | This Dockerfile sets up a Python 3.7-slim environment, installs dependencies, copies files and directories, pulls assets from S3 and exposes port 8000. It uses gunicorn and uvicorn to start the application. The purpose of this code snippet is to provide a containerized environment for a Python app called Tagifai that uses DVC to manage assets.                                                                                                             | Dockerfile |
| Makefile   | This is a Makefile that includes several targets for automating common tasks in a Python project. The'venv' target creates a virtual environment and installs dependencies, the'style' target formats code using black, flake8, and isort. The'clean' target deletes unnecessary files, and the'test' target runs tests on code, data, and models using pytest and great_expectations. The'dvc' target adds data files to DVC and pushes them to a remote repository. | Makefile   |
| setup.py   | The code defines a package "tagifai" with version number 0.1, which classifies machine learning projects. Required packages are loaded from a "requirements.txt" file. The package has three optional extras: "dev", "docs", and "test", with corresponding packages for development, documentation, and testing. The package can be installed using setuptools.                                                                                                      | setup.py   |

</details>

<details closed><summary>Streamlit</summary>

| File   | Summary                                                                                                                                                                                                                                                                                                                                           | Module           |
|:-------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| app.py | This code snippet imports required libraries and files, and then displays data, performance, and allows text inference using Streamlit. It loads a CSV file of labeled projects and displays it. It also displays the overall performance and performance by class and slice, along with allowing text input for inference using a trained model. | streamlit/app.py |

</details>

<details closed><summary>Tagifai</summary>

| File        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Module              |
|:------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------|
| predict.py  | This code snippet includes two functions, "custom_predict" and "predict". The custom_predict function takes a numpy array of predicted probabilities, a threshold value, and an index, and returns an array of predicted label indices based on the input. The predict function takes a list of input texts and a dictionary of artifacts, applies the custom_predict function on the artifacts, and returns a list of dictionaries with the input text and predicted tag for each input text. The artifacts include a trained model, a vectorizer, and a label encoder. | tagifai/predict.py  |
| utils.py    | The code snippet provides three functions: load_dict() to load a dictionary from a JSON file, save_dict() to save a dictionary to a specific file location in JSON format, and set_seeds() to set a seed for reproducibility using numpy and random libraries. The load_dict() function takes a file path as an argument, while the save_dict() function takes a dictionary to save and file path to save the dictionary. Sort_keys and encoder can be specified optionally in the save_dict() function. The set_seeds() function takes an integer seed value.           | tagifai/utils.py    |
| train.py    | The code defines a function `train()` that trains a machine learning model using Stochastic Gradient Descent on text data. The model is optimized using Optuna with early stopping, and the performance is evaluated using metrics like precision and recall. The code also includes an `objective()` function that defines the trial parameters for optimization.                                                                                                                                                                                                       | tagifai/train.py    |
| evaluate.py | The provided code snippet offers a collection of functions to generate performance metrics for classification tasks. The `get_metrics` function computes precision, recall, and F1 score for multiple classes, as well as performance across defined slices of data. Slicing functions, such as `nlp_cnn` and `short_text`, are used to create these slices. The `get_slice_metrics` function is utilized to generate metrics for each defined slice.                                                                                                                    | tagifai/evaluate.py |
| main.py     | The provided code is a Python script with command line interfaces implemented using Typer. It contains four main functions: elt_data() for data extraction, loading and transformation, train_model() for model training with hyperparameter optimization, optimize() for hyperparameter search using Optuna, and predict_tag() for predicting tags for new text data using saved artifacts from a trained model. The script also uses MLflow for logging and tracking model runs and Optuna for hyperparameter optimization.                                            | tagifai/main.py     |
| data.py     | This code snippet provides functions for preprocessing text data, replacing out of scope and minority labels, generating balanced data splits, and encoding labels into unique indices. It also includes a class for saving and loading label encoder instances as JSON files. The functions and class aim to facilitate efficient and effective text classification tasks.                                                                                                                                                                                              | tagifai/data.py     |

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
