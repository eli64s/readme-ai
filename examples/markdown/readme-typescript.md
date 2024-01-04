<p align="center">
  <img src="https://img.icons8.com/external-tal-revivo-duo-tal-revivo/100/external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-duo-tal-revivo.png" width="100" />
</p>
<p align="center">
    <h1 align="center">CHATGPT-APP-REACT-NATIVE-TYPESCRIPT</h1>
</p>
<p align="center">
    <em>ChatGPT: React Native. Powerful. Seamless. Conversational.</em>
</p>
<p align="center">
	<!-- Shields.io badges not used with skill icons. --><p>
<p align="center">
		<em>Developed with the software and tools below</em>
</p>
<p align="center">
	<a href="https://skillicons.dev">
		<img src="https://skillicons.dev/icons?i=express,js,md,react,ts&theme=light">
	</a>
</p>
<hr>

##  Quick Links
- [ Quick Links](#-quick-links)
- [ Overview](#-overview)
- [ Features](#-features)
- [ Repository Structure](#-repository-structure)
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

ChatGPT-App-React-Native-TypeScript is a project that aims to provide a user-friendly and intuitive chat application built with React Native and TypeScript. The core functionality of this app is centered around facilitating seamless communication between users through chat messages. Users can send and receive messages in real-time, making it easy to have engaging conversations. The value proposition of this project lies in its ability to provide a platform for users to connect and exchange information efficiently and conveniently. With its clean and modern design, this app offers a smooth user experience, making it an ideal solution for anyone looking for a reliable chat application.

---

##  Features

|    | Feature           | Description                                                                                                       |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**    | The codebase follows a client-server architecture, with React Native and TypeScript on the client side and a Node.js server using Express.js. |
| 📄 | **Documentation**  | The codebase lacks comprehensive documentation. There are some inline comments, but overall documentation is minimal. |
| 🔗 | **Dependencies**   | The project relies on various dependencies, including React Native, React Navigation, Axios, and Firebase. |
| 🧩 | **Modularity**     | The codebase demonstrates modularity by organizing components into separate folders and files based on their functionality. |
| 🧪 | **Testing**        | No information is available regarding the system's testing strategies and tools. |
| ⚡️ | **Performance**     | It is difficult to assess the system's performance without further information. However, React Native and Node.js are known for their speed and efficiency. |
| 🔐 | **Security**       | The codebase does not have explicit security measures. It relies on the security provided by Firebase for authentication and data storage.

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

<details closed><summary>.</summary>

| File                                                                                                             | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---                                                                                                              | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [App.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/App.tsx)                     | The `App.tsx` file in the repository is responsible for setting up the main application structure using React Native and TypeScript. It utilizes the `NavigationContainer` and `createNativeStackNavigator` components from React Navigation to define the app's navigation flow. Additionally, it includes a `DataProvider` component for managing global application state. The file renders two screens, HomeScreen and Infomation, and customizes their headers with styles and navigation options. |
| [app.json](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/app.json)                   | The code snippet in the components directory of the repository is responsible for rendering different chat message components in a React Native and TypeScript app. It includes components such as InputMessage, Layout, ListMessage, and Message. The code supports a chat-based application and contributes to the overall user interface and functionality of the app.                                                                                                                               |
| [package-lock.json](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/package-lock.json) | The code snippet in the ChatGPT-App-React-Native-TypeScript repository is responsible for managing the UI components, data providers, and helper functions of a chat application built using React Native and TypeScript. It facilitates inputting and displaying messages, fetching new messages, and maintaining app-wide constants.                                                                                                                                                                  |
| [package.json](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/package.json)           | This code snippet belongs to a React Native app that uses TypeScript. It includes components, context, hooks, and helpers for a chat interface. It relies on dependencies such as React, React Native, and React Navigation. The code focuses on managing chat messages and fetching data.                                                                                                                                                                                                              |
| [tsconfig.json](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/tsconfig.json)         | This code snippet is part of a React Native app built using TypeScript. It includes files for components, constants, context, helpers, hooks, screens, and types. The tsconfig.json file contains the compiler options for the TypeScript code.                                                                                                                                                                                                                                                         |

</details>

<details closed><summary>types</summary>

| File                                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                           |
| ---                                                                                                      | ---                                                                                                                                                                                                                                                                                                                                               |
| [types.d.ts](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/types/types.d.ts) | The code snippet in the types/types.d.ts file defines the interface for MessageType, which represents a message in the ChatGPT app. It includes properties such as id, creation time, model, text, user information, and usage statistics. This file is crucial for ensuring consistent data structure and type checking throughout the codebase. |

</details>

<details closed><summary>context</summary>

| File                                                                                                                   | Summary                                                                                                                                                                                                                                                     |
| ---                                                                                                                    | ---                                                                                                                                                                                                                                                         |
| [DataProvider.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/context/DataProvider.tsx) | The `DataProvider` component in the `context` directory manages and provides data to its children components through the `DataContext`. It uses React's `useState` hook to manage the `textInput` state and updates it through the `setTextInput` function. |

</details>

<details closed><summary>constants</summary>

| File                                                                                                             | Summary                                                                                                                                                                                                               |
| ---                                                                                                              | ---                                                                                                                                                                                                                   |
| [constants.ts](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/constants/constants.ts) | The code snippet in the constants file provides the API URL for the ChatGPT app. It exports the constant API_URL with the value http://10.0.2.2:3000, which is used for communication between the app and the server. |

</details>

<details closed><summary>server</summary>

| File                                                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---                                                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                                                                        |
| [index.js](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/server/index.js)                   | This code snippet is the server-side implementation of a chat application using Express.js and OpenAI API. It handles incoming chat requests and sends them to the OpenAI API for generating responses. The server listens on port 3000 and exposes a `/api/chat` endpoint for chat interactions.                                                                                                          |
| [config.js](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/server/config.js)                 | This code snippet provides the configuration for the ChatGPT application using environment variables. It sets up the OpenAI API key and organization using the values provided in the.env file. This allows the application to securely communicate with the OpenAI API.                                                                                                                                   |
| [package-lock.json](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/server/package-lock.json) | This code snippet contains critical features such as the input message component, message list component, and data provider. It plays a crucial role in the ChatGPT-App-React-Native-TypeScript repository's architecture by handling user input, displaying messages, and managing data for the chat application. The directory structure suggests a modular and organized approach to code organization. |
| [package.json](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/server/package.json)           | This code snippet is part of a React Native app for a ChatGPT application. It includes components, context, hooks, and helpers. The codebase also has a server using Express.js and OpenAI for handling requests.                                                                                                                                                                                          |

</details>

<details closed><summary>screens</summary>

| File                                                                                                               | Summary                                                                                                                                                                                               |
| ---                                                                                                                | ---                                                                                                                                                                                                   |
| [Infomation.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/screens/Infomation.tsx) | The code snippet is a React Native component called Infomation that displays a text saying Infomation in the center of the screen. It is part of the ChatGPT-App-React-Native-TypeScript repository.  |
| [HomeScreen.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/screens/HomeScreen.tsx) | This code snippet, located in the `screens` directory within the repository, defines the main screen of the ChatGPT app. It renders components for displaying and inputting messages within a layout. |

</details>

<details closed><summary>components</summary>

| File                                                                                                                      | Summary                                                                                                                                                                                                                                                                                                       |
| ---                                                                                                                       | ---                                                                                                                                                                                                                                                                                                           |
| [InputMessage.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/components/InputMessage.tsx) | The code snippet is a React Native component called InputMessage. It allows users to enter and send messages in a chat interface. It retrieves user input, sends the message, and updates the state accordingly.                                                                                              |
| [Layout.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/components/Layout.tsx)             | This code snippet defines the Layout component in a React Native app. It provides a container with a dark background color and centralizes the children components.                                                                                                                                           |
| [Message.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/components/Message.tsx)           | The `Message.tsx` file is a React Native component that displays a chat message. It includes features such as copying the message to the clipboard and showing a toast notification. The component's appearance and behavior depend on the user's name and avatar.                                            |
| [ListMessage.tsx](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/components/ListMessage.tsx)   | This code snippet is a React Native component called ListMessage that displays a list of messages. It fetches messages from an API based on user input, updates the list dynamically, and includes a pull-to-refresh feature. The component uses various hooks and context to manage state and data fetching. |

</details>

<details closed><summary>hooks</summary>

| File                                                                                                                     | Summary                                                                                                                                                                                                                                                           |
| ---                                                                                                                      | ---                                                                                                                                                                                                                                                               |
| [useFetchMessage.ts](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/hooks/useFetchMessage.ts) | The `useFetchMessage` hook in the `hooks` directory is responsible for fetching a message based on user input. It uses React's `useState` and `useEffect` hooks to manage state and perform the API call. It returns the fetched message data and loading status. |

</details>

<details closed><summary>helpers</summary>

| File                                                                                                             | Summary                                                                                                                                                                                                                                                                                                  |
| ---                                                                                                              | ---                                                                                                                                                                                                                                                                                                      |
| [getMessage.ts](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/helpers/getMessage.ts) | This code snippet is a helper function that makes an API call to retrieve a response message. It takes a user input message, sends it to a chatbot model, and returns the generated response. The function is used in the ChatGPT-App-React-Native-TypeScript repository for handling message retrieval. |

</details>

---

##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* TypeScript: `► INSERT-VERSION-HERE`
* `► ...`
* `► ...`

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
Use the following command to run ChatGPT-App-React-Native-TypeScript:
```sh
npm run build && node dist/main.js
```

###  Tests
To execute tests, run:
```sh
npm test
```

---

##  Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/issues)**: Submit bugs found or log feature requests for ChatGPT-App-React-Native-TypeScript.

<details closed>
<summary>Contributing Guidelines</summary>

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

[**Return**](#-quick-links)

---
