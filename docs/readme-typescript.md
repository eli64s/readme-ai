
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
ChatGPT-App-React-Native-TypeScript
</h1>
<h3 align="center">📍 Connecting conversations with ChatGPT-App-React Native and TypeScript!</h3>
<h3 align="center">⚙️ Developed with the software and tools below:</h3>

<p align="center">
<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=for-the-badge&logo=JavaScript&logoColor=black" alt="JavaScript" />
<img src="https://img.shields.io/badge/Nodemon-76D04B.svg?style=for-the-badge&logo=Nodemon&logoColor=white" alt="Nodemon" />
<img src="https://img.shields.io/badge/React-61DAFB.svg?style=for-the-badge&logo=React&logoColor=black" alt="React" />
<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white" alt="OpenAI" />
<img src="https://img.shields.io/badge/TypeScript-3178C6.svg?style=for-the-badge&logo=TypeScript&logoColor=white" alt="TypeScript" />

<img src="https://img.shields.io/badge/Expo-000020.svg?style=for-the-badge&logo=Expo&logoColor=white" alt="Expo" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white" alt="JSON" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="Markdown" />
<img src="https://img.shields.io/badge/Express-000000.svg?style=for-the-badge&logo=Express&logoColor=white" alt="Express" />
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
  - [🤖 Using ChatGPT-App-React-Native-TypeScript](#-using-chatgpt-app-react-native-typescript)
  - [🧪 Running Tests](#-running-tests)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The ChatGPT app is a React Native application that enables users to chat with an AI-powered language model. The app utilizes OpenAI's API for generating responses to user messages. The core functionalities of the app include displaying a list of messages, allowing the user to input new messages, and fetching responses via an API endpoint. The app provides a valuable platform for developers to experiment with integrating AI-powered conversation capabilities into their mobile applications.

---

## 💫 Features

Feature | Description |
|---|---|
| **🏗 Structure and Organization** | The codebase follows a component-based architecture with clear separation of concerns and proper naming conventions. It is organized into directories for components, screens, hooks, and context providers to enable easy navigation and maintenance.|
| **📝 Code Documentation** | The code is well-documented with comments and README files explaining its functionalities, dependencies, and setup instructions. It also defines clear interfaces and types to ensure code clarity and readability.|
| **🧩 Dependency Management** | Dependency management is handled using npm and package.json. The codebase makes use of various internal and external libraries such as React, React Native, FontAwesome, and dotenv.|
| **♻️ Modularity and Reusability** | The codebase is modular and reusable, with components and hooks being designed to be easily integrated into other parts of a React Native project. Components such as the InputMessage and ListMessage components can be used in other chat applications as well.|
| **✔️ Testing and Quality Assurance** | Currently, there are no tests included with the codebase. However, the code is structured in a way that makes testing relatively easy, with each component and hook handling a specific task.|
| **⚡️ Performance and Optimization** | The code includes optimization techniques such as using FlatList instead of ScrollView to render messages and utilizing a refresh control to enable the user to clear the message list. The use of memoization and useCallback hooks would further increase performance.|
| **🔒 Security Measures** | The codebase includes a dotenv file to store sensitive data and securely load environment variables into the process.env object. The server also logs input and output messages to enable debugging.|
| **🔄 Version Control and Collaboration** | The codebase is hosted on GitHub, which enables version control and facilitates collaboration. The codebase includes a README file with instructions on how to contribute to the project.|
| **🔌 External Integrations** | The codebase integrates with the OpenAI API to handle chat interactions. It also includes a server that runs on a local IP address and port number.|
| **📈 Scalability and Extensibility** | The codebase is scalable and extensible, with a clear separation of concerns and a modular structure. It would be easy to add features such as user authentication, file sharing, and more chat interaction models.

---


<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## 📂 Project Structure


```bash
repo
├── App.tsx
├── LICENSE
├── README.md
├── app.json
├── assets
│   ├── adaptive-icon.png
│   ├── favicon.png
│   ├── icon.png
│   └── splash.png
├── components
│   ├── InputMessage.tsx
│   ├── Layout.tsx
│   ├── ListMessage.tsx
│   └── Message.tsx
├── constants
│   └── constants.ts
├── context
│   └── DataProvider.tsx
├── data
│   └── messages.ts
├── helpers
│   └── getMessage.ts
├── hooks
│   └── useFetchMessage.ts
├── others
│   └── screen.png
├── package-lock.json
├── package.json
├── screens
│   ├── HomeScreen.tsx
│   └── Infomation.tsx
├── server
│   ├── config.js
│   ├── index.js
│   ├── package-lock.json
│   └── package.json
├── tsconfig.json
└── types
    └── types.d.ts

12 directories, 28 files
```

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 🧩 Modules

<details closed><summary>Components</summary>

| File             | Summary                                                                                                                                                                                                                                                                                                                                                                                                            | Module                      |
|:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------|
| InputMessage.tsx | This code snippet defines the InputMessage component, which allows the user to input text and send a message. It uses React's useState and useContext hooks to manage state, and the FontAwesome component to display a send icon. When the user clicks the send button, a new message object is created and added to the DataContext. The component also defines styling for the input field and send button.     | components/InputMessage.tsx |
| Layout.tsx       | The code exports a React component called Layout, which takes in a children prop as a ReactNode. The component returns a View with a StatusBar and the children passed in as props. The View is styled using the StyleSheet API with specific height, padding, and backgroundColor.                                                                                                                                | components/Layout.tsx       |
| Message.tsx      | The provided code snippet is a React Native component that renders a message bubble with an avatar image, message text, and author name. The message bubble is styled according to whether the user is "you" or another user. The component also provides a copy-to-clipboard functionality for the message text.                                                                                                  | components/Message.tsx      |
| ListMessage.tsx  | The provided code snippet is a React component that displays a list of messages fetched from an API. The component uses state to manage the messages displayed and a context to access the user input. It also utilizes a custom hook to fetch the messages and a refresh control to enable the user to clear the message list. The messages are displayed in a FlatList component with a custom styled container. | components/ListMessage.tsx  |

</details>

<details closed><summary>Constants</summary>

| File         | Summary                                                                                                                                                                                                                                                                       | Module                 |
|:-------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------|
| constants.ts | The code snippet exports a constant variable named API_URL, which is a string containing the URL of a server running on a local IP address (10.0.2.2) and port number 3000. This variable can be used in other parts of the code to specify the location of the server's API. | constants/constants.ts |

</details>

<details closed><summary>Context</summary>

| File             | Summary                                                                                                                                                                                                                                                                                                                                                                            | Module                   |
|:-----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------|
| DataProvider.tsx | The provided code snippet is a React component that exports a `DataContext` and `DataProvider`. The `DataProvider` component defines a `useState` hook that returns a `textInput` object and a `setTextInput` function to update it. The `DataContext.Provider` wraps around child components to provide access to the `textInput` object and `setTextInput` function via context. | context/DataProvider.tsx |

</details>

<details closed><summary>Helpers</summary>

| File          | Summary                                                                                                                                                                                                                                                                                                                            | Module                |
|:--------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
| getMessage.ts | This code exports a function called "getMessage" that takes a message as a parameter. It sends a fetch request to an API endpoint with the message as a payload and returns the response as a promise. The response contains a data object with a generated message based on the input message using a pre-trained language model. | helpers/getMessage.ts |

</details>

<details closed><summary>Hooks</summary>

| File               | Summary                                                                                                                                                                                                                                                                                                                                                                       | Module                   |
|:-------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------|
| useFetchMessage.ts | The provided code snippet is a custom hook called "useFetchMessage" that uses useState and useEffect from React to fetch a message from a helper function based on a provided string input. It returns a state object containing the fetched data and a loading indicator. If the input string is empty, it returns an empty data object and sets the loading state to false. | hooks/useFetchMessage.ts |

</details>

<details closed><summary>Root</summary>

| File    | Summary                                                                                                                                                                                                                                                                                                              | Module   |
|:--------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
| App.tsx | The code snippet imports necessary components and libraries for building a React Native app that includes navigation and state management using a data provider. It sets up a native stack navigator and defines two screens with navigation options. The stack navigator is rendered within a DataProvider wrapper. | App.tsx  |

</details>

<details closed><summary>Screens</summary>

| File           | Summary                                                                                                                                                                                                                                                                                                                                    | Module                 |
|:---------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------|
| Infomation.tsx | The provided code defines a functional component named `Infomation` that simply renders a `<View>` element with the text "Infomation", and applies some styling to center-align the content. The component is exported as a default export, and can be imported and used in other parts of a React Native app.                             | screens/Infomation.tsx |
| HomeScreen.tsx | The provided code defines a HomeScreen component that renders a Layout component with ListMessage and InputMessage components as children. The purpose of these components is to display and handle a list of messages and allow the user to input new messages. The code uses React and React Native libraries for building a mobile app. | screens/HomeScreen.tsx |

</details>

<details closed><summary>Server</summary>

| File      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Module           |
|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| index.js  | This code creates an Express server and uses the OpenAI API to handle chat interactions. The server listens to port 3000 and sends a'Hello World' message at the root endpoint. When a message is received at /api/chat, the OpenAI API generates a response based on the message, model, max_tokens, and temperature provided in the request body, and then returns this response along with additional data such as the created time and user avatar. The server logs the input and output messages. | server/index.js  |
| config.js | The code imports the dotenv library and loads environment variables from a.env file into the process.env object. It exports an object containing the environment variables OPENAI_API_KEY and OPENAI_ORGANIZATION, which can be accessed by other modules in the application. These environment variables are likely required to access the OpenAI API for further development.                                                                                                                        | server/config.js |

</details>

<details closed><summary>Types</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Module           |
|:-----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| types.d.ts | The code snippet defines three interfaces namely User, Usage, and MessageType. The User interface contains the name and avatar properties, the Usage interface contains the prompt_tokens, completion_tokens, and total_tokens properties, and the MessageType interface contains properties such as id, create, model, text, user, and usage that can be used to define a message type in an application. The interfaces help ensure that objects created from them have specific properties with defined types. | types/types.d.ts |

</details>

---

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - [📌  PREREQUISITE-1]
> - [📌  PREREQUISITE-2]
> - ...

### 🖥 Installation

1. Clone the ChatGPT-App-React-Native-TypeScript repository:
```sh
git clone https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript
```

2. Change to the project directory:
```sh
cd ChatGPT-App-React-Native-TypeScript
```

3. Install the dependencies:
```sh
npm install
```

### 🤖 Using ChatGPT-App-React-Native-TypeScript

```sh
npm run build && node dist/main.js
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
