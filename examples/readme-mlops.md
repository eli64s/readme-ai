
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
mlops-course
</h1>
<h3>◦ Accelerate your ML journey with MLOps</h3>
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
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="Markdown" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white" alt="JSON" />
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

The project is a comprehensive machine learning pipeline that provides end-to-end text classification of tags for input text. It includes functionality for data preprocessing, model training, hyperparameter tuning, and performance evaluation, with integration with MLFlow and Optuna for experiment tracking and optimization. The project also includes a Streamlit web app and FastAPI-based web service for predicting tags for input text, as well as an Airflow DAG for MLOps tasks. The project's value proposition lies in its ease of use, flexibility, and reproducibility, making it an ideal tool for machine learning practitioners looking to streamline their text classification pipelines.

---

## ⚙️ Features

Feature | Description |
|-----|-----|
|**🏗 Architecture**| The codebase follows the standard directory structure for a machine learning project with separate directories for data, models, and utilities. It also adopts a microservices-based architecture with separate modules for Streamlit, FastAPI, and Airflow which increases the code's modularity and scalability. The codebase also utilizes containerization, using Docker, to enable easy deployment and scaling of the application across multiple environments.|
|**📑 Documentation**|The codebase includes detailed README.md files that provide instructions on how to set up the project, install dependencies, and execute the code. Furthermore, the codebase includes comments and docstrings in the code files, providing detailed information about the purpose of each function and how it fits into the overall workflow.|
|**🧩 Dependencies**|The codebase relies on many popular Python libraries such as NumPy, pandas, Scikit-learn, and NLTK for data processing and machine learning tasks. Other important dependencies include optuna, dvc, streamlit, fastapi, and airflow, which are used to manage and optimize machine learning workflows.|
|**♻️ Modularity**|The codebase is modular with separate modules for data preparation, model training, prediction, and serving. The use of a microservices-based architecture further reinforces the code's modularity, with each microservice encapsulating distinct functionality. This design facilitates easier maintenance, testing, and refactoring.|
|**✔️ Testing**|The codebase includes a Makefile that contains a test command, which runs unit tests on the data, models, and utility modules. The tests validate the output of functions and predict that the code adheres to expected behavior, improving the code's reliability. The codebase also includes documentation on how to run the tests.|
|**⚡️ Performance**|The codebase utilizes several techniques to enhance performance, including parallel processing, in-memory processing, and caching. The use of optuna further optimizes hyperparameters, resulting in improved model performance. Moreover, the use of containerization reduces the overhead associated with environment setup, improving deployment speed.|
|**🔒 Security**|The codebase incorporates security best practices such as not storing confidential information in code and minimizing access to cloud storage. The use of FastAPI and Airflow's built-in authentication and authorization mechanisms ensures that sensitive data is not accessed by unauthorized users.|
|**🔀 Version Control**|The codebase uses Git for version control and includes a.gitignore file that specifies files and directories to be excluded from version control. Furthermore, the use of DVC for version control and data backup ensures that data is backed up at each stage of the machine learning pipeline.|
|**🔌 Integrations**|The codebase integrates with multiple external services, such as AWS S3 and Google BigQuery, providing easy access to commonly used

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

| File                | Summary                                                                                                                                                                                                                                                                                               | Module                      |
|:--------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------|
| webserver_config.py | The provided code snippet contains the default configuration for the Airflow webserver. It includes authentication settings such as authentication type and user self-registration, as well as theme configuration options. It also imports the AUTH_DB module from the fab_security.manager package. | airflow/webserver_config.py |

</details>

<details closed><summary>App</summary>

| File        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Module          |
|:------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------|
| api.py      | This code snippet defines endpoints for a FastAPI-based web service that performs text classification using a pre-trained ML model. The `load_artifacts()` function initializes the model artifacts required for inference. The `construct_response()` decorator is used to construct JSON responses for each endpoint. The endpoint functions return JSON responses with details of the model's performance metrics, the arguments used for training, and predictions made on input texts. | app/api.py      |
| gunicorn.py | This code snippet is a configuration file for Gunicorn, a Python WSGI HTTP server. It sets parameters for server socket, worker processes, server mechanics, logging, process naming, and server hooks. The parameters include the number of worker processes, maximum number of simultaneous clients, log file path, and hooks for worker signals and process execution.                                                                                                                   | app/gunicorn.py |
| schemas.py  | The code provides a data model for a PredictPayload object which includes a list of Text objects. The Text object, in turn, has a text field that must have a minimum length of 1. The code also includes a validator to ensure that the list of Text objects is not empty. The schema_extra attribute provides an example of the JSON structure expected in the payload.                                                                                                                   | app/schemas.py  |
| data.py     | The provided code snippet contains functions for text preprocessing, label encoding, and data splitting. The preprocess function can clean and preprocess raw text by removing stopwords, stemming, and replacing minor labels. The LabelEncoder class encodes labels into unique indices and can be saved and loaded from a JSON file. Finally, the get_data_splits function generates balanced data splits using train_test_split from sklearn.                                           | app/data.py     |

</details>

<details closed><summary>Config</summary>

