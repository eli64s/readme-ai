<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>CHATGPT-APP-REACT-NATIVE-TYPESCRIPT</h1>
<h3>◦ Transforming conversations with AI</h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=flat-square&logo=JavaScript&logoColor=black" alt="JavaScript" />
<img src="https://img.shields.io/badge/Nodemon-76D04B.svg?style=flat-square&logo=Nodemon&logoColor=white" alt="Nodemon" />
<img src="https://img.shields.io/badge/React-61DAFB.svg?style=flat-square&logo=React&logoColor=black" alt="React" />
<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=flat-square&logo=OpenAI&logoColor=white" alt="OpenAI" />

<img src="https://img.shields.io/badge/TypeScript-3178C6.svg?style=flat-square&logo=TypeScript&logoColor=white" alt="TypeScript" />
<img src="https://img.shields.io/badge/Expo-000020.svg?style=flat-square&logo=Expo&logoColor=white" alt="Expo" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style=flat-square&logo=JSON&logoColor=white" alt="JSON" />
<img src="https://img.shields.io/badge/Express-000000.svg?style=flat-square&logo=Express&logoColor=white" alt="Express" />
</p>
<img src="https://img.shields.io/github/license/Yuberley/ChatGPT-App-React-Native-TypeScript?style=flat-square&color=5D6D7E" alt="GitHub license" />
<img src="https://img.shields.io/github/last-commit/Yuberley/ChatGPT-App-React-Native-TypeScript?style=flat-square&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/Yuberley/ChatGPT-App-React-Native-TypeScript?style=flat-square&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/languages/top/Yuberley/ChatGPT-App-React-Native-TypeScript?style=flat-square&color=5D6D7E" alt="GitHub top language" />
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
  - [🤖 Running ChatGPT-App-React-Native-TypeScript](#-running-chatgpt-app-react-native-typescript)
  - [🧪 Tests](#-tests)
- [🛣 Project Roadmap](#-project-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The repository contains a React Native application called ChatGPT-App that allows users to have conversations with OpenAI's ChatGPT model. The app includes components for displaying messages, inputting messages, and managing data. It also has a server-side component that handles requests to the ChatGPT API and generates responses. The value proposition of the project is to provide a user-friendly interface for interacting with the ChatGPT model and creating conversational experiences.

---

## 📦 Features

|    | Feature            | Description                                                                                                        |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The codebase follows a typical React Native structure, with components, screens, context, helpers, and hooks folders. The server directory handles API communication. The app utilizes the OpenAI library for chat generation.                                                          |
| 📄 | **Documentation**  | There is no dedicated documentation in the repository. However, comments are present in some files to provide contextual information about their purpose and functionality.                                                        |
| 🔗 | **Dependencies**   | The app relies on various libraries and packages such as React Navigation, Expo, dotenv, express, OpenAI, and more. These dependencies are managed using the package manager npm and are specified in the package.json and package-lock.json files.                 |
| 🧩 | **Modularity**     | The codebase is well-organized into smaller components, making it easy to understand and maintain. Components are designed to be reusable and handle specific functionalities, such as input message, layout, list message, and individual messages.    |
| 🧪 | **Testing**        | There are no explicit testing strategies or tools mentioned in the repository. The absence of test files indicates a lack of standardized testing practices.                                                               |
| ⚡️  | **Performance**    | The performance of the app cannot be accurately assessed based solely on the codebase. Aspects such as speed and resource usage can be influenced by the network connection, server performance, and client device capabilities.                        |
| 🔐 | **Security**       | Security measures are not explicitly addressed in the repository. However, it is essential to ensure proper security practices during server deployment, including securing API keys and protecting against common security vulnerabilities.         |
| 🔀 | **Version Control**| The repository uses Git for version control. No specific version control strategies or tools are mentioned in the codebase.                                                                                                         |
| 🔌 | **Integrations**   | The app interacts with the OpenAI library to generate chat responses based on user messages. It also communicates with the server for sending and fetching messages.                                                                 |
| 📶 | **Scalability**    | Scalability considerations are not explicitly mentioned in the codebase. However, the app's modular structure and use of React Native allow for easier scalability by adding new components, screens, or integrations as the project grows.                  |

---


## 📂 Repository Structure

```sh
└── ./
    ├── App.tsx
    ├── app.json
    ├── components/
    │   ├── InputMessage.tsx
    │   ├── Layout.tsx
    │   ├── ListMessage.tsx
    │   └── Message.tsx
    ├── constants/
    │   └── constants.ts
    ├── context/
    │   └── DataProvider.tsx
    ├── helpers/
    │   └── getMessage.ts
    ├── hooks/
    │   └── useFetchMessage.ts
    ├── others/
    ├── package-lock.json
    ├── package.json
    ├── screens/
    │   ├── HomeScreen.tsx
    │   └── Infomation.tsx
    ├── server/
    │   ├── config.js
    │   ├── index.js
    │   ├── package-lock.json
    │   └── package.json
    ├── tsconfig.json
    └── types/
        └── types.d.ts

```

---


## ⚙️ Modules

<details closed><summary>Root</summary>

| File                                                                                                             | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---                                                                                                              | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [App.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/App.tsx)                     | The code is the main App component of a React Native application. It uses the NavigationContainer and createNativeStackNavigator from react-navigation to set up a stack-based navigation system. The App component renders a DataProvider component to provide data to the app. It also renders two screens, HomeScreen and Infomation, with custom header styles and options. The Infomation screen displays information about the app.                                                                                   |
| [app.json](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/app.json)                   | The code represents the directory structure of a React Native app called "ChatGPT-App" with various components, constants, context, helpers, hooks, screens, and types. The app.json file specifies configuration settings for the app, including its name, version, orientation, icons, splash screen, asset patterns, and platform-specific settings for iOS, Android, and web.                                                                                                                                           |
| [package-lock.json](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/package-lock.json) | This code represents a directory tree structure of a React Native chat application. It consists of various files and folders that make up the project, including components, constants, context, helpers, hooks, screens, server, types, and package configurations. It utilizes libraries like React Navigation, Expo, and React UUID. The package-lock.json file specifies the dependencies and versions used in the project.                                                                                             |
| [package.json](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/package.json)           | The code represents the directory tree and package.json file for a chat application called "chatgpt-app." The directory structure includes various folders such as components, constants, context, helpers, hooks, others, screens, server, and types. Each folder contains relevant files for different functionalities of the chat app. The package.json file specifies the dependencies and devDependencies required for running the app, including libraries like React Navigation, Expo, React Native, and TypeScript. |
| [tsconfig.json](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/tsconfig.json)         | The code provides a directory tree structure that organizes various files for a React Native application. It includes app components, constants, context providers, helpers, hooks, screens, server configuration, TypeScript definitions, and other necessary files. The listed "tsconfig.json" file ensures that strict TypeScript compilation options are in place for the project.                                                                                                                                      |

</details>

<details closed><summary>Types</summary>

| File                                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---                                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [types.d.ts](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/types/types.d.ts) | The code defines an interface called `MessageType` in the file `types/types.d.ts`. This interface describes the structure of a message object, including properties such as `id`, `create`, `model`, `text`, `user`, and `usage`. The `user` property is further defined by the `User` interface, which has properties for `name` and `avatar`. The `usage` property is defined by the `Usage` interface, which has properties for `prompt_tokens`, `completion_tokens`, and `total_tokens`. |

</details>

<details closed><summary>Context</summary>

| File                                                                                                                   | Summary                                                                                                                                                                                                                                                                                                                                                       |
| ---                                                                                                                    | ---                                                                                                                                                                                                                                                                                                                                                           |
| [DataProvider.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/context/DataProvider.tsx) | The code defines a DataProvider component that creates a context called DataContext. It provides the state for managing user input messages using the useState hook. The DataProvider component takes in children as props and renders them as its children, while passing the textInput state and a function to update it to the DataContext.Provider value. |

</details>

<details closed><summary>Constants</summary>

| File                                                                                                             | Summary                                                                                                                                                                                        |
| ---                                                                                                              | ---                                                                                                                                                                                            |
| [constants.ts](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/constants/constants.ts) | The code provides a constant variable named "API_URL" that stores the value "http://10.0.2.2:3000". This variable is likely used as the base URL for API endpoints throughout the application. |

</details>

<details closed><summary>Server</summary>

| File                                                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---                                                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [index.js](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/server/index.js)                   | The code is a server-side application that listens to incoming requests on port 3000. It uses Express.js and handles HTTP requests, including a GET request to the root URL ("/") that returns the response "Hello World!". There is also a POST request ("/api/chat") that accepts a JSON payload containing a message, model, max_tokens, and temperature. The code then uses the OpenAI library to generate a response based on the provided message and returns the generated data as a JSON response. The server also logs the input and output for debugging purposes.           |
| [config.js](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/server/config.js)                 | The code in the file `server/config.js` imports the `config` function from the `dotenv` package and calls it. This function loads environment variables from a `.env` file into `process.env`. The code then exports an object named `environment` which contains two properties: `OPENAI_API_KEY` and `OPENAI_ORGANIZATION`. The values of these properties are assigned using the corresponding environment variables from `process.env`.                                                                                                                                            |
| [package-lock.json](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/server/package-lock.json) | The code represents a directory tree structure of a project. It includes various files and directories such as App.tsx, components, constants, context, helpers, hooks, screens, server, and types. The server/package-lock.json file contains dependencies and devDependencies required for the server component, including body-parser, cors, dotenv, express, morgan, openai, and nodemon.                                                                                                                                                                                          |
| [package.json](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/server/package.json)           | The code defines the package.json file for a server application. It specifies the dependencies and devDependencies required for the server to run. The server uses Express.js framework for handling HTTP requests, body-parser for parsing request bodies, cors for enabling cross-origin resource sharing, morgan for logging HTTP requests, dotenv for managing environment variables, and nodemon for automatically restarting the server during development. The OpenAI library is also a dependency, potentially used for natural language processing or machine learning tasks. |

</details>

<details closed><summary>Screens</summary>

| File                                                                                                               | Summary                                                                                                                                                                                                                                                                                                                                          |
| ---                                                                                                                | ---                                                                                                                                                                                                                                                                                                                                              |
| [Infomation.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/screens/Infomation.tsx) | The code in the file "Infomation.tsx" defines a React Native component called "Infomation". It renders a view containing a text component with the content "Infomation". The view is styled using a style object defined in the "styles" variable, which centers the content vertically and horizontally within the view.                        |
| [HomeScreen.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/screens/HomeScreen.tsx) | The code in the HomeScreen.tsx file imports and renders components from the Layout, ListMessage, and InputMessage files. These components are used within a Layout component and displayed on the home screen. The purpose of this code is to create a user interface for displaying a list of messages and an input field for sending messages. |

</details>

<details closed><summary>Components</summary>

| File                                                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---                                                                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [InputMessage.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/components/InputMessage.tsx) | The code above defines a React component called "InputMessage". It imports necessary dependencies and uses React hooks to manage state. The component receives a text input from the user and sends it as a message by calling a function from the DataContext. It also renders a text input field and a button for sending the message. The component has styles defined using StyleSheet.                             |
| [Layout.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/components/Layout.tsx)             | The code defines the Layout component, which is responsible for rendering the main layout of the application. It includes a container View with custom styles, a StatusBar component, and the children components passed as props. The container has flexbox properties for layout, padding and background color configuration, while the StatusBar sets the background color and bar style of the device's status bar. |
| [Message.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/components/Message.tsx)           | The code in the "Message.tsx" file defines a React Native component called "Message". This component is responsible for rendering a chat message, including the user's name, avatar, and the message text. It also provides a feature to copy the message text to the clipboard when the user taps on it. The component's appearance and styling are defined using CSS-in-JS syntax.                                    |
| [ListMessage.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/components/ListMessage.tsx)   | The code is a React Native component called ListMessage, responsible for rendering a list of messages. It fetches messages from an API based on a user's text input and displays them in a FlatList. The component also handles adding new messages to the list when the user enters text, and it includes a refresh control to clear the message list.                                                                 |

</details>

<details closed><summary>Hooks</summary>

| File                                                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---                                                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [useFetchMessage.ts](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/hooks/useFetchMessage.ts) | The code defines a custom hook called useFetchMessage. It takes in a message as a parameter and returns a state object with data and isLoading properties. Inside the hook, there is a useEffect that calls the loadMessage function whenever the message value changes. The loadMessage function makes an asynchronous call to getMessage, passing the message as an argument. Once the data is fetched, it sets the state with the data and isLoading set to false. If the message is an empty string, the hook returns an empty state object with isLoading set to false. Overall, the code allows for fetching messages based on a given message and manages the state of the data and loading status. |

</details>

<details closed><summary>Helpers</summary>

| File                                                                                                             | Summary                                                                                                                                                                                                                                                                                                                   |
| ---                                                                                                              | ---                                                                                                                                                                                                                                                                                                                       |
| [getMessage.ts](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/helpers/getMessage.ts) | This code is a helper function that sends a message to an API endpoint for chat generation. It accepts a message as input, creates a request body with the message, and makes a POST call to the API URL defined in the constants. The response from the API is then parsed and returned as a Promise of the MessageType. |

</details>

---

## 🚀 Getting Started

***Dependencies***

Please ensure you have the following dependencies installed on your system:

`- ℹ️ Dependency 1`

`- ℹ️ Dependency 2`

`- ℹ️ ...`

### 🔧 Installation

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

### 🤖 Running ChatGPT-App-React-Native-TypeScript

```sh
npm run build && node dist/main.js
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

[**Discussions**](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/discussions)
  - Join the discussion here.

[**New Issue**](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/issues)
  - Report a bug or request a feature here.

[**Contributing Guidelines**](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/CONTRIBUTING.md)

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
