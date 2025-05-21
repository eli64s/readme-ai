<div id="top">

<!-- HEADER STYLE: BANNER -->
<div align="center">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 200">
	<defs>
		<linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
			<stop offset="0%" style="stop-color:#2de599;stop-opacity:1" />
			<stop offset="50%" style="stop-color:#2dc3e5;stop-opacity:1" />
			<stop offset="100%" style="stop-color:#2d55e5;stop-opacity:1" />
		</linearGradient>
		<filter id="shadow">
			<feDropShadow dx="2.0" dy="2.0" stdDeviation="4.0" flood-opacity="0.5" />
		</filter>
		<pattern id="dots" width="20.0" height="20.0" patternUnits="userSpaceOnUse">
			<circle cx="3" cy="3" r="1.5" fill="rgba(255,255,255,0.2)" />
		</pattern>
	</defs>
	<rect width="100%" height="100%" fill="url(#bg)" rx="5.0" />
	<rect width="100%" height="100%" fill="url(#dots)" />
	<circle cx="64.0" cy="50.0" r="30.0" fill="rgba(255,255,255,0.8)" />
	<circle cx="736.0" cy="150.0" r="40.0" fill="rgba(255,255,255,0.8)" />
	<path d="M 400.0 25.0
			 L 450.0 75.0
			 L 350.0 75.0 Z" fill="rgba(255,255,255,0.8)" />
	<text x="400.0" y="100.0" font-family="Arial, sans-serif" font-size="24" font-weight="bold" text-anchor="middle" fill="#FFFFFF" filter="url(#shadow)">
		github-readme-quotes
	</text>
	<text x="400.0" y="150.0" font-family="Arial, sans-serif" font-size="18" text-anchor="middle" fill="rgba(255,255,255,0.9)">
Elevate Your Code with Wisdom's Dynamic Spark</text></svg>

<!-- BADGES -->
<img src="https://img.shields.io/github/license/PiyushSuthar/github-readme-quotes?style=flat&logo=opensourceinitiative&logoColor=white&color=8a2be2" alt="license">
<img src="https://img.shields.io/github/last-commit/PiyushSuthar/github-readme-quotes?style=flat&logo=git&logoColor=white&color=8a2be2" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/PiyushSuthar/github-readme-quotes?style=flat&color=8a2be2" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/PiyushSuthar/github-readme-quotes?style=flat&color=8a2be2" alt="repo-language-count">

<em>Built with the tools and technologies:</em>

<img src="https://img.shields.io/badge/TypeScript-3178C6.svg?style=flat&logo=TypeScript&logoColor=white" alt="TypeScript">
<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat&logo=YAML&logoColor=white" alt="YAML">

</div>

---

## 🔵 Table of Contents

