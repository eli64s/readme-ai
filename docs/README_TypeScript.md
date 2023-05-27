
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
ChatGPT-App-React-Native-TypeScript
</h1>
<h3 align="center">📍 Bringing AI-Powered Conversation to Mobile with ChatGPT-App-React-Native-TypeScript!</h3>
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
- [🔮 Features](#-feautres)
  - [Distinctive Features](#distinctive-features)
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

The ChatGPT-App-React-Native-TypeScript project is an innovative tool that makes it easier for users to communicate with a chatbot. By utilizing React Native, TypeScript, and OpenAI technologies, this project provides a user-friendly interface to easily interact with the chatbot. It also provides a wide range of features such as message type definitions, data providers, and data contexts. All these features make it easier for users to get the most out of their chatbot interactions. In short, this project is a great example of the power of technology to improve communication between machines and humans.

---

## 🔮 Features

### Distinctive Features

1. **User-Centered Design:** This project has been designed with the user's experience in mind. It is easy to use, with intuitive controls and a responsive layout.
2. **React Native and Typescript:** The project uses React Native and Typescript, two of the most popular modern frameworks. This allows the code to be more efficient and reliable.
3. **Data Context and Data Provider:** The DataContext and DataProvider components allow for easy access to data from within the project. This allows for quick and easy access to information, and the ability to quickly update the data.
4. **Input Message Form:** The InputMessage component allows for the user to easily submit messages, and validate the input. It also clears the text after submission.
5. **ListMessage Component:** The ListMessage component is used to populate the FlatList with text input from the DataContext and messages from the database.
6. **UseFetchMessage Hook:** The useFetchMessage hook is used to fetch a message from a helper function. It takes in a message string as an argument and returns an object containing the message data and a boolean flag for loading state.
7. **GetMessage Helper:** The getMessage helper imports constants from its source and defines a type for the message. It then defines a function to get a message from an API, using the imported constants, the type, and an input message as parameters. The function sends a request to the API, and returns the response in the defined type. 
8. **Styling:** The project also includes styling options for the different components, such as StyleSheet.create for the View, and the "styles" object for the InputMessage form. This allows for a consistent and attractive look and feel.

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
│   └── Information.tsx
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

| File             | Summary                                                                                                                                                                                                                                                                                                                                                                                | Module                      |
|:-----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------|
| InputMessage.tsx | This code script imports the necessary components for React and React Native to create an input message form, which will store the message text, sender name, and token usage in a DataContext to be sent. The "handleSendMessage" function validates the input and sets the message data in the DataContext, then clears the input text. The form is styled with the "styles" object. | components/InputMessage.tsx |
| Layout.tsx       | This code script imports React and related libraries, defines an interface with a React children property, and creates a layout view with a StatusBar and background color. The view contains the children and is styled with a flexbox.                                                                                                                                               | components/Layout.tsx       |
| Message.tsx      | This code script renders a message, including the sender's profile image, name, and message text. When the text is tapped, it is copied to the clipboard and a Toast notification is displayed. The message box styling varies depending on whether the message is from "you" or the chatbot.                                                                                          | components/Message.tsx      |
| ListMessage.tsx  | This code script creates a ListMessage component in React. It uses the useState, useContext, useEffect and useFetchMessage hooks to populate the FlatList with text input from a DataContext and messages from a database. The RefreshControl allows for refreshing of the FlatList.                                                                                                   | components/ListMessage.tsx  |

</details>

<details closed><summary>Constants</summary>

| File         | Summary                                                                                                                                        | Module                 |
|:-------------|:-----------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------|
| constants.ts | This code script creates a constant named "API_URL" with the value "http://10.0.2.2:3000", used to define a server address for data retrieval. | constants/constants.ts |

</details>

<details closed><summary>Context</summary>

| File             | Summary                                                                                                                                                                                                                                                                                                | Module                   |
|:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------|
| DataProvider.tsx | This code script creates a DataContext and a DataProvider component which serves as a wrapper for any elements within it. The DataProvider component uses React's'useState' hook to store the user input as a MessageType object, and passes it to the DataContext for any child components to access. | context/DataProvider.tsx |

</details>

<details closed><summary>Helpers</summary>

| File          | Summary                                                                                                                                                                                                                                                                                                            | Module                |
|:--------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
| getMessage.ts | This code script imports constants from its source and defines a type for the message. It then defines a function to get a message from an API, using the imported constants, the type, and an input message as parameters. The function sends a request to the API, and returns the response in the defined type. | helpers/getMessage.ts |

</details>

<details closed><summary>Hooks</summary>

| File               | Summary                                                                                                                                                                                                                                                                                                                                    | Module                   |
|:-------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------|
| useFetchMessage.ts | This code script creates a'useFetchMessage' hook which is used to fetch a message from a helper function. It takes in a message string as an argument and returns an object containing the message data and a boolean flag for loading state. A conditional is used to ensure the message string is not empty before attempting the fetch. | hooks/useFetchMessage.ts |

</details>

<details closed><summary>Root</summary>

| File        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                    | Module      |
|:------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------|
| App.tsx     | This code script imports React, Text, TouchableOpacity and NavigationContainer from'react-native' as well as createNativeStackNavigator and DataProvider from'./context/DataProvider' and HomeScreen and Information from'./screens'. It sets up a NavigationContainer with a Stack.Navigator which contains two screens, Home and Information, each with their own styling options. DataProvider is used within the script. | App.tsx     |
| .prettierrc | This code script specifies formatting settings for JavaScript code, such as always using arrow parentheses, using single quotes, and setting tab width to 4. It also includes other settings regarding bracket spacing, whitespace sensitivity, and trailing commas.                                                                                                                                                       | .prettierrc |

</details>

<details closed><summary>Screens</summary>

| File           | Summary                                                                                                                                                                                                                                                                                      | Module                 |
|:---------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------|
| Information.tsx | This code script creates a React component, Information, which renders a View and Text component. The View is styled using StyleSheet.create.                                                                                                                                                 | screens/Information.tsx |
| HomeScreen.tsx | This script imports the React library and components from'react-native', then imports a Layout, ListMessage, and InputMessage component from a local directory. It then renders the Layout component, which includes the ListMessage and InputMessage components, in a HomeScreen component. | screens/HomeScreen.tsx |

</details>

<details closed><summary>Server</summary>

| File      | Summary                                                                                                                                                                                                                                                          | Module           |
|:----------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| index.js  | This code script creates a server using Express and CORS, configures OpenAI to use an organization and API key, and listens on port 3000. When a user sends a POST request to the'/api/chat' endpoint, it generates a response with text, model, and usage data. | server/index.js  |
| config.js | This code imports configuration from a'dotenv' package and assigns them to environment variables so they can be used for the OpenAI API.                                                                                                                         | server/config.js |

</details>

<details closed><summary>Types</summary>

| File       | Summary                                                                                                                                                                                                                 | Module           |
|:-----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| types.d.ts | This code script defines an interface for a message type, including the details of the user who sent it, when it was created, its model type, the text content, and usage details such as prompt and completion tokens. | types/types.d.ts |

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

