
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
assistant-chat-gpt
</h1>
<h3 align="center">📍 Unlocking the power of AI for seamless conversations-Assistant Chat GPT on GitHub</h3>
<h3 align="center">⚙️ Developed with the software and tools below:</h3>

<p align="center">
<img src="https://img.shields.io/badge/esbuild-FFCF00.svg?style=for-the-badge&logo=esbuild&logoColor=black" alt="esbuild" />
<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=for-the-badge&logo=JavaScript&logoColor=black" alt="JavaScript" />
<img src="https://img.shields.io/badge/Prettier-F7B93E.svg?style=for-the-badge&logo=Prettier&logoColor=black" alt="Prettier" />
<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=for-the-badge&logo=HTML5&logoColor=white" alt="HTML5" />
<img src="https://img.shields.io/badge/React-61DAFB.svg?style=for-the-badge&logo=React&logoColor=black" alt="React" />

<img src="https://img.shields.io/badge/ESLint-4B32C3.svg?style=for-the-badge&logo=ESLint&logoColor=white" alt="ESLint" />
<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=for-the-badge&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="Markdown" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white" alt="JSON" />
</p>
</div>

---

## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [💫 Features](#-features)
- [📂 Project Structure](#-project-structure)
- [🧩 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
  - [✅ Prerequisites](#-prerequisites)
  - [🖥 Installation](#-installation)
  - [🤖 Using assistant-chat-gpt](#-using-assistant-chat-gpt)
  - [🧪 Running Tests](#-running-tests)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

This project provides a voice-activated chatbot using OpenAI's GPT-3 API and the Web Speech API. Users can converse with the assistant using voice commands and receive spoken language responses using text-to-speech synthesis. The assistant also includes a chat history popup and features like voice trigger phrases and a settings toggle switch. The project aims to provide a more natural and conversational experience with an AI assistant.

---

## 💫 Features

Feature | Description |
|---|---|
| **🏗 Structure and Organization** | The codebase follows a typical folder structure for a Chrome Extension with folders for background, popup, and content scripts. The codebase also includes a build script that compiles the source files and creates a zip file for the extension. |
| **📝 Code Documentation** | The codebase includes some inline comments to help understand the code, but overall the code is not extensively documented. |
| **🧩 Dependency Management** | Dependencies are managed through the use of the `package.json` file and Node.js package manager (npm). |
| **♻️ Modularity and Reusability** | The codebase is structured into separate modules for different functionalities such as voice activation, chat UI, and audio settings, which enhances modularity and reusability. |
| **✔️ Testing and Quality Assurance** | No testing or quality assurance tools/frameworks have been integrated into the codebase. |
| **⚡️ Performance and Optimization** | Performance and optimization do not seem to be a primary focus of the codebase, although the use of the async/await syntax in several functions can improve performance. |
| **🔒 Security Measures** | The codebase does not contain any obvious security vulnerabilities, although some of the external APIs used by the code could potentially introduce vulnerabilities. |
| **🔄 Version Control and Collaboration** | The codebase is hosted on GitHub and version control follows the standard Git workflow. No other collaboration tools or features are used. |
| **🔌 External Integrations** | The codebase integrates with multiple external APIs such as OpenAI and the Web Speech API, enabling voice-activated chat and text-to-speech synthesis. |
| **📈 Scalability and Extensibility** | The modular design and organization of the codebase can allow for easier scalability and extensibility in the future, although the lack of documentation and testing could hinder this. |

---


<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

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

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 🧩 Modules

<details closed><summary>Background</summary>

| File      | Summary                                                                                                                                                                                  | Module                   |
|:----------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------|
| index.mjs | This code snippet registers an event listener for when the Chrome extension is started, logging a message to the console. It also opens the Chrome extension's options page when called. | src/background/index.mjs |

</details>

<details closed><summary>Components</summary>

| File              | Summary                                                                                                                                                                                                                                                                                                                                                                                             | Module                           |
|:------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------|
| TriggerInput.jsx  | The code implements a React component called VoiceDropdown which is used for setting a voice trigger phrase. It includes a state hook which initializes the default trigger phrase as "Hey girl". The handleChange function updates the trigger phrase and sets the new value in the input field. The component exports as a default component.                                                     | src/components/TriggerInput.jsx  |
| Popup.jsx         | This is a React component for a chat popup that displays a chat history fetched from the Chrome runtime. It uses the Chat UI Kit React library to render the chat messages and a setInterval function to continuously update the chat history. The component also includes a ref to automatically scroll to the bottom of the message list on update.                                               | src/components/Popup.jsx         |
| Callout.jsx       | This code defines a React functional component named "Callout" that takes in two props: "type" and "children". It returns a div element with a class name combining "callout" and the "type" prop, and renders the "children" prop inside that div.                                                                                                                                                 | src/components/Callout.jsx       |
| Info.jsx          | This code snippet defines the Info component which displays information about the ChassistantGPT voice assistant. It uses useState and useEffect hooks to set the microphone permission and check if the browser is Chrome. It renders various Callout components, input fields, and instructions on how to use the voice assistant. It also includes a function to check if the browser is Chrome. | src/components/Info.jsx          |
| VoiceDropdown.jsx | The code snippet is a React component that renders a dropdown menu allowing users to select a voice for text-to-speech output. The component fetches and displays available voices using the Web Speech API and sends the selected voice to a background script for processing. A "Test Voice" button allows users to preview the selected voice.                                                   | src/components/VoiceDropdown.jsx |
| Settings.jsx      | This code defines a React component that renders a toggle switch to enable or disable natural conversation mode. It uses the useState hook to manage the state of the toggle switch and the setFillerEnabled function to update the audio settings. The component exports as a default export.                                                                                                      | src/components/Settings.jsx      |

</details>

<details closed><summary>Content</summary>

| File                      | Summary                                                                                                                                                                                                                                                                                                                                                              | Module                                |
|:--------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------|
| index.html                | The provided code snippet is an HTML document that defines various CSS styles for use in web development. The styles include custom color variables, responsive design rules for different screen sizes, and various classes for formatting elements like callouts and buttons. The document also includes links to JavaScript files for dynamic behavior.           | src/content/index.html                |
| audio.mjs                 | The provided code snippet is a JavaScript module that uses the Web Speech API and OpenAI to enable voice-activated chat with an AI assistant. It allows users to converse with the assistant using voice commands and responds with spoken language using text-to-speech synthesis. The code interacts with the OpenAI chat API and fetches the data using fetchSSE. | src/content/audio.mjs                 |
| fetch-sse.mjs             | The provided code defines a function that fetches a Server-Sent Events (SSE) resource and processes its messages using a callback function. It uses the eventsource-parser library to parse the SSE response and convert it into individual events, which are then passed to the callback function. The response is streamed using the streamAsyncIterable function. | src/content/fetch-sse.mjs             |
| app.css                   | The code snippet initializes a Flask web application and defines a single route ("/") that accepts GET requests. When a GET request is made to this route, the function returns a string "Hello, World!" as the response. The app.run() method is used to run the application on the local server.                                                                   | src/content/app.css                   |
| info.mjs                  | The provided code imports React and ReactDOM libraries and renders the Info component to the DOM using the createRoot() method from ReactDOM. The Info component is passed to the createRoot() method via the React.createElement() method. This code snippet essentially renders the Info component to the root element in the DOM.                                 | src/content/info.mjs                  |
| index.mjs                 | The code snippet imports two modules-`info.mjs` and `audio.mjs`-using the asterisk syntax to import all their exports into `info` and `audio` objects. This enables access to the functionalities of these modules in the current module.                                                                                                                            | src/content/index.mjs                 |
| stream-async-iterable.mjs | The code defines an asynchronous generator function that takes a stream as an input parameter. It returns an async iterator that allows iterating over the chunks of data in the stream as they become available. The function uses the stream's reader to read the chunks of data and release the reader's lock once it's done.                                     | src/content/stream-async-iterable.mjs |

</details>

<details closed><summary>Popup</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                                                                 | Module               |
|:-----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------|
| index.html | The provided code snippet includes a CSS stylesheet and HTML markup that define styling for a web page. It also includes a script tag that links to a JS file, allowing for dynamic content to be displayed on the page. The styling includes variables for color schemes, and media queries for different color schemes depending on user preferences. | src/popup/index.html |
| index.mjs  | This code imports React and ReactDOM, and then renders a Popup component on the web page using the createRoot function and the React.createElement method. The Popup component is likely a modal or popup window that is displayed to the user.                                                                                                         | src/popup/index.mjs  |

</details>

<details closed><summary>Root</summary>

| File      | Summary                                                                                                                                                                                                                                                                                                                                              | Module    |
|:----------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------|
| build.mjs | The code begins by importing various modules such as archiver, esbuild, fs, etc. It then defines several asynchronous functions such as runEsbuild(), deleteOldDir(), and zipFiles(). This code compiles the source files and creates a compressed file for the Chromium browser by creating a zip file with a specific set of files included in it. | build.mjs |

</details>

---

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - [📌  PREREQUISITE-1]
> - [📌  PREREQUISITE-2]
> - ...

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

> - [X] [📌  Task 1: Implement X]
> - [ ] [📌  Task 2: Refactor Y]
> - [ ] [📌  Task 3: Optimize Z]
> - [ ] ...


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

## 📄 License

This project is licensed under the `[📌  INSERT-LICENSE-TYPE]` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 👏 Acknowledgments

> - [📌  List any resources, contributors, inspiration, etc.]

---
