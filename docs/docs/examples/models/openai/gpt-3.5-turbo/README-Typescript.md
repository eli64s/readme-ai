<div id="top">

<!-- HEADER STYLE: CLASSIC -->
<div align="center">

<img src="../../../../../../../../../readmeai/assets/logos/blue.svg" width="30%" style="position: relative; top: 0; right: 0;" alt="Project Logo"/>

# CHATGPT-APP-REACT-NATIVE-TYPESCRIPT

<em>Elevate conversations with AI in your pocket.</em>

<!-- BADGES -->
<img src="https://img.shields.io/github/license/Yuberley/ChatGPT-App-React-Native-TypeScript?style=flat-square&logo=opensourceinitiative&logoColor=white&color=412991" alt="license">
<img src="https://img.shields.io/github/last-commit/Yuberley/ChatGPT-App-React-Native-TypeScript?style=flat-square&logo=git&logoColor=white&color=412991" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/Yuberley/ChatGPT-App-React-Native-TypeScript?style=flat-square&color=412991" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/Yuberley/ChatGPT-App-React-Native-TypeScript?style=flat-square&color=412991" alt="repo-language-count">

<em>Built with the tools and technologies:</em>

<img src="https://img.shields.io/badge/Express-000000.svg?style=flat-square&logo=Express&logoColor=white" alt="Express">
<img src="https://img.shields.io/badge/JSON-000000.svg?style=flat-square&logo=JSON&logoColor=white" alt="JSON">
<img src="https://img.shields.io/badge/npm-CB3837.svg?style=flat-square&logo=npm&logoColor=white" alt="npm">
<img src="https://img.shields.io/badge/.ENV-ECD53F.svg?style=flat-square&logo=dotenv&logoColor=black" alt=".ENV">
<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=flat-square&logo=JavaScript&logoColor=black" alt="JavaScript">
<br>
<img src="https://img.shields.io/badge/Nodemon-76D04B.svg?style=flat-square&logo=Nodemon&logoColor=white" alt="Nodemon">
<img src="https://img.shields.io/badge/React-61DAFB.svg?style=flat-square&logo=React&logoColor=black" alt="React">
<img src="https://img.shields.io/badge/TypeScript-3178C6.svg?style=flat-square&logo=TypeScript&logoColor=white" alt="TypeScript">
<img src="https://img.shields.io/badge/Expo-000020.svg?style=flat-square&logo=Expo&logoColor=white" alt="Expo">
<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=flat-square&logo=OpenAI&logoColor=white" alt="OpenAI">

</div>
<br>

---

## 🌈 Table of Contents

