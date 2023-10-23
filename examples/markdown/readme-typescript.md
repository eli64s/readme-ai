<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>CHATGPT-APP-REACT-NATIVE-TYPESCRIPT</h1>
<h3>◦ Unleash limitless conversations with ChatGPT!</h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=plastic&logo=JavaScript&logoColor=black" alt="JavaScript" />
<img src="https://img.shields.io/badge/Nodemon-76D04B.svg?style=plastic&logo=Nodemon&logoColor=white" alt="Nodemon" />
<img src="https://img.shields.io/badge/React-61DAFB.svg?style=plastic&logo=React&logoColor=black" alt="React" />
<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=plastic&logo=OpenAI&logoColor=white" alt="OpenAI" />

<img src="https://img.shields.io/badge/TypeScript-3178C6.svg?style=plastic&logo=TypeScript&logoColor=white" alt="TypeScript" />
<img src="https://img.shields.io/badge/Expo-000020.svg?style=plastic&logo=Expo&logoColor=white" alt="Expo" />
<img src="https://img.shields.io/badge/Express-000000.svg?style=plastic&logo=Express&logoColor=white" alt="Express" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style=plastic&logo=JSON&logoColor=white" alt="JSON" />
</p>
<img src="https://img.shields.io/github/license/Yuberley/ChatGPT-App-React-Native-TypeScript?style=plastic&color=5D6D7E" alt="GitHub license" />
<img src="https://img.shields.io/github/last-commit/Yuberley/ChatGPT-App-React-Native-TypeScript?style=plastic&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/Yuberley/ChatGPT-App-React-Native-TypeScript?style=plastic&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/languages/top/Yuberley/ChatGPT-App-React-Native-TypeScript?style=plastic&color=5D6D7E" alt="GitHub top language" />
</div>

---

