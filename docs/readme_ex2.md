
<div align="center">
<h1 align="center">

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100">

<div><p>mlops-course</p></h1>


> [insert-project-summary]


![dvc](https://img.shields.io/badge/DVC-13ADC7.svg?style=for-the-badge&logo=DVC&logoColor=white)![fastapi](https://img.shields.io/badge/FastAPI-009688.svg?style=for-the-badge&logo=FastAPI&logoColor=white)![mlflow](https://img.shields.io/badge/MLflow-0194E2.svg?style=for-the-badge&logo=MLflow&logoColor=white)![numpy](https://img.shields.io/badge/NumPy-013243.svg?style=for-the-badge&logo=NumPy&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white)![scikit-learn](https://img.shields.io/badge/scikitlearn-F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

![streamlit](https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=for-the-badge&logo=Streamlit&logoColor=white)![json](https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white)![dvc](https://img.shields.io/badge/DVC-13ADC7.svg?style=for-the-badge&logo=DVC&logoColor=white)![py](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)
![ipynb](https://img.shields.io/badge/Jupyter-F37626.svg?style=for-the-badge&logo=Jupyter&logoColor=white)![markdown](https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white)

</div>


---

## Introduction

> [insert-description]

## Feautres

> [insert-description]

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## Repository Structure
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

## Modules



<details closed><summary>AIRFLOW</summary>

| file                | summary                                                                                                                                                                    |
|:--------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| webserver_config.py | This code provides the default configuration for the Airflow webserver.It includes settings for authentication type, user registration, recaptcha, mail server, and theme. |

</details>


<details closed><summary>APP</summary>

| file        | summary                                                                                                                                                                                                                                                           |
|:------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| api.py      | This code is a FastAPI application that provides endpoints for a machine learning project.It includes endpoints for health checks, performance metrics, arguments used for the run, and predictions.                                                              |
| gunicorn.py | This is a Gunicorn config file that sets up the server socket, worker processes, server mechanics, logging, process naming, and server hooks.                                                                                                                     |
| schemas.py  | This code defines a class called Text which takes a string as an argument and has a minimum length of 1.It also defines a class called PredictPayload which takes a list of Text objects as an argument and has a validator to ensure that the list is not empty. |
| data.py     | This code provides functions to preprocess data, encode labels, and generate balanced data splits.It imports json, re, collections, typing, numpy, pandas, nltk, and sklearn.                                                                                     |

</details>


<details closed><summary>CODE</summary>

| file             | summary                                                                                                                                                                                                                                                               |
|:-----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| test_utils.py    | This code tests two functions from the tagifai.utils module.The first function, save_and_load_dict, tests the ability to save a dictionary to a file and then load it back.                                                                                           |
| test_predict.py  | This code is testing the custom_predict function from the tagifai module.It is testing the function with three different thresholds (0.5, 0.6, and 0.75) and the expected output for each threshold (0, 1, and 1 respectively).                                       |
| test_evaluate.py | This code tests the tagifai evaluate module.It imports numpy, pandas, pytest, and the slicing module from snorkel.It then creates a dataframe with three entries and tests two slice functions, nlp_cnn and short_text, to make sure they return the correct indices. |
| test_data.py     | This code tests various functions related to data preprocessing and manipulation.It imports the necessary libraries and creates a fixture for a dataframe.                                                                                                            |
| test_main.py     | This code tests the Tagifai main module by running various commands such as elt-data, train-model, optimize, load-artifacts, and predict-tag.                                                                                                                         |

</details>


<details closed><summary>CONFIG</summary>

| file      | summary                                                                                                                                                         |
|:----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| config.py | This code imports logging, sys, and Path from the pathlib library.It also imports mlflow.It then sets up URLs, directories, stores, and logging configurations. |

</details>


<details closed><summary>DAGS</summary>

| file         | summary                                                                                                                                                                                                                                                                                                       |
|:-------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| workflows.py | The code provided is a Python script that creates a DAG (Directed Acyclic Graph) for MLOps tasks.It includes a PythonOperator to extract data from a BigQuery data warehouse, a GreatExpectationsOperator to validate the data, a PythonOperator to optimize the data, and a PythonOperator to train a model. |

</details>


<details closed><summary>MODEL</summary>

| file               | summary                                                                                                                                                                                                                                  |
|:-------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| test_behavioral.py | This code provides three tests for the Tagifai machine learning model.The first test checks for INVariance via verb injection, the second test checks for DIRectional expectations, and the third test checks for Minimum Functionality. |

</details>


<details closed><summary>STREAMLIT</summary>

| file   | summary                                                                                                                                                                                                                                     |
|:-------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| app.py | This code uses the Streamlit library to create a web application that allows users to view data from a labeled projects CSV file, view performance metrics for a tag or slice, and make predictions on text using a machine learning model. |

</details>


<details closed><summary>TAGIFAI</summary>

| file        | summary                                                                                                                                                                                                                                                              |
|:------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| predict.py  | This code provides a function, predict(), that takes in a list of texts and a dictionary of artifacts from a run and returns a list of predictions for the input texts.                                                                                              |
| utils.py    | This code provides two functions to load and save a dictionary from/to a JSON file, and a function to set seeds for reproducibility.                                                                                                                                 |
| train.py    | This code is a function that trains a model on data using the SGDClassifier, TfidfVectorizer, and RandomOverSampler.It also includes an objective function for optimization trials that sets additional attributes and returns the overall performance of the model. |
| evaluate.py | This code provides a function to generate performance metrics for a given set of true labels and predicted labels.It also provides a slicing function to generate metrics for slices of data.                                                                        |
| main.py     | This code provides a command line interface (CLI) for a tag prediction model.It includes commands to extract, load, and transform data, train a model, optimize hyperparameters, and predict tags.                                                                   |
| data.py     | This code provides functions to preprocess data, encode labels, and generate balanced data splits.It imports json, re, collections, typing, numpy, pandas, nltk, and sklearn.                                                                                        |

</details>
<hr />

## Getting Started

### Prerequisites

Before you begin, ensure that you have the following prerequisites installed:


> - [insert-prerequisites-if-needed]


### Installation

1. Clone the mlops-course repository:


```sh
git clone https://github.com/GokuMohandas/mlops-course && cd mlops-course
```

2. Create a new Conda environment and install the required dependencies:

```sh
conda env create -f setup/environment.yaml
conda activate mlops-course
```

> 3. [insert-additional-steps]


```sh
 #... 
```

### Running mlops-course

```sh
# ... 
```

---


## Roadmap


> - [X] [insert-task]

> - [ ] [insert-task]

> - [ ] [insert-task]

---


## Contributing

> [insert-description]

---


## License

> [insert-description]

---


## Contact

> [insert-description]

---


## Acknowledgments

> [insert-description]

---
