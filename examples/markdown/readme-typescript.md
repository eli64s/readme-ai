<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>ChatGPT-App-React-Native-TypeScript
</h1>
<h3>◦ Unleash conversations, powered by ChatGPT!</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style&logo=JavaScript&logoColor=black" alt="JavaScript" />
<img src="https://img.shields.io/badge/Nodemon-76D04B.svg?style&logo=Nodemon&logoColor=white" alt="Nodemon" />
<img src="https://img.shields.io/badge/React-61DAFB.svg?style&logo=React&logoColor=black" alt="React" />
<img src="https://img.shields.io/badge/OpenAI-412991.svg?style&logo=OpenAI&logoColor=white" alt="OpenAI" />
<img src="https://img.shields.io/badge/TypeScript-3178C6.svg?style&logo=TypeScript&logoColor=white" alt="TypeScript" />

<img src="https://img.shields.io/badge/Expo-000020.svg?style&logo=Expo&logoColor=white" alt="Expo" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style&logo=JSON&logoColor=white" alt="JSON" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
<img src="https://img.shields.io/badge/Express-000000.svg?style&logo=Express&logoColor=white" alt="Express" />
</p>
<img src="https://img.shields.io/github/languages/top/Yuberley/ChatGPT-App-React-Native-TypeScript?style&color=5D6D7E" alt="GitHub top language" />
<img src="https://img.shields.io/github/languages/code-size/Yuberley/ChatGPT-App-React-Native-TypeScript?style&color=5D6D7E" alt="GitHub code size in bytes" />
<img src="https://img.shields.io/github/commit-activity/m/Yuberley/ChatGPT-App-React-Native-TypeScript?style&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/license/Yuberley/ChatGPT-App-React-Native-TypeScript?style&color=5D6D7E" alt="GitHub license" />
</div>

---

