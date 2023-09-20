<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>CallMon
</h1>
<h3>◦ Connect, collaborate, and monitor calls with CallMon</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/C-A8B9CC.svg?style&logo=C&logoColor=black" alt="C" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
<img src="https://img.shields.io/badge/Rust-000000.svg?style&logo=Rust&logoColor=white" alt="Rust" />
</p>
<img src="https://img.shields.io/github/languages/top/DownWithUp/CallMon?style&color=5D6D7E" alt="GitHub top language" />
<img src="https://img.shields.io/github/languages/code-size/DownWithUp/CallMon?style&color=5D6D7E" alt="GitHub code size in bytes" />
<img src="https://img.shields.io/github/commit-activity/m/DownWithUp/CallMon?style&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/license/DownWithUp/CallMon?style&color=5D6D7E" alt="GitHub license" />
</div>

---

## 📖 Table of Contents
- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [⚙️ Modules](#modules)
- [🚀 Getting Started](#-getting-started)
    - [🔧 Installation](#-installation)
    - [🤖 Running CallMon](#-running-CallMon)
    - [🧪 Tests](#-tests)
- [🛣 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The project at https://github.com/DownWithUp/CallMon is a Windows driver and GUI application that allows for the monitoring and manipulation of system calls made by processes. It provides functionality to add and remove processes, suspend and resume processes, and register a handler for system calls. The project's value proposition lies in its ability to provide insights and control over system call activity, making it useful for debugging, security analysis, and performance profiling purposes.

---

## 📦 Features

| Feature                | Description                           |
| ---------------------- | ------------------------------------- |
| **⚙️ Architecture**     | The system follows a modular architecture, with separate components for the driver, Rust library, and GUI application. The driver allows monitoring and manipulation of system calls, while the Rust library provides integration with the Windows API. The GUI application provides a user-friendly interface for interacting with the driver. Overall, the system follows a layered design pattern, separating the UI, business logic, and system integration. |
| **📃 Documentation**   | The project lacks comprehensive documentation. While individual files have brief descriptions, there is no overarching documentation explaining the project's purpose, usage, or design decisions. This can make it challenging for new contributors or users to understand and navigate the codebase. Improved documentation would enhance the project's accessibility and usability. |
| **🔗 Dependencies**    | The system relies on various external libraries and crates, including "winapi," "winreg," "failure," and "obfstr." These dependencies provide integration with the Windows API, error handling functionality, and obfuscation capabilities. The project also utilizes environment variables to configure build paths and flags. Managing these dependencies is crucial to ensure compatibility and stability across different versions. |
| **🧩 Modularity**      | The codebase demonstrates good modularity by dividing the functionality into separate files and components. The driver, Rust library, and GUI application each have their own directories and files, encapsulating related functionalities. This modular approach makes the codebase easier to understand, maintain, and test. The use of different files for struct definitions, utility functions, and integration with external systems further enhances modularity. |
| **🧪 Testing**          | The project lacks explicit testing strategies and tools. While the code includes error handling and input validations, there is no evidence of unit tests or automated test suites. Introducing a testing framework, such as Rust's built-in testing framework or a third-party library like `rust-test` or `cargo-test`, would improve code reliability and maintainability. Proper testing is crucial for ensuring the project's correctness and identifying bugs or regressions. |
| **⚡️ Performance**      | As a driver-based system, performance is a critical aspect. The project leverages low-level system APIs and optimized Rust code to ensure efficient system call monitoring and manipulation. However, without specific performance benchmarks or profiling data, it is challenging to determine the performance characteristics accurately. To evaluate performance, it would be beneficial to conduct performance testing using realistic workloads and scenarios to identify any bottlenecks or areas for optimization. |
| **🔐 Security**        | The system's security measures are not explicitly mentioned in the provided information. However, given that the project involves manipulating system calls and interacting with the Windows API, it's crucial to ensure robust security practices. This includes handling user input securely, preventing privilege escalation, and protecting sensitive information. Conducting security audits, staying updated with security patches, and following secure coding practices are essential to maintain the project's security. |
| **🔀 Version Control** | The project uses Git for version control, with the codebase hosted on GitHub. The GitHub repository includes a complete history of commits, allowing for easy tracking of changes and collaboration among team members. It enables branching for feature development, bug fixes, and experimental work. However, without additional information, it is difficult to assess the specific version control strategies or

---


## 📂 Repository Structure


```bash
repo
├── Driver
│   ├── AltCall.c
│   └── Extras.h
├── GUI
│   ├── CallMon.c
│   ├── Resource.rc
│   ├── Utils.h
│   └── resource.h
├── README.md
└── Rust
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

5 directories, 16 files
```

---

## ⚙️ Modules

<details closed><summary>Driver</summary>

| File                                                                          | Summary                                                                                                                                                                                                                                                                                            |
| ---                                                                           | ---                                                                                                                                                                                                                                                                                                |
| [AltCall.c](https://github.com/DownWithUp/CallMon/blob/main/Driver/AltCall.c) | The code is a Windows driver that allows monitoring and manipulation of system calls made by processes. It provides functionality to add and remove processes, suspend and resume processes, and register a handler for system calls. It also includes device control functions for communication. |
| [Extras.h](https://github.com/DownWithUp/CallMon/blob/main/Driver/Extras.h)   | The code defines two structures: CUSTOM_HEADER and TOTAL_PACKET. The CUSTOM_HEADER structure contains a process ID and an array of stack data. The TOTAL_PACKET structure combines the CUSTOM_HEADER structure with a KTRAP_FRAME structure.                                                       |

</details>

<details closed><summary>Rust</summary>

| File                                                                                | Summary                                                                                                                                                                                                                                                                                                                                                                                              |
| ---                                                                                 | ---                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Makefile.toml](https://github.com/DownWithUp/CallMon/blob/main/Rust/Makefile.toml) | This code defines a set of tasks for building, renaming, and signing a Windows driver. It uses environment variables for target paths and build flags, and the tasks are executed sequentially with dependencies. The final task signs the driver using a self-signed certificate and a timestamp service.                                                                                           |
| [Cargo.toml](https://github.com/DownWithUp/CallMon/blob/main/Rust/Cargo.toml)       | The code is a Rust package named "AltCall" that contains a library with dynamic linking capabilities. It depends on other crates such as "kernel-print" and "kernel-alloc" for kernel-level operations, and "obfstr" for obfuscation functionality. It also relies on the "winapi" crate for Windows API integration. Additionally, it uses the "winreg" and "failure" crates for building purposes. |
| [rustfmt.toml](https://github.com/DownWithUp/CallMon/blob/main/Rust/rustfmt.toml)   | This code configures various formatting options for the Rust codebase. It sets rules for indentation, line breaks, ordering, and shorthand usage. The aim is to improve code readability and maintain consistency.                                                                                                                                                                                   |
| [build.rs](https://github.com/DownWithUp/CallMon/blob/main/Rust/build.rs)           | The code retrieves the path to the Windows Kits directory and the kernel mode libraries. It then determines the appropriate architecture and sets the link search path for the Rust compiler.                                                                                                                                                                                                        |

</details>

<details closed><summary>.cargo</summary>

| File                                                                         | Summary                                                                                                                                                                                                                                                                                         |
| ---                                                                          | ---                                                                                                                                                                                                                                                                                             |
| [config](https://github.com/DownWithUp/CallMon/blob/main/Rust/.cargo/config) | This code sets specific build configurations for a Rust project targeting Windows. It includes pre-link and post-link arguments, specifying various options for optimization, linking, and subsystems. The code aims to optimize and configure the executable for a native Windows environment. |

</details>

<details closed><summary>Src</summary>

| File                                                                              | Summary                                                                                                                                                                                                                                                                                                                                      |
| ---                                                                               | ---                                                                                                                                                                                                                                                                                                                                          |
| [externs.rs](https://github.com/DownWithUp/CallMon/blob/main/Rust/src/externs.rs) | This code provides bindings to various WinAPI functions for device creation, process suspension and resumption, file operations, and object handling. It also includes memory and process-related functions for managing kernel mode drivers efficiently.                                                                                    |
| [log.rs](https://github.com/DownWithUp/CallMon/blob/main/Rust/src/log.rs)         | This code provides a logging functionality utilizing Windows DbgPrint API. It includes a macro that allows printing formatted messages to the debug console, with support for variable arguments.                                                                                                                                            |
| [lib.rs](https://github.com/DownWithUp/CallMon/blob/main/Rust/src/lib.rs)         | The code is a driver that handles various functionalities such as handling IRP requests, creating and closing a named pipe, suspending and resuming processes, and registering an alternative system call handler. It also includes error handling and initialization functions.                                                             |
| [string.rs](https://github.com/DownWithUp/CallMon/blob/main/Rust/src/string.rs)   | The code defines a function that creates a UNICODE_STRING structure from a slice of UTF-16 encoded Unicode characters. It calculates the length of the string, removes any null terminator if present, and then initializes the fields of the UNICODE_STRING struct with appropriate values.                                                 |
| [defines.rs](https://github.com/DownWithUp/CallMon/blob/main/Rust/src/defines.rs) | This code defines various structs, unions, and constants that are required for interacting with the Windows operating system. It includes definitions for process and thread identifiers, object handle information, trap frames, and custom headers. Overall, it provides the necessary building blocks for working with Windows internals. |

</details>

<details closed><summary>Gui</summary>

| File                                                                           | Summary                                                                                                                                                                                                                                                                                                                                              |
| ---                                                                            | ---                                                                                                                                                                                                                                                                                                                                                  |
| [Utils.h](https://github.com/DownWithUp/CallMon/blob/main/GUI/Utils.h)         | This code includes functionality to create a driver handle, create a named pipe, add a process to the driver, obtain driver privilege, and load the driver. It also includes structures for stack chunks and custom headers, as well as a function to insert a column in a ListView.                                                                 |
| [Resource.rc](https://github.com/DownWithUp/CallMon/blob/main/GUI/Resource.rc) | The code is a resource script for a Windows application. It defines the layout and controls for a dialog window called "CallMon". The dialog includes a group box, buttons, an edit box, a list view, and a memo control. It provides functionality for initializing, adding and removing processes, capturing stack information, and clearing data. |
| [resource.h](https://github.com/DownWithUp/CallMon/blob/main/GUI/resource.h)   | The code consists of a dialog-based application with various controls such as buttons, edit boxes, and a list. The core functionalities include initializing the application, adding items to the list, removing items from the list, and clearing the list. There is also a memo stack control for displaying additional information.               |
| [CallMon.c](https://github.com/DownWithUp/CallMon/blob/main/GUI/CallMon.c)     | HTTPStatus Exception: 400                                                                                                                                                                                                                                                                                                                            |

</details>

---

## 🚀 Getting Started

***Dependencies***

Before you begin, ensure that you have the following prerequisites installed:
> - `ℹ️ Requirement 1`
> - `ℹ️ Requirement 2`
> - `ℹ️ ...`

### 🔧 Installation

1. Clone the CallMon repository:
```sh
git clone https://github.com/DownWithUp/CallMon
```

2. Change to the project directory:
```sh
cd CallMon
```

3. Install the dependencies:
```sh
cargo build
```

### 🤖 Running CallMon

```sh
cargo run
```

### 🧪 Tests
```sh
cargo test
```

---


## 🛣 Roadmap

> - [X] `ℹ️  Task 1: Implement X`
> - [ ] `ℹ️  Task 2: Refactor Y`
> - [ ] `ℹ️ ...`


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
7. Create a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 📄 License

This project is licensed under the `ℹ️  INSERT-LICENSE-TYPE` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 👏 Acknowledgments

> - `ℹ️  List any resources, contributors, inspiration, etc.`

---
