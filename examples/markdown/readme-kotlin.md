<p align="left">
  <img src="https://img.icons8.com/external-tal-revivo-regular-tal-revivo/96/external-readme-is-a-easy-to-build-a-developer-hub-that-adapts-to-the-user-logo-regular-tal-revivo.png" width="100" />
</p>
<p align="left">
    <h1 align="left">FILE.IO-ANDROID-CLIENT</h1>
</p>
<p align="left">
    <em>Simple file sharing made effortless and fast.</em>
</p>
<p align="left">
	<img src="https://img.shields.io/github/license/rumaan/file.io-Android-Client?style=flat&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/rumaan/file.io-Android-Client?style=flat&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/rumaan/file.io-Android-Client?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/rumaan/file.io-Android-Client?style=flat&color=0080ff" alt="repo-language-count">
<p>
<p align="left">
		<em>Developed with the software and tools below</em>
</p>
<p align="left">
	<img src="https://img.shields.io/badge/Firebase-FFCA28.svg?style=flat&logo=Firebase&logoColor=black" alt="Firebase">
	<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat&logo=YAML&logoColor=white" alt="YAML">
	<img src="https://img.shields.io/badge/Kotlin-7F52FF.svg?style=flat&logo=Kotlin&logoColor=white" alt="Kotlin">
	<img src="https://img.shields.io/badge/Org-77AA99.svg?style=flat&logo=Org&logoColor=white" alt="Org">
	<img src="https://img.shields.io/badge/Google-4285F4.svg?style=flat&logo=Google&logoColor=white" alt="Google">
	<img src="https://img.shields.io/badge/Android-3DDC84.svg?style=flat&logo=Android&logoColor=white" alt="Android">
	<br>
	<img src="https://img.shields.io/badge/GitHub-181717.svg?style=flat&logo=GitHub&logoColor=white" alt="GitHub">
	<img src="https://img.shields.io/badge/Gradle-02303A.svg?style=flat&logo=Gradle&logoColor=white" alt="Gradle">
	<img src="https://img.shields.io/badge/JetBrains-000000.svg?style=flat&logo=JetBrains&logoColor=white" alt="JetBrains">
	<img src="https://img.shields.io/badge/java-%23ED8B00.svg?style=flat&logo=openjdk&logoColor=white" alt="java">
	<img src="https://img.shields.io/badge/Markdown-000000.svg?style=flat&logo=Markdown&logoColor=white" alt="Markdown">
</p>
<hr>

