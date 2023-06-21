
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
energy-forecasting
</h1>
<h3>◦ Power up your predictions with energy forecasting.</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash" />
<img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?style&logo=Streamlit&logoColor=white" alt="Streamlit" />
<img src="https://img.shields.io/badge/Redis-DC382D.svg?style&logo=Redis&logoColor=white" alt="Redis" />
<img src="https://img.shields.io/badge/Plotly-3F4F75.svg?style&logo=Plotly&logoColor=white" alt="Plotly" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />

<img src="https://img.shields.io/badge/Docker-2496ED.svg?style&logo=Docker&logoColor=white" alt="Docker" />
<img src="https://img.shields.io/badge/pandas-150458.svg?style&logo=pandas&logoColor=white" alt="pandas" />
<img src="https://img.shields.io/badge/FastAPI-009688.svg?style&logo=FastAPI&logoColor=white" alt="FastAPI" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
</p>

![GitHub top language](https://img.shields.io/github/languages/top/iusztinpaul/energy-forecasting?style&color=5D6D7E)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/iusztinpaul/energy-forecasting?style&color=5D6D7E)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/iusztinpaul/energy-forecasting?style&color=5D6D7E)
![GitHub license](https://img.shields.io/github/license/iusztinpaul/energy-forecasting?style&color=5D6D7E)
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

HTTPStatusError: 400

---

## ⚙️ Features

HTTPStatusError: 400

---


## 📂 Project Structure


```bash
repo
├── LICENSE
├── README.md
├── README_CICD.md
├── README_DEPLOY.md
├── airflow
│   ├── Dockerfile
│   ├── dags
│   │   ├── __init__.py
│   │   └── ml_pipeline_dag.py
│   ├── docker-compose.yaml
│   ├── poetry.lock
│   └── pyproject.toml
├── app-api
│   ├── Dockerfile
│   ├── README.md
│   ├── api
│   │   ├── __init__.py
│   │   ├── __main__.py
│   │   ├── application.py
│   │   ├── config.py
│   │   ├── schemas
│   │   │   ├── __init__.py
│   │   │   ├── area_values.py
│   │   │   ├── consumer_type_values.py
│   │   │   ├── health.py
│   │   │   └── predictions.py
│   │   └── views.py
│   ├── poetry.lock
│   ├── pyproject.toml
│   ├── requirements.txt
│   └── run.sh
├── app-frontend
│   ├── Dockerfile
│   ├── README.md
│   ├── frontend
│   │   ├── __init__.py
│   │   ├── components.py
│   │   ├── main.py
│   │   └── settings.py
│   ├── poetry.lock
│   ├── pyproject.toml
│   └── requirements.txt
├── app-monitoring
│   ├── Dockerfile
│   ├── README.md
│   ├── monitoring
│   │   ├── __init__.py
│   │   ├── components.py
│   │   ├── main.py
│   │   └── settings.py
│   ├── poetry.lock
│   ├── pyproject.toml
│   └── requirements.txt
├── batch-prediction-pipeline
│   ├── README.md
│   ├── batch_prediction_pipeline
│   │   ├── __init__.py
│   │   ├── batch.py
│   │   ├── data.py
│   │   ├── monitoring.py
│   │   ├── settings.py
│   │   └── utils.py
│   ├── poetry.lock
│   └── pyproject.toml
├── deploy
│   ├── app-docker-compose.local.yml
│   ├── app-docker-compose.yml
│   └── ml-pipeline.sh
├── feature-pipeline
│   ├── README.md
│   ├── feature_pipeline
│   │   ├── __init__.py
│   │   ├── clean_feature_store.py
│   │   ├── etl
│   │   │   ├── __init__.py
│   │   │   ├── cleaning.py
│   │   │   ├── extract.py
│   │   │   ├── load.py
│   │   │   └── validation.py
│   │   ├── feature_view.py
│   │   ├── pipeline.py
│   │   ├── settings.py
│   │   └── utils.py
│   ├── poetry.lock
│   └── pyproject.toml
├── images
│   ├── airflow_login_screenshot.png
│   ├── airflow_ml_pipeline_dag_overview_screenshot.png
│   ├── airflow_ml_pipeline_dag_screenshot.png
│   ├── airflow_variables_screenshot.png
│   ├── architecture.png
│   ├── forecasting_demo_screenshot.png
│   ├── gcp_expose_ports_firewall_rule_screenshot.png
│   ├── gcp_gcs_screenshot.png
│   ├── gcp_iap_for_tcp_firewall_rule.png
│   ├── gcp_ssh_screenshot.png
│   ├── gcp_vm_external_ip_screenshot.png
│   ├── github_actions_secrets_screenshot.png
│   ├── github_actions_see_cicd_screenshot.png
│   ├── github_actions_variables_screenshot.png
│   ├── gmail.png
│   ├── linkedin.png
│   ├── medium.png
│   ├── screenshot_introduction_video.png
│   ├── substack.png
│   └── twitter.png
└── training-pipeline
    ├── README.md
    ├── poetry.lock
    ├── pyproject.toml
    └── training_pipeline
        ├── __init__.py
        ├── best_config.py
        ├── configs
        │   ├── __init__.py
        │   └── gridsearch.py
        ├── data.py
        ├── hyperparameter_tuning.py
        ├── models.py
        ├── settings.py
        ├── train.py
        ├── transformers.py
        └── utils.py

20 directories, 104 files
```

---

## 🧩 Modules

<details closed><summary>Airflow</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                                                                                  | Module             |
|:-----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
| Dockerfile | The code snippet installs Python dependencies and updates the operating system package list for the Apache Airflow version 2.5.2 image. The installation of the dependencies allows for the processing of private PyPI server wheels and build-essential packages are also installed. The installations are executed as root and then switched back to the current user. | airflow/Dockerfile |

</details>

<details closed><summary>Api</summary>

| File           | Summary                                                                                                                                                                                                                                                                                                                                                                                                                      | Module                     |
|:---------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------|
| config.py      | The provided code snippet defines an enum class for log levels, a settings class for application parameters with environment variable configurability, and a function that returns the application settings with caching for optimization purposes. The settings class includes parameters such as the host, port, log level, version, worker count, project name, and Google Cloud Platform credentials.                    | app-api/api/config.py      |
| application.py | This code sets up a FastAPI app with CORS middleware that allows requests from any origin. It includes an API router and uses settings from a config file to specify endpoints and documentation URLs. The `get_app()` function returns the FastAPI app instance.                                                                                                                                                            | app-api/api/application.py |
| __main__.py    | This code snippet starts the application through the uvicorn framework. It gets the application instance from the api module, and uses the settings specified in the config file such as workers count, host, port, reload, log level and factory. The main function is called as the entry point of the application.                                                                                                        | app-api/api/__main__.py    |
| views.py       | This code snippet defines several API endpoints for retrieving and querying energy consumption data stored on Google Cloud Storage. The endpoints allow for retrieving unique consumer types and areas, retrieving forecasted predictions based on the given area and consumer type, and retrieving monitoring metrics. The code uses the FastAPI framework and the GCSFS library for interacting with Google Cloud Storage. | app-api/api/views.py       |

</details>

<details closed><summary>App-api</summary>

| File         | Summary                                                                                                                                                                                                                                                                                                           | Module               |
|:-------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------|
| Dockerfile   | This code sets up the environment for a Python application using Poetry as a package manager. It installs Poetry, copies and installs the required packages specified in the pyproject.toml and poetry.lock files, adds the application code, and sets up the run.sh script to execute when the container is run. | app-api/Dockerfile   |
| run.sh       | The provided code snippet executes the Python module'api' as the main program, using the Python interpreter located in the'/usr/local/bin' directory.                                                                                                                                                             | app-api/run.sh       |
| .env.default | This code snippet defines environment variables for a Google Cloud Platform project, a GCP bucket, and a service account JSON path. These variables likely provide necessary authentication and authorization information for an application that will access and read data from a GCP bucket.                    | app-api/.env.default |

</details>

<details closed><summary>App-frontend</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                                   | Module                  |
|:-----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------|
| Dockerfile | This code snippet sets up a Python 3.9.8 environment and installs Poetry to manage dependencies. It copies the application files, installs the dependencies using Poetry, and then sets the command to run the Streamlit application on port 8501. Additionally, it configures Poetry to not create virtual environments. | app-frontend/Dockerfile |

</details>

<details closed><summary>App-monitoring</summary>

| File       | Summary                                                                                                                                                                                                                                                                            | Module                    |
|:-----------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------|
| Dockerfile | The provided code snippet sets up a Python environment with poetry, then installs project dependencies listed in pyproject.toml. After dependencies are installed, it copies the rest of the code and starts a Streamlit application on port 8502 with the main monitoring script. | app-monitoring/Dockerfile |

</details>

<details closed><summary>Batch-prediction-pipeline</summary>

| File         | Summary                                                                                                                                                                                                                                                                                                                                                                                                                   | Module                                 |
|:-------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------|
| .env.default | The provided code snippet defines various keys and paths required for running an energy consumption prediction project. It includes the Feature Store API key, W&B API key, entity, and project names, Google Cloud project ID and bucket name, as well as a path to a service account JSON file. These configurations are necessary for accessing and storing data, as well as performing model training and evaluation. | batch-prediction-pipeline/.env.default |

</details>

<details closed><summary>Batch_prediction_pipeline</summary>

| File          | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Module                                                            |
|:--------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------|
| monitoring.py | The provided code snippet computes metrics on the latest n_days of predictions by loading data from a feature store and comparing it to ground truth data. It uses the mean absolute percentage error (MAPE) to compute the metrics. The resulting metrics are saved in a monitoring file and the ground truth data is saved in a separate file.                                                                                                                   | batch-prediction-pipeline/batch_prediction_pipeline/monitoring.py |
| batch.py      | This code provides a function for batch prediction of energy consumption using a trained machine learning model and feature data stored in a feature store. It loads the feature and model metadata, connects to the feature store, loads the data from the feature store, loads the trained model, makes predictions using the model, and saves the predictions to Google Cloud Storage. It also saves the predictions to a parquet file for monitoring purposes. | batch-prediction-pipeline/batch_prediction_pipeline/batch.py      |
| utils.py      | The provided code snippet contains functions for logging, loading and saving JSON files, as well as working with Google Cloud Storage buckets to write and read Pandas dataframes in Parquet format. It also imports necessary modules and settings from other files and modules. These functions can be used to support building a batch prediction pipeline.                                                                                                     | batch-prediction-pipeline/batch_prediction_pipeline/utils.py      |
| settings.py   | This code snippet imports necessary modules and defines two functions: load_env_vars() and get_root_dir(). The load_env_vars() function loads environment variables from.env.default and.env files, while the get_root_dir() function returns the root directory of the project. The code also sets the ML_PIPELINE_ROOT_DIR and OUTPUT_DIR variables based on the output directory of the project and the loaded environment variables.                           | batch-prediction-pipeline/batch_prediction_pipeline/settings.py   |
| data.py       | The provided code defines a function that loads data from a feature store for a given time range. It takes in the feature store, feature view version, start and end datetimes, and target feature name as inputs, and returns a tuple of exogenous variables and the time series to be forecasted. The function uses the pandas library to manipulate the data and the HSFS library to retrieve data from the feature store.                                      | batch-prediction-pipeline/batch_prediction_pipeline/data.py       |

</details>

<details closed><summary>Configs</summary>

| File          | Summary                                                                                                                                                                                                                                                                                                                                                                           | Module                                                    |
|:--------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------|
| gridsearch.py | The code snippet contains a dictionary of hyperparameters that will be used in a grid search to find the optimal set of values for a time series forecasting model. The hyperparameters include the number of estimators, learning rate, maximum depth, regularization lambda, and lag features. The search is aimed at minimizing the validation mean absolute percentage error. | training-pipeline/training_pipeline/configs/gridsearch.py |

</details>

<details closed><summary>Dags</summary>

| File               | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                | Module                          |
|:-------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------|
| ml_pipeline_dag.py | This code snippet defines a DAG for a machine learning pipeline, which includes tasks for running feature engineering, training models, and batch prediction. The DAG includes branching logic to decide whether to run hyperparameter tuning, and uses Airflow variables to set configurable parameters such as the delay in the data and the URL to fetch data from. The tasks are defined as Python functions executed within virtual environments. | airflow/dags/ml_pipeline_dag.py |
| .env.default       | This code snippet defines several variables that are used to authenticate and connect to various APIs and cloud services. These include the feature store API key, WandB API key, entity, and project, as well as Google Cloud project, bucket name, and service account JSON path. These credentials and settings are important for running automated data pipelines or other processes in an Airflow DAG.                                            | airflow/dags/.env.default       |

</details>

<details closed><summary>Deploy</summary>

| File           | Summary                                                                                                                                                                                                                                                                                                                                                                                                                     | Module                |
|:---------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
| ml-pipeline.sh | This code snippet builds and publishes three packages (feature-pipeline, training-pipeline, and batch-prediction-pipeline) for running pipelines from the command line interface. The pipelines are executed in their respective directories, and the my-pypi repository must be defined in the project's poetry.toml file. This ensures that the pipelines are easily accessible and can be used by others in the project. | deploy/ml-pipeline.sh |

</details>

<details closed><summary>Etl</summary>

| File          | Summary                                                                                                                                                                                                                                                                                                                                                                                                      | Module                                              |
|:--------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------|
| load.py       | The code snippet defines a function'to_feature_store' that takes a pandas DataFrame, a validation expectation suite, and a feature group version as input. It then performs validation on the data, saves it to a feature store, and adds feature descriptions and statistics to the feature group. The feature group is created in a feature store using Hopsworks.                                         | feature-pipeline/feature_pipeline/etl/load.py       |
| extract.py    | The provided code snippet extracts data from the DK energy consumption API by querying the API with specified parameters and parsing the response. It returns a tuple containing a Pandas DataFrame with the exported data and a dictionary of metadata. The function also computes the export window based on input parameters and the current time. Logging is used to track the progress of the function. | feature-pipeline/feature_pipeline/etl/extract.py    |
| cleaning.py   | The provided code snippet consists of three functions: rename_columns renames certain columns of a given Pandas DataFrame, cast_columns changes the data types of specific columns, and encode_area_column encodes the "area" column from string values to integers. The functions are designed to preprocess energy consumption data and ensure it matches the required schema for further analysis.        | feature-pipeline/feature_pipeline/etl/cleaning.py   |
| validation.py | This code snippet builds an ExpectationSuite for validating a dataset of energy consumption. It defines expectations for column names, column count, column values not being null, distinct values for certain columns and column data types. The resulting ExpectationSuite can be used to validate new datasets for consistency with the defined expectations.                                             | feature-pipeline/feature_pipeline/etl/validation.py |

</details>

<details closed><summary>Feature-pipeline</summary>

| File         | Summary                                                                                                                                                                                                                                         | Module                        |
|:-------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------|
| .env.default | The code snippet declares and assigns values to various API keys and service account paths for Google Cloud and Weights & Biases. These are essential for authentication and access to the relevant services in the energy consumption project. | feature-pipeline/.env.default |

</details>

<details closed><summary>Feature_pipeline</summary>

| File                   | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Module                                                   |
|:-----------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------|
| clean_feature_store.py | The provided code snippet defines a function called "clean()" that is used to delete all feature views, training datasets, and feature groups from a feature store called "energy_consumption". This function is invoked using the Fire CLI library. The script requires the hopsworks and feature_pipeline modules to be imported to function properly.                                                                                                                                                                                                                      | feature-pipeline/feature_pipeline/clean_feature_store.py |
| utils.py               | This code snippet defines three functions: getting a logger, saving a dictionary as a JSON file, and loading a JSON file as a dictionary. The logger function returns a logger object. The save_json function saves a dictionary as a JSON file while the load_json function loads a JSON file and returns a dictionary object. The code uses the logging, pathlib, and json libraries, as well as the settings module.                                                                                                                                                       | feature-pipeline/feature_pipeline/utils.py               |
| pipeline.py            | The provided code snippet contains a function "run" that extracts data from an API, performs data cleaning and transformation using a function "transform", builds validation expectations, validates the data, and loads it to the feature store. The program accepts optional parameters such as the export end reference datetime, days delay, days export, URL of the API, and feature group version. The function returns a dictionary containing metadata of the pipeline. The program uses the Fire library to create a command-line interface for the function "run". | feature-pipeline/feature_pipeline/pipeline.py            |
| feature_view.py        | The code creates a new feature view version and training dataset based on a given feature group version and start/end datetimes. It first loads cached metadata or gets a feature group version if not specified, then logs into the Hopsworks API, deletes old feature views and creates a new feature view and training dataset. Finally, it saves metadata and returns the feature view version and training dataset version.                                                                                                                                              | feature-pipeline/feature_pipeline/feature_view.py        |
| settings.py            | The code snippet loads environment variables from.env.default and.env files and returns them as a dictionary. It also gets the root directory of the project and creates an output directory. The aim is to set up the necessary environment variables and directory structure for use in a machine learning pipeline.                                                                                                                                                                                                                                                        | feature-pipeline/feature_pipeline/settings.py            |

</details>

<details closed><summary>Frontend</summary>

| File          | Summary                                                                                                                                                                                                                                                                                                                                                                                                                            | Module                              |
|:--------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------|
| settings.py   | This code imports the URL class from the yarl library and defines the constants TITLE and API_URL as a string and URL object, respectively. The API_URL is set to a local IP address and port number for accessing an API. The code snippet aims to provide easy access to the API endpoint for energy consumption forecasting.                                                                                                    | app-frontend/frontend/settings.py   |
| components.py | This code snippet builds a plotly graph for energy consumption predictions and observations for a specific area and consumer type. It queries an API for predictions data and builds pandas dataframes to format the data for plotting. The resulting plot displays the observations and predictions on a graph with datetime on the x-axis and energy consumption on the y-axis.                                                  | app-frontend/frontend/components.py |
| main.py       | The provided code is a Python script that uses the Streamlit and Requests libraries to build an interactive dropdown interface which allows users to select a price area and consumer type. Information about these choices is obtained by sending requests to an API, and if both choices have been made, a data plot is generated using the Plotly library. The script also sets the page title and displays it using Streamlit. | app-frontend/frontend/main.py       |

</details>

<details closed><summary>Monitoring</summary>

| File          | Summary                                                                                                                                                                                                                                                                                                                                                                                             | Module                                  |
|:--------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------|
| settings.py   | The code snippet imports the URL module from yarl and defines a constant variable for the API URL. It also defines a constant variable for the page title which indicates it is related to monitoring energy consumption.                                                                                                                                                                           | app-monitoring/monitoring/settings.py   |
| components.py | The code snippet consists of functions that build plotly graphs for monitoring metrics and energy consumption data. The code collects data from an API and creates a pandas dataframe, resamples it to hourly frequency and plots it using plotly. If the API response is invalid, the code builds empty dataframes.                                                                                | app-monitoring/monitoring/components.py |
| main.py       | The code snippet imports necessary libraries, sets the page configuration and title using Streamlit. It creates a plot for metrics over time using the Plotly library and a dropdown menu for area and consumer type selection using values obtained from an API endpoint. If both area and consumer type values are selected in the dropdown, a plot for data is created using the Plotly library. | app-monitoring/monitoring/main.py       |

</details>

<details closed><summary>Root</summary>

| File         | Summary                                                                                                                                                                                                                                                                                                                                                              | Module       |
|:-------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------|
| .env.default | The provided code snippet sets several API keys, project names, and file paths, which are later used in an energy consumption project. These include keys for Feature Store and Weights & Biases (W&B), and project names for Google Cloud and W&B. It also sets the name and location of a Google Cloud Storage bucket and the path to a service account JSON file. | .env.default |

</details>

<details closed><summary>Schemas</summary>

| File                    | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Module                                      |
|:------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------|
| predictions.py          | The code snippet defines three Pydantic BaseModels-PredictionResults, MonitoringMetrics, and MonitoringValues. PredictionResults contains lists for datetime_utc, energy_consumption, preds_datetime_utc, and preds_energy_consumption. MonitoringMetrics contains lists for datetime_utc and mape. MonitoringValues contains lists for y_monitoring_datetime_utc, y_monitoring_energy_consumption, predictions_monitoring_datetime_utc, and predictions_monitoring_energy_consumptionc. These BaseModels can be used to serialize/deserialize data and enforce data types in Python applications. | app-api/api/schemas/predictions.py          |
| health.py               | The provided code snippet defines a Pydantic model called `Health` with two attributes, `name` and `api_version`, both of which are strings. This model can be used for validation of data that needs to conform to the specified attribute types.                                                                                                                                                                                                                                                                                                                                                 | app-api/api/schemas/health.py               |
| area_values.py          | The provided code defines a Pydantic model called UniqueArea with a single attribute'values' that is a list of integers. Pydantic is a library that provides data validation and parsing capabilities, enabling developers to define data models with a set of predefined validation rules. The typing module is used to specify the expected data types of the attributes.                                                                                                                                                                                                                        | app-api/api/schemas/area_values.py          |
| consumer_type_values.py | This code snippet defines a Pydantic BaseModel subclass called UniqueConsumerType, which has a single attribute called "values" that is a list of integers. The Pydantic library provides data validation and serialization functionality for Python data structures, making it easier to work with data in a type-safe and structured way.                                                                                                                                                                                                                                                        | app-api/api/schemas/consumer_type_values.py |

</details>

<details closed><summary>Training-pipeline</summary>

| File         | Summary                                                                                                                                                                                                                                                                                                                              | Module                         |
|:-------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------|
| .env.default | The provided code snippet declares variables for different API keys and project configurations related to feature store, tracking, cloud project, and bucket name. These variables are likely used to configure various services and tools used in an energy consumption prediction project, such as Google Cloud Storage and WandB. | training-pipeline/.env.default |

</details>

<details closed><summary>Training_pipeline</summary>

| File                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Module                                                       |
|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------|
| best_config.py           | The provided code snippet defines a function that uploads the best configuration of a hyperparameter optimization sweep to a Weights and Biases (W&B) artifact. The function takes in an optional sweep ID and uses the W&B API to retrieve the sweep and the best run within the sweep. It then logs the best configuration and validation results to a W&B artifact and finishes the run. The code also includes a note about a bug in W&B sweeps that affects the logging of the best model.                                                                                                                                       | training-pipeline/training_pipeline/best_config.py           |
| models.py                | The code provides functions to build Sktime forecasting models using lightgbm regressor and naive forecaster. The models have time series transformers for feature engineering, such as attaching area and consumer type and extracting date-time features. The models also support defaults for windowing parameters like lag, mean, and standard deviation.                                                                                                                                                                                                                                                                         | training-pipeline/training_pipeline/models.py                |
| transformers.py          | The provided code defines a transformer class called "AttachAreaConsumerType" that extracts the area and consumer type from the index to the input data. The transformer has methods to transform and inverse transform data. The class also includes various tags that describe the capabilities of the transformer.                                                                                                                                                                                                                                                                                                                 | training-pipeline/training_pipeline/transformers.py          |
| utils.py                 | The provided code snippet includes various utility functions such as saving and loading data to/from JSON and models to/from disk, loading data from a parquet file, getting logging instances, initializing WandB runs, checking if a WandB artifact exists, and getting the latest version of a WandB artifact. These functions are aimed to simplify the training pipeline and integration with the WandB tracking tool.                                                                                                                                                                                                           | training-pipeline/training_pipeline/utils.py                 |
| train.py                 | The provided code snippet defines functions for training, evaluating and forecasting time series models, using sktime library for performance metrics and LightGBM for building models. The main function from_best_config loads data from the feature store, trains and evaluates the best model found in a hyperparameter optimization run, saves the model and its metadata to wandb and Hopsworks, and returns the metadata. It also logs results and images to wandb, and attaches links to the saved artifacts in the feature view and training dataset of the feature store.                                                   | training-pipeline/training_pipeline/train.py                 |
| settings.py              | This code snippet imports necessary libraries and defines functions to load environment variables from.env files and get the root directory of a project. It also sets up an output directory and loads settings from the environment variables using the defined functions.                                                                                                                                                                                                                                                                                                                                                          | training-pipeline/training_pipeline/settings.py              |
| hyperparameter_tuning.py | This code snippet runs a hyperparameter optimization search for a forecasting model using W&B sweeps. It loads a dataset from a feature store, builds a model, and trains and evaluates the model using cross-validation. The results of the search are logged to W&B and metadata about the search is saved to a JSON file.                                                                                                                                                                                                                                                                                                          | training-pipeline/training_pipeline/hyperparameter_tuning.py |
| data.py                  | This code defines two functions for preparing and loading time series data from a feature store for use in a forecasting model. The `load_dataset_from_feature_store` function loads data from the feature store, logs metadata about the feature view, and splits the data into train and test sets using the `prepare_data` function. The `prepare_data` function structures the data for training, sets the index, prepares exogenous variables, and splits the data into train and test sets using `temporal_train_test_split` from the `sktime` library. WandB is used for logging metadata and artifacts during both functions. | training-pipeline/training_pipeline/data.py                  |

</details>

---

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - [ℹ️ Requirement 1]
> - [ℹ️ Requirement 2]
> - [...]

### 🖥 Installation

1. Clone the energy-forecasting repository:
```sh
git clone https://github.com/iusztinpaul/energy-forecasting
```

2. Change to the project directory:
```sh
cd energy-forecasting
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

### 🤖 Using energy-forecasting

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
