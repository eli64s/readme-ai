<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>CALLMON</h1>
<h3>◦ Monitor your calls, boost your performance!</h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/C-A8B9CC.svg?style=plastic&logo=C&logoColor=black" alt="C" />
<img src="https://img.shields.io/badge/Rust-000000.svg?style=plastic&logo=Rust&logoColor=white" alt="Rust" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=plastic&logo=Markdown&logoColor=white" alt="Markdown" />
</p>
<img src="https://img.shields.io/github/license/DownWithUp/CallMon?style=plastic&color=5D6D7E" alt="GitHub license" />
<img src="https://img.shields.io/github/last-commit/DownWithUp/CallMon?style=plastic&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/DownWithUp/CallMon?style=plastic&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/languages/top/DownWithUp/CallMon?style=plastic&color=5D6D7E" alt="GitHub top language" />
</div>

---

## 📖 Table of Contents
- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [⚙️ Modules](#️-modules)
- [🚀 Getting Started](#-getting-started)
  - [🔧 Installation](#-installation)
  - [🤖 Running CallMon](#-running-callmon)
  - [🧪 Tests](#-tests)
- [🛣 Project Roadmap](#-project-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The CallMon repository is a project that consists of a device driver and a GUI application. The driver creates a device named "CallMon" and supports various IOCTLs for monitoring processes and initializing a named pipe for communication with the GUI. The driver uses Windows NT kernel functions for process suspension, resume, and system call registration. The GUI application interfaces with the driver and provides functionality such as adding processes, obtaining driver privilege, and loading the driver. Overall, the project allows for monitoring and managing processes through a driver and GUI application.

---

## 📦 Features

|    | Feature            | Description                                                                                                        |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The codebase follows a modular architecture with separate directories for GUI, Driver, and Rust components. It leverages the Windows Driver Model (WDM) and uses a named pipe for communication between the GUI and driver components. The Rust code acts as a bridge between the GUI and the driver, providing an alternate system call handler. |
| 📄 | **Documentation**  | The codebase lacks comprehensive documentation. Some code files have brief comments, but overall the documentation is insufficient.                                 |
| 🔗 | **Dependencies**   | The codebase relies on external libraries like `winapi` for Windows kernel mode programming and `toml` for parsing TOML files. There are also dependencies on the Windows API.                                |
| 🧩 | **Modularity**     | The codebase exhibits modularity with separate components for GUI, driver, and Rust code. Each component has its own directory and set of files, promoting encapsulation and separation of concerns.              |
| 🧪 | **Testing**        | The codebase does not have explicit testing strategies or tools defined. There is no testing code or test directories present.                                              |
| ⚡️  | **Performance**    | The codebase does not have any performance optimizations explicitly mentioned. Evaluation of performance aspects would require analyzing specific code implementations.    |
| 🔐 | **Security**       | The codebase does not contain explicit security measures. Considering it is a driver-based application, security concerns should be addressed, such as access control and validation of user inputs.                                 |
| 🔀 | **Version Control**| No information is available about the version control strategies or tools used for this codebase.                                                            |
| 🔌 | **Integrations**   | The codebase interacts with other systems through the Windows API and relies on the `winapi` library for kernel mode programming. It also integrates with the GUI component using a named pipe.                                                                                                                                |
| 📶 | **Scalability**    | The codebase does not have explicit scalability considerations. Scaling the system would require analyzing specific code implementations and the ability to handle a growing number of monitored processes.                                           |

---


## 📂 Repository Structure

```sh
└── ./
    ├── Driver/
    │   ├── AltCall.c
    │   └── Extras.h
    ├── GUI/
    │   ├── CallMon.c
    │   ├── Resource.rc
    │   ├── Utils.h
    │   └── resource.h
    └── Rust/
        ├── .cargo/
        │   └── config
        ├── Cargo.toml
        ├── Makefile.toml
        ├── build.rs
        ├── rustfmt.toml
        └── src/
            ├── defines.rs
            ├── externs.rs
            ├── lib.rs
            ├── log.rs
            └── string.rs

```

---


## ⚙️ Modules

<details closed><summary>Driver</summary>

| File                                                                          | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---                                                                           | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [AltCall.c](https://github.com/DownWithUp/CallMon/blob/main/Driver/AltCall.c) | The code is a device driver that creates a device named "CallMon". It supports three IOCTLs:-IOCTL_ADD_PROCESS: adds a process to the list of monitored processes.-IOCTL_REMOVE_PROCESS: removes a process from the list of monitored processes.-IOCTL_INIT: initializes a named pipe for communication with the user-mode GUI.The driver also provides functions for handling driver entry and unloading. It uses various Windows NT kernel functions for process suspension, resume, and system call registration. |
| [Extras.h](https://github.com/DownWithUp/CallMon/blob/main/Driver/Extras.h)   | The code contains two structs, `CUSTOM_HEADER` and `TOTAL_PACKET`, defined in the `Extras.h` file. The `CUSTOM_HEADER` struct has two fields: `ProcessId` and `StackData`, with the latter being an array of type `ULONG64`. The `TOTAL_PACKET` struct includes the `CUSTOM_HEADER` struct and another struct called `KTRAP_FRAME`, creating a composite data structure. The `KTRAP_FRAME` is not defined in the provided code snippet.                                                                              |

</details>

<details closed><summary>Rust</summary>

| File                                                                                | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---                                                                                 | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Makefile.toml](https://github.com/DownWithUp/CallMon/blob/main/Rust/Makefile.toml) | The given code defines a directory tree structure and a Makefile.toml file in the'Rust' directory. It also contains tasks for building, renaming, and signing a driver file. The'build-driver' task compiles the driver code using Cargo. The'rename' task renames the compiled driver file from'driver.dll' to'driver.sys'. The'sign' task signs the driver file using a self-signed certificate and a timestamp from Digicert.                                                                                                                                                                                                                   |
| [Cargo.toml](https://github.com/DownWithUp/CallMon/blob/main/Rust/Cargo.toml)       | The code represents the directory tree structure of a project called "readmeai". It consists of three main directories: Driver, GUI, and Rust. The Rust directory contains configuration files and source code for a Rust library called "AltCall". The code in Rust/Cargo.toml includes package metadata, library information, dependencies, and build configuration for the AltCall library, including dependencies on other Rust libraries and the Windows API.                                                                                                                                                                                 |
| [rustfmt.toml](https://github.com/DownWithUp/CallMon/blob/main/Rust/rustfmt.toml)   | The code sets formatting rules for Rust code using the rustfmt tool. It specifies various style preferences for code formatting, such as the placement of braces, line lengths, merging imports, reordering items, and using shorthand syntax. These rules aim to improve consistency and readability of the codebase.                                                                                                                                                                                                                                                                                                                             |
| [build.rs](https://github.com/DownWithUp/CallMon/blob/main/Rust/build.rs)           | This code defines functions for retrieving the path to the Windows Kits directory and the kernel mode libraries path. It uses the `winreg` crate to access the Windows registry and retrieve the necessary information. The `get_windows_kits_dir` function returns the path to the Windows Kits directory, while the `get_km_dir` function returns the path to the kernel mode libraries. The `internal_link_search` function uses these paths to set the link directory for the Rust code. The `main` function determines whether to perform an extra link search based on a cargo feature flag, and calls the appropriate function accordingly. |

</details>

<details closed><summary>.cargo</summary>

| File                                                                         | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---                                                                          | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [config](https://github.com/DownWithUp/CallMon/blob/main/Rust/.cargo/config) | The code is a configuration file for the Rust build system in the directory "Rust/.cargo/config". It specifies the target platform as "x86_64-pc-windows-msvc" and sets various compile and link flags for building a Windows driver. The compile flags include disabling certain default libraries, specifying the subsystem as "native" and "driver", enabling ASLR, and disabling certain features like the manifest and PDBALT. The link flags include optimization options, specifying the entry point as "DriverEntry", merging sections, and enabling integrity checking. |

</details>

<details closed><summary>Src</summary>

| File                                                                              | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---                                                                               | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [externs.rs](https://github.com/DownWithUp/CallMon/blob/main/Rust/src/externs.rs) | The code in `externs.rs` declares a set of external functions using the `winapi` crate for Windows kernel mode programming. These functions include operations like creating devices and symbolic links, completing I/O requests, suspending and resuming processes, creating and writing to files, and working with process handles and objects. The code also includes some utility functions for memory manipulation and retrieving process IDs.                          |
| [log.rs](https://github.com/DownWithUp/CallMon/blob/main/Rust/src/log.rs)         | The code in the "log.rs" file is a logging module written in Rust. It provides a macro called "log!" that allows logging messages using the "DbgPrint" function from the Windows Driver Model (WDM) API. The macro accepts a string expression and optional additional arguments, which are formatted and passed to the "DbgPrint" function for logging.                                                                                                                     |
| [lib.rs](https://github.com/DownWithUp/CallMon/blob/main/Rust/src/lib.rs)         | The code defines a Rust driver that creates a device and handles device control operations. It initializes and communicates with a named pipe, suspends/resumes processes, and registers an alternate system call handler. Certain IOCTL operations allow adding/removing processes from a list and initializing the driver. The driver entry point sets up the driver and creates necessary data structures. The driver also includes error handling and cleanup functions. |
| [string.rs](https://github.com/DownWithUp/CallMon/blob/main/Rust/src/string.rs)   | The code in "string.rs" file in the "Rust/src" directory defines a function called "create_unicode_string" which takes a slice of u16 values as an argument. This function creates a UNICODE_STRING struct and initializes its properties based on the length and content of the input slice. The struct represents a Unicode string in Windows API and is used to interact with WinAPI functions that require Unicode strings.                                              |
| [defines.rs](https://github.com/DownWithUp/CallMon/blob/main/Rust/src/defines.rs) | The code defines various constants, types, and structs used in a Rust project. It includes definitions for custom types and structs that are either not available in the winapi crate or require additional functionality. Additionally, it defines unions and structs related to the KTRAP_FRAME structure used in kernel mode programming. Overall, the code provides the necessary foundations for working with Windows drivers and system calls in Rust.                 |

</details>

<details closed><summary>Gui</summary>

| File                                                                           | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---                                                                            | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Utils.h](https://github.com/DownWithUp/CallMon/blob/main/GUI/Utils.h)         | The code provides functionality for a GUI application that interfaces with a driver called "AltCall.sys". It includes functions for creating a named pipe, adding a process to the driver, obtaining driver privilege, and loading the driver. It also includes various data structures and constants used by the driver and GUI application.                                                                                                       |
| [Resource.rc](https://github.com/DownWithUp/CallMon/blob/main/GUI/Resource.rc) | The code is a resource script written in C++ for a Windows GUI application called CallMon. It defines the layout and design of a dialog box named IDD_DIALOG1, which includes various elements such as group boxes, buttons, text fields, and a list view control. The script also includes resource definitions for the English (United States) language. This script is responsible for creating the visual interface of the CallMon application. |
| [resource.h](https://github.com/DownWithUp/CallMon/blob/main/GUI/resource.h)   | The code represents a resource header file for a graphical user interface (GUI). It defines various IDs for controls and resources used in the GUI, such as buttons, edit boxes, lists, and static labels. The code also includes default values for the next resource, command, and control values. Overall, this header file provides the necessary definitions for the GUI components.                                                           |
| [CallMon.c](https://github.com/DownWithUp/CallMon/blob/main/GUI/CallMon.c)     | HTTPStatus Exception: 400                                                                                                                                                                                                                                                                                                                                                                                                                           |

</details>

---

## 🚀 Getting Started

***Dependencies***

Please ensure you have the following dependencies installed on your system:

`- ℹ️ Dependency 1`

`- ℹ️ Dependency 2`

`- ℹ️ ...`

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


## 🛣 Project Roadmap

> - [X] `ℹ️  Task 1: Implement X`
> - [ ] `ℹ️  Task 2: Implement Y`
> - [ ] `ℹ️ ...`


---

## 🤝 Contributing

[**Discussions**](https://github.com/DownWithUp/CallMon/discussions)
  - Join the discussion here.

[**New Issue**](https://github.com/DownWithUp/CallMon/issues)
  - Report a bug or request a feature here.

[**Contributing Guidelines**](https://github.com/DownWithUp/CallMon/blob/main/CONTRIBUTING.md)

- Contributions are welcome! Please follow these steps:

1. Fork the project repository to your GitHub account.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive such as `new-feature-x` or `bugfix-issue-x`.
```sh
git checkout -b new-feature-x
```
4. Develop your changes locally.
5. Commit your updates with a clear explanation of the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub.
```sh
git push origin new-feature-x
```
7. Create a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
8. Once your pull request is reviewed, it will be merged into the main branch of the project repository.

---

## 📄 License


This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 👏 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#Top)

---
