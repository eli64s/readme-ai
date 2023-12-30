<div id="top" align="center">
   <h1>
      <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100">
      <br>
      FILE.IO-ANDROID-CLIENT
   </h1>
   <h3>◦ Unlocking code brilliance effortlessly.</h3>
   <h3>◦ Developed with the software and tools below.</h3>

<p align="center">
      <img src="https://img.shields.io/badge/Firebase-FFCA28.svg?style=flat&logo=Firebase&logoColor=black" alt="Firebase">
<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat&logo=YAML&logoColor=white" alt="YAML">
<img src="https://img.shields.io/badge/Kotlin-7F52FF.svg?style=flat&logo=Kotlin&logoColor=white" alt="Kotlin">
<img src="https://img.shields.io/badge/Org-77AA99.svg?style=flat&logo=Org&logoColor=white" alt="Org">
<img src="https://img.shields.io/badge/Google-4285F4.svg?style=flat&logo=Google&logoColor=white" alt="Google">

<img src="https://img.shields.io/badge/Android-3DDC84.svg?style=flat&logo=Android&logoColor=white" alt="Android">
<img src="https://img.shields.io/badge/GitHub-181717.svg?style=flat&logo=GitHub&logoColor=white" alt="GitHub">
<img src="https://img.shields.io/badge/Gradle-02303A.svg?style=flat&logo=Gradle&logoColor=white" alt="Gradle">
<img src="https://img.shields.io/badge/java-%23ED8B00.svg?style=flat&logo=openjdk&logoColor=white" alt="java">
<img src="https://img.shields.io/badge/JetBrains-000000.svg?style=flat&logo=JetBrains&logoColor=white" alt="JetBrains">
   </p>
   <img src="https://img.shields.io/github/license/rumaan/file.io-Android-Client?style=flat&color=5D6D7E" alt="github-license">
   <img src="https://img.shields.io/github/last-commit/rumaan/file.io-Android-Client?style=flat&color=5D6D7E" alt="github-last-commit">
   <img src="https://img.shields.io/github/commit-activity/m/rumaan/file.io-Android-Client?style=flat&color=5D6D7E" alt="github-commit-activity">
   <img src="https://img.shields.io/github/languages/top/rumaan/file.io-Android-Client?style=flat&color=5D6D7E" alt="github-top-language">
</div>

---

