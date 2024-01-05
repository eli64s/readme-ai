<p align="left">
<img src="https://img.icons8.com/?size=512&id=55494&format=png" width="100" alt="ChatGPT-App-React-Native-TypeScript">
</p>
<p align="left">
    <h1 align="left">CHATGPT-APP-REACT-NATIVE-TYPESCRIPT</h1>
</p>
<p align="left">
    <em>ChatGPT: Conversations Perfected in Your Palm</em>
</p>
<p align="left">
	<img src="https://img.shields.io/github/license/Yuberley/ChatGPT-App-React-Native-TypeScript?style=flat&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/Yuberley/ChatGPT-App-React-Native-TypeScript?style=flat&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/Yuberley/ChatGPT-App-React-Native-TypeScript?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/Yuberley/ChatGPT-App-React-Native-TypeScript?style=flat&color=0080ff" alt="repo-language-count">
<p>
<p align="left">
		<em>Developed with the software and tools below.</em>
</p>
<p align="left">
	<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=flat&logo=JavaScript&logoColor=black" alt="JavaScript">
	<img src="https://img.shields.io/badge/Nodemon-76D04B.svg?style=flat&logo=Nodemon&logoColor=white" alt="Nodemon">
	<img src="https://img.shields.io/badge/React-61DAFB.svg?style=flat&logo=React&logoColor=black" alt="React">
	<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=flat&logo=OpenAI&logoColor=white" alt="OpenAI">
	<img src="https://img.shields.io/badge/TypeScript-3178C6.svg?style=flat&logo=TypeScript&logoColor=white" alt="TypeScript">
	<img src="https://img.shields.io/badge/Expo-000020.svg?style=flat&logo=Expo&logoColor=white" alt="Expo">
	<img src="https://img.shields.io/badge/Express-000000.svg?style=flat&logo=Express&logoColor=white" alt="Express">
	<img src="https://img.shields.io/badge/JSON-000000.svg?style=flat&logo=JSON&logoColor=white" alt="JSON">
</p>
<hr>

## 🔗 Quick Links

