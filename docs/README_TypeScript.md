
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
ChatGPT-App-React-Native-TypeScript
</h1>
<h3 align="center">📍 TypeScript your way into awesome chat-based apps with ChatGPT!</h3>
<h3 align="center">🚀 Developed with the software and tools below.</h3>
<p align="center">

<img src="https://img.shields.io/badge/TypeScript-3178C6.svg?style=for-the-badge&logo=TypeScript&logoColor=white" alt="TypeScript" />
<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=for-the-badge&logo=JavaScript&logoColor=black" alt="JavaScript" />
<img src="https://img.shields.io/badge/React-61DAFB.svg?style=for-the-badge&logo=React&logoColor=black" alt="React" />
<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white" alt="OpenAI" />

<img src="https://img.shields.io/badge/Nodemon-76D04B.svg?style=for-the-badge&logo=Nodemon&logoColor=white" alt="Nodemon" />
<img src="https://img.shields.io/badge/Express-000000.svg?style=for-the-badge&logo=Express&logoColor=white" alt="Express" />
<img src="https://img.shields.io/badge/Expo-000020.svg?style=for-the-badge&logo=Expo&logoColor=white" alt="Expo" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="Markdown" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white" alt="JSON" />
</p>

</div>

---

## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍Overview](#overview)
- [🔮 Feautres](#-feautres)
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

ChatGPT-App-React-Native-TypeScript is a React Native project that implements the OpenAI GPT-3 API in a mobile chat app. It provides an easy-to-use interface to interact with the OpenAI GPT-3 API and allows users to customize the appearance of the chat window. ChatGPT is perfect for creating demos and experimenting with OpenAI GPT-3 in a mobile environment.

## 🔮 Feautres

> `[📌  INSERT-PROJECT-FEATURES]`

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

| File             | Summary                                                                                                                                                                                                                                                                                                                         | Module                      |
|:-----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------|
| InputMessage.tsx | This code imports React, uuid, FontAwesome, and StyleSheet from React Native, as well as the MessageType and DataContext from other files. It then creates an InputMessage component that allows users to input text and send it as a message with a timestamp, avatar, and other data. The component is then exported for use. | components/InputMessage.tsx |
| Layout.tsx       | This code imports React and React Native components, creates a Layout component which renders a StatusBar with a light-content style and a background color of #222f3e, and applies styling to the container View.                                                                                                              | components/Layout.tsx       |
| Message.tsx      | This code imports React components and types, and creates a Message component that displays a message and allows the user to copy it to their clipboard. It also includes styling for the message, such as background color and font size.                                                                                      | components/Message.tsx      |
| ListMessage.tsx  | This code imports React, React Native, and UUID, as well as components from a data provider and a custom hook, to create a FlatList component that displays a message based on a text input. It also has a refresh control that clears the messages when triggered.                                                             | components/ListMessage.tsx  |

</details>

<details closed><summary>Constants</summary>

| File         | Summary                                                                                                                                  | Module                 |
|:-------------|:-----------------------------------------------------------------------------------------------------------------------------------------|:-----------------------|
| constants.ts | This code exports a constant API_URL with the value of'http://10.0.2.2:3000', which can be used to access a server on the local network. | constants/constants.ts |

</details>

<details closed><summary>Context</summary>

| File             | Summary                                                                                                                                                                                                        | Module                   |
|:-----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------|
| DataProvider.tsx | This code creates a React Context Provider which provides a state object for textInput and a setter function for updating it. It is used to pass down data and functions to components in a React application. | context/DataProvider.tsx |

</details>

<details closed><summary>Helpers</summary>

| File          | Summary                                                                                                                                                             | Module                |
|:--------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
| getMessage.ts | This code is an async function that sends a POST request to an API URL with a message and other parameters as the body, and returns the response data as a promise. | helpers/getMessage.ts |

</details>

<details closed><summary>Hooks</summary>

| File               | Summary                                                                                                                                                                                                                                                        | Module                   |
|:-------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------|
| useFetchMessage.ts | This code uses React's useState and useEffect hooks to fetch a message from an external source, and store the data and loading status in a state object. If an empty message is passed in, the state is set to an empty message and isLoading is set to false. | hooks/useFetchMessage.ts |

</details>

<details closed><summary>Root</summary>

| File        | Summary                                                                                                                                                                                                                                                                                                                                    | Module      |
|:------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------|
| App.tsx     | This code imports React, Text, TouchableOpacity, NavigationContainer, and createNativeStackNavigator from the React Native library, as well as a DataProvider and two screens from a local source. It then creates a stack navigator, and uses it to render the HomeScreen and Infomation screens, each with their own navigation options. | App.tsx     |
| .prettierrc | This code sets formatting preferences for a programming language, including use of single quotes, tab width, trailing commas, and bracket spacing.                                                                                                                                                                                         | .prettierrc |

</details>

<details closed><summary>Screens</summary>

| File           | Summary                                                                                                                                                                                                                                                                 | Module                 |
|:---------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------|
| Infomation.tsx | This code imports the React library, the StyleSheet, Text, View, and SliderComponent from the React Native library, and creates a component called Infomation which displays a Text element when rendered. It also creates a styles object to style the View container. | screens/Infomation.tsx |
| HomeScreen.tsx | This code imports React, useState, Text, View, Layout, ListMessage, and InputMessage components from the React Native library and renders them in a Layout component.                                                                                                   | screens/HomeScreen.tsx |

</details>

<details closed><summary>Server</summary>

| File      | Summary                                                                                                                                                                                                                                                                                                        | Module           |
|:----------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| index.js  | This code imports the Express framework, the CORS library, and the OpenAIApi library to create an application that listens on port 3000 and responds to GET and POST requests. When a POST request is sent, the code will generate a response using OpenAIApi and return a JSON object with the response data. | server/index.js  |
| config.js | This code imports configuration variables from the environment and exports them as environment variables for use in the application.                                                                                                                                                                           | server/config.js |

</details>

<details closed><summary>Types</summary>

| File       | Summary                                                                                                                                                                              | Module           |
|:-----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| types.d.ts | This code defines an interface for a message type that contains the user's name, avatar, prompt tokens, completion tokens, total tokens, message id, creation time, model, and text. | types/types.d.ts |

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

