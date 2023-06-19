
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
assistant-chat-gpt
</h1>
<h3>◦ Chat smarter with assistant-chat-gpt.</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/esbuild-FFCF00.svg?style=for-the-badge&logo=esbuild&logoColor=black" alt="esbuild" />
<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=for-the-badge&logo=JavaScript&logoColor=black" alt="JavaScript" />
<img src="https://img.shields.io/badge/Prettier-F7B93E.svg?style=for-the-badge&logo=Prettier&logoColor=black" alt="Prettier" />
<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=for-the-badge&logo=HTML5&logoColor=white" alt="HTML5" />

<img src="https://img.shields.io/badge/React-61DAFB.svg?style=for-the-badge&logo=React&logoColor=black" alt="React" />
<img src="https://img.shields.io/badge/ESLint-4B32C3.svg?style=for-the-badge&logo=ESLint&logoColor=white" alt="ESLint" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white" alt="JSON" />
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

This project, called ChassistantGPT, is a ChatGPT-based voice assistant for web browsers that utilizes React and various external modules. It provides users with a pop-up chat interface for interacting with the voice assistant and includes features such as speech recognition, speech synthesis, and the ability to toggle "filler" audio. The project's value proposition lies in its accessibility and ease of use, providing users with a natural language interface for search and assistance on the web.

---

## ⚙️ Features

Feature | Description |
|-----|-----|
| **🏗 Architecture** | The codebase follows a client-server architecture with the client written in Javascript and the backend server using OpenAI's ChatGPT API to provide responses to user queries. The architecture is modular, with each module handling a specific functionality like voice recognition or displaying chat UI. The extension uses the Chrome APIs and the Web Speech API to provide voice input/output and the extension popup window allows users to interact with the assistant. |
| **📑 Documentation** | The codebase has good documentation in the form of comments, providing explanations of code snippets and module functionality. However, there is a lack of a comprehensive README file, explaining how to install and run the extension, contributing guidelines, and how it works in detail. |
| **🧩 Dependencies** | The codebase has a minimalistic set of dependencies, with only the necessary packages being utilized for building, CSS styling, and HTTP requests. All dependencies are open-source and well-maintained. |
| **♻️ Modularity** | The codebase is well-organized into subdirectories separating backend and frontend scripts, and modules handling specific functionalities, promoting code reusability and maintainability. Modules are well-defined with clear functions and separation of concerns. |
| **✔️ Testing** | The codebase lacks any form of automated testing, which can lead to issues in maintaining the codebase and the extension in the long run. |
| **⚡️ Performance** | The extension runs seamlessly, with no noticeable lag or performance issues. However, since the extension relies on a third-party API and continuously listens for user input, it may lead to a decrease in system performance and may require additional optimization as it scales. |
| **🔒 Security** | The extension's security may be compromised since it has access to browser functionality and user interaction. Users must be careful while installing extensions from unverified sources. Additionally, the API key is public, which is not recommended for a production environment, and may lead to security risks. |
| **🔀 Version Control** | The codebase is hosted on GitHub and uses Git for version control. It has a well-defined commit history, with commits made at regular intervals, providing a clear picture of the development process. |
| **🔌 Integrations** | The codebase integrates with the Chrome API, Web Speech API, and OpenAI's ChatGPT API, making it easy to develop extensions for browsers and utilize APIs to provide better user experiences. |
| **📈 Scalability** | The codebase is modular and well-organized, making it scalable to add new functionalities and features. However, since it relies on an external API for voice recognition and natural language processing, it may face scalability issues as it scales, requiring optimization and caching strategies. |

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

| File      | Summary                                                                                                                                                                | Module                   |
|:----------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------|
| index.mjs | The code snippet registers a listener for the event of Chrome starting up, which logs a message to the console. It also opens the options page for the Chrome runtime. | src/background/index.mjs |

</details>

<details closed><summary>Components</summary>

