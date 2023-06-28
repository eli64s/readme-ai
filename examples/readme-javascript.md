
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
assistant-chat-gpt
</h1>
<h3>◦ Bringing AI chat to life!</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/esbuild-FFCF00.svg?style&logo=esbuild&logoColor=black" alt="esbuild" />
<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style&logo=JavaScript&logoColor=black" alt="JavaScript" />
<img src="https://img.shields.io/badge/Prettier-F7B93E.svg?style&logo=Prettier&logoColor=black" alt="Prettier" />
<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style&logo=HTML5&logoColor=white" alt="HTML5" />
<img src="https://img.shields.io/badge/React-61DAFB.svg?style&logo=React&logoColor=black" alt="React" />

<img src="https://img.shields.io/badge/ESLint-4B32C3.svg?style&logo=ESLint&logoColor=white" alt="ESLint" />
<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style&logo=JSON&logoColor=white" alt="JSON" />
</p>

![GitHub top language](https://img.shields.io/github/languages/top/idosal/assistant-chat-gpt?style&color=5D6D7E)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/idosal/assistant-chat-gpt?style&color=5D6D7E)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/idosal/assistant-chat-gpt?style&color=5D6D7E)
![GitHub license](https://img.shields.io/github/license/idosal/assistant-chat-gpt?style&color=5D6D7E)
</div>

---

## 📒 Table of Contents
- [📒 Table of Contents](#-table-of-contents)
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

The project is a web application that serves as a voice assistant using OpenAI's ChatGPT and the Web Speech API. The codebase includes components for managing user input, rendering chat interfaces, and providing information about the assistant. It supports voice input and output, real-time chat history, and various settings options. The project aims to provide an intuitive and interactive interface for users to interact with ChatGPT and receive spoken responses, enhancing the experience of using a voice assistant.

---

## ⚙️ Features

| Feature                | Description                           |
| ---------------------- | ------------------------------------- |
| **⚙️ Architecture**    | The codebase follows a modular architecture, with separate folders for different components and functionalities such as background, popup, content, and components. The background script listens to events, while the popup and content scripts handle UI interactions. The communication between these components is done through the messaging system provided by Chrome extensions.
| **📖 Documentation**   | The repository lacks comprehensive documentation. While some files have brief comments and explanations, there is no dedicated documentation detailing the system's usage, design patterns, or architectural decisions.
| **🔗 Dependencies**    | The codebase relies on various external packages, including React, ReactDOM, Sass, esbuild, archiver, and react-toggle. These libraries provide support for UI rendering, CSS styling, package bundling, and toggle functionality. The OpenAI API is used for the ChatGPT integration.
| **🧩 Modularity**      | The system is organized into smaller, interchangeable components, making it easier to understand and maintain. Each component has a specific responsibility, such as handling background events, rendering UI, managing settings, and communicating with third-party APIs.
| **✔️ Testing**         | There is no explicit mention of testing in the repository. The absence of testing files or scripts indicates that testing may not be practiced extensively in this codebase.
| **⚡️ Performance**     | Performance cannot be fully assessed without analyzing the entire codebase. However, based on the provided summaries, the codebase seems to handle speech recognition, speech synthesis, and chat interactions efficiently using Web Speech API and OpenAI's ChatGPT.
| **🔐 Security**        | The codebase does not explicitly detail security measures, but it handles authentication with the OpenAI API. It's important to ensure that user data is handled securely, especially for a chat assistant that may process sensitive information.
| **🔀 Version Control** | The codebase is hosted on GitHub, suggesting the use of Git for version control. However, further analysis is required to evaluate the specific version control strategies or practices implemented.
| **🔌 Integrations**    | The codebase interacts with Chrome extensions' APIs for browser events and UI rendering. It also integrates with the OpenAI API for natural language processing and the Web Speech API for speech recognition and synthesis.
| **📶 Scalability**     | Scalability cannot be determined without a more detailed analysis. However, the use of modular components and external APIs allows for flexibility and potential scalability in handling additional features or expanding the system's functionality.

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

<details closed><summary>Root</summary>

| File                                                                          | Summary                                                                                                                                                                                                                                                                                                                |
| ---                                                                           | ---                                                                                                                                                                                                                                                                                                                    |
| [build.mjs](https://github.com/idosal/assistant-chat-gpt/blob/main/build.mjs) | The code snippet uses esbuild and archiver libraries to build and package a web application. It compiles various entry points, applies plugins (including a Sass plugin), minifies the code, and creates a build directory. It then zips the necessary files into separate archives for Chrome and Firefox extensions. |

</details>

<details closed><summary>Background</summary>

| File                                                                                         | Summary                                                                                                                                               |
| ---                                                                                          | ---                                                                                                                                                   |
| [index.mjs](https://github.com/idosal/assistant-chat-gpt/blob/main/src/background/index.mjs) | The code snippet sets up an event listener for when Chrome starts up and logs a message. It also opens the options page of the extension when called. |

</details>

<details closed><summary>Popup</summary>

| File                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                         |
| ---                                                                                       | ---                                                                                                                                                                                                                                                                                                                                             |
| [index.html](https://github.com/idosal/assistant-chat-gpt/blob/main/src/popup/index.html) | The provided code snippet is an HTML document that defines a CSS style sheet and includes a JavaScript module file. It sets up the structure and styling for a web page, with specific formatting for different color schemes. It also contains a container element with an ID "app" where a JavaScript application can be loaded and executed. |
| [index.mjs](https://github.com/idosal/assistant-chat-gpt/blob/main/src/popup/index.mjs)   | The code imports React and ReactDOM libraries and the Popup component. It uses ReactDOM to render the Popup component to the "app" id element. This code sets up a root app element and renders a popup component onto it.                                                                                                                      |

</details>

<details closed><summary>Content</summary>

| File                                                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                           |
| ---                                                                                                                       | ---                                                                                                                                                                                                                                                                                                                                                               |
| [index.html](https://github.com/idosal/assistant-chat-gpt/blob/main/src/content/index.html)                               | This code snippet is an HTML document with embedded CSS styles. It sets various CSS variables for different color schemes (light and dark) and defines styles for different elements such as headings, paragraphs, buttons, and callouts with different colors. It also includes links to external JavaScript files that are commented out.                       |
| [audio.mjs](https://github.com/idosal/assistant-chat-gpt/blob/main/src/content/audio.mjs)                                 | This code snippet sets up a voice assistant using Web Speech API and OpenAI's ChatGPT. It listens for user speech input, sends it to ChatGPT for processing, and generates a spoken response. It also handles authentication, history tracking, and system events.                                                                                                |
| [fetch-sse.mjs](https://github.com/idosal/assistant-chat-gpt/blob/main/src/content/fetch-sse.mjs)                         | The provided code snippet is a function that uses the fetch API to retrieve server-sent events (SSE) from a specified resource. It creates an eventsource-parser to parse the SSE data and calls the onMessage callback for each event received. It uses a streamAsyncIterable function to iterate over the response body in chunks and feeds them to the parser. |
| [app.css](https://github.com/idosal/assistant-chat-gpt/blob/main/src/content/app.css)                                     | The code snippet is a function that takes in a list of numbers and returns the sum of all odd numbers in the list. It uses a loop to iterate over each number in the list, checks if it is odd, and adds it to a running total. Finally, it returns the total sum of the odd numbers.                                                                             |
| [info.mjs](https://github.com/idosal/assistant-chat-gpt/blob/main/src/content/info.mjs)                                   | The code imports React and ReactDOM libraries, as well as the Info component. It uses ReactDOM's createRoot method to render the Info component on the root element of the HTML document. The Info component is created using the React.createElement function.                                                                                                   |
| [index.mjs](https://github.com/idosal/assistant-chat-gpt/blob/main/src/content/index.mjs)                                 | The code snippet imports two modules,'info' and'audio', providing access to their respective functionalities.                                                                                                                                                                                                                                                     |
| [stream-async-iterable.mjs](https://github.com/idosal/assistant-chat-gpt/blob/main/src/content/stream-async-iterable.mjs) | The code snippet provides a function called "streamAsyncIterable" which takes a stream as input and returns an async iterable. It uses the stream's reader object to read data asynchronously in a looping fashion. It yields data until the reader is done or until there is no more data to read. Finally, it releases the lock of the reader.                  |

</details>

<details closed><summary>Components</summary>

| File                                                                                                         | Summary                                                                                                                                                                                                                                                                                                                                                                              |
| ---                                                                                                          | ---                                                                                                                                                                                                                                                                                                                                                                                  |
| [TriggerInput.jsx](https://github.com/idosal/assistant-chat-gpt/blob/main/src/components/TriggerInput.jsx)   | This code snippet is for a VoiceDropdown component in a React application. It allows the user to set a trigger phrase which is stored and displayed in an input field. The onChange event updates the trigger value and invokes the setTriggerPhrase function with the updated trigger value.                                                                                        |
| [Popup.jsx](https://github.com/idosal/assistant-chat-gpt/blob/main/src/components/Popup.jsx)                 | This code snippet is a React component that renders a chat UI for a chat assistant. It retrieves chat history from a Chrome extension and displays messages in a MessageList component. The component uses useRef and useEffect hooks to handle scrolling and update the chat history.                                                                                               |
| [Callout.jsx](https://github.com/idosal/assistant-chat-gpt/blob/main/src/components/Callout.jsx)             | This code exports a React component called Callout. It takes two props: type (defines the styling) and children (the content inside the Callout component). It returns a div element with the classNames'callout' and the type prop, containing the children.                                                                                                                        |
| [Info.jsx](https://github.com/idosal/assistant-chat-gpt/blob/main/src/components/Info.jsx)                   | This code snippet is for a React component called "Info". It renders a page with information about a voice assistant called ChassistantGPT. The component checks if the user is using Chrome and if the microphone permission is granted. It displays relevant messages and provides settings options. It also explains how to use ChassistantGPT and highlights its privacy policy. |
| [VoiceDropdown.jsx](https://github.com/idosal/assistant-chat-gpt/blob/main/src/components/VoiceDropdown.jsx) | This code snippet is a React component that renders a voice selection dropdown menu. It uses the Web Speech API to get available voices and updates the dropdown options accordingly. When a voice is selected, it updates the state and sends the selected voice to a background script. It also includes a button to test the selected voice.                                      |
| [Settings.jsx](https://github.com/idosal/assistant-chat-gpt/blob/main/src/components/Settings.jsx)           | The code snippet defines a Settings component that manages a toggle switch for enabling/disabling filler in a voice conversation. It uses the useState hook to track the state of the toggle switch and onChange event to update the state and trigger an action. The component renders a Toggle component from the react-toggle library along with a label.                         |

</details>

---

## 🚀 Getting Started

### ✔️ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - `ℹ️ Requirement 1`
> - `ℹ️ Requirement 2`
> - `ℹ️ ...`

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

### 🎮 Using assistant-chat-gpt

```sh
node app.js
```

### 🧪 Running Tests
```sh
npm test
```

---


## 🗺 Roadmap

> - [X] `ℹ️  Task 1: Implement X`
> - [ ] `ℹ️  Task 2: Refactor Y`
> - [ ] `ℹ️ ...`


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

This project is licensed under the `ℹ️  INSERT-LICENSE-TYPE` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 👏 Acknowledgments

> - `ℹ️  List any resources, contributors, inspiration, etc.`

---
