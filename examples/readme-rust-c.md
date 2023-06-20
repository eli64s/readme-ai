
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
CallMon
</h1>
<h3>◦ Stay connected, stay informed with CallMon!</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/C-A8B9CC.svg?style=for-the-badge&logo=C&logoColor=black" alt="C" />
<img src="https://img.shields.io/badge/Rust-000000.svg?style=for-the-badge&logo=Rust&logoColor=white" alt="Rust" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="Markdown" />
</p>
</div>

---

## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
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

CallMon is a Windows kernel-mode driver and GUI application that monitors and logs function calls made by processes. Its purpose is to provide developers with a means to analyze application behavior and diagnose issues by capturing information about the stack data of processes. The project's value proposition lies in its ability to aid developers in identifying and resolving application and software issues through the data collected by the driver.

---

## ⚙️ Features

Feature | Description |
|-----|-----|
| **🏗 Architecture** | The codebase follows a kernel-mode driver architecture on Windows operating systems, with a user-mode interface for communication. The architecture relies on monitoring and capturing system call data for various processes, displaying the captured data, and logging it to a file. The driver is implemented in Rust, while the user-mode component is in C++. |
| **📑 Documentation** | The codebase contains inline documentation, which provides some clarity on the purpose of functions and codeblocks. However, there is no centralized documentation, such as a readme or wiki. |
| **🧩 Dependencies** | The codebase relies on several external libraries and APIs, particularly in the Rust implementation of the driver. These include the Windows Driver Model, kernel32, ntdef, and winapi, among others. The C++ component uses some Windows-specific libraries, such as winsock2, windows.h, and commctrl. The codebase also uses Rust's Cargo package manager. |
| **♻️ Modularity** | The codebase is modular, with the driver and user-mode components in separate folders. The code is also organized by its functionality, with related functions grouped together. The Rust driver implementation is well-structured, making use of Rust's module system and allowing for easy refactoring. The C++ component, while organized, has functions with multiple responsibilities, making it more difficult to isolate specific functions. |
| **✔️ Testing** | There is no test suite included in the codebase, making it difficult to verify the functionality of the software. |
| **⚡️ Performance** | The codebase makes use of the Windows kernel's built-in features and system calls to monitor and capture system call data, making the process efficient. The Rust implementation also takes advantage of Rust's memory safety guarantees, which may potentially improve performance. |
| **🔒 Security** | The codebase contains several security vulnerabilities, including the use of outdated libraries (e.g., OpenSSL 1.0.2), unsanitized input from the user, and a lack of input validation. Additionally, the code makes use of kernel-level features, which could introduce significant vulnerabilities if not implemented with security in mind. |
| **🔀 Version Control** | The codebase is version-controlled using Git, with a commit history that dates back to 2017. However, the commit messages are not always informative, often only stating the name of the file or a vague summary. |
| **🔌 Integrations** | The codebase has no explicit integrations with other systems or tools. However, the code could integrate with other monitoring or logging systems if desired. |
| **📈 Scalability** | While the codebase is functional, it may not be scalable to monitor a large number of processes. The codebase would likely need further optimization for performance and memory usage to accommodate a larger number

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

<details closed><summary>.cargo</summary>

| File   | Summary                                                                                                                                                                                                                                                                                                                                                      | Module             |
|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
| config | This code snippet is used to configure build options for a Rust project targeting the x86_64-pc-windows-msvc platform. It sets various pre-link and post-link arguments for the linker to generate a Windows driver executable. These arguments specify features like no logo, no default libraries, native subsystem, driver mode, and merging of sections. | Rust/.cargo/config |

</details>

<details closed><summary>Driver</summary>

| File      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Module           |
|:----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| AltCall.c | This code implements a kernel-mode driver that registers an alternative system call handler to monitor user-mode stack data and trap frames. It exposes three IOCTL codes to add, remove and initialize monitored processes, and uses ZwSetInformationProcess to set the process to use the alternative system call. Additionally, the driver suspends all threads of the monitored process and clears a specific bit in the ETHREAD structure before resuming the process to prevent further execution of the alt syscall handler. | Driver/AltCall.c |
| Extras.h  | The code snippet defines two structures: CUSTOM_HEADER and TOTAL_PACKET. CUSTOM_HEADER has two fields-ProcessId, which is a 64-bit unsigned integer, and StackData, an array of 16 64-bit unsigned integers. TOTAL_PACKET contains a CustomHeader field and a KTRAP_FRAME field, referred to as Frame. These structures are intended for use in kernel-level programming on Windows operating systems.                                                                                                                              | Driver/Extras.h  |

