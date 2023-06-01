
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
ChatGPT-App-React-Native-TypeScript
</h1>
<h3 align="center">📍 Connect, Collaborate, and Code with ChatGPT-App!</h3>
<h3 align="center">🚀 Developed with the software and tools below:</h3>

<p align="center">
<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=for-the-badge&logo=JavaScript&logoColor=black" alt="JavaScript" />
<img src="https://img.shields.io/badge/Nodemon-76D04B.svg?style=for-the-badge&logo=Nodemon&logoColor=white" alt="Nodemon" />
<img src="https://img.shields.io/badge/React-61DAFB.svg?style=for-the-badge&logo=React&logoColor=black" alt="React" />
<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white" alt="OpenAI" />
<img src="https://img.shields.io/badge/TypeScript-3178C6.svg?style=for-the-badge&logo=TypeScript&logoColor=white" alt="TypeScript" />

<img src="https://img.shields.io/badge/Expo-000020.svg?style=for-the-badge&logo=Expo&logoColor=white" alt="Expo" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="Markdown" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white" alt="JSON" />
<img src="https://img.shields.io/badge/Express-000000.svg?style=for-the-badge&logo=Express&logoColor=white" alt="Express" />
</p>
</div>

---

## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍Overview](#-overview)
- [🔮 Features](#-features)
- [⚙️ Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🏎💨 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [🪪 License](#-license)
- [📫 Contact](#-contact)
- [🙏 Acknowledgments](#-acknowledgments)

---


## 📍Overview

ChatGPT-App-React-Native-TypeScript is a React Native app that utilizes the OpenAI API to generate chat responses based on user input. The app includes a stack navigator with two screens, HomeScreen and Information. The app's value proposition is its ability to provide users with an AI-powered chat experience that is both customizable and user-friendly. Its purpose is to simplify the process of implementing AI chatbots in mobile applications.

---

## 🔮 Features

Feature | Description |
|---|---|
| **🏗 Overall Structure and Organization** | The codebase follows a typical React Native structure with separate directories for components, screens, and context. The codebase also uses the React Navigation library to create a stack navigator and a custom DataProvider context to manage state. |
| **📝 Code Documentation** | The codebase has minimal inline comments, but file names and directory structure are self-explanatory. |
| **🧩 Dependency Management** | The codebase manages dependencies with npm and uses a package.json file to list dependencies and scripts. |
| **♻️ Code Modularity and Reusability** | The codebase is modular and follows a component-based architecture which allows for easy reuse and extensibility. |
| **✅ Testing and Quality Assurance** | The codebase does not have any automated tests or linting, but it does include error handling for API requests and a 429 error message for rate limiting. |
| **⚡️ Performance and Optimization** | The codebase does not have any notable performance optimizations or lazy loading, but it does use memoization in some components to avoid unnecessary re-renders. |
| **🔒 Security Measures** | The codebase does not have any explicit security measures, but it does include middleware for handling CORS and parsing JSON payloads on the server. |
| **🔄 Version Control and Collaboration** | The codebase uses Git for version control and has a clear commit history with informative commit messages. |
| **🔌 External Integrations** | The codebase integrates with the OpenAI API to generate chat responses based on user input. |
| **📈 Scalability and Extensibility** | The codebase can be easily extended by adding new components or screens, and the use of a custom DataProvider context allows for easy integration of new state management functionality. The server can also be scaled horizontally by deploying it on multiple instances. |

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

| File             | Summary                                                                                                                                                                                                                                                                                                                                                                                      | Module                      |
|:-----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------|
| InputMessage.tsx | This code snippet defines a React component called InputMessage that renders a text input and a send button. When the send button is pressed, it creates a new message object with a unique ID, timestamp, and user information, and updates the message state in the context using the setTextInput function. The component also applies specific styles to the text input and send button. | components/InputMessage.tsx |
| Layout.tsx       | This code provides a layout component that takes in a child component as a prop and renders it within a container view. The container view has specific styling including a background color, padding, and alignment. It also includes a status bar with a specified background color and bar style.                                                                                         | components/Layout.tsx       |
| Message.tsx      | The provided code snippet exports a component called Message that displays a chat message with an avatar, author name, and text. The component has a function to copy the message text to the clipboard on press, along with a toast message indicating that the text has been copied. The styles for the message, text, profile, author, and image are defined using StyleSheet.            | components/Message.tsx      |
| ListMessage.tsx  | The provided code snippet is a React component that displays a list of messages fetched from an API using a custom hook called "useFetchMessage". It uses the "useState", "useContext", and "useEffect" hooks to manage state and side effects. The component renders a FlatList with a RefreshControl and applies some styling using StyleSheet.                                            | components/ListMessage.tsx  |

</details>

<details closed><summary>Constants</summary>

| File         | Summary                               | Module                 |
|:-------------|:--------------------------------------|:-----------------------|
| constants.ts | HTTP 429 error when fetching summary. | constants/constants.ts |

</details>

<details closed><summary>Context</summary>

| File             | Summary                                                                                                                                                                                                                                                                                                                                                           | Module                   |
|:-----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------|
| DataProvider.tsx | This code defines a React context called "DataContext" and a provider component called "DataProvider". The "DataProvider" component uses the "useState" hook to manage the state of a message input field. It passes the state and a setter function to the "DataContext" provider, allowing child components to access and update the message input field state. | context/DataProvider.tsx |

</details>

<details closed><summary>Helpers</summary>

| File          | Summary                                                                                                                                                                                                                                                                                                                                        | Module                |
|:--------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
| getMessage.ts | This code snippet exports a function called "getMessage" which takes in a message string as input. The function sends a POST request to a chat API endpoint with the input message and returns the response data as a Promise. The request body includes various parameters such as the model to use and maximum number of tokens to generate. | helpers/getMessage.ts |

</details>

<details closed><summary>Hooks</summary>

| File               | Summary                                                                                                                                                                                                                                                                                                                                                                           | Module                   |
|:-------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------|
| useFetchMessage.ts | This code snippet exports a custom hook called "useFetchMessage" that takes in a message string and returns a state object with data and isLoading properties. It makes an API call to get the message and updates the state accordingly using the useState and useEffect hooks from React. If the message is empty, it returns an empty data object with isLoading set to false. | hooks/useFetchMessage.ts |

</details>

<details closed><summary>Root</summary>

| File    | Summary                                                                                                                                                                                                                                                                                          | Module   |
|:--------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
| App.tsx | The code snippet is a React Native app that uses the React Navigation library to create a stack navigator with two screens: HomeScreen and Information. The app also uses a DataProvider context. The HomeScreen has a customized header with a button that navigates to the Information screen. | App.tsx  |

</details>

<details closed><summary>Screens</summary>

| File           | Summary                                                                                                                                                                                                                                                                                                                                          | Module                 |
|:---------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------|
| Infomation.tsx | The provided code is a React Native component called "Infomation" that displays a centered text saying "Infomation" within a container using flexbox properties. It imports the necessary components from React Native and exports the Infomation component as a default export. It also uses StyleSheet to create the styles for the container. | screens/Infomation.tsx |
| HomeScreen.tsx | This code defines a HomeScreen component using React and React Native. It imports and renders two custom components: ListMessage and InputMessage, both of which are wrapped in a Layout component. The HomeScreen component is then exported for use in other parts of the application.                                                         | screens/HomeScreen.tsx |

</details>

<details closed><summary>Server</summary>

| File      | Summary                                                                                                                                                                                                                                                                                                                                                                         | Module           |
|:----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| index.js  | The provided code snippet contains an Express server that listens on port 3000 and utilizes the OpenAI API to generate chat responses based on user input. The server accepts POST requests to the'/api/chat' endpoint and responds with a JSON object containing the generated chat response. The server also includes middleware for handling CORS and parsing JSON payloads. | server/index.js  |
| config.js | This code snippet imports the config function from the dotenv library and executes it. It then exports an object containing the environment variables OPENAI_API_KEY and OPENAI_ORGANIZATION, which are retrieved from the process environment variables.                                                                                                                       | server/config.js |

</details>

<details closed><summary>Types</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                                                         | Module           |
|:-----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| types.d.ts | The code defines three interfaces-User, Usage, and MessageType. User interface contains name and avatar of a user, Usage interface contains prompt_tokens, completion_tokens, and total_tokens, and MessageType interface contains id, create, model, text, user, and usage. These interfaces define the structure of their respective objects. | types/types.d.ts |

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

