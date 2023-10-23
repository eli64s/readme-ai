<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>FILE.IO-ANDROID-CLIENT</h1>
<h3>◦ Share files effortlessly on the go with file.io!</h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat-square&logo=YAML&logoColor=white" alt="YAML" />
<img src="https://img.shields.io/badge/Kotlin-7F52FF.svg?style=flat-square&logo=Kotlin&logoColor=white" alt="Kotlin" />
<img src="https://img.shields.io/badge/Gradle-02303A.svg?style=flat-square&logo=Gradle&logoColor=white" alt="Gradle" />
<img src="https://img.shields.io/badge/java-%23ED8B00.svg?style=flat-square&logo=openjdk&logoColor=white" alt="java" />
</p>
<img src="https://img.shields.io/github/license/rumaan/file.io-Android-Client?style=flat-square&color=5D6D7E" alt="GitHub license" />
<img src="https://img.shields.io/github/last-commit/rumaan/file.io-Android-Client?style=flat-square&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/rumaan/file.io-Android-Client?style=flat-square&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/languages/top/rumaan/file.io-Android-Client?style=flat-square&color=5D6D7E" alt="GitHub top language" />
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
    - [🤖 Running file.io-Android-Client](#-running-file.io-Android-Client)
    - [🧪 Tests](#-tests)
- [🛣 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The file.io-Android-Client repository is a project that provides an Android client for the file.io service. It allows users to easily upload and share files with others, providing a convenient way to transfer large files securely. The application is built using the Android development framework and includes features such as file selection, progress tracking, and sharing options. Overall, this project offers a user-friendly and efficient solution for file sharing on Android devices.

---

## 📦 Features

|    | Feature            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|----|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The codebase follows the Model-View-ViewModel (MVVM) architectural pattern. The UI layer is separated from the business logic and data layer, improving testability and maintainability. The LiveData and ViewModel components from the Android Architecture Components are used for data binding and lifecycle management.                                                                                                                                                                                |
| 📄 | **Documentation**  | The documentation in the repository is limited. There is a `readme.txt` file inside the `screenshots` directory, but it does not provide comprehensive information about the project or its components. Additional documentation or code comments are recommended to improve understanding and ease of maintenance for developers.                                                                                                                                                  |
| 🔗 | **Dependencies**   | The project relies on various external libraries and dependencies. Some notable ones include Kotlin, Kotlin Gradle Plugin, Android Architecture Components (LiveData, ViewModel, Navigation), Kotlin Reflection, and Travis CI for continuous integration. These libraries enhance development speed, offer architectural guidance, and provide tooling and testability improvements.                                                                                                                                                                           |
| 🧩 | **Modularity**     | The codebase is organized into several packages, each representing a specific functionality or feature. This promotes modularity, making it easier to understand and maintain the code. The project uses the Single-Activity Architecture, where fragments handle different screens and navigation is facilitated by the Navigation component. These modular components enable easy extensibility and separation of concerns.                                                                   |
| 🧪 | **Testing**        | The project includes both unit tests and instrumented tests. However, there is room for improvement in terms of code coverage. The AndroidX testing libraries, such as Espresso and JUnit, are utilized for UI and unit testing. The project could benefit from additional tests for edge cases and integration tests to ensure the correctness and reliability of the application.                                                                                                                                 |
| ⚡️  | **Performance**    | The performance of the system appears to be acceptable. However, without detailed profiling and benchmarking, it is challenging to provide specific insights regarding speed, efficiency, and resource usage. Optimization efforts, such as reducing memory allocations and applying caching strategies, can further enhance performance. Monitoring and analyzing real-world usage metrics would provide a more accurate understanding of performance.                                                                 |
| 🔐 | **Security**       | The codebase demonstrates some security measures. It includes proguard-rules to obfuscate the code during the release build. However, a more thorough analysis would be needed to evaluate if other security best practices are followed, such as using secure network protocols (HTTPS), data encryption in transit and at rest, input validation, and proper handling of sensitive user information. Implementing security code reviews and periodic vulnerability assessments would strengthen security measures.                                         |
| 🔀 | **Version Control**| The version control system used is Git, and the repository is hosted on GitHub. The commit history indicates regular commits and updates, implying a version control workflow is in place. However, the usage of branching, pull requests, and code reviews, as well as any code formatting or linting checks, would shed more light on the effectiveness of version control strategies and tools used in the project.                                                                                         |
| 🔌 | **Integrations**   | The project does not have explicit integrations with other systems or services mentioned in the provided repository. However, through

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


## ⚙️ Modules

<details closed><summary>Root</summary>

| File                                                                                          | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---                                                                                           | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [build.gradle](https://github.com/rumaan/file.io-Android-Client/blob/main/build.gradle)       | The code in the build.gradle file sets the configuration for Gradle, the build automation tool. It specifies the dependencies needed for the Android app development, including the Android build tools, Fabric for crash reporting, Google Services, and the Kotlin language. It also adds repositories to resolve these dependencies, such as Google, JCenter, and JitPack. The "allprojects" block specifies the repositories for all projects within the directory tree. |
| [settings.gradle](https://github.com/rumaan/file.io-Android-Client/blob/main/settings.gradle) | The code in the settings.gradle file includes the app module in the project directory tree structure. This allows the app module to be built and treated as a part of the overall project.                                                                                                                                                                                                                                                                                   |
| [.travis.yml](https://github.com/rumaan/file.io-Android-Client/blob/main/.travis.yml)         | This code is a configuration file for Travis CI, a continuous integration platform. It specifies the language, JDK version, and Android components required for building the project. It also sets up caching for Gradle to improve build speed.                                                                                                                                                                                                                             |

</details>

<details closed><summary>Screenshots</summary>

| File                                                                                            | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---                                                                                             | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [readme.txt](https://github.com/rumaan/file.io-Android-Client/blob/main/screenshots/readme.txt) | The code represents a directory tree with several files and folders. In the "file.io-Android-Client" directory, there are subdirectories such as "app" and "gradle". The "app" directory contains files related to building an Android app, including the source code and build configurations. The "gradle" directory contains wrapper files for the Gradle build system. The "screenshots" directory includes a "readme.txt" file and two image files, "screenshot.png" and "todo-ui.png". |

</details>

<details closed><summary>App</summary>

| File                                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---                                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [proguard-rules.pro](https://github.com/rumaan/file.io-Android-Client/blob/main/app/proguard-rules.pro) | The given code is a ProGuard configuration file for an Android app. It specifies rules for code obfuscation and optimization. It disables warnings for specific packages, keeps attributes related to annotations, source files, and line numbers, and preserves specific class and package names. It also includes rules for Crashlytics integration, such as keeping all classes in the "com.crashlytics" package. |
| [build.gradle](https://github.com/rumaan/file.io-Android-Client/blob/main/app/build.gradle)             | This code is for an Android application. It configures various plugins and dependencies for the app's build process. It specifies the application ID, version, and build type settings. It includes libraries for UI components, testing, permission handling, crash reporting, networking, data persistence, navigation, and logging. It applies plugins for Fabric, Kotlin, and Google Play services.              |

</details>

<details closed><summary>Fileio</summary>

| File                                                                                                                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---                                                                                                                                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [ExampleInstrumentedTest.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/androidTest/java/com/thecoolguy/rumaan/fileio/ExampleInstrumentedTest.kt)                 | This code is a sample instrumented test written in Kotlin for an Android application. It uses the AndroidJUnit4 test runner and the InstrumentationRegistry to get the context of the app being tested. The test checks if the package name of the app under test is equal to "com.thecoolguy.rumaan.fileio". It is executed on an Android device and is considered a small test.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [FileEntityDaoTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/androidTest/java/com/thecoolguy/rumaan/fileio/FileEntityDaoTest.java)                         | The code above is a test file for a RoomDatabase in an Android app. It contains three test methods:1. `check_CountTheRows()`: This method checks the number of rows in the database. It initializes an in-memory database and verifies that the initial count is zero. It then inserts a new item into the database and checks that the count increases by one.2. `check_InsertUploadItemSaves()`: This method checks if inserting an upload item into the database and retrieving it works correctly. It creates a new `FileEntity`, inserts it into the database, and then retrieves it using its generated ID.3. `check_saveMultipleItemsRetrieves()`: This method checks if saving multiple items and retrieving them works correctly. It creates multiple `FileEntity` objects, inserts them into the database, and then checks if the count and the retrieved items match the expected values.These tests ensure the proper functioning of the database and its operations. |
| [UploadHistoryInstrumentedTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/androidTest/java/com/thecoolguy/rumaan/fileio/UploadHistoryInstrumentedTest.java) | The code represents an instrumented test for the Upload History feature of an Android app. It sets up the necessary dependencies such as the UploadHistoryRoomDatabase, defines a matcher for file names, and initializes the test by adding five items to the database. The test itself is for long-pressing an item to delete it, but the implementation for the test case is not included in the code snippet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [ExampleUnitTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/test/java/com/thecoolguy/rumaan/fileio/ExampleUnitTest.java)                                    | The code is an example unit test for an Android application. It tests the correctness of the addition operation. The test asserts that the sum of 2 + 2 should be equal to 4.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [UploadRepositoryTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/test/java/com/thecoolguy/rumaan/fileio/UploadRepositoryTest.java)                          | The code above is a JUnit test case for the UploadRepository class in the file.io-Android-Client project. It tests the functionality of the getExpireUrl() method in the URLParser class. The test checks if the generated URL matches the expected URL. It also checks if the generated URL matches a URL built using constants from the ConstantsKt class.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [UrlTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/test/java/com/thecoolguy/rumaan/fileio/UrlTest.java)                                                    | The code is a unit test for a URL parsing method in a file.io Android client app. It verifies the behavior of the method URLParser.parseEncryptUrl() by comparing the output against an expected URL. If the output matches the expected URL, the test passes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [FileEntityTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/test/java/com/thecoolguy/rumaan/fileio/FileEntityTest.java)                                      | The code above is a test case written in Java that checks the functionality of the FileEntity class in the file.io Android client. In this test, the code sets values for the name and URL attributes of the FileEntity object, and then checks if the values are correctly set. The test passes if the values are not null and if they match the expected values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

</details>

<details closed><summary>Viewmodel</summary>

| File                                                                                                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                                                                               |
| ---                                                                                                                                                                        | ---                                                                                                                                                                                                                                                                                                                                                                                                   |
| [UploadHistoryViewModel.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/viewmodel/UploadHistoryViewModel.kt) | The code defines a ViewModel class called UploadHistoryViewModel, which extends AndroidViewModel. It initializes a LiveData object called uploadList, which holds a list of FileEntity objects. The uploadList is populated with data from a Room database through the UploadHistoryRoomDatabase class. The ViewModel is responsible for managing data for the UI and survives configuration changes. |

</details>

<details closed><summary>Ui</summary>

| File                                                                                                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---                                                                                                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [FileioApplication.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/FileioApplication.kt)               | The code is a Kotlin class named "FileioApplication" that extends the "Application" class. It initializes the Timber logging library to be used for logging debug messages. It also configures the Custom Activity on Crash library, specifying that the "ErrorActivity" class should be launched in case of a crash.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [UploadHistoryListAdapter.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/UploadHistoryListAdapter.kt) | The code above defines an UploadHistoryListAdapter class in an Android application. It is responsible for managing and displaying a list of uploaded files in a RecyclerView. The adapter has methods to update and display the list, as well as handle user interactions with the items. It also includes two inner ViewHolder classes for different types of item views in the list.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [SwipeToDeleteCallBack.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/SwipeToDeleteCallBack.kt)       | The code above is an implementation of a SwipeToDeleteCallBack for a RecyclerView in an Android app. The callback handles swiping left to delete an item in the RecyclerView. It provides a red background with a delete icon on the right side of the swiped item. The callback also disables swiping for a specific view type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [NotificationHelper.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/NotificationHelper.kt)             | The provided code is a Kotlin class called "NotificationHelper", which is responsible for creating and displaying notifications in an Android application. It allows the app to show a notification when a file upload is successful. The class includes a method, "create", that takes a Context and a FileEntity object as parameters. It creates an intent to open the UploadHistoryActivity, sets some data into the intent, and creates a pending intent with the intent. Then, using NotificationCompat.Builder, it configures the notification with various properties such as icon, title, text, sound, priority, and others. If the device's API level is Oreo or higher, it also creates a notification channel to handle the notification. Finally, it uses NotificationManagerCompat to post the notification. |

</details>

<details closed><summary>Fragments</summary>

| File                                                                                                                                                                            | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---                                                                                                                                                                             | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [NoNetworkDialogFragment.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/NoNetworkDialogFragment.kt) | This code defines a Dialog Fragment class called NoNetworkDialogFragment. It extends the androidx.fragment.app.DialogFragment class and implements the View.OnClickListener interface. This class displays a dialog to the user when there is no network connection. The dialog is created using an AlertDialog and a custom layout file. It also includes a callback listener interface, DialogClickListener, to handle button clicks in the dialog. The dialog is shown to the user when the onCreateDialog() method is called, and the onClick() method is called when the user clicks the "ok" button in the dialog. |
| [HomeFragment.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/HomeFragment.kt)                       | The code above represents the HomeFragment class in an Android app. This class is responsible for displaying a layout and handling user interactions within the home screen of the app. It inflates a layout file, sets up a button click listener, and communicates with other components through an interface. The HomeFragment class also has lifecycle methods for attaching and detaching from the parent activity.                                                                                                                                                                                                 |
| [ResultFragment.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/ResultFragment.kt)                   | This code defines a ResultFragment class in an Android app. The fragment displays the result of a file operation. It receives a URL and a number of days as parameters, which it uses to populate and update the UI elements. The fragment also handles user interactions with the UI, such as copying the URL to the clipboard and showing a toast message.                                                                                                                                                                                                                                                             |

</details>

<details closed><summary>Activities</summary>

| File                                                                                                                                                                         | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---                                                                                                                                                                          | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [MainActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/MainActivity.kt)                   | The code above is the implementation of the `MainActivity` class in an Android app. This class represents the main activity of the app, which is responsible for displaying the UI and handling user interactions. The key functionalities of this code include:-Handling menu options for the activity, such as navigating to the upload history and about screens.-Setting up and managing background upload tasks using the WorkManager API.-Handling user interactions, such as choosing a file to upload and showing the result of the upload.-Handling runtime permissions for accessing external storage.-Handling back button presses and managing the fragment stack.-Implementing interfaces for various dialogs and click events.These functionalities contribute to the overall user experience of the app, allowing users to upload files, view upload history, and access other app screens in a seamless manner. |
| [ErrorActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/ErrorActivity.kt)                 | The code is for an Android app's ErrorActivity class. It extends AppCompatActivity and handles runtime crashes. The onBackPressed() function finishes all activities in the app's task stack and the onCreate() function sets the layout for the error activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [UploadHistoryActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/UploadHistoryActivity.kt) | This code is for an Android application that manages the upload history of files. It includes functionalities such as displaying the upload history, clearing the upload history, and removing individual items from the history. It also implements swipe-to-delete functionality for removing items. The code uses WorkManager for background processing and LiveData for observing changes in the upload history. The UI is updated dynamically based on the upload history data.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [AboutActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/AboutActivity.kt)                 | The code above is an implementation of an activity called "AboutActivity" in an Android app. It inflates a menu with an option for "Open Source", and when selected, it starts the "LicenseActivity". The activity sets a transparent navigation theme, sets the layout using "activity_about.xml", and displays a toolbar with a back arrow button.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [LicenseActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/LicenseActivity.kt)             | The code represents an Android activity that displays a list of open source licenses. The list is created using the MaterialAboutLibrary and includes various licenses such as AOSP Support Libraries, Architecture Components, MaterialAboutLibrary, Fuel, NumberProgressBar, Permission Dispatcher, and CustomActivityOnCrash. Each license is displayed in a card format with relevant information such as the creator, year, and license type. The activity is titled "Open Source Licenses" and the list is populated with icons representing each license.                                                                                                                                                                                                                                                                                                                                                                |

</details>

<details closed><summary>Repository</summary>

| File                                                                                                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---                                                                                                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [UploadHistoryWorkers.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/repository/UploadHistoryWorkers.kt) | The code consists of two worker classes, "ClearHistoryWorker" and "DeleteSingleItemWorker", within the "com.thecoolguy.rumaan.fileio.repository" package. These workers perform database operations using Room, an ORM library for Android. "ClearHistoryWorker" clears all upload history items from the database, while "DeleteSingleItemWorker" deletes a specific item based on an ID passed to it. Both workers extend the Worker class from the AndroidX WorkManager library and are executed asynchronously.                                                                  |
| [UploadWorker.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/repository/UploadWorker.kt)                 | The code is an implementation of a `Worker` class in an Android app for uploading a file to the `https://file.io` server. The code takes a file URI as an input, opens an input stream for the file, and uses the Fuel HTTP library to upload the file to the server. It also tracks the progress of the upload and handles the server response. Upon successful upload, the code saves the file details to a local database, sends a notification about the upload, and returns a success result. If any errors occur during the upload process, the code returns a failure result. |

</details>

<details closed><summary>Utils</summary>

| File                                                                                                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---                                                                                                                                                                        | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Extensions.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Extensions.kt)                             | The code provides two extension functions for Android views. The `toast` function displays a toast message with the provided string on a given context. The `toggleClickable` function toggles the clickability of a view based on the provided boolean value.                                                                                                                                                                                                                                                                                                                |
| [WorkManagerHelper.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/WorkManagerHelper.kt)               | The code is a Kotlin file named "WorkManagerHelper" located in the "utils" package of an Android client app. It contains a function called "createUploadWork" that creates and configures a OneTimeWorkRequest object for uploading a file. The function takes a parameter "uri" (String) that represents the file's URI. It sets constraints to require a connected network for the upload and adds the URI as input data to the request. The request is tagged with "UploadWork" and returned.                                                                              |
| [Utils.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Utils.kt)                                       | The code provided is a Kotlin file that contains a collection of helper methods for various functionalities. It includes methods for retrieving file details from the Android Provider Database, opening and reading files, checking network connectivity, showing dialogs, dismissing dialogs, opening app settings, copying text to clipboard, parsing file.io URLs, parsing JSON responses, and working with dates. These methods are organized into three wrapper classes: Utils.Android, Utils.URLParser, and Utils.JSONParser.                                          |
| [Helpers.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Helpers.kt)                                   | The code defines utility functions in the Helpers.kt file for file-related operations. 1. getFileMetaData function retrieves file metadata such as name and size from a file URI.2. getFile function retrieves file details such as name and size from a file URI and returns a File object.3. composeIntoFileEntity function takes a File object and a Response object and creates a FileEntity object with the file name, URI, creation date, and expiration days.These functions can be used to handle file operations and create file entities in an Android application. |
| [FragmentHelperExtensions.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/FragmentHelperExtensions.kt) | The code provides extension functions for the `FragmentManager` class in the Android app. The `addFragment` function adds a fragment to a container with an optional tag and transition animation. The `replaceFragment` function replaces an existing fragment in a container with a new fragment, also supporting optional tag and transition animation.                                                                                                                                                                                                                    |
| [MaterialIn.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/MaterialIn.kt)                             | The code provides a set of utility functions in the MaterialIn object for animating views in an Android app. It allows for animating views in different directions (e.g., from bottom, top, left, right) using fade and slide animations. The `animate` function is used to initiate the animation, while the `startAnimators` function handles the actual animation by setting the necessary properties and starting the animation. The `convertGravity` function is used to handle RTL (Right-to-Left) layout direction and adjust the gravity accordingly.                 |
| [Constants.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Constants.kt)                               | This code defines global constants for the file.io-Android-Client app. It includes a base URL, expiration parameters, query strings, default expiration length, URLs for GitHub and Twitter, an email address, a postfix to append to links, and a timestamp format. These constants are used throughout the app for various functionalities.                                                                                                                                                                                                                                 |

</details>

<details closed><summary>Listeners</summary>

| File                                                                                                                                                                                     | Summary                                                                                                                                                                                                                                                                                                                               |
| ---                                                                                                                                                                                      | ---                                                                                                                                                                                                                                                                                                                                   |
| [DialogClickListener.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/listeners/DialogClickListener.kt)                     | This code defines an interface called "DialogClickListener" with a single method called "onDialogPositiveClick". This method takes in two parameters-a Dialog object and a androidx.fragment.app.Fragment object. This interface is intended to be implemented by classes that need to handle positive click events in dialogs.       |
| [OnFragmentInteractionListener.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/listeners/OnFragmentInteractionListener.kt) | This code defines an interface called OnFragmentInteractionListener in the package "com.thecoolguy.rumaan.fileio.listeners". It has two functions: onUploadFileClick() and onDone(). These functions are used to handle user interactions within a fragment, specifically when uploading a file and when the interaction is complete. |

</details>

---

## 🚀 Getting Started

***Dependencies***

Please ensure you have the following dependencies installed on your system:

`- ℹ️ Dependency 1`

`- ℹ️ Dependency 2`

`- ℹ️ ...`

### 🔧 Installation

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

```sh
java -jar build/libs/myapp.jar
```

### 🧪 Tests
```sh
gradle test
```

---


## 🛣 Project Roadmap

> - [X] `ℹ️  Task 1: Implement X`
> - [ ] `ℹ️  Task 2: Implement Y`
> - [ ] `ℹ️ ...`


---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/rumaan/file.io-Android-Client/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/rumaan/file.io-Android-Client/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/rumaan/file.io-Android-Client/issues)**: Submit bugs found or log feature requests for RUMAAN.

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
