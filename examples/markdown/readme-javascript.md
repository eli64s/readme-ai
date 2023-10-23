<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>ASSISTANT-CHAT-GPT</h1>
<h3>◦ Unlock endless possibilities with Assistant Chat GPT!</h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/esbuild-FFCF00.svg?style=flat-square&logo=esbuild&logoColor=black" alt="esbuild" />
<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=flat-square&logo=JavaScript&logoColor=black" alt="JavaScript" />
<img src="https://img.shields.io/badge/Prettier-F7B93E.svg?style=flat-square&logo=Prettier&logoColor=black" alt="Prettier" />
<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=flat-square&logo=HTML5&logoColor=white" alt="HTML5" />
<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat-square&logo=YAML&logoColor=white" alt="YAML" />

<img src="https://img.shields.io/badge/React-61DAFB.svg?style=flat-square&logo=React&logoColor=black" alt="React" />
<img src="https://img.shields.io/badge/ESLint-4B32C3.svg?style=flat-square&logo=ESLint&logoColor=white" alt="ESLint" />
<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=flat-square&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style=flat-square&logo=JSON&logoColor=white" alt="JSON" />
</p>
<img src="https://img.shields.io/github/license/idosal/assistant-chat-gpt?style=flat-square&color=5D6D7E" alt="GitHub license" />
<img src="https://img.shields.io/github/last-commit/idosal/assistant-chat-gpt?style=flat-square&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/idosal/assistant-chat-gpt?style=flat-square&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/languages/top/idosal/assistant-chat-gpt?style=flat-square&color=5D6D7E" alt="GitHub top language" />
</div>

---