## 🔗 Quick Links
- [🔗 Quick Links](#-quick-links)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [🧩 Modules](#modules)
- [🚀 Getting Started](#-getting-started)
    - [⚙️ Installation](#-installation)
    - [🤖 Running file.io-Android-Client](#-running-file.io-Android-Client)
    - [🧪 Tests](#-tests)
- [🛠 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

The file.io-Android-Client project is an Android app that provides a convenient and secure way to share files with others. It allows users to easily upload files from their Android devices and generate shareable links. The app also supports downloading files shared through link access. With a simple and intuitive user interface, this project aims to streamline the file sharing process, making it efficient and hassle-free. Whether it's sharing documents, images, or any other file type, this app ensures that users can quickly share files with others while maintaining data privacy and security.

---

## 📦 Features

|    | Feature           | Description                                                                                                       |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**    | The codebase follows the Model-View-ViewModel (MVVM) architectural pattern.|
| 📄 | **Documentation**  | The codebase has limited documentation. It could benefit from more comprehensive documentation to improve understanding.|
| 🔗 | **Dependencies**   | The codebase relies on various external libraries, including Firebase, ConstraintLayout, CardView, and AndroidX.|
| 🧩 | **Modularity**     | The system is organized into smaller, interchangeable components, with separate modules for tests and Android-specific code.|
| 🧪 | **Testing**        | The codebase includes unit tests for some classes, but overall, the testing strategy could be improved with more comprehensive test coverage.|
| ⚡️ | **Performance**     | The performance of the system depends on external factors such as network speeds and file sizes. The codebase itself does not have significant performance optimizations.|
| 🔐 | **Security**       | The codebase does not explicitly address security measures, but it relies on external systems like Firebase for authentication and data protection.|
| 🔀 | **Version Control**| The codebase uses Git for version control.|
| 🔌 | **Integrations**   | The system integrates with Firebase for authentication and Firebase Cloud Storage for file storage.|
| 📶 | **Scalability**    | The system's scalability depends on external factors, such as the scalability of Firebase Cloud Storage. The codebase itself does not have explicit scalability measures.|

---

## 📂 Repository Structure

```sh
└── file.io-Android-Client/
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

## 🧩 Modules

<details closed><summary>.</summary>

| File                                                                                          | Summary                                                                                                                                                                                                                                                      |
| ---                                                                                           | ---                                                                                                                                                                                                                                                          |
| [build.gradle](https://github.com/rumaan/file.io-Android-Client/blob/main/build.gradle)       | The code snippet in the `build.gradle` file sets up the necessary dependencies and repositories for the Android client application in the `file.io` repository. It includes configurations for the Android build tools, Fabric, Google services, and Kotlin. |
| [settings.gradle](https://github.com/rumaan/file.io-Android-Client/blob/main/settings.gradle) | The code snippet is part of the file.io-Android-Client repository. It plays a key role in the architecture by including the:app file. The repository's layout consists of necessary directories and dependencies to enable the Android client functionality. |
| [.travis.yml](https://github.com/rumaan/file.io-Android-Client/blob/main/.travis.yml)         | This code snippet includes the configuration for the Android build process in the parent repository. It sets up the necessary dependencies and software, manages caching and licenses, and ensures compatibility with Android versions 26 and 27.            |

</details>

<details closed><summary>screenshots</summary>

| File                                                                                            | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---                                                                                             | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [readme.txt](https://github.com/rumaan/file.io-Android-Client/blob/main/screenshots/readme.txt) | The code snippet in the `app` directory of the `file.io-Android-Client` repository serves as the main Android client for accessing and interacting with the file.io platform. It includes build configurations, source code, and test files necessary for the functionality of the app. The codebase relies on various dependencies and software as documented in the `screenshots/readme.txt` file. Additionally, key files such as `readme.txt`, `screenshot.png`, and `todo-ui.png` provide further information and visual representations about the codebase. |

</details>

<details closed><summary>app</summary>

| File                                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---                                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [proguard-rules.pro](https://github.com/rumaan/file.io-Android-Client/blob/main/app/proguard-rules.pro) | This code snippet adds and configures ProGuard rules in the Android client of the file.io repository. It ensures proper obfuscation and exclusion of certain classes, while preserving necessary attributes for debugging and Crashlytics integration.                                                                                                                                                                                 |
| [build.gradle](https://github.com/rumaan/file.io-Android-Client/blob/main/app/build.gradle)             | This code snippet is part of an Android client for the file.io file-sharing service. It applies various plugins and dependencies, including permissions_dispatcher, Firebase Crashlytics, Room, Fuel, Gson, Kotlin, and more. Additionally, it configures build types and sets up necessary dependencies for testing. The code focuses on providing a smooth user experience and robust functionality for file sharing and management. |

</details>

<details closed><summary>app.src.androidTest.java.com.thecoolguy.rumaan.fileio</summary>

| File                                                                                                                                                                                      | Summary                                                                                                                                                                                                                                                                                                                     |
| ---                                                                                                                                                                                       | ---                                                                                                                                                                                                                                                                                                                         |
| [ExampleInstrumentedTest.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/androidTest/java/com/thecoolguy/rumaan/fileio/ExampleInstrumentedTest.kt)                 | This code snippet is an instrumented test that validates the context of the app under test. It uses the AndroidJUnit4 framework and asserts that the package name matches the expected value. The main role of this code in the repository's architecture is to ensure the correctness of the app's context during testing. |
| [FileEntityDaoTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/androidTest/java/com/thecoolguy/rumaan/fileio/FileEntityDaoTest.java)                         | This code snippet is a test suite for the RoomDatabase in the File.io Android Client repository. It tests the functionality of the FileEntityDao, such as counting rows, inserting and retrieving items, and saving multiple items. The tests ensure that the database operations are working correctly.                    |
| [UploadHistoryInstrumentedTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/androidTest/java/com/thecoolguy/rumaan/fileio/UploadHistoryInstrumentedTest.java) | This code snippet is an instrumented test for the UploadHistoryActivity in the File.io-Android-Client repository. It sets up the database, adds test data, and tests a long press action.                                                                                                                                   |

</details>

<details closed><summary>app.src.test.java.com.thecoolguy.rumaan.fileio</summary>

| File                                                                                                                                                             | Summary                                                                                                                                                                                                                                                                                                                        |
| ---                                                                                                                                                              | ---                                                                                                                                                                                                                                                                                                                            |
| [ExampleUnitTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/test/java/com/thecoolguy/rumaan/fileio/ExampleUnitTest.java)           | This code snippet contains a unit test file that checks if the addition operation is correct. It is part of an Android client repository for file.io service.                                                                                                                                                                  |
| [UploadRepositoryTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/test/java/com/thecoolguy/rumaan/fileio/UploadRepositoryTest.java) | This code snippet is a test file within the `UploadRepositoryTest` class, located in the `com.thecoolguy.rumaan.fileio` package. It verifies the functionality of the `getExpireUrl` method by comparing the expected URL with the actual URL. The test checks that the expiration parameter is correctly appended to the URL. |
| [UrlTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/test/java/com/thecoolguy/rumaan/fileio/UrlTest.java)                           | The code snippet in `UrlTest.java` tests the functionality of `URLParser` in the `Utils` class. It checks if the `parseEncryptUrl` method correctly extracts the base URL from an encrypted URL. The test asserts the expected output with the actual result.                                                                  |
| [FileEntityTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/test/java/com/thecoolguy/rumaan/fileio/FileEntityTest.java)             | This code snippet is a test file that verifies the functionality of the FileEntity class within the parent repository. It checks if the name and URL values are properly set and retrieved. The test ensures that the FileEntity object is functioning correctly.                                                              |

</details>

<details closed><summary>app.src.main.java.com.thecoolguy.rumaan.fileio.viewmodel</summary>

| File                                                                                                                                                                       | Summary                                                                                                                                                                                                                       |
| ---                                                                                                                                                                        | ---                                                                                                                                                                                                                           |
| [UploadHistoryViewModel.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/viewmodel/UploadHistoryViewModel.kt) | The code snippet is part of the `file.io-Android-Client` repository and is located in the `UploadHistoryViewModel` file. It defines a ViewModel class that retrieves and stores a list of file uploads using a Room database. |

</details>

<details closed><summary>app.src.main.java.com.thecoolguy.rumaan.fileio.ui</summary>

| File                                                                                                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---                                                                                                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                                                                         |
| [FileioApplication.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/FileioApplication.kt)               | This code snippet is a key file in the repository's architecture. It initializes the application and handles logging and error handling. It uses libraries like Timber and Custom Activity on Crash. The code sets up logging and configures a custom error activity for crashes.                                                                                                                           |
| [UploadHistoryListAdapter.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/UploadHistoryListAdapter.kt) | The `UploadHistoryListAdapter` is a key file in the `file.io-Android-Client` repository. It handles the UI and data binding for displaying a list of uploaded files in a RecyclerView. It uses different view types to display dates and file details, and handles user interactions such as copying file URLs to the clipboard and showing toast messages.                                                 |
| [SwipeToDeleteCallBack.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/SwipeToDeleteCallBack.kt)       | The `SwipeToDeleteCallBack` class is a key file in the `com.thecoolguy.rumaan.fileio.ui` package. It provides functionality to enable swiping and deleting items in a RecyclerView. It handles the drawing of the delete icon and the red background, as well as the logic for canceling the swipe action.                                                                                                  |
| [NotificationHelper.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/NotificationHelper.kt)             | The code snippet is a NotificationHelper class that creates and displays a notification for a successful file upload. It sets the notification's content, icon, and behavior, and also handles the creation of a notification channel for devices running Android O and above. The main role of this code is to provide a convenient way to generate and display notifications for file uploads in the app. |

</details>

<details closed><summary>app.src.main.java.com.thecoolguy.rumaan.fileio.ui.fragments</summary>

| File                                                                                                                                                                            | Summary                                                                                                                                                                                                                                                                                                                                                                        |
| ---                                                                                                                                                                             | ---                                                                                                                                                                                                                                                                                                                                                                            |
| [NoNetworkDialogFragment.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/NoNetworkDialogFragment.kt) | The code snippet is a Kotlin class file named NoNetworkDialogFragment.kt within the com.thecoolguy.rumaan.fileio.ui.fragments package. It creates a dialog fragment that displays an AlertDialog when there is no network connection. It includes a button that triggers a callback to the parent activity when clicked.                                                       |
| [HomeFragment.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/HomeFragment.kt)                       | The `HomeFragment` class is part of the `file.io-Android-Client` repository. It represents a UI fragment for displaying the main layout of the app and handles user interactions. It has a callback for choosing a file and storing it in the local file object cache. The fragment communicates with its parent activity using the `OnFragmentInteractionListener` interface. |
| [ResultFragment.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/ResultFragment.kt)                   | This code snippet is a key file within the ResultFragment package of the Android client app. It handles the logic and UI for displaying the result of a file upload, including the URL and expiration days. Users can copy the link to the clipboard and mark the task as done.                                                                                                |

</details>

<details closed><summary>app.src.main.java.com.thecoolguy.rumaan.fileio.ui.activities</summary>

| File                                                                                                                                                                         | Summary                                                                                                                                                                                                                                                                                                                                                               |
| ---                                                                                                                                                                          | ---                                                                                                                                                                                                                                                                                                                                                                   |
| [MainActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/MainActivity.kt)                   | The code snippet represents the MainActivity file in the file.io-Android-Client repository. It handles various activities and fragments, including file uploads, displaying results, and handling permissions.                                                                                                                                                        |
| [ErrorActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/ErrorActivity.kt)                 | This code snippet represents the ErrorActivity class within the Android client of the file.io project. It is responsible for displaying an error screen in case of runtime crashes and allows users to exit the app. Its main features include handling the back button press and setting the error view layout.                                                      |
| [UploadHistoryActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/UploadHistoryActivity.kt) | This code snippet represents the `UploadHistoryActivity` file in the `file.io-Android-Client` repository. It is responsible for displaying and managing the upload history in the app, including clearing the history and deleting individual items. It uses various components like RecyclerView, ViewModel, WorkManager, and Snackbar for a smooth user experience. |
| [AboutActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/AboutActivity.kt)                 | The code snippet is a key file in the repository's architecture. It defines the behavior of the About screen in the Android app, including menu options and navigation to the License screen.                                                                                                                                                                         |
| [LicenseActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/LicenseActivity.kt)             | This code snippet is responsible for displaying a list of open source licenses in the LicenseActivity of the Android app. It uses MaterialAboutLibrary to create license cards for various libraries used in the app, including AOSP Support Libraries, Architecture Components, Fuel, and more.                                                                      |

</details>

<details closed><summary>app.src.main.java.com.thecoolguy.rumaan.fileio.repository</summary>

| File                                                                                                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---                                                                                                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [UploadHistoryWorkers.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/repository/UploadHistoryWorkers.kt) | This code snippet contains two worker classes (`ClearHistoryWorker` and `DeleteSingleItemWorker`) that handle clearing and deleting items from the upload history database in the parent Android client repository. The workers are responsible for interacting with the `UploadHistoryRoomDatabase` and performing the necessary operations for clearing all items or deleting a single item based on the provided ID. |
| [UploadWorker.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/repository/UploadWorker.kt)                 | The `UploadWorker.kt` file in the `com.thecoolguy.rumaan.fileio.repository` package is responsible for uploading files to a server using Fuel library and WorkManager. It handles file uploads, saves the upload history to a database, and sends a notification about the upload progress.                                                                                                                             |

</details>

<details closed><summary>app.src.main.java.com.thecoolguy.rumaan.fileio.utils</summary>

| File                                                                                                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                    |
| ---                                                                                                                                                                        | ---                                                                                                                                                                                                                                                                                                                                        |
| [Extensions.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Extensions.kt)                             | The code snippet in the `Extensions.kt` file provides utility functions to display toast messages and toggle the clickable state of a view in an Android application. These functions enhance user interaction and provide feedback.                                                                                                       |
| [WorkManagerHelper.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/WorkManagerHelper.kt)               | This code snippet in the file `WorkManagerHelper.kt` is responsible for creating and configuring an upload work request using the Android WorkManager library. The request includes constraints for network connectivity and data input. The request is associated with the `UploadWorker` class and is tagged with the `UPLOAD_WORK_TAG`. |
| [Utils.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Utils.kt)                                       | This code snippet provides a set of helper methods for various tasks such as retrieving file details, opening files, checking network connectivity, showing dialogs, copying text to clipboard, and parsing URLs and JSON. It is part of the Android client for the file.io repository and enhances the app's functionality.               |
| [Helpers.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Helpers.kt)                                   | This code snippet contains helper functions that retrieve file metadata, get file details, and compose a FileEntity object. These functions are used in the Android Client repository to handle file operations and data manipulation.                                                                                                     |
| [FragmentHelperExtensions.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/FragmentHelperExtensions.kt) | This code snippet provides utility functions for adding and replacing fragments in an Android app. It helps manage the view hierarchy and transitions between fragments, enhancing the user experience.                                                                                                                                    |
| [MaterialIn.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/MaterialIn.kt)                             | The code snippet in the `MaterialIn.kt` file is part of the `file.io-Android-Client` repository. It provides a utility function to animate views using material design principles, including fading and sliding effects. The code determines the animation direction based on gravity and implements the animation using `ObjectAnimator`. |
| [Constants.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Constants.kt)                               | This code snippet provides global constants for the Android client of the file.io repository. It includes base URLs, expiration parameters, default values, and timestamp formats. It also defines GitHub and Twitter URLs and an email address. The snippet is located in the `utils` package.                                            |

</details>

<details closed><summary>app.src.main.java.com.thecoolguy.rumaan.fileio.listeners</summary>

| File                                                                                                                                                                                     | Summary                                                                                                                                                                                                                                                                                                |
| ---                                                                                                                                                                                      | ---                                                                                                                                                                                                                                                                                                    |
| [DialogClickListener.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/listeners/DialogClickListener.kt)                     | This code snippet defines an interface called DialogClickListener in the listeners package. It provides a method for handling positive button clicks in a dialog. Its purpose is to enable communication between dialogs and fragments in the file.io-Android-Client repository.                       |
| [OnFragmentInteractionListener.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/listeners/OnFragmentInteractionListener.kt) | This code snippet, located in the `com.thecoolguy.rumaan.fileio.listeners` package, defines an interface called `OnFragmentInteractionListener`. It has two functions: `onUploadFileClick()` and `onDone()`. This interface is part of the larger Android Client codebase for the File.io application. |

</details>

---

## 🚀 Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* Kotlin: `► INSERT-VERSION-HERE`
* `► ...`
* `► ...`

### ⚙️ Installation

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

### 🤖 Running file.io-Android-Client
Use the following command to run file.io-Android-Client:
```sh
java -jar build/libs/myapp.jar
```

### 🧪 Tests
To execute tests, run:
```sh
gradle test
```

---

## 🛠 Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

---

## 🤝 Contributing

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

## 📄 License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 👏 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-quick-links)

---
