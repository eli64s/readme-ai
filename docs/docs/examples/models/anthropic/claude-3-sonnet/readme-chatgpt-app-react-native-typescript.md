<div id="top">

<!-- HEADER STYLE: COMPACT -->
<img src="readmeai/assets/logos/orange.svg" width="30%" align="left" style="margin-right: 15px">

# CHATGPT-APP-REACT-NATIVE-TYPESCRIPT
<em>Unleash AI-powered conversations in your pocket instantly</em>

<!-- BADGES -->
<img src="https://img.shields.io/github/license/Yuberley/ChatGPT-App-React-Native-TypeScript?style=plastic&logo=opensourceinitiative&logoColor=white&color=0077cc" alt="license">
<img src="https://img.shields.io/github/last-commit/Yuberley/ChatGPT-App-React-Native-TypeScript?style=plastic&logo=git&logoColor=white&color=0077cc" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/Yuberley/ChatGPT-App-React-Native-TypeScript?style=plastic&color=0077cc" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/Yuberley/ChatGPT-App-React-Native-TypeScript?style=plastic&color=0077cc" alt="repo-language-count">

<em>Built with the tools and technologies:</em>

<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=plastic&logo=JavaScript&logoColor=black" alt="JavaScript">
<img src="https://img.shields.io/badge/TypeScript-3178C6.svg?style=plastic&logo=TypeScript&logoColor=white" alt="TypeScript">

<br clear="left"/>

## 🔷 Table of Contents

<details>
<summary>Table of Contents</summary>

