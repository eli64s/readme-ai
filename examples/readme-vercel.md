<p align="center">
    <img src="/docs/assets/images/dalle/github-readme-quotes.png" align="center" width="30%">
</p>
<p align="center"><h1 align="center">GITHUB-README-QUOTES</h1></p>
<p align="center"><em>Code consistency, creativity, and motivation unleashed!</em></p>
<p align="center">
	<img src="https://img.shields.io/github/license/PiyushSuthar/github-readme-quotes?style=flat-square&logo=opensourceinitiative&logoColor=white&color=skyblue" alt="license">
	<img src="https://img.shields.io/github/last-commit/PiyushSuthar/github-readme-quotes?style=flat-square&logo=git&logoColor=white&color=skyblue" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/PiyushSuthar/github-readme-quotes?style=flat-square&color=skyblue" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/PiyushSuthar/github-readme-quotes?style=flat-square&color=skyblue" alt="repo-language-count">
</p>
<p align="center">Built with the tools and technologies:</p>
<p align="center">
	<img src="https://img.shields.io/badge/Vercel-000000.svg?style=flat-square&logo=Vercel&logoColor=white" alt="Vercel">
	<img src="https://img.shields.io/badge/npm-CB3837.svg?style=flat-square&logo=npm&logoColor=white" alt="npm">
	<img src="https://img.shields.io/badge/Prettier-F7B93E.svg?style=flat-square&logo=Prettier&logoColor=black" alt="Prettier">
	<img src="https://img.shields.io/badge/TypeScript-3178C6.svg?style=flat-square&logo=TypeScript&logoColor=white" alt="TypeScript">
	<img src="https://img.shields.io/badge/Axios-5A29E4.svg?style=flat-square&logo=Axios&logoColor=white" alt="Axios">
</p>
<br>

## 🔗 Table of Contents

