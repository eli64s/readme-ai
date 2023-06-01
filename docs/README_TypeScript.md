
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
ChatGPT-App-React-Native-TypeScript
</h1>
<h3 align="center">📍 Connecting the dots in a chat with ChatGPT!</h3>
<h3 align="center">🚀 Developed with the software and tools below:</h3>

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
- [📍Overview](#overview)
- [🔮 Features](#-features)
- [⚙️ Project Structure](#️-project-structure)
- [💻 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
  - [✅ Prerequisites](#-prerequisites)
  - [💻 Installation](#-installation)
  - [🤖 Using ChatGPT-App-React-Native-TypeScript](#-using-chatgpt-app-react-native-typescript)
  - [🧪 Running Tests](#-running-tests)
- [🛠 Future Development](#-future-development)
- [🤝 Contributing](#-contributing)
- [🪪 License](#-license)
- [🙏 Acknowledgments](#-acknowledgments)

---


## 📍Overview

The ChatGPT-App-React-Native-TypeScript project showcases the potential of React Native and TypeScript for developing robust and versatile mobile apps. With its basic navigation functionality, messaging features, and AI-generated responses, this app can be applied to various real-world scenarios. Enterprises that require secure and efficient communication among their employees and customers can benefit from adopting this project, reducing communication barriers and dependencies on third-party messaging services. From a user perspective, the ChatGPT-App offers a seamless and intuitive messaging experience, eliminating the need for switching between different messaging apps and simplifying communication through the implementation of contextual awareness, user feedback and AI-assisted prompts that encourage meaningful conversation.

---

## 🔮 Features

| Feature | Description |
| --- | --- |
| **Overall Structure and Organization** | The codebase is organized into several directories for easy navigation and readability. Major components, screens, and context providers are placed in the main components directory. Routing components can be found in App.tsx, while API integration and server logic are placed in the server directory. The hook directory holds custom hooks while helper functions go to helpers. This organization provides a clear separation of concerns and readability of code. |
| **Code Documentation** | The code is adequately documented using comments, explaining the purpose of the code and the expected behavior of components and functions. However, the documentation may be more detailed, particularly in custom hooks such as "useFetchMessage." It would be more beneficial if it contains descriptions of all the important parameters, their data type, and possibly side effects and error handling. |
| **Dependency Management** | Dependency management is done through package.json, including libraries such as React, React Native, and Axios for making API requests. All dependencies are up-to-date and are optimized for compatibility with the current version of the code. The code also includes optional devDependencies such as TypeScript, ESlint, and Prettier, which imply certain quality standards to adhere to. |
| **Code Modularity and Reusability** | The code follows React's modularity concept where each component/feature is encapsulated, testable, and independent of the others. The project has many isolated and reusable components, such as Message, InputMessage, and ListMessage. The context provider, DataProvider, and related context such as DataContext can be used to share data across components without restructuring the app. The modular design of the code allows for easy performing op optimization, testing, and easier scaling of the codebase.|
| **Testing and Quality Assurance** | The code has no unit or integration tests, suggesting no automated testing regime. However, the standard adopted for ESlint code quality is high, with adequate formatting and descriptive names offered.|
| **Performance and Optimization** | Loading indicators are displayed as requests are loading, optimizing the application's user experience. The use of 'react-native-code-push' allows for faster addressing of bugs, optimization, and continuous deployment. Continuous performance improvements could benefit from developing memory-safe and fast versions of developed code and libraries.|
| **Security Measures** | The code includes the use of environment variables to store API keys, which ensures secure integration with third-party APIs. Current integration uses open API credentials; however, production scenario specifications rely on replacing it with required role-based access control systems taking into account user authorization, authentications and enforced HTTPS support. Verification using third party audits may also hugely benefit app security. |
| **Version Control and Collaboration** | Git is used for version control, with the use of GitHub repository providing visibility and an enablement to collaborative remote development without hinderances. The use of Github workflow helps address quality verification standardized merging preconditions, conflict identification,

---


<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## ⚙️ Project Structure


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

## 💻 Modules

<details closed><summary>Components</summary>

| File             | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Module                      |
|:-----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------|
| InputMessage.tsx | The provided code is an Input component for a messaging feature, allowing users to input and send messages. The component uses React hooks such as useState and useContext to manage state and data, and it includes validation to prevent empty messages from being sent. The component is styled using StyleSheet to provide a cohesive and sleek view.                                                                                                                 | components/InputMessage.tsx |
| Layout.tsx       | This is a React Native functional component that provides a basic layout structure for displaying children components within a centered container that has a dark background color. It sets the status bar to have a light content style and a dark background color. Additionally, the container has flexible dimensions and padding for a styled look.                                                                                                                  | components/Layout.tsx       |
| Message.tsx      | This code defines the Message component in a React Native app that displays a message with the name, avatar, and text of a user. It determines whether the message was sent by the current user or another, and formats the display accordingly. Tapping on the message allows the user to copy the message text to the clipboard and displays a Toast notification indicating a successful copy.                                                                         | components/Message.tsx      |
| ListMessage.tsx  | This code exports a component called ListMessage which renders a flat list of messages fetched from a server using the custom hook useFetchMessage. It also listens for updates from a textInput that it gets from the context provided by DataProvider and renders any new incoming messages while allowing the user to refresh the list. The code utilizes useState and useEffect hooks from React as well as FlatList and RefreshControl components from React Native. | components/ListMessage.tsx  |

</details>

<details closed><summary>Constants</summary>

| File         | Summary                                   | Module                 |
|:-------------|:------------------------------------------|:-----------------------|
| constants.ts | Error generating file summary. Exception: | constants/constants.ts |

</details>

<details closed><summary>Context</summary>

| File             | Summary                                                                                                                                                                                                                                                                                                                                                                                                              | Module                   |
|:-----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------|
| DataProvider.tsx | The code snippet defines a DataProvider component and a DataContext context for sharing data across the components. The DataProvider sets up a state for textInput and a function to update it using useState hook and then wraps the children in the DataContext.Provider. The context value contains the textInput state and the setTextInput function, which can be accessed by any component in the application. | context/DataProvider.tsx |

</details>

<details closed><summary>Helpers</summary>

| File          | Summary                                   | Module                |
|:--------------|:------------------------------------------|:----------------------|
| getMessage.ts | Error generating file summary. Exception: | helpers/getMessage.ts |

</details>

<details closed><summary>Hooks</summary>

| File               | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Module                   |
|:-------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------|
| useFetchMessage.ts | The provided code is a custom React hook called "useFetchMessage", which takes in a message input and returns an object containing the message data and a boolean value representing whether the data is still loading or not. The hook uses the "useState" and "useEffect" hooks to manage state and make an asynchronous call to retrieve the message data through the "getMessage" function. If the message input is empty, the hook immediately returns an object with empty data and isLoading set to false. | hooks/useFetchMessage.ts |

</details>

<details closed><summary>Root</summary>

| File        | Summary                                                                                                                                                                                                                                                                                                                                                                                    | Module      |
|:------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------|
| App.tsx     | The code provides basic navigation functionality for a React Native app using the NavigationContainer and NativeStackNavigator imports. It also includes a DataProvider for context and two screens: HomeScreen and Infomation, each with different header options and TouchableOpacity buttons for navigation.                                                                            | App.tsx     |
| .prettierrc | This code snippet provides a set of configuration options for formatting code written in various languages. It includes options for controlling white space, line spacing, indentation, line wrapping, quoting, comma usage, and spacing around brackets and arrow functions. These options can be used in various programming and markup languages, including HTML, CSS, Vue, and others. | .prettierrc |

</details>

<details closed><summary>Screens</summary>

| File           | Summary                                                                                                                                                                                                                                                                                                                                                                         | Module                 |
|:---------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------|
| Infomation.tsx | Error generating file summary. Exception:                                                                                                                                                                                                                                                                                                                                       | screens/Infomation.tsx |
| HomeScreen.tsx | The code belongs to a React Native component that renders a simple interface comprising two child components and wrapped in a parent component called "Layout". The two child components are named "ListMessage" and "InputMessage". "ListMessage" renders a list of previously sent messages, while "InputMessage" renders an input field for typing and sending new messages. | screens/HomeScreen.tsx |

</details>

<details closed><summary>Server</summary>

| File      | Summary                                                                                                                                                                                                                                                                                                                                                                 | Module           |
|:----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| index.js  | The provided code snippet sets up an Express server that uses the OpenAI API to create AI-generated responses to user chat messages. The server listens on port 3000 and sends JSON responses to incoming POST requests made to the "/api/chat" endpoint. The code also sets up CORS to allow cross-origin requests and uses environment variables for API credentials. | server/index.js  |
| config.js | This code uses the'dotenv' package to initialize configuration variables from a local '.env' file. It then exports an object containing two properties,'OPENAI_API_KEY' and'OPENAI_ORGANIZATION', which are retrieved from the process environment variables. These variables are likely used to authenticate access to an OpenAI API.                                  | server/config.js |

</details>

<details closed><summary>Types</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                                                                                         | Module           |
|:-----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| types.d.ts | The code defines two interfaces, User and Usage, which specify the properties of their respective objects. It then exports the MessageType interface, which combines properties from both of these interfaces to describe an object that includes a unique identifier, creation time, message model text, the sending user's name and avatar, and usage data about the message. | types/types.d.ts |

</details>

<hr />

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> `[📌  INSERT-PROJECT-PREREQUISITES]`

### 💻 Installation

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

