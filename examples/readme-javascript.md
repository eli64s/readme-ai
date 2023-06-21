
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
assistant-chat-gpt
</h1>
<h3>◦ Get personalized solutions with Assistant Chat GPT!</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/esbuild-FFCF00.svg?style&logo=esbuild&logoColor=black" alt="esbuild" />
<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style&logo=JavaScript&logoColor=black" alt="JavaScript" />
<img src="https://img.shields.io/badge/Prettier-F7B93E.svg?style&logo=Prettier&logoColor=black" alt="Prettier" />
<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style&logo=HTML5&logoColor=white" alt="HTML5" />

<img src="https://img.shields.io/badge/React-61DAFB.svg?style&logo=React&logoColor=black" alt="React" />
<img src="https://img.shields.io/badge/ESLint-4B32C3.svg?style&logo=ESLint&logoColor=white" alt="ESLint" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style&logo=JSON&logoColor=white" alt="JSON" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
</p>

![GitHub top language](https://img.shields.io/github/languages/top/idosal/assistant-chat-gpt?style&color=5D6D7E)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/idosal/assistant-chat-gpt?style&color=5D6D7E)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/idosal/assistant-chat-gpt?style&color=5D6D7E)
![GitHub license](https://img.shields.io/github/license/idosal/assistant-chat-gpt?style&color=5D6D7E)
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

The project is a Chrome extension that integrates OpenAI's GPT-3 language model for conversational AI functionality. It uses Web Speech API and custom Chrome extension APIs for speech recognition and synthesis, as well as offering a chat interface for user interaction. The extension's core functionality is to provide users with a voice assistant that can help with tasks such as web search, language translation, and general conversation. Its value proposition lies in offering a free, open-source, and customizable alternative to commercial voice assistants.

---

## ⚙️ Features

Feature | Description |
|-----|-----|
| **🏗 Architecture** | The codebase follows a modular architecture, with different functionalities separated into their respective folders. The codebase utilizes the React library for creating UI components and Web Speech API for speech recognition and speech synthesis. The codebase is designed to be used as a Chrome extension. |
| **📑 Documentation** | The codebase contains documentation in the form of comments and README file. The README file provides installation instructions, usage instructions, and an overview of the codebase. The comments in the codebase are comprehensive, providing explanations for the functionalities of each module and component. |
| **🧩 Dependencies** | The codebase has various dependencies, including "@chatscope/chat-ui-kit-react" and "@chatscope/chat-ui-kit-styles" for UI components, "eventsource-parser" for parsing SSE responses, and "esbuild" for bundling and minifying JavaScript files. |
| **♻️ Modularity** | The codebase is highly modular, with different functionalities separated into their respective folders. Each module has its own responsibility and functionality, and can be imported into other modules as needed. This makes the codebase easy to maintain and modify. |
| **✔️ Testing** | The codebase does not have any test files or automated testing implemented. |
| **⚡️ Performance** | The codebase utilizes esbuild to bundle and minify JavaScript files, reducing the file size and improving loading times. The codebase also utilizes asynchronous function calls and generators for efficiency. |
| **🔒 Security** | The codebase utilizes Chrome's extension API for icon and command management, and has appropriate permissions set for the various functionalities used. However, as with any Chrome extension, the user should only install and run the extension from a trusted source. |
| **🔀 Version Control** | The codebase is hosted on GitHub, with version control managed using Git. Commits and pull requests are appropriately labeled and documented. |
| **🔌 Integrations** | The codebase integrates with OpenAI's GPT-3 language model to provide conversational AI functionality, utilizing Web Speech API for speech recognition and speech synthesis. |
| **📈 Scalability** | The codebase can be scaled to add additional functionalities as needed, with the modular architecture making it easy to add and remove modules as necessary. However, the codebase may need to be refactored to ensure scalability and maintainability as the codebase grows in size and complexity. |

---


## 📂 Project Structure


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

## 🧩 Modules

<details closed><summary>Background</summary>

| File      | Summary                                                                                                                                                                                                                  | Module                   |
|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------|
| index.mjs | This code snippet registers an event listener that logs a message to the console when the Chrome extension is started up. It then calls the `openOptionsPage()` function which opens the options page for the extension. | src/background/index.mjs |

</details>

<details closed><summary>Components</summary>

| File              | Summary                                                                                                                                                                                                                                                                                                                                                                                                        | Module                           |
|:------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------|
| TriggerInput.jsx  | This code snippet defines a React component called VoiceDropdown that displays a setting for a trigger phrase input field. The current trigger phrase value is stored in state, and is updated via the handleChange function when the user types into the input field. The function also calls the setTriggerPhrase function from an external audio module to update the trigger phrase for voice recognition. | src/components/TriggerInput.jsx  |
| Popup.jsx         | This code snippet is a React component for a chat window that retrieves a chat history from a Chrome extension, displays it along with a welcome message in a message list, and automatically scrolls to the latest message. The component utilizes various modules from "@chatscope/chat-ui-kit-react" and "@chatscope/chat-ui-kit-styles" to render the chat window.                                         | src/components/Popup.jsx         |
| Callout.jsx       | The code snippet defines a functional component called Callout that receives two props, type and children. It returns a div element with a class of "callout" and the type passed in as a class as well. The children are rendered within the div.                                                                                                                                                             | src/components/Callout.jsx       |
| Info.jsx          | The provided code snippet is a React component that represents an information page for a voice assistant application. It includes various sections such as Chrome compatibility check, microphone access request, settings options, usage instructions, and privacy information. The component also utilizes hooks such as useEffect and useState for handling state and media permissions.                    | src/components/Info.jsx          |
| VoiceDropdown.jsx | This code defines a'VoiceDropdown' component that dynamically retrieves and displays various available voices for text-to-speech synthesis. The component allows the user to select a voice and provides a'Test Voice' button for audio output testing. The selected voice is sent to the back-end script for speech synthesis.                                                                                | src/components/VoiceDropdown.jsx |
| Settings.jsx      | This code exports a React component called Settings that renders a toggle switch and a label. The toggle switch has a default value of true and when toggled, it updates the component state as well as calls the setFillerEnabled function from an external module. The component is used to control a setting for enabling or disabling filler words in a speech recognition system.                         | src/components/Settings.jsx      |

</details>

<details closed><summary>Content</summary>

| File                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                   | Module                                |
|:--------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------|
| index.html                | The provided code contains HTML, CSS, and JavaScript code used for styling and rendering the UI of an application called ChassistantGPT. It defines variables, styles, and animations used for UI elements such as callouts, buttons, and containers. It also references two JavaScript files-index.js and audio.js, with index.js being the main script file.                                            | src/content/index.html                |
| audio.mjs                 | The code snippet is a JavaScript module that integrates with OpenAI's GPT-3 language model to provide conversational AI functionality. It uses Web Speech API for speech recognition and speech synthesis, as well as Chrome's extension API for icon and command management. It also includes functionality for handling user interaction and maintaining conversation history.                          | src/content/audio.mjs                 |
| fetch-sse.mjs             | The code defines a function called fetchSSE that fetches data from a server using the Server-Sent Events (SSE) protocol. It parses the response data using a third-party eventsource-parser library and calls the onMessage function provided in the options argument for each parsed event. The parsed data is obtained by iterating over the response body using a custom streamAsyncIterable function. | src/content/fetch-sse.mjs             |
| app.css                   | As an AI language model, I am unable to see the provided code snippet. Thus, I cannot offer a summary of its core functionalities. Could you provide me with the code snippet, please?                                                                                                                                                                                                                    | src/content/app.css                   |
| info.mjs                  | This code imports the React and ReactDOM libraries to render the Info component onto a web page. It creates a root element with the ID "root" and uses the createRoot method to render the Info component using the React.createElement function.                                                                                                                                                         | src/content/info.mjs                  |
| index.mjs                 | The provided code snippet imports all the exported functionalities from two different modules:'info.mjs' and'audio.mjs' using ES6 module syntax. These modules can then be utilized in the code where this import statement is called.                                                                                                                                                                    | src/content/index.mjs                 |
| stream-async-iterable.mjs | The code snippet exports an asynchronous generator function that iterates over a stream by continually reading from it using a reader obtained from the stream. The generator yields each value read from the stream until the stream is done, at which point it returns. Finally, the reader is released after the loop is finished.                                                                     | src/content/stream-async-iterable.mjs |

</details>

<details closed><summary>Popup</summary>

| File       | Summary                                                                                                                                                                                                                                                             | Module               |
|:-----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------|
| index.html | The code snippet defines CSS variables for different color schemes and sets the default font and layout for the HTML page, while allowing for media query-based overrides. It also includes a container div and script tag to load JavaScript code from "index.js". | src/popup/index.html |
| index.mjs  | This code snippet imports the necessary modules for rendering a popup component in React. Using ReactDOM, the root element is created and rendered using the Popup component created with React.createElement().                                                    | src/popup/index.mjs  |

</details>

<details closed><summary>Root</summary>

| File      | Summary                                                                                                                                                                                                                                                                                                                                            | Module    |
|:----------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------|
| build.mjs | The code is using the Node.js packages "archiver", "esbuild", and "fs" to build and package a Chrome extension. It first deletes the old build directory, then uses esbuild to bundle and minify several entry points (JavaScript files). Finally, it zips various common files and the newly created build files into a Chrome extension package. | build.mjs |

</details>

---

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - [ℹ️ Requirement 1]
> - [ℹ️ Requirement 2]
> - [...]

### 🖥 Installation

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
npm test
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
