
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
energy-forecasting
</h1>
<h3>◦ Power up your predictions with energy-forecasting.</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

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

| File       | Summary                                                                                                                                                                                                                                                                                                                                                                                                | Module             |
|:-----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
| Dockerfile | The code snippet contains a Dockerfile for configuring the Apache Airflow image version 2.5.2. It installs Python dependencies required to process the wheels from a private PyPI server, including python3.9-distutils, python3.9-dev, and build-essential packages. The Dockerfile sets the user to root during installation and reverts back to the current user using the "CURRENT_USER" argument. | airflow/Dockerfile |

</details>

<details closed><summary>Api</summary>

| File           | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Module                     |
|:---------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------|
| config.py      | The code snippet defines an enum class for log levels and a settings class for the application with default values that can be overridden by environment variables. The settings are loaded using the lru_cache function, which caches the result for faster subsequent access. The pydantic library is used for type validation of the settings.                                                                                                                                                 | app-api/api/config.py      |
| application.py | This code creates and configures a FastAPI app with CORS middleware, API router, and settings for documentation and API versioning. It allows for all origins to be accepted for demo purposes, and returns the FastAPI app.                                                                                                                                                                                                                                                                      | app-api/api/application.py |
| __main__.py    | This code snippet defines a main function that runs a web application using the Uvicorn server. The function uses settings from the config file to specify the number of workers, host, port, reload, log level, and factory for the application. If the script is executed directly, the main function is called.                                                                                                                                                                                | app-api/api/__main__.py    |
| views.py       | This code snippet is an API for retrieving data about energy consumption predictions for specific areas and consumer types. It uses GCSFileSystem to download data from Google Cloud Storage, then uses Pandas to query and manipulate the data. Endpoints include health check, retrieving unique values for areas and consumer types, and retrieving predictions and monitoring metrics for specific area and consumer type combinations. Responses are formatted according to defined schemas. | app-api/api/views.py       |

</details>

<details closed><summary>App-api</summary>

| File         | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Module               |
|:-------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------|
| Dockerfile   | The provided code snippet builds a Docker image for a Python application using Poetry as a package manager. It first updates and upgrades the system, then installs Poetry and configures it to not create a virtual environment. The Docker image is then built by copying the pyproject.toml and poetry.lock files to the working directory, installing the dependencies with Poetry, and adding the remaining application files. Finally, the run.sh script is given executable permission and set as the entry point for the container. | app-api/Dockerfile   |
| run.sh       | The code snippet executes the "api" module using the Python interpreter located in "/usr/local/bin/python". This is a common way to run a Python program from the command line by using the "-m" switch followed by the module name.                                                                                                                                                                                                                                                                                                        | app-api/run.sh       |
| .env.default | The provided code snippet sets three variables for a Google Cloud Platform project, bucket and service account JSON path. These variables are likely used for reading hourly batch predictions related to energy consumption from a GCP bucket.                                                                                                                                                                                                                                                                                             | app-api/.env.default |

</details>

<details closed><summary>App-frontend</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                                                                                          | Module                  |
|:-----------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------|
| Dockerfile | This code snippet sets up a Docker container for a Python app built using Streamlit and Poetry. It installs necessary dependencies, copies the app files into the container, and sets up a command to run the app with a specified server port. The containerization process is optimized by first copying and installing requirements before copying the rest of the app files. | app-frontend/Dockerfile |

</details>

<details closed><summary>App-monitoring</summary>

| File       | Summary                                                                                                                                                                                                                                                                                        | Module                    |
|:-----------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------|
| Dockerfile | This code sets up a Docker image with a Python 3.9.8 environment, installs and configures Poetry to manage dependencies, copies the project files and installs them, and then specifies a command to execute when the container runs (in this case, starting a Streamlit server on port 8502). | app-monitoring/Dockerfile |

</details>

<details closed><summary>Batch-prediction-pipeline</summary>

| File         | Summary                                                                                                                                                                                                                                                                                                                                                                    | Module                                 |
|:-------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------|
| .env.default | The code snippet defines several API keys and paths for connecting to different services and storing data related to the "energy_consumption" project. These services include feature store, WANDB (a platform for machine learning development), and Google Cloud Storage for hosting batch predictions. A service account JSON path is also provided for authentication. | batch-prediction-pipeline/.env.default |

