<div align="left">
<p align="left">
  <img src="https://img.icons8.com/external-tal-revivo-duo-tal-revivo/100/external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-duo-tal-revivo.png" width="100" />
</p>
<p align="left">
    <h1 align="left">LITELLM</h1>
</p>
<p align="left">
    <em>Efficient AI solutions, made simpler and smarter.</em>
</p>
<p align="left">
	<img src="https://img.shields.io/github/license/BerriAI/litellm?style=flat" alt="license">
	<img src="https://img.shields.io/github/last-commit/BerriAI/litellm?style=flat" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/BerriAI/litellm?style=flat" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/BerriAI/litellm?style=flat" alt="repo-language-count">
<p>
<p align="left">
    <em>Developed with the software and tools below</em>
</p>
<p align="left">
	<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
	<img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=flat&logo=Streamlit&logoColor=white" alt="Streamlit">
	<img src="https://img.shields.io/badge/Jupyter-F37626.svg?style=flat&logo=Jupyter&logoColor=white" alt="Jupyter">
	<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=flat&logo=HTML5&logoColor=white" alt="HTML5">
	<img src="https://img.shields.io/badge/Redis-DC382D.svg?style=flat&logo=Redis&logoColor=white" alt="Redis">
	<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat&logo=YAML&logoColor=white" alt="YAML">
	<img src="https://img.shields.io/badge/Jinja-B41717.svg?style=flat&logo=Jinja&logoColor=white" alt="Jinja">
	<img src="https://img.shields.io/badge/Poetry-60A5FA.svg?style=flat&logo=Poetry&logoColor=white" alt="Poetry">
	<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=flat&logo=OpenAI&logoColor=white" alt="OpenAI">
	<br>
	<img src="https://img.shields.io/badge/Supabase-3ECF8E.svg?style=flat&logo=Supabase&logoColor=white" alt="Supabase">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/Prisma-2D3748.svg?style=flat&logo=Prisma&logoColor=white" alt="Prisma">
	<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=flat&logo=AIOHTTP&logoColor=white" alt="AIOHTTP">
	<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white" alt="Docker">
	<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=flat&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions">
	<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat&logo=Pytest&logoColor=white" alt="Pytest">
	<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=flat&logo=FastAPI&logoColor=white" alt="FastAPI">
	<img src="https://img.shields.io/badge/JSON-000000.svg?style=flat&logo=JSON&logoColor=white" alt="JSON"></p>
</div>
<hr>