| File      | Summary                                                                                                                                                                                                                                                                                                | Module           |
|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| config.py | The provided code snippet sets up directories, assets, MLFlow model registry, and loggers for a machine learning project. It also includes a list of stop words commonly used in natural language processing. The code showcases best practices for structuring a project and logging its performance. | config/config.py |

</details>

<details closed><summary>Dags</summary>

| File         | Summary                                                                                                                                                                                                                                                                                                                                                                    | Module                    |
|:-------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------|
| workflows.py | The code snippet defines an Airflow DAG for MLOps tasks, containing four tasks: extracting data from a BigQuery data warehouse and saving it locally, validating the data using Great Expectations, optimizing hyperparameters using Optuna, and training a model using the optimized hyperparameters. The DAG is set to catch up on missed runs and is tagged as "mlops". | airflow/dags/workflows.py |

</details>

<details closed><summary>Notebooks</summary>

| File          | Summary                                 | Module                  |
|:--------------|:----------------------------------------|:------------------------|
| tagifai.ipynb | Prompt exceeds max token limit: 214676. | notebooks/tagifai.ipynb |

</details>

<details closed><summary>Root</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                      | Module     |
|:-----------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------|
| Dockerfile | The provided code snippet defines a Docker image based on Python 3.7-slim, installs dependencies, copies application files, pulls assets from S3 using DVC, exports ports, and starts the app using Gunicorn and Uvicorn. It also installs the required packages and sets up the working directory.                                                                                                                                          | Dockerfile |
| Makefile   | This code snippet is a Makefile that contains several commands to manage a Python project. The'venv' command helps create a virtual environment, the'style' command runs style formatting tools, the'clean' command deletes unnecessary files, and the'test' command runs tests on code, data, and models. The file also includes a'dvc' command that adds and pushes data files using DVC.                                                  | Makefile   |
| setup.py   | The given code snippet is a Python script that defines a package named "tagifai" with version 0.1 and describes it as a tool for classifying machine learning projects. It imports necessary libraries, loads required packages from a "requirements.txt" file, and defines the dependencies for development, documentation, and testing as extra requirements. The package can be installed using the standard "setup.py" file through pip. | setup.py   |

</details>

<details closed><summary>Streamlit</summary>

| File   | Summary                                                                                                                                                                                                                                                                                                                                    | Module           |
|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| app.py | This code snippet imports necessary modules and files for a Streamlit web app that displays labeled projects data, model performance metrics, and allows for text input to generate predictions using the Tagifai library. The app also includes user input for selecting specific performance metrics and slices based on available data. | streamlit/app.py |

</details>

<details closed><summary>Tagifai</summary>

| File        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Module              |
|:------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------|
| predict.py  | The provided code snippet contains two functions, custom_predict and predict. The custom_predict function takes predicted probabilities, a threshold and an index and returns predicted label indices. The predict function takes a list of raw input texts and a dictionary of artifacts, applies a vectorizer to the texts, calls the custom_predict function with the model and threshold from the artifacts dictionary, and returns a list of input texts with predicted tags.                                                                          | tagifai/predict.py  |
| utils.py    | The provided code snippet consists of three functions. The first function loads a dictionary from a JSON file, the second function saves a dictionary to a specific file location, and the third function sets seeds for reproducibility using the numpy and random modules. These functions can be used in data manipulation and analysis tasks that involve working with JSON files and generating reproducible results.                                                                                                                                  | tagifai/utils.py    |
| train.py    | This code snippet trains a text classification model using a random oversampling technique and stochastic gradient descent classifier with log loss. It uses Tf-idf vectorization and Optuna library for hyperparameter tuning. The trained model is evaluated using precision, recall, and F1 score. The performance metrics are logged using MLflow and printed to the console.                                                                                                                                                                           | tagifai/train.py    |
| evaluate.py | The code snippet defines two slicing functions for identifying subsets of data, and functions for generating performance metrics (precision, recall, F1 score) on the overall dataset and subsets. The slicing functions use Pandas and Snorkel libraries to identify projects related to natural language processing and those with short titles/descriptions. The performance metrics functions use NumPy and Scikit-learn libraries to calculate overall and per-class metrics, as well as slice metrics if a Pandas DataFrame is provided.              | tagifai/evaluate.py |
| main.py     | The provided code snippet executes an end-to-end machine learning pipeline for predicting tags for input text. It uses the Typer library for command-line interface and integrates with MLflow and Optuna for experiment tracking and hyperparameter optimization. The pipeline involves extracting, loading and transforming data, training a model, hyperparameter tuning, and predicting tags for input text using the trained model. Artifacts such as model, vectorizer, performance metrics, and hyperparameters are logged and saved for future use. | tagifai/main.py     |
| data.py     | The provided code snippet includes functions for preprocessing and cleaning text data, replacing out of scope and minority labels, and generating balanced data splits. It also includes a LabelEncoder class for encoding labels into unique indices and saving the encoder as a JSON file. The code utilizes popular Python libraries including pandas, NumPy, Scikit-learn, and NLTK.                                                                                                                                                                    | tagifai/data.py     |

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
