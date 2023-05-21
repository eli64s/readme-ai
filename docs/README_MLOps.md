
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
mlops-course
</h1>
<h3 align="center">📍 The ultimate course for MlOps with Machine Learning!</h3>
<h3 align="center">🚀 Developed with the software and tools below.</h3>
<p align="center">

<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=for-the-badge&logo=FastAPI&logoColor=white" alt="typer" />
<img src="https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="numpyencoder" />
<img src="https://img.shields.io/badge/NumPy-013243.svg?style=for-the-badge&logo=NumPy&logoColor=white" alt="css" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="py" />
<img src="https://img.shields.io/badge/DVC-13ADC7.svg?style=for-the-badge&logo=DVC&logoColor=white" alt="" />
<img src="https://img.shields.io/badge/MLflow-0194E2.svg?style=for-the-badge&logo=MLflow&logoColor=white" alt="numpy" />

<img src="https://img.shields.io/badge/scikitlearn-F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="ipynb" />
<img src="https://img.shields.io/badge/Jupyter-F37626.svg?style=for-the-badge&logo=Jupyter&logoColor=white" alt="uvicorn" />
<img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=for-the-badge&logo=Streamlit&logoColor=white" alt="sample" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white" alt="dvc" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="rich" />
</p>

</div>

---
## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍Overview](#overview)
- [🔮 Feautres](#-feautres)
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

The GitHub project mlops-course is a course that teaches you how to use machine learning in your workflows.

## 🔮 Feautres

> `[📌  INSERT-PROJECT-FEATURES]`

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## ⚙️ Project Structure

```bash
.
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
<details closed><summary>.</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                              |
|:-----------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| .flake8    | This code is a configuration for the Flake8 linter, which is used to detect and report errors in Python code. It excludes the venv directory from linting, and ignores errors related to line length (E501), line breaks before binary operators (W503), and missing white space around arithmetic operators (E226). |
| Dockerfile | This code creates a Docker image for a machine learning application. It installs dependencies, copies files, pulls assets from S3, and exports ports.                                                                                                                                                                |
| .dvcignore | This code allows users to add patterns of files that should be ignored by DVC, which can improve performance. For more information, please refer to the DVC user guide.                                                                                                                                              |

</details>

<details closed><summary>.dvc</summary>

| File   | Summary                                                                                     |
|:-------|:--------------------------------------------------------------------------------------------|
| config | This code sets up a remote connection to a storage location with the URL ". ./stores/blob". |

</details>

<details closed><summary>Airflow</summary>

| File                | Summary                                                                                                                                             |
|:--------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------|
| webserver_config.py | This code provides the default configuration for the Airflow webserver, including enabling WTF_CSRF and setting the authentication type to AUTH_DB. |

</details>

<details closed><summary>Airflow/dags</summary>

| File         | Summary                                                                                                                                                                                                              |
|:-------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| workflows.py | This code creates a MLOps workflow using Airflow, BigQuery, and Great Expectations. It extracts labeled data from a BigQuery data warehouse, validates it with Great Expectations, optimizes it, and trains a model. |

</details>

<details closed><summary>App</summary>

| File        | Summary                                                                                                                                                                                                              |
|:------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| api.py      | This code is for a FastAPI application that provides a web API for classifying machine learning projects. It includes endpoints for health checks, performance metrics, arguments used for the run, and predictions. |
| gunicorn.py | This code sets up a web server with the port number taken from the environment variable PORT, or 8000 if PORT is not set.                                                                                            |
| schemas.py  | This code creates a class called PredictPayload which is used to store a list of Text objects. The Text class contains a string field called 'text' which must have a minimum length of 1.                           |
| data.py     | This code provides functions to preprocess text data, replace out of scope (OOS) labels, replace minority labels, encode labels, and generate balanced data splits.                                                  |

</details>

<details closed><summary>Config</summary>

| File      | Summary                                                                                                                          |
|:----------|:---------------------------------------------------------------------------------------------------------------------------------|
| config.py | This code imports logging, sys, and pathlib, sets up directories and files, configures logging, and creates a list of stopwords. |

</details>

<details closed><summary>Notebooks</summary>

| File          | Summary                              |
|:--------------|:-------------------------------------|
| tagifai.ipynb | Prompt too long to generate summary. |

</details>

<details closed><summary>Streamlit</summary>

| File   | Summary                                                                                                                                                                                                                           |
|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| app.py | This code imports the Path, pandas, streamlit, and tagifai libraries, and uses them to create a web application that allows users to view data, performance metrics, and make predictions on text using a machine learning model. |

</details>

<details closed><summary>Tagifai</summary>

| File        | Summary                                                                                                                                                                                                                                                                                                      |
|:------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| predict.py  | This code provides a function to predict tags for given texts using a vectorizer, model, and label encoder. It also includes a custom_predict function that defaults to an index if conditions are not met.                                                                                                  |
| utils.py    | This code provides functions to load and save dictionaries from/to a JSON file, as well as set a seed for reproducibility.                                                                                                                                                                                   |
| train.py    | This code is a training function for a supervised machine learning model. It uses the TfidfVectorizer to vectorize the data, RandomOverSampler to oversample the data, and SGDClassifier to train the model.                                                                                                 |
| evaluate.py | This code provides performance metrics for a given set of true and predicted labels, as well as metrics for slices of data generated by two slicing functions.                                                                                                                                               |
| main.py     | This code is a command line application for training a model, optimizing hyperparameters, and predicting tags for text. It uses libraries such as joblib, mlflow, optuna, pandas, and typer to extract, load, and transform data assets, train a model, optimize hyperparameters, and predict tags for text. |
| data.py     | This code provides functions to preprocess text data, replace out of scope (OOS) labels, replace minority labels, encode labels, and generate balanced data splits.                                                                                                                                          |

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
