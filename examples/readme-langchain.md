
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
lanarky
</h1>
<h3 align="center">📍 Empower your code with Lanarky: Unleash your creativity!</h3>
<h3 align="center">🚀 Developed with the software and tools below:</h3>

<p align="center">
<img src="https://img.shields.io/badge/tqdm-FFC107.svg?style=for-the-badge&logo=tqdm&logoColor=black" alt="tqdm" />
<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=for-the-badge&logo=HTML5&logoColor=white" alt="HTML5" />
<img src="https://img.shields.io/badge/Redis-DC382D.svg?style=for-the-badge&logo=Redis&logoColor=white" alt="Redis" />
<img src="https://img.shields.io/badge/Jinja-B41717.svg?style=for-the-badge&logo=Jinja&logoColor=white" alt="Jinja" />
<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white" alt="OpenAI" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=for-the-badge&logo=AIOHTTP&logoColor=white" alt="AIOHTTP" />

<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=for-the-badge&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions" />
<img src="https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="pandas" />
<img src="https://img.shields.io/badge/NumPy-013243.svg?style=for-the-badge&logo=NumPy&logoColor=white" alt="NumPy" />
<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=for-the-badge&logo=FastAPI&logoColor=white" alt="FastAPI" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="Markdown" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white" alt="JSON" />
</p>
</div>

---

## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍Overview](#-overview)
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

Lanarky is a tool for generating language models with FastAPI. It includes various dependencies such as OpenAI, Langchain, and Redis, and provides pre-commit hooks for code formatting and syntax checking. The project includes routers, callbacks, and responses for building API endpoints and handling user requests, as well as examples for creating chatbots and conversational AI systems. Lanarky enables developers to create scalable and efficient language models with ease, while providing robust error handling and testing capabilities.

---

## 🔮 Features

Feature | Description |
|---|---|
| **🏗 Overall Structure and Organization** | The codebase follows a clear structure and organization, with separate directories for modules, callbacks, routing, and responses. The use of a Makefile for running tests and pre-commit hooks adds to the overall organization and maintainability of the code. |
| **📝 Code Documentation** | The codebase includes documentation in the form of docstrings and comments, though some areas could benefit from more detailed explanations. There is also a README file that provides an overview of the codebase and its usage. |
| **🧩 Dependency Management** | The codebase uses Poetry for dependency management, with a pyproject.toml file specifying the required dependencies. The use of versioned dependencies and separate groups for development, documentation, and testing adds to the overall robustness of the codebase. |
| **♻️ Code Modularity and Reusability** | The codebase demonstrates good modularity, with separate modules for routing, callbacks, and responses that can be easily reused in other projects. The use of FastAPI and Pydantic also adds to the reusability of the code. |
| **✅ Testing and Quality Assurance** | The codebase includes comprehensive unit tests and a Continuous Integration workflow for ensuring code quality and preventing merge conflicts. The use of pre-commit hooks also helps ensure consistent code style and formatting. |
| **⚡️ Performance and Optimization** | The codebase includes various optimization techniques, such as caching and streaming, to improve performance and scalability. The use of Faiss-CPU for similarity search also adds to the overall speed of the code. |
| **🔒 Security Measures** | The codebase includes a sample.env file for setting environment variables, which can help prevent sensitive information from being exposed. The use of authenticated APIs and user authentication would further improve security. |
| **🔄 Version Control and Collaboration** | The codebase is hosted on GitHub and includes a clear version control history with pull requests and issues. The use of GitHub Actions for automating workflows and publishing packages also adds to the overall collaboration and teamwork of the project. |
| **🔌 External Integrations** | The codebase includes several external dependencies and integrations, such as OpenAI, TikToken, and Gradio, which add to the overall functionality and capabilities of the code. |
| **📈 Scalability and Extensibility** | The use of FastAPI and Pydantic, as well as caching and streaming techniques, contribute to the overall scalability and extensibility of the codebase. The modular design also allows for easy addition of new functionality and integration with other tools and APIs. |

---


<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## ⚙️ Project Structure


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
│   ├── schemas.py
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
    └── test_schemas.py

