<div align="left">
<h1><img src=https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg width="100" />
<br>CHATGPT-APP-REACT-NATIVE-TYPESCRIPT</h1>
<h3>◦ Unlock the power of code with ease</h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="left">
<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=plastic&logo=JavaScript&logoColor=black" alt="JavaScript" />
<img src="https://img.shields.io/badge/Nodemon-76D04B.svg?style=plastic&logo=Nodemon&logoColor=white" alt="Nodemon" />
<img src="https://img.shields.io/badge/React-61DAFB.svg?style=plastic&logo=React&logoColor=black" alt="React" />
<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=plastic&logo=OpenAI&logoColor=white" alt="OpenAI" />

<img src="https://img.shields.io/badge/TypeScript-3178C6.svg?style=plastic&logo=TypeScript&logoColor=white" alt="TypeScript" />
<img src="https://img.shields.io/badge/Expo-000020.svg?style=plastic&logo=Expo&logoColor=white" alt="Expo" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style=plastic&logo=JSON&logoColor=white" alt="JSON" />
<img src="https://img.shields.io/badge/Express-000000.svg?style=plastic&logo=Express&logoColor=white" alt="Express" />
</p>
<img src="https://img.shields.io/github/license/Yuberley/ChatGPT-App-React-Native-TypeScript?style=plastic&color=5D6D7E" alt="GitHub license" />
<img src="https://img.shields.io/github/last-commit/Yuberley/ChatGPT-App-React-Native-TypeScript?style=plastic&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/Yuberley/ChatGPT-App-React-Native-TypeScript?style=plastic&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/languages/top/Yuberley/ChatGPT-App-React-Native-TypeScript?style=plastic&color=5D6D7E" alt="GitHub top language" />
</div>
<hr>

