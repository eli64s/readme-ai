<div id="top">

<!-- HEADER STYLE: CONSOLE -->
<div align="center">

```console
██████ ██████  ████  ██████   ██    ████           ██   ██████
  ██     ██   ██       ██    ████  ██             ████    ██
  ██     ██   ██       ██   ██  ██ ██     ██████ ██  ██   ██
  ██     ██   ██       ██   ██████ ██            ██████   ██
  ██   ██████  ████    ██   ██  ██  ████         ██  ██ ██████

Master the game with unbeatable AI strategies.
```

</div>

<!-- BADGES -->
<img src="https://img.shields.io/bitbucket/license/lusinabrian/tictac-ai?style=flat-square&logo=opensourceinitiative&logoColor=white&color=2e7d32" alt="license">
<img src="https://img.shields.io/bitbucket/last-commit/lusinabrian/tictac-ai?style=flat-square&logo=git&logoColor=white&color=2e7d32" alt="last-commit">
<img src="https://img.shields.io/bitbucket/languages/top/lusinabrian/tictac-ai?style=flat-square&color=2e7d32" alt="repo-top-language">
<img src="https://img.shields.io/bitbucket/languages/count/lusinabrian/tictac-ai?style=flat-square&color=2e7d32" alt="repo-language-count">

<em>Built with the tools and technologies:</em>

<img src="https://img.shields.io/badge/JSON-000000.svg?style=flat-square&logo=JSON&logoColor=white" alt="JSON">
<img src="https://img.shields.io/badge/TOML-9C4121.svg?style=flat-square&logo=TOML&logoColor=white" alt="TOML">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/TypeScript-3178C6.svg?style=flat-square&logo=TypeScript&logoColor=white" alt="TypeScript">
<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=flat-square&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions">
<img src="https://img.shields.io/badge/Poetry-60A5FA.svg?style=flat-square&logo=Poetry&logoColor=white" alt="Poetry">

</div>
<br>

## 🌈 Table of Contents

