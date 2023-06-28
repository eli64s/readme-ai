
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
ChatGPT-App-React-Native-TypeScript
</h1>
<h3>◦ Unleash your creativity with ChatGPT-App!</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style&logo=JavaScript&logoColor=black" alt="JavaScript" />
<img src="https://img.shields.io/badge/Nodemon-76D04B.svg?style&logo=Nodemon&logoColor=white" alt="Nodemon" />
<img src="https://img.shields.io/badge/React-61DAFB.svg?style&logo=React&logoColor=black" alt="React" />
<img src="https://img.shields.io/badge/OpenAI-412991.svg?style&logo=OpenAI&logoColor=white" alt="OpenAI" />
<img src="https://img.shields.io/badge/TypeScript-3178C6.svg?style&logo=TypeScript&logoColor=white" alt="TypeScript" />

<img src="https://img.shields.io/badge/Expo-000020.svg?style&logo=Expo&logoColor=white" alt="Expo" />
<img src="https://img.shields.io/badge/Express-000000.svg?style&logo=Express&logoColor=white" alt="Express" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style&logo=JSON&logoColor=white" alt="JSON" />
</p>

![GitHub top language](https://img.shields.io/github/languages/top/Yuberley/ChatGPT-App-React-Native-TypeScript?style&color=5D6D7E)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Yuberley/ChatGPT-App-React-Native-TypeScript?style&color=5D6D7E)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/Yuberley/ChatGPT-App-React-Native-TypeScript?style&color=5D6D7E)
![GitHub license](https://img.shields.io/github/license/Yuberley/ChatGPT-App-React-Native-TypeScript?style&color=5D6D7E)
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

The ChatGPT App is a React Native mobile application that allows users to have interactive conversations with an AI language model powered by OpenAI's GPT-3 technology. The app provides a user-friendly interface for sending messages and receiving AI-generated responses. The core functionalities include managing chat messages, navigating between screens, and handling API requests to fetch or send messages. The purpose of the project is to provide a seamless and engaging user experience for interacting with the AI model, enhancing communication capabilities, and showcasing the potential of conversational AI. Overall, the app offers a convenient and novel way for users to access and leverage AI-generated responses in real-time conversations.

---

## ⚙️ Features

| Feature                | Description                           |
| ---------------------- | ------------------------------------- |
| **⚙️ Architecture**    | The codebase follows a modular architecture, separating different functionalities into components and screens. It uses a stack navigation pattern for screen transition. The server-side is implemented using an Express.js server, which handles API requests and communicates with OpenAI's API for generating responses. The client-side is built with React Native and TypeScript, ensuring type safety and scalability. Overall, the architecture allows for easy extensibility and maintainability. |
| **📖 Documentation**   | The codebase lacks comprehensive documentation. While some files have summary comments, the overall documentation is limited. Additional comments and inline explanations could improve the understanding of the codebase for future developers. |
| **🔗 Dependencies**    | The codebase relies on various external libraries such as React, React Native, react-navigation, and axios for client-side development. On the server-side, it utilizes Express.js and dotenv for handling API requests and managing environment variables. The integration with OpenAI's API is significant for generating responses. The codebase includes a package.json file that lists all the dependencies. |
| **🧩 Modularity**      | The codebase demonstrates good modularity by organizing functionality into components and screens. Each component focuses on a specific task, promoting reusability and maintainability. The use of a DataProvider context ensures centralized state management, enhancing the separation of concerns. However, there are opportunities to further modularize specific code sections for improved code clarity and organization. |
| **✔️ Testing**         | There is no explicit testing framework or tests provided in the codebase. Incorporating unit tests, integration tests, and end-to-end tests would enhance the codebase's reliability, correctness, and maintainability. Adding a testing framework like Jest or React Native Testing Library would be beneficial for thorough testing coverage. |
| **⚡️ Performance**     | The codebase appears to handle performance reasonably well. However, without specific performance metrics or details, it is challenging to provide a comprehensive evaluation. To optimize performance further, considerations like code profiling, performance monitoring tools, and caching mechanisms could be implemented. |
| **🔐 Security**        | The codebase does not explicitly address security measures other than fetching messages from an API using POST requests. Depending on the API's implementation, additional security measures may be required, such as input sanitization and data validation for user-generated content, rate limiting to prevent abuse, and secure communication protocols like HTTPS. |
| **🔀 Version Control** | The codebase utilizes Git for version control as shown by the presence of a GitHub repository. However, no explicit version control strategies or tools are mentioned in the repository itself. It would be beneficial to include a clear version control strategy, branching model, and commit guidelines in the project documentation or a version control guide. |
| **🔌 Integrations**    | The codebase

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

<details closed><summary>Root</summary>

| File                                                                                         | Summary                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---                                                                                          | ---                                                                                                                                                                                                                                                                                                                                                                                                              |
| [App.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/App.tsx) | The code snippet sets up the navigation and screens for a React Native app. It uses react-navigation to create a stack navigator with two screens: Home and Information. The Home screen has a custom header with a title and an "About" button that navigates to the Information screen. The Information screen has a custom header with a title. The data for the app is managed using a DataProvider context. |

</details>

<details closed><summary>Types</summary>

| File                                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                                                  |
| ---                                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                                                      |
| [types.d.ts](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/types/types.d.ts) | The code snippet defines interfaces for a user and their message. The MessageType interface includes properties for the message's ID, creation timestamp, model, text content, the user who sent the message, and the usage statistics of the message. These statistics include the number of tokens used for prompting and completion, as well as the total tokens used in the message. |

</details>

<details closed><summary>Context</summary>

| File                                                                                                                   | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---                                                                                                                    | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [DataProvider.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/context/DataProvider.tsx) | The code snippet defines a `DataProvider` component and a corresponding `DataContext` which acts as a global state for the text input. It utilizes the `useState` hook to manage the state. The `DataProvider` component wraps its children with the `DataContext.Provider` and provides the textInput state and setTextInput function as values to its descendant components. This allows the descendants to access and modify the text input state. |

</details>

<details closed><summary>Constants</summary>

| File                                                                                                             | Summary                                                                                                                                                                                                      |
| ---                                                                                                              | ---                                                                                                                                                                                                          |
| [constants.ts](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/constants/constants.ts) | The code snippet provides the API_URL constant, defining the URL address of the API server. This allows easy access and communication with the server for data retrieval or manipulation in the application. |

</details>

<details closed><summary>Server</summary>

| File                                                                                                    | Summary                                                                                                                                                                                                                                                                                                                       |
| ---                                                                                                     | ---                                                                                                                                                                                                                                                                                                                           |
| [index.js](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/server/index.js)   | This code snippet sets up an Express server using Node.js to create an API endpoint. It handles HTTP requests, which include receiving chat messages and using OpenAI's API to generate responses. The generated response is then returned as a JSON object. The code also includes error handling and logging functionality. |
| [config.js](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/server/config.js) | This code snippet initializes the configuration from the.env file and exports key environment variables: OPENAI_API_KEY and OPENAI_ORGANIZATION.                                                                                                                                                                              |

</details>

<details closed><summary>Screens</summary>

| File                                                                                                               | Summary                                                                                                                                                                                                                                                                                                                       |
| ---                                                                                                                | ---                                                                                                                                                                                                                                                                                                                           |
| [Infomation.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/screens/Infomation.tsx) | This code snippet creates a React Native component called "Infomation" that renders a View containing a Text component saying "Infomation". It styles the View container to use flexbox to center its contents vertically and horizontally. This component can be used to display information in a visually appealing manner. |
| [HomeScreen.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/screens/HomeScreen.tsx) | The provided code snippet is a functional React Native component called HomeScreen. It imports and renders three components-Layout, ListMessage, and InputMessage-inside a Layout component. The purpose of this code is to display a list of messages and provide a text input field for sending new messages.               |

</details>

<details closed><summary>Components</summary>

| File                                                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---                                                                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [InputMessage.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/components/InputMessage.tsx) | This code snippet is a React component that renders an input field and a send button for sending messages. It utilizes useState and useContext hooks to handle state and context management respectively. When the send button is pressed, it creates a new message object and updates the context data. The input field and send button have corresponding styles applied to them using StyleSheet.                                                                                                                                                                                                                  |
| [Layout.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/components/Layout.tsx)             | The code snippet defines a React component called Layout that provides a basic app layout. It includes a container View with specific styling, a StatusBar component to control the status bar appearance, and a dynamic children prop to render any child components within the Layout component.                                                                                                                                                                                                                                                                                                                    |
| [Message.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/components/Message.tsx)           | This code snippet defines a React Native component called "Message". It renders a chat message with the author's name and avatar. The message's text can be copied to the clipboard when the user taps on it. The styling includes different backgrounds for messages sent by the user and received from others.                                                                                                                                                                                                                                                                                                      |
| [ListMessage.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/components/ListMessage.tsx)   | The code snippet is a functional component written in JavaScript using React and React Native. It imports necessary modules and contains a `ListMessage` component that renders a list of messages. It utilizes state hooks for managing the list of messages and a context hook for accessing a data provider. It also uses an effect hook for updating the list of messages based on changes in the text input and fetched data. The component renders a `FlatList` to display the messages and includes a refresh control.The code snippet focuses on fetching messages and updating the message list dynamically. |

</details>

<details closed><summary>Hooks</summary>

| File                                                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                                |
| ---                                                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                                    |
| [useFetchMessage.ts](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/hooks/useFetchMessage.ts) | This code snippet is a custom hook called useFetchMessage that handles fetching a message based on the input provided. It uses useState and useEffect hooks to manage the loading state and trigger the message retrieval. The fetch request is made using the getMessage function from a helper file. The hook returns the fetched message data and a loading status. |

</details>

<details closed><summary>Helpers</summary>

| File                                                                                                             | Summary                                                                                                                                                                                                                                                                                                   |
| ---                                                                                                              | ---                                                                                                                                                                                                                                                                                                       |
| [getMessage.ts](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/helpers/getMessage.ts) | This code snippet defines a function named "getMessage" that takes a message as input. It sends a HTTP POST request to an API endpoint, passing the input message and some parameters. It then returns the response data from the API. The said API is used to generate a message using a language model. |

</details>

---

## 🚀 Getting Started

### ✔️ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - `ℹ️ Requirement 1`
> - `ℹ️ Requirement 2`
> - `ℹ️ ...`

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

### 🎮 Using ChatGPT-App-React-Native-TypeScript

```sh
npm run build && node dist/main.js
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
