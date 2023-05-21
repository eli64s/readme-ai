
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
lanarky
</h1>
<h3 align="center">📍 Lanarky: Unleashing Possibilities Through Technology!</h3>
<h3 align="center">🚀 Developed with the software and tools below.</h3>
<p align="center">

<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white" alt="charset-normalizer" />
<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=for-the-badge&logo=HTML5&logoColor=white" alt="filelock" />
<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=for-the-badge&logo=FastAPI&logoColor=white" alt="jsonschema" />
<img src="https://img.shields.io/badge/NumPy-013243.svg?style=for-the-badge&logo=NumPy&logoColor=white" alt="" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="aiosignal" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="txt" />

<img src="https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white" alt="zipp" />
<img src="https://img.shields.io/badge/Jinja-B41717.svg?style=for-the-badge&logo=Jinja&logoColor=white" alt="fonttools" />
<img src="https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="numexpr" />
<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=for-the-badge&logo=AIOHTTP&logoColor=white" alt="restructuredtext" />
<img src="https://img.shields.io/badge/tqdm-FFC107.svg?style=for-the-badge&logo=tqdm&logoColor=black" alt="md" />
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

Lanarky is a GitHub project designed to provide users with an organizational structure for their code repository. It provides additional features such as grouping multiple repositories in a single namespace, various alert options and more. Lanarky helps developers keep their code organized, while also giving them greater visibility and control over their repositories.

## 🔮 Feautres

> `[📌  INSERT-PROJECT-FEATURES]`

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
│   ├── advanced
│   │   └── custom_callbacks.rst
│   ├── conf.py
│   ├── features.rst
│   ├── getting_started.rst
│   ├── index.rst
│   ├── lanarky
│   │   ├── lanarky.callbacks.rst
│   │   ├── lanarky.register.rst
│   │   ├── lanarky.responses.rst
│   │   ├── lanarky.rst
│   │   ├── lanarky.schemas.rst
│   │   ├── lanarky.testing.rst
│   │   └── lanarky.websockets.rst
│   └── requirements.txt
├── examples
│   ├── README.md
│   ├── app
│   │   ├── __init__.py
│   │   ├── conversation_chain.py
│   │   ├── conversational_retrieval.py
│   │   └── retrieval_qa_w_sources.py
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
│   │   ├── base.py
│   │   ├── llm.py
│   │   ├── qa_with_sources.py
│   │   └── retrieval_qa.py
│   ├── register.py
│   ├── responses
│   │   ├── __init__.py
│   │   └── streaming.py
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
    │   ├── test_base.py
    │   ├── test_init.py
    │   ├── test_llm.py
    │   └── test_retrieval_qa.py
    ├── conftest.py
    ├── responses
    │   └── test_streaming.py
    ├── test_register.py
    └── test_schemas.py

