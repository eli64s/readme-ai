
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
MLOps-Basics
</h1>
<h3 align="center">📍 MLOps-Basics: Automating Machine Learning for Maximum Efficiency!</h3>
<h3 align="center">🚀 Developed with the software and tools below.</h3>
<p align="center">

<img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="yml" />
<img src="https://img.shields.io/badge/scikitlearn-F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="torchmetrics" />
<img src="https://img.shields.io/badge/Jupyter-F37626.svg?style=for-the-badge&logo=Jupyter&logoColor=white" alt="python" />

<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=for-the-badge&logo=FastAPI&logoColor=white" alt="pack" />
<img src="https://img.shields.io/badge/DVC-13ADC7.svg?style=for-the-badge&logo=DVC&logoColor=white" alt="pytorch-lightning" />
<img src="https://img.shields.io/badge/JPEG-8A8A8A.svg?style=for-the-badge&logo=JPEG&logoColor=white" alt="txt" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white" alt="md" />
</p>

</div>

---
## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍Overview](#-introdcution)
- [🔮 Features](#-features)
- [⚙️ Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🏎💨 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [🪪 License](#-license)
- [📫 Contact](#-contact)
- [🙏 Acknowledgments](#-acknowledgments)

---

## 📍Overview

MLOps-Basics is a GitHub project that enables developers to quickly and easily incorporate MLOps best practices into their project flow. It provides tools and tutorials to help developers build and maintain ML applications, like automated

## 🔮 Features

> `[📌  INSERT-PROJECT-FEATURES]`

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## ⚙️ Project Structure

```bash
.
├── LICENSE
├── README.md
├── images
│   ├── basic_flow.png
│   ├── docker_flow.png
│   ├── dvc.png
│   ├── ecr_flow.png
│   ├── hydra.png
│   ├── kibana_flow.png
│   ├── lambda_flow.png
│   ├── onnx.jpeg
│   ├── pl.jpeg
│   ├── summary.png
│   └── wandb.png
├── week_0_project_setup
│   ├── README.md
│   ├── data.py
│   ├── experimental_notebooks
│   │   └── data_exploration.ipynb
│   ├── inference.py
│   ├── model.py
│   ├── requirements.txt
│   └── train.py
├── week_1_wandb_logging
│   ├── README.md
│   ├── data.py
│   ├── experimental_notebooks
│   │   └── data_exploration.ipynb
│   ├── inference.py
│   ├── model.py
│   ├── requirements.txt
│   └── train.py
├── week_2_hydra_config
│   ├── README.md
│   ├── configs
│   │   ├── config.yaml
│   │   ├── model
│   │   │   └── default.yaml
│   │   ├── processing
│   │   │   └── default.yaml
│   │   └── training
│   │       └── default.yaml
│   ├── data.py
│   ├── experimental_notebooks
│   │   └── data_exploration.ipynb
│   ├── inference.py
│   ├── model.py
│   ├── requirements.txt
│   └── train.py
├── week_3_dvc
│   ├── README.md
│   ├── configs
│   │   ├── config.yaml
│   │   ├── model
│   │   │   └── default.yaml
│   │   ├── processing
│   │   │   └── default.yaml
│   │   └── training
│   │       └── default.yaml
│   ├── data.py
│   ├── dvcfiles
│   │   └── trained_model.dvc
│   ├── experimental_notebooks
│   │   └── data_exploration.ipynb
│   ├── inference.py
│   ├── model.py
│   ├── models
│   ├── requirements.txt
│   └── train.py
├── week_4_onnx
│   ├── README.md
│   ├── configs
│   │   ├── config.yaml
│   │   ├── model
│   │   │   └── default.yaml
│   │   ├── processing
│   │   │   └── default.yaml
│   │   └── training
│   │       └── default.yaml
│   ├── convert_model_to_onnx.py
│   ├── data.py
│   ├── dvcfiles
│   │   └── trained_model.dvc
│   ├── experimental_notebooks
│   │   └── data_exploration.ipynb
│   ├── inference.py
│   ├── inference_onnx.py
│   ├── model.py
│   ├── requirements.txt
│   ├── train.py
│   └── utils.py
├── week_5_docker
│   ├── Dockerfile
│   ├── README.md
│   ├── app.py
│   ├── configs
│   │   ├── config.yaml
│   │   ├── model
│   │   │   └── default.yaml
│   │   ├── processing
│   │   │   └── default.yaml
│   │   └── training
│   │       └── default.yaml
│   ├── convert_model_to_onnx.py
│   ├── data.py
│   ├── docker-compose.yml
│   ├── dvcfiles
│   │   └── trained_model.dvc
│   ├── experimental_notebooks
│   │   └── data_exploration.ipynb
│   ├── inference.py
│   ├── inference_onnx.py
│   ├── model.py
│   ├── requirements.txt
│   ├── requirements_inference.txt
│   ├── train.py
│   └── utils.py
├── week_6_github_actions
│   ├── Dockerfile
│   ├── README.md
│   ├── app.py
│   ├── configs
│   │   ├── config.yaml
│   │   ├── model
│   │   │   └── default.yaml
│   │   ├── processing
│   │   │   └── default.yaml
│   │   └── training
│   │       └── default.yaml
│   ├── convert_model_to_onnx.py
│   ├── data.py
│   ├── docker-compose.yml
│   ├── dvcfiles
│   │   └── trained_model.dvc
│   ├── experimental_notebooks
│   │   └── data_exploration.ipynb
│   ├── inference.py
│   ├── inference_onnx.py
│   ├── model.py
│   ├── parse_json.py
│   ├── requirements.txt
│   ├── requirements_inference.txt
│   ├── train.py
│   └── utils.py
├── week_7_ecr
│   ├── Dockerfile
│   ├── README.md
│   ├── app.py
│   ├── configs
│   │   ├── config.yaml
│   │   ├── model
│   │   │   └── default.yaml
│   │   ├── processing
│   │   │   └── default.yaml
│   │   └── training
│   │       └── default.yaml
│   ├── convert_model_to_onnx.py
│   ├── data.py
│   ├── docker-compose.yml
│   ├── dvcfiles
│   │   └── trained_model.dvc
│   ├── experimental_notebooks
│   │   └── data_exploration.ipynb
│   ├── inference.py
│   ├── inference_onnx.py
│   ├── model.py
│   ├── parse_json.py
│   ├── requirements.txt
│   ├── requirements_inference.txt
│   ├── train.py
│   └── utils.py
├── week_8_serverless
│   ├── Dockerfile
│   ├── README.md
│   ├── app.py
│   ├── configs
│   │   ├── config.yaml
│   │   ├── model
│   │   │   └── default.yaml
│   │   ├── processing
│   │   │   └── default.yaml
│   │   └── training
│   │       └── default.yaml
│   ├── convert_model_to_onnx.py
│   ├── data.py
│   ├── docker-compose.yml
│   ├── dvcfiles
│   │   └── trained_model.dvc
│   ├── experimental_notebooks
│   │   └── data_exploration.ipynb
│   ├── inference.py
│   ├── inference_onnx.py
│   ├── lambda_handler.py
│   ├── model.py
│   ├── parse_json.py
│   ├── requirements.txt
│   ├── requirements_inference.txt
│   ├── train.py
│   └── utils.py
└── week_9_monitoring
    ├── Dockerfile
    ├── README.md
    ├── app.py
    ├── configs
    │   ├── config.yaml
    │   ├── model
    │   │   └── default.yaml
    │   ├── processing
    │   │   └── default.yaml
    │   └── training
    │       └── default.yaml
    ├── convert_model_to_onnx.py
    ├── data.py
    ├── docker-compose.yml
    ├── dvcfiles
    │   └── trained_model.dvc
    ├── experimental_notebooks
    │   └── data_exploration.ipynb
    ├── inference.py
    ├── inference_onnx.py
    ├── lambda_handler.py
    ├── model.py
    ├── parse_json.py
    ├── requirements.txt
    ├── requirements_inference.txt
    ├── train.py
    └── utils.py

62 directories, 166 files
```
---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 💻 Modules
<details closed><summary>.dvc</summary>

| File   | Summary                                                                                                                                             | Module      |
|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------|:------------|
| config | This code sets up two remote repositories, "storage" and "model-store", with URLs pointing to a Google Drive and an Amazon S3 bucket, respectively. | .dvc/config |

</details>

<details closed><summary>Dvcfiles</summary>

| File              | Summary                                                                                                                                                                                                     | Module                                           |
|:------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------|
| trained_model.dvc | This code is a summary of a file located in the ". ./models" directory. The file is named "best-checkpoint. ckpt" and has a size of 17567709 bytes.                                                         | week_4_onnx/dvcfiles/trained_model.dvc           |
| trained_model.dvc | This code is a summary of a model file located in the ". ./models" directory. The model file is named "model. onnx" and has an MD5 hash of "02f3b0034769ba45d758ad1bb9de33a3" and a size of 17562590 bytes. | week_9_monitoring/dvcfiles/trained_model.dvc     |
| trained_model.dvc | This code is a summary of a model file located in the ". ./models" directory. The model file is named "model. onnx" and has an MD5 hash of "02f3b0034769ba45d758ad1bb9de33a3" and a size of 17562590 bytes. | week_8_serverless/dvcfiles/trained_model.dvc     |
| trained_model.dvc | This code is a summary of a file located in the ". ./models" directory. The file is named "best-checkpoint. ckpt" and has a size of 17567709 bytes.                                                         | week_5_docker/dvcfiles/trained_model.dvc         |
| trained_model.dvc | This code is a summary of a file located in the ". ./models" directory. The file is named "best-checkpoint. ckpt" and has a size of 17567709 bytes.                                                         | week_3_dvc/dvcfiles/trained_model.dvc            |
| trained_model.dvc | This code is a summary of a model file located in the ". ./models" directory. The model file is named "model. onnx" and has an MD5 hash of "02f3b0034769ba45d758ad1bb9de33a3" and a size of 17562590 bytes. | week_7_ecr/dvcfiles/trained_model.dvc            |
| trained_model.dvc | This code is a summary of a model file located in the ". ./models" directory. The model file is named "model. onnx" and has an MD5 hash of "d82b8390fa2f09b121de4abfa094a7a9" and a size of 17562590 bytes. | week_6_github_actions/dvcfiles/trained_model.dvc |

</details>

<details closed><summary>Images</summary>

| File      | Summary                                                                                                           | Module           |
|:----------|:------------------------------------------------------------------------------------------------------------------|:-----------------|
| pl.jpeg   | This code is an error message indicating that a file could not be decoded because it is not a text or UTF-8 file. | images/pl.jpeg   |
| onnx.jpeg | This code is an error message indicating that a file could not be decoded because it is not a text or UTF-8 file. | images/onnx.jpeg |

</details>

<details closed><summary>Top Level</summary>

| File       | Summary                                                                                                                                                                 | Module     |
|:-----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------|
| .dvcignore | This code allows users to add patterns of files that should be ignored by DVC, which can improve performance. For more information, please refer to the DVC user guide. | .dvcignore |

</details>

<details closed><summary>Week_1_wandb_logging</summary>

| File         | Summary                                                                                                                                                                                                 | Module                            |
|:-------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------|
| model.py     | This code is a ColaModel class that uses PyTorch Lightning to create a model for sequence classification using the Google BERT model.                                                                   | week_1_wandb_logging/model.py     |
| train.py     | This code is a main function for training a ColaModel using PyTorch Lightning. It imports torch, wandb, pandas, pytorch_lightning, and two custom modules (DataModule and ColaModel).                   | week_1_wandb_logging/train.py     |
| inference.py | This code creates a ColaPredictor class which can be used to predict whether a sentence is acceptable or unacceptable. It uses a ColaModel and DataModule to tokenize the sentence and generate logits. | week_1_wandb_logging/inference.py |

</details>

<details closed><summary>Week_2_hydra_config</summary>

| File         | Summary                                                                                                                                                                                                 | Module                           |
|:-------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------|
| model.py     | This code is a ColaModel class that uses the PyTorch Lightning framework to train a BERT model for sequence classification.                                                                             | week_2_hydra_config/model.py     |
| train.py     | This code is a training script for a sentiment analysis model using PyTorch Lightning, Hydra, Wandb, and other libraries.                                                                               | week_2_hydra_config/train.py     |
| inference.py | This code creates a ColaPredictor class which can be used to predict whether a sentence is acceptable or unacceptable. It uses a ColaModel and DataModule to tokenize the sentence and generate logits. | week_2_hydra_config/inference.py |

</details>

<details closed><summary>Week_3_dvc</summary>

| File         | Summary                                                                                                                                                                                                 | Module                  |
|:-------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------|
| model.py     | This code is a ColaModel class that uses the PyTorch Lightning framework to create a model for sequence classification using the Transformers library.                                                  | week_3_dvc/model.py     |
| train.py     | This code is a training script for a sentiment analysis model using PyTorch Lightning, Hydra, Wandb, and other libraries.                                                                               | week_3_dvc/train.py     |
| inference.py | This code creates a ColaPredictor class which can be used to predict whether a sentence is acceptable or unacceptable. It uses a ColaModel and DataModule to tokenize the sentence and generate logits. | week_3_dvc/inference.py |

</details>

<details closed><summary>Week_4_onnx</summary>

| File                     | Summary                                                                                                                                                                                                                                                             | Module                               |
|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------|
| inference_onnx.py        | This code is a class for a ColaONNXPredictor which uses an ONNX model to predict the acceptability of a sentence. It uses the DataModule to tokenize the data and the scipy. special library to calculate the softmax scores.                                       | week_4_onnx/inference_onnx.py        |
| model.py                 | This code is a ColaModel class that uses the PyTorch Lightning library to create a model for sequence classification using the Transformers library.                                                                                                                | week_4_onnx/model.py                 |
| train.py                 | This code is a training script for a sentiment analysis model using PyTorch Lightning, Hydra, Wandb, and other libraries.                                                                                                                                           | week_4_onnx/train.py                 |
| inference.py             | This code creates a ColaPredictor class which uses a ColaModel to predict the acceptability of a given sentence. It uses a DataModule to tokenize the data, a Softmax to calculate the scores, and a timing decorator to measure the time taken for the prediction. | week_4_onnx/inference.py             |
| convert_model_to_onnx.py | This code uses the libraries torch, hydra, and omegaconf to convert a pre-trained ColaModel from a checkpoint into an ONNX format model.                                                                                                                            | week_4_onnx/convert_model_to_onnx.py |

</details>

<details closed><summary>Week_5_docker</summary>

| File                     | Summary                                                                                                                                                                                                                                                             | Module                                 |
|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------|
| inference_onnx.py        | This code is a class for a ColaONNXPredictor which uses an ONNX model to predict the acceptability of a sentence. It takes in a sentence, tokenizes it, and runs it through the ONNX model to get a score for each label.                                           | week_5_docker/inference_onnx.py        |
| model.py                 | This code is a ColaModel class that uses the PyTorch Lightning library to create a model for sequence classification using the Transformers library.                                                                                                                | week_5_docker/model.py                 |
| train.py                 | This code is a training script for a sentiment analysis model using PyTorch Lightning, Hydra, Wandb, and other libraries.                                                                                                                                           | week_5_docker/train.py                 |
| app.py                   | This code creates a FastAPI application that uses an ONNX model to make predictions. The application has two endpoints, one for the home page and one for making predictions.                                                                                       | week_5_docker/app.py                   |
| inference.py             | This code creates a ColaPredictor class which uses a ColaModel to predict the acceptability of a given sentence. It uses a DataModule to tokenize the data, a Softmax to calculate the scores, and a timing decorator to measure the time taken for the prediction. | week_5_docker/inference.py             |
| convert_model_to_onnx.py | This code uses the libraries torch, hydra, and omegaconf to convert a pre-trained ColaModel from a checkpoint into an ONNX format model.                                                                                                                            | week_5_docker/convert_model_to_onnx.py |

</details>

<details closed><summary>Week_6_github_actions</summary>

| File                     | Summary                                                                                                                                                                                                                                                             | Module                                         |
|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------|
| inference_onnx.py        | This code is a class for a ColaONNXPredictor which uses an ONNX model to predict the acceptability of a sentence. It takes in a sentence, tokenizes it, and runs it through the ONNX model to get a score for each label.                                           | week_6_github_actions/inference_onnx.py        |
| model.py                 | This code is a ColaModel class that uses the PyTorch Lightning library to create a model for sequence classification using the Transformers library.                                                                                                                | week_6_github_actions/model.py                 |
| train.py                 | This code is a training script for a sentiment analysis model using PyTorch Lightning, Hydra, Wandb, and other libraries.                                                                                                                                           | week_6_github_actions/train.py                 |
| app.py                   | This code creates a FastAPI application that uses an ONNX model to make predictions. The application has two endpoints, one for the home page and one for making predictions.                                                                                       | week_6_github_actions/app.py                   |
| inference.py             | This code creates a ColaPredictor class which uses a ColaModel to predict the acceptability of a given sentence. It uses a DataModule to tokenize the data, a Softmax to calculate the scores, and a timing decorator to measure the time taken for the prediction. | week_6_github_actions/inference.py             |
| convert_model_to_onnx.py | This code imports the necessary libraries and packages, loads a pre-trained model from a checkpoint, prepares and sets up the data, and then converts the model into ONNX format and saves it to a specified location.                                              | week_6_github_actions/convert_model_to_onnx.py |
| parse_json.py            | This code reads a file called 'creds. txt', evaluates the data, and then writes it to a file called 'test. json' using the json library.                                                                                                                            | week_6_github_actions/parse_json.py            |

</details>

<details closed><summary>Week_7_ecr</summary>

| File                     | Summary                                                                                                                                                                                                                                                             | Module                              |
|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------|
| inference_onnx.py        | This code is a class for a ColaONNXPredictor which uses an ONNX model to predict the acceptability of a sentence. It takes in a sentence, tokenizes it, and runs it through the ONNX model to get a score for each label.                                           | week_7_ecr/inference_onnx.py        |
| model.py                 | This code is a ColaModel class that uses the PyTorch Lightning framework to create a model for sequence classification using the Transformers library.                                                                                                              | week_7_ecr/model.py                 |
| train.py                 | This code is a training script for a sentiment analysis model using PyTorch Lightning, Hydra, Wandb, and other libraries.                                                                                                                                           | week_7_ecr/train.py                 |
| app.py                   | This code creates a FastAPI application that uses an ONNX model to make predictions. The application has two endpoints, one for the home page and one for making predictions.                                                                                       | week_7_ecr/app.py                   |
| inference.py             | This code creates a ColaPredictor class which uses a ColaModel to predict the acceptability of a given sentence. It uses a DataModule to tokenize the data, a Softmax to calculate the scores, and a timing decorator to measure the time taken for the prediction. | week_7_ecr/inference.py             |
| convert_model_to_onnx.py | This code uses the libraries torch, hydra, and omegaconf to convert a pre-trained ColaModel from a checkpoint into an ONNX format model.                                                                                                                            | week_7_ecr/convert_model_to_onnx.py |
| parse_json.py            | This code reads a file called 'creds. txt', evaluates the data, and then writes it to a file called 'test. json' in JSON format.                                                                                                                                    | week_7_ecr/parse_json.py            |

</details>

<details closed><summary>Week_8_serverless</summary>

| File                     | Summary                                                                                                                                                                                                                                                             | Module                                     |
|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------|
| inference_onnx.py        | This code is a class for a ColaONNXPredictor which uses an ONNX model to predict the acceptability of a sentence. It takes in a sentence, tokenizes it, and runs it through the ONNX model to get a score for each label.                                           | week_8_serverless/inference_onnx.py        |
| lambda_handler.py        | This code is a Lambda wrapper for a ColaONNXPredictor model, which is used to predict the linguistic acceptability of a given sentence.                                                                                                                             | week_8_serverless/lambda_handler.py        |
| model.py                 | This code is a ColaModel class that uses the PyTorch Lightning library to create a model for sequence classification using the Transformers library.                                                                                                                | week_8_serverless/model.py                 |
| train.py                 | This code is a training script for a sentiment analysis model using PyTorch Lightning, Hydra, Wandb, and other libraries.                                                                                                                                           | week_8_serverless/train.py                 |
| app.py                   | This code creates a FastAPI application that uses an ONNX model to make predictions. The application has two endpoints, one for the home page and one for making predictions.                                                                                       | week_8_serverless/app.py                   |
| inference.py             | This code creates a ColaPredictor class which uses a ColaModel to predict the acceptability of a given sentence. It uses a DataModule to tokenize the data, a Softmax to calculate the scores, and a timing decorator to measure the time taken for the prediction. | week_8_serverless/inference.py             |
| convert_model_to_onnx.py | This code uses the libraries torch, hydra, and omegaconf to convert a pre-trained ColaModel from a checkpoint into an ONNX format model.                                                                                                                            | week_8_serverless/convert_model_to_onnx.py |
| parse_json.py            | This code reads a file called 'creds. txt', evaluates the data, and then writes it to a file called 'test. json' using the json library.                                                                                                                            | week_8_serverless/parse_json.py            |

</details>

<details closed><summary>Week_9_monitoring</summary>

| File                     | Summary                                                                                                                                                                                                                                                             | Module                                     |
|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------|
| inference_onnx.py        | This code is a class for a ColaONNXPredictor which uses an ONNX model to predict the acceptability of a sentence. It uses the DataModule to tokenize the data, and the scipy. special softmax function to calculate the scores.                                     | week_9_monitoring/inference_onnx.py        |
| lambda_handler.py        | This code is a Lambda wrapper for a ColaONNXPredictor model. It takes in a sentence as input and returns a prediction of its linguistic acceptability.                                                                                                              | week_9_monitoring/lambda_handler.py        |
| model.py                 | This code is a ColaModel class that uses the PyTorch Lightning library to create a model for sequence classification using the Transformers library.                                                                                                                | week_9_monitoring/model.py                 |
| train.py                 | This code is a training script for a sentiment analysis model using PyTorch Lightning, Hydra, Wandb, and other libraries.                                                                                                                                           | week_9_monitoring/train.py                 |
| app.py                   | This code creates a FastAPI application that uses an ONNX model to make predictions. The application has two endpoints, one for the home page and one for making predictions.                                                                                       | week_9_monitoring/app.py                   |
| inference.py             | This code creates a ColaPredictor class which uses a ColaModel to predict the acceptability of a given sentence. It uses a DataModule to tokenize the data, a Softmax to calculate the scores, and a timing decorator to measure the time taken for the prediction. | week_9_monitoring/inference.py             |
| convert_model_to_onnx.py | This code uses the libraries torch, hydra, and omegaconf to convert a pre-trained ColaModel from a checkpoint into an ONNX format model.                                                                                                                            | week_9_monitoring/convert_model_to_onnx.py |
| parse_json.py            | This code reads a file called 'creds. txt', evaluates the data, and then writes it to a file called 'test. json' using the json library.                                                                                                                            | week_9_monitoring/parse_json.py            |

</details>
<hr />

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> `[📌  INSERT-PROJECT-PREREQUISITES]`

### 💻 Installation

1. Clone the MLOps-Basics repository:
```sh
git clone https://github.com/graviraja/MLOps-Basics
```

2. Change to the project directory:
```sh
cd MLOps-Basics
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

### 🤖 Using MLOps-Basics

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
