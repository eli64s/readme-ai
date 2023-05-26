
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
mlops-course
</h1>
<h3 align="center">📍 Unlock the Secrets of MLOps with mlops-course!</h3>
<h3 align="center">🚀 Developed with the software and tools below:</h3>
<p align="center">

<img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=for-the-badge&logo=Streamlit&logoColor=white" alt="Streamlit" />
<img src="https://img.shields.io/badge/scikitlearn-F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikitlearn" />
<img src="https://img.shields.io/badge/Jupyter-F37626.svg?style=for-the-badge&logo=Jupyter&logoColor=white" alt="Jupyter" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="pandas" />
<img src="https://img.shields.io/badge/NumPy-013243.svg?style=for-the-badge&logo=NumPy&logoColor=white" alt="NumPy" />

<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=for-the-badge&logo=FastAPI&logoColor=white" alt="FastAPI" />
<img src="https://img.shields.io/badge/DVC-13ADC7.svg?style=for-the-badge&logo=DVC&logoColor=white" alt="DVC" />
<img src="https://img.shields.io/badge/MLflow-0194E2.svg?style=for-the-badge&logo=MLflow&logoColor=white" alt="MLflow" />
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=for-the-badge&logo=Docker&logoColor=white" alt="Docker" />
<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=for-the-badge&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="Markdown" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white" alt="JSON" />
</p>

</div>

---

## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍Overview](#overview)
- [🔮 Feautres](#-feautres)
  - [Distinctive Features](#distinctive-features)
- [⚙️ Project Structure](#️-project-structure)
- [💻 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
  - [✅ Prerequisites](#-prerequisites)
  - [💻 Installation](#-installation)
  - [🤖 Using mlops-course](#-using-mlops-course)
  - [🧪 Running Tests](#-running-tests)
- [🛠 Future Development](#-future-development)
- [🤝 Contributing](#-contributing)
- [🪪 License](#-license)
- [🙏 Acknowledgments](#-acknowledgments)

---


## 📍Overview

The mlops-course GitHub project is an innovative tool designed to simplify and streamline the process of machine learning (ML) operations. It provides users with comprehensive data, performance metrics, and automated text classification capabilities. It offers a user-friendly interface to set up a MLOps workflow, with tasks such as extracting labeled data from a BigQuery data warehouse, validating the data using Great Expectations, optimizing the data using Tagifai, and training a model. The project also offers the ability to customize the webserver's look and feel with predefined themes. Ultimately, this project provides users with a powerful, feature-rich MLOps solution that helps to accelerate the development process.

---

## 🔮 Feautres

### Distinctive Features

1. **User-Centered Design Elements:** The project features a user-centered design with endpoints for health checks, obtaining performance metrics, getting and setting run arguments, and making predictions for a list of texts.
2. **Data Pipeline:** The project implements a data pipeline with a directory structure, configures logging, sets up MLFlow model registry, and stores a list of stopwords. It also includes functions to load and save dictionaries from/to a filepath, as well as set seeds for reproducibility.
3. **Machine Learning Model:** The machine learning model implemented in the project is used for text classification, by preprocessing the data, splitting it into train, validation, and test sets, and applying a TF-IDF vectorizer, random oversampling, and SGDClassifier. The model is optimized using Optuna for hyperparameter tuning.
4. **Apache Airflow:** The project includes an Apache Airflow webserver with authentication type, user registration, and optional OAuth and LDAP setup. It also includes various predefined themes for customizing the webserver's look and feel. The project also includes a DAG with four tasks: extracting labeled data from a BigQuery data warehouse, validating the data using Great Expectations, optimizing the data using Tagifai, and training a model using Tagifai.
5. **Jupyter Notebook:** The project includes a Jupyter Notebook for text classification which provides functions to extract, load, transform data from two sources, train a model with given arguments, optimize hyperparameters, and predict a tag for input text. 
6. **Transfer Learning:** The project includes transfer learning for text classification, using a pre-trained transformer model. 
7. **Automation:** The project includes automation of the MLOps project, with automatic model training and deployment.

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

| File                | Summary                                                                                                                                                                                                                                                               | Module                      |
|:--------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------|
| webserver_config.py | This code script contains the configuration for the Apache Airflow webserver, including authentication type, user registration, and optional OAuth and LDAP setup. Additionally, it includes various predefined themes for customizing the webserver's look and feel. | airflow/webserver_config.py |

</details>

<details closed><summary>App</summary>

| File        | Summary                                                                                                                                                                                                                                                                                                                                                                          | Module          |
|:------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------|
| api.py      | This code script is for a FastAPI application that provides a machine learning classification service. It includes endpoints for health checks, obtaining performance metrics, getting and setting run arguments, and making predictions for a list of texts.                                                                                                                    | app/api.py      |
| gunicorn.py | This Gunicorn config file contains settings related to the server socket, worker processes, server mechanics, logging, process naming, and server hooks. It binds to a specified port, defines the number of workers, sets a maximum timeout, and defines logging variables. It also contains hooks for post-fork, pre-fork, pre-exec, when-ready, and error-handling functions. | app/gunicorn.py |
| schemas.py  | This code script creates a class for a'PredictPayload' object which contains a list of Text objects. Text objects are validated to ensure that they have a minimum length, and an example is provided for the'PredictPayload' object.                                                                                                                                            | app/schemas.py  |

</details>

<details closed><summary>Config</summary>

| File      | Summary                                                                                                                                                                                                                                                      | Module           |
|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| config.py | This code script sets up a directory structure, configures logging, sets up MLFlow model registry, and stores a list of stopwords. It creates directories for data, stores, and logs, as well as downloads datasets from Github and specifies accepted tags. | config/config.py |

</details>

<details closed><summary>Dags</summary>

| File         | Summary                                                                                                                                                                                                                      | Module                    |
|:-------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------|
| workflows.py | This code script creates a DAG with four tasks: extracting labeled data from a BigQuery data warehouse, validating the data using Great Expectations, optimizing the data using Tagifai, and training a model using Tagifai. | airflow/dags/workflows.py |

</details>

<details closed><summary>Notebooks</summary>

| File          | Summary                                | Module                  |
|:--------------|:---------------------------------------|:------------------------|
| tagifai.ipynb | Prompt exceeds max token limit: 214665 | notebooks/tagifai.ipynb |

</details>

<details closed><summary>Streamlit</summary>

| File   | Summary                                                                                                                                                                                                                                                                                                                                                                | Module           |
|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| app.py | This code script is used to create an MLOps course that provides data, performance metrics and automated text classification using transfer learning and transformer models. It includes a data section showing labeled projects, a performance section showing overall and class-level metrics, and an inference section for entering text and receiving predictions. | streamlit/app.py |

</details>

<details closed><summary>Tagifai</summary>

| File        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                           | Module              |
|:------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------|
| predict.py  | This code script provides a custom prediction function that takes a predicted probability array, a minimum softmax score, and a label index to use if the custom conditions are not met, and returns a predicted label index array. It also provides a predict function that takes raw input texts and artifacts from a run and returns predictions, in the form of a dictionary containing the input text and the predicted tag. | tagifai/predict.py  |
| utils.py    | This code script provides functions to load and save dictionaries from/to a filepath, as well as set seeds for reproducibility.                                                                                                                                                                                                                                                                                                   | tagifai/utils.py    |
| train.py    | This code script implements a supervised machine learning model for text classification, by preprocessing the data, splitting it into train, validation, and test sets, and applying a TF-IDF vectorizer, random oversampling, and SGDClassifier. The model is optimized using Optuna for hyperparameter tuning. The performance is evaluated and reported using metrics such as precision, recall, and F1 score.                 | tagifai/train.py    |
| evaluate.py | This code script implements a function to generate performance metrics from ground truth labels and predicted labels. It also includes functions for slicing data and measuring metrics for slices of data.                                                                                                                                                                                                                       | tagifai/evaluate.py |
| main.py     | This code script imports necessary libraries to extract, load, transform data from two sources, train a model with given arguments, optimize hyperparameters, and predict a tag for input text. The code saves results and performance metrics into an MLflow experiment.                                                                                                                                                         | tagifai/main.py     |

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
#run tests
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

[📌  INSERT-DESCRIPTION]


---

