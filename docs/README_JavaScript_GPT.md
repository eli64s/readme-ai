
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
assistant-chat-gpt
</h1>
<h3 align="center">📍 Chat smarter, not harder with Assistant-Chat-GPT on GitHub!</h3>
<h3 align="center">🚀 Developed with the software and tools below:</h3>

<p align="center">
<img src="https://img.shields.io/badge/esbuild-FFCF00.svg?style=for-the-badge&logo=esbuild&logoColor=black" alt="esbuild" />
<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=for-the-badge&logo=JavaScript&logoColor=black" alt="JavaScript" />
<img src="https://img.shields.io/badge/Prettier-F7B93E.svg?style=for-the-badge&logo=Prettier&logoColor=black" alt="Prettier" />
<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=for-the-badge&logo=HTML5&logoColor=white" alt="HTML5" />
<img src="https://img.shields.io/badge/React-61DAFB.svg?style=for-the-badge&logo=React&logoColor=black" alt="React" />

<img src="https://img.shields.io/badge/ESLint-4B32C3.svg?style=for-the-badge&logo=ESLint&logoColor=white" alt="ESLint" />
<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=for-the-badge&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white" alt="JSON" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="Markdown" />
</p>
</div>

---

## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍Overview](#overview)
- [🔮 Features](#-features)
- [⚙️ Project Structure](#️-project-structure)
- [💻 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
  - [✅ Prerequisites](#-prerequisites)
  - [💻 Installation](#-installation)
  - [🤖 Using assistant-chat-gpt](#-using-assistant-chat-gpt)
  - [🧪 Running Tests](#-running-tests)
- [🛠 Future Development](#-future-development)
- [🤝 Contributing](#-contributing)
- [🪪 License](#-license)
- [🙏 Acknowledgments](#-acknowledgments)

---


## 📍Overview

The assistant-chat-gpt project is a browser extension that allows users to interact with OpenAI's GPT chatbot through a voice assistant. It includes features such as obtaining voice input, processing user queries, generating spoken responses, and maintaining a conversation history. The project aims to provide a hands-free and natural way of communicating with the chatbot, improving accessibility and convenience for users. Its value proposition lies in its ability to seamlessly integrate with the user's browsing experience, enhancing productivity and efficiency.

---

## 🔮 Features

| Feature | Description |
| --- | --- |
| **🏗 Overall Structure and Organization** | The codebase is organized into separate directories for different parts of the application, such as background, content, and popup. The use of React and modular code promotes separation of concerns and maintainability. |
| **📝 Code Documentation** | The codebase has minimal documentation, with some files containing no comments or explanations. However, the use of descriptive variable and function names makes the code somewhat self-documenting. |
| **🧩 Dependency Management** | The codebase uses npm for package management and includes a package-lock.json file to ensure consistent dependencies. Dependencies are also listed in the manifest file for the browser extension. |
| **♻️ Code Modularity and Reusability** | The codebase is modular, with separate files for different components and functionalities. React components are designed for reusability, and some modules are imported and used in multiple files. |
| **✅ Testing and Quality Assurance** | The codebase does not include any automated tests or linting tools. However, the use of modern JavaScript features and libraries may help to mitigate some potential issues. |
| **⚡️ Performance and Optimization** | The use of esbuild and archiver libraries for building and packaging the browser extension helps to optimize file size and load times. The codebase also includes some optimizations for text-to-speech processing. |
| **🔒 Security Measures** | The codebase does not include any significant security measures beyond the standard browser extension permissions model. However, the use of third-party libraries and integrations could potentially introduce security vulnerabilities. |
| **🔄 Version Control and Collaboration** | The codebase is hosted on GitHub and includes a.gitignore file to exclude unnecessary files from version control. The repository includes a README file with instructions for building and running the application. |
| **🔌 External Integrations** | The codebase includes integrations with OpenAI's GPT chatbot and the window.speechSynthesis API for text-to-speech processing. The code also includes some integration with browser-specific APIs for managing browser tabs and windows. |
| **📈 Scalability and Extensibility** | The use of modular code and React components allows for easy scalability and extensibility of the application. However, the lack of automated testing and documentation could potentially make future development more challenging. |

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## ⚙️ Project Structure


```bash
repo
├── LICENSE
├── README.md
├── build.mjs
├── package-lock.json
├── package.json
└── src
    ├── assets
    │   ├── logo.png
    │   ├── logo_handling.png
    │   └── logo_recording.png
    ├── background
    │   └── index.mjs
    ├── components
    │   ├── Callout.jsx
    │   ├── Info.jsx
    │   ├── Popup.jsx
    │   ├── Settings.jsx
    │   ├── TriggerInput.jsx
    │   └── VoiceDropdown.jsx
    ├── content
    │   ├── app.css
    │   ├── audio.mjs
    │   ├── fetch-sse.mjs
    │   ├── index.html
    │   ├── index.mjs
    │   ├── info.mjs
    │   └── stream-async-iterable.mjs
    ├── manifest.json
    └── popup
        ├── index.html
        └── index.mjs

7 directories, 25 files
```

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 💻 Modules

<details closed><summary>Background</summary>

| File      | Summary                                                            | Module                   |
|:----------|:-------------------------------------------------------------------|:-------------------------|
| index.mjs | HTTP 429 error when fetching summary for src/background/index.mjs. | src/background/index.mjs |
|           | Too many requests, retrying...                                     |                          |

</details>

<details closed><summary>Components</summary>

| File              | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Module                           |
|:------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------|
| TriggerInput.jsx  | The provided code snippet is a React component called VoiceDropdown that creates a form input for a trigger phrase with a default value of "Hey girl". When the input value is changed, the state is updated and a function called setTriggerPhrase is called with the new value. The component is exportable and can be used in other parts of the application.                                                                                                                                                        | src/components/TriggerInput.jsx  |
| Popup.jsx         | HTTP 429 error when fetching summary for src/components/Popup.jsx.                                                                                                                                                                                                                                                                                                                                                                                                                                                      | src/components/Popup.jsx         |
|                   | Too many requests, retrying...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                  |
| Callout.jsx       | This code exports a React component called "Callout", which takes in two props: "type" and "children". It returns a div element with the class name "callout" followed by the value of the "type" prop. The children of the component are also included within this div element.                                                                                                                                                                                                                                        | src/components/Callout.jsx       |
| Info.jsx          | This code defines a React component for a voice assistant app called ChassistantGPT. It includes features such as checking for microphone permission, displaying status messages, allowing users to customize trigger phrase and language, and providing instructions for use. It also checks if the user is using Chrome and provides an error message if not. The app relies on an existing session with ChatGPT and does not store or transmit any data except for the prompt directly following the trigger phrase. | src/components/Info.jsx          |
| VoiceDropdown.jsx | This code snippet defines a React component for a voice selection dropdown menu. It uses useState and useEffect hooks to manage state and retrieve available voices from the window.speechSynthesis API. When a user selects a voice, the component sends the chosen voice to a background script. The component also includes a button to test the selected voice.                                                                                                                                                     | src/components/VoiceDropdown.jsx |
| Settings.jsx      | The code defines a Settings component that renders a toggle switch labeled "Natural conversation". The toggle switch controls the state of isFillerEnabled and calls the setFillerEnabled function from an external module with the updated state. The component utilizes useState hook from React to manage state.                                                                                                                                                                                                     | src/components/Settings.jsx      |

</details>

<details closed><summary>Content</summary>

| File                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Module                                |
|:--------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------|
| index.html                | The code snippet defines CSS variables for background color, text color, and callout colors based on a light or dark theme. It also styles various elements such as headings, paragraphs, and buttons. The HTML file includes a div container and JavaScript file for a web application called ChassistantGPT.                                                                                                                                                                               | src/content/index.html                |
| audio.mjs                 | This code snippet defines a set of functionalities that enable a voice assistant to interact with OpenAI's GPT chatbot. It includes functions for obtaining voice input, processing user queries, and generating spoken responses using text-to-speech technology. Other features include the ability to enable/disable filler speech, test the voice settings, and maintain a conversation history. The code also implements measures to prevent accidental closure of the voice assistant. | src/content/audio.mjs                 |
| fetch-sse.mjs             | This code snippet defines a function called fetchSSE that fetches a resource using the fetch API and parses it as a Server-Sent Event (SSE) stream using the eventsource-parser library. It then iterates over the stream, decodes each chunk using a TextDecoder, and feeds it into the parser. Finally, it passes any parsed events of type'event' to a provided onMessage callback function.                                                                                              | src/content/fetch-sse.mjs             |
| app.css                   | The code snippet is a Python function that takes in a list of integers and returns the sum of the even numbers in the list. It uses a for loop to iterate through the list and an if statement to check if each number is even before adding it to the sum variable. The final sum is returned as the output of the function.                                                                                                                                                                | src/content/app.css                   |
| info.mjs                  | The code imports the React and ReactDOM libraries, as well as a custom component called Info. It then uses ReactDOM to render the Info component to the root element of the HTML document. This code is written using the createRoot method, which is a new feature in React version 18.                                                                                                                                                                                                     | src/content/info.mjs                  |
| index.mjs                 | The code imports two modules, "info" and "audio", using the ES6 import syntax. These modules are written in the JavaScript module format and are located in separate files, "info.mjs" and "audio.mjs". The imported modules likely contain code that provides functionality related to information and audio processing, respectively.                                                                                                                                                      | src/content/index.mjs                 |
| stream-async-iterable.mjs | The code defines an async generator function that takes in a stream and returns an async iterable. The function uses the stream reader to read the stream and yield each value as it becomes available. The function also releases the reader's lock once the stream is finished.                                                                                                                                                                                                            | src/content/stream-async-iterable.mjs |

</details>

<details closed><summary>Popup</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                                                 | Module               |
|:-----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------|
| index.html | The provided code is an HTML webpage with embedded CSS styles and a JavaScript file. The CSS styles define variables for color themes and layout properties for the webpage. The HTML body contains a container with an ID of "app" where the JavaScript file is loaded, likely containing the logic and functionality for the webpage. | src/popup/index.html |
| index.mjs  | This code snippet creates a root element in the DOM with the ID "app" using ReactDOM, and renders a Popup component using React. The Popup component is imported from a separate file and is likely a reusable component that displays a popup window.                                                                                  | src/popup/index.mjs  |

</details>

<details closed><summary>Root</summary>

| File             | Summary                                                                                                                                                                                                                                                                                                                                                                               | Module           |
|:-----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| build.mjs        | The provided code snippet is a Node.js script that uses the esbuild and archiver libraries to build and package a browser extension. It first deletes any existing build directory, then uses esbuild to bundle and minify JavaScript and CSS files. Finally, it packages the resulting files, along with static assets and a manifest file, into zip files for Chromium and Firefox. | build.mjs        |
| .prettierrc.yaml | The provided code snippet sets two configuration options for the formatting of code. "semi: false" means that semicolons will not be automatically inserted at the end of statements, while "singleQuote: true" means that single quotes will be used for string literals instead of double quotes.                                                                                   | .prettierrc.yaml |

</details>

<details closed><summary>Workflows</summary>

| File        | Summary                                                                                                                                                                                                                                                                                               | Module                        |
|:------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------|
| release.yml | The provided code snippet sets up a Github action that runs on push and builds a project on Ubuntu using Node.js version 18. It then creates a release using the softprops/action-gh-release action if the push is a tag push, generating release notes and including a specific file in the release. | .github/workflows/release.yml |

</details>

<hr />

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> `[📌  INSERT-PROJECT-PREREQUISITES]`

### 💻 Installation

1. Clone the assistant-chat-gpt repository:
```sh
git clone https://github.com/idosal/assistant-chat-gpt
```

2. Change to the project directory:
```sh
cd assistant-chat-gpt
```

3. Install the dependencies:
```sh
npm install
```

### 🤖 Using assistant-chat-gpt

```sh
node app.js
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

