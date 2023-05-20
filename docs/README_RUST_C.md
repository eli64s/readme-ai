
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
CallMon
</h1>
<h3 align="center">📍 Empowering developers everywhere - with CallMon!</h3>
<h3 align="center">🚀 Developed with the software and tools below.</h3>
<p align="center">

<img src="https://img.shields.io/badge/C-A8B9CC.svg?style=for-the-badge&logo=C&logoColor=black" alt="" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="rc" />
<img src="https://img.shields.io/badge/Rust-000000.svg?style=for-the-badge&logo=Rust&logoColor=white" alt="c" />
</p>

</div>

---

## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍Overview](#-introdcution)
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

CallMon is a powerful GitHub project that enables developers to easily monitor their services for unhandled exception and application errors. It also provides detailed error analytics and automated notification of errors via email, Slack, or webhooks so developers can react quickly to any outages.

## 🔮 Feautres

> `[📌  INSERT-PROJECT-FEATURES]`

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

| File   | Summary                                                                                                                                      | Module             |
|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
| config | This code builds a Rust program for the x86_64- pc- windows- msvc target with various pre- and post- link arguments to optimize the program. | Rust/.cargo/config |

</details>

<details closed><summary>Driver</summary>

| File      | Summary                                                                                                                                                                                                                                                                                                                                                                  | Module           |
|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| AltCall.c | This code is a Windows kernel driver that implements a system call hooking mechanism. It includes functions to add and remove processes from the hooking mechanism, as well as an initialization function to set up a named pipe for communication. It also includes a handler function that is called when a system call is made, which reads the stack data and writes | Driver/AltCall.c |
| Extras.h  | This code defines two structures, CUSTOM_HEADER and TOTAL_PACKET. CUSTOM_HEADER contains a ProcessId and an array of StackData, while TOTAL_PACKET contains a CUSTOM_HEADER and a KTRAP_FRAME.                                                                                                                                                                           | Driver/Extras.h  |

</details>

<details closed><summary>Gui</summary>

| File        | Summary                                                                                                                                                                                                                                                                                                                                    | Module          |
|:------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------|
| Utils.h     | This code is taken from a GUI program for Windows called WinObjEx64. It contains global variables, functions, and structures related to the program. The functions include obtaining a device, creating a pipe, adding a process, getting driver privileges, loading a driver, and inserting a column. The structures include STACK_CHUNK, | GUI/Utils.h     |
| Resource.rc | This code is a Microsoft Visual C++ generated resource script that includes a dialog box with various controls such as push buttons, edit texts, and list views. It also includes a text include resource and a design info resource. It is used to create a dialog box for the " CallMon " application.                                   | GUI/Resource.rc |
| resource.h  | This code defines the resources for a dialog box, including buttons, text boxes, and labels. It also defines the next default values for new objects.                                                                                                                                                                                      | GUI/resource.h  |
| CallMon.c   | Error fetching summary.                                                                                                                                                                                                                                                                                                                    | GUI/CallMon.c   |

</details>

<details closed><summary>Rust</summary>

| File     | Summary                                                                                                                                                                             | Module        |
|:---------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------|
| build.rs | This code searches for the path to the kernel mode libraries in the Windows Kits directory and sets the native link search to the library directory for the specified architecture. | Rust/build.rs |

</details>

<details closed><summary>Src</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                                                        | Module              |
|:-----------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------|
| externs.rs | This code imports various Windows API functions related to driver and process management, such as IoCreateDevice, ZwCreateFile, and PsSuspendProcess. It also imports functions related to memory management, such as ProbeForRead and memmove. Finally, it imports functions related to object handles, such as ObReferenceObjectByHandle and | Rust/src/externs.rs |
| log.rs     | This code creates a macro called " log " which allows for printing of strings to the Windows Debugger. It uses the winapi::km::wdm::DbgPrint function to do this.                                                                                                                                                                              | Rust/src/log.rs     |
| lib.rs     | This code is a driver for the Windows operating system written in Rust. It provides functions to add and remove processes, as well as an initialization function. It also contains a panic handler and a global allocator. It also contains a function to handle device control requests, which can be used to perform various operations.     | Rust/src/lib.rs     |
| string.rs  | This code creates a UNICODE_STRING from a slice of u16 values. It takes into account the possibility of a null- terminated string, and sets the Length and MaximumLength fields accordingly.                                                                                                                                                   | Rust/src/string.rs  |
| defines.rs | This code defines custom structs, unions, and constants related to the Windows API. It includes structs such as _ CLIENT_ID, _ OBJECT_HANDLE_INFORMATION, _ CUSTOM_HEADER, and _ KTRAP_FRAME, unions such as u1, u2, and u                                                                                                                     | Rust/src/defines.rs |

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
#run tests
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