- [🔷 Table of Contents](#-table-of-contents)
- [🌀 Overview](#-overview)
- [🔶 Features](#-features)
- [🔺 Project Structure](#-project-structure)
    - [🔹 Project Index](#-project-index)
- [🔸 Getting Started](#-getting-started)
    - [① Prerequisites](#-prerequisites)
    - [② Installation](#-installation)
    - [③ Usage](#-usage)
    - [④ Testing](#-testing)
- [🔳 Roadmap](#-roadmap)
- [🔲 Contributing](#-contributing)
- [◼ ️ License](#-license)
- [✨ Acknowledgments](#-acknowledgments)

</details>

---

## 🌀 Overview

ChatGPT-App-React-Native-TypeScript is a powerful starter kit for building AI-powered chat applications using React Native and TypeScript. It combines modern web technologies with artificial intelligence to streamline development.

**Why ChatGPT-App-React-Native-TypeScript?**

This project accelerates the creation of sophisticated AI chat applications. The core features include:

- **🚀 React Native + TypeScript:** Ensures type-safe, cross-platform development
- **🤖 OpenAI Integration:** Seamlessly incorporates AI-powered chat functionality
- **🔄 Context API:** Efficiently manages state across components
- **🖥️ Express.js Server:** Handles API requests and enhances security
- **🎣 Custom Hooks:** Promotes code reuse for data fetching
- **🧩 Modular Architecture:** Improves maintainability and scalability

---

## 🔶 Features

|      | Component       | Details                              |
| :--- | :-------------- | :----------------------------------- |
| ⚙️  | **Architecture**  | <ul><li>React Native mobile app</li><li>TypeScript for type safety</li><li>Expo managed workflow</li><li>React Navigation for routing</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>ESLint for linting</li><li>Prettier for code formatting</li><li>TypeScript for static typing</li></ul> |
| 📄 | **Documentation** | <ul><li>Basic README with setup instructions</li><li>In-code comments for complex logic</li></ul> |
| 🔌 | **Integrations**  | <ul><li>OpenAI API for ChatGPT functionality</li><li>AsyncStorage for local data persistence</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Component-based architecture</li><li>Separate files for screens and components</li><li>Utility functions in separate files</li></ul> |
| 🧪 | **Testing**       | <ul><li>No visible testing setup</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Optimized rendering with `React.memo()`</li><li>Efficient state management with `useReducer`</li></ul> |
| 🛡️ | **Security**      | <ul><li>Environment variables for API key storage</li><li>Input validation for user messages</li></ul> |
| 📦 | **Dependencies**  | <ul><li>React Native</li><li>Expo</li><li>React Navigation</li><li>Axios for API requests</li><li>react-native-gifted-chat for UI</li></ul> |

---

## 🔺 Project Structure

```sh
└── ChatGPT-App-React-Native-TypeScript/
    ├── App.tsx
    ├── LICENSE
    ├── README.md
    ├── app.json
    ├── assets
    │   ├── adaptive-icon.png
    │   ├── favicon.png
    │   ├── icon.png
    │   └── splash.png
    ├── components
    │   ├── InputMessage.tsx
    │   ├── Layout.tsx
    │   ├── ListMessage.tsx
    │   └── Message.tsx
    ├── constants
    │   └── constants.ts
    ├── context
    │   └── DataProvider.tsx
    ├── data
    │   └── messages.ts
    ├── helpers
    │   └── getMessage.ts
    ├── hooks
    │   └── useFetchMessage.ts
    ├── others
    │   └── screen.png
    ├── package-lock.json
    ├── package.json
    ├── screens
    │   ├── HomeScreen.tsx
    │   └── Information.tsx
    ├── server
    │   ├── .gitignore
    │   ├── config.js
    │   ├── index.js
    │   ├── package-lock.json
    │   └── package.json
    ├── tsconfig.json
    └── types
        └── types.d.ts
```

### 🔹 Project Index

<details open>
	<summary><b><code>CHATGPT-APP-REACT-NATIVE-TYPESCRIPT/</code></b></summary>
	<!-- __root__ Submodule -->
	<details>
		<summary><b>__root__</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ __root__</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/App.tsx'>App.tsx</a></b></td>
					<td style='padding: 8px;'>- Home and Information<br>- The app utilizes a DataProvider for state management and customizes the navigation header with styling and an About button<br>- This file establishes the core architecture for the user interface and navigation flow of the application.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- types Submodule -->
	<details>
		<summary><b>types</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ types</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/types/types.d.ts'>types.d.ts</a></b></td>
					<td style='padding: 8px;'>- Defines essential TypeScript interfaces for the projects data structures<br>- Establishes User and Usage interfaces, along with a comprehensive MessageType interface that incorporates user information, message content, and usage statistics<br>- These type definitions ensure consistent data handling and provide a robust foundation for type-safe development across the application, enhancing code reliability and maintainability.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- context Submodule -->
	<details>
		<summary><b>context</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ context</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/context/DataProvider.tsx'>DataProvider.tsx</a></b></td>
					<td style='padding: 8px;'>- Creates and provides a data context for managing text input across the application<br>- Utilizes Reacts context API to share state between components without prop drilling<br>- Exports a DataProvider component that wraps child components, allowing them to access and update the textInput state through the context<br>- Facilitates centralized state management and improves component reusability in the projects architecture.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- constants Submodule -->
	<details>
		<summary><b>constants</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ constants</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/constants/constants.ts'>constants.ts</a></b></td>
					<td style='padding: 8px;'>- Defines a crucial constant for API communication in the project<br>- Establishes the base URL for API requests, pointing to a local development server<br>- This constant likely serves as a central reference point for all API-related operations throughout the application, ensuring consistency in network requests and simplifying URL management across different components and modules.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- server Submodule -->
	<details>
		<summary><b>server</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ server</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/server/index.js'>index.js</a></b></td>
					<td style='padding: 8px;'>- Serves as the main entry point for the server application, setting up an Express.js server with CORS support and OpenAI integration<br>- Defines routes for handling API requests, including a chat endpoint that processes user messages using OpenAIs API<br>- Configures the server to listen on port 3000 and provides basic error handling for empty messages.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/server/config.js'>config.js</a></b></td>
					<td style='padding: 8px;'>- Configures environment variables for the server application, specifically for OpenAI API integration<br>- Utilizes the dotenv package to load environment variables from a.env file, ensuring secure storage of sensitive information like API keys and organization identifiers<br>- Exports an environment object containing these variables, making them accessible throughout the server-side codebase for OpenAI-related functionality.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- screens Submodule -->
	<details>
		<summary><b>screens</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ screens</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/screens/Information.tsx'>Information.tsx</a></b></td>
					<td style='padding: 8px;'>- Defines the Information screen component for a React Native application<br>- Renders a simple view with centered text displaying Information<br>- Utilizes React Native's StyleSheet for basic styling<br>- As part of the screens directory, this component likely serves as a standalone page or section within the app's navigation structure, potentially providing user information or app details.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/screens/HomeScreen.tsx'>HomeScreen.tsx</a></b></td>
					<td style='padding: 8px;'>- HomeScreen component serves as the main interface for the messaging application<br>- It integrates key elements such as the message list and input field within a layout structure<br>- By combining these components, HomeScreen creates a cohesive user experience, allowing users to view existing messages and compose new ones<br>- This screen forms the core of the apps functionality, centralizing message-related interactions in one place.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- components Submodule -->
	<details>
		<summary><b>components</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ components</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/components/InputMessage.tsx'>InputMessage.tsx</a></b></td>
					<td style='padding: 8px;'>- InputMessage component handles user message input and submission in the chat interface<br>- It provides a text input field and a send button, allowing users to enter and send messages<br>- Upon submission, it creates a new message object with a unique ID, timestamp, and user details, then updates the application state through the DataContext<br>- The component also manages its own local state for the input text.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/components/Layout.tsx'>Layout.tsx</a></b></td>
					<td style='padding: 8px;'>- Layout component serves as a wrapper for the applications content, providing a consistent structure and styling<br>- It sets up a container with a dark background, centers its children, and applies padding<br>- The component also configures the status bar appearance<br>- By encapsulating these common layout elements, it ensures a uniform look and feel across different screens or views within the React Native application.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/components/Message.tsx'>Message.tsx</a></b></td>
					<td style='padding: 8px;'>- Message component renders individual chat messages in the application<br>- It displays the users avatar, name, and message text, differentiating between user and ChatGPT messages through styling<br>- The component allows users to copy message content to the clipboard with a tap, enhancing usability<br>- It contributes to the overall chat interface by presenting messages in a visually appealing and interactive manner.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/components/ListMessage.tsx'>ListMessage.tsx</a></b></td>
					<td style='padding: 8px;'>- Renders and manages a list of messages in a chat-like interface<br>- Utilizes React hooks and context to handle state, fetch new messages, and update the display<br>- Implements a FlatList component for efficient rendering of messages, along with a pull-to-refresh functionality<br>- Integrates with the broader application architecture by consuming data from context and custom hooks.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- hooks Submodule -->
	<details>
		<summary><b>hooks</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ hooks</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/hooks/useFetchMessage.ts'>useFetchMessage.ts</a></b></td>
					<td style='padding: 8px;'>- Implements a custom React hook, useFetchMessage, for retrieving and managing message data<br>- Handles asynchronous fetching, loading states, and data updates based on the provided message input<br>- Integrates with the getMessage helper function and utilizes Reacts useState and useEffect hooks for state management and side effects<br>- Enhances code reusability and separation of concerns in the applications data fetching logic.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- helpers Submodule -->
	<details>
		<summary><b>helpers</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ helpers</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/helpers/getMessage.ts'>getMessage.ts</a></b></td>
					<td style='padding: 8px;'>- Facilitates communication with an AI model by handling message requests<br>- Exports a function that takes a user message, constructs a request body, and sends it to a specified API endpoint<br>- Retrieves and returns the AI-generated response, enabling seamless integration of AI-powered chat functionality within the applications broader architecture.</td>
				</tr>
			</table>
		</blockquote>
	</details>
</details>

---

## 🔸 Getting Started

### ① Prerequisites

This project requires the following dependencies:

- **Programming Language:** TypeScript

### ② Installation

Build ChatGPT-App-React-Native-TypeScript from the source and install dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd ChatGPT-App-React-Native-TypeScript
    ```

3. **Install the dependencies:**

echo 'INSERT-INSTALL-COMMAND-HERE'

### ③ Usage

Run the project with:

echo 'INSERT-RUN-COMMAND-HERE'

### ④ Testing

Chatgpt-app-react-native-typescript uses the {__test_framework__} test framework. Run the test suite with:

echo 'INSERT-TEST-COMMAND-HERE'

---

## 🔳 Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🔲 Contributing

- **💬 [Join the Discussions](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/issues)**: Submit bugs found or log feature requests for the `ChatGPT-App-React-Native-TypeScript` project.
- **💡 [Submit Pull Requests](https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
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
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/Yuberley/ChatGPT-App-React-Native-TypeScript/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=Yuberley/ChatGPT-App-React-Native-TypeScript">
   </a>
</p>
</details>

---

## ◼️ License

Chatgpt-app-react-native-typescript is protected under the [LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## ✨ Acknowledgments

- Credit `contributors`, `inspiration`, `references`, etc.

<div align="left"><a href="#top">⬆ Return</a></div>

---

<!-- README-AI COMMAND: -->
<!--
```sh
readmeai \
    --repository 'https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript' \
    --output 'docs/docs/examples/ai-providers/anthropic/claude-3-sonnet/readme-chatgpt-app-react-native-typescript.md' \
    --badge-style 'plastic' \
    --badge-color '0077cc' \
    --logo 'ORANGE' \
    --header-style 'COMPACT' \
    --navigation-style 'ACCORDION' \
    --emojis 'ascension' \
    --temperature 0.442 \
    --tree-max-depth 4 \
    --api anthropic \
    --model claude-3-5-sonnet-20240620
```
-->
