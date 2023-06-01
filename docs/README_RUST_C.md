
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
CallMon
</h1>
<h3 align="center">📍 Stay connected with CallMon-your one-stop solution for call monitoring!</h3>
<h3 align="center">🚀 Developed with the software and tools below:</h3>

<p align="center">
<img src="https://img.shields.io/badge/C-A8B9CC.svg?style=for-the-badge&logo=C&logoColor=black" alt="C" />
<img src="https://img.shields.io/badge/Rust-000000.svg?style=for-the-badge&logo=Rust&logoColor=white" alt="Rust" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="Markdown" />
</p>
</div>

---

## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍Overview](#-overview)
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

CallMon is a Windows kernel-mode driver that monitors and intercepts system calls made by processes, allowing them to be added or removed from a list. The driver creates a named pipe to send data, which can be received by a GUI program that displays the list of monitored processes. The project provides a valuable tool for developers and security professionals to analyze and debug system calls made by processes.

---

## 🔮 Features

Feature | Description |
|---|---|
| **🏗 Overall Structure and Organization** | The codebase is divided into three main folders: Driver, Rust, and GUI, with the Rust folder containing the core driver code. The codebase follows a clear naming convention and separates utility functions from core functionality. |
| **📝 Code Documentation** | The codebase lacks comprehensive documentation, with only a few comments and code snippets providing context for certain functions. |
| **🧩 Dependency Management** | Dependencies are managed using Rust's package manager, Cargo, with various external dependencies used for printing to the kernel, memory allocation, and obfuscation. The build process is automated using a Makefile and signtool for signing the driver using a self-signed certificate. |
| **♻️ Code Modularity and Reusability** | The codebase is structured to promote modularity and reusability, with functions separated into their own files and a clear separation of utility functions from core functionality. However, there is a lack of clear API documentation to promote reuse. |
| **✅ Testing and Quality Assurance** | There is no evidence of unit tests or any other form of automated testing in the codebase. The code formatting is consistent and follows Rust's recommended style guidelines. |
| **⚡️ Performance and Optimization** | The codebase utilizes various performance optimization techniques such as removing unused code and merging data sections in the post-linking phase. However, there is a lack of profiling or benchmarking to measure performance. |
| **🔒 Security Measures** | The codebase lacks any clear security measures such as input validation or error handling. The use of a self-signed certificate for signing the driver may also pose a security risk. |
| **🔄 Version Control and Collaboration** | The codebase is hosted on GitHub and follows a standard Git workflow with frequent commits and pull requests. However, there is no clear indication of a code review process in place. |
| **🔌 External Integrations** | The codebase integrates with various Windows APIs for creating and manipulating devices, suspending and resuming processes, creating and writing to files, and referencing and dereferencing objects. |
| **📈 Scalability and Extensibility** | The codebase is designed to handle monitoring and intercepting system calls made by processes and can be extended to include additional functionality. However, the lack of comprehensive documentation and testing may hinder scalability and extensibility. |

---


<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## ⚙️ Project Structure


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

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 💻 Modules

<details closed><summary>.cargo</summary>

| File   | Summary                                                                                                                                                                                                                                                                                                                                                                         | Module             |
|:-------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
| config | The provided code snippet contains build configurations for a Rust project targeting the "x86_64-pc-windows-msvc" platform. It sets panic behavior to abort and includes pre and post-link arguments for the linker. The pre-link arguments specify various linker options while the post-link arguments optimize the binary by removing unused code and merging data sections. | Rust/.cargo/config |

</details>

<details closed><summary>Driver</summary>

| File      | Summary                                                                                                                                                                                                                                                                                           | Module           |
|:----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| AltCall.c | HTTP 429 error when fetching summary.                                                                                                                                                                                                                                                             | Driver/AltCall.c |
| Extras.h  | The code snippet defines two structures: CUSTOM_HEADER and TOTAL_PACKET. CUSTOM_HEADER contains a process ID and an array of 16 stack data elements. TOTAL_PACKET includes a CUSTOM_HEADER and a KTRAP_FRAME structure. These structures can be used in conjunction with kernel mode programming. | Driver/Extras.h  |

</details>

<details closed><summary>Gui</summary>