18 directories, 56 files
```

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 💻 Modules

<details closed><summary>App</summary>

| File                        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                     | Module                                   |
|:----------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------|
| retrieval_qa_w_sources.py   | This code mounts a FastAPI app with a web UI and websocket endpoint that allows users to interact with a RetrievalQAWithSourcesChain model. The app loads a pre-trained model from a local vector store and allows users to query it for answers and related source documents.                                                                                                                                                              | examples/app/retrieval_qa_w_sources.py   |
| conversation_chain.py       | This code creates a FastAPI application with an endpoint for querying a ConversationChain, a websocket endpoint, and a template for the home page. The ConversationChain is created with a ChatOpenAI model and verbose set to True. The chat endpoint returns a StreamingResponse with the query and media type set to "text/event-stream". The websocket endpoint creates a WebsocketConnection from the ConversationChain and websocket. | examples/app/conversation_chain.py       |
| conversational_retrieval.py | This code is for a FastAPI application that uses a ConversationalRetrievalChain to generate responses to user queries. It uses a Jinja2Templates directory to provide templates, a QueryRequest class to define the query and history, and a lru_cache to store the ConversationalRetrievalChain. It also uses langchain and lanarky modules to provide responses and mount a gradio app.                                                   | examples/app/conversational_retrieval.py |

</details>

<details closed><summary>Callbacks</summary>

| File               | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Module                               |
|:-------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------|
| retrieval_qa.py    | This code defines classes for streaming and websocket callbacks for RetrievalQA and VectorDBQA, which extend from AsyncLLMChainStreamingCallback and AsyncLLMChainWebsocketCallback. It also defines a source document template for formatting the output of the callbacks. Finally, it registers the callbacks with the register_streaming_callback and register_websocket_callback functions.                                                                                | lanarky/callbacks/retrieval_qa.py    |
| qa_with_sources.py | This code registers streaming and websocket callbacks for BaseQAWithSources, QAWithSourcesChain, VectorDBQAWithSourcesChain, RetrievalQAWithSourcesChain, and ConversationalRetrievalChain.                                                                                                                                                                                                                                                                                    | lanarky/callbacks/qa_with_sources.py |
| llm.py             | This code registers two streaming and two websocket callbacks for LLMChain and ConversationChain, each with a unique on_llm_new_token method. The callbacks are based on AsyncStreamingResponseCallback and AsyncWebsocketCallback, respectively.                                                                                                                                                                                                                              | lanarky/callbacks/llm.py             |
| base.py            | This code implements two classes, AsyncStreamingResponseCallback and AsyncWebsocketCallback, which extend the abstract class AsyncLanarkyCallback. AsyncLanarkyCallback provides an abstract method for constructing a message from a string, and a property for always calling verbose callbacks. AsyncStreamingResponseCallback and AsyncWebsocketCallback both implement this abstract method, constructing a Message and a WebsocketResponse, respectively, from a string. | lanarky/callbacks/base.py            |

</details>

<details closed><summary>Lanarky</summary>

| File        | Summary                                                                                                                                                                                                                                                                                                                                                | Module              |
|:------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------|
| register.py | This code provides two functions, register_streaming_callback and register_websocket_callback, which allow classes to be registered in dictionaries(STREAMING_CALLBACKS and WEBSOCKET_CALLBACKS) with a key and, optionally, a list of required keyword arguments. It also provides a register function which adds the class/function to the registry. | lanarky/register.py |
| schemas.py  | This code defines a class, WebsocketResponse, that contains three fields: sender, message, and message_type. The sender and message_type fields are Enums, while the message field is either a Message Enum or a string. This class can be used to create a response object for a websocket connection.                                                | lanarky/schemas.py  |

</details>

<details closed><summary>Responses</summary>

| File         | Summary                                                                                                                                                                            | Module                         |
|:-------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------|
| streaming.py | This code creates a StreamingResponse class wrapper for langchain chains, which allows a chain to be executed with inputs and callbacks, and the resulting outputs to be streamed. | lanarky/responses/streaming.py |

</details>

<details closed><summary>Templates</summary>

| File       | Summary                                                                                                                                                                                                                                                                       | Module                        |
|:-----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------|
| index.html | This code creates a web page that allows users to communicate with a chatbot. It includes styling elements such as background colors, padding, and border radius, as well as a script that allows for the sending and receiving of messages between the user and the chatbot. | examples/templates/index.html |

</details>

<details closed><summary>Vector_stores</summary>

| File                   | Summary                                                                                                                             | Module                                        |
|:-----------------------|:------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------|
| langchain-python.faiss | This code indicates that an error has occurred when attempting to decode a file that is not a text file or is not encoded in UTF-8. | examples/vector_stores/langchain-python.faiss |

</details>

<details closed><summary>Websockets</summary>

| File    | Summary                                                                                                                                                                                                                                                  | Module                     |
|:--------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------|
| base.py | This code provides a class for connecting to a websocket and running a chain executor in response to user messages. The class provides methods for creating a chain executor and connecting to a websocket, as well as a wrapper for LLMChain instances. | lanarky/websockets/base.py |

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
