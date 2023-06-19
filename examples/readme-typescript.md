
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
ChatGPT-App-React-Native-TypeScript
</h1>
<h3>◦ Chat smarter, not harder with ChatGPT!</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=for-the-badge&logo=JavaScript&logoColor=black" alt="JavaScript" />
<img src="https://img.shields.io/badge/Nodemon-76D04B.svg?style=for-the-badge&logo=Nodemon&logoColor=white" alt="Nodemon" />
<img src="https://img.shields.io/badge/React-61DAFB.svg?style=for-the-badge&logo=React&logoColor=black" alt="React" />
<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white" alt="OpenAI" />
<img src="https://img.shields.io/badge/TypeScript-3178C6.svg?style=for-the-badge&logo=TypeScript&logoColor=white" alt="TypeScript" />

<img src="https://img.shields.io/badge/Expo-000020.svg?style=for-the-badge&logo=Expo&logoColor=white" alt="Expo" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="Markdown" />
<img src="https://img.shields.io/badge/Express-000000.svg?style=for-the-badge&logo=Express&logoColor=white" alt="Express" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white" alt="JSON" />
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

The ChatGPT-App-React-Native-TypeScript project is a messaging app that leverages OpenAI's GPT-3 model to generate automated responses. The app allows users to send and receive messages in a chat interface, which can be styled using custom components and layout options. The project provides a robust codebase that implements best practices in React Native development, including the use of TypeScript, a React context, and custom hooks to manage state and API calls. Overall, the project offers a valuable solution for automating messaging workflows and can be customized to suit different use cases.

---

## ⚙️ Features

Feature | Description |
|-----|-----|
| **🏗 Architecture** | The codebase follows a client-server architecture, with the React Native application acting as the client and the Node.js server serving as the backend. The frontend uses the context API and state management to manage user input and fetch chat messages from the server via API requests. The server uses Express.js to handle incoming requests, fetches data from OpenAI's GPT-3 model, and responds with JSON data. |
| **📑 Documentation** | The codebase includes detailed documentation in the form of comments and README files to guide developers on how to set up and use the application. Additionally, the code uses TypeScript interfaces and type definitions for enhanced documentation and type checking. |
| **🧩 Dependencies** | The codebase uses a variety of third-party dependencies, including @react-navigation/native for navigation, Axios for HTTP requests, dotenv for environment variables, and OpenAI API for language processing. The use of these dependencies enhances the functionality and modularity of the codebase. |
| **♻️ Modularity** | The codebase is modular, with each component or module responsible for performing a specific task. The use of TypeScript interfaces, context API, and custom hooks promotes code reuse and maintainability. Additionally, the separation of the server and client-side code further enhances modularity and maintainability. |
| **✔️ Testing** | The codebase does not include any unit tests or automated testing scripts. Implementing tests would greatly enhance code reliability and maintainability. |
| **⚡️ Performance** | The React Native frontend uses the FlatList component to display chat messages, which optimizes performance by only rendering the visible elements on the screen. Additionally, the use of async/await and Axios for HTTP requests provides efficient data fetching. However, the use of the OpenAI API to process natural language may have a performance impact on the server. |
| **🔒 Security** | The codebase does not implement any security measures such as authentication or data encryption. Transmitting data over HTTP instead of HTTPS also poses a security risk. Implementing security measures would greatly enhance the overall security of the application. |
| **🔀 Version Control** | The codebase is version-controlled using Git, with detailed commit messages that provide insight into the changes made to the codebase. The use of branches also enhances collaboration and ensures code stability. However, the absence of a.gitignore file increases the risk of sensitive data being uploaded to the repository. |
| **🔌 Integrations** | The codebase integrates with the OpenAI API to process natural language and Express.js to handle incoming requests. The use of these integrations enhances the functionality and performance of the application. |
| **📈 Scalability** | The codebase is designed to be scalable, with the server handling incoming requests asynchronously and returning data in a structured JSON format. Additionally, the use of

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

| File             | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Module                      |
|:-----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------|
| InputMessage.tsx | The provided code snippet is a React functional component that renders an input field and a send button. When the send button is pressed, the input text is sent to a context provider using a unique ID generated by the'react-uuid' package and other relevant data. The component also defines the styling of the input field and send button using the'StyleSheet' component from React Native.                                                                          | components/InputMessage.tsx |
| Layout.tsx       | This code snippet defines a React Native component called Layout that renders a View container with specific style properties. It also sets a StatusBar with a specified background color and bar style. The Layout component takes in children as props to be rendered within the container.                                                                                                                                                                                | components/Layout.tsx       |
| Message.tsx      | The provided code snippet defines a "Message" component in React Native that displays a message with an avatar, message text, author name, and a copy-to-clipboard function when the message is pressed. The component's styling is determined by the message sender's name, with different colors and alignment for "you" versus other senders. The component imports necessary modules including Clipboard and defines TypeScript type definitions for the message object. | components/Message.tsx      |
| ListMessage.tsx  | This code snippet is a React Native component that renders a list of messages fetched from a remote API using the `useFetchMessage` hook. The component also utilizes the `useContext` hook to get input from a context provider and displays the messages in a `FlatList`. Additionally, the component has a refresh feature that clears the messages displayed when the user pulls down the list.                                                                          | components/ListMessage.tsx  |

