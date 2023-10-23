<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>FILE.IO-ANDROID-CLIENT</h1>
<h3>◦ Unleash the power of file.io on your Android!</h3>
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
- [📂 Repository Structure](#-repository-structure)
- [⚙️ Modules](#️-modules)
- [🚀 Getting Started](#-getting-started)
  - [🔧 Installation](#-installation)
  - [🤖 Running file.io-Android-Client](#-running-fileio-android-client)
  - [🧪 Tests](#-tests)
- [🛣 Project Roadmap](#-project-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The repository is an Android client for the file.io file-sharing service. It allows users to easily upload, download, and manage files on their Android devices. The project provides a user-friendly interface and utilizes the file.io API to handle file transfers securely. This client app simplifies the process of sharing files between devices and offers a convenient solution for managing file uploads and downloads on Android.

---

## 📦 Features

|    | Feature            | Description                                                                                                        |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The codebase follows the Model-View-ViewModel (MVVM) architectural pattern. It separates the user interface (View) from the business logic (ViewModel) and data (Model) using reactive programming principles.|
| 📄 | **Documentation**  | The repository lacks comprehensive documentation. There is a `readme.txt` file in the `screenshots` directory, but it may not provide sufficient guidance for understanding the codebase. More documentation would improve code comprehension and onboarding.|
| 🔗 | **Dependencies**   | The repository has a dependency on `permissionsdispatcher` for handling runtime permissions and `navigation-fragment-ktx` for navigation. Other dependencies include `androidx` libraries for UI components, `work-runtime-ktx` for scheduling background tasks, and `gradle` for build automation.|
| 🧩 | **Modularity**     | The codebase is modular with clear separation of concerns. It is organized into different packages for activities, fragments, adapters, view models, and utilities. This modular design enhances code maintainability and reusability.|
| 🧪 | **Testing**        | There are some test files present in the repository, such as `UploadHistoryInstrumentedTest.java` and `ExampleInstrumentedTest.kt`. However, the test coverage is limited, and more comprehensive testing strategies and tools, such as unit testing and test automation frameworks, would benefit the codebase.|
| ⚡️  | **Performance**    | Performance analysis is difficult based on the information provided. It would require profiling and benchmarking to evaluate the codebase's performance in terms of speed, efficiency, and resource usage.|
| 🔐 | **Security**       | The codebase doesn't have explicit security measures implemented. Secure coding practices like input validation, data encryption, and secure network communication should be considered to protect user data and maintain system functionality.|
| 🔀 | **Version Control**| The repository is hosted on GitHub and utilizes Git for version control. The presence of a `.travis.yml` file suggests possible integration with continuous integration tools like Travis CI.|
| 🔌 | **Integrations**   | The codebase doesn't have direct integrations with other systems or services. However, it may interact with backend APIs to upload and retrieve files. Integration with cloud storage providers or authentication systems would enhance its functionality.|
| 📶 | **Scalability**    | The codebase's scalability is hard to determine without further information. It would depend on factors such as the backend infrastructure and the ability to handle increased user load. Proper design and scalable architecture can support future growth.|

---


## 📂 Repository Structure

```sh
└── ./
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

| File                                                                                          | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---                                                                                           | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [build.gradle](https://github.com/rumaan/file.io-Android-Client/blob/main/build.gradle)       | The code above sets up the build configuration for an Android project using Gradle. It specifies the dependencies, repositories, and plugins required for the project. It includes configurations for Kotlin, Google Services, Fabric, and other necessary libraries. It also defines the repositories from which the project will retrieve the necessary dependencies.                                                                                 |
| [settings.gradle](https://github.com/rumaan/file.io-Android-Client/blob/main/settings.gradle) | The code in the settings.gradle file includes the app module in the project's build.                                                                                                                                                                                                                                                                                                                                                                    |
| [.travis.yml](https://github.com/rumaan/file.io-Android-Client/blob/main/.travis.yml)         | This code sets up the necessary components and configurations for building an Android app using Travis CI. It specifies the Java Development Kit, the Android components required, and the licenses needed. It also includes commands to be executed before the build, such as setting permissions and installing Android platform versions. Additionally, it sets up caching to speed up the build process by storing Gradle and Android build caches. |

</details>

<details closed><summary>Screenshots</summary>

| File                                                                                            | Summary                                                                                                                                                                                      |
| ---                                                                                             | ---                                                                                                                                                                                          |
| [readme.txt](https://github.com/rumaan/file.io-Android-Client/blob/main/screenshots/readme.txt) | The code represents a directory tree with various files and folders. The "screenshots/readme.txt" file contains a list of files including "readme.txt", "screenshot.png", and "todo-ui.png". |

</details>

<details closed><summary>App</summary>

| File                                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ---                                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [proguard-rules.pro](https://github.com/rumaan/file.io-Android-Client/blob/main/app/proguard-rules.pro) | The code in the "proguard-rules.pro" file is used to configure ProGuard, a tool used in Android development to optimize, obfuscate, and shrink the size of the code. It contains rules to keep specific classes and attributes, ignore warnings for certain packages, and preserve line number and source file information for debugging. Additionally, it includes rules for keeping classes related to Crashlytics, a crash reporting tool.                                                                                                                                                                                                                                  |
| [build.gradle](https://github.com/rumaan/file.io-Android-Client/blob/main/app/build.gradle)             | This code is for an Android application's build.gradle file. It includes plugins for Android application, fabric, Kotlin, and Kotlin kapt. It sets up the Android version, application ID, min and target SDK versions, and version code and name. It also configures build types for release and debug versions. The dependencies include various Android libraries, test dependencies, permission dispatcher, Firebase Crashlytics, Room, custom activity on crash, Fuel android service, Gson Deserializer, Kotlin reflection, Work Manager, Material About Library, Navigation components, and Timber for logging. The code ends with applying the google services plugin. |

</details>

<details closed><summary>Fileio</summary>

| File                                                                                                                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---                                                                                                                                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [ExampleInstrumentedTest.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/androidTest/java/com/thecoolguy/rumaan/fileio/ExampleInstrumentedTest.kt)                 | The code is an Instrumented Test written in Kotlin for an Android app. It uses the AndroidJUnit4 test runner and the ActivityTestRule class to test the MainActivity class of the app. The test asserts that the app's package name is "com.thecoolguy.rumaan.fileio". The purpose of this test is to ensure that the app's context is correctly set.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [FileEntityDaoTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/androidTest/java/com/thecoolguy/rumaan/fileio/FileEntityDaoTest.java)                         | The code provided is a test class called "FileEntityDaoTest". It tests the functionality of a RoomDatabase, specifically the "FileEntityDao" class. The test class contains three test methods:1. "check_CountTheRows" method checks if the number of rows in the upload item database is accurate. It initially asserts that the count is 0. Then, it creates a FileEntity object, inserts it into the database, and asserts that the count is now 1.2. "check_InsertUploadItemSaves" method checks if inserting an upload item into the database is successful. It creates a FileEntity object and asserts that it is not null. It also asserts that the name and URL of the FileEntity object match the expected values. It then inserts the object into the database and asserts that it returns a valid ID upon insertion.3. "check_saveMultipleItemsRetrieves" method checks if saving multiple upload items and retrieving them from the database is successful. It creates a list of FileEntity objects and adds multiple objects to it. It then inserts all the objects into the database using a forEach loop. It asserts that the number of items in the database matches the expected count. It also retrieves all the upload items from the database and asserts that the list is not null and matches the original list of objects. |
| [UploadHistoryInstrumentedTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/androidTest/java/com/thecoolguy/rumaan/fileio/UploadHistoryInstrumentedTest.java) | The provided code is an Android Instrumented Test for the UploadHistoryActivity class. It initializes a Room database, adds five sample items to the database, and defines a matcher for file names. The test method "check_longPressItemDelete" is empty and needs to be implemented.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [ExampleUnitTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/test/java/com/thecoolguy/rumaan/fileio/ExampleUnitTest.java)                                    | The code above contains a unit test class, "ExampleUnitTest", which tests the correctness of an addition operation on the development machine. It asserts that the result of adding 2 and 2 should be equal to 4.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [UploadRepositoryTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/test/java/com/thecoolguy/rumaan/fileio/UploadRepositoryTest.java)                          | The code is a test case for the function `check_ExpireUrl()` in the class `UploadRepositoryTest`. It tests if the `getExpireUrl()` function in the `URLParser` class correctly generates a URL with an expiration parameter. The test compares the generated URL with a manually constructed URL and also with a URL built using constants defined in `ConstantsKt`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [UrlTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/test/java/com/thecoolguy/rumaan/fileio/UrlTest.java)                                                    | The code above is a unit test written in Java for a URL parsing function. It tests the functionality of a method called `parseEncryptUrl` from the `URLParser` class in the `com.thecoolguy.rumaan.fileio.utils.Utils` package. The test checks if the parsed URL from the `testUrl` string is equal to the `check` string. The test uses the `assertEquals` method from the JUnit framework to assert the equality.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [FileEntityTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/test/java/com/thecoolguy/rumaan/fileio/FileEntityTest.java)                                      | The code defines a test case (`FileEntityTest`) for a `FileEntity` class. The test case validates that the `FileEntity` object is able to correctly set and retrieve the `name` and `url` properties. It ensures that setting the properties returns non-null values and that the values can be retrieved and match the expected values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

</details>

<details closed><summary>Viewmodel</summary>

| File                                                                                                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---                                                                                                                                                                        | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [UploadHistoryViewModel.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/viewmodel/UploadHistoryViewModel.kt) | The code above is for an Android ViewModel class called "UploadHistoryViewModel". It extends the "AndroidViewModel" class and provides a LiveData object called "uploadList" that holds a list of "FileEntity" objects. The ViewModel is responsible for retrieving a database instance and accessing the "allUploads" data from the "uploadItemDao". The ViewModel is used to update and manage UI-related data for the Upload History feature in an Android application. |

</details>

<details closed><summary>Ui</summary>

| File                                                                                                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---                                                                                                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [FileioApplication.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/FileioApplication.kt)               | The code above represents the FileioApplication class in an Android application. Its core functionalities include:-Initializing and configuring logging using Timber library.-Setting up a custom error activity using CaocConfig from the customactivityoncrash library.                                                                                                                                                               |
| [UploadHistoryListAdapter.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/UploadHistoryListAdapter.kt) | This code defines the `UploadHistoryListAdapter` class, which is responsible for populating a RecyclerView with data. It takes a list of `FileEntity` objects and displays them in the appropriate view holder depending on the type of data. The class also handles item click events and provides methods for updating the data set and performing specific operations on the list.                                                   |
| [SwipeToDeleteCallBack.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/SwipeToDeleteCallBack.kt)       | The code represents a SwipeToDeleteCallBack class that extends the ItemTouchHelper.SimpleCallback class. This class allows for swiping to delete functionality in a RecyclerView. It provides methods to handle various touch events, such as onChildDraw, where it draws a red delete background and a delete icon on the item being swiped. It also checks for certain conditions, such as disabling swipes for a specific view type. |
| [NotificationHelper.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/NotificationHelper.kt)             | The code represents a NotificationHelper class in an Android app. It allows creating notifications for successful file uploads. It sets up a notification channel and builds a notification with various properties such as title, content, icon, intent, etc. It also handles compatibility for different Android versions. The notifications are created using the NotificationCompat and NotificationManagerCompat classes.          |

</details>

<details closed><summary>Fragments</summary>

| File                                                                                                                                                                            | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---                                                                                                                                                                             | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [NoNetworkDialogFragment.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/NoNetworkDialogFragment.kt) | The code is an implementation of a dialog fragment that displays an alert dialog when there is no network connection. It extends the androidx.fragment.app.DialogFragment class and implements the View.OnClickListener interface. It creates an AlertDialog and inflates a layout file (dialog_no_network_error.xml). It also handles the click event of the "Ok" button and calls a listener to notify the parent activity whenever the button is clicked. |
| [HomeFragment.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/HomeFragment.kt)                       | The code represents a HomeFragment class in an Android app where users can choose a file to upload. It inflates a layout file, handles button clicks, and communicates with the activity using the OnFragmentInteractionListener. It also has lifecycle methods for attaching and detaching from the context. The class has a companion object with a constant TAG for identification and a factory method for creating instances of the fragment.           |
| [ResultFragment.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/ResultFragment.kt)                   | The code above defines a ResultFragment class that extends the Fragment class. It provides the functionality for displaying a result view with a URL and the number of days until expiration. It also allows the user to copy the URL to the clipboard and notifies the listener when the "Done" button is clicked. The ResultFragment class can be instantiated with a URL and days parameter using the newInstance() method.                               |

</details>

<details closed><summary>Activities</summary>

| File                                                                                                                                                                         | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---                                                                                                                                                                          | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [MainActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/MainActivity.kt)                   | The code represents the MainActivity class of an Android app. It is responsible for handling user interactions and managing the UI. Some of the core functionalities include:-Implementing various interfaces for dialog clicks, fragment interactions, and menu item selections.-Setting up the work manager for uploading files.-Handling the result of file selection and initiating the upload process.-Managing permissions for reading and writing external storage.-Initializing the main fragment layout and showing the result fragment.-Handling back button presses and app exit.-Showing permission denied messages and opening app settings if needed. |
| [ErrorActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/ErrorActivity.kt)                 | The code above represents an ErrorActivity class in an Android application. It extends the AppCompatActivity class and is responsible for displaying an activity when runtime crashes occur. It overrides the onBackPressed() method to call finishAffinity() and ensures that the activity is finished when the back button is pressed. The onCreate() method sets the content view to activity_error layout.                                                                                                                                                                                                                                                      |
| [UploadHistoryActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/UploadHistoryActivity.kt) | This code represents an activity in an Android app called "UploadHistoryActivity" that displays a list of uploaded files. It handles user interactions such as clearing the upload history and deleting individual items from the list. The activity uses a RecyclerView with a custom adapter to display the list of uploaded files. It also implements swipe-to-delete functionality, where the user can swipe left on an item to delete it. The activity communicates with a ViewModel to fetch the list of uploaded files and updates the UI accordingly.                                                                                                       |
| [AboutActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/AboutActivity.kt)                 | The code represents an Android activity called "AboutActivity" that sets up a UI for displaying information about the app. It inflates a menu in the toolbar, sets a custom theme, and handles menu item clicks. When the "menu_open_source" item is clicked, it starts a new activity called "LicenseActivity".                                                                                                                                                                                                                                                                                                                                                    |
| [LicenseActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/LicenseActivity.kt)             | The code above defines a LicenseActivity in an Android app. The activity displays a list of open source licenses using the MaterialAboutLibrary. The list includes licenses for various components and libraries used in the app, along with their respective authors and years. The licenses are displayed in card format, each with an icon and a title. The activity overrides two methods to set the activity title and populate the list with the license cards.                                                                                                                                                                                               |

</details>

<details closed><summary>Repository</summary>

| File                                                                                                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---                                                                                                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [UploadHistoryWorkers.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/repository/UploadHistoryWorkers.kt) | The code contains two Worker classes, ClearHistoryWorker and DeleteSingleItemWorker, which are used in a background process for data management. ClearHistoryWorker clears all the upload history data by accessing the UploadHistoryRoomDatabase and calling the clearAll() method.DeleteSingleItemWorker deletes a single item from the upload history by accessing the UploadHistoryRoomDatabase and calling the deleteItemWithId() method, using the ID passed in as input data.These Worker classes are designed to be used with the Android WorkManager library to perform asynchronous tasks efficiently and reliably. |
| [UploadWorker.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/repository/UploadWorker.kt)                 | The code is for an UploadWorker class that handles uploading a file to a server using Fuel library. It extends the Worker class from the WorkManager library. It takes in a file URI as input, sends an HTTP upload request to the server, and retrieves the response. It saves the file information to a local database, creates a notification for the upload, and returns the result of the upload process (SUCCESS or FAILURE).                                                                                                                                                                                           |

</details>

<details closed><summary>Utils</summary>

| File                                                                                                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---                                                                                                                                                                        | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Extensions.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Extensions.kt)                             | The code provides two extension functions for convenient handling of toast messages and toggling the clickable state of a view.The first function, `toast`, allows displaying toast messages with a given context.The second function, `toggleClickable`, enables toggling the clickable state of a view by accepting a boolean value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [WorkManagerHelper.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/WorkManagerHelper.kt)               | The code defines a function called "createUploadWork" that creates and configures a OneTimeWorkRequest object for uploading a file. The function takes a URI parameter and creates work data with it. It also sets constraints on the work, specifying that it should only run when there is a connected network. The function then builds and returns the configured OneTimeWorkRequest object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Utils.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Utils.kt)                                       | This code defines a set of utility methods for file handling in an Android application. The `getLocalFile` function retrieves file details such as name and size from the Android Provider Database and wraps the information into a `LocalFile` object. The `getFileInputStream` function opens a file from storage in read mode and returns an input stream.The `Android` object contains helper methods for various Android-related tasks, such as checking network connectivity, creating intents, showing dialog fragments, dismissing dialogs, and opening app details settings.The `URLParser` object defines methods for parsing file.io URLs and extracting expiration URLs.The `JSONParser` object provides methods for parsing JSON responses and extracting link and expiry information.The `Date` object includes a helper method for getting the current date in a specific date format. |
| [Helpers.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Helpers.kt)                                   | The code defines a set of utility functions in the file "Helpers.kt" that deal with file operations. These functions allow for retrieving metadata about a file, obtaining the file itself, and composing a file entity object. The metadata function retrieves the name and size of a file based on its URI. The getFile function retrieves the File object based on the URI. The composeIntoFileEntity function takes a File object and a Response object and creates a FileEntity object using the file's name, URI, current date, and expiry information from the response.                                                                                                                                                                                                                                                                                                                        |
| [FragmentHelperExtensions.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/FragmentHelperExtensions.kt) | The code provides two extension functions for the FragmentManager class in Android. The addFragment function adds a fragment to a container with a specified ID, using a tag to identify it. It also sets a transition animation and adds the fragment to the back stack, allowing it to be navigated back to.The replaceFragment function replaces an existing fragment in a container with a new one, using the same parameters as the addFragment function. It also sets a transition animation and adds the new fragment to the back stack.                                                                                                                                                                                                                                                                                                                                                        |
| [MaterialIn.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/MaterialIn.kt)                             | The code defines an object called MaterialIn that contains functions for animating views. The `animate()` function takes a view, delayDirection, and slideDirection as parameters. It adds a pre-draw listener to the view and initializes an animation using the `initAnimation()` function. The `initAnimation()` function recursively animates child views by calculating offset values based on the delay and slide directions. The `startAnimators()` function starts the animation by setting up fade and slide animations for the view.                                                                                                                                                                                                                                                                                                                                                         |
| [Constants.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Constants.kt)                               | The code defines a Kotlin file that contains global constants for a file management Android application. It includes constants for base URL, expiration parameters, queries, default expiration weeks, URLs for GitHub and Twitter, email address, postfix for link, and timestamp format. These constants are used to define various functionalities and behaviors within the app.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

</details>

<details closed><summary>Listeners</summary>

| File                                                                                                                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                |
| ---                                                                                                                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                    |
| [DialogClickListener.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/listeners/DialogClickListener.kt)                     | The provided code defines an interface called DialogClickListener in the `com.thecoolguy.rumaan.fileio.listeners` package. This interface includes a single method named `onDialogPositiveClick`, which takes two parameters: a Dialog object and a Fragment object. This interface is used to handle positive click events in dialogs within the app. |
| [OnFragmentInteractionListener.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/listeners/OnFragmentInteractionListener.kt) | This code defines an interface named `OnFragmentInteractionListener` in the package `com.thecoolguy.rumaan.fileio.listeners`. The interface has two methods: `onUploadFileClick()` and `onDone()`, which can be implemented by other classes to handle user interactions with a fragment.                                                              |

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

[**Discussions**](https://github.com/rumaan/file.io-Android-Client/discussions)
  - Join the discussion here.

[**New Issue**](https://github.com/rumaan/file.io-Android-Client/issues)
  - Report a bug or request a feature here.

[**Contributing Guidelines**](https://github.com/rumaan/file.io-Android-Client/blob/main/CONTRIBUTING.md)

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