</details>

<details closed><summary>Batch_prediction_pipeline</summary>

| File          | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Module                                                            |
|:--------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------|
| monitoring.py | The code snippet defines a function called `compute` that loads old predictions and latest data from a feature store, computes mean absolute percentage error (MAPE) metrics on data points that have ground truth, and saves the metrics to a blob in a storage bucket. The function takes an optional argument for the version of the feature view to load data from the feature store. The code uses various utility functions defined in other modules. The `if __name__ == "__main__":` block at the end of the code calls the `compute` function when the script is run directly. | batch-prediction-pipeline/batch_prediction_pipeline/monitoring.py |
| batch.py      | The provided code snippet contains a Python script that performs batch predictions for energy consumption using machine learning models.                                                                                                                                                                                                                                                                                                                                                                                                                                                | batch-prediction-pipeline/batch_prediction_pipeline/batch.py      |
|               | The script loads data from a feature store, loads a model from a model registry, makes predictions on the loaded data, and saves the predictions to a specified location (Google Cloud Storage bucket).                                                                                                                                                                                                                                                                                                                                                                                 |                                                                   |
|               | It also includes functions for loading and forecasting with the model, as well as for saving the predictions to a bucket for monitoring.                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                   |
| utils.py      | This code snippet contains various functions for loading and saving data, connecting to a Google Cloud Storage bucket, and reading and writing data to and from the bucket using Pandas dataframes in the parquet format. It also includes a logger template and a model loading function. Overall, this code is useful for implementing a batch prediction pipeline.                                                                                                                                                                                                                   | batch-prediction-pipeline/batch_prediction_pipeline/utils.py      |
| settings.py   | The provided code snippet contains functions to load environment variables from.env files and to get the root directory of a project. The ML_PIPELINE_ROOT_DIR directory is set as the root directory, and the settings are loaded and saved to the OUTPUT_DIR directory relative to the root directory. The warnings module is also used to ignore future warnings from the sktime library.                                                                                                                                                                                            | batch-prediction-pipeline/batch_prediction_pipeline/settings.py   |
| data.py       | This code defines a function that loads data from a feature store for a given time range, identified by a feature view version. It uses the Hopsworks feature store library to retrieve the data and Pandas to manipulate it according to the required format of the target variable, which is a time series to be forecasted. It then returns the exogenous variables and the time series in a tuple.                                                                                                                                                                                  | batch-prediction-pipeline/batch_prediction_pipeline/data.py       |

</details>

<details closed><summary>Configs</summary>

| File          | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Module                                                    |
|:--------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------|
| gridsearch.py | The code snippet provides a set of configuration parameters for grid search optimization of machine learning models in a production environment. The configurations include the method of search, metric for evaluation, and a range of parameter values for various model components such as the estimator, daily seasonality, and window summarizer. The configurations provide flexibility in the optimization process to minimize the validation MAPE metric. | training-pipeline/training_pipeline/configs/gridsearch.py |

</details>

<details closed><summary>Dags</summary>

| File               | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Module                          |
|:-------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------|
| ml_pipeline_dag.py | This code snippet defines an Airflow DAG named "ml_pipeline" that orchestrates the end-to-end process of building and deploying a machine learning pipeline. The DAG comprises several tasks that execute feature engineering, model training, batch prediction, and monitoring. The pipeline takes in several parameters, including export_end_reference_datetime, days_delay, days_export, url, and feature_group_version, and depends on external libraries such as feature_pipeline, training_pipeline, and batch_prediction_pipeline. | airflow/dags/ml_pipeline_dag.py |
| .env.default       | The code snippet defines several variables for API keys, entity, project, bucket name, and service account JSON path. These variables are likely being used in an Airflow DAG to access and process data related to energy consumption in a cloud environment.                                                                                                                                                                                                                                                                             | airflow/dags/.env.default       |

</details>

<details closed><summary>Deploy</summary>