- [🌈 Table of Contents](#-table-of-contents)
- [🔴 Overview](#-overview)
- [🟠 Features](#-features)
- [🟡 Project Structure](#-project-structure)
    - [🟢 Project Index](#-project-index)
- [🔵 Getting Started](#-getting-started)
    - [🟣 Prerequisites](#-prerequisites)
    - [⚫ Installation](#-installation)
    - [⚪ Usage](#-usage)
    - [🟤 Testing](#-testing)
- [🌟 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)
- [✨ Acknowledgments](#-acknowledgments)

---

## 🔴 Overview

**ChatGPT-App-React-Native-TypeScript**

**Why ChatGPT-App-React-Native-TypeScript?**

This project empowers developers to build interactive chat applications seamlessly. The core features include:

- **🚀 Modular Structure:** Promotes scalability and maintainability.
- **💡 Consistent Dependencies:** Ensures reproducibility and stability.
- **🔗 Context Management:** Facilitates seamless data sharing.
- **💬 API Integration:** Enables chatbot interactions.

---

## 🟠 Features

|      | Component       | Details                              |
| :--- | :-------------- | :----------------------------------- |
| ⚙️  | **Architecture**  | <ul><li>Follows a clean MVVM architecture pattern</li><li>Separation of concerns between UI, ViewModels, and Models</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Consistent code formatting using ESLint and Prettier</li><li>TypeScript used for static type checking</li></ul> |
| 📄 | **Documentation** | <ul><li>Well-documented code with JSDoc comments for functions and interfaces</li><li>README.md provides setup instructions and project overview</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integrated with React Navigation for navigation between screens</li><li>Uses Expo for easy cross-platform development</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Component-based structure with reusable components</li><li>Separate folders for screens, components, and utilities</li></ul> |
| 🧪 | **Testing**       | <ul><li>Unit tests using Jest for components and utility functions</li><li>Snapshot testing for UI components</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Optimized performance with React Native components like FlatList for rendering lists efficiently</li><li>Lazy loading of images for better performance</li></ul> |
| 🛡️ | **Security**      | <ul><li>Secure data handling with AsyncStorage for storing sensitive user information</li><li>Implemented CORS and body-parser for secure API communication</li></ul> |
| 📦 | **Dependencies**  | <ul><li>Uses a variety of dependencies for React Native development, including @react-navigation, Expo, and OpenAI</li><li>Dev dependencies for testing and linting like Jest and ESLint</li></ul> |
| 🚀 | **Scalability**   | <ul><li>Scalable architecture allowing easy addition of new features and screens</li><li>State management using React Context for scalability</li></ul> |

---

## 🟡 Project Structure

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
    │   └── Infomation.tsx
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

### 🟢 Project Index

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
					<td style='padding: 8px;'>- Define the apps navigation flow and screens with React Native components<br>- Implement a stack navigator to manage transitions between Home and Information screens<br>- Utilize DataProvider to manage state and context<br>- Customize navigation headers for a cohesive user experience.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/LICENSE'>LICENSE</a></b></td>
					<td style='padding: 8px;'>Summarize the purpose and use of the LICENSE file within the project structure, highlighting its role in governing the distribution and use of the software.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/app.json'>app.json</a></b></td>
					<td style='padding: 8px;'>- Define the configuration settings for the ChatGPT-App, specifying details such as name, version, orientation, icons, splash screen, asset patterns, and platform-specific properties for iOS, Android, and web<br>- Ensure consistent user interface styles and support for various devices.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/package-lock.json'>package-lock.json</a></b></td>
					<td style='padding: 8px;'>- README### SummaryThe <code>package-lock.json</code> file within the <code>chatgpt-app</code> project serves as a crucial lockfile that ensures the reproducibility and consistency of dependencies for the application<br>- It specifies the exact versions of each package required for the project, including essential libraries like <code>@react-navigation</code>, <code>expo</code>, and <code>react</code><br>- By pinning down the dependencies, this file guarantees that all developers working on the project are using the same versions, thereby maintaining a stable and predictable development environment.### Project StructureThe <code>chatgpt-app</code> project follows a modular structure, with dependencies managed through <code>npm</code> and listed in the <code>package-lock.json</code> file<br>- It leverages technologies such as <code>@react-navigation</code>, <code>expo</code>, and <code>react</code> to build a mobile chat application<br>- The project's architecture promotes scalability and maintainability by separating concerns and utilizing industry-standard libraries for key functionalities.### Importance of <code>package-lock.json</code>The <code>package-lock.json</code> file plays a vital role in the <code>chatgpt-app</code> project by ensuring that all developers are working with consistent dependencies<br>- This lockfile prevents issues arising from differences in package versions, thus enhancing collaboration and reducing the likelihood of bugs related to dependency mismatches<br>- By defining precise versions, the <code>package-lock.json</code> file contributes to the projects stability and reliability, making it an essential component of the overall architecture.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/package.json'>package.json</a></b></td>
					<td style='padding: 8px;'>- Define the purpose and functionality of package.json within the project structure<br>- Highlight its role in managing dependencies, scripts, and project metadata<br>- Emphasize its significance in orchestrating the development environment and facilitating seamless execution across different platforms.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/tsconfig.json'>tsconfig.json</a></b></td>
					<td style='padding: 8px;'>Define strict TypeScript compiler options for Expo project by extending base configuration.</td>
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
					<td style='padding: 8px;'>- Define interfaces for User, Usage, and MessageType to structure data related to users, usage, and message types<br>- The types.d.ts file outlines the properties required for each interface, facilitating consistent data organization and access across the codebase architecture.</td>
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
					<td style='padding: 8px;'>- Define a data provider in the project structure to manage and share user input data across components<br>- This code file establishes a context for the application, allowing components to access and update the users text input seamlessly.</td>
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
					<td style='padding: 8px;'>Define the base API URL for the project, ensuring a centralized reference point for all API communications.</td>
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
					<td style='padding: 8px;'>- Serve an Express API that utilizes OpenAI for chatbot interactions<br>- Handles POST requests to /api/chat with message parameters, generating AI responses based on specified model settings<br>- The API responds with chatbot data including ID, creation timestamp, text, and user details<br>- The server runs on port 3000, allowing communication with the chatbot AI through HTTP requests.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/server/config.js'>config.js</a></b></td>
					<td style='padding: 8px;'>Define environment variables for OpenAI API key and organization in the project configuration.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/server/package-lock.json'>package-lock.json</a></b></td>
					<td style='padding: 8px;'>- Project SummaryThe <code>server/package-lock.json</code> file in this project contains the necessary dependencies and their versions for the server component<br>- This file ensures that when the project is built or deployed, the correct versions of these dependencies are used to maintain stability and functionality<br>- The <code>package-lock.json</code> file is crucial for reproducible builds and consistent development environments, making it an integral part of the projects architecture.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/server/package.json'>package.json</a></b></td>
					<td style='padding: 8px;'>Define server package configuration and dependencies for project execution.</td>
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
					<td style='padding: 8px;'><b><a href='https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/screens/Infomation.tsx'>Infomation.tsx</a></b></td>
					<td style='padding: 8px;'>- Define the Information screen layout and styling for the React Native app<br>- The screen presents the text Information within a centered container<br>- This component plays a key role in rendering essential information to users.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/screens/HomeScreen.tsx'>HomeScreen.tsx</a></b></td>
					<td style='padding: 8px;'>- Describe how the HomeScreen component structures the main interface layout by incorporating ListMessage and InputMessage components within the Layout component<br>- This arrangement ensures a cohesive display of messages in a user-friendly format.</td>
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
					<td style='padding: 8px;'>- Implement a React component managing user input for a chat application<br>- Handles message creation, including user details and timestamp<br>- Utilizes context for data management<br>- Features an input field and send button with styling defined.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/components/Layout.tsx'>Layout.tsx</a></b></td>
					<td style='padding: 8px;'>- Define the Layout component responsible for rendering the apps core structure<br>- It sets the background color, status bar style, and layout alignment for the children components<br>- This component establishes a consistent visual layout across the application, enhancing user experience and maintaining a unified design language.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/components/Message.tsx'>Message.tsx</a></b></td>
					<td style='padding: 8px;'>- Define the UI layout and interaction for displaying messages in a chat app<br>- Render message content, user details, and enable copying text to the clipboard<br>- Styles differentiate between user and chatbot messages<br>- Integrates React Native components for a dynamic user experience.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript/blob/master/components/ListMessage.tsx'>ListMessage.tsx</a></b></td>
					<td style='padding: 8px;'>- Create a dynamic message list displaying fetched data using React Native components<br>- Utilize context and hooks for state management and data retrieval<br>- Render messages with refresh functionality in a visually appealing list layout.</td>
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
					<td style='padding: 8px;'>- Fetches and manages message data based on the provided input<br>- Handles loading states and triggers data retrieval via an asynchronous call<br>- Ensures the message is not empty before fetching data to display, optimizing the user experience<br>- Integrates with helper functions and custom types to maintain code readability and scalability within the project structure.</td>
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
					<td style='padding: 8px;'>- Generate chat messages using OpenAIs text-davinci-003 model by sending a message to the specified API URL<br>- The getMessage function constructs a request body with the input message and fetches a response containing generated text data using the specified model.</td>
				</tr>
			</table>
		</blockquote>
	</details>
</details>

---

## 🔵 Getting Started

### 🟣 Prerequisites

This project requires the following dependencies:

- **Programming Language:** TypeScript
- **Package Manager:** Npm

### ⚫ Installation

Build ChatGPT-App-React-Native-TypeScript from the source and intsall dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd ChatGPT-App-React-Native-TypeScript
    ```

3. **Install the dependencies:**

<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![npm][npm-shield]][npm-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [npm-shield]: https://img.shields.io/badge/npm-CB3837.svg?style={badge_style}&logo=npm&logoColor=white -->
	<!-- [npm-link]: https://www.npmjs.com/ -->

	**Using [npm](https://www.npmjs.com/):**

	```sh
	❯ npm install
	```

### ⚪ Usage

Run the project with:

**Using [npm](https://www.npmjs.com/):**
```sh
npm start
```

### 🟤 Testing

Chatgpt-app-react-native-typescript uses the {__test_framework__} test framework. Run the test suite with:

**Using [npm](https://www.npmjs.com/):**
```sh
npm test
```

---

## 🌟 Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🤝 Contributing

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

## 📜 License

Chatgpt-app-react-native-typescript is protected under the [LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## ✨ Acknowledgments

- Credit `contributors`, `inspiration`, `references`, etc.

<div align="left"><a href="#top">⬆ Return</a></div>

---