</details>

<details closed><summary>Constants</summary>

| File         | Summary                                                                                                                                                                                                                                                                                                            | Module                 |
|:-------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------|
| constants.ts | The code snippet exports a constant variable named API_URL that contains the URL pointing to a local server running on port 3000. The IP address used (10.0.2.2) is commonly used for android emulators to access the host machine's localhost. This constant can be imported and used in other parts of the code. | constants/constants.ts |

</details>

<details closed><summary>Context</summary>

| File             | Summary                                                                                                                                                                                                                                                                                                                                                                             | Module                   |
|:-----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------|
| DataProvider.tsx | This code snippet defines a React context called DataContext that wraps around the provided children components. The DataProvider component is responsible for managing the state of a text input field and exposing it through the context to other components that need it. The use of useState hook and MessageType type ensure type safety and maintainability in the codebase. | context/DataProvider.tsx |

</details>

<details closed><summary>Helpers</summary>

| File          | Summary                                                                                                                                                                                                                                                                                 | Module                |
|:--------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
| getMessage.ts | This code exports a function called getMessage that takes a string argument'message'. The function sends a POST request to an API endpoint and returns a Promise that resolves with data of type MessageType. The request body contains a model, message, max_tokens and a temperature. | helpers/getMessage.ts |

</details>

<details closed><summary>Hooks</summary>

| File               | Summary                                                                                                                                                                                                                                                                                                                                                                                                                         | Module                   |
|:-------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------|
| useFetchMessage.ts | This code exports a custom React hook called `useFetchMessage`, which takes a message as an argument and returns a state object containing the message data and a loading flag. It uses the `useState` and `useEffect` hooks to manage state and perform an asynchronous API call using the `getMessage` helper function. If an empty message is provided, the hook returns an empty object and sets the loading flag to false. | hooks/useFetchMessage.ts |

</details>

<details closed><summary>Root</summary>

| File    | Summary                                                                                                                                                                                                                                                                                                                                                                                                         | Module   |
|:--------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
| App.tsx | The provided code is a React Native application that uses the `NavigationContainer` and `createNativeStackNavigator` components from the `@react-navigation/native` library to create a navigation system with two screens, `HomeScreen` and `Infomation`. The `DataProvider` component is also implemented, and a `TouchableOpacity` component is used to navigate between the two screens with a touch event. | App.tsx  |

</details>

<details closed><summary>Screens</summary>

| File           | Summary                                                                                                                                                                                                                                                                                                                   | Module                 |
|:---------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------|
| Infomation.tsx | This code defines a component called "Information" which displays a centered text element inside a container view. The view is styled using flexbox properties to ensure it occupies the full width and height of the parent container. The component is exported for use in other parts of the React Native application. | screens/Infomation.tsx |
| HomeScreen.tsx | The provided code snippet is a React Native component that defines the HomeScreen for a messaging app. It imports and renders two custom components: ListMessage for displaying messages and InputMessage for entering new messages. These components are wrapped in a Layout component.                                  | screens/HomeScreen.tsx |

</details>

<details closed><summary>Server</summary>

| File      | Summary                                                                                                                                                                                                                                                                                                                                                                  | Module           |
|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| index.js  | This code provides an API endpoint for a chatbot that communicates with OpenAI's GPT-3 model. The endpoint receives a message and some configuration options as a request payload, sends the message to the model, and returns the model's response as a JSON object. The endpoints use Express.js and the OpenAI API.                                                   | server/index.js  |
| config.js | This code snippet imports the'dotenv' package and uses its'config' method to load environment variables from a '.env' file. It then exports an object that contains two properties-'OPENAI_API_KEY' and'OPENAI_ORGANIZATION'-which map to the corresponding environment variables. This allows other modules to access and use these variables without hard-coding them. | server/config.js |

</details>

<details closed><summary>Types</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                          | Module           |
|:-----------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| types.d.ts | The code provides an interface definition for User and Usage objects, as well as a MessageType object that includes properties such as id, create, model, text, user (which is a User object), and usage (which is a Usage object). These interfaces can be used to define and enforce data types in TypeScript. | types/types.d.ts |

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
