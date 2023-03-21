
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
mlops-course
</h1>
<h3 align="center">📍 GitHub repo for a course on MLOps which covers topics such as data management, feature engineering, model training and deployment, and model monitoring.</h3>
<h3 align="center">🚀 Developed using OpenAI's language model API and the software tools below.</h3>
<p align="center">

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

></p>

</div>

---
## 📍 Table of Contents
- [📍 Table of Contents](#-table-of-contents)
- [👋 Introdcution](#-introdcution)
- [🔮 Feautres](#-feautres)
- [⚙️ Project Structure](#️-project-structure)
- [🧩 Modules](#-modules)
- [🏎💨 Getting Started](#-getting-started)
  - [✅ Prerequisites](#-prerequisites)
  - [💻 Installation](#-installation)
  - [🤖 Running mlops-course](#-running-mlops-course)
  - [🧪 Running Tests](#-running-tests)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [🪪 License](#-license)
- [📫 Contact](#-contact)
- [🙏 Acknowledgments](#-acknowledgments)

---

## 👋 Introdcution

This GitHub project provides code for a course on MLOps (Machine Learning Operations). The course covers topics such as data management, feature engineering, model training and deployment, and model monitoring.

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

## 🧩 Modules
<details closed><summary>.</summary>

| File                    | Summary                                                                                                                                                                                                                                                               |
|:------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| .dvcignore              | DVCignore is a feature of DVC (Data Version Control) that allows users to specify patterns of files that should be ignored when running DVC commands.                                                                                                                 |
| .flake8                 | This flake8 configuration file is used to set up linting rules for Python code. It specifies that the linter should ignore errors related to line length (E501), line break before binary operator (W503), and missing white space around arithmetic operator (E226). |
| .pre-commit-config.yaml | This code file is a configuration file for pre-commit, a tool for managing and maintaining git pre-commit hooks. It specifies the repositories and hooks to be used for the pre-commit process.                                                                       |
| Dockerfile              | This code file is a Dockerfile used to create a Docker image for a machine learning application. It starts with a base image of Python 3. 7-slim and then installs dependencies, copies files, pulls assets from S3, and exports ports.                               |
| mkdocs.yml              | Made With ML is a website created by GokuMohandas and hosted on GitHub. It provides a comprehensive guide to MLOps, a set of practices that enable organizations to manage the production lifecycle of machine learning models.                                       |
| pyproject.toml          | This configuration file is used to set up the formatting and linting tools Black, iSort, Pytest, and Pytest Coverage for a Python project.                                                                                                                            |

</details>

<details closed><summary>.dvc</summary>

| File   | Summary                                                                                                 |
|:-------|:--------------------------------------------------------------------------------------------------------|
| config | url ". ./stores/blob"']                                                                                 |
|        |                                                                                                         |
|        | This code file defines a remote storage location with the name "storage" and the URL ". ./stores/blob". |

</details>

<details closed><summary>.github/workflows</summary>

| File              | Summary                                                                                                                                                                             |
|:------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| documentation.yml | This code file is a GitHub Action workflow that builds and deploys documentation for a project. It is triggered when a push or pull request is made to the master or main branches. |

</details>

<details closed><summary>Airflow</summary>

| File                | Summary                                                                        |
|:--------------------|:-------------------------------------------------------------------------------|
| airflow.cfg         | ether to enable pickling for xcom (note that this is insecure and allows for   |
|                     | # RCE exploits). This will be deprecated in Airflow 2. 0 (be forced to False). |
| webserver_config.py | if you are using a predefined theme.                                           |
|                     |                                                                                |
|                     | # Appbuilder base template                                                     |
|                     | # APP_THEME = "bootstrap-theme. css"  # default                                |
|                     | # APP_THEME = "amelia. css"                                                    |
|                     | # APP_THEME = "cerulean. css"                                                  |
|                     | # APP_THEME = "cosmo. css"                                                     |
|                     | # APP_THEME = "cyborg. css"                                                    |
|                     | # APP_THEM                                                                     |

</details>

<details closed><summary>Airflow/dags</summary>

| File         | Summary                                                                                               |
|:-------------|:------------------------------------------------------------------------------------------------------|
| workflows.py | Summary                                                                                               |
|              | This code file contains a DAG definition for an MLOps workflow. The workflow consists of four tasks:  |
|              | 1. Extracting labeled data from a BigQuery data warehouse and saving it locally.                      |

</details>

<details closed><summary>App</summary>

| File        | Summary                                                                                                                                                             |
|:------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| api.py      | Summary Documentation                                                                                                                                               |
|             | This code file contains the code for a FastAPI application called TagIfAI. It is used to classify machine learning projects.                                        |
| data.py     | s_dict: Dict[str, int] = None):                                                                                                                                     |
|             |         """Initialize LabelEncoder. Args:cls_dict (Dict[str, int], optional): dictionary of classes and indices.                                                    |
| gunicorn.py | or "0xFF" are valid for                                                                                                                                             |
|             | #       hex)                                                                                                                                                        |
|             |                                                                                                                                                                     |
|             | daemon = False                                                                                                                                                      |
|             | # raw_env =['SECRET_KEY']                                                                                                                                           |
|             | pidfile = None                                                                                                                                                      |
|             | user = None                                                                                                                                                         |
|             | group = None                                                                                                                                                        |
|             | umask = 0                                                                                                                                                           |
|             |                                                                                                                                                                     |
|             | # Gunicorn config file                                                                                                                                              |
|             | This file is used to configure the Gunicorn server.                                                                                                                 |
| schemas.py  | This code file defines a class called Text and a class called PredictPayload. The Text class has one attribute, text, which is a string with a minimum length of 1. |

</details>

<details closed><summary>Config</summary>

| File             | Summary                                                                                                                                                                                                                                              |
|:-----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| args.json        | This code file contains parameters for a machine learning algorithm. The parameters are:                                                                                                                                                             |
|                  | - shuffle: a boolean value indicating whether the data should be shuffled before training                                                                                                                                                            |
|                  | - subset: a value indicating the subset of data to use for training                                                                                                                                                                                  |
|                  | - min_freq: an integer value indicating the minimum frequency of words to include in the model                                                                                                                                                       |
|                  | - lower: a boolean value indicating whether words should be lowercased                                                                                                                                                                               |
|                  | - stem: a boolean value indicating whether words should be stemmed                                                                                                                                                                                   |
|                  | -                                                                                                                                                                                                                                                    |
| config.py        | This code file is used to set up the environment for a project. It imports the necessary libraries, sets up directories, stores, and logging, and defines constants such as URLs and accepted tags.                                                  |
| performance.json | This code file contains performance metrics for a machine learning model. The overall performance of the model is a precision of 0. 9178004535147392, a recall of 0. 7986111111111112, and an F1 score of 0. 8265063522446623, based on 144 samples. |
| run_id.txt       | This code file is a JavaScript program that implements a function called "getRandomNumber". The function takes two parameters, a minimum and a maximum, and returns a random number between the two values.                                          |

</details>

<details closed><summary>Data</summary>

| File                     | Summary                                                                                                                                                          |
|:-------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| labeled_projects.csv.dvc | The file labeled_projects. csv has an MD5 checksum of c44608ed5dd50f5fbff99575bd0f2062 and a size of 179101 bytes. It contains data related to labeled projects. |
| projects.csv.dvc         | The file `projects. csv` is a comma-separated values (CSV) file with a size of 159728 bytes and an MD5 checksum of e4d4a68c076a3853a4c1594029a44165.             |
| tags.csv.dvc             | The file `tags. csv` is a comma-separated values (CSV) file with a size of 23720 bytes and an MD5 checksum of dff460f6909d270f17bc06733c3a1f80.                  |

</details>

<details closed><summary>Notebooks</summary>

| File          | Summary                                                        |
|:--------------|:---------------------------------------------------------------|
| tagifai.ipynb | ract, transform, load) to get the data into a usable format. " |
|               |       ]                                                        |
|               |     }                                                          |
|               |   ],                                                           |
|               |   "metadata": {                                                |
|               |     "kernelspec": {                                            |
|               |       "display_name": "Python 3",                              |
|               |       "language": "python",                                    |
|               |       "name": "python3"                                        |
|               |     },                                                         |
|               |     "language_info": {                                         |
|               |       "codemirror_mode": {                                     |
|               |         "name": "ipython",                                     |
|               |         "                                                      |

</details>

<details closed><summary>Streamlit</summary>

| File   | Summary                                                                                                                                           |
|:-------|:--------------------------------------------------------------------------------------------------------------------------------------------------|
| app.py | Summary                                                                                                                                           |
|        | This code file contains a Streamlit app that allows users to view data, performance metrics, and make predictions using a machine learning model. |

</details>

<details closed><summary>Tagifai</summary>

| File        | Summary                                                                                                                                                                                                                                                                   |
|:------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| data.py     | s_dict: Dict[str, int] = None):                                                                                                                                                                                                                                           |
|             |         """Initialize LabelEncoder. Args:cls_dict (Dict[str, int], optional): Dictionary with class labels and indices.                                                                                                                                                   |
| evaluate.py | This code file contains functions to generate performance metrics for a given dataset. The first function, `nlp_cnn`, is a slicing function that returns a boolean value based on whether the dataset contains natural language processing projects that use convolution. |
| main.py     | study. best_trial                                                                                                                                                                                                                                                         |
|             |     logger. info(f"Best trial: {t. number}")                                                                                                                                                                                                                              |
|             |     logger. info(f"Best params: {t. params}")                                                                                                                                                                                                                             |
|             |     logger. info(f"Best value: {t. value}")                                                                                                                                                                                                                               |
|             |                                                                                                                                                                                                                                                                           |
|             |                                                                                                                                                                                                                                                                           |
|             | @app. command()                                                                                                                                                                                                                                                           |
|             | def predict_tags(                                                                                                                                                                                                                                                         |
|             |     args_fp: str = "config/args. json",                                                                                                                                                                                                                                   |
|             |     run_id: str = None,                                                                                                                                                                                                                                                   |
|             |     project_fp                                                                                                                                                                                                                                                            |
| predict.py  | Summary Documentation                                                                                                                                                                                                                                                     |
|             |                                                                                                                                                                                                                                                                           |
|             | This code file contains two functions: custom_predict and predict. custom_predict takes three arguments: y_prob (np. ndarray), threshold (float), and index (int).                                                                                                        |
| train.py    | alpha = trial. suggest_loguniform("alpha", 1e-5, 1e-2)                                                                                                                                                                                                                    |
|             |     args. learning_rate = trial. suggest_loguniform("learning_rate", 1e-3, 1e-1)                                                                                                                                                                                          |
| utils.py    | Summary                                                                                                                                                                                                                                                                   |
|             | This code file contains functions to load and save dictionaries from/to a JSON file, and to set seeds for reproducibility.                                                                                                                                                |

</details>
<hr />

## 🏎💨 Getting Started

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

### 🤖 Running mlops-course

```sh
python main.py
```

### 🧪 Running Tests
```sh
#run tests
```

<hr />

## 🗺 Roadmap

- [X] [📌  INSERT-TASK-TODO]
- [X] [📌  INSERT-TASK-TODO]
- [ ] [📌  INSERT-TASK-TODO]
- [ ] [📌  INSERT-TASK-TODO]


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

## 📫 Contact

If you have any questions or concerns, please open an issue on GitHub or contact the repo owner at `[📌  INSERT-EMAIL-ADDRESS]`

---

## 🙏 Acknowledgments
> `[📌  INSERT-DESCRIPTION]`


---