| File           | Summary                                                                                                                                                                                                                                                                                                                  | Module                |
|:---------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
| ml-pipeline.sh | This code snippet builds and publishes three packages (feature-pipeline, training-pipeline, and batch-prediction-pipeline) so that they can be run from the command line interface (CLI). The packages are executed in their respective directories, and the repository my-pypi must be defined in the poetry.toml file. | deploy/ml-pipeline.sh |

</details>

<details closed><summary>Etl</summary>

| File          | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Module                                              |
|:--------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------|
| load.py       | The provided code defines a function to save a Pandas DataFrame to a feature store in Hopsworks after performing validation using an expectation suite. The function creates a Feature Group in the feature store, uploads the data to it, and adds feature descriptions. It also updates statistics and returns the Feature Group.                                                                                                                                                                                            | feature-pipeline/feature_pipeline/etl/load.py       |
| extract.py    | The code snippet provides a function that extracts energy consumption data from a Denmark API. The function takes parameters for the desired time window and API URL, and returns a tuple containing the data in a Pandas DataFrame and metadata in a dictionary. The function also logs information about the API request and handles potential errors in parsing the API response.                                                                                                                                           | feature-pipeline/feature_pipeline/etl/extract.py    |
| cleaning.py   | The provided code snippet contains three functions that process a pandas DataFrame. The first function renames specific columns, the second function casts columns to the correct data type, and the third function encodes the area column to integers using a predefined mapping. The functions are designed to be used together in a data preprocessing pipeline.                                                                                                                                                           | feature-pipeline/feature_pipeline/etl/cleaning.py   |
| validation.py | This code builds an expectation suite for validating energy consumption data. It defines expectations for column names and types, as well as for specific ranges of values in the datetime_utc and energy_consumption columns. It also enforces that there are no null values in the datetime_utc and energy_consumption columns and that the values in the area and consumer_type columns are within predefined sets. The expectation suite is returned as an instance of the ExpectationSuite class from Great Expectations. | feature-pipeline/feature_pipeline/etl/validation.py |

</details>

<details closed><summary>Feature-pipeline</summary>

| File         | Summary                                                                                                                                                                                                                                                                                                                                                                                            | Module                        |
|:-------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------|
| .env.default | This code snippet initializes various API and storage keys and paths for a project related to energy consumption. These keys and paths include the Feature Store API key, W&B API key, Google Cloud project name, bucket name, and service account credentials in JSON format. These values are required to connect to and interact with various APIs and storage services throughout the project. | feature-pipeline/.env.default |

</details>

<details closed><summary>Feature_pipeline</summary>

| File                   | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Module                                                   |
|:-----------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------|
| clean_feature_store.py | This code snippet defines a function called "clean" that is used to clean all the data from a feature store in a Hopsworks project. The function uses the Hopsworks Python SDK to log in to the project and delete feature views, training datasets, and feature groups. The code snippet also uses the Python library "fire" to enable the function to be called from the command line.                                                                                    | feature-pipeline/feature_pipeline/clean_feature_store.py |
| utils.py               | The provided code snippet contains three functions: get_logger, save_json, and load_json.                                                                                                                                                                                                                                                                                                                                                                                   | feature-pipeline/feature_pipeline/utils.py               |
|                        | get_logger creates a logger object for logging information.                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                          |
|                        | save_json saves a given dictionary as a JSON file in a specified directory.                                                                                                                                                                                                                                                                                                                                                                                                 |                                                          |
|                        | load_json loads a JSON file from a specified directory and returns its contents as a dictionary. The directory can be specified using the settings.OUTPUT_DIR variable.                                                                                                                                                                                                                                                                                                     |                                                          |
| pipeline.py            | This Python code extracts data from an API and transforms it using a set of cleaning functions. It then builds a validation expectation suite and validates the data before loading it into a feature store. The metadata of the pipeline is saved in a JSON file and a logger is used to track progress. This code can be run from the command line using the Fire library.                                                                                                | feature-pipeline/feature_pipeline/pipeline.py            |
| feature_view.py        | The code creates a new feature view version and training dataset based on a given feature group version and start/end datetimes using Hopsworks Feature Store (HSFS). It first logs in to HSFS and deletes any old feature views, then creates a new feature view and training dataset based on the given parameters. Finally, it saves metadata about the feature view and training dataset versions. The script can be run from the command line with optional arguments. | feature-pipeline/feature_pipeline/feature_view.py        |
| settings.py            | The code snippet loads environment variables from.env.default and.env files and returns them as a dictionary. It also gets the root directory of the project using the "ML_PIPELINE_ROOT_DIR" environment variable, and creates an output directory within that. The "SETTINGS" variable is assigned the dictionary of environment variables.                                                                                                                               | feature-pipeline/feature_pipeline/settings.py            |