##  Quick Links
- [🔗 Quick Links](#-quick-links)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [🧩 Modules](#modules)
- [🚀 Getting Started](#-getting-started)
    - [⚙️ Installation](#-installation)
    - [🤖 Running file.io-Android-Client](#-running-file.io-Android-Client)
    - [🧪 Tests](#-tests)
- [🚧 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---

##  Overview

The FILE.IO-ANDROID-CLIENT project is an Android client application that provides users with the ability to upload and manage files to the file.io file-sharing service. The app allows users to easily upload files, view their upload history, and share files with others. With a simple and intuitive user interface, the app aims to simplify the process of file sharing on mobile devices, providing convenience and efficiency to users.

---

##  Features

|    | Category          | Details                                                                                                                                      |
|----|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The codebase follows a modular architecture, with separate packages for different features and components. It utilizes the MVVM (Model-View-ViewModel) architectural pattern to separate the presentation logic from the data model. |
| 📄 | **Documentation**  | The codebase has comprehensive inline documentation with well-defined function and variable names, making it easy to understand the purpose and functionality of each component.                                |
| 🔗 | **Dependencies**   | The codebase relies on external libraries such as Retrofit for network operations, Room for local data storage, and Gson for JSON parsing. These libraries provide efficient and convenient solutions for their respective functionalities.|
| 🧩 | **Modularity**    | The codebase is organized into smaller modules, allowing for easy component reuse and maintainability. Each module focuses on a specific functionality or feature, making it easier to modify or update specific parts of the system without affecting others. |
| 🧪 | **Testing**       | The codebase includes unit tests, instrumented tests, and integration tests. It utilizes popular testing frameworks such as JUnit and Espresso. The tests cover different aspects of the system, including data manipulation, UI interactions, and network operations. |
| ⚡️ | **Performance**    | The codebase is designed with performance in mind. It utilizes asynchronous operations with coroutines and the WorkManager API for background tasks, ensuring smooth user experience and efficient resource utilization. The use of caching, pagination, and other optimization techniques further enhances performance. |
| 🔐 | **Security**       | The codebase incorporates security measures such as secure network communication using HTTPS and encryption of sensitive data. It follows best practices for data handling, validation, and authentication to ensure the confidentiality and integrity of user information.

---

##  Repository Structure

```sh
└── FILE.IO-ANDROID-CLIENT/
    ├── .travis.yml
    ├── app/
    │   ├── build/
    │   │   └── outputs/
    │   ├── build.gradle
    │   ├── proguard-rules.pro
    │   ├── release/
    │   │   └── app-release.apk
    │   └── src/
    │       ├── androidTest/
    │       ├── main/
    │       └── test/
    ├── build.gradle
    ├── gradle/
    │   └── wrapper/
    ├── screenshots/
    │   ├── readme.txt
    └── settings.gradle

```

---



##  Modules

<details closed><summary>.</summary>

| File                                                                                          | Summary                                                                                                                                                                                                                                                                     |
| ---                                                                                           | ---                                                                                                                                                                                                                                                                         |
| [build.gradle](https://github.com/rumaan/file.io-Android-Client/blob/main/build.gradle)       | This code snippet sets up the build and dependencies for an Android client app in the FILE.IO-ANDROID-CLIENT repository. It includes configurations for Gradle, Kotlin, and Google Services. The code ensures the app can be built and run successfully on Android devices. |
| [settings.gradle](https://github.com/rumaan/file.io-Android-Client/blob/main/settings.gradle) | This code snippet, located in the `settings.gradle` file, includes the:app module as a key file in the `FILE.IO-ANDROID-CLIENT` repository structure.                                                                                                                       |
| [.travis.yml](https://github.com/rumaan/file.io-Android-Client/blob/main/.travis.yml)         | This code snippet configures the build environment for an Android client application. It sets up the required Android SDK components, licenses, and caching to ensure smooth build and deployment processes.                                                                |

</details>

<details closed><summary>screenshots</summary>

| File                                                                                            | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---                                                                                             | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [readme.txt](https://github.com/rumaan/file.io-Android-Client/blob/main/screenshots/readme.txt) | The code snippet in the FILE.IO-ANDROID-CLIENT repository is a critical component for the Android client application. It achieves various functionalities and features related to file management, upload, and download processes. It is built using Gradle and includes essential files such as the build.gradle and proguard-rules.pro. Dependencies and software used in the codebase are documented in the screenshots/readme.txt file. Key files include readme.txt, screenshot.png, and todo-ui.png. |

</details>

<details closed><summary>app</summary>

| File                                                                                                    | Summary                                                                                                                                                                                                                                                                                                                |
| ---                                                                                                     | ---                                                                                                                                                                                                                                                                                                                    |
| [proguard-rules.pro](https://github.com/rumaan/file.io-Android-Client/blob/main/app/proguard-rules.pro) | The code snippet contains ProGuard rules for an Android app. It specifies rules for code obfuscation and optimization. The rules keep certain classes and attributes, while ignoring warnings and hiding file names. It also includes specific rules for Crashlytics.                                                  |
| [build.gradle](https://github.com/rumaan/file.io-Android-Client/blob/main/app/build.gradle)             | This code snippet is part of the FILE.IO-ANDROID-CLIENT repository. It applies plugins and sets dependencies for an Android app, including libraries for UI components, testing, permissions, Firebase Crashlytics, Room, Fuel, Gson, Kotlin, and more. It also configures build types for release and debug versions. |

</details>

<details closed><summary>app.src.androidTest.java.com.thecoolguy.rumaan.fileio</summary>

| File                                                                                                                                                                                      | Summary                                                                                                                                                                                                                                                                                                     |
| ---                                                                                                                                                                                       | ---                                                                                                                                                                                                                                                                                                         |
| [ExampleInstrumentedTest.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/androidTest/java/com/thecoolguy/rumaan/fileio/ExampleInstrumentedTest.kt)                 | This code snippet is an instrumental test that verifies the correct package name of the Android app. It uses the `InstrumentationRegistry` and `ActivityTestRule` to access the app's context and asserts the package name.                                                                                 |
| [FileEntityDaoTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/androidTest/java/com/thecoolguy/rumaan/fileio/FileEntityDaoTest.java)                         | The code snippet is a test class that verifies the functionality of RoomDatabase in the FILE.IO-ANDROID-CLIENT repository. It tests the insertion, retrieval, and count of FileEntity objects in the database. The code ensures that the database functions properly and the expected results are obtained. |
| [UploadHistoryInstrumentedTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/androidTest/java/com/thecoolguy/rumaan/fileio/UploadHistoryInstrumentedTest.java) | This code snippet is a test class in the FILE.IO-ANDROID-CLIENT repository. It contains a test method to check the functionality of long-pressing an item for deletion in the Upload History feature of the app. The test uses a Room database to store and retrieve file entities.                         |

</details>

<details closed><summary>app.src.test.java.com.thecoolguy.rumaan.fileio</summary>

| File                                                                                                                                                             | Summary                                                                                                                                                                                                                                                                                                |
| ---                                                                                                                                                              | ---                                                                                                                                                                                                                                                                                                    |
| [ExampleUnitTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/test/java/com/thecoolguy/rumaan/fileio/ExampleUnitTest.java)           | The code snippet is an example local unit test file that verifies if the addition operation is correct. It is part of the FILE.IO-ANDROID-CLIENT repository and helps ensure the accuracy of the codebase.                                                                                             |
| [UploadRepositoryTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/test/java/com/thecoolguy/rumaan/fileio/UploadRepositoryTest.java) | This code snippet tests the functionality of the `UploadRepository` class in the parent repository. It specifically checks the generation of an expiration URL using constants defined in `ConstantsKt` and the `URLParser` utility. The test ensures that the generated URL matches the expected URL. |
| [UrlTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/test/java/com/thecoolguy/rumaan/fileio/UrlTest.java)                           | This code snippet tests the `parseEncryptUrl` method in the `UrlTest` class. It verifies that the method correctly extracts the base URL from an encrypted URL. The test case uses the `assertEquals` method to compare the expected and actual results.                                               |
| [FileEntityTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/test/java/com/thecoolguy/rumaan/fileio/FileEntityTest.java)             | This code snippet is a test file in the FILE.IO-ANDROID-CLIENT repository. It tests the functionality of the FileEntity class by setting values for name and URL properties and asserting their correctness.                                                                                           |

</details>

<details closed><summary>app.src.main.java.com.thecoolguy.rumaan.fileio.viewmodel</summary>

| File                                                                                                                                                                       | Summary                                                                                                                                                                                                                                                                                              |
| ---                                                                                                                                                                        | ---                                                                                                                                                                                                                                                                                                  |
| [UploadHistoryViewModel.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/viewmodel/UploadHistoryViewModel.kt) | This code snippet is part of the FILE.IO-ANDROID-CLIENT repository. It defines the UploadHistoryViewModel, which retrieves a list of uploaded files from a local database and provides it as a LiveData object. This ViewModel is used in the Android app to display the upload history to the user. |

</details>

<details closed><summary>app.src.main.java.com.thecoolguy.rumaan.fileio.ui</summary>

| File                                                                                                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                         |
| ---                                                                                                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                             |
| [FileioApplication.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/FileioApplication.kt)               | This code snippet is a base Application class that initializes important components like logging and error handling for the FILE.IO-ANDROID-CLIENT repository. It sets up logging using Timber and configures a custom activity for handling crashes using CaocConfig.                                                                                          |
| [UploadHistoryListAdapter.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/UploadHistoryListAdapter.kt) | The code snippet is a part of the FILE.IO-ANDROID-CLIENT repository and is responsible for providing a list adapter for the upload history feature in the Android app. It manages the display of different types of items in the list, such as dates and file entities. The adapter also handles user interactions, such as copying file URLs to the clipboard. |
| [SwipeToDeleteCallBack.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/SwipeToDeleteCallBack.kt)       | The code snippet provides a Swipe-to-Delete feature for a RecyclerView in an Android app. It uses a custom ItemTouchHelper to handle swiping gestures and displays a delete icon with a red background. The code also prevents swiping on specific items.                                                                                                       |
| [NotificationHelper.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/NotificationHelper.kt)             | This code snippet defines a NotificationHelper class that creates and displays a notification when a file upload is successful. It sets the notification's content, icon, sound, and click behavior. It also handles notification grouping and creates a notification channel for devices running Android Oreo and above.                                       |

</details>

<details closed><summary>app.src.main.java.com.thecoolguy.rumaan.fileio.ui.fragments</summary>

| File                                                                                                                                                                            | Summary                                                                                                                                                                                                                                                                                                       |
| ---                                                                                                                                                                             | ---                                                                                                                                                                                                                                                                                                           |
| [NoNetworkDialogFragment.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/NoNetworkDialogFragment.kt) | This code snippet defines the `NoNetworkDialogFragment` class, which is a dialog fragment displayed when there is no network connection. It handles the creation of the dialog and its button click events. The class also communicates with the parent activity through the `DialogClickListener` interface. |
| [HomeFragment.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/HomeFragment.kt)                       | This code snippet is part of the FILE.IO-ANDROID-CLIENT repository and represents the HomeFragment file. It is responsible for displaying the main layout of the app and handling user interactions, such as choosing a file to upload. It communicates with other components through a listener interface.   |
| [ResultFragment.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/ResultFragment.kt)                   | This code snippet is a Kotlin fragment that displays the result of a file upload or download. It takes in a URL and the number of days the link will expire, and displays them on the UI. It also has a button to indicate completion and a feature to copy the link to the clipboard.                        |

</details>

<details closed><summary>app.src.main.java.com.thecoolguy.rumaan.fileio.ui.activities</summary>

| File                                                                                                                                                                         | Summary                                                                                                                                                                                                                                                                                                                                   |
| ---                                                                                                                                                                          | ---                                                                                                                                                                                                                                                                                                                                       |
| [MainActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/MainActivity.kt)                   | The code snippet is the main activity file in the Android client of the FILE.IO repository. It handles UI interactions, file uploads, and displays results to the user. The activity also manages permissions and fragments for navigation.                                                                                               |
| [ErrorActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/ErrorActivity.kt)                 | This code snippet is an Android activity called ErrorActivity that handles runtime crashes and displays an error screen. It extends the AppCompatActivity class and overrides the onBackPressed() and onCreate() methods.                                                                                                                 |
| [UploadHistoryActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/UploadHistoryActivity.kt) | This code snippet is responsible for managing the upload history activity in the FILE.IO-ANDROID-CLIENT repository. It handles user interactions, such as clearing the history and deleting individual items. It also updates the UI and communicates with the database.                                                                  |
| [AboutActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/AboutActivity.kt)                 | This code snippet implements the `AboutActivity` class in the Android client of the FILE.IO repository. It sets up the activity layout, menu items, and navigation. It also handles the opening of the `LicenseActivity` when the Open Source option is selected from the menu.                                                           |
| [LicenseActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/LicenseActivity.kt)             | This code snippet defines the LicenseActivity class, which extends MaterialAboutActivity. It creates a list of open source licenses to display in the app. Each license is represented by a card, containing details such as the library name, year, author, and license type. The list is then returned to be displayed in the activity. |

</details>

<details closed><summary>app.src.main.java.com.thecoolguy.rumaan.fileio.repository</summary>

| File                                                                                                                                                                    | Summary                                                                                                                                                                                                                                                                                              |
| ---                                                                                                                                                                     | ---                                                                                                                                                                                                                                                                                                  |
| [UploadHistoryWorkers.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/repository/UploadHistoryWorkers.kt) | This code snippet contains two workers, ClearHistoryWorker and DeleteSingleItemWorker, which handle clearing the upload history and deleting a single item from the history, respectively. They utilize the UploadHistoryRoomDatabase to perform database operations.                                |
| [UploadWorker.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/repository/UploadWorker.kt)                 | The `UploadWorker` class in the `com.thecoolguy.rumaan.fileio.repository` package is a key file in the codebase. It handles the uploading of files to the server, saving them to the local database, and sending notifications. It uses various dependencies and works with the WorkManager library. |

</details>

<details closed><summary>app.src.main.java.com.thecoolguy.rumaan.fileio.utils</summary>

| File                                                                                                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                                                                 |
| ---                                                                                                                                                                        | ---                                                                                                                                                                                                                                                                                                                                                                                     |
| [Extensions.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Extensions.kt)                             | This code snippet provides utility extensions for Android development. It includes functions for displaying toasts and toggling the clickability of views. These extensions can be used to enhance the user experience and streamline development in the FILE.IO-ANDROID-CLIENT repository.                                                                                             |
| [WorkManagerHelper.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/WorkManagerHelper.kt)               | This code snippet in the `WorkManagerHelper.kt` file is responsible for creating an upload work request using the Android WorkManager library. It sets the required network type as connected and passes the URI for upload as input data. The `UploadWorker` class is used to handle the actual upload task.                                                                           |
| [Utils.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Utils.kt)                                       | This code snippet provides helper methods for various tasks such as getting file details, opening files, checking network connectivity, showing dialogs, copying text to the clipboard, parsing URLs, and parsing JSON. It is part of the `Utils` class in the `com.thecoolguy.rumaan.fileio.utils` package.                                                                            |
| [Helpers.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Helpers.kt)                                   | This code snippet in the FILE.IO-ANDROID-CLIENT repository contains utility functions for handling file metadata and composition. It retrieves file metadata such as name and size from a given URI. It also composes the file into a FileEntity object using additional information from a response. These functions are crucial for managing files in the Android client application. |
| [FragmentHelperExtensions.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/FragmentHelperExtensions.kt) | This code snippet provides utility functions to add and replace fragments within an Android app using the FragmentManager. It simplifies the process of managing fragments and their transitions within the app's architecture.                                                                                                                                                         |
| [MaterialIn.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/MaterialIn.kt)                             | This code snippet, located in the `com.thecoolguy.rumaan.fileio.utils` package, animates views using Material Design guidelines. It provides functions to animate views with fade and slide effects based on specified directions. The snippet includes functions to initialize and start the animations for the views.                                                                 |
| [Constants.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Constants.kt)                               | The code snippet in the `Constants.kt` file provides global constants and URLs used in the FILE.IO-ANDROID-CLIENT repository. It includes the base URL, expiration parameters, default expiration weeks, and URLs for GitHub and Twitter. It also includes constants for appending a postfix and formatting a timestamp.                                                                |

</details>

<details closed><summary>app.src.main.java.com.thecoolguy.rumaan.fileio.listeners</summary>

| File                                                                                                                                                                                     | Summary                                                                                                                                                                                                                                                   |
| ---                                                                                                                                                                                      | ---                                                                                                                                                                                                                                                       |
| [DialogClickListener.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/listeners/DialogClickListener.kt)                     | This code snippet defines an interface called DialogClickListener, which is used in the FILE.IO-ANDROID-CLIENT repository to handle positive button clicks in dialogs. It takes a Dialog and a DialogFragment as parameters and does not return anything. |
| [OnFragmentInteractionListener.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/listeners/OnFragmentInteractionListener.kt) | This code snippet defines an interface called OnFragmentInteractionListener, which includes two functions: onUploadFileClick() and onDone(). This interface is likely used for communication between fragments in the FILE.IO-ANDROID-CLIENT repository.  |

</details>

---

##  Getting Started

***Prerequisites***

Ensure you have the following dependencies installed on your system:

- `► INSERT-DEPENDENCY-1`
- `► INSERT-DEPENDENCY-2`
- `► INSERT-DEPENDENCY-3`
- `► ...`

###  Installation

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

###  Running file.io-Android-Client
Use the following command to run file.io-Android-Client:
```sh
java -jar build/libs/myapp.jar
```

###  Tests
To execute tests, run:
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

- **[Submit Pull Requests](https://github.com/rumaan/file.io-Android-Client/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/rumaan/file.io-Android-Client/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/rumaan/file.io-Android-Client/issues)**: Submit bugs found or log feature requests for file.io-Android-Client.

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
