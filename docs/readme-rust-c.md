
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
CallMon
</h1>
<h3 align="center">📍 Track every call with CallMon: Your all-in-one call monitoring solution!</h3>
<h3 align="center">⚙️ Developed with the software and tools below:</h3>

<p align="center">
<img src="https://img.shields.io/badge/C-A8B9CC.svg?style=for-the-badge&logo=C&logoColor=black" alt="C" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="Markdown" />
<img src="https://img.shields.io/badge/Rust-000000.svg?style=for-the-badge&logo=Rust&logoColor=white" alt="Rust" />
</p>
</div>

---

## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [💫 Features](#-features)
- [📂 Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🚀 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

CallMon is a Windows kernel driver and UI application that monitors system calls made by processes. It captures the process ID, stack data, and KTRAP_FRAME pointer and sends it to the user-mode application via a named pipe. The tool provides the ability to add or remove processes from monitoring and displays the monitored calls and their arguments in a user-friendly GUI. Its value proposition lies in its ability to detect malicious processes or behavior by providing insight into system calls made by programs.

---

## 💫 Features

Error generating file summary. Exception: Server error '502 Bad Gateway' for url 'https://api.openai.com/v1/chat/completions'
For more information check: https://httpstatuses.com/502

---


<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

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

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 🧩 Modules

<details closed><summary>.cargo</summary>

| File   | Summary                                                                                                                                                                                                                                                                                                                             | Module             |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
| config | The provided code snippet is a configuration file for building Rust code targeting the x86_64-pc-windows-msvc platform. It specifies various pre and post link arguments, such as disabling logging, setting up the subsystem as a driver, and optimizing the binary by merging sections. It also sets the panic behavior to abort. | Rust/.cargo/config |

</details>

<details closed><summary>Driver</summary>

| File      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Module           |
|:----------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| AltCall.c | The provided code is a Windows kernel-mode driver that registers a custom system call handler and provides functions to add and remove a process from monitoring. It uses IOCTLs to communicate with a user-mode application via a named pipe. When triggered, the custom system call handler captures the stack data of the calling thread and sends it to the user-mode application through the named pipe. The driver also creates a device and symbolic link for user-mode access. | Driver/AltCall.c |
| Extras.h  | The code snippet defines two C structs: CUSTOM_HEADER which contains the process ID and stack data of a process, and TOTAL_PACKET which includes the CUSTOM_HEADER and a KTRAP_FRAME struct. These structs can be used to store and transfer data between different parts of a program.                                                                                                                                                                                                | Driver/Extras.h  |

</details>

<details closed><summary>Gui</summary>

| File        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Module          |
|:------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------|
| Utils.h     | The provided code snippet defines various constants and data structures and includes libraries necessary for interacting with a driver. It also contains functions to obtain the driver, create a pipe, add a process, get driver privilege, and load the driver. Additionally, it includes a helper function to insert a column into a list view.                                                                                                                                                                         | GUI/Utils.h     |
| Resource.rc | The code snippet is a Microsoft Visual C++ generated resource script for a UI application called "CallMon". The script defines the layout, design, and functionality of the application's main dialog window, including configuration options, buttons to initialize, add or remove processes, a list view control to display information, and a stack capture feature.                                                                                                                                                    | GUI/Resource.rc |
| resource.h  | The provided code snippet is a resource file generated by Microsoft Visual C++. It contains definitions for various UI elements like buttons, text boxes, and labels that can be used to create an interactive GUI application. The code also includes default values for new objects.                                                                                                                                                                                                                                     | GUI/resource.h  |
| CallMon.c   | The code snippet contains a GUI application that monitors system calls made by processes. It includes functionality to initialize the monitoring, add or remove processes to monitor, and clear the list of monitored calls. The code uses various Windows libraries and APIs, includes a custom message handler, and uses multi-threading to listen for incoming data. The GUI is designed with a list view control to display the monitored calls and a memo control to display the arguments passed to a selected call. | GUI/CallMon.c   |

</details>

<details closed><summary>Rust</summary>

| File     | Summary                                                                                                                                                                                                                                                                                                                                                                   | Module        |
|:---------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------|
| build.rs | The code snippet contains functions for retrieving the path to the Windows Kits directory, finding the kernel mode libraries within the directory, and specifying search paths for linking during compilation. If a cargo feature for extra link search is enabled, the extra_link_search() function is called; otherwise, the internal_link_search() function is called. | Rust/build.rs |

</details>

<details closed><summary>Src</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Module              |
|:-----------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------|
| externs.rs | The provided code snippet contains a set of external functions from the Windows Driver Model API used for device driver development, process management, and file handling. These functions include creating devices and symbolic links, creating and writing to files, suspending and resuming processes, and obtaining process information. The code also includes memory management and object reference functions.                                                                                         | Rust/src/externs.rs |
| log.rs     | The provided code snippet defines a macro for logging message strings using the `DbgPrint` function from the Windows kernel-mode `winapi` library. The macro accepts a string expression and optionally additional arguments to be formatted into the message string. The logged message is prefixed with "[>]" and terminated with a null character.                                                                                                                                                          | Rust/src/log.rs     |
| lib.rs     | This code is for a Windows kernel driver that sets up a named pipe and handles IOCTL requests to add or remove processes from the driver's monitoring list. When a monitored process makes a system call, a trap handler captures the process ID, stack data, and the KTRAP_FRAME pointer, and writes it to the named pipe. The driver also uses PsRegisterAltSystemCallHandler to replace system call handlers with custom ones, allowing the driver to intercept and log all system calls made by a process. | Rust/src/lib.rs     |
| string.rs  | This code snippet exports a public function called "create_unicode_string" which accepts a slice of u16 integers and returns a UNICODE_STRING structure with Length, MaximumLength, and Buffer fields. It computes the Length and MaximumLength values based on the input slice and assigns the Buffer field to the pointer of the input slice. It is used to create a Unicode string from a u16 buffer.                                                                                                       | Rust/src/string.rs  |
| defines.rs | The provided code snippet contains various custom defines, structs and unions not present in the winapi crate. These include constants for file access, IOCTL codes, and structs such as KTRAP_FRAME and CUSTOM_HEADER. The code also includes a struct for TOTAL_PACKET which contains a CUSTOM_HEADER and KTRAP_FRAME, along with padding to account for differences between C and Rust versions of the struct.                                                                                              | Rust/src/defines.rs |

</details>

---

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - [📌  PREREQUISITE-1]
> - [📌  PREREQUISITE-2]
> - ...

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

> - [X] [📌  Task 1: Implement X]
> - [ ] [📌  Task 2: Refactor Y]
> - [ ] [📌  Task 3: Optimize Z]
> - [ ] ...


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

## 📄 License

This project is licensed under the `[📌  INSERT-LICENSE-TYPE]` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 👏 Acknowledgments

> - [📌  List any resources, contributors, inspiration, etc.]

---