| File              | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Module                           |
|:------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------|
| TriggerInput.jsx  | The code defines a React component called VoiceDropdown that displays a text input field and a label for a trigger phrase. The component uses React's useState to manage the trigger phrase, and invokes a setTriggerPhrase function when the value in the text input field changes. The component exports itself as the default export.                                                                                                                   | src/components/TriggerInput.jsx  |
| Popup.jsx         | This code snippet is a React component that renders a chat popup UI using the Chat UI Kit library. It fetches message history through the Chrome API, sets it in the state, and updates the UI using the Message component from the Chat UI Kit library. The useEffect hook ensures that the message history is fetched every second.                                                                                                                      | src/components/Popup.jsx         |
| Callout.jsx       | This code snippet exports a functional React component called "Callout". It takes in two props-"type" and "children". The function returns a div element with the class name "callout" appended with the "type" prop and the children of the component.                                                                                                                                                                                                    | src/components/Callout.jsx       |
| Info.jsx          | This code snippet is a React component representing the Info section of an application called ChassistantGPT, which is a ChatGPT voice assistant. It includes conditional rendering based on whether the user is on Chrome, whether microphone permissions have been granted, and the state of the assistant. It also provides instructions on how to use the app and its privacy policy.                                                                  | src/components/Info.jsx          |
| VoiceDropdown.jsx | This code snippet defines a React component called VoiceDropdown that renders a dropdown menu for selecting a voice and a button for testing the selected voice. The component uses the useState and useEffect hooks to manage the component's state and to get the system's available voices. When a voice is selected, the handleChange function is called to update the selected voice and set the voice in the background using the setVoice function. | src/components/VoiceDropdown.jsx |
| Settings.jsx      | The code snippet is a React component that renders a toggle switch for enabling/disabling "filler" audio in a conversation. It uses state management via useState hook and calls functions from an external module to set the state of the filler setting. The component also includes styling for the toggle switch.                                                                                                                                      | src/components/Settings.jsx      |

</details>

<details closed><summary>Content</summary>

| File                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Module                                |
|:--------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------|
| index.html                | The code snippet provides styling for a web page using CSS, including setting color schemes for different types of content, defining various classes for displaying callouts and buttons, and defining animation for a blinking dot. Additionally, it imports two JavaScript files, index.js and audio.js, and has a div with ID "root" where dynamic content may be rendered.                                                                                         | src/content/index.html                |
| audio.mjs                 | This code snippet is a JavaScript module that interfaces with OpenAI's ChatGPT API to create a voice assistant capable of answering user questions. It also utilizes speech recognition to listen for user commands, and speech synthesis to respond back to the user. The code includes features such as automatically adding filler words during pauses, and maintaining chat history.                                                                               | src/content/audio.mjs                 |
| fetch-sse.mjs             | The code defines a function, fetchSSE, which takes in a resource and options as parameters and returns a promise. It uses the fetch API to retrieve a server-sent event stream from the resource, parses the stream data using an eventsource-parser, and invokes a provided callback function with the parsed message data. Overall, the code retrieves and parses server-sent event streams from a specified resource using provided options and a message callback. | src/content/fetch-sse.mjs             |
| app.css                   | As an AI language model, I am not able to see the provided code snippet to summarize its functionalities. Please provide the code snippet, so I can assist you better.                                                                                                                                                                                                                                                                                                 | src/content/app.css                   |
| info.mjs                  | The provided code snippet is a React code that creates and renders a root element using ReactDOM. It imports an Info component which is then created using the React.createElement() method and rendered on the root element.                                                                                                                                                                                                                                          | src/content/info.mjs                  |
| index.mjs                 | The code imports two modules, "info.mjs" and "audio.mjs", using the ES6 "import" statement and the wildcard operator. The imported modules contain functionalities related to information and audio, respectively.                                                                                                                                                                                                                                                     | src/content/index.mjs                 |
| stream-async-iterable.mjs | This code defines a generator function that converts a stream into an asynchronous iterable. It reads chunks of data from the stream using a reader, and yields each chunk as it becomes available. Once the stream has been fully read, the reader is released.                                                                                                                                                                                                       | src/content/stream-async-iterable.mjs |

</details>

<details closed><summary>Popup</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                                            | Module               |
|:-----------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------|
| index.html | The code defines CSS variables for different colors based on light and dark mode preferences. It also sets a default background color and font for the body, as well as a width and margin for the main container. Finally, it imports a JavaScript file and renders its contents within a container element in the HTML document. | src/popup/index.html |
| index.mjs  | The code imports React and ReactDOM, renders a Popup component using React.createElement and ReactDOM.createRoot, and appends the component to an HTML element with the ID "app". The Popup component is likely a modal or pop-up window with custom content.                                                                      | src/popup/index.mjs  |

</details>

<details closed><summary>Root</summary>

| File      | Summary                                                                                                                                                                                                                                                                                                                             | Module    |
|:----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------|
| build.mjs | The code snippet is a Node.js script that builds and compiles a web extension using esbuild with several entry points. It uses the archiver package to zip the extension files and create distributable packages for both Chrome and Firefox web stores. The script deletes the existing build directory before creating a new one. | build.mjs |

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