</details>

<details closed><summary>Frontend</summary>

| File          | Summary                                                                                                                                                                                                                                                                                                                                                                                | Module                              |
|:--------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------|
| settings.py   | This code imports the URL class from the yarl library and creates a constant variable called TITLE which stores a string value. It also creates a constant variable called API_URL which stores a URL object with a specific address. These constants can be used in other parts of the code.                                                                                          | app-frontend/frontend/settings.py   |
| components.py | This code snippet retrieves energy consumption predictions from an API endpoint and builds a plot using Plotly. If the API response is invalid, empty dataframes are built, and the title of the plot indicates that no data is available. The build_dataframe function is used to create dataframes for plotting.                                                                     | app-frontend/frontend/components.py |
| main.py       | The provided code utilizes the requests and streamlit libraries to create an interactive web interface for users to select an area and consumer type for Danish energy data. The data is retrieved through an API and plotted using Plotly. The interface also includes dropdown menus for area and consumer type selection, with helpful explanatory text provided to guide the user. | app-frontend/frontend/main.py       |

</details>

<details closed><summary>Monitoring</summary>

| File          | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                              | Module                                  |
|:--------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------|
| settings.py   | The code snippet imports the URL module from the yarl package, sets a constant TITLE variable to a string, and creates an API URL object pointing to a specific endpoint. The endpoint is for monitoring energy consumption data and hosted at the IP address 172.17.0.1 on port 8001.                                                                                                                                                               | app-monitoring/monitoring/settings.py   |
| components.py | This code snippet imports necessary libraries and functions to build plotly graphs for monitoring energy consumption data and metrics from an API. It includes functions to retrieve data from the API, build dataframes in the proper format, and plot the data in a visually appealing graph using plotly. The plots show the observations and predictions of energy consumption and the Mean Absolute Percentage Error (MAPE) of the predictions. | app-monitoring/monitoring/components.py |
| main.py       | The provided code snippet retrieves data from an API and displays plots using the Streamlit library. It allows the user to select an area and a consumer type, and then plots the corresponding data using the selected inputs. The code also provides information about the selected options and includes a divider for visual separation.                                                                                                          | app-monitoring/monitoring/main.py       |

</details>

<details closed><summary>Root</summary>

| File         | Summary                                                                                                                                                                                                                                                                                                                                                                                                                      | Module       |
|:-------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------|
| .env.default | The provided code snippet defines several variables required for different APIs and services. It includes the feature store API key, the Wandb API key, and the Wandb entity and project names. Additionally, it specifies the Google Cloud project name, bucket name, and service account JSON path. These variables are likely used throughout the codebase for various integrations and interactions with these services. | .env.default |

</details>

<details closed><summary>Schemas</summary>

| File                    | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Module                                      |
|:------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------|
| predictions.py          | The code snippet defines three Pydantic BaseModel classes that encapsulate data related to energy consumption prediction and monitoring metrics. The PredictionResults class contains lists of predicted and actual energy consumption values and their corresponding datetimes. The MonitoringMetrics class contains a list of datetimes and the mean absolute percentage error (MAPE) values. The MonitoringValues class contains lists of energy consumption values and their corresponding datetimes for both actual and predicted values. | app-api/api/schemas/predictions.py          |
| health.py               | The code defines a Pydantic model called "Health" that has two attributes: "name" and "api_version". This allows for easy and efficient validation and serialization of data in Python.                                                                                                                                                                                                                                                                                                                                                        | app-api/api/schemas/health.py               |
| area_values.py          | The provided code defines a Pydantic BaseModel class called UniqueArea, which has one attribute called values that is a list of integers. This class can be used to represent a unique area in an application. The typing module is used to provide type hints for the Any and List data types.                                                                                                                                                                                                                                                | app-api/api/schemas/area_values.py          |
| consumer_type_values.py | The provided code defines a Pydantic BaseModel called UniqueConsumerType that includes a field called "values" that is a list of integers. This model can be used to validate and serialize/deserialize data that includes this field. The typing module is imported to provide type hinting functionality.                                                                                                                                                                                                                                    | app-api/api/schemas/consumer_type_values.py |

