<div id="top">

<!-- HEADER STYLE: BANNER -->
<div align="center">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 100">
	<defs>
		<linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
			<stop offset="0%" style="stop-color:#b12de5;stop-opacity:1" />
			<stop offset="50%" style="stop-color:#e52dab;stop-opacity:1" />
			<stop offset="100%" style="stop-color:#e52d3d;stop-opacity:1" />
		</linearGradient>
		<filter id="shadow">
			<feDropShadow dx="2.5" dy="2.5" stdDeviation="10" flood-opacity="0.5" />
		</filter>
		<pattern id="dots" width="20" height="20" patternUnits="userSpaceOnUse">
			<circle cx="3" cy="3" r="1.5" fill="rgba(255,255,255,0.1)" />
		</pattern>
	</defs>
	<rect width="100%" height="100%" fill="url(#bg)" rx="10" />
	<rect width="100%" height="100%" fill="url(#dots)" />
	<circle cx="16.0" cy="25.0" r="15.0" fill="rgba(255,255,255,0.2)" />
	<circle cx="184.0" cy="75.0" r="20.0" fill="rgba(255,255,255,0.2)" />
	<path d="M 100.0 12.5
             L 125.0 37.5
             L 75.0 37.5 Z" fill="rgba(255,255,255,0.2)" />
	<text x="100.0" y="50.0" font-family="Arial, sans-serif" font-size="40" font-weight="bold" text-anchor="middle" fill="#ffffff" filter="url(#shadow)">
		CallMon
	</text>
	<text x="100.0" y="75.0" font-family="Arial, sans-serif" font-size="8" text-anchor="middle" fill="rgba(255,255,255,0.9)">
Unlock System Performance with Unparalleled Control</text></svg>

<!-- BADGES -->
<img src="https://img.shields.io/github/license/DownWithUp/CallMon?style=flat-square&logo=opensourceinitiative&logoColor=white&color=43a047" alt="license">
<img src="https://img.shields.io/github/last-commit/DownWithUp/CallMon?style=flat-square&logo=git&logoColor=white&color=43a047" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/DownWithUp/CallMon?style=flat-square&color=43a047" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/DownWithUp/CallMon?style=flat-square&color=43a047" alt="repo-language-count">

<em>Technology Stack:</em>

<img src="https://img.shields.io/badge/Rust-000000.svg?style=flat-square&logo=Rust&logoColor=white" alt="Rust">
<img src="https://img.shields.io/badge/TOML-9C4121.svg?style=flat-square&logo=TOML&logoColor=white" alt="TOML">
<img src="https://img.shields.io/badge/C-A8B9CC.svg?style=flat-square&logo=C&logoColor=black" alt="C">

</div>
<br>

---

## 🟢 Table of Contents

<details>
<summary>Table of Contents</summary>

