
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
mlops course
</h1>

> <h3 align="center">
>
> `[📌  INSERT-PROJECT-SUMMARY]`
>
> </h3>
> <h3 align="center">🚀 Developed using OpenAI's language model API and the software tools below.</h3>
> <p align="center">
> 
> ![dvc](https://img.shields.io/badge/DVC-13ADC7.svg?style=for-the-badge&logo=DVC&logoColor=white)
> ![fastapi](https://img.shields.io/badge/FastAPI-009688.svg?style=for-the-badge&logo=FastAPI&logoColor=white)
> ![mlflow](https://img.shields.io/badge/MLflow-0194E2.svg?style=for-the-badge&logo=MLflow&logoColor=white)
> ![numpy](https://img.shields.io/badge/NumPy-013243.svg?style=for-the-badge&logo=NumPy&logoColor=white)
> ![pandas](https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
> ![scikit-learn](https://img.shields.io/badge/scikitlearn-F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
>
> ![streamlit](https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=for-the-badge&logo=Streamlit&logoColor=white)
> ![ipynb](https://img.shields.io/badge/Jupyter-F37626.svg?style=for-the-badge&logo=Jupyter&logoColor=white)
> ![py](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)
> ![json](https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white)
> ![dvc](https://img.shields.io/badge/DVC-13ADC7.svg?style=for-the-badge&logo=DVC&logoColor=white)
> ![markdown](https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white)
> </p>

</div>


---

## 📦 Table of Contents


- [📦 Table of Contents](#-table-of-contents)
- [👋 Introduction](#-introduction)
- [🔮 Feautres](#-feautres)
- [⚙️ Repository Structure](#️-repository-structure)
- [🧩 Modules](#-modules)
- [🏎💨 Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running mlops course](#running-mlops-course)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [🪪 License](#-license)
- [📲 Contact](#-contact)
- [🙏 Acknowledgments](#-acknowledgments)

---
## 👋 Introduction

The mlops-course repository contains the course materials for mlops-course.

## 🔮 Feautres

* The mlops-course repository contains the course materials for mlops-course.
* The course is split up into four parts:
    1. Part 1: Introduction to MLOps
    2. Part 2: MLOps Workflow
    3. Part 3: MLOps Tools
    4. Part 4: Advanced MLOps
* Each part of the course contains a corresponding Jupyter Notebook.
* The course also contains a requirements.txt file, which lists the dependencies needed to run the notebooks.

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## ⚙️ Repository Structure
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

## 🧩 Modules


<details closed><summary>AIRFLOW</summary>

| File Name           | Summary                                                                                                                                                                                                            |
|:--------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| webserver_config.py | This code is a configuration for the Apache Airflow webserver. It allows for the selection of an authentication type, such as OpenID, LDAP, OAuth, or Remote User, and the selection of a theme for the webserver. |

</details>

<details closed><summary>APP</summary>

| File Name   | Summary                                                                                                                                                                                                          |
|:------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| api.py      | This code is a FastAPI application that provides endpoints for classifying machine learning projects. It includes endpoints for health checks, performance metrics, arguments used for the run, and predictions. |
| gunicorn.py | This is a Gunicorn config file which sets up the server socket, worker processes, server mechanics, logging, process naming, and server hooks.                                                                   |
| schemas.py  | This code creates a class called PredictPayload which is used to store a list of Text objects. The Text class contains a string field called 'text' which must have a minimum length of 1.                       |
| data.py     | This code provides functions to preprocess text data, replace out of scope (OOS) labels, replace minority labels, encode labels, and generate balanced data splits.                                              |

</details>

<details closed><summary>CODE</summary>

| File Name        | Summary                                                                                                                                                                                                                                                    |
|:-----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| test_utils.py    | This code tests the functions save_dict and set_seed from the utils module of the tagifai library. The save_dict function is tested by creating a dictionary and saving it to a filepath, then loading it back and asserting that the values are the same. |
| test_predict.py  | This code tests the custom_predict function from the tagifai package. It tests the function with three different thresholds (0. 5, 0. 6, and 0. 75) and the corresponding expected output (0, 1, and 1).                                                   |
| test_evaluate.py | This code tests the Tagifai evaluate module, which provides functions for evaluating the performance of a text classification model.                                                                                                                       |
| test_data.py     | This code provides a set of tests for the tagifai data module. It tests the functions replace_oos_labels, replace_minority_labels, clean_text, preprocess, LabelEncoder, and get_data_splits.                                                              |
| test_main.py     | This code tests the Tagifai application, which is used for text classification. It tests the functions elt-data, train-model, optimize, load-artifacts, and predict-tag.                                                                                   |

</details>

<details closed><summary>CONFIG</summary>

| File Name   | Summary                                                                                                                                                                          |
|:------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| config.py   | This code imports logging, sys, and pathlib, sets up URLs and directories, creates directories, sets up MLFlow model registry, sets up logging, and creates a list of stopwords. |

</details>

<details closed><summary>DAGS</summary>

| File Name    | Summary                                                                                                                                                                                                                             |
|:-------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| workflows.py | This code creates a DAG (Directed Acyclic Graph) for MLOps tasks. It includes PythonOperator tasks to extract data from a BigQuery data warehouse, validate the data with GreatExpectations, optimize a model, and train the model. |

</details>

<details closed><summary>MODEL</summary>

| File Name          | Summary                                                                                                                                                    |
|:-------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| test_behavioral.py | This code tests the Tagifai machine learning model by running three types of tests: INVariance, DIRectional expectations, and Minimum Functionality Tests. |

</details>

<details closed><summary>STREAMLIT</summary>

| File Name   | Summary                                                                                                                                |
|:------------|:---------------------------------------------------------------------------------------------------------------------------------------|
| app.py      | This code is a Streamlit app that allows users to view data, performance metrics, and make predictions using a machine learning model. |

</details>

<details closed><summary>TAGIFAI</summary>

| File Name   | Summary                                                                                                                                                                                                      |
|:------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| predict.py  | This code provides a function to predict tags for given texts using a vectorizer, model, and label encoder. It also includes a custom_predict function that defaults to an index if conditions are not met.  |
| utils.py    | This code contains functions to load and save dictionaries from/to a JSON file, as well as set seeds for reproducibility.                                                                                    |
| train.py    | This code is a training function for a supervised machine learning model. It uses the TfidfVectorizer to vectorize the data, RandomOverSampler to oversample the data, and SGDClassifier to train the model. |
| evaluate.py | This code provides performance metrics for a given set of true and predicted labels, as well as metrics for slices of data generated by two slicing functions.                                               |
| main.py     | This code is a CLI app that allows users to extract, load, and transform data assets, train a model, optimize hyperparameters, and predict tags for text.                                                    |
| data.py     | This code provides functions to preprocess text data, replace out of scope (OOS) labels, replace minority labels, encode labels, and generate balanced data splits.                                          |

</details>
<hr />

## 🏎💨 Getting Started

### Prerequisites

Before you begin, ensure that you have the following prerequisites installed:


- `[📌  INSERT-PREREQUISITES-IF-NEEDED]`


### Installation

1. Clone the mlops course repository:


```sh
git clone https://github.com/GokuMohandas/mlops-course && cd mlops course
```

2. Create a new Conda environment and install the required dependencies:

```sh
conda env create -f setup/environment.yaml
conda activate mlops course
```

3. `[📌  insert-additional-steps]`


```sh
 #... 
```

### Running mlops course

```sh
# ... 
```

---

## 🗺 Roadmap

- [X] `[📌  INSERT-TASK-TODO]`
- [ ] `[📌  INSERT-TASK-TODO]`
- [ ] `[📌  INSERT-TASK-TODO]`

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

## 📲 Contact

If you have any questions or concerns, please open an issue on GitHub or contact the repo owner at `[📌  your-email@example.com]`


---

## 🙏 Acknowledgments

 `[📌  INSERT-DESCRIPTION]`

---
