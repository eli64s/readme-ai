
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
javascript-react-chat-app
</h1>
<h3 align="center">📍 Chat Smarter with JavaScript React Chat App!</h3>
<h3 align="center">🚀 Developed with the software and tools below.</h3>
<p align="center">

<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=for-the-badge&logo=HTML5&logoColor=white" alt="" />
<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=for-the-badge&logo=JavaScript&logoColor=black" alt="html-react-parser" />
<img src="https://img.shields.io/badge/Redux-764ABC.svg?style=for-the-badge&logo=Redux&logoColor=white" alt="sample" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white" alt="txt" />
<img src="https://img.shields.io/badge/React-61DAFB.svg?style=for-the-badge&logo=React&logoColor=black" alt="@testing-library/user-event" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="redux-thunk" />
</p>

</div>

---

## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍Overview](#-introdcution)
- [🔮 Features](#-features)
- [⚙️ Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🏎💨 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [🪪 License](#-license)
- [📫 Contact](#-contact)
- [🙏 Acknowledgments](#-acknowledgments)

---


## 📍Overview

This is a GitHub project that provides a tutorial for creating a JavaScript and React-based chat application with real-time messaging features such as file sharing, emoji support, and private messaging. The tutorial includes detailed instructions on how to set up the application as well as how to add additional features.

## 🔮 Feautres

> `[📌  INSERT-PROJECT-FEATURES]`

---


<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## ⚙️ Project Structure


```bash
repo
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── SECURITY.md
├── SUPPORT.md
├── Screenshots
│   ├── constants.png
│   ├── home.png
│   ├── login.png
│   ├── logo.png
│   └── main.png
├── package-lock.json
├── package.json
├── postinstall.js
├── public
│   ├── cometchat_rounded@3x.png
│   ├── cometchat_rounded_white@3x.png
│   ├── favicon.ico
│   ├── index.html
│   ├── manifest.json
│   └── robots.txt
└── src
    ├── PrivateRoute
    │   └── index.js
    ├── babel.config.json
    ├── consts.js
    ├── defaultPages
    │   ├── App
    │   │   ├── index.js
    │   │   └── style.js
    │   ├── HomePage
    │   │   ├── index.js
    │   │   ├── resources
    │   │   │   ├── CometChatUI.png
    │   │   │   ├── components.png
    │   │   │   └── wall.png
    │   │   └── style.js
    │   └── KitchenSinkApp
    │       ├── index.js
    │       ├── loader.js
    │       └── style.js
    ├── index.js
    ├── index.scss
    ├── main.js
    ├── serviceWorker.js
    └── store
        ├── action.js
        ├── actionTypes.js
        └── reducer.js

11 directories, 39 files
```

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 💻 Modules

<details closed><summary>App</summary>

| File     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Module                        |
|:---------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------|
| index.js | This code imports React, React Router, and Redux to create a Router with PrivateRoute components for CometChatUI, CometChatConversationListWithMessages, CometChatGroupListWithMessages, CometChatUserListWithMessages, CometChatConversationList, CometChatGroupList, CometChatUserList, and CometChatMessages. It also imports HomePage and KitchenSinkApp as components and connects them to the Redux store. The code also includes a componentDidMount() method to get the logged in user. | src/defaultPages/App/index.js |
| style.js | This function creates an object containing the width and height set to 100% of the viewport.                                                                                                                                                                                                                                                                                                                                                                                                    | src/defaultPages/App/style.js |

</details>

<details closed><summary>Homepage</summary>

| File     | Summary                                                                                                                                                                                                                                      | Module                             |
|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------|
| index.js | Error generating file summary.                                                                                                                                                                                                               | src/defaultPages/HomePage/index.js |
| style.js | This code exports a series of styles for a UI component, including display, flex direction, align items, justify content, padding, margin, width, and font size. It also includes hover styles and media queries for different screen sizes. | src/defaultPages/HomePage/style.js |

</details>

<details closed><summary>Kitchensinkapp</summary>

| File      | Summary                                                                                                                                                                                                                                                                                                                                                            | Module                                    |
|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------|
| index.js  | This code is a React component for a Kitchen Sink App that allows users to log in with one of five sample users or with a UID. It imports React, Emotion, and Redux libraries, and includes functions to handle login and loading, as well as styling for the app. It also utilizes the CometChatAvatar component from the CometChat Pro React UI Kit.             | src/defaultPages/KitchenSinkApp/index.js  |
| style.js  | This code exports several styles for use in a React component, including wrapperStyle, errorStyle, titleStyle, subtitleStyle, userContainerStyle, userWrapperStyle, thumbnailWrapperStyle, uidWrapperStyle, inputWrapperStyle, and loginBtn. These styles provide flexbox layout, font size, color, width, text alignment, and hover effects for various elements. | src/defaultPages/KitchenSinkApp/style.js  |
| loader.js | This code creates a loading style with a transparent overlay, a spinner animation, and a radial gradient background. It is designed to be fixed in the center of the page and have a z-index of 999.                                                                                                                                                               | src/defaultPages/KitchenSinkApp/loader.js |

</details>

<details closed><summary>Privateroute</summary>

| File     | Summary                                                                                                                                                                                                       | Module                    |
|:---------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------|
| index.js | PrivateRoute is a React component that allows users to access a path if they are logged in, otherwise redirects them to the login page. It is connected to the Redux store to check if the user is logged in. | src/PrivateRoute/index.js |

</details>

<details closed><summary>Public</summary>

| File        | Summary                                                                                                                                                                                                                                         | Module             |
|:------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
| favicon.ico | This code is an error message indicating that a file is not in a text or UTF-8 format and therefore cannot be decoded.                                                                                                                          | public/favicon.ico |
| index.html  | This code sets up the HTML structure for a web application, including the title, meta tags, and manifest. It also sets up the basic structure of the page, including the root div. It requires JavaScript to be enabled to run the application. | public/index.html  |

</details>

<details closed><summary>Root</summary>

| File           | Summary                                                                                                                             | Module         |
|:---------------|:------------------------------------------------------------------------------------------------------------------------------------|:---------------|
| postinstall.js | This code downloads a zip file from a given URL, extracts it, moves it to a specified directory, and deletes the original zip file. | postinstall.js |

</details>

<details closed><summary>Src</summary>

| File             | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Module               |
|:-----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------|
| index.scss       | This code sets the font family of the body to "Inter", sans-serif, sets font size to 1.4rem, and sets font size of h4 to 2.2rem. It also sets all elements to box-sizing: border-box, and sets all links to white color and no text decoration. Additionally, it sets all images to max-width: 100%, and all buttons, inputs, select, and textareas to font-family: inherit and font-size: 100%. Finally, it sets all h1-h6 elements to the same font family as the body. | src/index.scss       |
| consts.js        | This code exports a constant object containing the necessary credentials to access the CometChat API, including an app ID, region, and authentication key.                                                                                                                                                                                                                                                                                                                | src/consts.js        |
| index.js         | This code imports the necessary React components and libraries to create a store with the reducer and thunk middleware, initiate CometChat with an appID and region, and render the App component in the DOM. It also unregisters the service worker.                                                                                                                                                                                                                     | src/index.js         |
| main.js          | This code creates a function called'sum_of_digits' which takes a single argument, an integer, and returns the sum of the digits of the integer. The function iterates through each digit of the integer, adds it to a total, and returns the total.                                                                                                                                                                                                                       | src/main.js          |
| serviceWorker.js | This code registers a service worker to enable faster loading and offline capabilities on subsequent visits to a page in production. It also ensures that deployed updates are only seen on subsequent visits after all existing tabs have been closed. To learn more about the benefits of this model, visit the provided link.                                                                                                                                          | src/serviceWorker.js |

</details>

<details closed><summary>Store</summary>

| File           | Summary                                                                                                                                                                                                        | Module                   |
|:---------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------|
| action.js      | This code imports CometChat from the @cometchat-pro/chat library and defines several functions to handle authentication, logging out, and setting an authentication redirect path.                             | src/store/action.js      |
| reducer.js     | This code creates a reducer to handle authentication state changes, including setting user data, logging in/out, and setting the redirect path. It also defines the initial state of the authentication state. | src/store/reducer.js     |
| actionTypes.js | This code defines four constants related to authentication processes and one constant for setting an authentication redirect path.                                                                             | src/store/actionTypes.js |

</details>

<hr />

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> `[📌  INSERT-PROJECT-PREREQUISITES]`

### 💻 Installation

1. Clone the javascript-react-chat-app repository:
```sh
git clone https://github.com/cometchat-pro/javascript-react-chat-app
```

2. Change to the project directory:
```sh
cd javascript-react-chat-app
```

3. Install the dependencies:
```sh
npm install
```

### 🤖 Using javascript-react-chat-app

```sh
npm start
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

