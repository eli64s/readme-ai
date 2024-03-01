<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Android_dance.svg/524px-Android_dance.svg.png?20120402102952" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">FILE.IO-ANDROID-CLIENT</h1>
</p>
<p align="center">
    <em>Share files seamlessly with file.io-Android-Client!</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/rumaan/file.io-Android-Client?style=flat-square&logo=opensourceinitiative&logoColor=white&color=50C878" alt="license">
	<img src="https://img.shields.io/github/last-commit/rumaan/file.io-Android-Client?style=flat-square&logo=git&logoColor=white&color=50C878" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/rumaan/file.io-Android-Client?style=flat-square&color=50C878" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/rumaan/file.io-Android-Client?style=flat-square&color=50C878" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Firebase-FFCA28.svg?style=flat-square&logo=Firebase&logoColor=black" alt="Firebase">
	<img src="https://img.shields.io/badge/Kotlin-7F52FF.svg?style=flat-square&logo=Kotlin&logoColor=white" alt="Kotlin">
	<img src="https://img.shields.io/badge/Org-77AA99.svg?style=flat-square&logo=Org&logoColor=white" alt="Org">
	<img src="https://img.shields.io/badge/Google-4285F4.svg?style=flat-square&logo=Google&logoColor=white" alt="Google">
	<img src="https://img.shields.io/badge/Android-3DDC84.svg?style=flat-square&logo=Android&logoColor=white" alt="Android">
	<br>
	<img src="https://img.shields.io/badge/GitHub-181717.svg?style=flat-square&logo=GitHub&logoColor=white" alt="GitHub">
	<img src="https://img.shields.io/badge/Gradle-02303A.svg?style=flat-square&logo=Gradle&logoColor=white" alt="Gradle">
	<img src="https://img.shields.io/badge/java-%23ED8B00.svg?style=flat-square&logo=openjdk&logoColor=white" alt="java">
	<img src="https://img.shields.io/badge/JetBrains-000000.svg?style=flat-square&logo=JetBrains&logoColor=white" alt="JetBrains">
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
  - [ Using file.io-Android-Client](#-using-file.io-Android-Client)
  - [ Tests](#-tests)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)
</details>
<hr>

##  Overview

file.io-Android-Client is an Android application for secure and convenient file uploads. It includes features such as file upload history management, notification alerts for successful uploads, and obfuscation for enhanced security. The project utilizes Android architecture components like Room database, WorkManager for background tasks, and Fuel for HTTP requests. With a user-friendly interface, swiping to delete items, and interactive fragments, file.io-Android-Client offers a seamless experience for users to upload files with ease and track their upload history efficiently.

---

##  Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | The project follows a clean MVVM architecture with ViewModel, Repository, and UI components separated. It leverages Android Jetpack components like Room for database operations and WorkManager for background processing. |
| 🔩 | **Code Quality**  | The codebase adheres to Kotlin coding standards and best practices. It uses consistent naming conventions, follows SOLID principles, and includes unit tests for critical components. |
| 📄 | **Documentation** | The project has detailed inline comments, README files, and descriptive commit messages. Additionally, it includes documentation for classes and methods to aid in understanding the codebase. |
| 🔌 | **Integrations**  | Key integrations include Firebase for analytics, Katana for dependency injection, and Fuel for making HTTP requests. Google services are integrated for notifications and WorkManager for managing background tasks. |
| 🧩 | **Modularity**    | The codebase is modular, with separate packages for UI, ViewModel, Repository, and utils. This structure allows for easy maintenance, testing, and reusability of components across the project. |
| 🧪 | **Testing**       | Testing is done using JUnit for unit tests and Espresso for UI tests. Mocking frameworks like Mockito are utilized for simulating dependencies. Tests cover ViewModel logic, database operations, and UI interactions. |
| ⚡️  | **Performance**   | The app is designed for efficiency with optimized network requests using Fuel, background tasks handled by WorkManager, and local data storage managed by Room database. The architecture aims to provide a smooth user experience. |
| 🛡️ | **Security**      | Data protection measures include ProGuard for code obfuscation, ensuring secure HTTP requests with Fuel, and handling sensitive information securely. Permissions are carefully managed, and network security best practices are followed. |
| 📦 | **Dependencies**  | Key external libraries and dependencies include AndroidX components, Material design support, Kotlin extensions, Timber for logging, and Gson for JSON serialization. These libraries enhance app functionality and development speed. |

---

##  Repository Structure

```sh
└── file.io-Android-Client/
    ├── LICENSE
    ├── README.md
    ├── app
    │   ├── .gitignore
    │   ├── build
    │   ├── build.gradle
    │   ├── proguard-rules.pro
    │   ├── release
    │   └── src
    ├── build.gradle
    ├── gradle
    │   ├── .DS_Store
    │   └── wrapper
    ├── gradle.properties
    ├── gradlew
    ├── screenshots
    │   ├── readme.txt
    │   ├── screen1.png
    │   ├── screen2.png
    │   ├── screenshot.png
    │   └── todo-ui.png
    └── settings.gradle
```

---

##  Modules

<details closed><summary>.</summary>

| File                                                                                            | Summary                                                                                                                         |
| ---                                                                                             | ---                                                                                                                             |
| [build.gradle](https://github.com/rumaan/file.io-Android-Client/blob/master/build.gradle)       | Configures build dependencies for Android project-includes Google, Fabric.io, and Kotlin Gradle plugins with specific versions. |
| [settings.gradle](https://github.com/rumaan/file.io-Android-Client/blob/master/settings.gradle) | Manages app module configuration and inclusion within the project's build process.                                              |

</details>

<details closed><summary>screenshots</summary>

| File                                                                                              | Summary                                                                 |
| ---                                                                                               | ---                                                                     |
| [readme.txt](https://github.com/rumaan/file.io-Android-Client/blob/master/screenshots/readme.txt) | Generates and organizes project screenshots for documentation purposes. |

</details>

<details closed><summary>app</summary>

| File                                                                                                      | Summary                                                                                                                                                                                 |
| ---                                                                                                       | ---                                                                                                                                                                                     |
| [proguard-rules.pro](https://github.com/rumaan/file.io-Android-Client/blob/master/app/proguard-rules.pro) | Enhances app security via ProGuard rules for obfuscation and optimization. Maintains specific configurations for ProGuard in Android projects, ensuring code protection and efficiency. |
| [build.gradle](https://github.com/rumaan/file.io-Android-Client/blob/master/app/build.gradle)             | Configure Android application build settings, dependencies, and plugins for the file path app/build.gradle in the Android client repository.                                            |

</details>

<details closed><summary>app.src.androidTest.java.com.thecoolguy.rumaan.fileio</summary>

| File                                                                                                                                                                                        | Summary                                                                                                                                     |
| ---                                                                                                                                                                                         | ---                                                                                                                                         |
| [ExampleInstrumentedTest.kt](https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/androidTest/java/com/thecoolguy/rumaan/fileio/ExampleInstrumentedTest.kt)                 | Android Instrumented Test ensuring correct package name in the app under test.                                                              |
| [FileEntityDaoTest.java](https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/androidTest/java/com/thecoolguy/rumaan/fileio/FileEntityDaoTest.java)                         | Tests database operations on FileEntity using RoomDB in Android app. Performs row count checks, insertion, and retrieval of multiple items. |
| [UploadHistoryInstrumentedTest.java](https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/androidTest/java/com/thecoolguy/rumaan/fileio/UploadHistoryInstrumentedTest.java) | Implements database interactions for UploadHistoryActivity with Room database, inserting test data for upload items.                        |

</details>

<details closed><summary>app.src.test.java.com.thecoolguy.rumaan.fileio</summary>

| File                                                                                                                                                               | Summary                                                                                                              |
| ---                                                                                                                                                                | ---                                                                                                                  |
| [ExampleUnitTest.java](https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/test/java/com/thecoolguy/rumaan/fileio/ExampleUnitTest.java)           | Unit test ensuring addition correctness in Android app via JUnit assertions, contributing to app reliability.        |
| [UploadRepositoryTest.java](https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/test/java/com/thecoolguy/rumaan/fileio/UploadRepositoryTest.java) | Test code to validate URL expiration functionality and constants in the upload repository of the Android client app. |
| [UrlTest.java](https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/test/java/com/thecoolguy/rumaan/fileio/UrlTest.java)                           | Test URL parsing functionality for the Android Client app. Verifies URL extraction from encrypted link.              |
| [FileEntityTest.java](https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/test/java/com/thecoolguy/rumaan/fileio/FileEntityTest.java)             | Test code for setting and checking properties in `FileEntity` model.                                                 |

</details>

<details closed><summary>app.src.main.java.com.thecoolguy.rumaan.fileio.viewmodel</summary>

| File                                                                                                                                                                         | Summary                                                                                                             |
| ---                                                                                                                                                                          | ---                                                                                                                 |
| [UploadHistoryViewModel.kt](https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/viewmodel/UploadHistoryViewModel.kt) | ViewModel for Upload History in File.io Android Client repository. Manages file upload records using Room database. |

</details>

<details closed><summary>app.src.main.java.com.thecoolguy.rumaan.fileio.ui</summary>

| File                                                                                                                                                                      | Summary                                                                                                                                          |
| ---                                                                                                                                                                       | ---                                                                                                                                              |
| [FileioApplication.kt](https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/FileioApplication.kt)               | Base Application class for file.io Android client managing logging with Timber and custom error handling using Custom Activity on Crash library. |
| [UploadHistoryListAdapter.kt](https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/UploadHistoryListAdapter.kt) | Custom RecyclerView adapter for displaying upload history with date separators and clickable file entries.                                       |
| [SwipeToDeleteCallBack.kt](https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/SwipeToDeleteCallBack.kt)       | Enables swipe-to-delete functionality for RecyclerView items, featuring a red background and delete icon. Prevents swipes on specific views.     |
| [NotificationHelper.kt](https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/NotificationHelper.kt)             | Manages notifications upon successful file uploads, including creation, customization, and display with optional channel support.                |

</details>

<details closed><summary>app.src.main.java.com.thecoolguy.rumaan.fileio.ui.fragments</summary>

| File                                                                                                                                                                              | Summary                                                                                                                                                                                          |
| ---                                                                                                                                                                               | ---                                                                                                                                                                                              |
| [NoNetworkDialogFragment.kt](https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/NoNetworkDialogFragment.kt) | Dialog fragment for handling no network error, providing a customizable dialog with an OK button, facilitating interaction with the user.                                                        |
| [HomeFragment.kt](https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/HomeFragment.kt)                       | Implementing a HomeFragment for user interaction, facilitating file upload callbacks via a chosen file button click.                                                                             |
| [ResultFragment.kt](https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/ResultFragment.kt)                   | Fragment for displaying result details and interaction. Implements UI components, clipboard functionality, and fragment lifecycle methods for handling user interactions within the Android app. |

</details>

<details closed><summary>app.src.main.java.com.thecoolguy.rumaan.fileio.ui.activities</summary>

| File                                                                                                                                                                           | Summary                                                                                                                                                    |
| ---                                                                                                                                                                            | ---                                                                                                                                                        |
| [MainActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/MainActivity.kt)                   | Entry point for the Android client UI. Manages file uploads, displays results, and handles permissions. Integrates with WorkManager for upload processing. |
| [ErrorActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/ErrorActivity.kt)                 | ErrorActivity handles runtime crashes by displaying an error screen and ensuring app stability through an affinity finish.                                 |
| [UploadHistoryActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/UploadHistoryActivity.kt) | Clear/remove items, swipe to delete, group by date, and display in a list with animations.                                                                 |
| [AboutActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/AboutActivity.kt)                 | Manages the About section UI functionality, enabling navigation to the License page and incorporating a transparent navigation style.                      |
| [LicenseActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/LicenseActivity.kt)             | Generates Open Source License details for various components in Android app using MaterialAboutLibrary.                                                    |

</details>

<details closed><summary>app.src.main.java.com.thecoolguy.rumaan.fileio.repository</summary>

| File                                                                                                                                                                      | Summary                                                                                                                                                                |
| ---                                                                                                                                                                       | ---                                                                                                                                                                    |
| [UploadHistoryWorkers.kt](https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/repository/UploadHistoryWorkers.kt) | Worker classes for uploading history management in the Android client app. ClearHistoryWorker clears all items, DeleteSingleItemWorker deletes a specified item by ID. |
| [UploadWorker.kt](https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/repository/UploadWorker.kt)                 | Manages file upload tasks, saving to DB, and sending notifications. Utilizes Fuel for HTTP requests and WorkManager for background processing.                         |

</details>

<details closed><summary>app.src.main.java.com.thecoolguy.rumaan.fileio.utils</summary>

| File                                                                                                                                                                         | Summary                                                                                                                                                                               |
| ---                                                                                                                                                                          | ---                                                                                                                                                                                   |
| [Extensions.kt](https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Extensions.kt)                             | Adds toast messages and clickability toggling functionality to Android views.                                                                                                         |
| [WorkManagerHelper.kt](https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/WorkManagerHelper.kt)               | Creates a one-time upload task with specified constraints using WorkManager for the Android client app in the repository.                                                             |
| [Utils.kt](https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Utils.kt)                                       | Provides a set of utility methods for Android tasks, such as handling file details, file operations, network status check, dialog management, and more.                               |
| [Helpers.kt](https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Helpers.kt)                                   | Extracts file metadata and composes it into a FileEntity within the Android client. Includes functions to fetch file data and return a File object.                                   |
| [FragmentHelperExtensions.kt](https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/FragmentHelperExtensions.kt) | Conveniently manage fragment transactions in Android app with support for adding and replacing fragments seamlessly. Enhance user experience during navigation.                       |
| [MaterialIn.kt](https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/MaterialIn.kt)                             | Animate views with Material Design-inspired entrance effects based on specified directions like bottom or top, incorporating fading and sliding animations for smooth UI transitions. |
| [Constants.kt](https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Constants.kt)                               | Define global constants for API base URL, expiry parameters, default expiration, URLs for Github and Twitter, email address, suffix for download links, and timestamp format.         |

</details>

<details closed><summary>app.src.main.java.com.thecoolguy.rumaan.fileio.listeners</summary>

| File                                                                                                                                                                                       | Summary                                                                                                     |
| ---                                                                                                                                                                                        | ---                                                                                                         |
| [DialogClickListener.kt](https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/listeners/DialogClickListener.kt)                     | Interface for handling click events on dialogs in the Android client app.                                   |
| [OnFragmentInteractionListener.kt](https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/listeners/OnFragmentInteractionListener.kt) | Defines an interface for fragment interactions, enabling actions like file uploads and completion triggers. |

</details>

---

##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Kotlin**: `version x.y.z`

###  Install

1. Clone the file.io-Android-Client repository:

```sh
git clone https://github.com/rumaan/file.io-Android-Client
```

2. Change to the project directory:

```sh
cd file.io-Android-Client
```

3. Install the dependencies:

```sh
gradle build
```

###  Using `file.io-Android-Client`

Use the following command to run file.io-Android-Client:

```sh
java -jar build/libs/myapp.jar
```

###  Tests

Use the following command to run tests:

```sh
gradle test
```

---

##  Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/rumaan/file.io-Android-Client/issues)**: Submit bugs found or log feature requests for the `file.io-Android-Client` project.
- **[Submit Pull Requests](https://github.com/rumaan/file.io-Android-Client/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/rumaan/file.io-Android-Client/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/rumaan/file.io-Android-Client
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
<p align="left">
   <a href="https://github.com{/rumaan/file.io-Android-Client/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=rumaan/file.io-Android-Client">
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