> - [📍 Overview](#-overview)
> - [📦 Features](#-features)
> - [📂 Repository Structure](#-repository-structure)
> - [🧩 Modules](#-modules)
> - [🚀 Getting Started](#-getting-started)
>     - [⚙️ Installation](#-installation)
>     - [🤖 Running ChatGPT-App-React-Native-TypeScript](#-running-ChatGPT-App-React-Native-TypeScript)
>     - [🧪 Tests](#-tests)
> - [🛠 Project Roadmap](#-project-roadmap)
> - [🤝 Contributing](#-contributing)
> - [📄 License](#-license)
> - [👏 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

ChatGPT-App-React-Native-TypeScript is a mobile application built using React Native and TypeScript. The app allows users to chat with an AI-powered language model called ChatGPT. By leveraging the power of natural language processing and machine learning, ChatGPT can understand and respond to user messages in a conversational manner. The app provides a user-friendly interface where users can input their messages and receive thoughtful and coherent responses from ChatGPT. With this app, users can engage in meaningful conversations, seek advice, get recommendations, or simply have fun interacting with an AI-powered chatbot. The project aims to bring the benefits of AI language models to mobile devices, making them accessible and enjoyable for users on the go.

---

## 📦 Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | The project is built using React Native and TypeScript. The architecture follows a client-server model with a React Native front-end and an Express.js back-end. |
| 🔩 | **Code Quality**  | The codebase is well-structured and follows best practices. It utilizes TypeScript for type safety and has consistent coding style. |
| 📄 | **Documentation** | The extent of documentation is not specified in the given information. It is recommended to check the project's README or documentation files for more details. |
| 🔌 | **Integrations**  | The project integrates with openai, react-native-safe-area-context, and react-native-web libraries. |
| 🧩 | **Modularity**    | The codebase appears to be modular and reusable, with components like `Infomation.tsx`, `Message.tsx`, and `ListMessage.tsx` providing clear separation of concerns. |
| 🧪 | **Testing**       | No information is provided about the testing frameworks or tools used in the project. It is recommended to check the project's documentation or codebase for testing details. |
| ⚡️  | **Performance**   | The given information does not provide details on performance. Performance can be assessed by analyzing the code for efficient algorithms and optimization techniques. |
| 🛡️ | **Security**      | The details about data protection and access control measures are not specified. It is important to review the project's codebase and documentation for security considerations. |
| 📦 | **Dependencies**  | The project has dependencies on libraries such as express, openai, react-native-safe-area-context, and react-native-web. |
| 🚀 | **Scalability**   | Without specific information, it's not possible to assess the project's ability to handle increased traffic and load. Scalability considerations should be reviewed in the project's codebase and architecture. |


---

## 📂 Repository Structure

```sh
└── ChatGPT-App-React-Native-TypeScript/
    ├── App.tsx
    ├── app.json
    ├── components
    │   ├── InputMessage.tsx
    │   ├── Layout.tsx
    │   ├── ListMessage.tsx
    │   └── Message.tsx
    ├── constants
    │   └── constants.ts
    ├── context
    │   └── DataProvider.tsx
    ├── helpers
    │   └── getMessage.ts
    ├── hooks
    │   └── useFetchMessage.ts
    ├── package-lock.json
    ├── package.json
    ├── screens
    │   ├── HomeScreen.tsx
    │   └── Infomation.tsx
    ├── server
    │   ├── config.js
    │   ├── index.js
    │   ├── package-lock.json
    │   └── package.json
    ├── tsconfig.json
    └── types
        └── types.d.ts
```

---

## 🧩 Modules

<details closed><summary>.</summary>

| File                                                                                                               | Summary                                                                                                                                                                                                                                                                                                                           |
| ---                                                                                                                | ---                                                                                                                                                                                                                                                                                                                               |
| [App.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/App.tsx)                     | This code snippet in the App.tsx file is responsible for setting up the navigation and screens in the ChatGPT-App-React-Native-TypeScript repository. It creates a stack navigator with two screens, HomeScreen and Infomation, and provides a navigation container. It also includes the DataProvider context for managing data. |
| [app.json](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/app.json)                   | This code snippet, located in the `app.json` file, configures various settings for the ChatGPT-App, such as the app name, version, orientation, icons, splash screen, and asset bundle patterns.                                                                                                                                  |
| [package-lock.json](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/package-lock.json) | This code snippet is a crucial component in the ChatGPT-App-React-Native-TypeScript repository. It handles message retrieval and rendering within the app's chat interface.                                                                                                                                                       |
| [package.json](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/package.json)           | This code snippet is part of the ChatGPT-App-React-Native-TypeScript repository. It includes various components, screens, and helpers for a chat application. The package.json file contains dependencies and scripts related to the app's development and deployment.                                                            |
| [tsconfig.json](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/tsconfig.json)         | This code snippet, located in the tsconfig.json file, extends the base configuration and enables strict mode for the TypeScript compiler in the React Native app.                                                                                                                                                                 |

</details>

<details closed><summary>types</summary>

| File                                                                                                       | Summary                                                                                                                                                                                                                                                                                                                           |
| ---                                                                                                        | ---                                                                                                                                                                                                                                                                                                                               |
| [types.d.ts](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/types/types.d.ts) | The `types.d.ts` file in the `types` directory of the repository defines the structure of the `MessageType` interface. This interface represents the structure of a message object used in the ChatGPT app. It includes properties like the message ID, creation timestamp, text content, user information, and usage statistics. |

</details>

<details closed><summary>context</summary>

| File                                                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                                          |
| ---                                                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                                              |
| [DataProvider.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/context/DataProvider.tsx) | This code snippet is located in the `context/DataProvider.tsx` file and is part of the React Native TypeScript chat application repository. It creates a `DataProvider` component using React's context API to manage shared data state. The `DataProvider` component wraps its children components and provides a `textInput` state and a `setTextInput` function to update it. |

</details>

<details closed><summary>constants</summary>

| File                                                                                                               | Summary                                                                                                                                                                                                                          |
| ---                                                                                                                | ---                                                                                                                                                                                                                              |
| [constants.ts](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/constants/constants.ts) | The code snippet in `constants/constants.ts` exports the API_URL constant, which is set to `http://10.0.2.2:3000`. This constant likely represents the URL endpoint of the API used by the parent repository's React Native app. |

</details>

<details closed><summary>server</summary>

| File                                                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                            |
| ---                                                                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                |
| [index.js](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/server/index.js)                   | This code snippet is part of a server-side component in the ChatGPT-App-React-Native-TypeScript repository. It handles the incoming chat messages and uses the OpenAI API to generate responses. The server is built with Express, and it exposes an endpoint for receiving chat messages and returning AI-generated responses.                                    |
| [config.js](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/server/config.js)                 | This code snippet in the server/config.js file is responsible for configuring the environment variables required for the ChatGPT-App-React-Native-TypeScript repository. It imports the dotenv package and sets up the necessary environment variables.                                                                                                            |
| [package-lock.json](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/server/package-lock.json) | The code snippet in this repository is related to a React Native TypeScript app called ChatGPT. It includes components for inputting and displaying messages, along with constants and context for managing data. The code focuses on the app's UI and data management functionality.                                                                              |
| [package.json](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/server/package.json)           | The code snippet in the `server` directory contains the package.json file which defines the dependencies and scripts for running the server. It specifies the required packages for the server to function, such as `express`, `cors`, and `openai`. It also includes scripts for running the server in development mode (`dev`) and in production mode (`start`). |

</details>

<details closed><summary>screens</summary>

| File                                                                                                                 | Summary                                                                                                                                                                                                                                                  |
| ---                                                                                                                  | ---                                                                                                                                                                                                                                                      |
| [Infomation.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/screens/Infomation.tsx) | This code snippet represents the `Infomation` screen component in the ChatGPT-App-React-Native-TypeScript repository. It renders an informational page with a centered text element.                                                                     |
| [HomeScreen.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/screens/HomeScreen.tsx) | The code snippet in HomeScreen.tsx is a component that renders the home screen of the ChatGPT-App-React-Native-TypeScript repository. It imports and renders other components such as Layout, ListMessage, and InputMessage to display a chat interface. |

</details>

<details closed><summary>components</summary>

| File                                                                                                                        | Summary                                                                                                                                                                                                                                                                                                             |
| ---                                                                                                                         | ---                                                                                                                                                                                                                                                                                                                 |
| [InputMessage.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/components/InputMessage.tsx) | The `InputMessage.tsx` component in the `ChatGPT-App-React-Native-TypeScript` repository is responsible for rendering an input field and a send button for the user to send messages. The component manages the state of the input field and sends the message to the data context when the send button is pressed. |
| [Layout.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/components/Layout.tsx)             | The Layout component in the ChatGPT-App-React-Native-TypeScript repository provides a wrapper for the content of the app, including a status bar with a dark background color and centered content.                                                                                                                 |
| [Message.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/components/Message.tsx)           | The `Message.tsx` component in the `ChatGPT-App-React-Native-TypeScript` repository displays a chat message with the sender's name, avatar, and text. It allows the user to copy the text to the clipboard.                                                                                                         |
| [ListMessage.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/components/ListMessage.tsx)   | The ListMessage component in the ChatGPT-App-React-Native-TypeScript repository is responsible for displaying a list of messages. It fetches new messages, adds user input to the list, and updates the list with new messages. The component also handles refreshing the list when needed.                         |

</details>

<details closed><summary>hooks</summary>

| File                                                                                                                       | Summary                                                                                                                                                                                                                                                                                                              |
| ---                                                                                                                        | ---                                                                                                                                                                                                                                                                                                                  |
| [useFetchMessage.ts](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/hooks/useFetchMessage.ts) | This code snippet, located in the `hooks` directory, is part of a React Native TypeScript app. It defines a custom hook called `useFetchMessage` that handles fetching a message and its loading state. The `useFetchMessage` hook takes a message as input and returns the fetched message and a loading indicator. |

</details>

<details closed><summary>helpers</summary>

| File                                                                                                               | Summary                                                                                                                                                                                                                                                                            |
| ---                                                                                                                | ---                                                                                                                                                                                                                                                                                |
| [getMessage.ts](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/helpers/getMessage.ts) | This code snippet, located in the helpers/getMessage.ts file, is responsible for sending a message to an API endpoint and receiving a response. It uses the fetch function to make a POST request, passing the message as a parameter. The response from the API is then returned. |

</details>

---

## 🚀 Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **TypeScript**: `version x.y.z`

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

Use the following command to run ChatGPT-App-React-Native-TypeScript:

```sh
npm run build && node dist/main.js
```

### 🧪 Tests

To execute tests, run:

```sh
npm test
```

---

## 🛠 Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github/Yuberley/ChatGPT-App-React-Native-TypeScript/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github/Yuberley/ChatGPT-App-React-Native-TypeScript/issues)**: Submit bugs found or log feature requests for Chatgpt-app-react-native-typescript.

<details closed>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
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

[**Return**](#-quick-links)

---
