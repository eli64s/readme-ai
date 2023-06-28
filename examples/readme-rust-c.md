
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
CallMon
</h1>
<h3>◦ Tracking calls made easy.</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/C-A8B9CC.svg?style&logo=C&logoColor=black" alt="C" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
<img src="https://img.shields.io/badge/Rust-000000.svg?style&logo=Rust&logoColor=white" alt="Rust" />
</p>

![GitHub top language](https://img.shields.io/github/languages/top/DownWithUp/CallMon?style&color=5D6D7E)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/DownWithUp/CallMon?style&color=5D6D7E)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/DownWithUp/CallMon?style&color=5D6D7E)
![GitHub license](https://img.shields.io/github/license/DownWithUp/CallMon?style&color=5D6D7E)
</div>

---

## 📒 Table of Contents
- [📒 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [⚙️ Features](#-features)
- [📂 Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🚀 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The "CallMon" project is a kernel-mode driver and accompanying GUI application that work together to capture and display information about system call events in the Windows operating system. The driver component hooks system call handlers and communicates with the GUI application through a named pipe. The GUI application creates a dialog box and displays information about the processes that make system calls. By providing insights into the system call activities of different processes, the project enables users to monitor and analyze system-level behavior, aiding in debugging and security analysis efforts.

---

## ⚙️ Features

| Feature                | Description                           |
| ---------------------- | ------------------------------------- |
| **⚙️ Architecture**    | The system follows a modular architecture, with separate components for the driver and the GUI application. The driver handles system call monitoring and communicates with the GUI application via IOCTL requests and a named pipe. The GUI application is responsible for creating the GUI dialog and displaying information about system call events. Overall, the architecture promotes separation of concerns and allows for easy maintenance and scalability.    |
| **📖 Documentation**   | The codebase lacks comprehensive documentation. While some code files have brief comments, there is no centralized or detailed documentation explaining the purpose, usage, and design choices of the components. Improving the documentation would greatly benefit developers and make the codebase more accessible to new contributors.    |
| **🔗 Dependencies**    | The system relies on external dependencies such as the Windows API, Rust, and the winapi crate. These dependencies provide access to low-level functionality required for kernel-mode driver development and GUI development. The codebase should be kept updated with the latest versions of these dependencies to ensure compatibility and security.    |
| **🧩 Modularity**      | The system exhibits a good level of modularity, with clear separation between the driver and GUI components. Functionalities such as process management, syscall monitoring, communication, and GUI rendering are organized into their respective modules. This allows for easy maintenance, testing, and reusability of the codebase.    |
| **✔️ Testing**         | The codebase does not include a dedicated testing strategy or testing tools. Adding unit tests for critical components and employing a testing framework such as Rust's `cargo test` would help ensure the correctness and robustness of the system. Additionally, considering automated integration testing between the driver and GUI application would be beneficial.    |
| **⚡️ Performance**     | Given that the system deals with kernel-mode driver development, it is crucial to prioritize performance. However, without specific performance optimizations mentioned in the codebase, it is challenging to make conclusive remarks. Performance profiling and optimization techniques can be employed to analyze and enhance the system's speed, efficiency, and resource usage.    |
| **🔐 Security**        | Security measures must be a top concern in the development of a kernel-mode driver. While the codebase handles aspects such as process isolation, access control, and interaction with the Windows API, a comprehensive security analysis of the system could not be obtained solely from code review. Following secure coding practices, code audits, and threat modeling would be essential for ensuring the system's security.    |
| **🔀 Version Control** | The codebase utilizes the Git version control system, as evident from its presence on GitHub. However, the analysis of the repository did not provide an indication of specific version control strategies or tools employed. To streamline the development process and facilitate collaboration, teams should make use of branching, tagging, and code

---


## 📂 Project Structure


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

## 🧩 Modules

<details closed><summary>Driver</summary>

| File                                                                          | Summary                                                                                                                                                                                                                                                                                                                         |
| ---                                                                           | ---                                                                                                                                                                                                                                                                                                                             |
| [AltCall.c](https://github.com/DownWithUp/CallMon/blob/main/Driver/AltCall.c) | The provided code snippet is a driver implementation that provides functionality for adding and removing processes, as well as hooking system call handlers. It also includes an IOCTL handler for managing communication with a named pipe and a driver entry and unload function for initializing and cleaning up the driver. |
| [Extras.h](https://github.com/DownWithUp/CallMon/blob/main/Driver/Extras.h)   | The code snippet defines structures for a custom packet header and a total packet.The custom header contains a process ID and an array of stack data.The total packet combines the custom header with a KTRAP_FRAME structure.                                                                                                  |

</details>

<details closed><summary>Rust</summary>

| File                                                                      | Summary                                                                                                                                                                                                                                                         |
| ---                                                                       | ---                                                                                                                                                                                                                                                             |
| [build.rs](https://github.com/DownWithUp/CallMon/blob/main/Rust/build.rs) | The code snippet retrieves the path to Windows Kits directory and the kernel mode libraries. It then determines the appropriate architecture based on the target platform. Finally, it uses the obtained paths to configure the Rust build process for linking. |

</details>

<details closed><summary>.cargo</summary>

| File                                                                         | Summary                                                                                                                                                                                                                                                        |
| ---                                                                          | ---                                                                                                                                                                                                                                                            |
| [config](https://github.com/DownWithUp/CallMon/blob/main/Rust/.cargo/config) | This code snippet is a configuration file for building a Rust project on Windows. It sets various pre and post link arguments, like disabling certain default libraries, specifying the subsystem and entry point, optimizing code, and maintaining integrity. |

</details>

<details closed><summary>Src</summary>

| File                                                                              | Summary                                                                                                                                                                                                                                                                                                                                           |
| ---                                                                               | ---                                                                                                                                                                                                                                                                                                                                               |
| [externs.rs](https://github.com/DownWithUp/CallMon/blob/main/Rust/src/externs.rs) | This code snippet imports a set of functions from Windows API libraries and defines some types. These functions provide functionalities such as creating devices, creating symbolic links, suspending and resuming processes, creating and writing to files, closing file handles, managing process and object references, and memory operations. |
| [log.rs](https://github.com/DownWithUp/CallMon/blob/main/Rust/src/log.rs)         | The provided code snippet is a logging macro that utilizes the `DbgPrint` function from the `winapi` crate. It allows for printing messages to the debugger console with optional formatting and variable interpolation.                                                                                                                          |
| [lib.rs](https://github.com/DownWithUp/CallMon/blob/main/Rust/src/lib.rs)         | This code snippet is a kernel-mode driver that creates a device and handles various device I/O control requests. It also includes functions to add and remove processes, and supports a custom handler.                                                                                                                                           |
| [string.rs](https://github.com/DownWithUp/CallMon/blob/main/Rust/src/string.rs)   | This code snippet defines a function that creates a Unicode string from a slice of u16 values. It determines the length of the string, sets the length and maximum length fields of a UNICODE_STRING struct accordingly, and assigns the buffer pointer to the start of the string.                                                               |
| [defines.rs](https://github.com/DownWithUp/CallMon/blob/main/Rust/src/defines.rs) | The provided code snippet defines various structs, unions, and constants that are used for interacting with Windows kernel-mode APIs. It includes custom structs and unions that are not provided by the `winapi` crate. These definitions are necessary for utilizing specific functionality in kernel-mode programming.                         |

</details>

<details closed><summary>Gui</summary>

| File                                                                           | Summary                                                                                                                                                                                                                                                                                                                                    |
| ---                                                                            | ---                                                                                                                                                                                                                                                                                                                                        |
| [Utils.h](https://github.com/DownWithUp/CallMon/blob/main/GUI/Utils.h)         | The code snippet includes functionalities to obtain device access, create a named pipe, add processes, load a driver, and define data structures. It also includes a helper function for inserting a column in a list view.                                                                                                                |
| [Resource.rc](https://github.com/DownWithUp/CallMon/blob/main/GUI/Resource.rc) | This code snippet is a Microsoft Visual C++ generated resource script. It contains the definition and layout of a dialog box for a software application called "CallMon". The dialog box includes various controls such as buttons, text fields, and a list view. It also defines the design info and layout for the dialog box.           |
| [resource.h](https://github.com/DownWithUp/CallMon/blob/main/GUI/resource.h)   | The provided code snippet is a resource file for a Windows application. It defines various IDs for dialog controls, such as buttons, edit boxes, and lists. These IDs are used to reference and manipulate these controls within the application's code.                                                                                   |
| [CallMon.c](https://github.com/DownWithUp/CallMon/blob/main/GUI/CallMon.c)     | The provided code snippet is a Windows application that creates a GUI dialog to display information about system call events. It sets up the GUI and handles various window messages, including button clicks and resizing. It also communicates with a driver to capture and display data about system calls made by different processes. |

</details>

---

## 🚀 Getting Started

### ✔️ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - `ℹ️ Requirement 1`
> - `ℹ️ Requirement 2`
> - `ℹ️ ...`

### 💻 Installation

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

### 🎮 Using CallMon

```sh
cargo run
```

### 🧪 Running Tests
```sh
cargo test
```

---


## 🗺 Roadmap

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
