<div align="left">
<h1><img src=https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg width="100" />
<br>CALLMON</h1>
<h3>◦ Empowering Developers, One Repository at a Time</h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="left">
<img src="https://img.shields.io/badge/C-A8B9CC.svg?style=plastic&logo=C&logoColor=black" alt="C" />
<img src="https://img.shields.io/badge/Rust-000000.svg?style=plastic&logo=Rust&logoColor=white" alt="Rust" />
</p>
<img src="https://img.shields.io/github/license/DownWithUp/CallMon?style=plastic&color=5D6D7E" alt="GitHub license" />
<img src="https://img.shields.io/github/last-commit/DownWithUp/CallMon?style=plastic&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/DownWithUp/CallMon?style=plastic&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/languages/top/DownWithUp/CallMon?style=plastic&color=5D6D7E" alt="GitHub top language" />
</div>
<hr>

##  Quick Links
- [🔗 Quick Links](#-quick-links)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [🧩 Modules](#modules)
- [🚀 Getting Started](#-getting-started)
    - [⚙️ Installation](#-installation)
    - [🤖 Running CallMon](#-running-CallMon)
    - [🧪 Tests](#-tests)
- [🚧 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---

##  Overview

The code repository contains a project called CallMon, which is a comprehensive system for process management and monitoring. It includes three major components: 1. The Driver component, responsible for implementing a driver that handles process management operations, such as adding and removing processes, suspending and resuming processes, and handling device control requests.2. The GUI component, which provides a graphical user interface for the CallMon application. It handles functionality such as initializing the main form, handling user events, and displaying data in a ListView control.3. The Rust component, which includes Rust implementations for various functionalities. It consists of modules such as `log.rs` for debugging, `lib.rs` for driver initialization and device control request handling, and `externs.rs` for declaring external functions related to Windows kernel mode operations.Overall, the CallMon project offers a powerful solution for process

---

##  Features

|    | Feature            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The repository consists of three main components: the `Driver` component responsible for process management and handling device control requests, the `GUI` component handling the graphical user interface of the application, and the `Rust` component containing the implementation of the Rust driver. The architecture follows a modular design where each component has its own set of files and responsibilities. Communication between the components likely happens through function calls and shared data structures.                                                                                                                                                                                                                                                                                      |
| 📄 | **Documentation**  | The repository lacks comprehensive documentation. However, the codebase includes inline comments in some files (`Utils.h`, `log.rs`, etc.) providing explanations about the functionality of certain parts. The lack of explicit documentation could make it difficult for new contributors or maintainers to understand and modify the codebase effectively. Improving the documentation by adding high-level explanations, code comments, and usage examples would greatly enhance the maintainability and ease of adoption of the codebase.                                                                                                                                                                                                                                           |
| 🔗 | **Dependencies**   | The system relies on several external dependencies and software components: 1. The `Driver` component depends on the Windows API for process management and handling device control requests. 2. The `Rust` component utilizes the Rust programming language and its package manager, Cargo, for managing dependencies and building the driver. It also uses the rustfmt tool for code formatting. 3. The `GUI` component uses the Windows API and additional resources for GUI development, such as the Resource.rc and resource.h files for defining UI elements. 4. The overall system may depend on other system-level libraries and utilities that are not explicitly mentioned in the repository information. |
| 🧩 | **Modularity**     | The system demonstrates modularity through its organization into separate components (`Driver`, `GUI`, `Rust`) and their corresponding files. Each component contains files responsible for specific functionalities. For example, the `Driver` component has separate files, `AltCall.c` and `Extras.h`, for process management and struct definitions. The `GUI` component has files for main GUI functionality. The `Rust` component contains files like `lib.rs`, `externs.rs`, and `log.rs` for Rust driver implementation and supporting functionality. Modularity facilitates code organization, extensibility, and easier maintenance by isolating different concerns in separate modules.                                                |
| 🧪 | **Testing**        | The information provided does not explicitly mention the testing strategies and tools used in the repository. Testing practices play a crucial role in ensuring the reliability and stability of software. Adding unit tests, integration tests, and considering the use of testing frameworks like `cargo test` for the Rust component and testing frameworks for GUI testing, will help verify the correctness and robustness of the codebase. Additionally, incorporating continuous integration and deployment pipelines can automate the testing process, providing faster feedback on code changes and reducing the likelihood of introducing new issues.                                     |
| ⚡️  | **Performance**    | The information provided does not offer specific details regarding the performance characteristics of the system. Assessing the performance requires evaluating factors like speed, efficiency, and resource usage. To gauge performance, you could analyze the driver implementation in Rust, considering its interaction

---

##  Repository Structure

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


##  Modules

<details closed><summary>Driver</summary>

| File                                                                          | Summary                                                                                                                                                                                                                                                                                                                       |
| ---                                                                           | ---                                                                                                                                                                                                                                                                                                                           |
| [AltCall.c](https://github.com/DownWithUp/CallMon/blob/main/Driver/AltCall.c) | The code in the Driver/AltCall.c file is responsible for the implementation of a driver that performs various operations related to process management, including adding and removing processes, suspending and resuming processes, and handling device control requests.                                                     |
| [Extras.h](https://github.com/DownWithUp/CallMon/blob/main/Driver/Extras.h)   | The code snippet in the file Extras.h defines two struct types: CUSTOM_HEADER and TOTAL_PACKET. The CUSTOM_HEADER struct contains two members: ProcessId of type ULONG64 and StackData of type ULONG64 array. The TOTAL_PACKET struct contains two members: CustomHeader of type CUSTOM_HEADER and Frame of type KTRAP_FRAME. |

</details>

<details closed><summary>Rust</summary>

| File                                                                                | Summary                                                                                                                                                                                                                                                          |
| ---                                                                                 | ---                                                                                                                                                                                                                                                              |
| [Makefile.toml](https://github.com/DownWithUp/CallMon/blob/main/Rust/Makefile.toml) | This code snippet defines tasks for building, renaming, and signing the driver file in the Rust component of the parent repository.                                                                                                                              |
| [Cargo.toml](https://github.com/DownWithUp/CallMon/blob/main/Rust/Cargo.toml)       | This code snippet is responsible for managing the dependencies and build configuration for the AltCall package in the Rust component of the repository.                                                                                                          |
| [rustfmt.toml](https://github.com/DownWithUp/CallMon/blob/main/Rust/rustfmt.toml)   | The code snippet in rustfmt.toml file sets various formatting rules for Rust code, such as the preferred brace style, function arguments layout, maximum line width, and more. These rules ensure consistent and readable code formatting within the repository. |
| [build.rs](https://github.com/DownWithUp/CallMon/blob/main/Rust/build.rs)           | This code snippet in `Rust/build.rs` generates the path to the Windows Kits directory and the kernel mode libraries directory. It determines the architecture and adds the library directory to the Rust linker.                                                 |

</details>

<details closed><summary>Rust/.cargo</summary>

| File                                                                         | Summary                                                                                                                                                                                                 |
| ---                                                                          | ---                                                                                                                                                                                                     |
| [config](https://github.com/DownWithUp/CallMon/blob/main/Rust/.cargo/config) | The code snippet configures build settings for a Rust project in the specified repository to target the x86_64-pc-windows-msvc platform and includes pre and post-link arguments for the build process. |

</details>

<details closed><summary>Rust/src</summary>

| File                                                                              | Summary                                                                                                                                                                                                                                                                                                  |
| ---                                                                               | ---                                                                                                                                                                                                                                                                                                      |
| [externs.rs](https://github.com/DownWithUp/CallMon/blob/main/Rust/src/externs.rs) | The provided code snippet in the file `Rust/src/externs.rs` contains external function declarations for various Windows kernel mode operations such as creating devices, symbolically linking devices, suspending/resuming processes, file operations, memory operations, and process operations.        |
| [log.rs](https://github.com/DownWithUp/CallMon/blob/main/Rust/src/log.rs)         | The code snippet in Rust/src/log.rs provides a logging functionality that allows developers to print debug messages using the DbgPrint function. It includes a macro called log! that can take a string or string with formatting arguments to be printed as a debug message.                            |
| [lib.rs](https://github.com/DownWithUp/CallMon/blob/main/Rust/src/lib.rs)         | The code snippet defines the functionality for a Rust driver in the `src/lib.rs` file. It includes functions for driver initialization, handling device control requests, managing processes, and writing data to a named pipe. The code also sets up a register for an alternative system call handler. |
| [string.rs](https://github.com/DownWithUp/CallMon/blob/main/Rust/src/string.rs)   | The code snippet in Rust's `string.rs` file defines a function that creates a Unicode string from an array of 16-bit unsigned integers (UTF-16 characters). It returns a structure (`UNICODE_STRING`) containing the length, maximum length, and a pointer to the buffer of characters.                  |
| [defines.rs](https://github.com/DownWithUp/CallMon/blob/main/Rust/src/defines.rs) | The code in the defines.rs file defines custom structs, types, and constants related to Windows API calls and kernel-mode programming. It also includes a struct that encapsulates information related to trap frames and packets.                                                                       |

</details>

<details closed><summary>GUI</summary>

| File                                                                           | Summary                                                                                                                                                                                                                                                         |
| ---                                                                            | ---                                                                                                                                                                                                                                                             |
| [Utils.h](https://github.com/DownWithUp/CallMon/blob/main/GUI/Utils.h)         | The code snippet contains declarations for data structures and functions related to the GUI module of the repository. It includes definitions for window dimensions, global handles, and functions for creating a pipe, adding a process, and loading a driver. |
| [Resource.rc](https://github.com/DownWithUp/CallMon/blob/main/GUI/Resource.rc) | The code snippet represents the resource script for the GUI of the CallMon application. It defines the layout and configuration of the main dialog window.                                                                                                      |
| [resource.h](https://github.com/DownWithUp/CallMon/blob/main/GUI/resource.h)   | This code snippet in the repository's GUI/resource.h file defines the IDs and default values for various UI elements in a Windows application, including buttons, edit boxes, list boxes, and labels.                                                           |
| [CallMon.c](https://github.com/DownWithUp/CallMon/blob/main/GUI/CallMon.c)     | This code snippet handles the GUI functionality of the CallMon application. It initializes the main form, handles user events such as button clicks and window sizing, and displays data in a ListView control.                                                 |

</details>

---

##  Getting Started

***Prerequisites***

Ensure you have the following dependencies installed on your system:

- `► INSERT-DEPENDENCY-1`
- `► INSERT-DEPENDENCY-2`
- `► INSERT-DEPENDENCY-3`

###  Installation

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

###  Running CallMon

```sh
cargo run
```

###  Tests
```sh
cargo test
```

---


##  Project Roadmap

> - [X] `ℹ️  Task 1: Implement X`
> - [ ] `ℹ️  Task 2: Implement Y`
> - [ ] `ℹ️ ...`


---

##  Contributing

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

##  License


This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#Top)

---
