<p align="center">
  <img src="https://img.icons8.com/pulsar-color/96/markdown.png" width="100" />
</p>
<p align="center">
    <h1 align="center">CALLMON</h1>
</p>
<p align="center">
    <em>Revolutionizing Call Monitoring with CallMon</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/DownWithUp/CallMon?style=flat&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/DownWithUp/CallMon?style=flat&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/DownWithUp/CallMon?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/DownWithUp/CallMon?style=flat&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with the software and tools below</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/C-A8B9CC.svg?style=flat&logo=C&logoColor=black" alt="C">
	<img src="https://img.shields.io/badge/Rust-000000.svg?style=flat&logo=Rust&logoColor=white" alt="Rust">
	<img src="https://img.shields.io/badge/Markdown-000000.svg?style=flat&logo=Markdown&logoColor=white" alt="Markdown">
</p>
<hr>

##  Quick Links
- [ Quick Links](#-quick-links)
- [ Overview](#-overview)
- [ Features](#-features)
- [ Repository Structure](#-repository-structure)
- [ Modules](#modules)
- [ Getting Started](#-getting-started)
    - [ Installation](#-installation)
    - [ Running CallMon](#-running-CallMon)
    - [ Tests](#-tests)
- [ Roadmap](#-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

---

##  Overview

CallMon is a project that provides a way to monitor and intercept system calls in Windows applications. It aims to enhance application security and debugging by allowing developers to track and analyze the interactions between user-mode applications and the operating system kernel. By hooking into the Windows kernel, CallMon captures and logs system call information, providing valuable insights into the behavior of running applications. With the ability to suspend and resume processes, as well as register and remove system call handlers, CallMon enables developers to customize and control the monitoring process according to their specific needs. With its powerful functionality, CallMon offers a flexible and comprehensive solution for system call monitoring and analysis.

---

##  Features

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
```

|    | Feature           | Description                                                                                                       |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**    | The system seems to have a simple monolithic architecture, with a driver component, a GUI component, and a Rust component. |
| 📄 | **Documentation**  | The codebase lacks comprehensive documentation. More comments and explanations would improve understanding. |
| 🔗 | **Dependencies**   | External dependencies are not clearly mentioned in the repository. |
| 🧩 | **Modularity**     | The system does not demonstrate clear modularity. Components are organized by language but lack clear separation of concerns. |
| 🧪 | **Testing**        | There is no explicit mention of testing strategies or tools in the codebase. Testing may not be a focus of this project. |
| ⚡️ | **Performance**     | Performance characteristics are not explicitly discussed in the codebase. Optimization may not be a primary concern. |
| 🔐 | **Security**       | There is no explicit discussion of security measures. The codebase may not have implemented advanced security features.|
| 🔀 | **Version Control**| The codebase uses Git for version control, but there is no explicit discussion of version control strategies or tools.|
| 🔌 | **Integrations**   | There is no explicit discussion of how the system interacts with other systems or services. |
| 📶 | **Scalability**    | The codebase does not provide clear indications of how well it can handle growth or scalability. |

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

| File                                                                          | Summary                                                                                                                                                                                                                                                                                       |
| ---                                                                           | ---                                                                                                                                                                                                                                                                                           |
| [AltCall.c](https://github.com/DownWithUp/CallMon/blob/main/Driver/AltCall.c) | The code snippet is part of a driver in the CallMon repository. It adds and removes processes, handles system call interception, and communicates with a user-mode GUI through IOCTLs. The code implements the driver's entry point, device dispatch, and process manipulation functions.     |
| [Extras.h](https://github.com/DownWithUp/CallMon/blob/main/Driver/Extras.h)   | This code snippet, located in the Driver directory of the repository, defines structures for a custom header and a total packet. These structures are used in conjunction with the Extras.h dependency to facilitate communication and data handling in the driver component of the codebase. |

</details>

<details closed><summary>Rust</summary>

| File                                                                                | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---                                                                                 | ---                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [Makefile.toml](https://github.com/DownWithUp/CallMon/blob/main/Rust/Makefile.toml) | This code snippet is responsible for building, renaming, and signing a driver file in the CallMon repository. The code uses Rust and makefile.toml for dependencies and software. The snippet follows a sequence of tasks to compile the driver, rename it, and sign it with a self-signed certificate.                                                                                                                                      |
| [Cargo.toml](https://github.com/DownWithUp/CallMon/blob/main/Rust/Cargo.toml)       | This code snippet is part of the CallMon repository and resides in the Driver directory. It includes the AltCall.c file and Extras.h header file. The code is written in Rust and relies on various dependencies, such as kernel-print, kernel-alloc, obfstr, and winapi. The purpose of this code is to provide an alternative implementation for making system calls in the CallMon project.                                               |
| [rustfmt.toml](https://github.com/DownWithUp/CallMon/blob/main/Rust/rustfmt.toml)   | This code snippet in the CallMon repository is responsible for defining and handling various functions and structures related to logging and string manipulation in the Rust module. It includes configuration settings for formatting the code in the project according to specific rules. The code achieves efficient handling of log entries and manipulation of strings, enhancing the overall functionality of the CallMon application. |
| [build.rs](https://github.com/DownWithUp/CallMon/blob/main/Rust/build.rs)           | This code snippet is responsible for finding the path to the Windows Kits directory and the kernel mode libraries. It searches for the correct directories based on the target architecture and sets the appropriate link search paths for the Rust build system.                                                                                                                                                                            |

</details>

<details closed><summary>Rust..cargo</summary>

| File                                                                         | Summary                                                                                                                                                                                                                                                                                                |
| ---                                                                          | ---                                                                                                                                                                                                                                                                                                    |
| [config](https://github.com/DownWithUp/CallMon/blob/main/Rust/.cargo/config) | This code snippet is part of the CallMon repository's architecture. It includes a Rust module that builds a Windows driver using specific pre-link and post-link arguments for optimized performance and security. The code achieves efficient driver construction as per the specified configuration. |

</details>

<details closed><summary>Rust.src</summary>

| File                                                                              | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---                                                                               | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [externs.rs](https://github.com/DownWithUp/CallMon/blob/main/Rust/src/externs.rs) | The code snippet in `Rust/src/externs.rs` contains external function declarations and definitions that interface with the Windows Kernel and user mode APIs. These functions are used to create devices, handle file operations, manipulate processes, and perform memory operations. They are critical for the functioning of the CallMon repository's architecture, enabling communication with the underlying operating system and executing key functionalities. |
| [log.rs](https://github.com/DownWithUp/CallMon/blob/main/Rust/src/log.rs)         | The code snippet is part of the CallMon repository and is located in the `Rust/src/log.rs` file. It defines a macro called `log!`, which is used for logging purposes. The macro uses the `DbgPrint` function from the `winapi::km::wdm` dependency to print log messages.                                                                                                                                                                                           |
| [lib.rs](https://github.com/DownWithUp/CallMon/blob/main/Rust/src/lib.rs)         | This code snippet is a key file in the CallMon repository, which has a specific directory structure. It initializes and handles driver operations, including creating and managing a device, processing I/O control requests, and handling system calls.                                                                                                                                                                                                             |
| [string.rs](https://github.com/DownWithUp/CallMon/blob/main/Rust/src/string.rs)   | The code snippet in Rust/src/string.rs provides a function for creating Unicode strings using the winapi library. It takes an array of u16 characters and returns a UNICODE_STRING structure with the length, maximum length, and buffer pointer properly set. This code is a critical part of the CallMon repository, which is organized into directories for the driver, GUI, and Rust components.                                                                 |
| [defines.rs](https://github.com/DownWithUp/CallMon/blob/main/Rust/src/defines.rs) | This code snippet in `defines.rs` provides custom defines, unions, and structures used in the parent repository's architecture. It includes various constants, structs, and type aliases that are necessary for proper functioning and interaction with the Windows operating system.                                                                                                                                                                                |

</details>

<details closed><summary>GUI</summary>

| File                                                                           | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---                                                                            | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Utils.h](https://github.com/DownWithUp/CallMon/blob/main/GUI/Utils.h)         | This code snippet is a part of the CallMon repository. It includes functions and global variables related to driver loading, process management, and GUI creation. It also provides utility functions and data structures necessary for these functionalities.                                                                                                                                                                                                                                                      |
| [Resource.rc](https://github.com/DownWithUp/CallMon/blob/main/GUI/Resource.rc) | The code snippet in the GUI/Resource.rc file is responsible for defining and configuring the graphical user interface (GUI) for the CallMon application. It includes the layout and visual elements of the main dialog window, such as buttons, text fields, and a list view. The resource script is written in Microsoft Visual C++ and uses the winres.h header file. The GUI is designed to allow users to configure the application, initialize it, add and remove processes, and capture and clear stack data. |
| [resource.h](https://github.com/DownWithUp/CallMon/blob/main/GUI/resource.h)   | This code snippet, located in the GUI directory, contributes to the CallMon repository's architecture by providing the necessary resources for the graphical user interface (GUI). It includes resource definitions and controls for the main dialog window.                                                                                                                                                                                                                                                        |
| [CallMon.c](https://github.com/DownWithUp/CallMon/blob/main/GUI/CallMon.c)     | This code snippet is responsible for creating and managing a Graphical User Interface (GUI) in the CallMon software. It initializes the GUI and handles events such as button clicks and window resizing. The code also interacts with the underlying operating system to set up the GUI's appearance and behavior.                                                                                                                                                                                                 |

</details>

---

##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* Rust: `► INSERT-VERSION-HERE`
* `► ...`
* `► ...`

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
Use the following command to run CallMon:
```sh
cargo run
```

###  Tests
To execute tests, run:
```sh
cargo test
```

---

##  Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/DownWithUp/CallMon/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/DownWithUp/CallMon/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/DownWithUp/CallMon/issues)**: Submit bugs found or log feature requests for CallMon.

<details closed>
<summary>Contributing Guidelines</summary>

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

[**Return**](#-quick-links)

---