21 directories, 68 files
```

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 💻 Modules

<details closed><summary>App</summary>

| File                        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Module                                   |
|:----------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------|
| retrieval_qa_w_sources.py   | The provided code snippet imports several modules and defines functions to create a RetrievalQAWithSourcesChain model for chatbot functionality using OpenAI embeddings and a FAISS vector store. It also sets up a FastAPI server and mounts a Gradio app for API requests to the chatbot model via a LangchainRouter, with endpoints for HTTP requests and WebSockets.                                                                                                                                                          | examples/app/retrieval_qa_w_sources.py   |
| conversation_chain.py       | The provided code snippet imports necessary packages and defines functions to create a ConversationChain using ChatOpenAI and mount it onto a FastAPI app. It also includes routes for GET requests and LangchainRouter for handling language processing requests via API and WebSocket. The overall purpose of the code is to demonstrate the functionality of the ConversationChain package for conversational AI.                                                                                                              | examples/app/conversation_chain.py       |
| __init__.py                 | The code snippet defines a function called "reverse_words" that takes in a string and reverses the order of the words in the string while preserving the order of the characters in each word. It achieves this by splitting the string into a list of words, reversing the order of the list, and then joining the reversed list back into a string with the words in their new order.                                                                                                                                           | examples/app/__init__.py                 |
| zero_shot_agent.py          | The provided code snippet imports necessary modules and defines a FastAPI application with a Jinja2 template. It also creates a language AI chat agent with zero-shot capabilities, and sets up routes for handling chat requests and responses with the agent using LangchainRouter. Finally, the application includes the LangchainRouter and the agent is mounted using Gradio for testing.                                                                                                                                    | examples/app/zero_shot_agent.py          |
| conversational_retrieval.py | The provided code snippet implements a demo of ConversationalRetrievalChain, a conversational AI system that uses natural language processing to generate responses to user queries. It includes two endpoints for handling chat requests in both text and JSON formats, and uses FastAPI for web server functionality. The system relies on various dependencies imported from external packages such as LangChain and Gradio, and is designed to be scalable and efficient through the use of caching and streaming techniques. | examples/app/conversational_retrieval.py |

</details>

<details closed><summary>Callbacks</summary>

| File            | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Module                            |
|:----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------|
| retrieval_qa.py | The provided code snippet includes a set of callback functions that handle the end of the execution of various supported chains in a natural language processing application. These callbacks are responsible for constructing and sending messages that include source documents and their metadata to the appropriate destination (streaming client or websocket). The callbacks are implemented as classes and registered using the lanarky library.   | lanarky/callbacks/retrieval_qa.py |
| __init__.py     | The provided code snippet defines functions for getting callback handlers for different chain types. These functions utilize various callback registries and can return different types of callbacks depending on the chain type. If a requested chain type is not supported, an error message is raised. The code also imports various modules and classes needed for these functions.                                                                   | lanarky/callbacks/__init__.py     |
| llm.py          | The code provides callback handlers for LLMChain and ConversationChain, supporting both WebSocket and streaming JSON response. These handlers execute a function on_llm_new_token when a new token is received, constructing and sending a message accordingly. The code also imports necessary modules and defines a list of supported chains.                                                                                                           | lanarky/callbacks/llm.py          |
| agents.py       | The provided code snippet defines callback classes for handling streaming, websocket, and streaming JSON responses from an AgentExecutor. These callbacks inherit from base and LLM chain callbacks and include methods for checking if the final answer has been reached and constructing and sending the appropriate message based on the response type. The code also includes a base class for handling asynchronous callbacks for the AgentExecutor. | lanarky/callbacks/agents.py       |
| base.py         | The provided code snippet defines Async Callback handlers for FastAPI StreamingResponse, WebsocketConnection, and StreamingJSONResponse. These handlers construct Messages, WebsocketResponses, and JSON-encoded responses from strings and dictionaries. The code relies on imports from FastAPI, Pydantic, and Starlette.                                                                                                                               | lanarky/callbacks/base.py         |

</details>

<details closed><summary>Examples</summary>

| File            | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Module                   |
|:----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------|
| requirements.in | The provided code snippet includes the installation of several Python packages, including Lanarky for generating random text, Langchain for language modeling, OpenAI for natural language processing, TikToken for interacting with the TikTok API, Faiss-CPU for similarity search, Gradio for building web-based UIs, FastAPI for building APIs, and Uvicorn for running ASGI servers. These packages provide a range of functionalities for text and language-related tasks, as well as web development. | examples/requirements.in |

</details>

<details closed><summary>Lanarky</summary>

| File        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                              | Module              |
|:------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------|
| __init__.py | The code snippet imports the LangchainRouter class from the routing module and makes it available for use in the current module. The __all__ variable specifies that only the LangchainRouter class is intended for export when this module is imported elsewhere.                                                                                                                                                                   | lanarky/__init__.py |
| schemas.py  | The code snippet defines several Enum classes for Sender, Message, and MessageType, and two Pydantic models for Websocket and JSON responses. The WebsocketResponse model has attributes for sender, message, and message_type, while the StreamingJSONResponse model has a token attribute. Finally, the BaseRetrievalQAStreamingJSONResponse model is a subclass of StreamingJSONResponse and includes a list of source documents. | lanarky/schemas.py  |

</details>

<details closed><summary>Register</summary>

| File         | Summary                                                                                                                                                                                                                                                                                                                                         | Module                        |
|:-------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------|
| __init__.py  | This code snippet imports various callback functions from the "callbacks" module and makes them available for use in other parts of the code. The imported functions include those for streaming, streaming JSON, and websockets. The "__all__" list specifies which functions can be accessed through this module.                             | lanarky/register/__init__.py  |
| callbacks.py | The provided code snippet defines three dictionaries for storing callback functions for streaming, websocket, and streaming JSON. It also provides three decorator functions for registering callback functions to these dictionaries based on provided keys and additional arguments. The register function is imported from a base module.    | lanarky/register/callbacks.py |
| base.py      | The code provides a function called "register" that adds a class or function to a dictionary registry with required keyword arguments. The registry is a dictionary that maps a key to a tuple of the class/function and a list of required keyword arguments. The function also allows for overriding existing keys in the registry if needed. | lanarky/register/base.py      |

</details>

<details closed><summary>Responses</summary>

| File         | Summary                                                                                                                                                                                                                                                                                                                                                                         | Module                         |
|:-------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------|
| __init__.py  | The code snippet imports the StreamingResponse class from a module called "streaming" and makes it available for use by other modules. The "__all__" variable is used to specify which objects should be exported when the module is imported using the "from module import *" syntax.                                                                                          | lanarky/responses/__init__.py  |
| streaming.py | The provided code snippet contains a decorator that sets up an openai.aiosession for StreamingResponse, a subclass of _StreamingResponse. It also defines a method for creating a chain executor and a StreamingResponse from a given Chain object, inputs, and callback arguments. The StreamingResponse class overrides the __call__ method to handle the streaming response. | lanarky/responses/streaming.py |

</details>

<details closed><summary>Root</summary>

| File                    | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Module                  |
|:------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------|
| .env.sample             | This code snippet is setting a variable OPENAI_API_KEY to a value that is expected to be added by the user. The purpose of this variable is not explicitly stated, but it is likely used to authenticate the user's access to the OpenAI API.                                                                                                                                                                                                                                                        | .env.sample             |
| .pre-commit-config.yaml | This code snippet specifies a set of pre-commit hooks to be applied to code repositories. These hooks perform various checks and fixes on the code, including detecting merge conflicts, checking JSON and YAML syntax, fixing line endings and whitespace, and formatting code with black and prettier. The snippet also specifies the versions of Python and the repositories to be used for the hooks.                                                                                            | .pre-commit-config.yaml |
| Makefile                | This code provides a Makefile with several targets to run tests, generate coverage reports, build and clean documentation, and run pre-commit hooks. The "help" target displays a message with the available targets and their descriptions. The "tests" target runs unit tests with coverage, while the "coverage" target generates a coverage report. The "pre-commit" target runs pre-commit hooks, and the "build-docs" and "clean-docs" targets respectively build and clean the documentation. | Makefile                |
| pyproject.toml          | The provided code snippet is a configuration file for the Lanarky tool, which is used to facilitate the production of LLM projects with FastAPI. The configuration file contains dependencies for the tool, including FastAPI, langchain, and various optional packages such as Redis and OpenAI. The file also includes groups of dependencies for development, documentation, and testing.                                                                                                         | pyproject.toml          |
| .coveragerc             | The provided code snippet includes a configuration option for omitting specific directories during testing. The "omit" option is set to exclude any files located in the "lanarky/testing" directory. This functionality is useful for streamlining testing and avoiding unnecessary overhead.                                                                                                                                                                                                       | .coveragerc             |
| .readthedocs.yaml       | This code snippet is a configuration file for Read the Docs, a documentation hosting platform. It specifies the version of Python and other tools needed for building documentation, as well as the operating system to be used. It also declares the requirements for building the documentation and the method for installing them. Finally, it specifies the location of the Sphinx configuration file for building documentation in the docs/ directory.                                         | .readthedocs.yaml       |

</details>

<details closed><summary>Routing</summary>

| File         | Summary                                                                                                                                                                                                                                                                                                                                                                | Module                       |
|:-------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------|
| __init__.py  | The code imports two modules, LangchainRouter and utils, and makes three of their functions available to other modules through the __all__ list: LangchainRouter, StreamingMode, and LLMCacheMode.                                                                                                                                                                     | lanarky/routing/__init__.py  |
| utils.py     | This code snippet provides functions to create endpoints for a language model API using FastAPI. It includes functions to create dependencies, request and response models, and different types of endpoints (base, streaming, and websocket) based on the specified streaming mode. It also imports necessary modules such as enum, functools, pydantic, and lanarky. | lanarky/routing/utils.py     |
| langchain.py | The provided code defines a router for a FastAPI web application that interfaces with a language model chain. It includes methods for setting up the router, adding language chain routes, and adding language chain websocket routes. The router can be configured with options such as the language chain URL, object, and caching mode.                             | lanarky/routing/langchain.py |

</details>

<details closed><summary>Templates</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                | Module                        |
|:-----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------|
| index.html | The code snippet includes HTML, CSS, and JavaScript for a chatbot playground web application. It creates a chat interface where users can send messages to a server via WebSocket and receive responses from a chatbot. The application handles different message types and displays them accordingly. | examples/templates/index.html |

</details>

<details closed><summary>Vector_stores</summary>

| File                   | Summary                                                                                                                                                                                                  | Module                                        |
|:-----------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------|
| langchain-python.faiss | The code snippet provided cannot be decoded due to the content being either non-text or not in UTF-8 format. Without further context, it is not possible to determine the source or purpose of the code. | examples/vector_stores/langchain-python.faiss |

</details>

<details closed><summary>Websockets</summary>

| File        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                     | Module                         |
|:------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------|
| __init__.py | The provided code snippet imports the WebsocketConnection class from a module called "base" and makes it available for use in other parts of the code. The "__all__" variable specifies which objects should be exported when using the "from.base import *" syntax.                                                                                                                                                        | lanarky/websockets/__init__.py |
| base.py     | The provided code snippet defines a FastAPI WebSocket server that accepts user messages and sends them to a language processing Chain. The server then responds with the processed message and logs any errors that occur. The code includes a BaseWebsocketConnection class and a WebsocketConnection subclass that wrap a language processing Chain and provide a chain_executor function for handling incoming messages. | lanarky/websockets/base.py     |

</details>

<details closed><summary>Workflows</summary>

| File            | Summary                                                                                                                                                                                                                                                                                                                                                                                                             | Module                            |
|:----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------|
| ci.yaml         | This code snippet defines a Continuous Integration workflow that runs on push and pull request events for the main branch. It sets up a Python environment, installs dependencies using Poetry, runs unit tests, and uploads coverage to Coveralls. The workflow runs on Ubuntu-Latest and uses GitHub Actions to automate the process.                                                                             | .github/workflows/ci.yaml         |
| publish.yaml    | The provided code snippet is a GitHub Actions workflow that automates the process of building and publishing a Python package to PyPI. It uses Poetry to manage dependencies and package configuration, and sets up a Python environment with version 3.9. The workflow is triggered by either a manual request or a push to a git tag, and includes concurrency handling and token authentication for PyPI.        | .github/workflows/publish.yaml    |
| code-check.yaml | The code snippet is a GitHub Actions workflow that checks the code in a pull request against pre-commit hooks. It runs on push to the main branch and various pull request events, and uses Python version 3.9. It checks out the code, sets up Python, downloads pre-commit, and runs all pre-commit hooks, displaying diffs on failure. The workflow can be cancelled if another instance is already in progress. | .github/workflows/code-check.yaml |

</details>

<hr />

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> `[📌  INSERT-PROJECT-PREREQUISITES]`

### 💻 Installation

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
# [INSERT-COMMAND-FOR-TESTS]
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