## 📖 Table of Contents
- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [⚙️ Modules](#modules)
- [🚀 Getting Started](#-getting-started)
    - [🔧 Installation](#-installation)
    - [🤖 Running ChatGPT-App-React-Native-TypeScript](#-running-ChatGPT-App-React-Native-TypeScript)
    - [🧪 Tests](#-tests)
- [🛣 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The ChatGPT-App-React-Native-TypeScript project is a React Native chat application that uses OpenAI's GPT-3 to generate chatbot responses. It provides a user interface for sending and receiving messages, with a list of previous messages and an input field for new messages. The app offers a seamless and interactive chat experience, allowing users to communicate with the chatbot powered by GPT-3.

---

## 📦 Features

| Feature                | Description                           |
| ---------------------- | ------------------------------------- |
| **⚙️ Architecture**     | The codebase follows a typical React Native architecture with components for screens, components, context, hooks, and helpers. It utilizes React Navigation for navigation and React Context API for state management. The server folder contains the Express server for handling API requests to OpenAI's GPT-3 chatbot. The codebase enforces separation of concerns and follows a modular design pattern.    |
| **📃 Documentation**   | The codebase lacks comprehensive documentation. Although some files have comments explaining their purpose, there is no central documentation or README file. Further documentation could improve code understanding and onboarding.    |
| **🔗 Dependencies**    | The codebase relies on external dependencies such as React Native, React Navigation, and the OpenAI API for GPT-3. It also utilizes dotenv for environmental variable management. These libraries allow the codebase to leverage existing functionality and streamline development.    |
| **🧩 Modularity**      | The codebase is well-organized into smaller components, providing separation of concerns and reusability. Each component handles a specific functionality, such as rendering messages, handling user input, or managing data. This modularity enhances code maintainability and flexibility.    |
| **🧪 Testing**          | The codebase does not include any testing strategies or tools. Implementing unit tests, integration tests, or end-to-end tests would improve code reliability and ensure consistent behavior across different devices and scenarios.    |
| **⚡️ Performance**      | The performance of the codebase depends on factors such as the device and network conditions. It communicates with the OpenAI API for chatbot responses, which introduces potential latency. However, the codebase does not exhibit any obvious performance bottlenecks and can be optimized as needed.    |
| **🔐 Security**        | The codebase does not include explicit security measures. However, it is essential to handle user input securely and protect sensitive data when interacting with the OpenAI API. Implementing measures such as input validation, sanitization, and secure communication protocols would enhance security.    |
| **🔀 Version Control** | The codebase is stored in a Git repository hosted on GitHub. The use of version control enables collaboration, change tracking, and easy code rollbacks. However, the codebase lacks a clear version control strategy or branching model, which could benefit development and deployment processes.    |
| **🔌 Integrations**    | The codebase integrates with the OpenAI API for GPT-3 chatbot functionality. It also utilizes React Navigation for handling app navigation. These integrations enhance the capabilities of the app and provide a seamless user experience.    |
| **📶 Scalability**     | The codebase exhibits some scalability considerations. The separation of concerns and modularity allow for easy addition or modification of components. However, specific scalability strategies, such as load balancing or database scaling, are not apparent in the codebase. Adapting to increased user load may require additional implementation and infrastructure adjustments.    |

---


## 📂 Repository Structure


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

## ⚙️ Modules

<details closed><summary>Root</summary>

| File                                                                                         | Summary                                                                                                                                                                                                                                                                              |
| ---                                                                                          | ---                                                                                                                                                                                                                                                                                  |
| [App.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/App.tsx) | This code sets up a React Native app with navigation using React Navigation. It creates a stack navigator with two screens, HomeScreen and Information, and sets the header styles and options for each screen. It also wraps the app with a DataProvider context for managing data. |

</details>

<details closed><summary>Types</summary>

| File                                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                             |
| ---                                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                 |
| [types.d.ts](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/types/types.d.ts) | The code defines the structure of a MessageType object, which represents a message in a chat application. It includes properties for ID, creation timestamp, model used, text content, user information, and usage statistics. The User and Usage interfaces further define the structure of the user and usage data within the MessageType object. |

</details>

<details closed><summary>Context</summary>

| File                                                                                                                   | Summary                                                                                                                                                                                                                                                                                                                                                                                     |
| ---                                                                                                                    | ---                                                                                                                                                                                                                                                                                                                                                                                         |
| [DataProvider.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/context/DataProvider.tsx) | This code defines a DataProvider component using React's Context API. It creates a context object named DataContext and a provider component that wraps its children. The provider component provides a state variable called textInput and a function called setTextInput to update the state. These can be accessed by any components that are descendants of the DataProvider component. |

</details>

<details closed><summary>Constants</summary>

| File                                                                                                             | Summary                                                                                                        |
| ---                                                                                                              | ---                                                                                                            |
| [constants.ts](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/constants/constants.ts) | The code defines the API_URL constant as'http://10.0.2.2:3000', indicating the endpoint for accessing the API. |

</details>

<details closed><summary>Server</summary>

| File                                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                    |
| ---                                                                                                     | ---                                                                                                                                                                                                                                                                                                                                        |
| [index.js](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/server/index.js)   | This code sets up an Express server that handles API requests for a chatbot powered by OpenAI's GPT-3. It uses the OpenAI API to generate responses based on user input, and returns the response along with metadata such as timestamp and user information. The server listens on port 3000 and supports CORS for cross-origin requests. |
| [config.js](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/server/config.js) | This code imports the'dotenv' module to load environment variables from a '.env' file. It exports an object containing the OpenAI API key and organization from the environment variables.                                                                                                                                                 |

</details>

<details closed><summary>Screens</summary>

| File                                                                                                               | Summary                                                                                                                                                                                                                                                                                                                                          |
| ---                                                                                                                | ---                                                                                                                                                                                                                                                                                                                                              |
| [Infomation.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/screens/Infomation.tsx) | This code is a React Native component that renders a simple "Information" view with centered text. It utilizes the `View`, `Text`, and `StyleSheet` components from React Native. The `styles` object defines the style rules for the container, making it flexbox-based and centered. It is exported as the default component for external use. |
| [HomeScreen.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/screens/HomeScreen.tsx) | This code is for the HomeScreen component in a React Native app. It renders a Layout component that contains both the ListMessage and InputMessage components. The ListMessage component displays a list of messages, while the InputMessage component allows users to input new messages.                                                       |

</details>

<details closed><summary>Components</summary>

| File                                                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ---                                                                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [InputMessage.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/components/InputMessage.tsx) | The code defines a React component that allows users to input and send messages. It utilizes React hooks to manage state and Context API for data management. The component renders a text input field and a send button. When the button is pressed, the inputted text is sent as a message object to the data context. The component also applies styling using React Native's StyleSheet.                                                              |
| [Layout.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/components/Layout.tsx)             | The code defines a reusable layout component in React Native. It includes a container view with styling for background color, padding, and alignment. It also adds a status bar with a specified background color and content style. The layout component can wrap other components and render them within the container view.                                                                                                                            |
| [Message.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/components/Message.tsx)           | This code is a React Native component for rendering a chat message. It displays the message text along with the user's name and avatar. The component also provides an option to copy the message text to the clipboard. The styling is based on the user's role in the chat.                                                                                                                                                                             |
| [ListMessage.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/components/ListMessage.tsx)   | This code is responsible for rendering a list of messages in a React Native app. It uses the useState and useEffect hooks to manage the messages state and fetch new messages. The useFetchMessage hook is used to retrieve messages based on a text input. The messages are displayed in a FlatList component, with each message rendered using the Message component. The code also includes a refresh control for pulling to refresh the message list. |

</details>

<details closed><summary>Hooks</summary>

| File                                                                                                                     | Summary                                                                                                                                                                         |
| ---                                                                                                                      | ---                                                                                                                                                                             |
| [useFetchMessage.ts](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/hooks/useFetchMessage.ts) | This code utilizes React's useState and useEffect hooks to fetch a message based on a given input. It returns a state object with the fetched message data and a loading state. |

</details>

<details closed><summary>Helpers</summary>

| File                                                                                                             | Summary                                                                                                                                                                                                                                                   |
| ---                                                                                                              | ---                                                                                                                                                                                                                                                       |
| [getMessage.ts](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/helpers/getMessage.ts) | The code exports a function called getMessage that sends a message to an API for chatbot responses. It includes the message content, model details, and other parameters. The function makes a POST request to the API URL and returns the response data. |

</details>

---

## 🚀 Getting Started

***Dependencies***

Before you begin, ensure that you have the following prerequisites installed:
> - `ℹ️ Requirement 1`
> - `ℹ️ Requirement 2`
> - `ℹ️ ...`

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


## 🛣 Roadmap

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
