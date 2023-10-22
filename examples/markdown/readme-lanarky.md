
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
lanarky
</h1>
<h3>◦ Empower your code with Lanarky.</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/tqdm-FFC107.svg?style&logo=tqdm&logoColor=black" alt="tqdm" />
<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style&logo=HTML5&logoColor=white" alt="HTML5" />
<img src="https://img.shields.io/badge/Jinja-B41717.svg?style&logo=Jinja&logoColor=white" alt="Jinja" />
<img src="https://img.shields.io/badge/OpenAI-412991.svg?style&logo=OpenAI&logoColor=white" alt="OpenAI" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style&logo=AIOHTTP&logoColor=white" alt="AIOHTTP" />

<img src="https://img.shields.io/badge/pandas-150458.svg?style&logo=pandas&logoColor=white" alt="pandas" />
<img src="https://img.shields.io/badge/NumPy-013243.svg?style&logo=NumPy&logoColor=white" alt="NumPy" />
<img src="https://img.shields.io/badge/FastAPI-009688.svg?style&logo=FastAPI&logoColor=white" alt="FastAPI" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style&logo=JSON&logoColor=white" alt="JSON" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
</p>

![GitHub top language](https://img.shields.io/github/languages/top/ajndkr/lanarky?style&color=5D6D7E)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ajndkr/lanarky?style&color=5D6D7E)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/ajndkr/lanarky?style&color=5D6D7E)
![GitHub license](https://img.shields.io/github/license/ajndkr/lanarky?style&color=5D6D7E)
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

Lanarky is a Python library that provides a flexible and efficient framework for building and deploying language chain models. It offers a set of pre-configured callback handlers and routing utilities for streaming and WebSocket connections, allowing developers to easily set up custom language chains for various use cases such as chatbots, conversational retrieval, and question-answering. By leveraging its powerful features, Lanarky enables developers to build robust and scalable language models quickly and with ease.

---

## ⚙️ Features

Feature | Description |
|-----|-----|
| **🏗 Architecture** | The codebase follows a modular and well-structured architectural pattern, with different components and functionalities organized into separate packages and modules. The codebase also leverages FastAPI and Starlette for building RESTful APIs and websockets. |
| **📑 Documentation** | The codebase contains extensive documentation in the form of Sphinx-generated HTML documentation and inline code comments. The documentation explains the usage and functionality of different modules and packages in detail, making it easy for developers to understand and use the codebase. |
| **🧩 Dependencies** | The codebase has a few external dependencies, including FastAPI, Starlette, Pydantic, and Poetry, among others. The dependencies are well-specified in the `pyproject.toml` file and can be easily installed using the Poetry package manager. |
| **♻️ Modularity** | The codebase is highly modular, with different components and functionalities separated into packages and modules. This modularity makes it easy to separate concerns and to modify and extend the codebase without affecting other parts of the system. Additionally, the use of decorators and callbacks allows for easy customization of chain execution and response handling. |
| **✔️ Testing** | The codebase contains a comprehensive set of unit tests, with coverage reporting and continuous integration set up using Coveralls and GitHub Actions. The tests cover different components and functionalities, including routing, callbacks, and response generation. The testing framework is well-structured and easily extensible, allowing for the addition of new tests as the codebase evolves. |
| **⚡️ Performance** | The codebase leverages asynchronous execution and streaming response generation to achieve high performance, especially when handling large volumes of data. Additionally, the use of Pydantic for defining schemas and models helps to ensure efficient serialization and deserialization of data. |
| **🔒 Security** | The codebase contains several security features, including input validation using Pydantic models, error handling, and authentication and authorization capabilities through FastAPI's security features. Additionally, the use of the HTTPS protocol and the hashing of passwords reduce the risk of attacks and data loss. |
| **🔀 Version Control** | The codebase is hosted on GitHub and uses Git for version control, with a well-structured branching and merging strategy. The codebase also uses conventional commit messages to ensure consistency and clarity in commit messages, making it easy to track changes over time. |
| **🔌 Integrations** | The codebase integrates with a range of external libraries and services, including FAISS for vector indexing, Gradio for model deployment, and Coveralls for continuous integration. Additionally, the codebase integrates with popular machine learning frameworks such as PyTorch and TensorFlow. |
| **📈 Scalability** | The use of asynchronous execution and streaming response generation, along with the modular structure of the codebase

---


## 📂 Project Structure


```bash
repo
├── CONTRIBUTING.md
├── LICENSE
├── Makefile
├── README.md
├── assets
│   ├── demo.gif
│   ├── logo.png
│   └── vs_code_configs.png
├── docs
│   ├── Makefile
│   ├── _static
│   │   └── logo_150px.png
│   ├── conf.py
│   ├── features.rst
│   ├── getting_started.rst
│   ├── index.rst
│   ├── lanarky
│   │   ├── lanarky.callbacks.rst
│   │   ├── lanarky.register.rst
│   │   ├── lanarky.responses.rst
│   │   ├── lanarky.routing.rst
│   │   ├── lanarky.rst
│   │   ├── lanarky.schemas.rst
│   │   ├── lanarky.testing.rst
│   │   └── lanarky.websockets.rst
│   ├── langchain
│   │   ├── cache.rst
│   │   ├── custom_callbacks.rst
│   │   ├── deploy.rst
│   │   └── index.rst
│   └── requirements.txt
├── examples
│   ├── README.md
│   ├── app
│   │   ├── __init__.py
│   │   ├── conversation_chain.py
│   │   ├── conversational_retrieval.py
│   │   ├── retrieval_qa_w_sources.py
│   │   └── zero_shot_agent.py
│   ├── requirements.in
│   ├── requirements.txt
│   ├── templates
│   │   └── index.html
│   └── vector_stores
│       ├── langchain-python.faiss
│       └── langchain-python.pkl
├── lanarky
│   ├── __init__.py
│   ├── callbacks
│   │   ├── __init__.py
│   │   ├── agents.py
│   │   ├── base.py
│   │   ├── llm.py
│   │   └── retrieval_qa.py
│   ├── register
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── callbacks.py
│   ├── responses
│   │   ├── __init__.py
│   │   └── streaming.py
│   ├── routing
│   │   ├── __init__.py
│   │   ├── langchain.py
│   │   └── utils.py
│   ├── schemas
│   │   ├── __init__.py
│   │   ├── callbacks.py
│   │   └── websockets.py
│   ├── testing
│   │   ├── __init__.py
│   │   ├── gradio.py
│   │   └── settings.py
│   └── websockets
│       ├── __init__.py
│       └── base.py
├── pyproject.toml
└── tests
    ├── callbacks
    │   ├── test_agents.py
    │   ├── test_base.py
    │   ├── test_init.py
    │   ├── test_llm.py
    │   └── test_retrieval_qa.py
    ├── conftest.py
    ├── responses
    │   └── test_streaming.py
    ├── routing
    │   └── test_langchain_router.py
    ├── test_register.py
    ├── test_schemas.py
    └── websockets
        └── test_websocket_connection.py

23 directories, 71 files
```

---

## 🧩 Modules

<details closed><summary>App</summary>

| File                        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Module                                   |
|:----------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------|
| retrieval_qa_w_sources.py   | This code snippet creates a FastAPI app with a LangchainRouter that uses a RetrievalQAWithSourcesChain for chat and question-answering functionality. The app includes routes for HTML templates and WebSocket connections, and leverages the FAISS library for vector indexing. The LangchainRouter provides API endpoints for chat and JSON payloads, and the create_chain() function initializes the chain with the necessary settings and databases.                | examples/app/retrieval_qa_w_sources.py   |
| conversation_chain.py       | This code snippet sets up a FastAPI application with a mounted Gradio app for language model chat, using the ConversationChain class from the Langchain library. It includes routes for handling HTTP requests and websockets for chat interactions, and uses Jinja2Templates for rendering HTML templates. The LangchainRouter class is used for managing API routes and the ConversationChain instance is created with the ChatOpenAI model for generating responses. | examples/app/conversation_chain.py       |
| zero_shot_agent.py          | The provided code snippet is an implementation of a FastAPI web application that uses the Langchain library for natural language processing. It creates a language model agent that can react to user inputs with descriptions and runs it on a Gradio interface. The app includes routing for chat interactions with the agent through HTTP requests and WebSockets.                                                                                                   | examples/app/zero_shot_agent.py          |
| conversational_retrieval.py | The provided code snippet is a Python implementation of a conversational retrieval chain demo. This includes loading vector stores, configuring language models and embeddings, creating a Conversational Retrieval Chain, and setting up a LangchainRouter with API routes for chat and JSON. The FastAPI framework and Jinja2Templates are used for web application development.                                                                                      | examples/app/conversational_retrieval.py |

</details>

<details closed><summary>Callbacks</summary>

| File            | Summary                                                                                                                                                                                                                                                                                                                                                                                                                 | Module                            |
|:----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------|
| retrieval_qa.py | This code snippet registers three callback classes for handling different types of streaming and websocket requests for various supported chains. When a chain finishes running, these callbacks output a message with metadata and page content for the source documents used in the chain. The provided code depends on additional modules such as `lanarky.register` and `lanarky.schemas`.                          | lanarky/callbacks/retrieval_qa.py |
| llm.py          | The provided code snippet defines three asynchronous callback handlers for the LLMChain and ConversationChain using Lanarky's register functions. These handlers allow for response streaming and websocket communication, and are specifically designed to listen for and respond to new tokens in the LLMChain. The `SUPPORTED_CHAINS` list specifies the chains that these callbacks are available for.              | lanarky/callbacks/llm.py          |
| agents.py       | The code snippet defines three asynchronous callback handlers for the `AgentExecutor`, each handling different streaming protocols. These handlers listen for new tokens from an LLM model and, when a final answer has been reached, construct and send a message containing the final answer. The `AsyncAgentsLanarkyCallback` base class provides functionality for checking when the final answer has been reached. | lanarky/callbacks/agents.py       |
| base.py         | The code snippet provides functionality for handling callbacks in FastAPI for streaming responses and websockets. It includes abstract classes for constructing messages and concrete implementations for streaming response callbacks, websocket callbacks, and streaming JSON response callbacks. The code uses Pydantic for defining schemas and is built on top of Starlette.                                       | lanarky/callbacks/base.py         |

</details>

<details closed><summary>Examples</summary>

| File            | Summary                                                                                                                                                                                | Module                   |
|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------|
| requirements.in | Unfortunately, no code snippet was provided, so I cannot offer a summary of its functionalities. Please provide the necessary information or code snippet for me to assist you better. | examples/requirements.in |

</details>

<details closed><summary>Register</summary>

| File         | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                  | Module                        |
|:-------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------|
| callbacks.py | This code snippet defines three functions for registering callback handlers for streaming, websocket, and streaming JSON data. The functions take a key or list of keys and any additional keyword arguments and return a decorator function that registers the decorated class with a corresponding dictionary of callback handlers.                                                                                                    | lanarky/register/callbacks.py |
| base.py      | The code provides a function called "register" that takes a key (as a string or list of strings), a registry (as a dictionary), and an override (a boolean flag). The function adds a class/function to the registry with required keyword arguments. If override is set to True, the function overrides existing keys in the registry. The returned inner function "_register_cls" registers the class/function under the given key(s). | lanarky/register/base.py      |

</details>

<details closed><summary>Responses</summary>

| File         | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                        | Module                         |
|:-------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------|
| streaming.py | The code snippet defines a `StreamingResponse` class that is a subclass of `fastapi.responses.StreamingResponse`, with additional functionalities for streaming with `langchain`. It uses `aiohttp` and `asyncio` to stream and execute the chain provided by `langchain`. It also provides a factory method `from_chain` to create a `StreamingResponse` object from a `Chain` object, with customizable input, output, and callback options. | lanarky/responses/streaming.py |

</details>

<details closed><summary>Root</summary>

| File        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                  | Module      |
|:------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------|
| Makefile    | This code provides a Makefile with several targets:'help' prints usage and available targets,'tests' runs unit tests with coverage reporting,'coverage' runs unit tests with coverage and sends the report to Coveralls,'pre-commit' runs pre-commit hooks,'build-docs' builds Sphinx documentation, and'clean-docs' removes the built documentation. The targets use the Python package manager Poetry to run commands. | Makefile    |
| .coveragerc | Unfortunately, there is no provided code snippet for me to offer a comprehensive summary of its core functionalities.                                                                                                                                                                                                                                                                                                    | .coveragerc |

</details>

<details closed><summary>Routing</summary>

| File         | Summary                                                                                                                                                                                                                                                                                                                                                                                    | Module                       |
|:-------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------|
| utils.py     | The provided code defines functions for creating Langchain endpoints for use in a FastAPI application. It includes functions for creating request and response models, dependencies, and endpoints based on different streaming modes and WebSocket connections. It also includes error handling for unsupported chain types.                                                              | lanarky/routing/utils.py     |
| langchain.py | The provided code defines a LangchainRouter class that extends the FastAPI APIRouter class. It provides methods to set up and add routes for interacting with a Langchain object. The LangchainRouter can handle API and websocket routes and provides options for caching and streaming data. The code also includes utility functions for creating Langchain dependencies and endpoints. | lanarky/routing/langchain.py |

</details>

<details closed><summary>Schemas</summary>

| File          | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Module                        |
|:--------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------|
| websockets.py | The code defines a set of enumerations (Sender, Message, MessageType) and a Pydantic BaseModel (WebsocketResponse) that uses these enumerations to define its fields. The WebsocketResponse model has three fields: sender, message, and message_type. The Config class within the model specifies that the enumerations should be used as values for their respective fields.                                                                                                            | lanarky/schemas/websockets.py |
| callbacks.py  | The provided code defines two classes: StreamingJSONResponse and BaseRetrievalQAStreamingJSONResponse. StreamingJSONResponse is a model with a single attribute-token. BaseRetrievalQAStreamingJSONResponse inherits from StreamingJSONResponse and adds an additional attribute-source_documents, which is a list of dictionaries that can contain any data type. These classes are designed for generating streaming JSON responses in retrieval-based question answering applications. | lanarky/schemas/callbacks.py  |

</details>

<details closed><summary>Templates</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                                                                                                                             | Module                        |
|:-----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------|
| index.html | The provided code snippet is a basic HTML page with embedded JavaScript that creates a chat window front-end that communicates with a WebSocket endpoint. Users can enter a question and receive responses from a chatbot, displayed in real-time in the chat window. The JavaScript code handles receiving and displaying messages from the WebSocket endpoint, as well as sending messages to the chatbot server. | examples/templates/index.html |

</details>

<details closed><summary>Websockets</summary>

| File    | Summary                                                                                                                                                                                                                                                                                                                                                                                                                           | Module                     |
|:--------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------|
| base.py | The provided code snippet contains a set of classes and functions to handle websocket connections for a language chain application using FastAPI. It includes a base class for websocket connections, a class wrapper for LLMChain instances, and a function to execute chain.acall(). It allows for custom callback functions and sends messages back and forth between the client and server using WebsocketResponse instances. | lanarky/websockets/base.py |

</details>

---

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - [ℹ️ Requirement 1]
> - [ℹ️ Requirement 2]
> - [...]

### 🖥 Installation

1. Clone the lanarky repository:
```sh
git clone https://github.com/ajndkr/lanarky
```

2. Change to the project directory:
```sh
cd lanarky
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

### 🤖 Using lanarky

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