| File        | Summary                                                                                                                                                                                                                                                                                                                                                                | Module          |
|:------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------|
| Utils.h     | The code snippet includes functions for obtaining device access, creating and manipulating windows, loading a driver, and controlling processes. It also defines structures for passing data to and from the driver, as well as constants used in the code. The code is designed to monitor and intercept system calls made by processes.                              | GUI/Utils.h     |
| Resource.rc | The provided code snippet is a Microsoft Visual C++ generated resource script that defines the layout and design of a GUI for a program called "CallMon". The GUI includes a configuration group box with various controls such as push buttons, edit text boxes, and a list view control. The script also includes design information and layout details for the GUI. | GUI/Resource.rc |
| resource.h  | The provided code snippet defines the resource IDs for a dialog box interface in a Microsoft Visual C++ program. The interface includes buttons for initializing, adding, and removing items from a list, as well as a memo stack and a static label. The code also sets default values for new objects in the interface.                                              | GUI/resource.h  |
| CallMon.c   | HTTP 400 error when fetching summary.                                                                                                                                                                                                                                                                                                                                  | GUI/CallMon.c   |

</details>

<details closed><summary>Rust</summary>

| File          | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                | Module             |
|:--------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
| Makefile.toml | The code snippet defines three tasks: "build-driver" to build the driver binary using Cargo, "rename" to rename the built driver file to ".sys" extension, and "sign" to sign the driver using signtool with a self-signed certificate. The "sign" task also loads the Visual Studio Developer environment and creates a certificate if it does not exist. The script can be used to automate the driver building and signing process. | Rust/Makefile.toml |
| Cargo.toml    | The provided code snippet is a configuration file for a Rust package called "AltCall". It specifies the package name, version, and dependencies, including ones for printing to the kernel, memory allocation, and obfuscation. The package also includes a build script that utilizes Windows API and requires the winreg and failure dependencies. The package is compiled as a dynamic library.                                     | Rust/Cargo.toml    |
| rustfmt.toml  | The provided code snippet sets various configuration options for formatting Rust code using the Rustfmt tool. These options include the preferred brace style, color usage, function argument layout, and various other formatting preferences. The configuration aims to maintain a maximum line width of 120 characters and includes options for merging imports, reordering items, and using shorthand syntax where possible.       | Rust/rustfmt.toml  |
| build.rs      | The code snippet provides functions for finding the path to the Windows Kits directory and kernel mode libraries. It then determines the architecture of the machine and specifies the search path for linking native Rust code. The main function determines whether to perform extra link search or internal link search based on the presence of a specific Cargo feature.                                                          | Rust/build.rs      |

</details>

<details closed><summary>Src</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                                                                                                                  | Module              |
|:-----------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------|
| externs.rs | The code snippet provides a list of external functions available through the Windows Driver Model and Native API. These functions include creating and manipulating devices, suspending and resuming processes, creating and writing to files, and referencing and dereferencing objects. The functions are declared with their respective parameters and return values.                                 | Rust/src/externs.rs |
| log.rs     | This code snippet provides a macro called "log" that allows for printing debug messages using the Windows Driver Model (WDM) DbgPrint function. The macro can take in a single string argument or multiple arguments using Rust's variadic syntax. The messages are formatted with a prefix of "[>]" and null-terminated before being passed to the DbgPrint function.                                   | Rust/src/log.rs     |
| lib.rs     | This code is a Windows kernel-mode driver that creates a named pipe and allows processes to be added or removed from a list. It contains functions to initialize, add and remove processes, and a device dispatch function to handle IOCTL requests. The driver also registers a custom system call handler to write data to the named pipe using an assembly block.                                     | Rust/src/lib.rs     |
| string.rs  | The code defines a function that takes a slice of u16 values and returns a UNICODE_STRING struct. The function calculates the length of the slice, determines the actual length based on whether the last value is a null terminator, and then populates the struct with the length, maximum length, and buffer pointer. The resulting struct can be used to represent a Unicode string in WinAPI calls. | Rust/src/string.rs  |
| defines.rs | The code snippet defines custom structs and constants that are used in Windows kernel programming. These include structures for process and thread identification, access masks, trap frames, and custom headers. The code also includes unions for the trap frame structure and a total packet structure that combines a custom header and a trap frame.                                                | Rust/src/defines.rs |

</details>

<hr />

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> `[📌  INSERT-PROJECT-PREREQUISITES]`

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

### 🤖 Using CallMon

```sh
cargo run
```

### 🧪 Running Tests
```sh
# [INSERT-COMMAND-FOR-TESTS]
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

