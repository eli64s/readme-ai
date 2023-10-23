<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>MLOPS-COURSE</h1>
<h3>◦ Code, Deploy, Transform: MLOps made simple!</h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash" />
<img src="https://img.shields.io/badge/precommit-FAB040.svg?style=flat&logo=pre-commit&logoColor=black" alt="precommit" />
<img src="https://img.shields.io/badge/scikitlearn-F7931E.svg?style=flat&logo=scikit-learn&logoColor=white" alt="scikitlearn" />
<img src="https://img.shields.io/badge/Jupyter-F37626.svg?style=flat&logo=Jupyter&logoColor=white" alt="Jupyter" />
<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat&logo=YAML&logoColor=white" alt="YAML" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=flat&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions" />

<img src="https://img.shields.io/badge/pandas-150458.svg?style=flat&logo=pandas&logoColor=white" alt="pandas" />
<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat&logo=Pytest&logoColor=white" alt="Pytest" />
<img src="https://img.shields.io/badge/Ray-028CF0.svg?style=flat&logo=Ray&logoColor=white" alt="Ray" />
<img src="https://img.shields.io/badge/MLflow-0194E2.svg?style=flat&logo=MLflow&logoColor=white" alt="MLflow" />
<img src="https://img.shields.io/badge/NumPy-013243.svg?style=flat&logo=NumPy&logoColor=white" alt="NumPy" />
<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=flat&logo=FastAPI&logoColor=white" alt="FastAPI" />
</p>
<img src="https://img.shields.io/github/license/GokuMohandas/mlops-course?style=flat&color=5D6D7E" alt="GitHub license" />
<img src="https://img.shields.io/github/last-commit/GokuMohandas/mlops-course?style=flat&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/GokuMohandas/mlops-course?style=flat&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/languages/top/GokuMohandas/mlops-course?style=flat&color=5D6D7E" alt="GitHub top language" />
</div>

---