I. [🌈 Table of Contents](#-table-of-contents)<br>
II. [🔴 Overview](#-overview)<br>
III. [🟠 Features](#-features)<br>
IV. [🟡 Project Structure](#-project-structure)<br>
&nbsp;&nbsp;&nbsp;&nbsp;IV.a. [🟢 Project Index](#-project-index)<br>
V. [🔵 Getting Started](#-getting-started)<br>
&nbsp;&nbsp;&nbsp;&nbsp;V.a. [🟣 Prerequisites](#-prerequisites)<br>
&nbsp;&nbsp;&nbsp;&nbsp;V.b. [⚫ Installation](#-installation)<br>
&nbsp;&nbsp;&nbsp;&nbsp;V.c. [⚪ Usage](#-usage)<br>
&nbsp;&nbsp;&nbsp;&nbsp;V.d. [🟤 Testing](#-testing)<br>
VI. [🌟 Roadmap](#-roadmap)<br>
VII. [🤝 Contributing](#-contributing)<br>
VIII. [📜 License](#-license)<br>
IX. [✨ Acknowledgments](#-acknowledgments)<br>

---

## 🔴 Overview

**tictac-ai: Revolutionizing Tic-Tac-Toe Gaming**

**Why tictac-ai?**

This project redefines the Tic-Tac-Toe gaming experience with cutting-edge features:

- **🚀 Automates CI/CD:** Seamlessly integrate Bitbucket Pipelines for efficient development workflows.
- **🤖 Minimax AI Algorithm:** Experience optimal gameplay strategies powered by advanced AI decision-making.
- **🎮 Diverse Player Interfaces:** Choose from console, browser, or graphical window interfaces for versatile gameplay.
- **🎨 Smooth Player Interactions:** Enjoy seamless interactions and visually appealing game rendering.

---

## 🟠 Features

|      | Component       | Details                              |
| :--- | :-------------- | :----------------------------------- |
| ⚙️  | **Architecture**  | <ul><li>Follows a modular design with separate modules for game logic, AI algorithms, and user interface.</li><li>Uses TypeScript for frontend and Python for backend, ensuring clear separation of concerns.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Consistent code style maintained throughout the project.</li><li>Includes linting configurations for both TypeScript and Python codebases.</li></ul> |
| 📄 | **Documentation** | <ul><li>Currently lacks comprehensive documentation.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integrated with Bitbucket Pipelines and GitHub Actions for CI/CD.</li><li>Dependency management handled by Poetry for Python packages.</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Codebase structured into reusable components for easy maintenance and scalability.</li><li>Separate configuration files for CI/CD and package management enhance modularity.</li></ul> |
| 🧪 | **Testing**       | <ul><li>Includes unit tests for critical functions in both TypeScript and Python codebases.</li><li>Test coverage reports generated to ensure code reliability.</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Efficient AI algorithms implemented, such as minimax with alpha-beta pruning for optimal gameplay.</li><li>Optimized frontend rendering for smooth user experience.</li></ul> |
| 🛡️ | **Security**      | <ul><li>Security configurations like code scanning with CodeQL and dependency updates with Dependabot enhance project security.</li><li>License file included to clarify usage permissions.</li></ul> |
| 📦 | **Dependencies**  | <ul><li>Dependencies managed using Poetry for Python packages, ensuring version consistency and easy installation.</li><li>Specific dependencies like TypeScript for frontend and minimax.json for AI algorithms utilized.</li></ul> |

---

## 🟡 Project Structure

```sh
└── tictac-ai/
    ├── .github
    ├── LICENSE
    ├── Makefile
    ├── README.md
    ├── bitbucket-pipelines.yml
    ├── clients
    ├── dangerfile.ts
    ├── docs
    └── tictacai
```

### 🟢 Project Index

<details open>
	<summary><b><code>TICTAC-AI/</code></b></summary>
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
					<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/LICENSE'>LICENSE</a></b></td>
					<td style='padding: 8px;'>- Define the projects licensing terms using the provided MIT License in the LICENSE file<br>- Grant users the freedom to use, modify, and distribute the software while ensuring proper attribution<br>- This file sets the guidelines for leveraging the project within legal boundaries.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/Makefile'>Makefile</a></b></td>
					<td style='padding: 8px;'>- Facilitates project setup, installation, testing, linting, and building<br>- Orchestrates virtual environment creation, dependency installation, code quality checks, and application building<br>- Centralizes essential commands for seamless development workflows.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/dangerfile.ts'>dangerfile.ts</a></b></td>
					<td style='padding: 8px;'>Ensure proper PR assignment, size, and package integrity checks in the dangerfile.ts to maintain code quality and streamline review processes within the project architecture.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/bitbucket-pipelines.yml'>bitbucket-pipelines.yml</a></b></td>
					<td style='padding: 8px;'>- Configure Bitbucket Pipelines for Python project CI/CD<br>- Define caching, linting, testing, building, packaging, and releasing steps<br>- Utilizes Poetry for dependency management<br>- Executes tasks in isolated environments<br>- Facilitates seamless integration with Bitbucket for automated deployment.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- clients Submodule -->
	<details>
		<summary><b>clients</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ clients</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/clients/play.py'>play.py</a></b></td>
					<td style='padding: 8px;'>- Play a game of Tic-Tac-Toe with a console player and a random computer player<br>- This code file in the clients directory orchestrates the game setup and execution, utilizing components from the tictacai and console modules<br>- The game logic, player interactions, and rendering are all managed seamlessly to provide an engaging gaming experience.</td>
				</tr>
			</table>
			<!-- browser Submodule -->
			<details>
				<summary><b>browser</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ clients.browser</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/clients/browser/index.html'>index.html</a></b></td>
							<td style='padding: 8px;'>- Define the browser client interface for the TicTacToe game, specifying player options and rendering the game board<br>- Include player selection dropdowns, SVG board layout, and game status display<br>- Integrate Python environment for AI gameplay and link external script for game logic.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/clients/browser/renderers.py'>renderers.py</a></b></td>
							<td style='padding: 8px;'>- Render method updates the browser UI based on game state, handling win/tie scenarios and enabling replay<br>- It interacts with the DOM to reflect game progress and outcomes visually, ensuring a seamless user experience during gameplay.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/clients/browser/cli.py'>cli.py</a></b></td>
							<td style='padding: 8px;'>- Serve HTTP content and open a browser to display it<br>- Run a local server to host files and automatically launch a browser to view them<br>- This functionality enhances user experience by simplifying the process of previewing content.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/clients/browser/players.py'>players.py</a></b></td>
							<td style='padding: 8px;'>- Define a BrowserPlayer class extending AsyncPlayer, handling player moves asynchronously based on received events<br>- The class initializes with a mark and event queue, fetching moves from the queue to update game state.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/clients/browser/script.py'>script.py</a></b></td>
							<td style='padding: 8px;'>- Execute script to enable browser-based Tic Tac Toe game with AI opponents and human players<br>- Handles player selections, game logic, rendering, and event handling<br>- Integrates async functionality for smooth gameplay<br>- Click events trigger game actions<br>- Replay button resets game state<br>- Enhances user experience with interactive features.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/clients/browser/__main__.py'>__main__.py</a></b></td>
							<td style='padding: 8px;'>Execute the browser clients main functionality from the CLI module.</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- window Submodule -->
			<details>
				<summary><b>window</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ clients.window</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/clients/window/renderers.py'>renderers.py</a></b></td>
							<td style='padding: 8px;'>- Render Tic Tac Toe game interface and state updates in a graphical window using tkinter<br>- Display the game grid and update button labels accordingly<br>- Change window title based on game outcomes like a win or tie<br>- Highlight winning cells with a bold style.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/clients/window/cli.py'>cli.py</a></b></td>
							<td style='padding: 8px;'>- Execute the game loop for a Tic-Tac-Toe match using a graphical window interface<br>- Players can compete against a Minimax AI opponent, with real-time updates displayed on the window<br>- The main function initializes the game loop by creating player instances and starting the game with the specified starting mark.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/clients/window/players.py'>players.py</a></b></td>
							<td style='padding: 8px;'>- Implement a WindowPlayer class that extends Player, handling player moves via events<br>- The class initializes with a mark and event queue, fetching moves from the queue and updating game state accordingly.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/clients/window/__main__.py'>__main__.py</a></b></td>
							<td style='padding: 8px;'>Execute the CLI interface for the window client.</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- console Submodule -->
			<details>
				<summary><b>console</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ clients.console</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/clients/console/renderers.py'>renderers.py</a></b></td>
							<td style='padding: 8px;'>- Render tic-tac-toe game state on the console, displaying the winner or a tie message<br>- Clear the screen before rendering and highlight winning cells with blinking text<br>- The grid is presented with player marks in a structured format<br>- The code enhances user experience by providing clear visual feedback during gameplay.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/clients/console/cli.py'>cli.py</a></b></td>
							<td style='padding: 8px;'>- Execute the CLI game engine to facilitate player interaction and gameplay rendering<br>- Parse command-line arguments to determine player configurations and starting conditions<br>- Utilize the TicTacToe game engine with a console renderer to orchestrate gameplay between two players.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/clients/console/players.py'>players.py</a></b></td>
							<td style='padding: 8px;'>- Implement a console player that interacts with the game state to make moves based on user input<br>- The player converts user-provided grid coordinates into the corresponding index on the game board<br>- Handles exceptions for invalid moves and occupied cells to ensure smooth gameplay.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/clients/console/args.py'>args.py</a></b></td>
							<td style='padding: 8px;'>- Parse command-line arguments to determine player types and starting marks for a Tic-Tac-Toe game<br>- The Args class provides type safety and named access to player configurations<br>- The parse_args function uses argparse to handle argument parsing and returns the specified player configurations.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/clients/console/__main__.py'>__main__.py</a></b></td>
							<td style='padding: 8px;'>Launches the command-line interface for the console client, serving as the entry point for user interaction.</td>
						</tr>
					</table>
				</blockquote>
			</details>
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
					<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/.github/CODEOWNERS'>CODEOWNERS</a></b></td>
					<td style='padding: 8px;'>- Define ownership rules for the projects codebase, specifying patterns and corresponding owners<br>- The file assigns @BrianLusina as the owner for all files and directories, ensuring clarity and accountability in managing the project.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/.github/dependabot.yml'>dependabot.yml</a></b></td>
					<td style='padding: 8px;'>- Configure Dependabot to manage Python dependencies in the project, ensuring timely updates and pull requests<br>- Set a weekly schedule for dependency checks, with specific labels, assignees, and reviewers for streamlined maintenance.</td>
				</tr>
			</table>
			<!-- workflows Submodule -->
			<details>
				<summary><b>workflows</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ .github.workflows</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/.github/workflows/release.yml'>release.yml</a></b></td>
							<td style='padding: 8px;'>- Automate release process on main branch using semantic-release with GitHub Actions<br>- Setup Node.js environment and trigger release on push events.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/.github/workflows/lint_test_build.yml'>lint_test_build.yml</a></b></td>
							<td style='padding: 8px;'>- Define a GitHub workflow for linting, testing, and building the project<br>- The workflow runs on push and pull requests, checking code quality, running tests, and building the application<br>- It ensures code consistency and functionality before merging changes into the codebase.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/.github/workflows/dangerci.yml'>dangerci.yml</a></b></td>
							<td style='padding: 8px;'>- Create a Danger CI workflow that checks pull requests on the main branch<br>- It runs on Ubuntu, installs NodeJS 16.x, adds Danger dependencies if not cached, and performs Danger CI checks using danger-js 9.1.8, leveraging GitHub tokens for authentication.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/.github/workflows/pypy_upload.yml'>pypy_upload.yml</a></b></td>
							<td style='padding: 8px;'>- Facilitates automated PyPI package uploads by setting up Python, installing necessary tools, building distributions, and uploading to PyPI via Twine<br>- This workflow ensures seamless deployment to PyPI upon code changes in the main branch.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/.github/workflows/codeql_analysis.yml'>codeql_analysis.yml</a></b></td>
							<td style='padding: 8px;'>- Automates CodeQL analysis for vulnerabilities and errors on push, pull request, and scheduled events<br>- Initializes CodeQL tools, performs analysis, and auto-builds compiled languages<br>- Ensures code security and quality.</td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<!-- tictacai Submodule -->
	<details>
		<summary><b>tictacai</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ tictacai</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/tictacai/LICENSE'>LICENSE</a></b></td>
					<td style='padding: 8px;'>- Define the projects licensing terms within the tictacai/LICENSE file, granting users the freedom to use, modify, and distribute the software<br>- This file establishes the permissions and conditions for utilizing the codebase, ensuring compliance with the MIT License.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/tictacai/pyproject.toml'>pyproject.toml</a></b></td>
					<td style='padding: 8px;'>- Create a Tic-Tac-Toe game using Minimax AI players<br>- The project structure includes dependencies for linting, testing, and packaging<br>- The game is written in Python and follows the MIT license<br>- The README file provides detailed information on how to play the game and the AI strategies used.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/tictacai/MANIFEST.in'>MANIFEST.in</a></b></td>
					<td style='padding: 8px;'>Expose the minimax algorithm configuration for Tic-Tac-Toe AI logic.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/tictacai/setup.py'>setup.py</a></b></td>
					<td style='padding: 8px;'>- Create a setup configuration for the Tic-Tac-Toe game, specifying metadata like name, description, and version<br>- It handles package requirements, sets up project details, and ensures compatibility<br>- This file streamlines the setup process for the project.</td>
				</tr>
			</table>
			<!-- tictacai Submodule -->
			<details>
				<summary><b>tictacai</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ tictacai.tictacai</b></code>
					<!-- logic Submodule -->
					<details>
						<summary><b>logic</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ tictacai.tictacai.logic</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/tictacai/tictacai/logic/minimax.py'>minimax.py</a></b></td>
									<td style='padding: 8px;'>- Optimizes finding the best move in Tic-Tac-Toe by implementing the Minimax algorithm<br>- The code calculates the optimal move for the current player by recursively simulating possible game states and evaluating scores<br>- Additionally, it offers precomputed scores for faster decision-making<br>- The functions provided enable efficient gameplay decision-making based on game state evaluation.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/tictacai/tictacai/logic/models.py'>models.py</a></b></td>
									<td style='padding: 8px;'>- Define game logic and state transitions for a Tic-Tac-Toe AI<br>- Models grid, moves, and game state, allowing evaluation of scores based on current game status<br>- Implements methods for making moves, checking game end conditions, and generating possible moves for the AI to choose from.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/tictacai/tictacai/logic/minimax.json'>minimax.json</a></b></td>
									<td style='padding: 8px;'>- SummaryThe <code>minimax.json</code> file in the <code>tictacai/logic</code> directory of the project contains pre-calculated game states and their corresponding scores for a Tic-Tac-Toe AI using the Minimax algorithm<br>- These game states represent different board configurations during gameplay, with each state having an associated score indicating the AIs evaluation of that particular board position<br>- The purpose of this file is to provide the AI with a reference to make optimal moves by selecting the next best move based on the calculated scores for each possible game state<br>- This aids in enhancing the AI's decision-making process and ultimately improving its gameplay strategy within the Tic-Tac-Toe game.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/tictacai/tictacai/logic/validators.py'>validators.py</a></b></td>
									<td style='padding: 8px;'>- Validate functions ensure game integrity by checking grid consistency, marking correctness, and player differentiation<br>- These functions maintain game fairness by enforcing rules on marks, player order, and winner conditions.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/tictacai/tictacai/logic/exceptions.py'>exceptions.py</a></b></td>
									<td style='padding: 8px;'>Define custom exceptions for invalid game states, moves, and unknown game scores within the Tic Tac Toe AI logic module.</td>
								</tr>
							</table>
						</blockquote>
					</details>
					<!-- game Submodule -->
					<details>
						<summary><b>game</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ tictacai.tictacai.game</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/tictacai/tictacai/game/renderers.py'>renderers.py</a></b></td>
									<td style='padding: 8px;'>Visualize the game grid through the Renderer to display the current game state.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/tictacai/tictacai/game/engine.py'>engine.py</a></b></td>
									<td style='padding: 8px;'>- Drive the game engines logic by orchestrating player moves and rendering the game state<br>- Utilize a pull strategy to prompt players for moves, alternating turns until the game concludes<br>- Map player marks to player objects for seamless gameplay flow.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/tictacai/tictacai/game/players.py'>players.py</a></b></td>
									<td style='padding: 8px;'>- Define player logic for Tic-Tac-Toe game<br>- Player classes determine moves based on game state<br>- Computer players include a delay before making a move<br>- Options include a random move or using the minimax algorithm for optimal play<br>- Players extend base classes to implement move strategies efficiently.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/tictacai/tictacai/game/players_async.py'>players_async.py</a></b></td>
									<td style='padding: 8px;'>- Implement asynchronous computer players for Tic-Tac-Toe gameplay<br>- Define classes for players to make moves based on game states<br>- AsyncRandomComputerPlayer selects moves randomly, while AsyncMinimaxComputerPlayer uses a precomputed algorithm for optimal moves<br>- These classes enhance the games AI capabilities.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://bitbucket.org/lusinabrian/tictac-ai/blob/master/tictacai/tictacai/game/engine_async.py'>engine_async.py</a></b></td>
									<td style='padding: 8px;'>- Define the asynchronous Tic-Tac-Toe game engine, orchestrating player moves and rendering the game state<br>- Validates player inputs and handles errors<br>- The engine facilitates player interactions and game progression, ensuring a seamless gaming experience within the broader project architecture.</td>
								</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---

## 🔵 Getting Started

### 🟣 Prerequisites

This project requires the following dependencies:

- **Programming Language:** Python
- **Package Manager:** Poetry

### ⚫ Installation

Build tictac-ai from the source and intsall dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://bitbucket.org/lusinabrian/tictac-ai
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd tictac-ai
    ```

3. **Install the dependencies:**

<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![poetry][poetry-shield]][poetry-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [poetry-shield]: https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json -->
	<!-- [poetry-link]: https://python-poetry.org/ -->

	**Using [poetry](https://python-poetry.org/):**

	```sh
	❯ poetry install
	```

### ⚪ Usage

Run the project with:

**Using [poetry](https://python-poetry.org/):**
```sh
poetry run python {entrypoint}
```

### 🟤 Testing

Tictac-ai uses the {__test_framework__} test framework. Run the test suite with:

**Using [poetry](https://python-poetry.org/):**
```sh
poetry run pytest
```

---

## 🌟 Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🤝 Contributing

- **💬 [Join the Discussions](https://bitbucket.org/lusinabrian/tictac-ai/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://bitbucket.org/lusinabrian/tictac-ai/issues)**: Submit bugs found or log feature requests for the `tictac-ai` project.
- **💡 [Submit Pull Requests](https://bitbucket.org/lusinabrian/tictac-ai/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your bitbucket account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://bitbucket.org/lusinabrian/tictac-ai
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
6. **Push to bitbucket**: Push the changes to your forked repository.
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
   <a href="https://bitbucket.org{/lusinabrian/tictac-ai/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=lusinabrian/tictac-ai">
   </a>
</p>
</details>

---

## 📜 License

Tictac-ai is protected under the [LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## ✨ Acknowledgments

- Credit `contributors`, `inspiration`, `references`, etc.

<div align="left"><a href="#top">⬆ Return</a></div>

---

<!-- README-AI COMMAND: -->
<!--
```sh
readmeai \
    --repository 'https://bitbucket.org/lusinabrian/tictac-ai' \
    --badge-style 'flat-square' \
    --badge-color '2e7d32' \
    --logo 'GREEN' \
    --header-style 'CONSOLE' \
    --navigation-style 'ROMAN' \
    --emojis 'rainbow' \
    --temperature 0.353 \
    --tree-max-depth 1 \
    --api openai \
    --model gpt-3.5-turbo
```
-->
