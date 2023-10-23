<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>CALLMON</h1>
<h3>◦ Streamline call monitoring for flawless efficiency.</h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/C-A8B9CC.svg?style=for-the-badge&logo=C&logoColor=black" alt="C" />
<img src="https://img.shields.io/badge/Rust-000000.svg?style=for-the-badge&logo=Rust&logoColor=white" alt="Rust" />
</p>
<img src="https://img.shields.io/github/license/DownWithUp/CallMon?style=for-the-badge&color=5D6D7E" alt="GitHub license" />
<img src="https://img.shields.io/github/last-commit/DownWithUp/CallMon?style=for-the-badge&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/DownWithUp/CallMon?style=for-the-badge&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/languages/top/DownWithUp/CallMon?style=for-the-badge&color=5D6D7E" alt="GitHub top language" />
</div>

---

## 📖 Table of Contents
- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 repository Structure](#-repository-structure)
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

The repository "CallMon" contains code for a Windows driver that enables monitoring and manipulation of system calls. It provides functionality for adding and removing processes, suspending and resuming processes, and handling system calls. The code includes a graphical user interface (GUI) for easy interaction with the driver. The driver supports various IOCTLs (Input/Output Control Codes) for managing processes and intercepting system calls. Overall, this project offers a valuable tool for understanding and controlling system behavior in Windows.

---

## 📦 Features

|    | Feature            | Description                                                                                                        |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The codebase follows a modular architecture with separate components for the driver, GUI, and Rust code. The driver component handles system call monitoring and manipulation, while the GUI component provides a graphical interface for interacting with the driver. The Rust code component is responsible for building the driver using Cargo and includes various build tasks and configuration files. Overall, the codebase demonstrates a layered architecture with clear separation of concerns.|
| 📄 | **Documentation**  | The repository lacks comprehensive documentation. While some code files have brief comments, there isn't an overarching documentation explaining the architecture, design patterns, or module interactions. This makes it challenging for newcomers to understand the project. A comprehensive README file or inline comments explaining the overall structure and guiding principles would greatly improve the documentation.|
| 🔗 | **Dependencies**   | The system relies on various dependencies such as "rust", "winapi", "c", and others. These dependencies are crucial for interacting with the Windows operating system, accessing low-level functionality, and building the driver. The repository utilizes the Rust package manager Cargo.toml to manage and resolve these dependencies. It's essential to keep these dependencies up to date to ensure compatibility and security.|
| 🧩 | **Modularity**     | The codebase is organized into smaller, interchangeable components. The directory tree consists of three main components: "Driver", "GUI", and "Rust". Each component encapsulates related functionality and follows the Single Responsibility Principle. The driver component handles system call monitoring, the GUI component provides the graphical interface, and the Rust component manages the building and configuration of the driver. This modular design allows for easier development, maintenance, and testing of individual components.|
| 🧪 | **Testing**        | No information is provided about the system's testing strategies or tools. It's essential to incorporate testing methodologies like unit testing, integration testing, and possibly end-to-end testing to ensure robustness and reliability. Testing frameworks like `rust-test`, `winapi-test`, or `cargo-test` can be utilized for automated testing. Adding tests would enhance the codebase's quality and facilitate bug detection and resolution.|
| ⚡️  | **Performance**    | The performance of the system depends on multiple factors such as the efficiency of the system call hooking mechanism, memory management, and I/O operations. Without detailed performance analysis, it's challenging to provide a comprehensive evaluation. However, since the system operates at a low level, it has the potential to impact overall system performance. Performance optimizations like minimizing unnecessary system calls, memory optimizations, and efficient I/O handling would lead to better performance.|
| 🔐 | **Security**       | The system's security measures are not explicitly mentioned in the repository. When handling low-level operations and interacting with the Windows operating system, it is essential to ensure data security and maintain system integrity. Measures such as input validation, secure memory operations, and privilege management need to be properly implemented. Additionally, ensuring that the project incorporates security best practices and avoids potential vulnerabilities is crucial.|
| 🔀 | **Version Control**| The repository uses Git as the version control system, which allows for effective collaboration, code versioning, and tracking changes. However, no specific version control strategies or tools are described in the repository. Employing practices such as branching,

---


## 📂 Repository Structure

```sh
└── CallMon/
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

| File                                                                          | Summary                                                                                                                                                                                                                                                                                                                    |
| ---                                                                           | ---                                                                                                                                                                                                                                                                                                                        |
| [AltCall.c](https://github.com/DownWithUp/CallMon/blob/main/Driver/AltCall.c) | The code represents a driver that allows monitoring and manipulation of system calls in Windows. The driver provides functionality for adding and removing processes, suspending and resuming processes, and handling system calls. It also includes device dispatch functions for handling input/output control requests. |
| [Extras.h](https://github.com/DownWithUp/CallMon/blob/main/Driver/Extras.h)   | The code defines two structures: `CUSTOM_HEADER` and `TOTAL_PACKET`. The `CUSTOM_HEADER` structure contains an unsigned long long integer `ProcessId` and an array `StackData` of 16 unsigned long long integers. The `TOTAL_PACKET` structure contains a `CUSTOM_HEADER` and a `KTRAP_FRAME` structure.                   |

</details>

<details closed><summary>Rust</summary>

| File                                                                                | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---                                                                                 | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Makefile.toml](https://github.com/DownWithUp/CallMon/blob/main/Rust/Makefile.toml) | This code defines various build tasks for a driver written in Rust. It includes tasks to build the driver in both development and production environments. It also includes tasks to rename the built driver file and sign it using a self-signed certificate. The signing task includes loading the Visual Studio Developer environment, creating a self-signed certificate (if not already created), and signing the driver file using signtool.                                                                                                                                                                                                     |
| [Cargo.toml](https://github.com/DownWithUp/CallMon/blob/main/Rust/Cargo.toml)       | The code represents a directory tree containing different components. The "AltCall" project in the "Rust" directory has a Cargo.toml file that defines the project's name, version, and dependencies. It also specifies the path to the source code and the crate type. The dependencies include "kernel-print," "kernel-alloc," and "obfstr" libraries. Additionally, the "winapi" dependency is specified with specific features and a custom branch. The project also has build dependencies on "winreg" and "failure" libraries.                                                                                                                   |
| [rustfmt.toml](https://github.com/DownWithUp/CallMon/blob/main/Rust/rustfmt.toml)   | The code is a configuration file (rustfmt.toml) that defines the formatting rules for Rust code. It specifies various preferences such as the style of braces, colors, layout of function arguments, handling of code in documentation comments, and more. The aim is to ensure consistent and readable code by specifying how the code should be formatted.                                                                                                                                                                                                                                                                                           |
| [build.rs](https://github.com/DownWithUp/CallMon/blob/main/Rust/build.rs)           | The code in the "build.rs" file of the "Rust" directory is responsible for finding the path to the Windows Kits directory and the kernel mode libraries. It uses the Windows registry to retrieve the Windows Kits directory path and then searches for the kernel mode libraries within that directory. Once the libraries are found, the code determines the target architecture and sets the library directory accordingly. Finally, it prints the library path to be used by the Rust build system. If a specific feature is enabled, the code executes extra link search functionality, otherwise it executes internal link search functionality. |

</details>

<details closed><summary>.cargo</summary>

| File                                                                         | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---                                                                          | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [config](https://github.com/DownWithUp/CallMon/blob/main/Rust/.cargo/config) | The code above is a configuration file for Rust's Cargo build system. It specifies various pre and post-link arguments for the compilation process, targeting the "x86_64-pc-windows-msvc" platform. These arguments include settings for the panic behavior, linker flags, and subsystem options for creating a native Windows driver. The configuration aims to optimize the resulting binary by reducing its size and improving performance through various optimizations and integrity checks. |

</details>

<details closed><summary>Src</summary>

| File                                                                              | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---                                                                               | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [externs.rs](https://github.com/DownWithUp/CallMon/blob/main/Rust/src/externs.rs) | The code in `externs.rs` defines various external functions used in the Rust project. These functions are imported from the Windows Driver Model (WDM) and Windows API. The functions include operations such as creating and manipulating devices, creating symbolic links, suspending and resuming processes, creating and writing to files, and other memory and process-related operations. These functions are essential for interacting with the underlying operating system and performing low-level tasks in the Rust project.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [log.rs](https://github.com/DownWithUp/CallMon/blob/main/Rust/src/log.rs)         | The code in log.rs provides a logging functionality for the Rust project. It includes a macro called "log" that takes a string parameter and uses the winapi library to print a formatted log message. The macro accepts additional parameters for formatting the log message. This functionality is useful for debugging and monitoring the Rust project.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [lib.rs](https://github.com/DownWithUp/CallMon/blob/main/Rust/src/lib.rs)         | The provided code is a Rust driver for the Windows operating system. It implements a device driver that creates and manages a device named "CallMon". The driver provides several functionalities:-The driver's entry point, `DriverEntry`, initializes the driver and creates a device object for communication.-The driver's unload function, `DriverUnloadFunction`, is called when the driver is unloaded from memory.-The driver's device dispatch function, `DeviceDispatch`, handles various IOCTLs (Input/Output Control Code) sent to the device, such as adding a process, removing a process, and initializing the driver.-The `MyHandler` function is a callback for a system call hook.-The `AddProcess` and `RemoveProcess` functions add and remove processes, respectively.-The `PreformInit` function performs initialization tasks, such as creating or closing a named pipe.-The `panic` function is a panic handler that causes an infinite loop when a panic occurs.Overall, this code implements a driver that provides functionality related to process management and system call interception. |
| [string.rs](https://github.com/DownWithUp/CallMon/blob/main/Rust/src/string.rs)   | The code in Rust/src/string.rs contains a function called create_unicode_string that creates a UNICODE_STRING object. This function takes an input string as a slice of 16-bit unsigned integers and returns the created UNICODE_STRING object. The function calculates the length of the string, determines the actual length without the null terminator, and then initializes the fields of the UNICODE_STRING struct with the calculated values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [defines.rs](https://github.com/DownWithUp/CallMon/blob/main/Rust/src/defines.rs) | The code in "defines.rs" file defines custom structs, types, and constants that are used in the Windows kernel mode. It includes definitions for handles, processor mode, access masks, IOCTL codes, and various data structures like KTRAP_FRAME. These definitions are used for handling system calls, exceptions, and other low-level operations in the Windows kernel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

</details>

<details closed><summary>Gui</summary>

| File                                                                           | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ---                                                                            | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Utils.h](https://github.com/DownWithUp/CallMon/blob/main/GUI/Utils.h)         | The code is a header file containing necessary headers and definitions for the graphical user interface (GUI) of the CallMon application. It includes functions for creating a pipe for inter-process communication, obtaining device handles and privileges, loading a driver, and adding a process to monitor. It also defines structures for storing and manipulating data related to trap frames and custom headers. Additionally, it includes a function for inserting a column into a list view control. |
| [Resource.rc](https://github.com/DownWithUp/CallMon/blob/main/GUI/Resource.rc) | The code is a resource script written in C++ for a Microsoft Visual C++ application. It defines the GUI layout and configuration for a program called "CallMon". The script includes a dialog box with various controls such as buttons, text boxes, and a list view. Users can interact with the controls to initialize the program, add or remove processes, clear data, and view stack captures. The script also includes language and design information.                                                  |
| [resource.h](https://github.com/DownWithUp/CallMon/blob/main/GUI/resource.h)   | The code provided is a resource file for a GUI application. It includes various definitions and IDs for dialog controls such as buttons, edit boxes, lists, and labels. The resource file is used to generate the user interface of the application.                                                                                                                                                                                                                                                           |
| [CallMon.c](https://github.com/DownWithUp/CallMon/blob/main/GUI/CallMon.c)     | HTTPStatus Exception: 400                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

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

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/DownWithUp/CallMon/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/DownWithUp/CallMon/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/DownWithUp/CallMon/issues)**: Submit bugs found or log feature requests for DOWNWITHUP.

#### *Contributing Guidelines*

<details closed>
<summary>Click to expand</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone <your-forked-repo-url>
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear and concise message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

## 📄 License


This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 👏 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#Top)

---
