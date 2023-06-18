
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
energy-forecasting
</h1>
<h3 align="center">📍 Power up your predictions with energy-forecasting on GitHub</h3>
<h3 align="center">⚙️ Developed with the software and tools below:</h3>

<p align="center">
<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=for-the-badge&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash" />
<img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=for-the-badge&logo=Streamlit&logoColor=white" alt="Streamlit" />
<img src="https://img.shields.io/badge/Redis-DC382D.svg?style=for-the-badge&logo=Redis&logoColor=white" alt="Redis" />
<img src="https://img.shields.io/badge/Plotly-3F4F75.svg?style=for-the-badge&logo=Plotly&logoColor=white" alt="Plotly" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="Python" />

<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=for-the-badge&logo=Docker&logoColor=white" alt="Docker" />
<img src="https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="pandas" />
<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=for-the-badge&logo=FastAPI&logoColor=white" alt="FastAPI" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="Markdown" />
</p>
</div>

---

## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [💫 Features](#-features)
- [📂 Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🚀 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

Error while fetching summary: 2
Client error '400 Bad Request' for url 'https://api.openai.com/v1/chat/completions'
For more information check: https://httpstatuses.com/400

---

## 💫 Features

Error while fetching summary: 3
Client error '400 Bad Request' for url 'https://api.openai.com/v1/chat/completions'
For more information check: https://httpstatuses.com/400

---


<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

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

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 🧩 Modules

<details closed><summary>Airflow</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                                                                                     | Module             |
|:-----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
| Dockerfile | The code snippet is written in Dockerfile format and is used for building a Docker container for Apache Airflow version 2.5.2. It installs necessary Python dependencies required for processing wheels from a private PyPI server. The code switches to root user, updates and upgrades packages, installs required packages, and then switches back to the previous user. | airflow/Dockerfile |

</details>

<details closed><summary>Api</summary>

| File           | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Module                     |
|:---------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------|
| config.py      | The code snippet defines an enum class for logging levels and a class for application settings that can be configured with environment variables. It also includes a function that returns the application settings using caching for optimization purposes. The settings include general configurations such as the host, port, log level, and number of workers, as well as optional Google Cloud Platform credentials.                                                                    | app-api/api/config.py      |
| application.py | The provided code snippet creates a FastAPI app that includes a router for handling API requests. It also includes middleware for enabling Cross-Origin Resource Sharing (CORS) and sets up documentation and OpenAPI endpoints. The app is configured with settings obtained from the'api.config' module.                                                                                                                                                                                   | app-api/api/application.py |
| __main__.py    | The code snippet is an entry point for a web application built using FastAPI framework, using the Uvicorn server. It retrieves application settings from the config file and passes them to the Uvicorn server for running the application. It allows for customization of host, port, workers, and log levels.                                                                                                                                                                              | app-api/api/__main__.py    |
| views.py       | This code snippet defines a FastAPI router that exposes various endpoints for retrieving data related to energy consumption predictions. The data is downloaded from Google Cloud Storage using the gcsfs library. Endpoints are provided for retrieving unique consumer types and areas, as well as for retrieving predictions and monitoring metrics based on a given area and consumer type. The API responds to requests with JSON-encoded data in accordance with the provided schemas. | app-api/api/views.py       |

</details>

<details closed><summary>App-api</summary>

| File         | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Module               |
|:-------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------|
| Dockerfile   | The code snippet sets up a Python 3.9.4 environment with Poetry installed. It installs dependencies specified in pyproject.toml and poetry.lock files, and copies the app-api directory to the working directory. Finally, it gives permission to run a shell script named "run.sh" and executes it when the container is started.                                                                                                                                                                                      | app-api/Dockerfile   |
| run.sh       | The code snippet uses the Python interpreter to execute the "api" module located at the /usr/local/bin/python directory. This could be a script or a package that provides a set of APIs to be used by other programs. The "-m" option specifies that the module should be executed as the main program.                                                                                                                                                                                                                | app-api/run.sh       |
| .env.default | The code snippet defines three variables in a Python script for accessing a Google Cloud Platform (GCP) project named "energy_consumption". The variables specify the name of a GCP storage bucket, "hourly-batch-predictions", and the file path for a service account JSON key, "/app/src/credentials/gcp/energy_consumption/read-buckets.json", used for read access to GCP storage buckets. These variables can be utilized in subsequent code instructions to programmatically access the specified GCP resources. | app-api/.env.default |

</details>

<details closed><summary>App-frontend</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                               | Module                  |
|:-----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------|
| Dockerfile | This code snippet sets up a Docker container with Python 3.9.8 and installs Poetry (a package manager) to manage dependencies. It copies the necessary files for installing dependencies and installs them to speed up the build process. Then, it copies the rest of the code and runs a Streamlit app on port 8501. | app-frontend/Dockerfile |

</details>

<details closed><summary>App-monitoring</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                       | Module                    |
|:-----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------|
| Dockerfile | This code sets up a Docker container for a Python application using Streamlit for monitoring. Poetry is used to install package dependencies and the application is copied to the container's working directory. Finally, the container is configured to run the monitoring app using Streamlit on port 8502. | app-monitoring/Dockerfile |

</details>

<details closed><summary>Batch-prediction-pipeline</summary>

| File         | Summary                                                                                                                                                                                                                                                                                                                   | Module                                 |
|:-------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------|
| .env.default | The code snippet defines various keys and configurations required for accessing different services such as the feature store API, WandB, Google Cloud, and its bucket name for storing batch predictions. The snippet also specifies the path to the service account JSON file needed to access the Google Cloud project. | batch-prediction-pipeline/.env.default |

</details>

<details closed><summary>Batch_prediction_pipeline</summary>

| File          | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Module                                                            |
|:--------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------|
| monitoring.py | The provided code snippet computes performance metrics (MAPE) for a forecasting model's latest predictions and saves them to a Parquet file. It loads old predictions from a cached file, retrieves new ground truths from a feature store, and computes metrics only on data that has ground truth. The output files include metrics_monitoring.parquet and y_monitoring.parquet.                                                                                                                              | batch-prediction-pipeline/batch_prediction_pipeline/monitoring.py |
| batch.py      | The code snippet is a Python function for doing batch predictions. It loads data from a feature store, loads a trained machine learning model from a model registry, makes predictions using the model, saves the input data, target data, and predictions to a cloud storage bucket, and saves the predictions to the bucket for monitoring. The function takes several optional parameters for customizing the predictions.                                                                                   | batch-prediction-pipeline/batch_prediction_pipeline/batch.py      |
| utils.py      | The provided code snippet includes functions for logging, loading and saving JSON files, loading ML models, and interfacing with Google Cloud Storage to read and write parquet files. The code uses the `joblib` and `pandas` libraries for model loading and DataFrame manipulation, respectively. The code also relies on an external `settings` module for configuration.                                                                                                                                   | batch-prediction-pipeline/batch_prediction_pipeline/utils.py      |
| settings.py   | This code snippet imports necessary packages, sets up environment variables for a machine learning pipeline, and creates a directory for saving outputs. The `load_env_vars` function loads environment variables from `.env.default` and `.env` files, while `get_root_dir` function gets the root directory of the project. Finally, the `ML_PIPELINE_ROOT_DIR` and `OUTPUT_DIR` variables are defined using the output directory relative to `ML_PIPELINE_ROOT_DIR` and saved in the `OUTPUT_DIR` directory. | batch-prediction-pipeline/batch_prediction_pipeline/settings.py   |
| data.py       | The provided code defines a function that loads data from a feature store for a given time range, specified by start and end datetimes, and a target feature name. It uses the HSFS library to retrieve data from a feature view and returns a tuple of exogenous variables and the time series to be forecasted. The function also sets the index of the data and prepares the input and output data for use in time series forecasting.                                                                       | batch-prediction-pipeline/batch_prediction_pipeline/data.py       |

</details>

<details closed><summary>Configs</summary>

| File          | Summary                                                                                                                                                                                                                                                                                                                                                         | Module                                                    |
|:--------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------|
| gridsearch.py | The provided code defines a dictionary containing configurations for hyperparameter tuning using a grid search method. The configurations include parameters related to the forecaster estimator, daily season selection, window summarization, and number of jobs to use. The metric used for optimization is validation MAPE, with the goal of minimizing it. | training-pipeline/training_pipeline/configs/gridsearch.py |

</details>

<details closed><summary>Dags</summary>

| File               | Summary                                                                                                                                                                                                                                                                                                                                                                                                                  | Module                          |
|:-------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------|
| ml_pipeline_dag.py | This code defines an Airflow DAG called "ml_pipeline" that executes a machine learning pipeline. It includes tasks for running a feature pipeline, creating a feature view, hyperparameter tuning, model training, computing monitoring metrics, and batch prediction. The DAG structure includes branching for whether or not to run hyperparameter tuning and uses Airflow variables to customize pipeline parameters. | airflow/dags/ml_pipeline_dag.py |
| .env.default       | The code snippet defines several global variables containing API keys, project names, and file paths for a machine learning project focused on energy consumption. These variables are likely used throughout the rest of the codebase to connect to various services and resources such as a feature store, WandB (a machine learning experiment tracking tool), and Google Cloud Storage.                              | airflow/dags/.env.default       |

</details>

<details closed><summary>Deploy</summary>

| File           | Summary                                                                                                                                                                                                                                                                                                                                                                              | Module                |
|:---------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
| ml-pipeline.sh | The Bash script builds and publishes three Python packages-feature-pipeline, training-pipeline, and batch-prediction-pipeline-to a PyPI repository named'my-pypi'. It changes directories to each pipeline's location and executes the'poetry build' and'poetry publish' commands. The script assumes that the project's poetry.toml file has'my-pypi' defined as a PyPI repository. | deploy/ml-pipeline.sh |

</details>

<details closed><summary>Etl</summary>

| File          | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Module                                              |
|:--------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------|
| load.py       | The provided code snippet defines a function to upload data to a feature store in Hopsworks. The function takes in a Pandas DataFrame and a validation expectation suite, performs validation on the data using the suite, creates a feature group in the feature store, uploads the data to the feature group, adds feature descriptions, updates statistics, and returns the feature group. The aim of the function is to provide a streamlined workflow for uploading and managing data in a feature store. | feature-pipeline/feature_pipeline/etl/load.py       |
| extract.py    | The code defines a function that extracts data from an external API for energy consumption in Denmark. It takes in several parameters such as the export window, days of delay, and API URL. It then queries the API using requests, parses the JSON response, creates a Pandas DataFrame from the records, and returns both the DataFrame and metadata in a tuple. The function also logs information using the logging module.                                                                               | feature-pipeline/feature_pipeline/etl/extract.py    |
| cleaning.py   | The provided code snippet contains three functions that operate on a Pandas DataFrame object. The first function renames the columns of the DataFrame to match a specific schema, while the second function casts the columns to their correct data types. The third function encodes the values of the "area" column into integers based on a pre-defined mapping. Overall, these functions serve to clean and prepare the DataFrame for further analysis or manipulation.                                    | feature-pipeline/feature_pipeline/etl/cleaning.py   |
| validation.py | This code defines a function to build an expectation suite for validating a dataset on energy consumption. It checks that the dataset has 4 columns named datetime_utc, area, consumer_type, and energy_consumption, that datetime_utc is not null, that area is an integer within the set of (0,1,2), that consumer_type is a specific integer type, and that energy_consumption is a non-negative float. The function returns the expectation suite for use in data validation.                              | feature-pipeline/feature_pipeline/etl/validation.py |

</details>

<details closed><summary>Feature-pipeline</summary>

| File         | Summary                                                                                                                                                                                                                                  | Module                        |
|:-------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------|
| .env.default | The provided code defines API keys, entity, and project names for Feature Store, Weights and Biases, and Google Cloud. It also specifies the Google Cloud bucket name and service account credentials for an energy consumption project. | feature-pipeline/.env.default |

</details>

<details closed><summary>Feature_pipeline</summary>

| File                   | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Module                                                   |
|:-----------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------|
| clean_feature_store.py | The provided code snippet defines a function named'clean' that deletes feature views and training datasets from the feature store for the'energy_consumption' project. The function is executed when the script is called on the command line and utilizes the'fire' and'hopsworks' libraries.                                                                                                                                                                                                                                                                                                                                | feature-pipeline/feature_pipeline/clean_feature_store.py |
| utils.py               | The provided code snippet contains three functions: get_logger(), save_json(), and load_json(). The get_logger() function sets up a logger with a given name. The save_json() function saves a given dictionary as a JSON file, while the load_json() function loads a JSON file and returns its contents as a dictionary. All three functions utilize the Python logging and json modules.                                                                                                                                                                                                                                   | feature-pipeline/feature_pipeline/utils.py               |
| pipeline.py            | This code extracts data from an API, performs data cleaning and transformation operations, validates the data, and loads it into a feature store. The user can specify parameters such as the API URL, days to export, and feature group version. The code also logs messages to provide status updates and saves pipeline metadata to a JSON file.                                                                                                                                                                                                                                                                           | feature-pipeline/feature_pipeline/pipeline.py            |
| feature_view.py        | The code creates a feature view version and a training dataset based on a given feature group version and start and end datetimes. It logs into a project in Hopsworks, deletes old feature views, creates a new feature view in the given feature group version, and creates a training dataset with the specified start and end datetimes. It then saves metadata and returns it. The script can be run from the command line and takes optional arguments for feature_group_version, start_datetime, and end_datetime.                                                                                                     | feature-pipeline/feature_pipeline/feature_view.py        |
| settings.py            | This code snippet defines two utility functions to help load environment variables and get the root directory of a project. "load_env_vars" loads environment variables from ".env.default" and ".env" files located in a specified root directory and returns a dictionary containing the environment variables. "get_root_dir" returns the root directory of the project by getting the value of an environment variable called "ML_PIPELINE_ROOT_DIR" or returning the default value if the variable is not set. The code also creates an output directory and loads the environment variables into a "SETTINGS" variable. | feature-pipeline/feature_pipeline/settings.py            |

</details>

<details closed><summary>Frontend</summary>

| File          | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                          | Module                              |
|:--------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------|
| settings.py   | The code imports URL from the yarl library and defines a TITLE variable as "Energy Consumption Forecasting". It also sets the API_URL variable to the URL "http://172.17.0.1:8001/api/v1".                                                                                                                                                                                                                                                       | app-frontend/frontend/settings.py   |
| components.py | The provided code snippet includes a function that builds a Plotly graph for energy consumption data based on API responses, utilizing Pandas to build dataframes for plotting and Plotly to create visualizations. The function also includes error handling if the API response is invalid, producing an empty dataframe. Overall, the code provides a straightforward approach for producing plot visualizations for energy consumption data. | app-frontend/frontend/components.py |
| main.py       | The provided code snippet imports necessary packages, sets page configuration and gets area and consumer type values from an API using dropdowns in Streamlit. It then checks if both area and consumer type have values listed and creates a plot for the corresponding data using the Plotly library. The objective of this code snippet is to display data related to Danish energy companies based on user input.                            | app-frontend/frontend/main.py       |

</details>

<details closed><summary>Monitoring</summary>

| File          | Summary                                                                                                                                                                                                                                                                                                                                                                                                                           | Module                                  |
|:--------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------|
| settings.py   | The code imports the URL class from the yarl library and sets the value of the TITLE variable to "Monitoring | Energy Consumption". It also sets the value of the API_URL variable to a URL object representing the API endpoint "http://172.17.0.1:8001/api/v1".                                                                                                                                                                 | app-monitoring/monitoring/settings.py   |
| components.py | The provided code snippet defines functions to build two different plotly graphs for monitoring metrics and energy consumption data. The functions make requests to an API, handle possible errors, and create scatter plots using plotly's graph_objects module. The build_dataframe function is used to prepare the data for plotting by converting timestamps to datetime objects and resampling the data to hourly frequency. | app-monitoring/monitoring/components.py |
| main.py       | This code snippet imports necessary modules, sets page configuration, builds and displays plots for metrics over time and data based on user-selected values from dropdowns for area and consumer type. Requests are made to an API for dropdown options and plot data.                                                                                                                                                           | app-monitoring/monitoring/main.py       |

</details>

<details closed><summary>Root</summary>

| File         | Summary                                                                                                                                                                                                                                                                                 | Module       |
|:-------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------|
| .env.default | The code snippet defines a set of variables that store various API keys, project names, and file paths for a machine learning project focused on energy consumption. These variables are likely used throughout the project to access and manipulate data, models, and other resources. | .env.default |

</details>

<details closed><summary>Schemas</summary>

| File                    | Summary                                                                                                                                                                                                                                                                                                               | Module                                      |
|:------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------|
| predictions.py          | The code snippet defines three Pydantic models: PredictionResults, MonitoringMetrics, and MonitoringValues. Each model has several attributes that define the data it can hold, including lists of integers and floats. These models can be used to validate and manipulate data objects in a Python program.         | app-api/api/schemas/predictions.py          |
| health.py               | The code snippet defines a Pydantic BaseModel called "Health" with two attributes: "name" and "api_version". This model can be used to ensure strict typing and validation of incoming data for an API endpoint that returns information about the health of a service or application.                                | app-api/api/schemas/health.py               |
| area_values.py          | The code snippet defines a Pydantic BaseModel known as UniqueArea that has a single attribute called "values"-a list of integers. This BaseModel can be used to validate and serialize data that conforms to this schema. The typing module is imported to specify the types of values and lists that should be used. | app-api/api/schemas/area_values.py          |
| consumer_type_values.py | The provided code defines a Pydantic model called UniqueConsumerType, which has a single attribute called values that is a list of integers. Pydantic provides data validation and serialization capabilities. The typing module is used to provide type hints for function signatures.                               | app-api/api/schemas/consumer_type_values.py |

</details>

<details closed><summary>Training-pipeline</summary>

| File         | Summary                                                                                                                                                                                                                                                                                                                      | Module                         |
|:-------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------|
| .env.default | The provided code snippet defines a set of variables that contain API keys and project information required to access different cloud services, including feature store, weight & bias, and Google Cloud Platform. The variables are necessary for setting up a machine learning pipeline for energy consumption prediction. | training-pipeline/.env.default |

</details>

<details closed><summary>Training_pipeline</summary>

| File                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Module                                                       |
|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------|
| best_config.py           | The provided code snippet defines a Python function that uploads the best configuration from a sweep to the "best_experiment" artifact in the Weights & Biases platform. The function uses the wandb package to access the W&B API and retrieve metadata about the sweep, and it also logs information about the best run and its configuration. The script is designed to be run as a standalone program using the Fire CLI.                                                                                                                                           | training-pipeline/training_pipeline/best_config.py           |
| models.py                | The code defines functions to build Sktime models for forecasting time series data. The `build_model` function uses a LGBMRegressor as the forecasting model, and supports windowing of lag, mean, and standard deviation features. The `build_baseline_model` function builds a simple NaiveForecaster model that predicts the last value given a seasonal periodicity.                                                                                                                                                                                                | training-pipeline/training_pipeline/models.py                |
| transformers.py          | The provided code contains a transformer class called "AttachAreaConsumerType" that has two methods: "_transform" and "_inverse_transform". The "_transform" method takes input data and extracts the area and consumer type from the index, while the "_inverse_transform" method drops these two features from the input data. The class also includes various tags that describe the capabilities and requirements of the transformer.                                                                                                                               | training-pipeline/training_pipeline/transformers.py          |
| utils.py                 | The provided code snippet defines various utility functions for working with data, models, logging, and Weights and Biases (W&B). These functions include saving and loading data as JSON or parquet files, saving and loading machine learning models, setting up a logger, initializing and checking W&B runs and artifacts. The functions are designed to be easily customizable and adaptable to different projects.                                                                                                                                                | training-pipeline/training_pipeline/utils.py                 |
| train.py                 | The code snippet defines a function `from_best_config()` that loads a dataset from a feature store, trains and evaluates a machine learning model on the dataset, saves the trained model, and attaches it to a feature store to create a new version. The function uses various packages, including Sktime, Matplotlib, Pandas, Wandb, and Hopsworks. The evaluation metrics include mean absolute percentage error (MAPE) and mean squared percentage error (MSPE). The function also logs the experiment results using Wandb and saves the metadata using Hopsworks. | training-pipeline/training_pipeline/train.py                 |
| settings.py              | This code snippet imports necessary libraries such as os, warnings, pathlib, typing, and matplotlib. It defines two functions-load_env_vars() to load environment variables from.env.default and.env files, and get_root_dir() to get the root directory of the project. Finally, it sets the project root directory and output directory using the defined functions.                                                                                                                                                                                                  | training-pipeline/training_pipeline/settings.py              |
| hyperparameter_tuning.py | This code snippet implements a hyperparameter optimization search for time series forecasting models. It uses the sktime library to perform cross-validation and evaluate the model's performance using mean absolute percentage error. The hyperparameter optimization search is done using WandB sweeps and the resulting metadata is saved in a JSON file. The code also includes functions for loading data from a feature store and rendering the cross-validation scheme, which is logged to WandB as an image.                                                   | training-pipeline/training_pipeline/hyperparameter_tuning.py |
| data.py                  | The provided code snippet loads data from a feature store, prepares it for training, and splits it into train and test sets. The sktime library is used to split the time series data. The prepared data is logged using WandB for monitoring and analysis.                                                                                                                                                                                                                                                                                                             | training-pipeline/training_pipeline/data.py                  |

</details>

---

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - [📌  PREREQUISITE-1]
> - [📌  PREREQUISITE-2]
> - ...

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

> - [X] [📌  Task 1: Implement X]
> - [ ] [📌  Task 2: Refactor Y]
> - [ ] [📌  Task 3: Optimize Z]
> - [ ] [📌  Task 4: Fix Bug A]


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

This project is licensed under the `[📌  INSERT-LICENSE-TYPE]` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 👏 Acknowledgments

> - [📌  List any resources, contributors, inspiration, etc.]

---