- [🔵 Table of Contents](#-table-of-contents)
- [🟢 Overview](#-overview)
- [🟡 Features](#-features)
- [🟠 Project Structure](#-project-structure)
    - [🔴 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
    - [🟣 Prerequisites](#-prerequisites)
    - [🟤 Installation](#-installation)
    - [⚫ Usage](#-usage)
    - [⚪ Testing](#-testing)
- [🌈 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)
- [✨ Acknowledgments](#-acknowledgments)

---

## 🟢 Overview

GitHub README Quotes is a powerful tool that dynamically generates inspiring programming quotes as customizable SVG images for your GitHub profile or project README.

**Why github-readme-quotes?**

This project enhances your GitHub presence with motivational content while offering extensive customization options. The core features include:

- **🎨 Dynamic SVG Generation:** Create high-quality, scalable quote images on-the-fly.
- **🔧 Flexible Layouts:** Choose between vertical and horizontal card designs to fit your needs.
- **🌈 Customizable Themes:** Personalize your cards with light/dark modes and custom color schemes.
- **📚 Quote API Integration:** Easily fetch and display programming-related quotes from an external source.
- **💖 Open-Source Sustainability:** Support ongoing development through integrated funding options.

---

## 🟡 Features

|      | Component       | Details                              |
| :--- | :-------------- | :----------------------------------- |
| ⚙️  | **Architecture**  | <ul><li>TypeScript-based project</li><li>Serverless architecture (likely Vercel)</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>TypeScript for type safety</li><li>ESLint for code linting (inferred)</li></ul> |
| 📄 | **Documentation** | <ul><li>README.md (assumed)</li><li>Likely API documentation in code comments</li></ul> |
| 🔌 | **Integrations**  | <ul><li>GitHub API integration (inferred)</li><li>Possible integration with quote APIs</li></ul> |
| 🧩 | **Modularity**    | <ul><li>TypeScript modules</li><li>Likely separation of concerns (e.g., API, rendering)</li></ul> |
| 🧪 | **Testing**       | <ul><li>No explicit testing framework mentioned</li><li>Possible unit tests using Jest (common in TS projects)</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Serverless architecture for scalability</li><li>Likely caching mechanisms for quote retrieval</li></ul> |
| 🛡️ | **Security**      | <ul><li>TypeScript for type safety</li><li>Possible API key management for external services</li></ul> |
| 📦 | **Dependencies**  | <ul><li>TypeScript</li><li>pnpm as package manager</li><li>Other dependencies in `pnpm-lock.yaml`</li></ul> |
| 🚀 | **Scalability**   | <ul><li>Serverless architecture allows easy scaling</li><li>Stateless design (inferred from project nature)</li></ul> |

---

## 🟠 Project Structure

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
    │   └── renderer
    ├── tsconfig.json
    └── vercel.json
```

### 🔴 Project Index

<details open>
	<summary><b><code>GITHUB-README-QUOTES/</code></b></summary>
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
					<td style='padding: 8px;'><b><a href='https://github.com/PiyushSuthar/github-readme-quotes/blob/master/pnpm-lock.yaml'>pnpm-lock.yaml</a></b></td>
					<td style='padding: 8px;'>- Dependency Management: It specifies exact versions of both production dependencies (axios) and development dependencies (@vercel/node, prettier, typescript, and vercel).2<br>- Version Consistency: By locking dependency versions, it prevents unexpected updates that could potentially break the project.3<br>- Project Integrity: It helps maintain the integrity of the project by ensuring all developers and deployment environments use the same dependency versions.4<br>- Faster Installations: The lock file allows for faster and more efficient package installations by providing a pre-resolved dependency tree.5<br>- Security: By specifying exact versions, it helps mitigate potential security risks associated with automatic dependency updates.In the context of the project architecture, this file is crucial for maintaining a stable and consistent development and deployment environment across the team and different stages of the project lifecycle.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- .github Submodule -->
	<details>
		<summary><b>.github</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ .github</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/PiyushSuthar/github-readme-quotes/blob/master/.github/FUNDING.yml'>FUNDING.yml</a></b></td>
					<td style='padding: 8px;'>- Configures funding options for the project through GitHub Sponsors<br>- Specifies Ko-fi as the supported platform, with the username piyush designated as the recipient<br>- Enables project contributors to receive financial support from the community, encouraging ongoing development and maintenance of the open-source initiative.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- api Submodule -->
	<details>
		<summary><b>api</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ api</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/PiyushSuthar/github-readme-quotes/blob/master/api/index.ts'>index.ts</a></b></td>
					<td style='padding: 8px;'>- Serves as the API entry point for generating quote images<br>- Handles incoming requests, processes query parameters, and fetches quotes if not provided<br>- Utilizes the fetcher and renderer modules to create SVG images based on specified themes and card types<br>- Sets appropriate headers and returns the rendered SVG image as the response, enabling dynamic quote image generation for the project.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- src Submodule -->
	<details>
		<summary><b>src</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ src</b></code>
			<!-- renderer Submodule -->
			<details>
				<summary><b>renderer</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ src.renderer</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/PiyushSuthar/github-readme-quotes/blob/master/src/renderer/render-svg.ts'>render-svg.ts</a></b></td>
							<td style='padding: 8px;'>- Renders SVG cards for quotes based on specified parameters<br>- Determines the card type (vertical or horizontal), applies the chosen theme, and handles border options<br>- Utilizes separate rendering functions for different card types and themes<br>- Serves as a central hub for generating customized quote cards, integrating various components of the projects rendering system.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/PiyushSuthar/github-readme-quotes/blob/master/src/renderer/constants.ts'>constants.ts</a></b></td>
							<td style='padding: 8px;'>- Defines a constant containing SVG markup for embedding the Poppins font<br>- Enables consistent typography across the application by providing a web-safe fallback for the Poppins typeface<br>- Supports the renderers visual styling, ensuring font consistency regardless of local system font availability<br>- Contributes to maintaining a uniform user interface appearance throughout the project.</td>
						</tr>
					</table>
					<!-- type Submodule -->
					<details>
						<summary><b>type</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ src.renderer.type</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/PiyushSuthar/github-readme-quotes/blob/master/src/renderer/type/horizontal-card.ts'>horizontal-card.ts</a></b></td>
									<td style='padding: 8px;'>- Renders horizontal quote cards as SVG images for the project<br>- Defines a function that generates customizable card layouts with quotes, authors, and themes<br>- Supports light and dark modes, custom color schemes, and optional borders<br>- Utilizes imported font and theme constants to ensure consistent styling across the application<br>- Plays a crucial role in creating visually appealing, responsive quote displays for various project components.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/PiyushSuthar/github-readme-quotes/blob/master/src/renderer/type/vertical-card.ts'>vertical-card.ts</a></b></td>
									<td style='padding: 8px;'>- Renders vertical quote cards as SVG images for the project<br>- Defines a function that generates customizable card layouts with quotes, authors, and themes<br>- Supports light and dark modes, custom color schemes, and optional borders<br>- Utilizes imported font and theme constants to ensure consistent styling across the application<br>- Plays a crucial role in creating visually appealing, responsive quote displays for various project components.</td>
								</tr>
							</table>
						</blockquote>
					</details>
					<!-- theme Submodule -->
					<details>
						<summary><b>theme</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ src.renderer.theme</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/PiyushSuthar/github-readme-quotes/blob/master/src/renderer/theme/awesome-card.ts'>awesome-card.ts</a></b></td>
									<td style='padding: 8px;'>- Defines and exports a collection of color themes for an awesome card component<br>- Provides a Theme interface and a themes object containing various predefined color schemes<br>- Includes a renderTheme function to select the appropriate theme based on user input, defaulting to a light theme with dark mode support if an invalid or default theme is specified.</td>
								</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<!-- fetcher Submodule -->
			<details>
				<summary><b>fetcher</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ src.fetcher</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/PiyushSuthar/github-readme-quotes/blob/master/src/fetcher/fetch-quotes.ts'>fetch-quotes.ts</a></b></td>
							<td style='padding: 8px;'>- Fetches and processes programming quotes from an external API<br>- Implements functionality to retrieve a random quote, ensuring it meets specific length criteria<br>- Parses and formats the quote data for consistency<br>- Provides error handling for invalid data structures and empty quote lists<br>- Serves as a crucial component for supplying motivational content to the applications user interface.</td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---

## 🚀 Getting Started

### 🟣 Prerequisites

This project requires the following dependencies:

- **Programming Language:** TypeScript

### 🟤 Installation

Build github-readme-quotes from the source and intsall dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/PiyushSuthar/github-readme-quotes
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd github-readme-quotes
    ```

3. **Install the dependencies:**

echo 'INSERT-INSTALL-COMMAND-HERE'

### ⚫ Usage

Run the project with:

echo 'INSERT-RUN-COMMAND-HERE'

### ⚪ Testing

Github-readme-quotes uses the {__test_framework__} test framework. Run the test suite with:

echo 'INSERT-TEST-COMMAND-HERE'

---

## 🌈 Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🤝 Contributing

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

## 📜 License

Github-readme-quotes is protected under the [LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## ✨ Acknowledgments

- Credit `contributors`, `inspiration`, `references`, etc.

<div align="left"><a href="#top">⬆ Return</a></div>

---

<!-- README-AI COMMAND: -->
<!--
```sh
readmeai \
    --repository 'https://github.com/PiyushSuthar/github-readme-quotes' \
    --output 'docs/docs/examples/ai-providers/anthropic/claude-3-sonnet/readme-github-readme-quotes.md' \
    --badge-style 'flat' \
    --badge-color '8a2be2' \
    --logo 'ANIMATED' \
    --header-style 'BANNER' \
    --navigation-style 'BULLET' \
    --emojis 'gradient' \
    --temperature 0.156 \
    --tree-max-depth 2 \
    --api anthropic \
    --model claude-3-5-sonnet-20240620
```
-->