##  Table of Contents
- [ Table of Contents](#-table-of-contents)
- [ Overview](#-overview)
- [ Features](#-features)
- [ repository Structure](#-repository-structure)
- [ Modules](#modules)
- [ Getting Started](#-getting-started)
    - [ Installation](#-installation)
    - [ Running mlops-course](#-running-mlops-course)
    - [ Tests](#-tests)
- [ Roadmap](#-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

---


##  Overview

The repository provides a comprehensive MLOps course with code and examples covering various functionalities such as training, evaluation, prediction, and serving of machine learning models. It includes code for setting up cluster environments, running jobs, and serving models using frameworks like Ray and FastAPI. The repository also contains notebooks for benchmarks and an extensive directory tree with configuration files. The codebase emphasizes automation and scalability through the use of GitHub Actions workflows and integration with AWS services. Overall, the repository offers practical knowledge and tools for deploying and managing machine learning projects.

---

##  Features

HTTPStatus Exception: 400

---


##  Repository Structure

```sh
└── mlops-course/
    ├── .github/
    │   └── workflows/
    │       ├── documentation.yaml
    │       ├── json_to_md.py
    │       ├── serve.yaml
    │       └── workloads.yaml
    ├── Makefile
    ├── datasets/
    ├── deploy/
    │   ├── cluster_compute.yaml
    │   ├── cluster_env.yaml
    │   ├── jobs/
    │   │   ├── workloads.sh
    │   │   └── workloads.yaml
    │   └── services/
    │       ├── serve_model.py
    │       └── serve_model.yaml
    ├── madewithml/
    │   ├── config.py
    │   ├── data.py
    │   ├── evaluate.py
    │   ├── models.py
    │   ├── predict.py
    │   ├── serve.py
    │   ├── train.py
    │   ├── tune.py
    │   └── utils.py
    ├── notebooks/
    │   ├── benchmarks.ipynb
    │   └── madewithml.ipynb
    ├── pyproject.toml
    ├── requirements.txt

```

---


##  Modules

<details closed><summary>Root</summary>

| File                                                                                        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---                                                                                         | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [requirements.txt](https://github.com/GokuMohandas/mlops-course/blob/main/requirements.txt) | The code in the `requirements.txt` file lists the required dependencies for different purposes. It includes packages for default functionality (e.g., hyperopt, matplotlib), notebooks (e.g., jupyterlab, lime), documentation (e.g., mkdocs, mkdocstrings), styling (e.g., black, flake8), testing (e.g., pytest, pytest-cov), development (e.g., fastapi, pre-commit), and deployment (e.g., anyscale). These dependencies are necessary for running, developing, testing, and deploying the project.                                                                                                         |
| [Makefile](https://github.com/GokuMohandas/mlops-course/blob/main/Makefile)                 | The code in the Makefile provides several functionalities:1. Styling: The `style` target uses various tools to format the code in the project. It runs `black` to apply consistent styles, `flake8` to check for code quality, `isort` to organize imports, and `pyupgrade` to upgrade code syntax.2. Cleaning: The `clean` target removes unnecessary files and folders generated during development. It deletes `.DS_Store` files, Python cache files (`__pycache__`, `.pyc`, and `.pyo`), PyTest cache files, and Jupyter Notebook checkpoint files. Additionally, it removes coverage files (`.coverage*`). |
| [pyproject.toml](https://github.com/GokuMohandas/mlops-course/blob/main/pyproject.toml)     | The code provided is a configuration file (pyproject.toml) that sets up formatting, linting, and testing options for a Python project. It includes configurations for tools such as Black for code formatting, iSort for import sorting, Flake8 for linting, PyUpgrade for updating code to newer Python versions, and Pytest for testing. It also specifies specific exclusions and options for each tool to customize the project's development environment.                                                                                                                                                  |

</details>

<details closed><summary>Deploy</summary>

| File                                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---                                                                                                        | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [cluster_env.yaml](https://github.com/GokuMohandas/mlops-course/blob/main/deploy/cluster_env.yaml)         | The code defines configuration settings for creating a cluster environment. It specifies the base image, environment variables, and debian packages required. It also allows for customization through pip and conda packages. After the cluster is built, it runs a series of post-build commands, including upgrading pip, installing necessary packages from the specified requirements.txt file hosted on GitHub.                                                             |
| [cluster_compute.yaml](https://github.com/GokuMohandas/mlops-course/blob/main/deploy/cluster_compute.yaml) | The code in `deploy/cluster_compute.yaml` defines the configuration for a compute cluster in the AWS cloud. It specifies the cloud provider, region, and the types of nodes in the cluster. There is a head node with 8 CPUs and 32 GB RAM, and a worker node with 4 CPUs, 1 GPU, and 16 GB RAM. The worker node can have a minimum of 0 and a maximum of 1 instance. The configuration also includes AWS-specific settings such as block device mappings and tag specifications. |

</details>

<details closed><summary>Jobs</summary>

| File                                                                                                | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---                                                                                                 | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [workloads.yaml](https://github.com/GokuMohandas/mlops-course/blob/main/deploy/jobs/workloads.yaml) | This code defines the configuration for a job named "workloads" within the "deploy" directory. The job is associated with a specific project ID and cluster environment, and uses a specified compute configuration. The job's runtime environment is defined with the working directory, upload path, and environment variables. The entrypoint for the job is a shell script located at "deploy/jobs/workloads.sh". The job has no maximum number of retries. |
| [workloads.sh](https://github.com/GokuMohandas/mlops-course/blob/main/deploy/jobs/workloads.sh)     | The code deploys a machine learning (ML) project using workflows and job scripts. It tests data and code, trains a model, evaluates it, and tests the trained model. It also saves the trained model and results to an S3 bucket. The job script sets environment variables, runs tests and training, saves the run ID, evaluates the model, tests the model, and uploads the model and results to S3.                                                          |

</details>

<details closed><summary>Services</summary>

| File                                                                                                        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---                                                                                                         | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [serve_model.yaml](https://github.com/GokuMohandas/mlops-course/blob/main/deploy/services/serve_model.yaml) | The code above is a YAML configuration file named "serve_model.yaml" located in the "deploy/services" directory. It contains settings for serving a machine learning model using Ray Serve. The configuration includes the name of the project, project ID, cluster environment name, compute configuration name, import path for the model-serving code, runtime environment settings, S3 upload path for model artifacts, environment variables, and the rollout strategy for updating the serving model. |
| [serve_model.py](https://github.com/GokuMohandas/mlops-course/blob/main/deploy/services/serve_model.py)     | This code is a part of a directory structure for an MLOps course. The "serve_model.py" script is responsible for copying files from an S3 bucket, setting up the entry point for the model deployment, and binding the run ID and threshold value.                                                                                                                                                                                                                                                          |

</details>

<details closed><summary>Madewithml</summary>

| File                                                                                         | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---                                                                                          | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [config.py](https://github.com/GokuMohandas/mlops-course/blob/main/madewithml/config.py)     | The code defines a configuration file for a machine learning project. It sets up logging, creates directories, and specifies MLflow settings. It also defines a logger and a list of stopwords for text processing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [models.py](https://github.com/GokuMohandas/mlops-course/blob/main/madewithml/models.py)     | The code defines a PyTorch module for a Finetuned Large Language Model (LLM). It takes in the LLM, dropout probability, embedding dimension, and number of classes as inputs. It has a forward function that performs forward propagation on a batch of data, applying dropout, passing it through the LLM, and returning the output logits.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [predict.py](https://github.com/GokuMohandas/mlops-course/blob/main/madewithml/predict.py)   | The code defines a Typer CLI app that allows for predicting tags for projects given their title and description. It includes functions for decoding indices to labels, formatting probabilities, and predicting tags with probabilities for input data. The code also includes functions for getting the best run ID from an MLflow experiment and getting the best checkpoint from a specific run. The main function loads components, predicts tags for a given title and description using a loaded predictor, and returns the prediction results.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [serve.py](https://github.com/GokuMohandas/mlops-course/blob/main/madewithml/serve.py)       | The code defines a FastAPI application that serves a machine learning model for predicting and evaluating text data. It uses the Ray Serve framework for deployment. The application has several endpoints including a health check, getting the run ID, evaluating a dataset, and predicting the class of input text. The model is loaded from a specified MLflow run ID and predictions are made using a TorchPredictor. The application can be run with different run IDs and a threshold for classifying instances as "other".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [utils.py](https://github.com/GokuMohandas/mlops-course/blob/main/madewithml/utils.py)       | The code in `utils.py` provides several utility functions. These functionalities include:-Setting seeds for reproducibility.-Loading and saving dictionaries to JSON files.-Padding arrays with zeros.-Converting batches of numpy arrays to tensors.-Getting the MLflow run ID for a given Ray trial ID.-Converting a dictionary to a list of dictionaries.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [tune.py](https://github.com/GokuMohandas/mlops-course/blob/main/madewithml/tune.py)         | The code is for a command line interface (CLI) app that performs hyperparameter tuning experiments using the Ray framework. It loads a dataset, splits it into training and validation sets, and preprocesses the data. It then creates a TorchTrainer object and sets up configurations for scaling, dataset, checkpoint, and run. It uses a HyperOptSearch algorithm to explore the hyperparameter space and an AsyncHyperBandScheduler to manage the experiment. The tuner fits the model and returns the results, including the best trial's configuration and metrics.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [train.py](https://github.com/GokuMohandas/mlops-course/blob/main/madewithml/train.py)       | The code is a part of the madewithml project and focuses on the training of a machine learning model using distributed computing. It utilizes the `Ray` library and `Torch` for distributed training, and `Transformers` for model architecture. The `train_model` function is the main function that coordinates the training process, with the ability to specify various parameters such as the number of workers, experiment name, dataset location, number of epochs, batch size, and more. The training process includes training and evaluation steps, using hyperparameters and datasets specified in the config. The results are logged using the MLflow callback and returned as a `Result` object.                                                                                                                                                                                                                                                                                                                   |
| [evaluate.py](https://github.com/GokuMohandas/mlops-course/blob/main/madewithml/evaluate.py) | This code defines a Python module called "evaluate" that contains functions for evaluating the performance of a machine learning model. The module uses the Typer library to create a command-line interface (CLI) for running the evaluation. The main function in the module is `evaluate()`, which takes three optional arguments: `run_id`, `dataset_loc`, and `results_fp`. The function loads a dataset, retrieves the best trained model checkpoint, and predicts the labels for the dataset. It then calculates various performance metrics, including precision, recall, F1 score, and the number of samples, both overall and per class. Additionally, the function calculates metrics for specific slices of the data based on predefined slicing functions. The resulting metrics are logged and can be saved to a file if specified.The code also includes helper functions for getting overall and per-class metrics, as well as slicing functions for creating subsets of the data based on specific conditions. |
| [data.py](https://github.com/GokuMohandas/mlops-course/blob/main/madewithml/data.py)         | The code provides functions and classes for loading, splitting, cleaning, and preprocessing text data. It uses the Ray library to handle large datasets and a BERT tokenizer for tokenizing the text inputs. The main functionalities include:-`load_data`: Loads data from a CSV file into a Ray Dataset.-`stratify_split`: Splits a dataset into train and test sets while ensuring an equal distribution of data points for each class in a specified column.-`clean_text`: Cleans raw text by converting to lowercase, removing stopwords, special characters, and non-alphanumeric characters.-`tokenize`: Tokenizes text inputs using a BERT tokenizer and returns the tokenized data.-`preprocess`: Preprocesses a DataFrame by combining title and description columns, cleaning text, label encoding, and tokenizing the data.-`CustomPreprocessor`: A custom preprocessor class that fits on a dataset to obtain class-to-index and index-to-class mappings and transforms batches by preprocessing the text data.    |

</details>

<details closed><summary>Workflows</summary>

| File                                                                                                              | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ---                                                                                                               | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [serve.yaml](https://github.com/GokuMohandas/mlops-course/blob/main/.github/workflows/serve.yaml)                 | The code is a GitHub Actions workflow named "serve" that is triggered manually or on a push to the main branch. It sets up a job to serve a machine learning model using AWS credentials and dependencies. The job includes steps to configure the AWS credentials, set up dependencies including Python packages, and run a command to serve the model using AnyScale.                                                                                                                                                                                                                                                                                                                                        |
| [json_to_md.py](https://github.com/GokuMohandas/mlops-course/blob/main/.github/workflows/json_to_md.py)           | The code is a Python script that converts a JSON file into a Markdown file. It takes the paths to the input JSON file and the output Markdown file as command-line arguments. The script reads the JSON file, iterates over its contents, and generates Markdown content based on the structure and values of the JSON data. The resulting Markdown content is then saved to the specified output file.                                                                                                                                                                                                                                                                                                        |
| [workloads.yaml](https://github.com/GokuMohandas/mlops-course/blob/main/.github/workflows/workloads.yaml)         | The code is a GitHub Actions workflow called "workloads". It is triggered manually (workflow_dispatch) or when a pull request is made to the main branch. The workflow runs on an Ubuntu machine and performs the following steps:1. Configures AWS credentials for accessing S3.2. Sets up dependencies by checking out the repository and installing specific Python packages.3. Runs a workload by submitting a YAML file (deploy/jobs/workloads.yaml) to AnyScale and waits for completion.4. Reads results from S3, including training results and evaluation results in JSON format.5. Converts the JSON results to Markdown format.6. Comments the training and evaluation results on the pull request. |
| [documentation.yaml](https://github.com/GokuMohandas/mlops-course/blob/main/.github/workflows/documentation.yaml) | The code in the "documentation.yaml" file sets up a GitHub workflow that automatically builds and deploys documentation for the project. It listens for pushes to the main branch and runs on an Ubuntu 22.04 environment. It performs the following steps: 1. Checks out the repository.2. Sets up Python 3.10.11 and caches pip dependencies.3. Installs specific versions of the "mkdocs" and "mkdocstrings" packages.4. Deploys the documentation using the "mkdocs gh-deploy" command, forcing an overwrite if necessary.                                                                                                                                                                                 |

</details>

<details closed><summary>Notebooks</summary>

| File                                                                                                  | Summary                                                                                                                                                                                                                                                                                                                                                                           |
| ---                                                                                                   | ---                                                                                                                                                                                                                                                                                                                                                                               |
| [benchmarks.ipynb](https://github.com/GokuMohandas/mlops-course/blob/main/notebooks/benchmarks.ipynb) | The code represents the directory structure of a project. It includes folders for datasets, deployment, code files for various functionalities like training, prediction, evaluation, and serving, a folder for notebooks, and configuration files. Specifically, the code snippet represents a Jupyter notebook file named "benchmarks.ipynb" located in the "notebooks" folder. |
| [madewithml.ipynb](https://github.com/GokuMohandas/mlops-course/blob/main/notebooks/madewithml.ipynb) | This code is a cell in a Jupyter Notebook named "madewithml.ipynb" located in the "notebooks" directory. It contains markdown code for the header and logo image of the "Made With ML" website. The markdown code includes links to the website, a badge to subscribe, and a badge to star the GitHub repository.                                                                 |

</details>

---

##  Getting Started

***Dependencies***

Please ensure you have the following dependencies installed on your system:

`- ℹ️ Dependency 1`

`- ℹ️ Dependency 2`

`- ℹ️ ...`

###  Installation

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

###  Running mlops-course

```sh
python main.py
```

###  Tests
```sh
pytest
```

---


##  Project Roadmap

> - [X] `ℹ️  Task 1: Implement X`
> - [ ] `ℹ️  Task 2: Implement Y`
> - [ ] `ℹ️ ...`


---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/GokuMohandas/mlops-course/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/GokuMohandas/mlops-course/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/GokuMohandas/mlops-course/issues)**: Submit bugs found or log feature requests for GOKUMOHANDAS.

#### *Contributing Guidelines*

<details closed>
<summary>Click to expand</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone <your-forked-repo-url>
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear and concise message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

##  License


This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#Top)

---
