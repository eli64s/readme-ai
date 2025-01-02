<p align="center">
  <img src="https://img.icons8.com/external-tal-revivo-regular-tal-revivo/96/external-readme-is-a-easy-to-build-a-developer-hub-that-adapts-to-the-user-logo-regular-tal-revivo.png" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">CALLMON</h1>
</p>
<p align="center">
    <em>Revolutionizing Call Monitoring with CallMon</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/DownWithUp/CallMon?style=flat&logo=opensourceinitiative&logoColor=white&color=lightgrey" alt="license">
	<img src="https://img.shields.io/github/last-commit/DownWithUp/CallMon?style=flat&logo=git&logoColor=white&color=lightgrey" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/DownWithUp/CallMon?style=flat&color=lightgrey" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/DownWithUp/CallMon?style=flat&color=lightgrey" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/C-A8B9CC.svg?style=flat&logo=C&logoColor=black" alt="C">
	<img src="https://img.shields.io/badge/Rust-000000.svg?style=flat&logo=Rust&logoColor=white" alt="Rust">
</p>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>

- [ Overview](#-overview)
- [ Features](#-features)
- [ Repository Structure](#-repository-structure)
- [ Modules](#-modules)
- [ Getting Started](#-getting-started)
  - [ Install](#-install)
  - [ Using CallMon](#-using-CallMon)
  - [ Tests](#-tests)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)
</details>
<hr>

##  Overview

CallMon is a comprehensive system monitoring tool that combines kernel-level functions for system call monitoring and process management with a user-friendly graphical interface. The project offers value by providing real-time data display and interactive features to monitor system activities efficiently. Leveraging Rust for kernel interactions and WinAPI support, CallMon automates driver building and signing processes, ensuring streamlined development. With functionalities such as process suspension, resumption, and system call handling, CallMon caters to users seeking a robust system monitoring solution with both powerful backend capabilities and intuitive frontend usability.

---

##  Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | The project is structured with a Rust module for kernel interactions and a GUI component for user interface management. The architecture emphasizes system monitoring and process management at a kernel level. |
| 🔩 | **Code Quality**  | The codebase maintains a high level of quality with consistent style formatting using tools like `rustfmt`. It also follows best practices for Windows driver development, ensuring readability and maintainability. |
| 📄 | **Documentation** | The project includes detailed documentation within the codebase outlining the functionalities of each module. However, external documentation could be enhanced for easier onboarding and understanding of the project. |
| 🔌 | **Integrations**  | Key integrations include Rust for kernel-level interactions, WinAPI for Windows-specific functionality, and Visual C++ for GUI development. External dependencies include 'toml' and 'rc'. |
| 🧩 | **Modularity**    | The codebase is modular, with separate modules for driver functionality and GUI components. This design promotes code reusability and ease of maintenance for specific functionalities. |
| 🧪 | **Testing**       | Testing frameworks and tools used are not explicitly mentioned in the repository contents. Adding testing frameworks like `cargo test` could enhance code reliability and robustness. |
| ⚡️  | **Performance**   | Efficiency and speed are prioritized in the project, especially in kernel interactions for system call monitoring and process management. Resource usage is optimized for better performance. |
| 🛡️ | **Security**      | Security measures for data protection and access control are not explicitly mentioned in the repository contents. Implementing secure coding practices and access control mechanisms would enhance the security of the project. |
| 📦 | **Dependencies**  | Key external libraries and dependencies include 'rust', 'toml', 'rc', 'c', 'Cargo.toml', 'rs', and 'h' for various functionalities like kernel interactions, GUI development, and Windows driver management. |
| 🚀 | **Scalability**   | The project demonstrates potential scalability by focusing on system monitoring and process management at a kernel level. Additional optimizations can be made to handle increased traffic and load effectively. |

---

##  Repository Structure

```sh
└── CallMon/
    ├── Driver
    │   ├── AltCall.c
    │   └── Extras.h
    ├── GUI
    │   ├── CallMon.c
    │   ├── Resource.rc
    │   ├── Utils.h
    │   └── resource.h
    ├── README.md
    └── Rust
        ├── .cargo
        ├── Cargo.toml
        ├── Makefile.toml
        ├── build.rs
        ├── rustfmt.toml
        └── src
```

---

##  Modules

<details closed><summary>Driver</summary>

| File                                                                            | Summary                                                                                                                                            |
| ---                                                                             | ---                                                                                                                                                |
| [AltCall.c](https://github.com/DownWithUp/CallMon/blob/master/Driver/AltCall.c) | Implements kernel-level functions for system call monitoring and process management.                                                               |
| [Extras.h](https://github.com/DownWithUp/CallMon/blob/master/Driver/Extras.h)   | Defines structures for a custom header and a total packet containing process ID and stack data for driver functionality in the CallMon repository. |

</details>

<details closed><summary>Rust</summary>

| File                                                                                  | Summary                                                                                                                  |
| ---                                                                                   | ---                                                                                                                      |
| [Makefile.toml](https://github.com/DownWithUp/CallMon/blob/master/Rust/Makefile.toml) | Automates building, renaming, and signing Windows driver file in the CallMon repository's Rust module.                   |
| [Cargo.toml](https://github.com/DownWithUp/CallMon/blob/master/Rust/Cargo.toml)       | Generates a Rust library AltCall for kernel interactions, utilizing winapi, with features like WDM and NTSTATUS support. |
| [rustfmt.toml](https://github.com/DownWithUp/CallMon/blob/master/Rust/rustfmt.toml)   | Automates code formatting for Rust project, ensuring consistent style and readability.                                   |
| [build.rs](https://github.com/DownWithUp/CallMon/blob/master/Rust/build.rs)           | Defines functions to locate Windows Kits directory & kernel mode libraries for link search in Rust build.                |

</details>

<details closed><summary>Rust..cargo</summary>

| File                                                                           | Summary                                                                                                                                                                       |
| ---                                                                            | ---                                                                                                                                                                           |
| [config](https://github.com/DownWithUp/CallMon/blob/master/Rust/.cargo/config) | Configures Rust compiler flags and build settings for Windows driver development. Setting pre-link and post-link arguments for optimization and driver-specific requirements. |

</details>

<details closed><summary>Rust.src</summary>

| File                                                                                | Summary                                                                                                                                              |
| ---                                                                                 | ---                                                                                                                                                  |
| [externs.rs](https://github.com/DownWithUp/CallMon/blob/master/Rust/src/externs.rs) | Provides Rust externs for Windows Kernel-mode functions like creating devices, managing processes, and file I/O operations.                          |
| [log.rs](https://github.com/DownWithUp/CallMon/blob/master/Rust/src/log.rs)         | Exported macro for logging messages with DbgPrint in Rust source.                                                                                    |
| [lib.rs](https://github.com/DownWithUp/CallMon/blob/master/Rust/src/lib.rs)         | Implements driver functionalities including process suspension, resumption, and system call handling for the Rust section of the CallMon repository. |
| [string.rs](https://github.com/DownWithUp/CallMon/blob/master/Rust/src/string.rs)   | Creates a Unicode string from a slice of u16 integers, handling null termination and constructing a UNICODE_STRING struct for WinAPI compatibility.  |
| [defines.rs](https://github.com/DownWithUp/CallMon/blob/master/Rust/src/defines.rs) | Defines and structs for custom winapi types; includes device flags, IOCTL codes, and trap frame data structures.                                     |

</details>

<details closed><summary>GUI</summary>

| File                                                                             | Summary                                                                                                                                                                     |
| ---                                                                              | ---                                                                                                                                                                         |
| [Utils.h](https://github.com/DownWithUp/CallMon/blob/master/GUI/Utils.h)         | Manages driver interaction, process addition, pipe creation, privilege handling, and driver loading for efficient system monitoring in the GUI component of the repository. |
| [Resource.rc](https://github.com/DownWithUp/CallMon/blob/master/GUI/Resource.rc) | Manages the user interface layout for CallMon's configuration settings dialog window.                                                                                       |
| [resource.h](https://github.com/DownWithUp/CallMon/blob/master/GUI/resource.h)   | Manages resource IDs for GUI components in a Visual C++ project.                                                                                                            |
| [CallMon.c](https://github.com/DownWithUp/CallMon/blob/master/GUI/CallMon.c)     | Manages the graphical user interface of CallMon, enabling user interaction and real-time data display through ListView columns and event handling.                          |

</details>

---

##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Rust**: `version x.y.z`

###  Install

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

###  Using `CallMon`

Use the following command to run CallMon:

```sh
cargo run
```

###  Tests

Use the following command to run tests:

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

- **[Report Issues](https://github.com/DownWithUp/CallMon/issues)**: Submit bugs found or log feature requests for the `CallMon` project.
- **[Submit Pull Requests](https://github.com/DownWithUp/CallMon/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/DownWithUp/CallMon/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/DownWithUp/CallMon
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="center">
   <a href="https://github.com{/DownWithUp/CallMon/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=DownWithUp/CallMon">
   </a>
</p>
</details>

---

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-overview)

---
