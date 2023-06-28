
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
mlops-course
</h1>
<h3>◦ Unlock the power of MLOps!</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?style&logo=Streamlit&logoColor=white" alt="Streamlit" />
<img src="https://img.shields.io/badge/scikitlearn-F7931E.svg?style&logo=scikit-learn&logoColor=white" alt="scikitlearn" />
<img src="https://img.shields.io/badge/Jupyter-F37626.svg?style&logo=Jupyter&logoColor=white" alt="Jupyter" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style&logo=Docker&logoColor=white" alt="Docker" />
<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions" />
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

## 📒 Table of Contents
- [📒 Table of Contents](#-table-of-contents)
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

The project is a Machine Learning Operations (MLOps) course that includes various code snippets and examples for building and deploying machine learning models. It covers topics such as data preprocessing, model training and evaluation, web application development, and Docker containerization. The project's purpose is to provide a comprehensive guide to implementing best practices in managing and deploying machine learning models, enabling developers to build efficient and scalable ML pipelines. Its value proposition lies in offering practical examples and templates that can be easily adapted and extended in real-world MLOps projects.

---

## ⚙️ Features

| Feature                | Description                                                                                                                                                                                                                                                       |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **⚙️ Architecture**    | The codebase follows a modular architecture with separate directories for different components such as app, tagifai, configs, etc. It uses popular frameworks like FastAPI, Streamlit, and Gunicorn to build web applications and APIs.                             |
| **📖 Documentation**   | The codebase includes README files, inline comments, and docstrings for code explanation. The documentation is well-structured, providing instructions for installation, usage, and development.                                                                     |
| **🔗 Dependencies**    | The codebase relies on a variety of dependencies such as FastAPI, SciKit-Learn, Pydantic, Optuna, Streamlit, Gunicorn, MLflow, DVC, and other standard libraries. These dependencies enable building robust ML applications with efficient data handling and experimentation. |
| **🧩 Modularity**      | The codebase promotes modularity by separating functionalities into separate files and directories. Each component has well-defined responsibilities and can be independently developed, tested, and deployed.                                                        |
| **✔️ Testing**         | The codebase includes a "Makefile" with commands for running tests. It is structured to test code, data, and models, ensuring comprehensive test coverage. The code adheres to best practices in terms of unit testing and test data handling.                         |
| **⚡️ Performance**     | The codebase leverages optimized libraries and techniques to achieve high-performance and resource efficiency. It uses TF-IDF vectorization, SGD classifier, efficient preprocessing, and data balancing techniques to train models on large datasets effectively.         |
| **🔐 Security**        | The codebase does not explicitly address security measures in the provided files. However, the use of proven libraries and frameworks like FastAPI and Gunicorn can provide a strong foundation for implementing security measures such as JWT authentication and HTTPS. |
| **🔀 Version Control** | The codebase utilizes Git for version control, as indicated by the GitHub repository. Git provides a robust version control system, allowing for tracking changes, merging code, collaboration, and rolling back to previous versions.                                     |
| **🔌 Integrations**    | The codebase integrates with MLflow for experiment tracking and artifact management. It provides support for Airflow, Streamlit, DVC, and other tools, enabling better workflow automation and experimentation.                                                          |
| **📶 Scalability**     | The codebase demonstrates good scalability by using scalable frameworks like FastAPI, allowing for horizontal scaling across multiple instances. The modular structure also enables easier scaling of individual components as necessary.                                       |

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

<details closed><summary>Root</summary>

| File                                                                            | Summary                                                                                                                                                                                                                                                                                                                  |
| ---                                                                             | ---                                                                                                                                                                                                                                                                                                                      |
| [Dockerfile](https://github.com/GokuMohandas/mlops-course/blob/main/Dockerfile) | The given code snippet builds a Docker container with a Python 3.7-slim base image. It installs dependencies, copies necessary files, pulls assets from S3 using DVC, and exposed port 8000. Finally, it starts the app using Gunicorn as the server with UvicornWorker and the specified configuration.                 |
| [Makefile](https://github.com/GokuMohandas/mlops-course/blob/main/Makefile)     | The code snippet is a Makefile script that provides several commands:-"venv" to create a virtual environment and set it up with necessary dependencies.-"style" to execute code styling and formatting.-"clean" to remove unnecessary files.-"test" to run tests on code, data, and models.                              |
| [setup.py](https://github.com/GokuMohandas/mlops-course/blob/main/setup.py)     | This code snippet is a setup script for a Python package. It loads packages from a requirements.txt file, defines the package details (name, version, description), and specifies package dependencies. It also includes optional extra requirements for different development scenarios (e.g., documentation, testing). |

</details>

<details closed><summary>Streamlit</summary>

| File                                                                              | Summary                                                                                                                                                                                                                   |
| ---                                                                               | ---                                                                                                                                                                                                                       |
| [app.py](https://github.com/GokuMohandas/mlops-course/blob/main/streamlit/app.py) | This code snippet uses the Streamlit library to create a web application. It loads and displays data from a CSV file, shows performance metrics, and allows users to input text for prediction using a pre-trained model. |

</details>

<details closed><summary>App</summary>

| File                                                                                  | Summary                                                                                                                                                                                                                                                                                                                                                                                               |
| ---                                                                                   | ---                                                                                                                                                                                                                                                                                                                                                                                                   |
| [api.py](https://github.com/GokuMohandas/mlops-course/blob/main/app/api.py)           | The provided code snippet is a FastAPI web application that provides several endpoints. It allows users to check the health of the application, get performance metrics, retrieve run arguments, and make predictions using a machine learning model. The code defines helper functions for constructing JSON responses and loads necessary artifacts on application startup.                         |
| [gunicorn.py](https://github.com/GokuMohandas/mlops-course/blob/main/app/gunicorn.py) | The provided code snippet is a Gunicorn configuration file. It defines various options such as server socket, worker processes, server mechanics, logging, process naming, and server hooks. These options control the behavior and settings of Gunicorn, an HTTP server for running Python web applications.                                                                                         |
| [schemas.py](https://github.com/GokuMohandas/mlops-course/blob/main/app/schemas.py)   | The provided code defines two Pydantic models, "Text" and "PredictPayload", for handling input data. The "Text" model represents a single text and includes validation for a non-empty string. The "PredictPayload" model represents a list of "Text" objects and includes validation for a non-empty list. Each model also includes example data and extra configuration for documentation purposes. |
| [data.py](https://github.com/GokuMohandas/mlops-course/blob/main/app/data.py)         | This code snippet provides several functions for preprocessing and encoding data. It includes functions for replacing out of scope labels and minority labels, cleaning text, and generating data splits. It also includes a LabelEncoder class for encoding labels into unique indices.                                                                                                              |

</details>

<details closed><summary>Config</summary>

| File                                                                                 | Summary                                                                                                                                                                                                                                                                                                         |
| ---                                                                                  | ---                                                                                                                                                                                                                                                                                                             |
| [config.py](https://github.com/GokuMohandas/mlops-course/blob/main/config/config.py) | The provided code snippet sets up the necessary directories and logging configuration for a machine learning project. It also initializes the MLFlow model registry and defines a list of stopwords. Overall, the code organizes the project structure and sets up logging for tracking and debugging purposes. |

</details>

<details closed><summary>Tagifai</summary>

| File                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---                                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [predict.py](https://github.com/GokuMohandas/mlops-course/blob/main/tagifai/predict.py)   | The code provides two functions: "custom_predict" and "predict". "custom_predict" takes predicted probabilities and a threshold value, and returns predicted label indices based on conditions. "predict" uses the "custom_predict" function to make predictions for a list of input texts using a set of artifacts. The function transforms the texts using a vectorizer, predicts probabilities using a model, applies the custom predict function, and then decodes the predicted labels. Finally, it returns a list of dictionaries containing predictions for each input text. |
| [utils.py](https://github.com/GokuMohandas/mlops-course/blob/main/tagifai/utils.py)       | This code snippet provides functions to load and save dictionaries from/to JSON files, as well as a function to set a seed for reproducibility in random number generation. The code uses the json library to handle JSON data and the numpy library to set a seed value.                                                                                                                                                                                                                                                                                                           |
| [train.py](https://github.com/GokuMohandas/mlops-course/blob/main/tagifai/train.py)       | This code snippet implements the functionality to train a text classification model using the SGD classifier and perform hyperparameter optimization using Optuna. It preprocesses the data, applies TF-IDF vectorization, oversamples the training data, trains the model, and evaluates its performance. The objective of the optimization trial is to maximize the F1 score of the model.                                                                                                                                                                                        |
| [evaluate.py](https://github.com/GokuMohandas/mlops-course/blob/main/tagifai/evaluate.py) | This code snippet provides functionality for generating performance metrics for classification models. It includes slicing functions for generating metrics on specific slices of data (e.g., projects with NLP and CNN), and overall and per-class metrics. Additionally, it supports generating slice metrics using a Pandas DataFrame. The code promotes modularity and extensibility by using functions and parameterization.                                                                                                                                                   |
| [main.py](https://github.com/GokuMohandas/mlops-course/blob/main/tagifai/main.py)         | This code snippet represents a Python CLI application that extracts, transforms, and loads data, trains a machine learning model, optimizes hyperparameters, and makes predictions. It integrates with MLflow for experiment tracking and artifact management.                                                                                                                                                                                                                                                                                                                      |
| [data.py](https://github.com/GokuMohandas/mlops-course/blob/main/tagifai/data.py)         | The provided code snippet includes functions to preprocess text data, replace out of scope (OOS) and minority labels, and perform label encoding. It also includes a function to generate balanced data splits for training, validation, and testing. The code follows best practices for modularization and includes type hints for better code readability.                                                                                                                                                                                                                       |

</details>

<details closed><summary>Airflow</summary>

| File                                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                         |
| ---                                                                                                       | ---                                                                                                                                                                                                                                                                                                                                                             |
| [webserver_config.py](https://github.com/GokuMohandas/mlops-course/blob/main/airflow/webserver_config.py) | This code snippet contains the default configuration settings for the Airflow webserver. It includes authentication configuration options, such as the authentication type and authentication providers like database, LDAP, and OAuth. It also includes settings for user self-registration, recaptcha, email configuration, and themes for the web interface. |

</details>

<details closed><summary>Dags</summary>

| File                                                                                             | Summary                                                                                                                                                                                                                               |
| ---                                                                                              | ---                                                                                                                                                                                                                                   |
| [workflows.py](https://github.com/GokuMohandas/mlops-course/blob/main/airflow/dags/workflows.py) | This code snippet creates a DAG (Directed Acyclic Graph) in Airflow for MLOps tasks. It connects to a BigQuery data warehouse, extracts labeled data, validates it using Great Expectations, optimizes a model, and trains the model. |

</details>

<details closed><summary>Notebooks</summary>

| File                                                                                            | Summary                                 |
| ---                                                                                             | ---                                     |
| [tagifai.ipynb](https://github.com/GokuMohandas/mlops-course/blob/main/notebooks/tagifai.ipynb) | Prompt exceeds max token limit: 214679. |

</details>

---

## 🚀 Getting Started

### ✔️ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - `ℹ️ Requirement 1`
> - `ℹ️ Requirement 2`
> - `ℹ️ ...`

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

### 🎮 Using mlops-course

```sh
python main.py
```

### 🧪 Running Tests
```sh
pytest
```

---


## 🗺 Roadmap

> - [X] `ℹ️  Task 1: Implement X`
> - [ ] `ℹ️  Task 2: Refactor Y`
> - [ ] `ℹ️ ...`


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

This project is licensed under the `ℹ️  INSERT-LICENSE-TYPE` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 👏 Acknowledgments

> - `ℹ️  List any resources, contributors, inspiration, etc.`

---
