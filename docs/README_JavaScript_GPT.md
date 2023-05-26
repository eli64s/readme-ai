
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
assistant-chat-gpt
</h1>
<h3 align="center">📍 GitHub's Assistant-Chat GPT: Unlocking Your AI Conversation Potential!</h3>
<h3 align="center">🚀 Developed with the software and tools below.</h3>
<p align="center">

<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=for-the-badge&logo=JavaScript&logoColor=black" alt="JavaScript" />
<img src="https://img.shields.io/badge/React-61DAFBp.svg?style=for-the-badge&logo=React&logoColor=black" alt="React" />
<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=for-the-badge&logo=HTML5&logoColor=white" alt="HTML5" />
<img src="https://img.shields.io/badge/Prettier-F7B93E.svg?style=for-the-badge&logo=Prettier&logoColor=black" alt="Prettier" />
<img src="https://img.shields.io/badge/esbuild-FFCF00.svg?style=for-the-badge&logo=esbuild&logoColor=black" alt="esbuild" />

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
- [🔮 Feautres](#-feautres)
  - [Distinctive Features](#distinctive-features)
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

The assistant-chat-gpt GitHub project is a powerful tool for creating voice-controlled assistants that utilize the OpenAI ChatGPT platform. It enables users to set a trigger phrase, language, and voice, as well as customize the background and text colors of the interface. Additionally, the project allows users to test their voice and retrieve conversation history. Overall, this project provides a valuable tool for creating a personalized voice assistant that can easily interact with users in many different languages.

---

## 🔮 Feautres

### Distinctive Features

1. **User-Centered Design Elements:** The project provides a user-friendly experience through its customizable background and text colors, providing options for both a light and dark theme. Additionally, it includes animation and styling for buttons and other elements, as well as support for a dark mode.
2. **Architecture:** The project uses a variety of code scripts to provide a comprehensive solution. It utilizes HTML, JavaScript, CSS, images, and manifest files, as well as React and ReactDOM libraries. It also contains scripts for background, popup, content, audio, fetch-sse, app.css, info, index, and stream-async-iterable. 
3. **ChatGPT Platform Support:** The project supports the OpenAI ChatGPT platform, allowing for conversational interactions with the assistant. It allows the user to customize the trigger phrase, language, voice, and filler words in order to communicate with the ChatGPT. 
4. **Data Storage:** The project includes a code script that provides a way to store and retrieve data in a database using a unique identifier. It utilizes a key-value store to assign each data entry a unique identifier, allowing for easy access and manipulation of the data.
5. **Testing Functionality:** The project provides a way to test the voice, retrieve history, and prevent the page from closing. It uses the uuidv4 library to generate unique ids, and the fetchSSE library to make requests. 
6. **Components:** The project includes components such as the TriggerInput, Popup, Callout, Info, VoiceDropdown, and Settings components, which provide the user with a comprehensive and interactive UI experience.

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

| File      | Summary                                                                                                                    | Module                   |
|:----------|:---------------------------------------------------------------------------------------------------------------------------|:-------------------------|
| index.mjs | This script adds a listener that logs'onStartup' when the Chrome runtime starts and opens the Chrome runtime options page. | src/background/index.mjs |

</details>

<details closed><summary>Components</summary>

| File              | Summary                                                                                                                                                                                                                                                                                                                                                                                        | Module                           |
|:------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------|
| TriggerInput.jsx  | This code script implements a React component that contains an input field where the user can set a trigger phrase. When the phrase is changed, the new value is passed to the setTriggerPhrase function.                                                                                                                                                                                      | src/components/TriggerInput.jsx  |
| Popup.jsx         | This code script renders a message list in React that displays a welcome message followed by a chronological list of messages from the user and the assistant. It sends a request to the chrome runtime to get the history of messages and updates accordingly with a new message every second.                                                                                                | src/components/Popup.jsx         |
| Callout.jsx       | This script imports the React library and exports a Callout function that takes a'type' and'children' as parameters, and returns a div element with a class name of'callout' plus the type parameter.                                                                                                                                                                                          | src/components/Callout.jsx       |
| Info.jsx          | ChassistantGPT is a voice assistant that utilizes the ChatGPT platform. It supports 60+ languages and dialects, and can be triggered by voice command("Hey girl") or by pressing Ctrl/Cmd + Shift + E. It provides audio feedback and displays conversation history. No data is stored or transmitted from the device.                                                                         | src/components/Info.jsx          |
| VoiceDropdown.jsx | This script imports React, useState and useEffect from the React library, as well as a setVoice and testVoice function from another library. It then renders a VoiceDropdown component which contains a select menu to choose a voice or language, and a test button to test the selected voice. Upon selection, the setVoice function is called to update the voice in the background script. | src/components/VoiceDropdown.jsx |
| Settings.jsx      | This code script uses React to create a toggle setting with a label for natural conversation. The toggle can be used to set the value of a "filler" variable, and the corresponding function setFillerEnabled is triggered upon a change in the toggle state.                                                                                                                                  | src/components/Settings.jsx      |

</details>

<details closed><summary>Content</summary>

| File                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                     | Module                                |
|:--------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------|
| index.html                | This code script contains HTML, CSS and JavaScript elements to create a web page with customizable background and text colors, as well as styles for success, warning, info and error messages. It also includes animation and styling for buttons and other elements. Additionally, support for dark mode is included.                                                                                     | src/content/index.html                |
| audio.mjs                 | This code script provides the functionality to interact with an OpenAI ChatGPT conversation, including setting the trigger phrase, language, voice, and filler words in order to communicate with the ChatGPT. It also provides a way to test the voice, retrieve history, and prevent the page from closing. It uses the uuidv4 library to generate unique ids, and the fetchSSE library to make requests. | src/content/audio.mjs                 |
| fetch-sse.mjs             | This code script provides a function for fetching Server-Sent Events(SSE). It uses'eventsource-parser' to create a parser for reading the events, and'stream-async-iterable' to stream them. It then decodes the events and calls the user-provided'onMessage' callback with the event data.                                                                                                                | src/content/fetch-sse.mjs             |
| app.css                   | This code script provides a way to store and retrieve data in a database using a unique identifier. It utilizes a key-value store to assign each data entry a unique identifier, allowing for easy access and manipulation of the data.                                                                                                                                                                     | src/content/app.css                   |
| info.mjs                  | This code script imports the React and ReactDOM libraries, and renders a component called Info within the HTML element with the ID'root'.                                                                                                                                                                                                                                                                   | src/content/info.mjs                  |
| index.mjs                 | This code script imports info and audio modules from the specified files, allowing for access to their respective functions and data.                                                                                                                                                                                                                                                                       | src/content/index.mjs                 |
| stream-async-iterable.mjs | This code script creates an asynchronous iterable from a given stream by reading the stream with a reader and yielding any values that it finds until the stream is done, after which the reader lock is released.                                                                                                                                                                                          | src/content/stream-async-iterable.mjs |

</details>

<details closed><summary>Popup</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                                                             | Module               |
|:-----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------|
| index.html | This code script defines the colors and styling of an HTML page. The background and text colors are set to a light or dark theme based on the user's preferences. The body font-family, font-size, and margin are also specified. Additionally, the script imports a CSS stylesheet and a JavaScript module, which will be used to render the page. | src/popup/index.html |
| index.mjs  | This script imports the React and ReactDOM libraries, and renders a Popup component in the root element of the DOM.                                                                                                                                                                                                                                 | src/popup/index.mjs  |

</details>

<details closed><summary>Root</summary>

| File      | Summary                                                                                                                                                                                                                             | Module    |
|:----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------|
| build.mjs | This code script deletes and replaces an existing directory, runs an ESBuild to bundle and minify files, and zips them together into a Chrome and Firefox extension. It includes HTML, JavaScript, CSS, images, and manifest files. | build.mjs |

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

