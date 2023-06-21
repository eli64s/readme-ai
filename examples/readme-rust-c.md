
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
CallMon
</h1>
<h3>◦ Stay on top of your calls with CallMon.</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/C-A8B9CC.svg?style&logo=C&logoColor=black" alt="C" />
<img src="https://img.shields.io/badge/Rust-000000.svg?style&logo=Rust&logoColor=white" alt="Rust" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
</p>

![GitHub top language](https://img.shields.io/github/languages/top/DownWithUp/CallMon?style&color=5D6D7E)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/DownWithUp/CallMon?style&color=5D6D7E)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/DownWithUp/CallMon?style&color=5D6D7E)
![GitHub license](https://img.shields.io/github/license/DownWithUp/CallMon?style&color=5D6D7E)
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

The CallMon project is a driver program in the Windows kernel mode that allows users to monitor and manipulate system calls. It can suspend and resume processes, examine user mode stack, and write data to a named pipe. The Rust code provides the driver functionality and the GUI allows users to interact with the driver. This project's value proposition is its ability to help users effectively debug system calls and monitor system performance.

---

## ⚙️ Features

Feature | Description |
|-----|-----|
| **🏗 Architecture** | The codebase is a kernel-mode driver that creates a device object and registers an alternative system call handler. It provides functionality for adding and removing processes, initializing a named pipe, suspending and resuming processes, and walking through user mode stacks. The code is written in Rust and uses the winapi crate to interface with the Windows API. |
| **📑 Documentation** | The repository lacks detailed documentation, but the codebase is well-commented, providing insights into the functions and structures' purpose. The comments explain the primary functionalities, making it relatively easy to understand the codebase's design decisions and flow. |
| **🧩 Dependencies** | The codebase relies on the Rust programming language, which provides a powerful and safe foundation for systems-level programming. It also uses the winapi and kernel32 crates for interfacing with the Windows API and handles various kernel-mode programming constructs. The codebase's build process uses the Cargo build system to manage dependencies and build the final driver. |
| **♻️ Modularity** | The codebase is relatively modular, with each file having a specific purpose and set of functionalities. The Rust code defines custom types, constants, structs, unions, and pointers used in Windows kernel-mode programming and provides various functions for interacting with the Windows API. The driver's core functionalities are located in the lib.rs file, making it easy to modify and add new features. |
| **✔️ Testing** | The codebase lacks testing, which is typical for low-level systems-level programming. Due to the codebase's nature, testing is impossible without using external tools that are not present in the repository. Therefore, any change made to the codebase must be thoroughly reviewed and tested manually to avoid introducing new bugs or regressions. |
| **⚡️ Performance** | The codebase focuses on high performance and low overhead, prioritizing efficient memory handling and interaction with the Windows API. The codebase's Rust implementation compiles to a native executable, which compared to a VM-based language interpreter, helps to reduce overheads. The Rust programming language also benefits from zero-cost abstractions, making it possible to write high-level code that compiles to low-level machine code. |
| **🔒 Security** | The codebase is written in Rust, a programming language that emphasizes memory safety and low-level system programming. The Rust language's design guarantees that memory accesses are always safe and that the code does not contain common vulnerabilities such as buffer overflows, null pointer dereferences, and dangling pointers. The codebase's adherence to Rust's memory safety guarantees makes it significantly less likely to be affected by common security vulnerabilities. |
| **🔀 Version Control** | The repository uses git as its version control system, providing support for collaboration and enabling contributors to fork and submit pull requests. The repository follows a traditional branching model, with the master branch

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

| File   | Summary                                                                                                                                                                                                                                                                                                                                                                                                              | Module             |
|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
| config | The provided code snippet sets build target to "x86_64-pc-windows-msvc" and specifies various rustflags including pre-link and post-link arguments such as disabling logging, enabling DEP, disabling default libraries, setting subsystem to native, enabling dynamic base addresses, etc. These flags help optimize the build process and ensure the resulting driver has high integrity and improved performance. | Rust/.cargo/config |

</details>

<details closed><summary>Driver</summary>

| File      | Summary                                                                                                                                                                                                                                                                                                      | Module           |
|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| AltCall.c | This code is a kernel mode driver that creates a device object and registers an alternative system call handler. It exposes three different IOCTLs for adding, removing, and initializing a process. It can also suspend and resume a process, walk through user mode stack, and write data to a named pipe. | Driver/AltCall.c |
| Extras.h  | The code snippet defines two structures, CUSTOM_HEADER and TOTAL_PACKET. The CUSTOM_HEADER structure contains a ProcessId field and an array of 16 StackData elements. The TOTAL_PACKET structure comprises a CUSTOM_HEADER and a KTRAP_FRAME, creating a total packet for data transmission.                | Driver/Extras.h  |

</details>

<details closed><summary>Gui</summary>

| File        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                          | Module          |
|:------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------|
| Utils.h     | The provided code snippet contains various function definitions and global variables. It includes functions for obtaining device handles, creating pipes, adding processes, obtaining driver privileges, and loading drivers. It also includes various struct definitions, including one for a custom header and another for a KTrap frame. Additionally, it includes a function for inserting a column into a ListView control. | GUI/Utils.h     |
| Resource.rc | The code snippet provides a resource script for a Windows dialog box application. It includes the definition for the dialog box layout, the controls used, and the associated resources, such as strings. The script is generated by Microsoft Visual C++ and primarily uses the English (United States) language.                                                                                                               | GUI/Resource.rc |
| resource.h  | The code snippet provides a resource file with various predefined dialog box components such as buttons, text fields, and a list. These are identified by associated ID numbers and provide functionality for adding, removing, and clearing items in a stack.                                                                                                                                                                   | GUI/resource.h  |
| CallMon.c   | HTTPStatusError: 400                                                                                                                                                                                                                                                                                                                                                                                                             | GUI/CallMon.c   |

</details>

<details closed><summary>Rust</summary>

| File     | Summary                                                                                                                                                                                                                                                                                                                                                                                                     | Module        |
|:---------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------|
| build.rs | The provided code snippet defines functions for finding the path to the Windows Kits directory and the kernel mode libraries, to be used for linking in Rust code. It also includes logic to handle different architectures and a conditional branch for extra link search functionality. The code utilizes the `winreg` and `failure` crates for interacting with the Windows registry and error handling. | Rust/build.rs |

</details>

<details closed><summary>Src</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Module              |
|:-----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------|
| externs.rs | This code snippet provides external function declarations for various Windows kernel functions such as creating and opening device objects, suspending and resuming processes, writing to files, and accessing process information. It also includes memory handling functions for moving data and reference and dereference operations for accessing kernel objects.                                                                                     | Rust/src/externs.rs |
| log.rs     | This code defines a macro called "log" that can be used for debugging purposes. The macro uses the winapi library's DbgPrint function to print the provided string to the kernel debugger. It has two variations: one for a single string argument, and another using printf-style formatting with multiple arguments.                                                                                                                                    | Rust/src/log.rs     |
| lib.rs     | The code defines a kernel-mode driver that creates a device object and handles major device control IRPs. It also provides functions to add and remove a process and initialize a named pipe. Additionally, it uses an alternate system call handler to write data to the pipe when a trap handler is called. The code relies on several external functions and defines a few global variables and macros.                                                | Rust/src/lib.rs     |
| string.rs  | The provided code snippet defines a function called "create_unicode_string" that takes a string of 16-bit Unicode characters as input and returns a structure of type "UNICODE_STRING". The function determines the length of the input string, creates a new string with no null terminator if necessary, and returns the new Unicode string as a "UNICODE_STRING" structure with its length, maximum length, and buffer pointer values set accordingly. | Rust/src/string.rs  |
| defines.rs | The provided code snippet defines various custom types, constants, structs, unions, and pointers used in Windows kernel-mode programming. It includes definitions for accessing and manipulating system registers and structures, handling system calls, and interacting with hardware. The code is written in Rust and uses the winapi crate to interface with the Windows API.                                                                          | Rust/src/defines.rs |

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