##  Table of Contents
- [ Table of Contents](#-table-of-contents)
- [ Overview](#-overview)
- [ Features](#-features)
- [ repository Structure](#-repository-structure)
- [ Modules](#modules)
- [ Getting Started](#-getting-started)
    - [ Installation](#-installation)
    - [ Running ChatGPT-App-React-Native-TypeScript](#-running-ChatGPT-App-React-Native-TypeScript)
    - [ Tests](#-tests)
- [ Roadmap](#-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

---


##  Overview

The repository "ChatGPT-App-React-Native-TypeScript" is a React Native app that provides a chat interface powered by ChatGPT AI. This app uses React Navigation for navigation between screens and includes components for inputting and displaying messages. The app also has a server-side implementation using Express.js to handle HTTP requests for chat messages. The value proposition of this project is to allow users to have interactive and engaging conversations with the AI-powered ChatGPT model through a mobile app.

---

##  Features

|    | Feature            | Description                                                                                                                                                                                                                                                |
|----|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The codebase follows a typical React Native app structure with separate directories for components, constants, context, helpers, hooks, screens, server, types, and others. It uses the `DataProvider` component to manage the application's data and React Navigation for screen navigation. The server-side implementation uses Express.js for handling API requests and OpenAI API for generating model responses. |
| 📄 | **Documentation**  | The documentation in the repository is sparse and could be improved. It lacks detailed explanations of the codebase's components, functions, and overall architecture. Adding inline comments, code comments, and a README file would enhance the comprehensiveness and usefulness of the documentation.                                      |
| 🔗 | **Dependencies**   | The codebase relies on various external libraries and systems, including React Native, React Navigation, Expo, TypeScript, Express.js, OpenAI API, and other utility packages. These dependencies provide the necessary tools and frameworks for building and running the ChatGPT app.                                                                 |
| 🧩 | **Modularity**     | The codebase is organized into small, interchangeable components. Each component is responsible for a specific part of the application's functionality and can be reused or replaced easily. The use of React context and custom hooks promotes modularity and separation of concerns.                                                                                     |
| 🧪 | **Testing**        | The codebase lacks explicit testing strategies and tools. Testing frameworks like Jest and tools like React Testing Library could be implemented to ensure the reliability and correctness of the application. Integrating unit tests, integration tests, and end-to-end tests would be beneficial for maintaining code quality and preventing regressions.                 |
| ⚡️  | **Performance**    | The performance of the system depends on factors such as network latency, response times from the OpenAI API, and the efficiency of the server-side implementation. Proper caching mechanisms, optimizing API requests, and implementing code-level optimizations can enhance the app's speed and resource usage.                                                     |
| 🔐 | **Security**       | The codebase doesn't include specific measures for client-side or server-side security. Implementing authentication, input validation, and secure communication protocols (such as SSL/TLS) would be necessary to protect user data and prevent malicious attacks. Care should be taken when handling user input and interacting with external APIs.           |
| 🔀 | **Version Control**| The version control strategy and tools for the codebase are not mentioned in the provided information. Adopting a version control system (e.g., Git) and following best practices like branching, merging, and commit conventions would facilitate collaboration, code review, and easier rollback to previous versions.                       |
| 🔌 | **Integrations**   | The system integrates with various external systems and services, including the OpenAI API for generating model responses, React Navigation for screen navigation, and Expo for building and deploying the React Native app. The Express.js server interacts with the mobile app through API endpoints for sending and receiving messages.                  |
| 📶 | **Scalability**    | The codebase's scalability depends on factors like the capacity of the server hosting the Express.js app and the performance of the OpenAI API. Scaling the backend infrastructure and optimizing API request handling can help accommodate a growing user base and ensure responsiveness of the

---


##  Repository Structure

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


##  Modules

<details closed><summary>Root</summary>

| File                                                                                                             | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---                                                                                                              | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [App.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/App.tsx)                     | This code is a React Native app that provides a chat interface powered by ChatGPT AI. It uses React Navigation to handle navigation between screens. The `DataProvider` component is used to manage the application's data. The `HomeScreen` component displays the chat interface, and the `Infomation` component shows information about the app. The app's navigation bar includes an "About" button that navigates to the `Infomation` screen.      |
| [app.json](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/app.json)                   | The code represents the directory tree structure of a React Native app called "ChatGPT-App" built with TypeScript. It includes various directories such as components, constants, context, helpers, hooks, screens, server, types, and others. The app.json file contains configuration details for the Expo framework, including app name, version, orientation, icons, splash screen, and asset patterns for different platforms.                     |
| [package-lock.json](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/package-lock.json) | This code represents the directory tree and package dependencies for a ChatGPT mobile app built using React Native and TypeScript. The code includes various components, screens, helpers, hooks, and a server configuration file. The package-lock.json file specifies the dependencies needed for the app, including packages for navigation, Expo, React Native, and more.                                                                           |
| [package.json](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/package.json)           | The code represents the directory structure and dependencies of a ChatGPT app built with React Native and TypeScript. The project has various components, screens, and helpers, along with a server configuration. It relies on packages like React Navigation, Expo, and React UUID. The package.json file contains the project's name, version, scripts for running the app, and lists the dependencies and devDependencies required for the project. |
| [tsconfig.json](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/tsconfig.json)         | The code represents the directory structure of a React Native TypeScript app called ChatGPT-App. It includes various components, constants, context, helpers, hooks, screens, and types. The tsconfig.json file specifies that strict type checking should be enabled for the project.                                                                                                                                                                  |

</details>

<details closed><summary>Types</summary>

| File                                                                                                     | Summary                                                                                                                                                                                                                                                                                                              |
| ---                                                                                                      | ---                                                                                                                                                                                                                                                                                                                  |
| [types.d.ts](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/types/types.d.ts) | The code defines TypeScript interfaces for the User and Usage objects, and exports the MessageType interface. The MessageType interface represents a message in the chat application and includes properties such as id, creation timestamp, model used, message text, user information, and token usage statistics. |

</details>

<details closed><summary>Context</summary>

| File                                                                                                                   | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---                                                                                                                    | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [DataProvider.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/context/DataProvider.tsx) | The code in "DataProvider.tsx" establishes a React context called "DataContext" that provides a shared state for its child components. It imports the "MessageType" type from "../types/types" and creates a context with an initial state of an empty "textInput" object. It also defines a "DataProvider" component that takes in children as props. Inside the component, it uses the "useState" hook to create a "textInput" state variable and a "setTextInput" function to update that state. It wraps the children components with the "DataProvider" context and makes the "textInput" state and "setTextInput" function available to them. |

</details>

<details closed><summary>Constants</summary>

| File                                                                                                             | Summary                                                                                                                                                                                                                      |
| ---                                                                                                              | ---                                                                                                                                                                                                                          |
| [constants.ts](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/constants/constants.ts) | The code defines a constant variable `API_URL` with the value `'http://10.0.2.2:3000'`. This constant is likely used as the base URL for an API in the project, allowing communication between the frontend and the backend. |

</details>

<details closed><summary>Server</summary>

| File                                                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---                                                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [index.js](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/server/index.js)                   | This code is for the server-side implementation of a chat application using Express.js. It sets up an Express server that listens on port 3000 and handles HTTP requests for chat messages. The server uses the OpenAI API to generate model responses based on the provided message. When a POST request is made to'/api/chat', it sends the message to the OpenAI API, receives a response, and returns the processed data to the client. The server also includes basic error handling and logging functionalities. |
| [config.js](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/server/config.js)                 | The code in `server/config.js` imports the `config` function from the `dotenv` package and calls it. This function loads environment variables from a `.env` file into `process.env`. The `environment` object is then exported, containing values for `OPENAI_API_KEY` and `OPENAI_ORGANIZATION` that are retrieved from `process.env`.                                                                                                                                                                               |
| [package-lock.json](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/server/package-lock.json) | The code represents a server package for an application called ChatGPT-App-React-Native-TypeScript. The package contains dependencies such as body-parser, cors, dotenv, express, morgan, and openai which are used to build the server. This package also includes a devDependency called nodemon.                                                                                                                                                                                                                    |
| [package.json](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/server/package.json)           | This code represents a React Native mobile app called ChatGPT, built with TypeScript. It includes various directories like components, screens, context, and helpers, each containing relevant files for app functionality. The server directory consists of files for a backend server, written in Express, which handles API requests from the app. Dependencies like Express, body-parser, cors, dotenv, and openai are used for server functionality, while nodemon is used for development purposes.              |

</details>

<details closed><summary>Screens</summary>

| File                                                                                                               | Summary                                                                                                                                                                                                                                                                                                                                      |
| ---                                                                                                                | ---                                                                                                                                                                                                                                                                                                                                          |
| [Infomation.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/screens/Infomation.tsx) | The code in'screens/Infomation.tsx' is a React Native component that displays a simple screen with a centered text displaying "Infomation". The component is styled using a StyleSheet to center its contents and make it occupy the entire screen.                                                                                          |
| [HomeScreen.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/screens/HomeScreen.tsx) | The code consists of a React Native TypeScript application with a directory structure containing various folders for components, constants, context, helpers, hooks, screens, and types. The specific code in HomeScreen.tsx imports three components (Layout, ListMessage, and InputMessage), and renders them within the Layout component. |

</details>

<details closed><summary>Components</summary>

| File                                                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---                                                                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [InputMessage.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/components/InputMessage.tsx) | The `InputMessage` component is responsible for handling user input and sending messages in a chat application. It renders a view with a text input and a send button. When the user clicks the send button, it checks if the input text is not empty. If it is not empty, it creates a new message object with the input text, sets the necessary properties such as message ID, creation time, user information, and usage statistics. The message object is then passed to the `setTextInput` function in the `DataContext` context, which updates the application state with the new message. Finally, the input text is cleared. |
| [Layout.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/components/Layout.tsx)             | The code defines a React Native component called "Layout" that serves as a container for other components. It includes a StatusBar component with a specific background color and bar style. The children of the Layout component are rendered inside a View component with specific styling properties for flex, padding, background color, and alignment.                                                                                                                                                                                                                                                                           |
| [Message.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/components/Message.tsx)           | The Message component in the ChatGPT app is a React Native component that displays a chat message. It takes in a message object as a prop and renders the message text along with the name and avatar of the user who sent the message. The component also provides the functionality to copy the message text to the clipboard when pressed. The style of the message component varies depending on whether the user is "you" or "ChatGPT", with different background colors and alignment.                                                                                                                                          |
| [ListMessage.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/components/ListMessage.tsx)   | The code defines a React Native component called `ListMessage` that renders a flat list of messages. It uses the `useState` hook to keep track of an array of messages and the `useFetchMessage` hook to fetch new messages. It also uses the `useEffect` hook to update the messages array when new messages are fetched or when the user inputs a text. The component renders a `FlatList` with a refresh control to display the messages.                                                                                                                                                                                          |

</details>

<details closed><summary>Hooks</summary>

| File                                                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---                                                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [useFetchMessage.ts](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/hooks/useFetchMessage.ts) | The code in "hooks/useFetchMessage.ts" defines a custom hook named "useFetchMessage". This hook is used to fetch a message using the "getMessage" helper function. It takes a message as input and returns a state object with properties "data" (containing the fetched message) and "isLoading" (indicating whether the message is currently being loaded). The hook utilizes useState and useEffect hooks from React to manage the state and trigger the message fetching process when the input message changes. |

</details>

<details closed><summary>Helpers</summary>

| File                                                                                                             | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---                                                                                                              | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [getMessage.ts](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/helpers/getMessage.ts) | The code in the "helpers/getMessage.ts" file is a function that sends a message to a chat API and retrieves a response. It imports the API URL and the MessageType interface from other files. The function takes a message as a parameter and constructs a request body with the necessary data. Then, it sends a POST request to the API using the fetch function, passing the request body in the JSON format. Upon receiving the response, it extracts the data and returns it as a Promise of type MessageType. |

</details>

---

##  Getting Started

***Dependencies***

Please ensure you have the following dependencies installed on your system:

`- ℹ️ Dependency 1`

`- ℹ️ Dependency 2`

`- ℹ️ ...`

###  Installation

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

###  Running ChatGPT-App-React-Native-TypeScript

```sh
npm run build && node dist/main.js
```

###  Tests
```sh
npm test
```

---


##  Project Roadmap

> - [X] `ℹ️  Task 1: Implement X`
> - [ ] `ℹ️  Task 2: Implement Y`
> - [ ] `ℹ️ ...`


---

##  Contributing

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

##  License


This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#Top)

---
