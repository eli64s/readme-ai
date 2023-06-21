
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
ChatGPT-App-React-Native-TypeScript
</h1>
<h3>◦ Connect, Collaborate, ChatGPT-Your ultimate communication solution!</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style&logo=JavaScript&logoColor=black" alt="JavaScript" />
<img src="https://img.shields.io/badge/Nodemon-76D04B.svg?style&logo=Nodemon&logoColor=white" alt="Nodemon" />
<img src="https://img.shields.io/badge/React-61DAFB.svg?style&logo=React&logoColor=black" alt="React" />
<img src="https://img.shields.io/badge/OpenAI-412991.svg?style&logo=OpenAI&logoColor=white" alt="OpenAI" />
<img src="https://img.shields.io/badge/TypeScript-3178C6.svg?style&logo=TypeScript&logoColor=white" alt="TypeScript" />

<img src="https://img.shields.io/badge/Expo-000020.svg?style&logo=Expo&logoColor=white" alt="Expo" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
<img src="https://img.shields.io/badge/Express-000000.svg?style&logo=Express&logoColor=white" alt="Express" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style&logo=JSON&logoColor=white" alt="JSON" />
</p>

![GitHub top language](https://img.shields.io/github/languages/top/Yuberley/ChatGPT-App-React-Native-TypeScript?style&color=5D6D7E)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Yuberley/ChatGPT-App-React-Native-TypeScript?style&color=5D6D7E)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/Yuberley/ChatGPT-App-React-Native-TypeScript?style&color=5D6D7E)
![GitHub license](https://img.shields.io/github/license/Yuberley/ChatGPT-App-React-Native-TypeScript?style&color=5D6D7E)
</div>

---

## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [⚙️ Features](#️-features)
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

The ChatGPT-App-React-Native-TypeScript is a messaging application that uses OpenAI's text-davinci-003 to generate responses for user messages. The app features a stack of screens, including a HomeScreen that displays a list of messages and allows users to input new messages, and an Information screen. The app is built with React Native and TypeScript, and it utilizes a context DataProvider to manage the state of the app. Its value proposition lies in its ability to provide a seamless messaging experience with the help of AI-generated responses.

---

## ⚙️ Features

Feature | Description |
|-----|-----|
| **🏗 Architecture** | The codebase follows a standard React Native architecture with a focus on modularity and separation of concerns. It utilizes context and custom hooks to manage state and functionality across various components and screens. The server-side code uses Express to create an API endpoint for the AI chatbot and includes configuration files for environment variables. |
| **📑 Documentation** | The codebase includes README files with instructions on running the app and server, as well as notes on dependencies and environment variables. The code itself includes comments explaining the purpose and functionality of each file and component. However, some of the comments are written in Spanish instead of English which could pose a challenge for non-Spanish-speaking developers. |
| **🧩 Dependencies** | The codebase includes several dependencies, such as React Navigation for screen navigation, Axios for HTTP requests, and OpenAI API for the AI chatbot functionality. The dependencies are managed by npm and listed in the package.json file. |
| **♻️ Modularity** | The codebase is highly modular, with components and screens separated into individual files and folders. The use of context and custom hooks allows for even further modularity and separation of concerns. Each file or folder contains only the necessary code for a specific feature or functionality, making the codebase easy to read and understand. |
| **✔️ Testing** | There is no testing included in the codebase. |
| **⚡️ Performance** | The performance of the app and server largely depend on the performance of the OpenAI API and the internet connection. The use of Axios for HTTP requests and the async/await pattern ensures that the app remains responsive while waiting for server responses. However, more performance optimization could be achieved by implementing features such as lazy loading and memoization of components. |
| **🔒 Security** | The server-side code includes configurable environment variables for API keys and organizations, which is a good practice for securing sensitive information. However, there is no validation or sanitization of user input in the client-side code, which could pose a security risk if the app were exposed to malicious users. |
| **🔀 Version Control** | The codebase uses Git for version control and is hosted on GitHub. Commits are regularly made with clear and descriptive messages, making it easy to track changes and understand the development history of the project. However, some commits are not pushed to the repository, which could make it difficult for other team members to access the latest codebase. |
| **🔌 Integrations** | The codebase includes integration with the OpenAI API for the AI chatbot functionality. The API key and organization are configured using environment variables, allowing for easy integration with other APIs or services. |
| **📈 Scalability** | The use of context and custom hooks makes it easy to add new features and functionality to the app without needing to

---


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

## 🧩 Modules

<details closed><summary>Components</summary>

| File             | Summary                                                                                                                                                                                                                                                                                                                                                                                                                              | Module                      |
|:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------|
| InputMessage.tsx | This code defines a functional component in React Native that displays an input field and a "send" button. When the button is pressed, it creates a new message object with a unique ID, timestamp, text, and user data, and passes it to a context provider for use in the app. The component also includes styling for the input field and button.                                                                                 | components/InputMessage.tsx |
| Layout.tsx       | The provided code snippet defines a React Native component called Layout. It includes a view with some stylings, and a StatusBar component with specific background color and status bar style. This Layout component takes in a child component as a prop and renders it inside the defined view.                                                                                                                                   | components/Layout.tsx       |
| Message.tsx      | The provided code snippet defines a React Native component for rendering chat messages. The component takes a message object as a prop and displays the message text along with the user avatar and name. It also allows the user to copy the message text to the clipboard by clicking on the message. The styling of the component varies based on whether the message was sent by the current user or received from another user. | components/Message.tsx      |
| ListMessage.tsx  | The provided code is a React Native component that renders a list of messages. It uses state and context to fetch and display messages received from a server using a custom hook. The component also includes a refresh control feature and styles the list container.                                                                                                                                                              | components/ListMessage.tsx  |

</details>

<details closed><summary>Constants</summary>

| File         | Summary                                                                                                                                                                                                                                | Module                 |
|:-------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------|
| constants.ts | The provided code snippet exports a constant variable named "API_URL" that has a value of'http://10.0.2.2:3000'. This variable is likely used in an application to specify the URL where the application sends requests to the server. | constants/constants.ts |

</details>

<details closed><summary>Context</summary>

| File             | Summary                                                                                                                                                                                                                                                                                                                                                | Module                   |
|:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------|
| DataProvider.tsx | The code defines a DataContext using the createContext function from React and exports it. It also exports a DataProvider component that takes in children as props and provides the textInput state and setTextInput function to the DataContext. This allows components nested within the DataProvider to access and manipulate the textInput state. | context/DataProvider.tsx |

</details>

<details closed><summary>Helpers</summary>

| File          | Summary                                                                                                                                                                                                                                             | Module                |
|:--------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
| getMessage.ts | This code exports a function that sends a message to an AI chatbot through an API endpoint. It uses the fetch() method to send a POST request, passing in a JSON object as the request body. The response is then parsed and returned as a Promise. | helpers/getMessage.ts |

</details>

<details closed><summary>Hooks</summary>

| File               | Summary                                                                                                                                                                                                                                                                                                                                                                                                                               | Module                   |
|:-------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------|
| useFetchMessage.ts | This code snippet defines a custom React Hook called `useFetchMessage` that fetches a message from an external API using the `getMessage` helper function. It also manages the loading state of the message and returns an object containing the message data and loading status. The hook takes a string parameter representing the message to be fetched and is triggered whenever the message changes due to the `useEffect` hook. | hooks/useFetchMessage.ts |

</details>

<details closed><summary>Root</summary>

| File    | Summary                                                                                                                                                                                                                                                                                           | Module   |
|:--------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
| App.tsx | The provided code snippet is a React Native app that uses the react-navigation library to create a stack of screens. It has two screens, HomeScreen and Infomation, and a button in the header to navigate between them. The app also uses a context DataProvider to manage the state of the app. | App.tsx  |

</details>

<details closed><summary>Screens</summary>

| File           | Summary                                                                                                                                                                                                                                                                                                                              | Module                 |
|:---------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------|
| Infomation.tsx | The provided code is a React Native component that renders a view with centered text reading "Infomation". It also imports and applies a stylesheet with flexbox styling to center the view in the container. The SliderComponent import is unused and unnecessary.                                                                  | screens/Infomation.tsx |
| HomeScreen.tsx | This code snippet is for a HomeScreen component in a React Native app. It imports the Layout, ListMessage, and InputMessage components, and displays these components when rendered. The ListMessage component is used to display a list of messages, while the InputMessage component is used to allow users to input new messages. | screens/HomeScreen.tsx |

</details>

<details closed><summary>Server</summary>

| File      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Module           |
|:----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| index.js  | This code sets up an Express server with CORS enabled and connects to the OpenAI API using an API key and organization specified in the config file. It listens to incoming POST requests on'/api/chat' and sends a prompt to OpenAI's'text-davinci-003' model, generating a response which is then returned as a JSON object. The response includes the generated text, along with metadata such as the model used and the user who initiated the request. | server/index.js  |
| config.js | This code snippet loads environment variables from a.env file using the dotenv library. It exports an object containing two environment variables, OPENAI_API_KEY and OPENAI_ORGANIZATION, which are retrieved from the process.env object. These variables can then be used throughout the application.                                                                                                                                                    | server/config.js |

</details>

<details closed><summary>Types</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                                                                                                                             | Module           |
|:-----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| types.d.ts | The code snippet defines three interfaces, "User" for user details, "Usage" for usage stats, and "MessageType" that combines these interfaces along with information about the message. The "MessageType" interface includes properties such as ID, creation time, message model, message text, user details, and usage stats. This code can be used to create and manage message types in a messaging application. | types/types.d.ts |

</details>

---

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - [ℹ️ Requirement 1]
> - [ℹ️ Requirement 2]
> - [...]

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