I. [📍 Overview](#-overview)
II. [👾 Features](#-features)
III. [📁 Project Structure](#-project-structure)
IV. [🚀 Getting Started](#-getting-started)
V. [📌 Project Roadmap](#-project-roadmap)
VI. [🔰 Contributing](#-contributing)
VII. [🎗 License](#-license)
VIII. [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

**github-readme-quotes** is a project aimed at enhancing GitHub README profiles by dynamically displaying inspirational programming quotes in the form of customizable SVG images. It allows developers to add a touch of motivation and personalization to their repositories, creating a more engaging and interactive experience for visitors.

With **github-readme-quotes**, you can:
🎨 **Customizable Themes**: Personalize the appearance of the quote cards with different themes and color schemes.
🔄 **Dynamic Quote Generation**: Fetch random programming quotes to display fresh and motivational content.
📐 **SVG Card Customization**: Customize the layout, font, and border of the SVG cards to match your README style.
🚀 **Caching Support**: Implement caching mechanisms to improve performance and reduce external API calls.
🌐 **Vercel Integration**: Easily deploy and serve the generated SVG images using Vercel's serverless functions.

---

## 👾 Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Utilizes **TypeScript** for type safety and enhanced developer experience.</li><li>Implements **Vercel** for serverless functions and routing management.</li><li>Uses **Axios** for making HTTP requests to external APIs.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Includes a **Prettier** script in `package.json` for consistent code formatting.</li><li>Employs strict type-checking settings in `tsconfig.json` for improved code quality.</li><li>Utilizes a lockfile `pnpm-lock.yaml` to manage dependency versions and ensure reproducibility.</li></ul> |
| 📄 | **Documentation** | <ul><li>Primary language is **TypeScript**.</li><li>Contains documentation in various formats such as **JSON**, **YAML**, and **TypeScript**.</li><li>Defines installation and usage commands in the documentation for easy onboarding.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integrates with **Vercel** for hosting and serverless functions.</li><li>Utilizes **Axios** for fetching external API data.</li><li>Integrates with **npm** for package management.</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Separates components like fetcher, renderer, and themes into distinct modules for maintainability.</li><li>Defines specific card types like horizontal and vertical for modularity and extensibility.</li><li>Encapsulates font data and theme configurations within separate files for easy management.</li></ul> |
| 🧪 | **Testing**       | <ul><li>Includes testing commands in the documentation for running unit tests.</li><li>Ensures testability of components like fetcher and renderer for code reliability.</li><li>Tests the API functionality for fetching and rendering quotes dynamically.</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Supports caching of image responses to improve performance.</li><li>Optimizes SVG rendering for fast generation of quote cards.</li><li>Utilizes serverless functions for efficient quote generation and delivery.</li></ul> |
| 🛡️ | **Security**      | <ul><li>Follows security best practices for making external API requests.</li><li>Secures API endpoints to prevent unauthorized access.</li><li>Implements secure coding practices to prevent common vulnerabilities.</li></ul> |
| 📦 | **Dependencies**  | <ul><li>Lists key dependencies like **Axios**, **Vercel**, and **TypeScript** in `package.json`.</li><li>Specifies versions and dependencies accurately in the lockfile `pnpm-lock.yaml`.</li><li>Manages package installation using **npm** as the package manager.</li></ul> |

---

## 📁 Project Structure

```sh
└── github-readme-quotes/
    ├── .github
    │   └── FUNDING.yml
    ├── LICENSE
    ├── README.md
    ├── api
    │   └── index.ts
    ├── assets
    │   └── logo.png
    ├── package.json
    ├── pnpm-lock.yaml
    ├── src
    │   ├── fetcher
    │   │   └── fetch-quotes.ts
    │   └── renderer
    │       ├── constants.ts
    │       ├── render-svg.ts
    │       ├── theme
    │       └── type
    ├── tsconfig.json
    └── vercel.json
```


### 📂 Project Index
<details open>
	<summary><b><code>GITHUB-README-QUOTES/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/PiyushSuthar/github-readme-quotes/blob/master/pnpm-lock.yaml'>pnpm-lock.yaml</a></b></td>
				<td>- The code file `pnpm-lock.yaml` serves as a lockfile for managing dependencies within the project architecture<br>- It specifies the versions of various dependencies such as '@vercel/node', axios, prettier, typescript, and vercel, ensuring consistency and reproducibility in the project's environment<br>- This file plays a crucial role in maintaining a stable and predictable development environment by pinning down specific versions of dependencies required for the project.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/PiyushSuthar/github-readme-quotes/blob/master/vercel.json'>vercel.json</a></b></td>
				<td>- Defines memory allocation and maximum duration for API functions, and sets up a redirect to the project's GitHub page<br>- This configuration file plays a crucial role in managing serverless functions and routing within the project structure.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/PiyushSuthar/github-readme-quotes/blob/master/package.json'>package.json</a></b></td>
				<td>- Implements a script that formats code using Prettier across TypeScript, JSON, and Markdown files in the project<br>- The script ensures consistent code styling and readability, enhancing the overall maintainability and collaboration within the codebase.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/PiyushSuthar/github-readme-quotes/blob/master/tsconfig.json'>tsconfig.json</a></b></td>
				<td>Enables strict type-checking and interoperability settings across the project, ensuring consistent code quality and compatibility.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- .github Submodule -->
		<summary><b>.github</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/PiyushSuthar/github-readme-quotes/blob/master/.github/FUNDING.yml'>FUNDING.yml</a></b></td>
				<td>Facilitates financial support for the project by defining supported funding platforms.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- api Submodule -->
		<summary><b>api</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/PiyushSuthar/github-readme-quotes/blob/master/api/index.ts'>index.ts</a></b></td>
				<td>- Generates SVG images with quotes based on query parameters, utilizing fetcher and renderer functions<br>- Allows customization of card type, theme, quote content, author, and border<br>- Supports caching and delivers image responses via Vercel.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- src Submodule -->
		<summary><b>src</b></summary>
		<blockquote>
			<details>
				<summary><b>renderer</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/PiyushSuthar/github-readme-quotes/blob/master/src/renderer/render-svg.ts'>render-svg.ts</a></b></td>
						<td>- Defines a function to render SVG cards based on input data, type, theme, and border settings<br>- Renders vertical or horizontal cards with specified colors and themes, falling back to defaults when necessary<br>- This function enhances the project's renderer capabilities, supporting various card types and themes for visual representation.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/PiyushSuthar/github-readme-quotes/blob/master/src/renderer/constants.ts'>constants.ts</a></b></td>
						<td>- Define and export a constant storing SVG font data for the "Poppins" font family in the renderer component<br>- This file manages the configuration for displaying text in the specified font style and weight.</td>
					</tr>
					</table>
					<details>
						<summary><b>type</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/PiyushSuthar/github-readme-quotes/blob/master/src/renderer/type/horizontal-card.ts'>horizontal-card.ts</a></b></td>
								<td>- Generates a horizontal card displaying a quote with author, customizable themes, and borders based on user-defined props<br>- Handles light and dark mode themes, adapting to system settings or custom color schemes.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/PiyushSuthar/github-readme-quotes/blob/master/src/renderer/type/vertical-card.ts'>vertical-card.ts</a></b></td>
								<td>Generate vertical card SVG markup based on quote, author, color, and border props using Poppins font and customizable themes.</td>
							</tr>
							</table>
						</blockquote>
					</details>
					<details>
						<summary><b>theme</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/PiyushSuthar/github-readme-quotes/blob/master/src/renderer/theme/awesome-card.ts'>awesome-card.ts</a></b></td>
								<td>- Define and export interface, themes, and render function for theme customization in the renderer layer<br>- Theme data includes quote, author, background, and symbol properties<br>- The renderTheme function validates and returns a specified theme or default light theme with dark mode support if not found.</td>
							</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<details>
				<summary><b>fetcher</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/PiyushSuthar/github-readme-quotes/blob/master/src/fetcher/fetch-quotes.ts'>fetch-quotes.ts</a></b></td>
						<td>- Enable fetching and parsing of random programming quotes from an external API<br>- Retrieves quotes data, selects a random quote, and parses it before returning the formatted quote along with its author<br>- This functionality aids in injecting dynamic and motivational content into the application to inspire users.</td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---
## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with github-readme-quotes, ensure your runtime environment meets the following requirements:

- **Programming Language:** TypeScript
- **Package Manager:** Npm


### ⚙️ Installation

Install github-readme-quotes using one of the following methods:

**Build from source:**

1. Clone the github-readme-quotes repository:
```sh
❯ git clone https://github.com/PiyushSuthar/github-readme-quotes
```

2. Navigate to the project directory:
```sh
❯ cd github-readme-quotes
```

3. Install the project dependencies:


**Using `npm`** &nbsp; [<img align="center" src="https://img.shields.io/badge/npm-CB3837.svg?style={badge_style}&logo=npm&logoColor=white" />](https://www.npmjs.com/)

```sh
❯ npm install
```




### 🤖 Usage
Run github-readme-quotes using the following command:
**Using `npm`** &nbsp; [<img align="center" src="https://img.shields.io/badge/npm-CB3837.svg?style={badge_style}&logo=npm&logoColor=white" />](https://www.npmjs.com/)

```sh
❯ npm start
```


### 🧪 Testing
Run the test suite using the following command:
**Using `npm`** &nbsp; [<img align="center" src="https://img.shields.io/badge/npm-CB3837.svg?style={badge_style}&logo=npm&logoColor=white" />](https://www.npmjs.com/)

```sh
❯ npm test
```


---
## 📌 Project Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/PiyushSuthar/github-readme-quotes/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/PiyushSuthar/github-readme-quotes/issues)**: Submit bugs found or log feature requests for the `github-readme-quotes` project.
- **💡 [Submit Pull Requests](https://github.com/PiyushSuthar/github-readme-quotes/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/PiyushSuthar/github-readme-quotes
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
   <a href="https://github.com{/PiyushSuthar/github-readme-quotes/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=PiyushSuthar/github-readme-quotes">
   </a>
</p>
</details>

---

## 🎗 License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 🙌 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---