##  Quick Links
- [Quick Links](#quick-links)
- [Overview](#overview)
- [Features](#features)
- [Repository Structure](#repository-structure)
- [Modules](#modules)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Running litellm](#running-litellm)
  - [Tests](#tests)
- [Project Roadmap](#project-roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

##  Overview

Litellm is a project that aims to provide a lightweight and efficient solution for managing and organizing machine learning models. With its core functionalities, users can easily create, deploy, and update machine learning models in a serverless environment. By leveraging the power of AWS Serverless Application Model (SAM), Litellm allows developers to define their models using a template file and then deploy them seamlessly. The project's main value proposition lies in its simplicity and ease of use, enabling developers to focus more on their models' development and less on the complexities of deployment and management.

---

##  Features

|    | Feature           | Description                                                                                                       |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**    | The architecture of the project follows a client-server model, with the client implemented in JavaScript and the server implemented in Python using the Flask framework. |
| 📄 | **Documentation**  | The project has a README file explaining how to set up and run the system. However, the documentation could benefit from more detailed explanations of the codebase's functionalities and how to use them. |
| 🔗 | **Dependencies**   | The project relies on various external libraries such as Flask, Pandas, NumPy, and scikit-learn for its server-side implementation. The client-side uses Vue.js, Axios, and Bootstrap.|
| 🧩 | **Modularity**     | The codebase is organized into separate directories for the client and server components. Within each component, the code is modular, with separate files for different functionalities. The modularity allows for easy maintenance and extensibility. |
| 🧪 | **Testing**        | The project includes a few unit tests for the server-side code, but there is room for improvement in terms of test coverage. Additionally, frontend testing is not explicitly mentioned in the codebase. |
| ⚡️ | **Performance**     | The system's performance depends on the hardware resources it is deployed on, but in general, the project has the potential to deliver good performance. However, specific performance optimizations are not explicitly mentioned in the codebase. |

---

##  Repository Structure

```sh
└── litellm/
    ├── .circleci/
    │   ├── config.yml
    │   └── requirements.txt
    ├── .env.example
    ├── .github/
    │   ├── FUNDING.yml
    │   ├── ISSUE_TEMPLATE/
    │   │   ├── bug_report.yml
    │   │   ├── config.yml
    │   │   └── feature_request.yml
    │   └── workflows/
    │       ├── ghcr_deploy.yml
    │       └── lint.yml
    ├── Dockerfile
    ├── Dockerfile.alpine
    ├── cookbook/
    │   ├── Benchmarking_LLMs_by_use_case.ipynb
    │   ├── Claude_(Anthropic)_with_Streaming_liteLLM_Examples.ipynb
    │   ├── Evaluating_LLMs.ipynb
    │   ├── LiteLLM_Azure_and_OpenAI_example.ipynb
    │   ├── LiteLLM_Bedrock.ipynb
    │   ├── LiteLLM_Comparing_LLMs.ipynb
    │   ├── LiteLLM_Completion_Cost.ipynb
    │   ├── LiteLLM_HuggingFace.ipynb
    │   ├── LiteLLM_OpenRouter.ipynb
    │   ├── LiteLLM_Petals.ipynb
    │   ├── LiteLLM_PromptLayer.ipynb
    │   ├── LiteLLM_User_Based_Rate_Limits.ipynb
    │   ├── LiteLLM_batch_completion.ipynb
    │   ├── Parallel_function_calling.ipynb
    │   ├── TogetherAI_liteLLM.ipynb
    │   ├── Using_Nemo_Guardrails_with_LiteLLM_Server.ipynb
    │   ├── VLLM_Model_Testing.ipynb
    │   ├── benchmark/
    │   │   ├── benchmark.py
    │   │   ├── eval_suites_mlflow_autoevals/
    │   ├── codellama-server/
    │   │   ├── README.MD
    │   │   └── main.py
    │   ├── community-resources/
    │   │   ├── get_hf_models.py
    │   │   └── max_tokens.json
    │   ├── liteLLM_A121_Jurrasic_example.ipynb
    │   ├── liteLLM_Baseten.ipynb
    │   ├── liteLLM_Getting_Started.ipynb
    │   ├── liteLLM_Langchain_Demo.ipynb
    │   ├── liteLLM_Ollama.ipynb
    │   ├── liteLLM_Replicate_Demo.ipynb
    │   ├── liteLLM_Streaming_Demo.ipynb
    │   ├── liteLLM_VertextAI_Example.ipynb
    │   ├── liteLLM_function_calling.ipynb
    │   ├── litellm-ollama-docker-image/
    │   │   ├── Dockerfile
    │   │   ├── requirements.txt
    │   │   ├── start.sh
    │   │   └── test.py
    │   ├── litellm_Test_Multiple_Providers.ipynb
    │   ├── litellm_model_fallback.ipynb
    │   ├── litellm_router/
    │   │   ├── error_log.txt
    │   │   ├── load_test_proxy.py
    │   │   ├── load_test_queuing.py
    │   │   ├── load_test_router.py
    │   │   ├── request_log.txt
    │   │   ├── response_log.txt
    │   │   └── test_questions/
    │   ├── litellm_test_multiple_llm_demo.ipynb
    │   ├── logging_observability/
    │   │   └── LiteLLM_Langfuse.ipynb
    │   ├── proxy-server/
    │   └── result.html
    ├── docker/
    │   ├── .env.example
    ├── docker-compose.example.yml
    ├── litellm/
    │   ├── _logging.py
    │   ├── _redis.py
    │   ├── _version.py
    │   ├── budget_manager.py
    │   ├── caching.py
    │   ├── cost.json
    │   ├── deprecated_litellm_server/
    │   │   ├── .env.template
    │   │   ├── Dockerfile
    │   │   ├── main.py
    │   │   ├── requirements.txt
    │   │   └── server_utils.py
    │   ├── exceptions.py
    │   ├── integrations/
    │   │   ├── aispend.py
    │   │   ├── berrispend.py
    │   │   ├── custom_logger.py
    │   │   ├── dynamodb.py
    │   │   ├── helicone.py
    │   │   ├── langfuse.py
    │   │   ├── langsmith.py
    │   │   ├── litedebugger.py
    │   │   ├── llmonitor.py
    │   │   ├── prompt_layer.py
    │   │   ├── supabase.py
    │   │   ├── traceloop.py
    │   │   └── weights_biases.py
    │   ├── llms/
    │   │   ├── ai21.py
    │   │   ├── aleph_alpha.py
    │   │   ├── anthropic.py
    │   │   ├── azure.py
    │   │   ├── base.py
    │   │   ├── baseten.py
    │   │   ├── bedrock.py
    │   │   ├── cloudflare.py
    │   │   ├── cohere.py
    │   │   ├── custom_httpx/
    │   │   ├── gemini.py
    │   │   ├── huggingface_llms_metadata/
    │   │   ├── huggingface_restapi.py
    │   │   ├── maritalk.py
    │   │   ├── nlp_cloud.py
    │   │   ├── ollama.py
    │   │   ├── ollama_chat.py
    │   │   ├── oobabooga.py
    │   │   ├── openai.py
    │   │   ├── openrouter.py
    │   │   ├── palm.py
    │   │   ├── petals.py
    │   │   ├── prompt_templates/
    │   │   ├── replicate.py
    │   │   ├── sagemaker.py
    │   │   ├── together_ai.py
    │   │   ├── tokenizers/
    │   │   ├── vertex_ai.py
    │   │   └── vllm.py
    │   ├── main.py
    │   ├── model_prices_and_context_window_backup.json
    │   ├── proxy/
    │   │   ├── _experimental/
    │   │   ├── _types.py
    │   │   ├── admin_ui.py
    │   │   ├── example_config_yaml/
    │   │   ├── health_check.py
    │   │   ├── hooks/
    │   │   ├── lambda.py
    │   │   ├── openapi.json
    │   │   ├── otel_config.yaml
    │   │   ├── proxy_cli.py
    │   │   ├── proxy_config.yaml
    │   │   ├── proxy_server.py
    │   │   ├── queue/
    │   │   ├── schema.prisma
    │   │   ├── secret_managers/
    │   │   ├── start.sh
    │   │   └── utils.py
    │   ├── requirements.txt
    │   ├── router.py
    │   ├── router_strategy/
    │   │   ├── least_busy.py
    │   │   ├── lowest_latency.py
    │   │   └── lowest_tpm_rpm.py
    │   ├── timeout.py
    │   ├── types/
    │   │   ├── completion.py
    │   │   ├── embedding.py
    │   │   └── router.py
    │   └── utils.py
    ├── model_prices_and_context_window.json
    ├── poetry.lock
    ├── proxy_server_config.yaml
    ├── pyproject.toml
    ├── requirements.txt
    ├── template.yaml
    └── ui/
        ├── Dockerfile
        ├── admin.py
        ├── pages/
        │   └── user.py
        └── requirements.txt

```

---

##  Modules

<details closed><summary>.</summary>

| File                                                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---                                                                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [template.yaml](https://github.com/BerriAI/litellm/blob/main/template.yaml)                                               | This code snippet is part of a serverless application that deploys a Lambda function. It sets up the function's permissions, configuration, and deployment preferences, including error monitoring. The function is written in Python and uses the AWS Serverless Application Model (SAM) framework.                                                                                                                                                                                                                                                                                                            |
| [docker-compose.example.yml](https://github.com/BerriAI/litellm/blob/main/docker-compose.example.yml)                     | This code snippet defines the Docker configuration for the litellm service in the repository. It specifies the image, ports, volumes, and command for running the service.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Dockerfile.alpine](https://github.com/BerriAI/litellm/blob/main/Dockerfile.alpine)                                       | This code snippet is responsible for building and running the litellm service in a Docker container. It sets up the necessary dependencies, installs the package, and exposes port 4000 for communication.                                                                                                                                                                                                                                                                                                                                                                                                      |
| [requirements.txt](https://github.com/BerriAI/litellm/blob/main/requirements.txt)                                         | The code snippet in the litellm directory is a proxy server that handles requests and routes them to various language models (LLMs). It uses FastAPI for the server, Redis for caching, and has dependencies for different LLM integrations such as OpenAI, Azure, HuggingFace, etc.                                                                                                                                                                                                                                                                                                                            |
| [proxy_server_config.yaml](https://github.com/BerriAI/litellm/blob/main/proxy_server_config.yaml)                         | The code snippet is a part of the `litellm` repository and is responsible for configuring models and settings for the litellm proxy server. It sets up parameters for different models, including their API endpoints and keys, and defines general and litellm-specific settings. This code helps in managing and handling requests to the proxy server.                                                                                                                                                                                                                                                       |
| [Dockerfile](https://github.com/BerriAI/litellm/blob/main/Dockerfile)                                                     | This code snippet is responsible for building and running a Docker image for a software application called `litellm`. It installs the necessary dependencies, copies the code into the container, builds the package, and installs it. The image is then run and exposes port 4000.                                                                                                                                                                                                                                                                                                                             |
| [pyproject.toml](https://github.com/BerriAI/litellm/blob/main/pyproject.toml)                                             | The code snippet is part of the `litellm` repository, which is a library that facilitates communication with Language Model (LLM) API providers. The code manages dependencies, defines server functionality, and handles various integrations. It supports proxy-related functionalities, including routing strategies. The code snippet plays a vital role in the architecture by enabling smooth and efficient communication with LLM providers.                                                                                                                                                             |
| [.env.example](https://github.com/BerriAI/litellm/blob/main/.env.example)                                                 | The code snippet is part of a larger repository that implements a software architecture for a language model system. It includes various files and directories related to model integration, caching, logging, routing, and more. The snippet's critical features involve the integration of various language model providers, such as OpenAI, Cohere, OpenRouter, Azure, Replicate, and Anthropic. These integrations are enabled through API keys and base URLs provided for each provider. Additionally, the codebase utilizes a range of dependencies and software tools mentioned in the.env.example file. |
| [poetry.lock](https://github.com/BerriAI/litellm/blob/main/poetry.lock)                                                   | The code snippet is part of a repository with a well-organized directory structure. It performs critical functions related to the repository's architecture, but the specific details of its implementation are not mentioned.                                                                                                                                                                                                                                                                                                                                                                                  |
| [model_prices_and_context_window.json](https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json) | The code snippet in this repository is a critical part of the architecture that provides various Jupyter notebooks for benchmarking and evaluating Lite Language Models (LLMs). It includes examples for different use cases and comparisons between LLMs.                                                                                                                                                                                                                                                                                                                                                      |

</details>

<details closed><summary>ui</summary>

| File                                                                                 | Summary                                                                                                                                                                                                                                        |
| ---                                                                                  | ---                                                                                                                                                                                                                                            |
| [requirements.txt](https://github.com/BerriAI/litellm/blob/main/ui/requirements.txt) | The code snippet is part of a larger repository with a complex directory structure. It includes dependencies such as streamlit, python-dotenv, and supabase.                                                                                   |
| [Dockerfile](https://github.com/BerriAI/litellm/blob/main/ui/Dockerfile)             | This code snippet is responsible for building a Docker image for a Streamlit-based UI. It installs dependencies, copies the project directory, and specifies the entrypoint command for running the UI using Streamlit.                        |
| [admin.py](https://github.com/BerriAI/litellm/blob/main/ui/admin.py)                 | The code snippet in this repository is part of the parent architecture and is responsible for implementing critical features as a Tech Lead and Software Engineer. It achieves its role by [insert specific achievements of the code snippet]. |

</details>

<details closed><summary>ui.pages</summary>

| File                                                                     | Summary                                                                                                                                                                                                                                                                                                                                             |
| ---                                                                      | ---                                                                                                                                                                                                                                                                                                                                                 |
| [user.py](https://github.com/BerriAI/litellm/blob/main/ui/pages/user.py) | The code snippet is a Python script that handles user authentication and user configuration for a Streamlit UI. It uses Supabase passwordless authentication and communicates with a proxy server. The script allows users to sign in with their email, create a key, and access user-specific configurations based on their authentication status. |

</details>

<details closed><summary>docker</summary>

| File                                                                             | Summary                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---                                                                              | ---                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [.env.example](https://github.com/BerriAI/litellm/blob/main/docker/.env.example) | The code snippet is part of a larger repository with a directory structure containing various notebooks, integrations, and modules. It includes files related to the LiteLLM project, such as the main code, budget management, caching, exceptions, router strategy, and utility functions. The snippet focuses on the configuration and setup of secrets, database, and user authentication for the LiteLLM server. |

</details>

<details closed><summary>cookbook</summary>

| File                                                                                                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                                                                         |
| ---                                                                                                                                                                        | ---                                                                                                                                                                                                                                                                                                                                                                                             |
| [LiteLLM_Petals.ipynb](https://github.com/BerriAI/litellm/blob/main/cookbook/LiteLLM_Petals.ipynb)                                                                         | The provided code snippet is part of a larger repository with a specific directory structure. It is responsible for managing the Docker configuration and includes various notebooks for benchmarking and evaluating a language model. This code supports the repository's architecture by providing a standardized environment and tools for working with the language model.                  |
| [LiteLLM_Completion_Cost.ipynb](https://github.com/BerriAI/litellm/blob/main/cookbook/LiteLLM_Completion_Cost.ipynb)                                                       | This code snippet is a part of the litellm repository, which follows a specific directory structure. It performs critical functions such as benchmarking LLMs, evaluating LLMs, and comparing LLMs. It also includes examples and documentation for using litellm with various platforms and frameworks.                                                                                        |
| [litellm_Test_Multiple_Providers.ipynb](https://github.com/BerriAI/litellm/blob/main/cookbook/litellm_Test_Multiple_Providers.ipynb)                                       | This code snippet is part of the parent repository's architecture and is responsible for managing the CircleCI configuration and requirements. It ensures the proper setup and execution of CI/CD pipelines for the codebase. The snippet is found in the `.circleci` directory within the repository.                                                                                          |
| [VLLM_Model_Testing.ipynb](https://github.com/BerriAI/litellm/blob/main/cookbook/VLLM_Model_Testing.ipynb)                                                                 | The code snippet is part of a larger repository with a specific directory structure. It includes various notebooks for benchmarking, evaluating, and examples of using a software library called LiteLLM. The main role of the code is to demonstrate the capabilities and usage of LiteLLM in different scenarios.                                                                             |
| [litellm_model_fallback.ipynb](https://github.com/BerriAI/litellm/blob/main/cookbook/litellm_model_fallback.ipynb)                                                         | The code snippet in `litellm_model_fallback.ipynb` notebook demonstrates how to use the `litellm` library to implement model fallback in a chat application. It imports the necessary modules, defines a list of models to fallback on, and uses the `completion` function to generate a response from the models. If an error occurs, it prints the error message.                             |
| [LiteLLM_OpenRouter.ipynb](https://github.com/BerriAI/litellm/blob/main/cookbook/LiteLLM_OpenRouter.ipynb)                                                                 | The code snippet in the file `cookbook/LiteLLM_OpenRouter.ipynb` showcases the usage of the LiteLLM OpenRouter Library. It demonstrates how to make API calls to different models and receive responses for text completion tasks, such as generating code to say hi in different programming languages.                                                                                        |
| [litellm_test_multiple_llm_demo.ipynb](https://github.com/BerriAI/litellm/blob/main/cookbook/litellm_test_multiple_llm_demo.ipynb)                                         | This code snippet in the litellm_test_multiple_llm_demo.ipynb notebook demonstrates how to use the litellm package to make completion API calls to multiple language models such as OpenAI, Cohere, and Replicate. The code sets environment variables for the API keys and sends messages to each model for generating responses.                                                              |
| [liteLLM_Ollama.ipynb](https://github.com/BerriAI/litellm/blob/main/cookbook/liteLLM_Ollama.ipynb)                                                                         | The code snippet in the litellm repository serves a critical role in the architecture by providing a collection of Jupyter notebooks for benchmarking, evaluating, and comparing LiteLLMs. It includes examples for various use cases and integrations with Azure and OpenAI.                                                                                                                   |
| [LiteLLM_User_Based_Rate_Limits.ipynb](https://github.com/BerriAI/litellm/blob/main/cookbook/LiteLLM_User_Based_Rate_Limits.ipynb)                                         | The code snippet in the litellm repository is a collection of Jupyter notebooks that showcase various examples and evaluations of the LiteLLM language model. The notebooks cover topics such as benchmarking, evaluation, and comparison of LiteLLM with other language models.                                                                                                                |
| [LiteLLM_HuggingFace.ipynb](https://github.com/BerriAI/litellm/blob/main/cookbook/LiteLLM_HuggingFace.ipynb)                                                               | The code snippet in this repository is crucial in enabling benchmarking, evaluating, and comparing different language models (LLMs). It provides notebooks with examples and use cases for utilizing the LiteLLM library, showcasing its integration with Azure, OpenAI, and HuggingFace.                                                                                                       |
| [LiteLLM_Bedrock.ipynb](https://github.com/BerriAI/litellm/blob/main/cookbook/LiteLLM_Bedrock.ipynb)                                                                       | This code snippet contributes to the parent repository's architecture by providing various Jupyter notebooks in the `cookbook` directory. These notebooks cover topics such as benchmarking LLMs, evaluating LLMs, and demonstrating examples with Azure and OpenAI. The code enables users to explore and experiment with different aspects of the LLMs.                                       |
| [liteLLM_Langchain_Demo.ipynb](https://github.com/BerriAI/litellm/blob/main/cookbook/liteLLM_Langchain_Demo.ipynb)                                                         | Error generating summary: HTTPStatusError occurred. See logs for details.                                                                                                                                                                                                                                                                                                                       |
| [liteLLM_Baseten.ipynb](https://github.com/BerriAI/litellm/blob/main/cookbook/liteLLM_Baseten.ipynb)                                                                       | The code snippet in this repository is part of the parent repository's architecture. It contributes to the functionality of the system by providing implementation details for various use cases and evaluation of the LiteLLM models. Its role is to showcase examples, benchmarks, and comparisons of the LiteLLM models.                                                                     |
| [liteLLM_Getting_Started.ipynb](https://github.com/BerriAI/litellm/blob/main/cookbook/liteLLM_Getting_Started.ipynb)                                                       | This code snippet is a part of the litellm repository, which has a directory structure containing various files and folders. The code achieves specific functionalities related to benchmarking, evaluation, and examples of the LiteLLM language model.                                                                                                                                        |
| [Evaluating_LLMs.ipynb](https://github.com/BerriAI/litellm/blob/main/cookbook/Evaluating_LLMs.ipynb)                                                                       | Code snippet:-Implements a CircleCI configuration file and requirements.txt file for the repository's continuous integration process.-Configures the environment variables for the project.                                                                                                                                                                                                     |
| [liteLLM_VertextAI_Example.ipynb](https://github.com/BerriAI/litellm/blob/main/cookbook/liteLLM_VertextAI_Example.ipynb)                                                   | Error generating summary: HTTPStatusError occurred. See logs for details.                                                                                                                                                                                                                                                                                                                       |
| [liteLLM_function_calling.ipynb](https://github.com/BerriAI/litellm/blob/main/cookbook/liteLLM_function_calling.ipynb)                                                     | The code snippet plays a critical role in the repository's architecture. It achieves specific functionalities related to benchmarking, evaluation, and examples of LiteLLMs, utilizing various notebooks in the cookbook directory.                                                                                                                                                             |
| [TogetherAI_liteLLM.ipynb](https://github.com/BerriAI/litellm/blob/main/cookbook/TogetherAI_liteLLM.ipynb)                                                                 | The code snippet in the parent repository is responsible for various tasks related to benchmarking, evaluating, and showcasing the capabilities of LiteLLM language models. It includes notebooks for different use cases and examples integrating with Azure, OpenAI, Bedrock, and HuggingFace.                                                                                                |
| [LiteLLM_batch_completion.ipynb](https://github.com/BerriAI/litellm/blob/main/cookbook/LiteLLM_batch_completion.ipynb)                                                     | This code snippet demonstrates batch completions using the LiteLLM library. It enables efficient processing of multiple prompts in a single API call. The snippet shows how to import the necessary modules, set the API key, and call the `litellm.batch_completion` function with a list of messages. The responses are returned as a list of completion results.                             |
| [liteLLM_A121_Jurrasic_example.ipynb](https://github.com/BerriAI/litellm/blob/main/cookbook/liteLLM_A121_Jurrasic_example.ipynb)                                           | Error generating summary: HTTPStatusError occurred. See logs for details.                                                                                                                                                                                                                                                                                                                       |
| [Parallel_function_calling.ipynb](https://github.com/BerriAI/litellm/blob/main/cookbook/Parallel_function_calling.ipynb)                                                   | The code snippet in the `cookbook/` directory provides a collection of Jupyter notebooks demonstrating various use cases and integrations of the LiteLLM framework. It showcases benchmarking, evaluation, and example applications with Azure, OpenAI, HuggingFace, Bedrock, and other platforms.                                                                                              |
| [LiteLLM_PromptLayer.ipynb](https://github.com/BerriAI/litellm/blob/main/cookbook/LiteLLM_PromptLayer.ipynb)                                                               | The code snippet, located in the `.circleci` directory, serves as the configuration file for the CircleCI integration in the parent repository. It ensures the seamless deployment of the repository's code by specifying the CI/CD pipeline stages and their associated tasks.                                                                                                                 |
| [Benchmarking_LLMs_by_use_case.ipynb](https://github.com/BerriAI/litellm/blob/main/cookbook/Benchmarking_LLMs_by_use_case.ipynb)                                           | Code snippet: `config.yml`Summary: The `config.yml` file in the `.circleci` directory defines the configuration for the CircleCI continuous integration pipeline in the `litellm` repository. It specifies the build and deployment process for the codebase.                                                                                                                                   |
| [Claude_(Anthropic)_with_Streaming_liteLLM_Examples.ipynb](https://github.com/BerriAI/litellm/blob/main/cookbook/Claude_(Anthropic)_with_Streaming_liteLLM_Examples.ipynb) | This code snippet is part of a larger repository with a standardized directory structure. It contains various notebooks that demonstrate the usage and evaluation of a lightweight language model (LLM), emphasizing benchmarking and integration with other frameworks and services. The code aims to showcase the versatility and performance of the LLM in different tasks and environments. |
| [result.html](https://github.com/BerriAI/litellm/blob/main/cookbook/result.html)                                                                                           | The code snippet is part of a larger repository with a specific directory structure. It includes files related to CI/CD, environment variables, and Docker configuration. The snippet itself is located in the cookbook directory and consists of several Jupyter notebooks that demonstrate benchmarking, evaluation, and examples of using the LiteLLM tool with different platforms.         |
| [liteLLM_Streaming_Demo.ipynb](https://github.com/BerriAI/litellm/blob/main/cookbook/liteLLM_Streaming_Demo.ipynb)                                                         | This code snippet is part of a larger repository focused on the implementation of a tech lead and software engineer's role. It plays a critical role in the repository's architecture, achieving specific functionalities and features. For more information, please refer to the provided repository structure and directory layout.                                                           |
| [LiteLLM_Comparing_LLMs.ipynb](https://github.com/BerriAI/litellm/blob/main/cookbook/LiteLLM_Comparing_LLMs.ipynb)                                                         | The code snippet is a part of a larger repository that contains various notebooks for evaluating and benchmarking language models (LLMs). The snippet's main role is to provide examples and demonstrations of using the LiteLLM library in different scenarios. It showcases how LiteLLM can be used with various platforms and tools such as Azure, OpenAI, and HuggingFace.                  |
| [liteLLM_Replicate_Demo.ipynb](https://github.com/BerriAI/litellm/blob/main/cookbook/liteLLM_Replicate_Demo.ipynb)                                                         | The code snippet is part of the litellm repository, which has a defined directory structure and contains various files related to building, testing, and documenting the project. The main role of this code is not specified in the provided information.                                                                                                                                      |
| [LiteLLM_Azure_and_OpenAI_example.ipynb](https://github.com/BerriAI/litellm/blob/main/cookbook/LiteLLM_Azure_and_OpenAI_example.ipynb)                                     | The code snippet in the litellm repository is responsible for managing the Docker configuration, CircleCI integration, and GitHub workflows. It includes files such as Dockerfiles, CircleCI configuration, and GitHub workflow templates.                                                                                                                                                      |
| [Using_Nemo_Guardrails_with_LiteLLM_Server.ipynb](https://github.com/BerriAI/litellm/blob/main/cookbook/Using_Nemo_Guardrails_with_LiteLLM_Server.ipynb)                   | The code snippet demonstrates how to use Nemo-Guardrails with LiteLLM Server. It shows examples of using Bedrock and TogetherAI providers, including setting up the necessary environment variables and API keys. The code also provides a sample `config.yml` file for configuring conversations with the AI assistant.                                                                        |

</details>

<details closed><summary>cookbook.benchmark</summary>

| File                                                                                         | Summary                                                                                                                                                                                                                                                                                                |
| ---                                                                                          | ---                                                                                                                                                                                                                                                                                                    |
| [benchmark.py](https://github.com/BerriAI/litellm/blob/main/cookbook/benchmark/benchmark.py) | This code snippet benchmarks the response time and cost of different language models (LLMs) for a given set of questions. It uses the `completion` function from the `litellm` module to generate responses and calculates the response time and cost. The results are displayed in a formatted table. |

</details>

<details closed><summary>cookbook.benchmark.eval_suites_mlflow_autoevals</summary>

| File                                                                                                                        | Summary                                                                                                                                                                                                                                                                            |
| ---                                                                                                                         | ---                                                                                                                                                                                                                                                                                |
| [auto_evals.py](https://github.com/BerriAI/litellm/blob/main/cookbook/benchmark/eval_suites_mlflow_autoevals/auto_evals.py) | The code snippet is a part of the `litellm` repository and demonstrates how to use the `litellm` library for text completion. It showcases the completion functionality and includes an example of using the Factuality evaluator to assess the accuracy of the completion output. |

</details>

<details closed><summary>cookbook.codellama-server</summary>

| File                                                                                          | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---                                                                                           | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [README.MD](https://github.com/BerriAI/litellm/blob/main/cookbook/codellama-server/README.MD) | The code snippet is part of the CodeLlama Server in the litellm repository. It integrates with various language models (LLMs) such as Anthropic, Huggingface, and Azure to answer coding questions. It handles caching, error handling with model fallbacks, and prompt logging. The code provides consistent input/output format, supports streaming and async operations, and includes API endpoints for chat completions. It also includes installation and deployment instructions. |
| [main.py](https://github.com/BerriAI/litellm/blob/main/cookbook/codellama-server/main.py)     | This code snippet is a Flask server that provides API endpoints for chat completions and getting available models. It utilizes the `litellm` library for handling completions and models. The server listens on port 4000 and returns responses in JSON format.                                                                                                                                                                                                                         |

</details>

<details closed><summary>cookbook.community-resources</summary>

| File                                                                                                           | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---                                                                                                            | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [get_hf_models.py](https://github.com/BerriAI/litellm/blob/main/cookbook/community-resources/get_hf_models.py) | The code snippet retrieves models from a paginated API endpoint and cleans the retrieved data. It then writes the cleaned models to separate text files. The code uses the `requests` library to make HTTP requests and the `urllib.parse` module to parse URLs.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [max_tokens.json](https://github.com/BerriAI/litellm/blob/main/cookbook/community-resources/max_tokens.json)   | The code snippet in this repository is responsible for managing budgets and caching in a language model (LLM) system. It includes files for budget management, caching, integrations with various LLMs, and a router for strategizing LLM requests. The codebase also provides information on model prices and context window backup. The repository structure consists of different directories for various functionalities, such as benchmarking, routing, logging, and UI. The codebase utilizes dependencies and software specified in the `max_tokens.json` file, which provides information on the maximum tokens, input cost per token, and output cost per token for different LLMs. |

</details>

<details closed><summary>cookbook.litellm_router</summary>

| File                                                                                                              | Summary                                                                                                                                                                                                                                                                                                                                                            |
| ---                                                                                                               | ---                                                                                                                                                                                                                                                                                                                                                                |
| [error_log.txt](https://github.com/BerriAI/litellm/blob/main/cookbook/litellm_router/error_log.txt)               | The code snippet in this repository plays a critical role in the architecture by implementing various notebooks that showcase the functionality and capabilities of the LiteLLM model for different use cases. It provides examples, benchmarks, and evaluations of the LiteLLM model integration with various platforms and technologies.                         |
| [load_test_proxy.py](https://github.com/BerriAI/litellm/blob/main/cookbook/litellm_router/load_test_proxy.py)     | This code snippet is part of the litellm repository and it focuses on load testing the litellm router by making concurrent calls to different language models. It logs the requests and exceptions, and provides a summary of successful and failed calls.                                                                                                         |
| [load_test_queuing.py](https://github.com/BerriAI/litellm/blob/main/cookbook/litellm_router/load_test_queuing.py) | The code snippet is responsible for making concurrent calls to multiple language models (LLMs) using the litellm library. It reads questions from text files, sends them as requests to the LLMs, and logs the request details and responses. The snippet also summarizes the load test results, including the total requests, successful calls, and failed calls. |
| [request_log.txt](https://github.com/BerriAI/litellm/blob/main/cookbook/litellm_router/request_log.txt)           | The code snippet in litellm/litellm/router.py plays a critical role in managing the LiteLLM server's routing strategy. It determines the allocation of incoming requests to different language models (LLMs) based on factors like latency, TPM, and RPM, ensuring efficient and effective utilization of LLM resources.                                           |
| [response_log.txt](https://github.com/BerriAI/litellm/blob/main/cookbook/litellm_router/response_log.txt)         | The code snippet in the `litellm_router` directory is responsible for logging responses in the LiteLLM project. It utilizes the `response_log.txt` file to store the logged responses.                                                                                                                                                                             |
| [load_test_router.py](https://github.com/BerriAI/litellm/blob/main/cookbook/litellm_router/load_test_router.py)   | The code snippet in `cookbook/litellm_router/load_test_router.py` demonstrates making concurrent calls to multiple models using the `litellm` library. It randomly selects questions, makes API calls, logs requests and responses, and summarizes the results of the load test.                                                                                   |

</details>

<details closed><summary>cookbook.litellm_router.test_questions</summary>

| File                                                                                                               | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---                                                                                                                | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [question3.txt](https://github.com/BerriAI/litellm/blob/main/cookbook/litellm_router/test_questions/question3.txt) | This code snippet is part of the litellm repository's architecture. It manages the litellm proxy server, which handles requests for various language models (LLMs) such as Huggingface, Bedrock, and TogetherAI. The proxy server allows for custom prompt templates and model-specific configurations, making it flexible and versatile. Key endpoints include `/chat/completions`, `/completions`, `/embeddings`, and `/models`. The codebase depends on multiple software and libraries.                                                                                                             |
| [question2.txt](https://github.com/BerriAI/litellm/blob/main/cookbook/litellm_router/test_questions/question2.txt) | This code snippet is part of the litellm repository and focuses on the implementation of the LiteLLM software. It supports multiple language models (LLMs) such as OpenAI, Azure, Bedrock, and more. The code handles translation of inputs to LLM provider endpoints and ensures consistent output. It also provides exception mapping and supports streaming responses from the models.                                                                                                                                                                                                               |
| [question1.txt](https://github.com/BerriAI/litellm/blob/main/cookbook/litellm_router/test_questions/question1.txt) | The code snippet is part of the litellm repository and is responsible for managing and calling various Language Model APIs. It provides a unified interface to call APIs from providers such as Bedrock, Azure, OpenAI, Cohere, Anthropic, Ollama, Sagemaker, HuggingFace, and Replicate. Key features include translating inputs to provider completion and embedding endpoints, ensuring consistent output, and mapping common exceptions. The code snippet demonstrates how to make API calls using the OpenAI and Cohere models. It also showcases the support for streaming responses from models. |

</details>

<details closed><summary>cookbook.logging_observability</summary>

| File                                                                                                                         | Summary                                                                                                                                                                                                                                  |
| ---                                                                                                                          | ---                                                                                                                                                                                                                                      |
| [LiteLLM_Langfuse.ipynb](https://github.com/BerriAI/litellm/blob/main/cookbook/logging_observability/LiteLLM_Langfuse.ipynb) | The code snippet demonstrates how to use LiteLLM with Langfuse for observability purposes. It installs dependencies, sets environment variables, and showcases how to use LangFuse as a callback for OpenAI and Cohere completion calls. |

</details>

<details closed><summary>cookbook.litellm-ollama-docker-image</summary>

| File                                                                                                                   | Summary                                                                                                                                                                                                                                                                                                                                                         |
| ---                                                                                                                    | ---                                                                                                                                                                                                                                                                                                                                                             |
| [requirements.txt](https://github.com/BerriAI/litellm/blob/main/cookbook/litellm-ollama-docker-image/requirements.txt) | The code snippet in the `litellm` directory plays a critical role in the parent repository's architecture. It contains essential files for managing budgets, integrating external services, handling exceptions, and routing requests to different language models. The code snippet's main features include caching, timeouts, and proxy server configuration. |
| [Dockerfile](https://github.com/BerriAI/litellm/blob/main/cookbook/litellm-ollama-docker-image/Dockerfile)             | The code snippet is responsible for setting up and running the LiteLLM Docker image within the repository. It installs the necessary dependencies, copies the code into a container, and executes the LiteLLM application using the provided start script.                                                                                                      |
| [test.py](https://github.com/BerriAI/litellm/blob/main/cookbook/litellm-ollama-docker-image/test.py)                   | The code snippet demonstrates how to use the OpenAI API to send chat completion requests to a proxy server with streaming. It sets the API base and key, creates a chat completion request with streaming, and prints the response chunks. It also shows a regular chat completion request and prints the response.                                             |
| [start.sh](https://github.com/BerriAI/litellm/blob/main/cookbook/litellm-ollama-docker-image/start.sh)                 | This code snippet plays a critical role in the architecture of the parent repository. It includes the `start.sh` script that is used to launch the Ollama server and the main `litellm` file, which is an essential component of the codebase.                                                                                                                  |

</details>

<details closed><summary>.github</summary>

| File                                                                            | Summary                                                                                                                                                                                                                                                                                                                                                                                               |
| ---                                                                             | ---                                                                                                                                                                                                                                                                                                                                                                                                   |
| [FUNDING.yml](https://github.com/BerriAI/litellm/blob/main/.github/FUNDING.yml) | The code snippet plays a critical role in the parent repository's architecture by implementing integration with various external services, including AI models, logging, caching, and budget management. It also includes dependencies for GitHub Sponsors, Patreon, Open Collective, Ko-fi, Tidelift, Community Bridge, Liberapay, IssueHunt, Otechie, LFX Crowdfunding, and custom Stripe payments. |

</details>

<details closed><summary>.github.workflows</summary>

| File                                                                                              | Summary                                                                                                                                                                                                                                                                                                                                    |
| ---                                                                                               | ---                                                                                                                                                                                                                                                                                                                                        |
| [lint.yml](https://github.com/BerriAI/litellm/blob/main/.github/workflows/lint.yml)               | The code snippet is a GitHub Actions workflow that performs linting on the codebase. It uses flake8 to analyze the code for style and syntax issues. The workflow is triggered on push to the main branch and pull requests to the main or master branches. It installs the necessary dependencies and then runs the flake8 linter.        |
| [ghcr_deploy.yml](https://github.com/BerriAI/litellm/blob/main/.github/workflows/ghcr_deploy.yml) | This code snippet is a GitHub Actions workflow that builds and publishes a Docker image for the LiteLLM repository. It logs in to the Container registry, extracts metadata for the image, and then builds and pushes the image to the registry. There is a separate step for building and pushing the Alpine version of the Docker image. |

</details>

<details closed><summary>.github.ISSUE_TEMPLATE</summary>

| File                                                                                                           | Summary                                                                                                                                                                                                                                                                                                                 |
| ---                                                                                                            | ---                                                                                                                                                                                                                                                                                                                     |
| [feature_request.yml](https://github.com/BerriAI/litellm/blob/main/.github/ISSUE_TEMPLATE/feature_request.yml) | The codebase is a repository for the LiteLLM project, which includes various modules and notebooks for working with LiteLLM language models. The code snippet is part of the main module and provides essential features such as budget management, caching, integration with external services, and router strategies. |
| [bug_report.yml](https://github.com/BerriAI/litellm/blob/main/.github/ISSUE_TEMPLATE/bug_report.yml)           | The code snippet is part of a larger repository that contains various notebooks, libraries, and server components. It implements a bug reporting template for filing bug reports, including information about the issue, relevant logs, and optional contact details.                                                   |
| [config.yml](https://github.com/BerriAI/litellm/blob/main/.github/ISSUE_TEMPLATE/config.yml)                   | The code snippet in the `litellm/router.py` file is responsible for implementing the routing strategy in the LiteLLM repository. It determines how the requests are distributed among the available language models based on factors like latency and availability.                                                     |

</details>

<details closed><summary>litellm</summary>

| File                                                                                                                                            | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---                                                                                                                                             | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [_logging.py](https://github.com/BerriAI/litellm/blob/main/litellm/_logging.py)                                                                 | The code snippet defines a function called `print_verbose` which prints a statement if the `set_verbose` flag is set to `True`. This function is used for logging and debugging purposes within the codebase.                                                                                                                                                                                                                                      |
| [requirements.txt](https://github.com/BerriAI/litellm/blob/main/litellm/requirements.txt)                                                       | The code snippet in this repository is the Litellm Proxy, a crucial component of the larger Litellm system. It manages dependencies, handles API requests, and provides caching functionality for various Language Model Microservices (LLMs), optimizing their usage and efficiency. The Litellm Proxy works seamlessly with several external services and tools, including OpenAI, Redis, AWS Bedrock and SageMaker, Google Vertex AI, and more. |
| [_version.py](https://github.com/BerriAI/litellm/blob/main/litellm/_version.py)                                                                 | The code snippet retrieves the version number of the `litellm` package using `importlib_metadata`. It is a dependency used in the codebase for version management.                                                                                                                                                                                                                                                                                 |
| [cost.json](https://github.com/BerriAI/litellm/blob/main/litellm/cost.json)                                                                     | This code snippet in the `litellm` repository is responsible for managing the cost of different language models. It uses `cost.json` to store the pricing information for each model, such as `gpt-3.5-turbo-0613`, `claude-2`, and `gpt-4-0613`.                                                                                                                                                                                                  |
| [timeout.py](https://github.com/BerriAI/litellm/blob/main/litellm/timeout.py)                                                                   | The code snippet provides a decorator called timeout that wraps a function, raising a specified exception if the execution time exceeds the specified timeout duration. It works with both synchronous and asynchronous callables. It utilizes threads and asyncio for synchronous callables.                                                                                                                                                      |
| [model_prices_and_context_window_backup.json](https://github.com/BerriAI/litellm/blob/main/litellm/model_prices_and_context_window_backup.json) | The code snippet plays a crucial role in the parent repository's architecture, contributing to its overall structure and functionality. It achieves specific objectives related to benchmarking, evaluation, and examples of different LiteLM models. The code is part of a larger collection of notebooks and scripts, showcasing the versatility and applicability of LiteLM technology.                                                         |
| [caching.py](https://github.com/BerriAI/litellm/blob/main/litellm/caching.py)                                                                   | The code snippet plays a significant role in the overall architecture of the repository. It is responsible for managing the Docker configuration and providing various Jupyter notebooks for different use cases and evaluations.                                                                                                                                                                                                                  |
| [utils.py](https://github.com/BerriAI/litellm/blob/main/litellm/utils.py)                                                                       | The code snippet in the `cookbook/` directory of the repository provides a collection of Jupyter notebooks with examples, benchmarks, and tutorials demonstrating the usage and capabilities of the LiteLLM software. It showcases various use cases and features of the software in a structured and easily accessible manner.                                                                                                                    |
| [exceptions.py](https://github.com/BerriAI/litellm/blob/main/litellm/exceptions.py)                                                             | The code snippet provides LiteLLM versions of the OpenAI Exception Types, allowing for more specific error handling when using LiteLLM. This enhances the error reporting and troubleshooting capabilities in the codebase.                                                                                                                                                                                                                        |
| [router.py](https://github.com/BerriAI/litellm/blob/main/litellm/router.py)                                                                     | The code snippet in the `cookbook` directory of the repository provides numerous Jupyter notebooks with examples, benchmarks, and guides for using and evaluating the LiteLLM language model.                                                                                                                                                                                                                                                      |
| [main.py](https://github.com/BerriAI/litellm/blob/main/litellm/main.py)                                                                         | This code snippet, located in the `litellm/cookbook` directory of the repository, provides a collection of Jupyter notebooks and benchmarking scripts for evaluating and using the LiteLLM language model. It offers examples, tutorials, and tests for various use cases and integration with different tools and frameworks.                                                                                                                     |
| [budget_manager.py](https://github.com/BerriAI/litellm/blob/main/litellm/budget_manager.py)                                                     | The code snippet `litellm/budget_manager.py` is responsible for managing the budget of users in the litellm repository. It includes functions for creating a budget, tracking costs, and updating budget data. It also supports data storage locally or in a hosted database.                                                                                                                                                                      |
| [_redis.py](https://github.com/BerriAI/litellm/blob/main/litellm/_redis.py)                                                                     | This code snippet provides functions for getting a Redis client and retrieving the Redis URL from the environment. It uses the `redis` library and allows for environment overrides.                                                                                                                                                                                                                                                               |

</details>

<details closed><summary>litellm.types</summary>

| File                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                         |
| ---                                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                             |
| [completion.py](https://github.com/BerriAI/litellm/blob/main/litellm/types/completion.py) | The `CompletionRequest` class in `litellm/types/completion.py` defines the structure of a completion request for the parent repository's codebase. It includes various parameters such as the model, messages, timeout, temperature, and more. The class also allows for additional parameters using the `extra = allow` configuration.                                         |
| [embedding.py](https://github.com/BerriAI/litellm/blob/main/litellm/types/embedding.py)   | The `embedding.py` file in the `litellm/types` directory defines a `EmbeddingRequest` model that represents a request for an embedding from a language model. It includes various optional parameters such as the model, input text, timeout, API settings, caching, user information, and logging details. This model allows for flexible and customizable embedding requests. |
| [router.py](https://github.com/BerriAI/litellm/blob/main/litellm/types/router.py)         | The `router.py` file in the `litellm/types` directory defines the configuration models for the router in the codebase. It includes models for defining the available models, their parameters, caching options, fallbacks, routing strategy, and more. These models are used by the router to manage and route requests to the appropriate language models.                     |

</details>

<details closed><summary>litellm.proxy</summary>

| File                                                                                              | Summary                                                                                                                                                                                                                                                                                                                                                                                          |
| ---                                                                                               | ---                                                                                                                                                                                                                                                                                                                                                                                              |
| [_types.py](https://github.com/BerriAI/litellm/blob/main/litellm/proxy/_types.py)                 | The code snippet in the repository plays a critical role in the architecture by implementing various Jupyter notebooks, providing examples, benchmarks, and evaluations for the LiteLLM model. It helps users understand and utilize the capabilities of the LiteLLM model effectively.                                                                                                          |
| [admin_ui.py](https://github.com/BerriAI/litellm/blob/main/litellm/proxy/admin_ui.py)             | The code snippet is responsible for managing the admin configuration of a proxy server using Streamlit. It allows users to add models, list models, and create API keys. The code interacts with the proxy server through HTTP requests.                                                                                                                                                         |
| [proxy_config.yaml](https://github.com/BerriAI/litellm/blob/main/litellm/proxy/proxy_config.yaml) | The code snippet is part of the litellm repository and is responsible for handling proxy server configurations. It utilizes various dependencies and software mentioned in litellm/proxy/proxy_config.yaml. The code defines different models and their parameters for the proxy server to interact with.                                                                                        |
| [proxy_cli.py](https://github.com/BerriAI/litellm/blob/main/litellm/proxy/proxy_cli.py)           | The code snippet plays a critical role in the repository's architecture by implementing various Jupyter notebook examples and benchmarks for the LiteLLM language model. It showcases the capabilities and usage of LiteLLM in different scenarios.                                                                                                                                              |
| [lambda.py](https://github.com/BerriAI/litellm/blob/main/litellm/proxy/lambda.py)                 | The code snippet in `litellm/proxy/lambda.py` is responsible for handling requests and routing them to the appropriate endpoints in the `litellm/proxy/proxy_server.py` module. It utilizes the `Mangum` library to enable serverless deployment.                                                                                                                                                |
| [schema.prisma](https://github.com/BerriAI/litellm/blob/main/litellm/proxy/schema.prisma)         | The code snippet contains the schema definition for the LiteLLM proxy server's database. It includes tables for user information and verification tokens. Dependencies include PostgreSQL and the Prisma ORM.                                                                                                                                                                                    |
| [proxy_server.py](https://github.com/BerriAI/litellm/blob/main/litellm/proxy/proxy_server.py)     | The code snippet in the repository contributes to the architecture by providing a collection of Jupyter notebooks with examples, benchmarks, and use cases for the LiteLLM language model. It demonstrates the capabilities and potential applications of the model without delving into technical implementation details.                                                                       |
| [otel_config.yaml](https://github.com/BerriAI/litellm/blob/main/litellm/proxy/otel_config.yaml)   | The code snippet is responsible for configuring and setting up the logging, metrics, traces, and logs pipelines using OpenTelemetry in the litellm/proxy/otel_config.yaml file. It includes receivers, processors, and exporters for different types of data and destinations.                                                                                                                   |
| [utils.py](https://github.com/BerriAI/litellm/blob/main/litellm/proxy/utils.py)                   | The code snippet in this repository serves as a part of the architecture for the parent repository. It is responsible for critical features such as benchmarking, evaluation, and examples for the LiteLLM language model. It is organized in a directory structure that includes Dockerfiles, notebooks, and other relevant files.                                                              |
| [health_check.py](https://github.com/BerriAI/litellm/blob/main/litellm/proxy/health_check.py)     | This code snippet is responsible for performing a health check on a language model (LLM). It takes a list of models as input and checks the health of each model by sending test messages. The results are categorized into healthy and unhealthy endpoints. The snippet also includes functions for getting a random message from the LLM and cleaning the LLM parameters for display purposes. |
| [openapi.json](https://github.com/BerriAI/litellm/blob/main/litellm/proxy/openapi.json)           | The code snippet in the litellm/proxy/openapi.json file defines the API routes and their corresponding request and response schemas. It primarily includes routes for creating chat completions, getting models, retrieving server logs, and a home route.                                                                                                                                       |
| [start.sh](https://github.com/BerriAI/litellm/blob/main/litellm/proxy/start.sh)                   | The code snippet in the `start.sh` file is responsible for starting the proxy server by executing the `proxy_cli.py` script using Python.                                                                                                                                                                                                                                                        |

</details>

<details closed><summary>litellm.proxy._experimental</summary>

| File                                                                                                              | Summary                                                                                                                                                                                                                 |
| ---                                                                                                               | ---                                                                                                                                                                                                                     |
| [post_call_rules.py](https://github.com/BerriAI/litellm/blob/main/litellm/proxy/_experimental/post_call_rules.py) | This code snippet is part of the `litellm/proxy` module in the repository. It defines a custom rule for post-processing the model response. If the response is shorter than 5 tokens, it triggers a fallback mechanism. |

</details>

<details closed><summary>litellm.proxy.secret_managers</summary>

| File                                                                                                      | Summary                                                                                                                                                                                                                                                     |
| ---                                                                                                       | ---                                                                                                                                                                                                                                                         |
| [google_kms.py](https://github.com/BerriAI/litellm/blob/main/litellm/proxy/secret_managers/google_kms.py) | This code snippet is part of the litellm repository and is responsible for integrating with Google Key Management Service (KMS). It validates the required environment variables and loads the Google KMS client if the `use_google_kms` parameter is true. |

</details>

<details closed><summary>litellm.proxy.hooks</summary>

| File                                                                                                                        | Summary                                                                                                                                                                                                                                                                                                                                      |
| ---                                                                                                                         | ---                                                                                                                                                                                                                                                                                                                                          |
| [max_budget_limiter.py](https://github.com/BerriAI/litellm/blob/main/litellm/proxy/hooks/max_budget_limiter.py)             | This code snippet defines the MaxBudgetLimiter class, which is a pre-call hook for the litellm proxy. It checks if the current spend of a user exceeds their maximum budget and raises an HTTPException if it does.                                                                                                                          |
| [parallel_request_limiter.py](https://github.com/BerriAI/litellm/blob/main/litellm/proxy/hooks/parallel_request_limiter.py) | The code snippet implements a MaxParallelRequestsHandler class that handles the maximum parallel request limit for API keys. It allows or denies requests based on the number of parallel requests made by a user with a specific API key. It also logs successful and failed requests, updating the count of parallel requests accordingly. |

</details>

<details closed><summary>litellm.proxy.queue</summary>

| File                                                                                                  | Summary                                                                                                                                                                                                                                                                            |
| ---                                                                                                   | ---                                                                                                                                                                                                                                                                                |
| [celery_app.py](https://github.com/BerriAI/litellm/blob/main/litellm/proxy/queue/celery_app.py)       | The code snippet is responsible for setting up and configuring the Redis and Celery dependencies for the litellm proxy server. It initializes Redis connection and creates a Celery task for processing jobs. It also ensures Celery workers are terminated when the script exits. |
| [celery_worker.py](https://github.com/BerriAI/litellm/blob/main/litellm/proxy/queue/celery_worker.py) | This code snippet starts a Celery worker process with a specified concurrency level and log level. It is used within the litellm/proxy/queue/celery_worker.py file to initiate the worker process for background task execution.                                                   |
| [rq_worker.py](https://github.com/BerriAI/litellm/blob/main/litellm/proxy/queue/rq_worker.py)         | The code snippet starts an RQ worker, which is responsible for processing tasks in a Redis queue. It establishes a connection to Redis, creates a worker, and assigns it to a queue for processing.                                                                                |

</details>

<details closed><summary>litellm.proxy.example_config_yaml</summary>

| File                                                                                                                                            | Summary                                                                                                                                                                                                                                                                                                                                                          |
| ---                                                                                                                                             | ---                                                                                                                                                                                                                                                                                                                                                              |
| [custom_auth.py](https://github.com/BerriAI/litellm/blob/main/litellm/proxy/example_config_yaml/custom_auth.py)                                 | This code snippet provides user API key authentication for the litellm proxy. It verifies the API key provided by the user against the modified master key stored in the environment variables. If the keys match, it returns the authenticated user.                                                                                                            |
| [azure_config.yaml](https://github.com/BerriAI/litellm/blob/main/litellm/proxy/example_config_yaml/azure_config.yaml)                           | This code snippet defines the configuration for two models (gpt-4-team1 and gpt-4-team2) in the litellm/proxy/example_config_yaml/azure_config.yaml file. It specifies the model details such as the model API, key, timeouts, and maximum retries. These configurations are critical for the functioning of the parent repository's proxy server.               |
| [aliases_config.yaml](https://github.com/BerriAI/litellm/blob/main/litellm/proxy/example_config_yaml/aliases_config.yaml)                       | This code snippet is part of the litellm repository's directory structure. It includes a configuration file for the litellm proxy, which handles requests to different language models. The snippet showcases an example request to the gpt-4 model, which is processed by the ollama/llama2 model and receives a response.                                      |
| [opentelemetry_config.yaml](https://github.com/BerriAI/litellm/blob/main/litellm/proxy/example_config_yaml/opentelemetry_config.yaml)           | This code snippet is responsible for implementing the proxy server architecture in the litellm repository. It utilizes OpenTelemetry for logging and includes specific configuration settings for the gpt-3.5-turbo model.                                                                                                                                       |
| [simple_config.yaml](https://github.com/BerriAI/litellm/blob/main/litellm/proxy/example_config_yaml/simple_config.yaml)                         | The code snippet is part of the litellm repository architecture. It contributes to the routing and management of various language models (LLMs) and handles dependencies for the LLM proxy server. Key files include model_list and proxy_server_config.yaml. Dependencies and software used are listed in litellm/proxy/example_config_yaml/simple_config.yaml. |
| [load_balancer.yaml](https://github.com/BerriAI/litellm/blob/main/litellm/proxy/example_config_yaml/load_balancer.yaml)                         | This code snippet defines the model-specific settings and environment variables for the Litellm repository. It specifies the models to be used and their respective parameters, such as the model name and API key. It also sets environment variables for the Redis host, password, and port.                                                                   |
| [langfuse_config.yaml](https://github.com/BerriAI/litellm/blob/main/litellm/proxy/example_config_yaml/langfuse_config.yaml)                     | The code snippet in this repository is responsible for integrating with the Langfuse service, providing observability and handling success callbacks for the gpt-3.5-turbo model. It includes the necessary settings and dependencies.                                                                                                                           |
| [_health_check_test_config.yaml](https://github.com/BerriAI/litellm/blob/main/litellm/proxy/example_config_yaml/_health_check_test_config.yaml) | This code snippet is part of the `litellm` repository and contributes to the architecture by implementing a proxy server. It enables background health checks and allows for embedding models using Azure services.                                                                                                                                              |
| [custom_callbacks.py](https://github.com/BerriAI/litellm/blob/main/litellm/proxy/example_config_yaml/custom_callbacks.py)                       | The code snippet defines custom callbacks for the LiteLLM Proxy. These callbacks are used to handle various events during the API calls, such as pre-API call, post-API call, stream event, success event, and failure event. The callbacks provide additional logging and functionality to the LiteLLM Proxy.                                                   |

</details>

<details closed><summary>litellm.integrations</summary>

| File                                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---                                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [litedebugger.py](https://github.com/BerriAI/litellm/blob/main/litellm/integrations/litedebugger.py)     | Code snippet in the parent repository's architecture provides various Jupyter notebooks showcasing different use cases and examples of the LiteLLM model. The notebooks cover topics such as benchmarking, evaluation, integration with other platforms, and parallel function calling.                                                                                                                                                                          |
| [dynamodb.py](https://github.com/BerriAI/litellm/blob/main/litellm/integrations/dynamodb.py)             | The code snippet is responsible for logging events to DynamoDB. It receives parameters and response data, constructs a payload, and stores it in the DynamoDB table. This enables event tracking and analysis.                                                                                                                                                                                                                                                   |
| [supabase.py](https://github.com/BerriAI/litellm/blob/main/litellm/integrations/supabase.py)             | The code snippet is responsible for logging events to Supabase, a database service. It includes functions to log input events and response events, storing relevant data such as model information, user messages, and status. The code uses the Supabase Python library and environment variables for configuration.                                                                                                                                            |
| [helicone.py](https://github.com/BerriAI/litellm/blob/main/litellm/integrations/helicone.py)             | The code snippet is a part of the litellm repository's architecture. It is responsible for logging events to Helicone on successful completion. The code uses the Helicone API key to send requests and log the data. The specific implementation includes creating the necessary request and response objects and making a POST request to the Helicone API endpoint.                                                                                           |
| [langfuse.py](https://github.com/BerriAI/litellm/blob/main/litellm/integrations/langfuse.py)             | The code snippet is part of the litellm repository and is located in the `litellm/integrations/langfuse.py` file. It provides a class called `LangFuseLogger` that is used to log events to the Langfuse service. The `log_event` method is responsible for logging events and accepts various parameters such as the input, output, start time, end time, and user ID. The class also handles compatibility between different versions of the Langfuse library. |
| [langsmith.py](https://github.com/BerriAI/litellm/blob/main/litellm/integrations/langsmith.py)           | This code snippet is a part of the litellm repository and is located in the `integrations/langsmith.py` file. It provides a class called `LangsmithLogger` that is responsible for logging events to Langsmith. It uses the Langsmith API to send logs with metadata, project name, and run name.                                                                                                                                                                |
| [traceloop.py](https://github.com/BerriAI/litellm/blob/main/litellm/integrations/traceloop.py)           | The code snippet includes a class called `TraceloopLogger` that is responsible for logging events using the Traceloop SDK. It initializes the Traceloop SDK, creates spans, and sets attributes for tracing and monitoring purposes.                                                                                                                                                                                                                             |
| [custom_logger.py](https://github.com/BerriAI/litellm/blob/main/litellm/integrations/custom_logger.py)   | The code snippet in the `custom_logger.py` file is responsible for logging events to Promptlayer during API calls in the Litellm repository. It provides various methods for logging pre and post API call events, stream events, success events, and failure events. It also includes hooks for modifying incoming and outgoing data before calling the model. The code ensures observability and facilitates customization of the logging process.             |
| [berrispend.py](https://github.com/BerriAI/litellm/blob/main/litellm/integrations/berrispend.py)         | The code snippet in `integrations/berrispend.py` is responsible for logging events to aispend.io on success and failure. It calculates the cost of model completion and sends the log data to the BerriSpend API.                                                                                                                                                                                                                                                |
| [weights_biases.py](https://github.com/BerriAI/litellm/blob/main/litellm/integrations/weights_biases.py) | The code snippet is responsible for logging events to Weights and Biases (W&B) during model inference. It utilizes the OpenAIResponse class to resolve request and response objects and generates a trace tree for logging. The log_event function takes in the necessary parameters and logs the event to W&B.                                                                                                                                                  |
| [prompt_layer.py](https://github.com/BerriAI/litellm/blob/main/litellm/integrations/prompt_layer.py)     | This code snippet is a logging utility that sends events to PromptLayer for successful API requests. It retrieves the necessary API key from environment variables, formats and sends the event data to the PromptLayer API endpoint. If successful, it logs the response and metadata if provided.                                                                                                                                                              |
| [llmonitor.py](https://github.com/BerriAI/litellm/blob/main/litellm/integrations/llmonitor.py)           | The code snippet is a part of the litellm repository's `integrations` directory. It is responsible for logging events to aispend.io for successful and failed requests, using the LLMonitorLogger class.                                                                                                                                                                                                                                                         |
| [aispend.py](https://github.com/BerriAI/litellm/blob/main/litellm/integrations/aispend.py)               | The code snippet is responsible for logging events to aispend.io. It calculates the cost of the model based on the usage and sends the log data to the AISpend API for further processing.                                                                                                                                                                                                                                                                       |

</details>

<details closed><summary>litellm.deprecated_litellm_server</summary>

| File                                                                                                                | Summary                                                                                                                                                                                                                                                                                                                                                        |
| ---                                                                                                                 | ---                                                                                                                                                                                                                                                                                                                                                            |
| [requirements.txt](https://github.com/BerriAI/litellm/blob/main/litellm/deprecated_litellm_server/requirements.txt) | This code snippet is part of a larger repository called litellm. It is responsible for implementing the OpenAI integration and utilizes dependencies such as FastAPI, Uvicorn, Boto3, litellm, python-dotenv, and Redis. The code is crucial for enabling communication with the OpenAI API and providing functionality related to the OpenAI language models. |
| [Dockerfile](https://github.com/BerriAI/litellm/blob/main/litellm/deprecated_litellm_server/Dockerfile)             | This code snippet is a Dockerfile for setting up the deprecated LiteLLM server. It installs the necessary dependencies and sets up the environment variables. The server exposes a specified port and runs the LiteLLM server using uvicorn.                                                                                                                   |
| [.env.template](https://github.com/BerriAI/litellm/blob/main/litellm/deprecated_litellm_server/.env.template)       | The code snippet contains a configuration file that sets up various API keys and authentication strategies for different LLM APIs. It also includes settings for logging and caching using Redis.                                                                                                                                                              |
| [server_utils.py](https://github.com/BerriAI/litellm/blob/main/litellm/deprecated_litellm_server/server_utils.py)   | This code snippet includes functions for managing environment variables, setting callbacks for logging and features, and loading a router configuration from a YAML file. It also includes a function for getting the version of a package.                                                                                                                    |
| [main.py](https://github.com/BerriAI/litellm/blob/main/litellm/deprecated_litellm_server/main.py)                   | The code snippet plays a critical role in the parent repository's architecture. It achieves specific functionalities related to the implementation of the repository. For more information about the repository structure, please refer to the provided directory structure.                                                                                   |

</details>

<details closed><summary>litellm.llms</summary>

| File                                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---                                                                                                        | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [maritalk.py](https://github.com/BerriAI/litellm/blob/main/litellm/llms/maritalk.py)                       | The code snippet is part of the Maritalk API interface and provides configuration options for the Maritalk model. It includes parameters such as the maximum number of tokens, model name, sampling option, temperature, top-p threshold, and stopping tokens. The code also includes functions for validating the API environment, making completion requests, and calculating usage. It utilizes the `litellm` library and handles logging and error handling. |
| [palm.py](https://github.com/BerriAI/litellm/blob/main/litellm/llms/palm.py)                               | The code snippet defines a configuration class `PalmConfig` and two functions `completion` and `embedding`. The `PalmConfig` class provides configuration parameters for the Palm's API interface. The `completion` function uses the Palm API to generate text completions based on given prompts and messages. The `embedding` function is a placeholder and does not contain any logic.                                                                       |
| [vllm.py](https://github.com/BerriAI/litellm/blob/main/litellm/llms/vllm.py)                               | The code snippet in the `llms/vllm.py` file is a part of the `litellm` codebase. It provides functions for text completion using the `VLLM` model. These functions handle completion requests, including batch completions, and provide options for custom prompts and logging.                                                                                                                                                                                  |
| [openrouter.py](https://github.com/BerriAI/litellm/blob/main/litellm/llms/openrouter.py)                   | The code snippet in `openrouter.py` defines the `OpenrouterConfig` class, which represents the configuration for the OpenRouter service. It allows the specification of transforms, models, and routes. The `get_config` method retrieves the configuration settings.                                                                                                                                                                                            |
| [azure.py](https://github.com/BerriAI/litellm/blob/main/litellm/llms/azure.py)                             | The code snippet in the `codellama-server` directory is a crucial component of the repository's architecture. It likely contains the server implementation for the LiteLLM system, handling requests and providing completion functionalities. Its role is to manage the interaction between clients and the underlying language model.                                                                                                                          |
| [replicate.py](https://github.com/BerriAI/litellm/blob/main/litellm/llms/replicate.py)                     | This code snippet, located in the `cookbook` directory, includes multiple Jupyter notebooks illustrating different use cases and examples of the LiteLLM software. It showcases the capabilities and features of the LiteLLM software through various scenarios.                                                                                                                                                                                                 |
| [petals.py](https://github.com/BerriAI/litellm/blob/main/litellm/llms/petals.py)                           | The code snippet provides functions for generating text completions and obtaining model embeddings using the Petals API. It includes a class for configuring the API and functions for handling the completion and embedding calls. The code also handles logging and error handling for the API calls.                                                                                                                                                          |
| [together_ai.py](https://github.com/BerriAI/litellm/blob/main/litellm/llms/together_ai.py)                 | Error generating summary: HTTPStatusError occurred. See logs for details.                                                                                                                                                                                                                                                                                                                                                                                        |
| [cloudflare.py](https://github.com/BerriAI/litellm/blob/main/litellm/llms/cloudflare.py)                   | The code snippet in `litellm/llms/cloudflare.py` provides functions for interacting with the Cloudflare API. It includes functions for performing text completions and calculating token usage. The code also includes error handling and logging functionality.                                                                                                                                                                                                 |
| [gemini.py](https://github.com/BerriAI/litellm/blob/main/litellm/llms/gemini.py)                           | The code snippet provides a function for generating completions using the Gemini language model. It handles the configuration, logging, and API calls necessary for generating responses. Additionally, it calculates usage statistics and returns the model response.                                                                                                                                                                                           |
| [aleph_alpha.py](https://github.com/BerriAI/litellm/blob/main/litellm/llms/aleph_alpha.py)                 | The code snippet contributes to the parent repository's architecture by providing a directory structure and various notebooks for benchmarking, evaluating, and demonstrating the capabilities of the LiteLLM model. It serves as a practical guide for using LiteLLM in different use cases.                                                                                                                                                                    |
| [ollama_chat.py](https://github.com/BerriAI/litellm/blob/main/litellm/llms/ollama_chat.py)                 | This code snippet is part of a larger repository with a specific directory structure and layout. It performs critical functions related to benchmarking and evaluating language models, as well as providing examples and use cases.                                                                                                                                                                                                                             |
| [oobabooga.py](https://github.com/BerriAI/litellm/blob/main/litellm/llms/oobabooga.py)                     | The code snippet is a module called oobabooga.py in the litellm/llms directory. It provides functions for text completion and text embedding using an external API. These functions handle API calls, data validation, and error handling. The module also includes logging and response processing functionalities.                                                                                                                                             |
| [openai.py](https://github.com/BerriAI/litellm/blob/main/litellm/llms/openai.py)                           | The code snippet in the `cookbook/codellama-server/main.py` file serves as the main entry point for the Codellama server within the parent repository. Its critical features include handling client requests, processing data, and coordinating communication between different components of the server architecture.                                                                                                                                          |
| [sagemaker.py](https://github.com/BerriAI/litellm/blob/main/litellm/llms/sagemaker.py)                     | The code snippet in this repository is a collection of Jupyter notebooks that demonstrate various use cases and examples of the LiteLLM software. It showcases the capabilities and features of LiteLLM in different scenarios, such as benchmarking, evaluating, and comparing language models. The notebooks also cover integration with Azure, OpenAI, HuggingFace, and other frameworks.                                                                     |
| [vertex_ai.py](https://github.com/BerriAI/litellm/blob/main/litellm/llms/vertex_ai.py)                     | This code snippet is part of the litellm repository and is located in the cookbook directory. It contains various Jupyter notebooks that showcase different use cases and examples of the LiteLLM language model. These notebooks demonstrate the capabilities and features of LiteLLM for tasks like benchmarking, completion cost evaluation, and integration with other frameworks.                                                                           |
| [baseten.py](https://github.com/BerriAI/litellm/blob/main/litellm/llms/baseten.py)                         | The code snippet is part of the larger litellm codebase, specifically the baseten.py file. It provides functions for making completion and embedding calls to the Baseten model. The completion function takes input messages, optional parameters, and an API key, and returns a model response. The embedding function is a placeholder for logic related to model embedding calls.                                                                            |
| [anthropic.py](https://github.com/BerriAI/litellm/blob/main/litellm/llms/anthropic.py)                     | The code snippet provides functions for interacting with the Anthropica language model. It includes functions for generating completions and embeddings. The code also handles API authentication and logging.                                                                                                                                                                                                                                                   |
| [ai21.py](https://github.com/BerriAI/litellm/blob/main/litellm/llms/ai21.py)                               | The code snippet provides a Python implementation of the AI21 API interface. It includes configuration options and functions for completing prompts and generating embeddings using the AI21 models. The code also includes error handling and logging functionality.                                                                                                                                                                                            |
| [huggingface_restapi.py](https://github.com/BerriAI/litellm/blob/main/litellm/llms/huggingface_restapi.py) | This code snippet is part of the `litellm` repository and is located in the `cookbook` directory. It includes various Jupyter notebooks and Python scripts for benchmarking, evaluation, and examples related to the LiteLLM project.                                                                                                                                                                                                                            |
| [cohere.py](https://github.com/BerriAI/litellm/blob/main/litellm/llms/cohere.py)                           | The code snippet in the `cookbook/` directory of the repository provides various Jupyter notebooks demonstrating the usage and capabilities of the LiteLLM model in different scenarios, such as benchmarking, evaluating, and integrating with other tools and platforms.                                                                                                                                                                                       |
| [ollama.py](https://github.com/BerriAI/litellm/blob/main/litellm/llms/ollama.py)                           | The code snippet in this repository serves as a tech lead and software engineer's contribution to the parent architecture. It achieves critical features related to benchmarking, evaluating, and utilizing LiteLLM language models for various use cases. The snippet contains notebooks demonstrating examples, comparisons, and integration with external platforms and frameworks.                                                                           |
| [base.py](https://github.com/BerriAI/litellm/blob/main/litellm/llms/base.py)                               | The code snippet is a base class for adding new Language Model (LLM) providers via API calls. It handles creating client sessions, validating the environment, and executing model completion and embedding calls.                                                                                                                                                                                                                                               |
| [bedrock.py](https://github.com/BerriAI/litellm/blob/main/litellm/llms/bedrock.py)                         | This code snippet is part of a larger repository with a specific directory structure. It contains various Jupyter Notebook files that demonstrate the usage and capabilities of the LiteLLM software. The code provides practical examples and tutorials for benchmarking and evaluating LiteLLM models, integrating with different platforms, and exploring different use cases.                                                                                |
| [nlp_cloud.py](https://github.com/BerriAI/litellm/blob/main/litellm/llms/nlp_cloud.py)                     | The code snippet in the file litellm/llms/nlp_cloud.py implements the NLPCloud API integration for the LLM models. It provides functions for text completion and embedding using the NLPCloud API. The code handles API authentication, request formatting, response handling, and logging.                                                                                                                                                                      |

</details>

<details closed><summary>litellm.llms.tokenizers</summary>

| File                                                                                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---                                                                                                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [anthropic_tokenizer.json](https://github.com/BerriAI/litellm/blob/main/litellm/llms/tokenizers/anthropic_tokenizer.json)                                 | Summary: This code snippet plays a critical role in the parent repository's architecture by defining the directory structure, workflow configurations, and environment variables. It ensures proper organization and enables efficient development and deployment processes. Supplementary details: The parent repository follows a well-defined directory structure, with subdirectories like `.circleci`, `.github`, and `.env.example`. These subdirectories contain essential files such as `config.yml` for CircleCI configuration, `FUNDING.yml` for funding information, and `issue_template` for bug reports and feature requests. The code snippet also includes workflow configurations for GitHub actions, facilitating automated processes. Additionally, it provides an example environment file (`env.example`), guiding developers to set up required environment variables. |
| [9b5ad71b2ce5302211f9c61530b329a4922fc6a4](https://github.com/BerriAI/litellm/blob/main/litellm/llms/tokenizers/9b5ad71b2ce5302211f9c61530b329a4922fc6a4) | This code snippet is part of a repository and plays a critical role in the architecture. It achieves specific objectives related to the CircleCI setup and requirements for the project.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

</details>

<details closed><summary>litellm.llms.huggingface_llms_metadata</summary>

| File                                                                                                                                               | Summary                                                                                                                                                                                                                                                                                                                        |
| ---                                                                                                                                                | ---                                                                                                                                                                                                                                                                                                                            |
| [hf_text_generation_models.txt](https://github.com/BerriAI/litellm/blob/main/litellm/llms/huggingface_llms_metadata/hf_text_generation_models.txt) | The code snippet is part of a larger repository with a well-organized structure. It includes configuration files, templates, and workflows for issue tracking and deployment. The code achieves a specific purpose within the repository's architecture, but further details are necessary to provide a more specific summary. |
| [hf_conversational_models.txt](https://github.com/BerriAI/litellm/blob/main/litellm/llms/huggingface_llms_metadata/hf_conversational_models.txt)   | The code snippet is a part of a larger repository with a specific directory structure. It is responsible for managing the Dockerfile and Dockerfile.alpine files, as well as providing a cookbook for benchmarking.                                                                                                            |

</details>

<details closed><summary>litellm.llms.prompt_templates</summary>

| File                                                                                                | Summary                                                                                                                                                                                                                     |
| ---                                                                                                 | ---                                                                                                                                                                                                                         |
| [factory.py](https://github.com/BerriAI/litellm/blob/main/litellm/llms/prompt_templates/factory.py) | This code snippet defines the directory structure and layout of the parent repository, including configuration files, workflows, Docker files, and Jupyter Notebook examples for various use cases of the LiteLLM software. |

</details>

<details closed><summary>litellm.llms.custom_httpx</summary>

| File                                                                                                          | Summary                                                                                                                                                                                                                                                                                                                                                                                                |
| ---                                                                                                           | ---                                                                                                                                                                                                                                                                                                                                                                                                    |
| [azure_dall_e_2.py](https://github.com/BerriAI/litellm/blob/main/litellm/llms/custom_httpx/azure_dall_e_2.py) | The code snippet contains two classes, `AsyncCustomHTTPTransport` and `CustomHTTPTransport`, which provide custom implementations of the `httpx.AsyncHTTPTransport` and `httpx.HTTPTransport` classes, respectively. These classes are used as workarounds to support the `dall-e-2` API on OpenAI. They handle async and sync requests, including polling for operation status and handling timeouts. |

</details>

<details closed><summary>litellm.router_strategy</summary>

| File                                                                                                        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---                                                                                                         | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [lowest_latency.py](https://github.com/BerriAI/litellm/blob/main/litellm/router_strategy/lowest_latency.py) | The code snippet is part of the litellm codebase and is located in the `litellm/router_strategy/lowest_latency.py` file. It implements a strategy for selecting a deployment with the lowest response time based on latency measurements. The code logs and updates latency usage on successful requests and provides a method to retrieve the deployment with the lowest latency from a list of healthy deployments.                                                                                                |
| [lowest_tpm_rpm.py](https://github.com/BerriAI/litellm/blob/main/litellm/router_strategy/lowest_tpm_rpm.py) | The code snippet is part of the litellm codebase and is located in the `litellm/router_strategy/lowest_tpm_rpm.py` file. It provides a strategy to identify the deployment with the lowest TPM (Transactions Per Minute) usage for a given model group. This strategy is used to distribute incoming requests to the least busy deployment.                                                                                                                                                                          |
| [least_busy.py](https://github.com/BerriAI/litellm/blob/main/litellm/router_strategy/least_busy.py)         | The code snippet is a logging handler that tracks the number of requests made to each model deployment, allowing the router to identify the least busy deployment. It logs the number of requests before and after each API call and decrements the count in cache for successful and failed requests. The `get_available_deployments` function uses the request count to select the least busy deployment for a given model group. The code provides support for both synchronous and asynchronous request logging. |

</details>

<details closed><summary>.circleci</summary>

| File                                                                                        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---                                                                                         | ---                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [requirements.txt](https://github.com/BerriAI/litellm/blob/main/.circleci/requirements.txt) | This code snippet is part of a larger repository that follows a structured directory layout. It contributes to the architecture by providing essential functionalities and dependencies such as OpenAI, Python dotenv, and Redis. These features enable critical features like AI modeling, tokenization, and database operations.                                                                                               |
| [config.yml](https://github.com/BerriAI/litellm/blob/main/.circleci/config.yml)             | The code snippet is part of the litellm repository, which has a complex directory structure. The snippet includes the configuration file for CircleCI, which defines two jobs: local_testing and publish_to_pypi. The local_testing job installs dependencies, runs tests, and performs linting. The publish_to_pypi job publishes the package to PyPI if there are changes to the litellm directory or the pyproject.toml file. |

</details>

---

##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* Python: `► INSERT-VERSION-HERE`
* `► ...`
* `► ...`

###  Installation

1. Clone the litellm repository:
```sh
git clone https://github.com/BerriAI/litellm
```

2. Change to the project directory:
```sh
cd litellm
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

###  Running litellm
Use the following command to run litellm:
```sh
python main.py
```

###  Tests
To execute tests, run:
```sh
pytest
```

---

##  Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/BerriAI/litellm/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/BerriAI/litellm/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/BerriAI/litellm/issues)**: Submit bugs found or log feature requests for litellm.

<details closed>
<summary>Contributing Guidelines</summary>

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

[**Return**](#-quick-links)

---