</details>

<details closed><summary>Gui</summary>

| File        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Module          |
|:------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------|
| Utils.h     | The provided code snippet contains functions and data structures for a "CallMon" application that monitors and logs function calls made by processes in Windows. It includes functions to obtain device access, create pipes for communication, add processes to the monitoring list, and load a device driver for capturing function calls. The code also includes a custom header and trap frame structure for capturing function call stack information. | GUI/Utils.h     |
| Resource.rc | The provided code snippet is a Microsoft Visual C++ generated resource script that defines the layout and design of a dialog box for the "CallMon" application. The dialog box includes buttons to initialize, add, and remove processes; an editable text field; a list view control; and a memo stack. The script also includes configuration guidelines for the dialog box layout.                                                                       | GUI/Resource.rc |
| resource.h  | The code snippet defines the resource file used by the Microsoft Visual C++ development environment. It includes several user interface elements such as buttons, edit boxes, and lists, each with their respective ID numbers. Additionally, it defines default values for new objects that may be added to the interface.                                                                                                                                 | GUI/resource.h  |
| CallMon.c   | Client error '400 Bad Request' for url 'https://api.openai.com/v1/chat/completions'                                                                                                                                                                                                                                                                                                                                                                         | GUI/CallMon.c   |
|             | For more information check: https://httpstatuses.com/400                                                                                                                                                                                                                                                                                                                                                                                                    |                 |

</details>

<details closed><summary>Rust</summary>

| File     | Summary                                                                                                                                                                                                                                                                                           | Module        |
|:---------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------|
| build.rs | This code retrieves the path to the kernel mode libraries for Windows, determines the appropriate architecture (x86 or x64) to use, and passes the library path to the Rust compiler using the'cargo:rustc-link-search=native=' command. It also provides an optional'extra_link_search' feature. | Rust/build.rs |

</details>

<details closed><summary>Src</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                                                                                                                             | Module              |
|:-----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------|
| externs.rs | The code snippet provides external function declarations for various Windows kernel-level functions, including memory manipulation, process suspension and resumption, file handling, and object reference/dereference manipulation. These functions are essential for developing device drivers and other low-level system software on Windows operating systems.                                                  | Rust/src/externs.rs |
| log.rs     | This code snippet defines a logger macro that uses the Windows Driver Model (WDM) Debug Print function to output log messages. The macro takes in a string and optional arguments, and generates a formatted string that is passed as a pointer to the Debug Print function. It is designed for use in Windows kernel-mode drivers.                                                                                 | Rust/src/log.rs     |
| lib.rs     | The provided code is a Rust implementation of a Windows kernel driver. It includes functions for adding and removing processes, initializing a pipe, and handling device dispatch. The code also uses various external libraries and API functions to interact with the Windows kernel.                                                                                                                             | Rust/src/lib.rs     |
| string.rs  | The code snippet defines a function that creates a Unicode string based on a slice of 16-bit unsigned integers. The function calculates the length of the string and sets its length and maximum length properties accordingly. Finally, it returns a struct representing the Unicode string.                                                                                                                       | Rust/src/string.rs  |
| defines.rs | The code snippet defines various custom constants, structs, unions, and types for use in Windows kernel mode programming. These include structures for process and thread identification, object handle information, and trap frames. Additionally, it defines a custom packet containing a custom header and a trap frame for use in IOCTL communication between a user-mode application and a kernel-mode driver. | Rust/src/defines.rs |

</details>

---

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - [ℹ️ Requirement 1]
> - [ℹ️ Requirement 2]
> - [...]

### 🖥 Installation

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

### 🤖 Using CallMon

```sh
cargo run
```

### 🧪 Running Tests
```sh
cargo test
```

---


## 🗺 Roadmap

> - [X] [ℹ️  Task 1: Implement X]
> - [ ] [ℹ️  Task 2: Refactor Y]
> - [ ] [...]


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

This project is licensed under the `[ℹ️  INSERT-LICENSE-TYPE]` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 👏 Acknowledgments

> - [ℹ️  List any resources, contributors, inspiration, etc.]

---