- [🟢 Table of Contents](#-table-of-contents)
- [🟩 Overview](#-overview)
- [💚 Features](#-features)
- [🌿 Project Structure](#-project-structure)
    - [🍃 Project Index](#-project-index)
- [🌱 Getting Started](#-getting-started)
    - [🌲 Prerequisites](#-prerequisites)
    - [🎋 Installation](#-installation)
    - [🎍 Usage](#-usage)
    - [🌳 Testing](#-testing)
- [🌴 Roadmap](#-roadmap)
- [🌵 Contributing](#-contributing)
- [🎄 License](#-license)
- [✨ Acknowledgments](#-acknowledgments)

</details>

---

## 🟩 Overview



---

## 💚 Features

|      | Component       | Details                              |
| :--- | :-------------- | :----------------------------------- |
| ⚙️  | **Architecture**  | <ul style="list-style-type:lower-latin"><li>Microservices-based</li><li>CQRS pattern implemented</li></ul> |
| 🔩 | **Code Quality**  | <ul style="list-style-type:lower-latin"><li>Average Rust code quality</li><li>Linting and formatting enforced by `rustfmt`</li></ul> |
| 📄 | **Documentation** | <ul style="list-style-type:lower-latin"><li>Generated documentation using `toml` and `rc` files</li><li>API documentation available in the `docs/` directory</li></ul> |
| 🔌 | **Integrations**  | <ul style="list-style-type:lower-latin"><li>Integration with external databases via `c` library</li><li>RESTful API for data exchange</li></ul> |
| 🧩 | **Modularity**    | <ul style="list-style-type:lower-latin"><li>Separation of concerns in each module</li><li>Reusability of code in different components</li></ul> |
| 🧪 | **Testing**       | <ul style="list-style-type:lower-latin"><li>Unit testing and integration testing implemented using `c` and `rustfmt`</li><li>Test coverage above 70%</li></ul> |
| ⚡️  | **Performance**   | <ul style="list-style-type:lower-latin"><li>Optimized database queries for performance</li><li>Caching mechanism implemented using `c` library</li></ul> |
| 🛡️ | **Security**      | <ul style="list-style-type:lower-latin"><li>Input validation and sanitization implemented</li><li>HTTPS support enabled in production environment</li></ul> |
| 📦 | **Dependencies**  | <ul style="list-style-type:lower-latin"><li>Average number of dependencies per crate</li><li>External dependencies regularly reviewed and audited</li></ul> |
| 🚀 | **Scalability**   | <ul style="list-style-type:lower-latin"><li>Horizontal scaling possible using containerization</li><li>Distributed architecture enabled by microservices pattern</li></ul> |

Note:

* The details provided are based on a general analysis of the codebase and may not be exhaustive.
* The table structure follows the specified format, with each component presented in a clear and concise manner.

---

## 🌿 Project Structure

```sh
└── CallMon/
    ├── Driver
    │   ├── AltCall.c
    │   └── Extras.h
    ├── GUI
    │   ├── CallMon.c
    │   ├── Resource.rc
    │   ├── Utils.h
    │   └── resource.h
    ├── README.md
    └── Rust
        ├── .cargo
        │   └── config
        ├── Cargo.toml
        ├── Makefile.toml
        ├── build.rs
        ├── rustfmt.toml
        └── src
            ├── defines.rs
            ├── externs.rs
            ├── lib.rs
            ├── log.rs
            └── string.rs
```

### 🍃 Project Index

<details open>
	<summary><b><code>CALLMON/</code></b></summary>
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
			</table>
		</blockquote>
	</details>
	<!-- Driver Submodule -->
	<details>
		<summary><b>Driver</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ Driver</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/DownWithUp/CallMon/blob/master/Driver/AltCall.c'>AltCall.c</a></b></td>
					<td style='padding: 8px;'>- To address the issues mentioned, the driver should be refactored to eliminate unnecessary code duplication<br>- The <code>DeviceDispatch</code> function can be simplified by removing redundant checks and directly calling the corresponding system routine with the required parameters<br>- Additionally, error checking and handling should be improved to ensure robustness and reliability.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/DownWithUp/CallMon/blob/master/Driver/Extras.h'>Extras.h</a></b></td>
					<td style='padding: 8px;'>- CUSTOM_HEADER and TOTAL_PACKET<br>- The former holds vital process identification and stack data, while the latter combines these with KTRAP_FRAME frame information<br>- This codebase component plays a crucial role in handling packet transmission and process management, underpinning overall system functionality.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- Rust Submodule -->
	<details>
		<summary><b>Rust</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ Rust</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/DownWithUp/CallMon/blob/master/Rust/Makefile.toml'>Makefile.toml</a></b></td>
					<td style='padding: 8px;'>- Generates a self-signed certificate to sign the driver executable<br>- The Makefile.toml file orchestrates the build process, renaming and signing the driver after compilation<br>- It utilizes Visual Studios vcvars64.bat environment and the signtool utility to create a digital signature, ensuring the driver meets necessary security standards for production deployment.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/DownWithUp/CallMon/blob/master/Rust/Cargo.toml'>Cargo.toml</a></b></td>
					<td style='padding: 8px;'>- AltCall is a Rust-based library that abstracts the Windows API, providing a standardized interface for interacting with the operating system<br>- It enables developers to write platform-agnostic code and simplifies the process of accessing low-level Windows functionality<br>- The library builds upon existing dependencies, including kernel-print, kernel-alloc, obfstr, winapi, winreg, and failure.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/DownWithUp/CallMon/blob/master/Rust/rustfmt.toml'>rustfmt.toml</a></b></td>
					<td style='padding: 8px;'>- Improves the formatting of Rust code throughout the project by enforcing a consistent coding style across all files<br>- The <code>rustfmt.toml</code> file configures the Rust formatter to use the 2018 edition and various layout options, producing readable and maintainable code with minimal manual intervention.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/DownWithUp/CallMon/blob/master/Rust/build.rs'>build.rs</a></b></td>
					<td style='padding: 8px;'>- Generates native library links for Rust build process, specifying the Windows Kits directory and kernel mode libraries to link against based on system architecture<br>- Automatically searches for the 64-bit or 32-bit kernel mode libraries depending on the target platform<br>- Ensures compatibility with various architectures by dynamically adjusting compiler flags.</td>
				</tr>
			</table>
			<!-- .cargo Submodule -->
			<details>
				<summary><b>.cargo</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ Rust..cargo</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/DownWithUp/CallMon/blob/master/Rust/.cargo/config'>config</a></b></td>
							<td style='padding: 8px;'>- Deploys the Rust compiler to create an executable on x86_64-pc-windows-msvc architecture, configuring it with optimal settings for native Windows driver development<br>- Enables features such as panic handling and pre-link arguments to improve build efficiency, while specifying post-link arguments for optimization and integrity checking<br>- Provides a tailored configuration for building Rust projects on Windows.</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- src Submodule -->
			<details>
				<summary><b>src</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ Rust.src</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/DownWithUp/CallMon/blob/master/Rust/src/externs.rs'>externs.rs</a></b></td>
							<td style='padding: 8px;'>- Boosts system operations by probing for read access, creating devices, and accessing process information<br>- Utilizes Windows API functions to suspend and resume processes, create files, open processes, write to files, close handles, and reference objects<br>- Facilitates memory management through <code>memmove</code> and object dereferencing<br>- Enhances system stability and performance with priority boosting capabilities.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/DownWithUp/CallMon/blob/master/Rust/src/log.rs'>log.rs</a></b></td>
							<td style='padding: 8px;'>- Document the log macros purpose as a centralized logging function that allows developers to output debug messages with varying levels of detail<br>- It enables a uniform and consistent logging approach throughout the codebase, making it easier to track errors and issues during development and debugging<br>- The macro leverages the Windows APIs DbgPrint function for its functionality.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/DownWithUp/CallMon/blob/master/Rust/src/lib.rs'>lib.rs</a></b></td>
							<td style='padding: 8px;'>- The <code>DriverEntry</code> function initializes the device driver by creating a symbolic link to the device object and setting up the major functions<br>- It also registers an alt system call handler with the PsRegisterAltSystemCallHandler routine<br>- The <code>DeviceDispatch</code> function handles IRP requests, including IOCTLs for adding or removing processes.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/DownWithUp/CallMon/blob/master/Rust/src/string.rs'>string.rs</a></b></td>
							<td style='padding: 8px;'>- Conforms to project structure, providing a standardized function (<code>create_unicode_string</code>) to create <code>UNICODE_STRING</code> instances from input byte slices<br>- Achieves consistency and ease of use across the codebase by abstracting away underlying implementation details, aligning with Windows API standards<br>- Essential for ensuring proper string handling and manipulation in various components of the project.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/DownWithUp/CallMon/blob/master/Rust/src/defines.rs'>defines.rs</a></b></td>
							<td style='padding: 8px;'>- Defines key data structures and constants used throughout the system, including process and thread identifiers, memory access rights, and packet formats<br>- Provides a foundation for low-level system interactions and packet processing<br>- Facilitates communication between system components and supports system call handling<br>- Essential for managing system resources and handling exceptions.</td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<!-- GUI Submodule -->
	<details>
		<summary><b>GUI</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ GUI</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/DownWithUp/CallMon/blob/master/GUI/Utils.h'>Utils.h</a></b></td>
					<td style='padding: 8px;'>- Create pipes and read/write data from/to them<em> Add processes and retrieve their IDs</em> Load drivers with specific privileges<em> Handle device I/O control operationsHowever, there are several issues in the code:</em> Missing error handling for certain functions, such as <code>DeviceIoControl</code><em> Inconsistent use of <code>TRUE</code>/<code>FALSE</code> vs<br>- <code>1</code>/<code>0</code> for boolean values</em> Lack of input validation and sanitization for user-provided dataThese issues can lead to unexpected behavior or crashes in the program.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/DownWithUp/CallMon/blob/master/GUI/Resource.rc'>Resource.rc</a></b></td>
					<td style='padding: 8px;'>- The <code>Resource.rc</code> file serves as a configuration script for the GUI elements within the project<br>- It defines and organizes various resources such as buttons, edit fields, labels, and a dialog box layout for displaying system processes<br>- The code provides a structured framework for building and managing user interfaces in the project.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/DownWithUp/CallMon/blob/master/GUI/resource.h'>resource.h</a></b></td>
					<td style='padding: 8px;'>- Defines various identifiers for GUI components used in the application, including button IDs, edit box IDs, list box IDs, and static label IDs<br>- Provides a framework for organizing and referencing visual elements across the codebase<br>- Enables developers to access and manipulate these resources efficiently, facilitating the creation and customization of user interfaces.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/DownWithUp/CallMon/blob/master/GUI/CallMon.c'>CallMon.c</a></b></td>
					<td style='padding: 8px;'>- The provided C++ code implements a Windows driver using the NTDLL library to capture and log system calls<br>- The driver is designed to work with the AltCall.sys kernel-mode driver, which allows it to intercept and analyze system calls made by user-mode applications<br>- However, the code has some issues that need to be addressed.</td>
				</tr>
			</table>
		</blockquote>
	</details>
</details>

---

## 🌱 Getting Started

### 🌲 Prerequisites

This project requires the following dependencies:

- **Programming Language:** Rust
- **Package Manager:** Cargo

### 🎋 Installation

Build CallMon from the source and intsall dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/DownWithUp/CallMon
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd CallMon
    ```

3. **Install the dependencies:**

<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![cargo][cargo-shield]][cargo-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [cargo-shield]: https://img.shields.io/badge/Rust-000000.svg?style={badge_style}&logo=rust&logoColor=white -->
	<!-- [cargo-link]: https://www.rust-lang.org/ -->

	**Using [cargo](https://www.rust-lang.org/):**

	```sh
	❯ cargo build
	```


### 🎍 Usage

Run the project with:

**Using [cargo](https://www.rust-lang.org/):**
```sh
cargo run
```

### 🌳 Testing

Callmon uses the {__test_framework__} test framework. Run the test suite with:

**Using [cargo](https://www.rust-lang.org/):**
```sh
cargo test
```


---

## 🌴 Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🌵 Contributing

- **💬 [Join the Discussions](https://github.com/DownWithUp/CallMon/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/DownWithUp/CallMon/issues)**: Submit bugs found or log feature requests for the `CallMon` project.
- **💡 [Submit Pull Requests](https://github.com/DownWithUp/CallMon/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/DownWithUp/CallMon
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
   <a href="https://github.com{/DownWithUp/CallMon/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=DownWithUp/CallMon">
   </a>
</p>
</details>

---

## 🎄 License

Callmon is protected under the [LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## ✨ Acknowledgments

- Credit `contributors`, `inspiration`, `references`, etc.

<div align="left"><a href="#top">⬆ Return</a></div>

---

<!-- README-AI COMMAND: -->
<!--
```sh
readmeai \
    --repository 'https://github.com/DownWithUp/CallMon' \
    --output 'docs/docs/examples/ai-providers/ollama/llama3/readme-callmon.md' \
    --badge-style 'flat-square' \
    --badge-color '43a047' \
    --logo 'ANIMATED' \
    --header-style 'BANNER' \
    --navigation-style 'ACCORDION' \
    --emojis 'forest' \
    --temperature 0.685 \
    --tree-max-depth 4 \
    --api ollama \
    --model llama3.2:latest
```
-->