</details>

<details closed><summary>Training-pipeline</summary>

| File         | Summary                                                                                                                                                                                                                                                                                      | Module                         |
|:-------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------|
| .env.default | The code snippet contains variables that store API keys for Feature Store and Weights and Biases, as well as information about the project and entity being used. It also includes variables for Google Cloud Project, bucket name, and service account JSON path for accessing credentials. | training-pipeline/.env.default |

</details>

<details closed><summary>Training_pipeline</summary>

| File                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Module                                                       |
|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------|
| best_config.py           | The code provides a function called "upload" that uploads the best configuration from a given sweep to the "best_experiment" wandb Artifact. It first loads the last sweep ID from the cached metadata file, then searches for the best run from the given sweep using the WandB API and logs the best config and validation results to an output file and an artifact respectively using WandB.                                                                                                                                | training-pipeline/training_pipeline/best_config.py           |
| models.py                | The code provides functions to build Sktime forecasting models for time series data. The `build_model` function builds a LightGBM regression model and utilizes Sktime's window summarizer transformer for feature engineering. The `build_baseline_model` function builds a simple baseline model that predicts the last value of the time series based on a seasonal periodicity.                                                                                                                                             | training-pipeline/training_pipeline/models.py                |
| transformers.py          | The code provides a transformer to extract the area and consumer type from the index of the input data. It includes functionality to transform and inverse transform the data, handle missing data, and returns output with the same time index as the input. The code also includes tags indicating the transformer's capabilities.                                                                                                                                                                                            | training-pipeline/training_pipeline/transformers.py          |
| utils.py                 | The provided code snippet contains functions related to saving and loading data (in JSON format, trained model, and parquet file), getting loggers, and interacting with Weights and Biases (W&B) platform (including creating runs/ experiments, checking artifact existence, and getting the latest version of an artifact). The code is designed to be reusable and customizable through input arguments.                                                                                                                    | training-pipeline/training_pipeline/utils.py                 |
| train.py                 | This code snippet contains a function for training and evaluating the best model found in a hyperparameter optimization run, and uploading the artifacts to wandb and hopsworks model registries. The function trains both a baseline model and the best model, and evaluates their performance on a test set. It also saves the best model and attaches it to the feature store. Other functions in the code include training and evaluating a model, rendering time series plots, and computing forecast exogenous variables. | training-pipeline/training_pipeline/train.py                 |
| settings.py              | The provided code snippet loads environment variables from.env.default and.env files, retrieves the root directory of a project, creates a directory for output if it doesn't exist, and loads settings from environment variables. The code also uses the matplotlib library and filters a FutureWarning. The functions and variables in the code are appropriately named and have clear docstrings that explain their functionality.                                                                                          | training-pipeline/training_pipeline/settings.py              |
| hyperparameter_tuning.py | This code implements a hyperparameter optimization search for a forecasting model using the sktime library and W&B sweeps. It loads data from a feature store, runs a cross-validation evaluation of the model, and logs the results to W&B. The code also includes utility functions for rendering the cross-validation scheme and saving metadata.                                                                                                                                                                            | training-pipeline/training_pipeline/hyperparameter_tuning.py |
| data.py                  | The code provides two functions for loading and preparing time series data for forecasting. The `load_dataset_from_feature_store` function loads data from a feature store using Hopsworks, logs metadata to Weights & Biases, and returns train and test splits as Pandas dataframes. The `prepare_data` function structures the data for training, sets the index for sktime, prepares exogenous variables, and splits the data into train and test sets.                                                                     | training-pipeline/training_pipeline/data.py                  |

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