## 📖 Table of Contents
- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [⚙️ Modules](#️-modules)
- [🚀 Getting Started](#-getting-started)
  - [🔧 Installation](#-installation)
  - [🤖 Running assistant-chat-gpt](#-running-assistant-chat-gpt)
  - [🧪 Tests](#-tests)
- [🛣 Project Roadmap](#-project-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The repository contains a project called "chassistant-gpt" that provides a browser extension for a voice assistant. The project uses React for building the UI and includes various packages such as'@chatscope/chat-ui-kit-react','esbuild','eslint', and'prettier'. It includes files for background operations, popup UI, and content handling. The code handles audio input and output, speech recognition and synthesis, and makes requests to a chat API for answers. It also includes scripts for building and packaging the extension for Chromium and Firefox browsers.

---

## 📦 Features

|    | Feature            | Description                                                                                                        |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The codebase follows a modular architectural pattern with separate directories for background, components, and content. The code utilizes React for building the UI components. Limit your response to a maximum of 200 characters.             |
| 📄 | **Documentation**  | The repository includes a README file that provides a basic overview of the project and its dependencies. The codebase itself lacks comprehensive documentation. The README could be improved to include detailed installation and usage instructions. Limit your response to a maximum of 200 characters.|
| 🔗 | **Dependencies**   | The codebase relies on various external libraries and packages such as React, uuid, esbuild, and eslint. It also includes packages for styling, UI components, and communication with external services. Limit your response to a maximum of 200 characters.|
| 🧩 | **Modularity**     | The codebase is organized into separate directories and files for different functionalities, such as background, components, and content. This modular structure allows for easier maintenance and reusability of the code. Limit your response to a maximum of 200 characters.|
| 🧪 | **Testing**        | The codebase does not include any significant testing strategies or tools. This could be improved by implementing unit tests and using testing frameworks such as Jest or React Testing Library. Limit your response to a maximum of 200 characters.       |
| ⚡️  | **Performance**    | The performance of the system would depend on factors such as the browser and hardware being used. However, the codebase does not appear to have any significant performance optimizations. Limit your response to a maximum of 200 characters.|
| 🔐 | **Security**       | The codebase does not have explicit security measures. To enhance security, measures such as input validation, data encryption, and secure communication protocols would need to be implemented. Limit your response to a maximum of 200 characters.|
| 🔀 | **Version Control**| The repository utilizes Git for version control. It includes a GitHub Actions workflow file that automatically triggers a build and release process for the extension when a push event occurs. Limit your response to a maximum of 200 characters.|
| 🔌 | **Integrations**   | The system interacts with the browser's APIs, such as the Speech Recognition and Speech Synthesis API. It also interacts with external services through HTTP requests. Limit your response to a maximum of 200 characters.|
| 📶 | **Scalability**    | The codebase does not appear to have specific scalability measures. To enhance scalability, the system could be designed to handle increased user load and data volume, utilize caching strategies, and employ cloud-based solutions. Limit your response to a maximum of 200 characters.           |

---


## 📂 Repository Structure

```sh
└── ./
    ├── .github/
    │   └── workflows/
    │       └── release.yml
    ├── .prettierrc.yaml
    ├── build.mjs
    ├── package-lock.json
    ├── package.json
    └── src/
        ├── background/
        │   └── index.mjs
        ├── components/
        │   ├── Callout.jsx
        │   ├── Info.jsx
        │   ├── Popup.jsx
        │   ├── Settings.jsx
        │   ├── TriggerInput.jsx
        │   └── VoiceDropdown.jsx
        ├── content/
        │   ├── app.css
        │   ├── audio.mjs
        │   ├── fetch-sse.mjs
        │   ├── index.html
        │   ├── index.mjs
        │   ├── info.mjs
        │   └── stream-async-iterable.mjs
        ├── manifest.json
        └── popup/
            ├── index.html
            └── index.mjs

```

---


## ⚙️ Modules

<details closed><summary>Root</summary>

| File                                                                                          | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ---                                                                                           | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [package-lock.json](https://github.com/idosal/assistant-chat-gpt/blob/main/package-lock.json) | The code represents a directory tree of a project called'chassistant-gpt'. It includes various files and folders such as a package-lock.json file, source code files (in the'src' folder), configuration files, and dependencies. The project uses React for building the UI and includes various packages such as'@chatscope/chat-ui-kit-react','esbuild','eslint', and'prettier'.                                                                                                                            |
| [package.json](https://github.com/idosal/assistant-chat-gpt/blob/main/package.json)           | This package.json file includes dependencies and devDependencies for a project called "chassistant-gpt". It specifies the project's name, version, author, and license. The main script is "background.js" and there are additional scripts for building the project, linting the code, and fixing linting errors. The dependencies include various libraries and packages such as react, react-dom, esbuild, and uuid, while the devDependencies include eslint and prettier for code linting and formatting. |
| [build.mjs](https://github.com/idosal/assistant-chat-gpt/blob/main/build.mjs)                 | The code is responsible for building and packaging a browser extension. It uses esbuild to bundle and minify JavaScript and CSS files. The extension is built for both Chromium and Firefox browsers. The code deletes the old build directory, runs esbuild to generate the bundled files, and then creates zip files for the Chromium and Firefox extensions by including the necessary source files, manifest file, and assets.                                                                             |
| [.prettierrc.yaml](https://github.com/idosal/assistant-chat-gpt/blob/main/.prettierrc.yaml)   | The code provided is a configuration file named ".prettierrc.yaml" that defines the formatting rules for the codebase. It specifies that semicolons should be omitted (semi: false) and that single quotes should be used for strings (singleQuote: true). This configuration helps ensure consistent and uniform code formatting throughout the project.                                                                                                                                                      |

</details>

<details closed><summary>Workflows</summary>

| File                                                                                                | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---                                                                                                 | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [release.yml](https://github.com/idosal/assistant-chat-gpt/blob/main/.github/workflows/release.yml) | The code is a GitHub Actions workflow file named "release.yml" found in the ".github/workflows" directory. It defines a workflow triggered by a push event. The workflow runs on the latest version of Ubuntu and consists of several steps. It checks out the repository, sets up Node.js version 18, installs dependencies, builds the project, and then uses the softprops/action-gh-release action to create a release and generate release notes if the push event includes a tag reference. The release includes the "chrome.zip" file from the "build" directory. |

</details>

<details closed><summary>Src</summary>

| File                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---                                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [manifest.json](https://github.com/idosal/assistant-chat-gpt/blob/main/src/manifest.json) | This code represents the manifest file for a browser extension called "ChassistantGPT." It defines the name, description, version, and icons for the extension. It also specifies commands for stopping playback and toggling voice commands, along with their keybindings. The extension requires host permissions for a specific website and uses a background service worker for handling background tasks. The extension's default popup and icon are specified, along with the options UI page. |

</details>

<details closed><summary>Background</summary>

| File                                                                                         | Summary                                                                                                                                                                                                                                                        |
| ---                                                                                          | ---                                                                                                                                                                                                                                                            |
| [index.mjs](https://github.com/idosal/assistant-chat-gpt/blob/main/src/background/index.mjs) | The code in src/background/index.mjs is responsible for the background operations of the Chrome extension. It registers an event listener on startup that logs a message to the console. It also invokes a function to open the options page of the extension. |

</details>

<details closed><summary>Popup</summary>

| File                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---                                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [index.html](https://github.com/idosal/assistant-chat-gpt/blob/main/src/popup/index.html) | This code represents the index.html file located in the'src/popup' directory. It is an HTML file that defines the structure, styling, and content of a web page. It includes a style section with CSS variables and media queries for different color schemes. The body of the page contains a main element with a fixed height and width, as well as a container div that houses an app div. It also includes a script tag that imports the index.js file. |
| [index.mjs](https://github.com/idosal/assistant-chat-gpt/blob/main/src/popup/index.mjs)   | The code in the file `index.mjs` in the `src/popup` directory is importing the `React` and `ReactDOM` libraries. It then uses `ReactDOM.createRoot` to render the `Popup` component from the `../components/Popup` file onto the element with the ID "app" in the HTML document.                                                                                                                                                                            |

</details>

<details closed><summary>Content</summary>

| File                                                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---                                                                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [index.html](https://github.com/idosal/assistant-chat-gpt/blob/main/src/content/index.html)                               | The code is an HTML file that defines the styling and structure of a web page. It sets global CSS variables for different color schemes, defines the layout and styling for various elements such as headings, paragraphs, callouts, buttons, and containers. It also includes a script tag to load the JavaScript code from the "index.js" file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [audio.mjs](https://github.com/idosal/assistant-chat-gpt/blob/main/src/content/audio.mjs)                                 | The code in the `audio.mjs` file is responsible for handling audio input and output in a web application. It imports the `uuid` library for generating unique identifiers and the `fetchSSE` function from another file `fetch-sse.mjs`. The code sets up a speech recognition instance using the `webkitSpeechRecognition` API and configures it to recognize English language speech continuously. It also sets up a speech synthesis instance using the `SpeechSynthesisUtterance` API for converting text to speech.The code exports functions related to audio processing, such as setting the voice, setting the trigger phrase, enabling/disabling filler words, and testing the voice. It also exports functions for obtaining an access token and making requests to a chat API for getting answers to questions.The code includes event listeners to start/stop the speech recognition, process audio input, and handle errors. It also includes functions to handle audio playback and manipulate the application icon.Overall, the code provides a way to process audio input, convert it to text, and generate appropriate audio output based on the application's logic. |
| [fetch-sse.mjs](https://github.com/idosal/assistant-chat-gpt/blob/main/src/content/fetch-sse.mjs)                         | The code in the file `fetch-sse.mjs` is importing the `createParser` function from the `eventsource-parser` library and the `streamAsyncIterable` function from the `stream-async-iterable.mjs` file. It exports an asynchronous function called `fetchSSE` that takes in a `resource` and `options` parameter. Inside the `fetchSSE` function, it extracts the `onMessage` property from the `options` object, and then makes a fetch request to the `resource` with the provided `fetchOptions`. It creates a parser using the `createParser` function, and sets up an event listener for `event` type messages. Once the fetch response is obtained, it iterates over the response body using the `streamAsyncIterable` function. For each chunk received, it decodes the chunk as a string and feeds it to the parser. If the event from the parser is of type'event', it calls the `onMessage` function with the data from the event.                                                                                                                                                                                                                                             |
| [app.css](https://github.com/idosal/assistant-chat-gpt/blob/main/src/content/app.css)                                     | The code represents the CSS file for the application's content section. It is located within the `src/content` directory and is named `app.css`. This file is responsible for styling the visual appearance of the application's content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [info.mjs](https://github.com/idosal/assistant-chat-gpt/blob/main/src/content/info.mjs)                                   | The code in "info.mjs" imports React and ReactDOM libraries to render the Info component using React's createRoot method. It retrieves the element with the ID "root" from the HTML document and renders the Info component on it.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [index.mjs](https://github.com/idosal/assistant-chat-gpt/blob/main/src/content/index.mjs)                                 | The code imports two modules `info.mjs` and `audio.mjs` from the `src/content` directory. These modules likely contain functionality related to information and audio processing respectively.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [stream-async-iterable.mjs](https://github.com/idosal/assistant-chat-gpt/blob/main/src/content/stream-async-iterable.mjs) | The code in `src/content/stream-async-iterable.mjs` provides a function `streamAsyncIterable` that accepts a `stream` as input. It asynchronously iterates over the stream and yields values as they become available. It uses the `getReader` method to obtain a reader for the stream, and then reads values from it using the `read` method. If the reader indicates that it's done, the function returns. Otherwise, it yields the value obtained from the reader. Finally, it releases the lock on the reader to clean up resources.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

</details>

<details closed><summary>Components</summary>

| File                                                                                                         | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---                                                                                                          | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [TriggerInput.jsx](https://github.com/idosal/assistant-chat-gpt/blob/main/src/components/TriggerInput.jsx)   | This code defines a React component called "TriggerInput". It imports a function called "setTriggerPhrase" from a file called "audio.mjs" within the "content" directory. The component renders a div containing a label and an input field. The value of the input field is set to a state variable called "trigger", which is initially set to "Hey girl". When the user types in the input field, the "handleChange" function is called, which updates the "trigger" state and calls the "setTriggerPhrase" function with the new value. |
| [Popup.jsx](https://github.com/idosal/assistant-chat-gpt/blob/main/src/components/Popup.jsx)                 | The code is a React component in the `Popup.jsx` file. It renders a chat interface using `@chatscope/chat-ui-kit-react`. The component uses `useRef`, `useEffect`, and `useState` hooks to handle the chat history and scroll behavior. It fetches the chat history from a background script using the `chrome.runtime.sendMessage` method and updates the state with the received history. The chat history is then displayed in the chat interface.                                                                                       |
| [Callout.jsx](https://github.com/idosal/assistant-chat-gpt/blob/main/src/components/Callout.jsx)             | The code consists of a React component called Callout.jsx. It imports the React library and exports a function component called Callout. The component takes in two props: type and children. It returns a div element with the className set to "callout" concatenated with the value of the type prop. The children prop is rendered inside the div element. This component can be used to render different types of callouts in a React application.                                                                                     |
| [Info.jsx](https://github.com/idosal/assistant-chat-gpt/blob/main/src/components/Info.jsx)                   | The code represents a React component called Info.jsx, which serves as the main information page for a voice assistant called ChassistantGPT. The component renders various sections including a welcome message, status information (including microphone access), settings options, instructions on how to use the voice assistant, privacy details, and more. The component also includes a function to check if the browser being used is Chrome.                                                                                       |
| [VoiceDropdown.jsx](https://github.com/idosal/assistant-chat-gpt/blob/main/src/components/VoiceDropdown.jsx) | The code describes a React component called "VoiceDropdown" that renders a dropdown menu of available voices for text-to-speech functionality. The component fetches the voices asynchronously using the Web Speech API when the component mounts, and updates the dropdown options accordingly. The component also allows the user to select a voice and test it with a button click.                                                                                                                                                      |
| [Settings.jsx](https://github.com/idosal/assistant-chat-gpt/blob/main/src/components/Settings.jsx)           | The `Settings.jsx` file defines a React component called `Settings` that allows users to toggle a setting for natural conversation. It imports functions from the `audio.mjs` file to set the state of the natural conversation setting and updates its value based on user input using the `Toggle` component from the `react-toggle` library. The component renders a toggle switch and a label for the natural conversation setting.                                                                                                     |

</details>

---

## 🚀 Getting Started

***Dependencies***

Please ensure you have the following dependencies installed on your system:

`- ℹ️ Dependency 1`

`- ℹ️ Dependency 2`

`- ℹ️ ...`

### 🔧 Installation

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

### 🤖 Running assistant-chat-gpt

```sh
node app.js
```

### 🧪 Tests
```sh
npm test
```

---


## 🛣 Project Roadmap

> - [X] `ℹ️  Task 1: Implement X`
> - [ ] `ℹ️  Task 2: Implement Y`
> - [ ] `ℹ️ ...`


---

## 🤝 Contributing

[**Discussions**](https://github.com/idosal/assistant-chat-gpt/discussions)
  - Join the discussion here.

[**New Issue**](https://github.com/idosal/assistant-chat-gpt/issues)
  - Report a bug or request a feature here.

[**Contributing Guidelines**](https://github.com/idosal/assistant-chat-gpt/blob/main/CONTRIBUTING.md)

- Contributions are welcome! Please follow these steps:

1. Fork the project repository to your GitHub account.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive such as `new-feature-x` or `bugfix-issue-x`.
```sh
git checkout -b new-feature-x
```
4. Develop your changes locally.
5. Commit your updates with a clear explanation of the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub.
```sh
git push origin new-feature-x
```
7. Create a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
8. Once your pull request is reviewed, it will be merged into the main branch of the project repository.

---

## 📄 License


This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 👏 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#Top)

---