## 🔗 Quick Links
- [🔗 Quick Links](#-quick-links)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [🧩 Modules](#modules)
- [🚀 Getting Started](#-getting-started)
    - [⚙️ Installation](#-installation)
    - [🤖 Running ChatGPT-App-React-Native-TypeScript](#-running-ChatGPT-App-React-Native-TypeScript)
    - [🧪 Tests](#-tests)
- [🚧 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

The code repository contains a React Native TypeScript application for a chat app powered by ChatGPT. It includes components such as InputMessage, Layout, ListMessage, and Message for rendering the chat interface, as well as a DataProvider for managing state. The repository also has server-side files for handling HTTP requests and interacting with the OpenAI API. The codebase has configuration files like app.json and tsconfig.json. It utilizes various dependencies and packages, including express, react-native-screens, react-navigation, react-uuid, and expo. The repository structure is well-organized with separate directories for components, screens, helpers, and more.

---

## 📦 Features

|    | Feature            | Description                                                                                                        |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The ChatGPT-App-React-Native-TypeScript repository follows a typical React Native architecture pattern with components, screens, helpers, hooks, and a server directory. It uses a stack navigator for navigation and organizes components into reusable modules. The app communicates with a server to fetch and send messages. The server uses the Express.js framework and relies on the OpenAI API for chat completions. The codebase shows a clear separation of concerns, separating UI components, data handling logic, and server communication.    |
| 📄 | **Documentation**  | The documentation in the repository appears to be limited. Some files have code comments, providing explanations for certain code snippets, but overall, the documentation is not comprehensive. More documentation, especially regarding the file structure and the purpose of each file, would greatly enhance the developer experience.    |
| 🔗 | **Dependencies**   | The repository has several dependencies. It relies on React Native, Expo, and related libraries for building mobile apps. @react-navigation/native-stack is used for navigation, and @react-navigation/native is used for providing navigation context. It uses axios and express for server communication. Other dependencies include react-uuid, react-native-safe-area-context, react-native-screens, react-native-web, etc. Additionally, it uses the OpenAI API for chat completions.    |
| 🧩 | **Modularity**     | The repository demonstrates modularity by organizing the codebase into separate directories for components, screens, context, helpers, hooks, constants, and types. Each directory contains related files, making it easier to navigate and maintain. Components are modular and reusable, focusing on individual UI elements. The use of a data provider context (DataProvider.tsx) shows a separation of data management from UI components. Overall, the codebase has a good level of modularity.    |
| 🧪 | **Testing**        | The repository does not contain any explicit testing code or test files. Adding tests using frameworks like Jest and React Native Testing Library would greatly enhance the codebase's reliability and maintainability. The absence of tests is a drawback that should be addressed for long-term project stability.    |
| ⚡️  | **Performance**    | Analyzing performance aspects of the repository based only on the code files is challenging. However, the codebase seems to follow React Native best practices, such as using FlatList for efficient rendering of the list of messages and optimizing UI updates. The use of React's useState and useEffect hooks indicates a focus on efficient state management. However, without performance measurement and profiling, it is challenging to provide a comprehensive analysis of the system's performance.    |
| 🔐 | **Security**       | The repository demonstrates basic security measures. The Express.js server appears to handle HTTP requests securely. It uses dotenv to load sensitive environment variables from a config file. However, a more detailed analysis of security measures would require deeper inspection of the server implementation, such as input validation, authentication, and authorization mechanisms. Additionally, handling the OpenAI API securely is important to protect user data and ensure the AI model's integrity.    |
| 🔀 | **Version Control**| The repository does not provide any explicit information regarding version control strategies and tools used. However, it is common practice to use Git for version control

---

## 📂 Repository Structure

```sh
└── ChatGPT-App-React-Native-TypeScript/
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


## 🧩 Modules

<details closed><summary>.</summary>

| File                                                                                                             | Summary                                                                                                                                                                                                                                                                                                                                                                          |
| ---                                                                                                              | ---                                                                                                                                                                                                                                                                                                                                                                              |
| [App.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/App.tsx)                     | The code snippet in the App.tsx file sets up the navigation for the ChatGPT AI app using React Native. It creates a stack navigator that allows users to navigate between the HomeScreen and Information screens. The header styles and options are also configured. The DataProvider component is included to provide data to the app.                                          |
| [app.json](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/app.json)                   | The `app.json` file contains configuration settings for the ChatGPT-App. It includes information such as the app's name, version, orientation, icons, splash screen, asset patterns, platform-specific settings (iOS and Android), and web settings.                                                                                                                             |
| [package-lock.json](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/package-lock.json) | Code snippet generates README files for repositories.                                                                                                                                                                                                                                                                                                                            |
| [package.json](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/package.json)           | The code snippet in the package.json file defines the dependencies and scripts required for the ChatGPT-App React Native TypeScript repository. It specifies the project's name, version, main file, and various scripts for running the project on different platforms like Android, iOS, and web. It also lists the dependencies and devDependencies required for the project. |
| [tsconfig.json](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/tsconfig.json)         | The code snippet in tsconfig.json file sets strict compiler options for the TypeScript project in the parent repository architecture.                                                                                                                                                                                                                                            |

</details>

<details closed><summary>types</summary>

| File                                                                                                     | Summary                                                                                                                                   |
| ---                                                                                                      | ---                                                                                                                                       |
| [types.d.ts](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/types/types.d.ts) | The code defines TypeScript interfaces for the `MessageType` and `User` objects, which are used to represent messages in the ChatGPT app. |

</details>

<details closed><summary>context</summary>

| File                                                                                                                   | Summary                                                                                                                                                                                                                                                                                                                                                                              |
| ---                                                                                                                    | ---                                                                                                                                                                                                                                                                                                                                                                                  |
| [DataProvider.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/context/DataProvider.tsx) | The code snippet in `DataProvider.tsx` is a React component that creates a data context provider. It creates a context using `createContext` and defines a state variable `textInput` using `useState`. The component renders the `children` passed as props within the context provider. It provides the `textInput` state and `setTextInput` function as the value of the context. |

</details>

<details closed><summary>constants</summary>

| File                                                                                                             | Summary                                                                                           |
| ---                                                                                                              | ---                                                                                               |
| [constants.ts](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/constants/constants.ts) | The code snippet in the file `constants/constants.ts` exports the API URL `http://10.0.2.2:3000`. |

</details>

<details closed><summary>server</summary>

| File                                                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                  |
| ---                                                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                      |
| [index.js](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/server/index.js)                   | The code snippet located at `server/index.js` is responsible for creating an Express.js server that handles HTTP requests. It utilizes the OpenAI API to generate chat completions based on the provided message. The completions are then sent back as a JSON response.                                                                                 |
| [config.js](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/server/config.js)                 | The code snippet located at `server/config.js` imports the `config` function from the `dotenv` package and calls it. It exports an object named `environment` with two properties: `OPENAI_API_KEY` and `OPENAI_ORGANIZATION`, which are assigned values from the `process.env` object.                                                                  |
| [package-lock.json](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/server/package-lock.json) | The code snippet generates README files for repositories.                                                                                                                                                                                                                                                                                                |
| [package.json](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/server/package.json)           | The code snippet in the server/package.json file contains the configuration and dependencies for the server component of the ChatGPT-App-React-Native-TypeScript repository. It includes scripts for development and starting the server, as well as dependencies for handling HTTP requests, server configuration, and interaction with the OpenAI API. |

</details>

<details closed><summary>screens</summary>

| File                                                                                                               | Summary                                                                                                                                                                 |
| ---                                                                                                                | ---                                                                                                                                                                     |
| [Infomation.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/screens/Infomation.tsx) | The code snippet in the file `Infomation.tsx` creates a React Native component called `Infomation`. It renders a view with centered text Infomation within a container. |
| [HomeScreen.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/screens/HomeScreen.tsx) | The code snippet represents the HomeScreen component in a React Native app. It renders the Layout component, followed by the ListMessage and InputMessage components.   |

</details>

<details closed><summary>components</summary>

| File                                                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                             |
| ---                                                                                                                       | ---                                                                                                                                                                                                                                                                                                                                                 |
| [InputMessage.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/components/InputMessage.tsx) | The `InputMessage.tsx` file is responsible for rendering an input field and a send button in a chat application. It allows users to enter and send messages.                                                                                                                                                                                        |
| [Layout.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/components/Layout.tsx)             | The `Layout.tsx` file in the `components` directory of the repository defines a React Native component called `Layout`. It wraps the provided children components in a container view and applies styling to create a layout with a specific background color. The component also includes a status bar with a specific background color and style. |
| [Message.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/components/Message.tsx)           | The code snippet in `Message.tsx` defines a React Native component that displays a message in a chat interface. It includes the message content, user profile information, and an option to copy the message to the clipboard.                                                                                                                      |
| [ListMessage.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/components/ListMessage.tsx)   | The code snippet is responsible for rendering a list of messages in a chat interface. It fetches messages from an API, allows the user to input text, and updates the list of messages accordingly.                                                                                                                                                 |

</details>

<details closed><summary>hooks</summary>

| File                                                                                                                     | Summary                                                                                                                                                                                                                                              |
| ---                                                                                                                      | ---                                                                                                                                                                                                                                                  |
| [useFetchMessage.ts](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/hooks/useFetchMessage.ts) | This code snippet defines a custom hook called useFetchMessage that is responsible for fetching a message from a server. It takes a message as input, loads the message from the server, and returns the fetched message along with a loading state. |

</details>

<details closed><summary>helpers</summary>

| File                                                                                                             | Summary                                                                                                                                                                           |
| ---                                                                                                              | ---                                                                                                                                                                               |
| [getMessage.ts](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/helpers/getMessage.ts) | The code snippet in helpers/getMessage.ts is responsible for sending a request to an API endpoint with a message. It then receives a response, extracts the data, and returns it. |

</details>

---

## 🚀 Getting Started

***Prerequisites***

Ensure you have the following dependencies installed on your system:

- `► INSERT-DEPENDENCY-1`
- `► INSERT-DEPENDENCY-2`
- `► INSERT-DEPENDENCY-3`

### ⚙️ Installation

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


## 🚧 Project Roadmap

> - [X] `ℹ️  Task 1: Implement X`
> - [ ] `ℹ️  Task 2: Implement Y`
> - [ ] `ℹ️ ...`


---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/issues)**: Submit bugs found or log feature requests for YUBERLEY.

#### *Contributing Guidelines*

<details closed>
<summary>Click to expand</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone <your-forked-repo-url>
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear and concise message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

## 📄 License


This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 👏 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#Top)

---
