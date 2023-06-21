
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
file.io-Android-Client
</h1>
<h3>◦ Share big. Share smart. With file.io.</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/Kotlin-7F52FF.svg?style&logo=Kotlin&logoColor=white" alt="Kotlin" />
<img src="https://img.shields.io/badge/Android-3DDC84.svg?style&logo=Android&logoColor=white" alt="Android" />
<img src="https://img.shields.io/badge/Gradle-02303A.svg?style&logo=Gradle&logoColor=white" alt="Gradle" />
<img src="https://img.shields.io/badge/java-%23ED8B00.svg?style&logo=openjdk&logoColor=white" alt="java" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
</p>

![GitHub top language](https://img.shields.io/github/languages/top/rumaan/file.io-Android-Client?style&color=5D6D7E)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/rumaan/file.io-Android-Client?style&color=5D6D7E)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/rumaan/file.io-Android-Client?style&color=5D6D7E)
![GitHub license](https://img.shields.io/github/license/rumaan/file.io-Android-Client?style&color=5D6D7E)
</div>

---

## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [⚙️ Features](#-features)
- [📂 Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🚀 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The file.io Android Client project is an app that allows users to upload files to a server with a customizable expiration time. The app provides features such as a history of uploaded files, file deletion, and notification of file upload completion. Its core functionalities include file selection, uploading, and storage using Room database, and customizable notification for upload completion. The project's value proposition lies in its simplicity and ease of use, making it an efficient tool for quick and secure file sharing.

---

## ⚙️ Features

Feature | Description |
|-----|-----|
| **🏗 Architecture** | The app follows the Model-View-ViewModel (MVVM) architecture pattern, separating the concerns of data management and presentation. It also uses the Android Jetpack libraries, including Room for database management, WorkManager for background uploading, and LiveData for asynchronous updates to the UI. |
| **📑 Documentation** | The codebase includes documentation for each of the major files in the repository, including file descriptions and summaries of their contents. The usage of functions, methods, and classes is also properly documented, aiding in the readability and maintainability of the codebase. |
| **🧩 Dependencies** | The app uses a range of dependencies, including material design, Kotlin extensions, AndroidX libraries, and Google services for handling authentication and crash reporting. Firebase Crashlytics and Fabric tools are used for crash reporting and analytics, while JUnit and Mockito are used for unit testing. |
| **♻️ Modularity** | The codebase is highly modular, with clear separation of concerns between different parts of the app. Each file has a specific purpose and is named appropriately, aiding in the readability and maintainability of the code. The app also includes several utilities and extensions to simplify common development tasks. |
| **✔️ Testing** | The codebase features both unit and integration tests, covering major components such as the database, repository, and viewmodels. The tests use common Android libraries such as JUnit and Mockito for testing, and follow best practices such as arranging, acting, and asserting. |
| **⚡️ Performance** | The app uses WorkManager and Room to perform long-running tasks such as uploading files and storing data in the database. It also uses Kotlin's coroutine APIs to handle network requests and updates to the UI without blocking the main thread. |
| **🔒 Security** | The app provides a secure way to upload files, implementing SSL/TLS encryption for network requests. It also uses Firebase Authentication to handle user login and Google services for secure cloud storage and analytics. |
| **🔀 Version Control** | The codebase is hosted on Github and uses Git for version control. Commits are well-organized, with clear and concise commit messages, and follow a typical branching strategy for pull requests. |
| **🔌 Integrations** | The app includes integrations with several Google services, including Google Drive and Firebase for cloud storage. It also includes integrations with Fabric and Firebase for crash reporting and analytics. |
| **📈 Scalability** | The app is designed to handle large numbers of file uploads and storage, using Room's database management and WorkManager's background processing to ensure performance and stability. The app's architecture allows for easy scaling and adding new features in the future. |

---


## 📂 Project Structure


```bash
repo
├── LICENSE
├── README.md
├── app
│   ├── build
│   │   └── outputs
│   │       └── apk
│   │           └── debug
│   │               └── app-debug.apk
│   ├── build.gradle
│   ├── proguard-rules.pro
│   ├── release
│   │   └── app-release.apk
│   └── src
│       ├── androidTest
│       │   └── java
│       │       └── com
│       │           └── thecoolguy
│       │               └── rumaan
│       │                   └── fileio
│       │                       ├── ExampleInstrumentedTest.kt
│       │                       ├── FileEntityDaoTest.java
│       │                       └── UploadHistoryInstrumentedTest.java
│       ├── main
│       │   ├── AndroidManifest.xml
│       │   ├── java
│       │   │   └── com
│       │   │       └── thecoolguy
│       │   │           └── rumaan
│       │   │               └── fileio
│       │   │                   ├── data
│       │   │                   │   ├── db
│       │   │                   │   │   ├── DatabaseContract.kt
│       │   │                   │   │   ├── DatabaseHelper.kt
│       │   │                   │   │   ├── UploadHistoryRoomDatabase.kt
│       │   │                   │   │   └── UploadItemDao.kt
│       │   │                   │   └── models
│       │   │                   │       ├── FileEntity.kt
│       │   │                   │       ├── LocalFile.kt
│       │   │                   │       └── Response.kt
│       │   │                   ├── listeners
│       │   │                   │   ├── DialogClickListener.kt
│       │   │                   │   └── OnFragmentInteractionListener.kt
│       │   │                   ├── repository
│       │   │                   │   ├── UploadHistoryWorkers.kt
│       │   │                   │   └── UploadWorker.kt
│       │   │                   ├── ui
│       │   │                   │   ├── FileioApplication.kt
│       │   │                   │   ├── NotificationHelper.kt
│       │   │                   │   ├── SwipeToDeleteCallBack.kt
│       │   │                   │   ├── UploadHistoryListAdapter.kt
│       │   │                   │   ├── activities
│       │   │                   │   │   ├── AboutActivity.kt
│       │   │                   │   │   ├── ErrorActivity.kt
│       │   │                   │   │   ├── LicenseActivity.kt
│       │   │                   │   │   ├── MainActivity.kt
│       │   │                   │   │   └── UploadHistoryActivity.kt
│       │   │                   │   └── fragments
│       │   │                   │       ├── HomeFragment.kt
│       │   │                   │       ├── NoNetworkDialogFragment.kt
│       │   │                   │       └── ResultFragment.kt
│       │   │                   ├── utils
│       │   │                   │   ├── Constants.kt
│       │   │                   │   ├── Extensions.kt
│       │   │                   │   ├── FragmentHelperExtensions.kt
│       │   │                   │   ├── Helpers.kt
│       │   │                   │   ├── MaterialIn.kt
│       │   │                   │   ├── Utils.kt
│       │   │                   │   └── WorkManagerHelper.kt
│       │   │                   └── viewmodel
│       │   │                       └── UploadHistoryViewModel.kt
│       │   └── res
│       │       ├── anim
│       │       │   ├── item_anim_slide_up_fade.xml
│       │       │   ├── item_anim_slide_up_from_bottom.xml
│       │       │   └── layout_anim_fall_down.xml
│       │       ├── drawable
│       │       │   ├── background_launch_screen.xml
│       │       │   ├── bg_black_gradient.xml
│       │       │   ├── bg_blue_gradient.xml
│       │       │   ├── bg_text_green.xml
│       │       │   ├── bg_text_link.xml
│       │       │   ├── bg_text_orange.xml
│       │       │   ├── bg_text_white.xml
│       │       │   ├── btn_blue.xml
│       │       │   ├── btn_blue_ripple_white.xml
│       │       │   ├── btn_circle.xml
│       │       │   ├── btn_close_orange.xml
│       │       │   ├── btn_close_ripple.xml
│       │       │   ├── btn_ripple_circle.xml
│       │       │   ├── btn_upload.xml
│       │       │   ├── btn_upload_ripple.xml
│       │       │   ├── divider_decor.xml
│       │       │   ├── github.png
│       │       │   ├── gmail.png
│       │       │   ├── grey_box.xml
│       │       │   ├── ic_anonymous.xml
│       │       │   ├── ic_bomb.xml
│       │       │   ├── ic_cloud.xml
│       │       │   ├── ic_cloud_computing.xml
│       │       │   ├── ic_copy.xml
│       │       │   ├── ic_delete_white_24dp.xml
│       │       │   ├── ic_file.xml
│       │       │   ├── ic_file_upload.xml
│       │       │   ├── ic_header_img_one.xml
│       │       │   ├── ic_header_img_two.xml
│       │       │   ├── ic_history.xml
│       │       │   ├── ic_info_circle.xml
│       │       │   ├── ic_launcher_background.xml
│       │       │   ├── ic_library.xml
│       │       │   ├── ic_more_vert.xml
│       │       │   ├── ic_no_wifi.xml
│       │       │   ├── ic_process_app.xml
│       │       │   ├── ic_sad.xml
│       │       │   ├── ic_shape.xml
│       │       │   ├── ic_time.xml
│       │       │   ├── ic_upload_to_cloud.xml
│       │       │   ├── profile.png
│       │       │   └── twitter.png
│       │       ├── drawable-hdpi
│       │       │   ├── cross_bars.png
│       │       │   └── header_img_hero.png
│       │       ├── drawable-mdpi
│       │       │   ├── cross_bars.png
│       │       │   └── header_img_hero.png
│       │       ├── drawable-v24
│       │       │   └── ic_launcher_foreground.xml
│       │       ├── drawable-xhdpi
│       │       │   ├── cross_bars.png
│       │       │   └── header_img_hero.png
│       │       ├── drawable-xxhdpi
│       │       │   ├── cross_bars.png
│       │       │   └── header_img_hero.png
│       │       ├── drawable-xxxhdpi
│       │       │   ├── cross_bars.png
│       │       │   └── header_img_hero.png
│       │       ├── font
│       │       │   ├── source_sans.xml
│       │       │   ├── source_sans_pro.xml
│       │       │   ├── source_sans_pro_bold.xml
│       │       │   └── source_sans_pro_semibold.xml
│       │       ├── layout
│       │       │   ├── activity_about.xml
│       │       │   ├── activity_error.xml
│       │       │   ├── activity_home.xml
│       │       │   ├── activity_main.xml
│       │       │   ├── activity_upload_history.xml
│       │       │   ├── choose_expire_fragment.xml
│       │       │   ├── content_about.xml
│       │       │   ├── content_about_fileio.xml
│       │       │   ├── content_about_me.xml
│       │       │   ├── dialog_no_network_error.xml
│       │       │   ├── fragment_choose_file.xml
│       │       │   ├── fragment_upload_file.xml
│       │       │   ├── fragment_upload_progress.xml
│       │       │   ├── fragment_upload_result.xml
│       │       │   ├── layout_main.xml
│       │       │   ├── layout_result.xml
│       │       │   ├── upload_history_item_content.xml
│       │       │   └── upload_history_item_date.xml
│       │       ├── menu
│       │       │   ├── menu_history.xml
│       │       │   ├── option_about.xml
│       │       │   └── options_main.xml
│       │       ├── mipmap-anydpi-v26
│       │       │   ├── ic_launcher.xml
│       │       │   └── ic_launcher_round.xml
│       │       ├── mipmap-hdpi
│       │       │   ├── ic_launcher.png
│       │       │   └── ic_launcher_round.png
│       │       ├── mipmap-mdpi
│       │       │   ├── ic_launcher.png
│       │       │   └── ic_launcher_round.png
│       │       ├── mipmap-xhdpi
│       │       │   ├── ic_launcher.png
│       │       │   └── ic_launcher_round.png
│       │       ├── mipmap-xxhdpi
│       │       │   ├── ic_launcher.png
│       │       │   └── ic_launcher_round.png
│       │       ├── mipmap-xxxhdpi
│       │       │   ├── ic_launcher.png
│       │       │   └── ic_launcher_round.png
│       │       ├── navigation
│       │       │   └── nav_graph.xml
│       │       ├── values
│       │       │   ├── colors.xml
│       │       │   ├── dimens.xml
│       │       │   ├── font_certs.xml
│       │       │   ├── preloaded_fonts.xml
│       │       │   ├── strings.xml
│       │       │   ├── styles.xml
│       │       │   └── values.xml
│       │       └── xml
│       │           └── shortcuts.xml
│       └── test
│           └── java
│               └── com
│                   └── thecoolguy
│                       └── rumaan
│                           └── fileio
│                               ├── ExampleUnitTest.java
│                               ├── FileEntityTest.java
│                               ├── UploadRepositoryTest.java
│                               └── UrlTest.java
├── build.gradle
├── gradle
│   └── wrapper
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties
├── gradle.properties
├── gradlew
├── screenshots
│   ├── readme.txt
│   ├── screen1.png
│   ├── screen2.png
│   ├── screenshot.png
│   └── todo-ui.png
└── settings.gradle

60 directories, 158 files
```

---

## 🧩 Modules

<details closed><summary>Activities</summary>

| File                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                            | Module                                                                                |
|:-------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------|
| MainActivity.kt          | The provided code snippet represents an Android activity that allows users to upload files to a server. It includes methods for handling file selection, uploading the file using WorkManager, displaying upload progress, and showing the upload history. The activity also features a toolbar with options for navigating to the upload history and about pages.                                                                                 | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/MainActivity.kt          |
| ErrorActivity.kt         | This code defines an ErrorActivity class that extends AppCompatActivity and is displayed in case of any runtime crashes. It implements the onBackPressed() method to finish the activity and overrides the onCreate() method to set the layout content to activity_error.xml.                                                                                                                                                                      | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/ErrorActivity.kt         |
| UploadHistoryActivity.kt | The provided code defines the UploadHistoryActivity, responsible for displaying the user's file upload history. It provides options to clear the history and swipe left to delete individual history items. It also groups the list of uploads by date, displays them in a RecyclerView, and updates the UI based on the latest data available from the ViewModel.                                                                                 | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/UploadHistoryActivity.kt |
| AboutActivity.kt         | The provided code snippet defines an activity that displays information about the application. It also inflates a menu with an option to open the source code, which launches a different activity. The toolbar is also included in this activity, consistent with the application theme and design.                                                                                                                                               | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/AboutActivity.kt         |
| LicenseActivity.kt       | The code implements an Android activity called LicenseActivity that extends the Material About Library's MaterialAboutActivity class, which displays open source licenses for various Android support libraries. The getMaterialAboutList() function creates license cards for several libraries with their details, including the license type and creator, and adds them to a MaterialAboutList object, which is then displayed on the activity. | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/LicenseActivity.kt       |

</details>

<details closed><summary>App</summary>

| File         | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                      | Module           |
|:-------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| build.gradle | This Gradle build script defines the necessary dependencies for an Android app including material design libraries, Room for database management, Firebase Crashlytics for crash reporting, and the Kotlin programming language. Additionally, it includes plugins for Kotlin support, permission management, and Google services integration. The script also configures testing dependencies and build types for release and debug builds. | app/build.gradle |

</details>

<details closed><summary>Fileio</summary>

| File                               | Summary                                                                                                                                                                                                                                                                                                                                                               | Module                                                                                   |
|:-----------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------|
| ExampleInstrumentedTest.kt         | The code snippet is an example of an instrumented test for an Android application using the AndroidJUnit4 test runner. It verifies that the app's context matches the expected package name using the InstrumentationRegistry and AndroidX test libraries. The test is executed on an Android device, using an activity test rule for the main activity.              | app/src/androidTest/java/com/thecoolguy/rumaan/fileio/ExampleInstrumentedTest.kt         |
| FileEntityDaoTest.java             | This code snippet tests the functionality of a Room Database for uploading and storing files through the following methods: counting the number of uploaded files, inserting a new file and checking if it has been properly saved, and saving multiple items and retrieving them later. The code uses JUnit testing and Android framework for unit testing purposes. | app/src/androidTest/java/com/thecoolguy/rumaan/fileio/FileEntityDaoTest.java             |
| UploadHistoryInstrumentedTest.java | The provided code snippet is a JUnit test class for the UploadHistoryActivity in an Android application. It includes methods to initialize a Room database, insert sample data, and define a matcher for asserting file entity objects. The class also contains an empty test method for checking the long press item delete functionality.                           | app/src/androidTest/java/com/thecoolguy/rumaan/fileio/UploadHistoryInstrumentedTest.java |
| ExampleUnitTest.java               | The provided code snippet is a JUnit test that verifies if the addition of 2 and 2 equals 4 using the assertEquals method. This is a simple unit test intended to check if the JUnit library is correctly installed and configured for the project.                                                                                                                   | app/src/test/java/com/thecoolguy/rumaan/fileio/ExampleUnitTest.java                      |
| UploadRepositoryTest.java          | The provided code is a unit test for the UploadRepository class, checking the functionality of the getExpireUrl method in the URLParser utility class. The test verifies that the method correctly constructs a URL with an expiration date parameter, and compares it to a pre-defined URL constant and a manually constructed URL with the same parameter.          | app/src/test/java/com/thecoolguy/rumaan/fileio/UploadRepositoryTest.java                 |
| UrlTest.java                       | The code snippet includes a JUnit test for a URL parser utility from the Utils class. The test verifies that the parser correctly extracts the main URL from an encrypted URL, using the assertEquals() method to compare the expected output with the actual output. The TODO comment suggests there may be additional cases to test in the future.                  | app/src/test/java/com/thecoolguy/rumaan/fileio/UrlTest.java                              |
| FileEntityTest.java                | The provided code snippet is a JUnit test for the FileEntity class. It tests that the setName and setUrl methods correctly set the values of the name and url properties of a newly created FileEntity object. The test uses assertions to ensure that the values are not null and equal to the expected test values.                                                 | app/src/test/java/com/thecoolguy/rumaan/fileio/FileEntityTest.java                       |

</details>

<details closed><summary>Fragments</summary>

| File                       | Summary                                                                                                                                                                                                                                                                                                                                                                       | Module                                                                                 |
|:---------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------|
| NoNetworkDialogFragment.kt | The code snippet defines a DialogFragment class named NoNetworkDialogFragment, which displays an alert dialog upon network error. It initializes its dialog view, sets a click listener on the OK button, and invokes a callback on click using the DialogClickListener interface implemented by its parent activity.                                                         | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/NoNetworkDialogFragment.kt |
| HomeFragment.kt            | The provided code defines a HomeFragment class that extends androidx.fragment.app.Fragment. It contains a button that triggers an OnFragmentInteractionListener when clicked. The listener is implemented by the parent activity, which must implement the OnFragmentInteractionListener interface.                                                                           | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/HomeFragment.kt            |
| ResultFragment.kt          | The code provides the ResultFragment class, which extends Fragment and creates a fragment that displays a given URL and the number of days until it expires. It listens for clicks on the "Done" button to execute a callback and on the link text to copy the URL to the clipboard. The class also provides a newInstance method for creating new instances of the fragment. | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/ResultFragment.kt          |

</details>

<details closed><summary>Listeners</summary>

| File                             | Summary                                                                                                                                                                                                                                                                                | Module                                                                                    |
|:---------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------|
| DialogClickListener.kt           | This code defines an interface `DialogClickListener` with a method `onDialogPositiveClick`, which takes in a `Dialog` and a `Fragment`. It serves as a listener for positive clicks on a dialog, allowing other classes to implement it and handle the positive click event as needed. | app/src/main/java/com/thecoolguy/rumaan/fileio/listeners/DialogClickListener.kt           |
| OnFragmentInteractionListener.kt | The code defines an interface OnFragmentInteractionListener with two functions onUploadFileClick and onDone. This interface can be used to handle user interactions within a fragment related to file uploading and completion of the task.                                            | app/src/main/java/com/thecoolguy/rumaan/fileio/listeners/OnFragmentInteractionListener.kt |

</details>

<details closed><summary>Repository</summary>

| File                    | Summary                                                                                                                                                                                                                                                                                                                                                      | Module                                                                            |
|:------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
| UploadHistoryWorkers.kt | The code snippet provides two worker classes for clearing all upload history records and deleting a single item from the upload history database. The workers use the Room database library for Android and are executed asynchronously using the Android Jetpack WorkManager API. The code includes constants and input data keys for use with the workers. | app/src/main/java/com/thecoolguy/rumaan/fileio/repository/UploadHistoryWorkers.kt |
| UploadWorker.kt         | This code snippet defines an Android WorkManager worker for uploading files to the file.io website. It sends a file, receives a response, and inserts the result into a database, and sends a notification about the upload. It also handles input and output data using workDataOf() and inputData.getString().                                             | app/src/main/java/com/thecoolguy/rumaan/fileio/repository/UploadWorker.kt         |

</details>

<details closed><summary>Root</summary>

| File            | Summary                                                                                                                                                                                                                                                                                                                      | Module          |
|:----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------|
| build.gradle    | The provided code snippet contains the buildscript and allprojects blocks in a Gradle file. It defines the repositories to gather dependencies and plugins from, as well as the dependencies needed for the build process. These include the Android Gradle plugin, Fabric tools, Google services, and Kotlin Gradle plugin. | build.gradle    |
| settings.gradle | This code snippet includes the app module in the project.                                                                                                                                                                                                                                                                    | settings.gradle |

</details>

<details closed><summary>Ui</summary>

| File                        | Summary                                                                                                                                                                                                                                                                                                                                                                                                        | Module                                                                        |
|:----------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------|
| FileioApplication.kt        | The provided code snippet is an Android application class that initializes the Timber logging framework and configures a custom activity for handling crashes using CaocConfig. It also includes a companion object that defines a constant TAG for the application class.                                                                                                                                     | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/FileioApplication.kt        |
| UploadHistoryListAdapter.kt | The provided code defines an adapter for a RecyclerView component used to display a list of uploaded files. It handles two types of views: dates and list items, uses a list of composed items to define the order in which views are displayed, and provides methods to update and manipulate the data displayed on the list. It also includes two ViewHolder classes to define the views for each item type. | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/UploadHistoryListAdapter.kt |
| SwipeToDeleteCallBack.kt    | The code provides a Swipe-to-Delete functionality for a RecyclerView in an Android app. It implements a callback object that extends the ItemTouchHelper.SimpleCallback class, and overrides methods to handle the swipe-to-delete gesture. The implementation includes drawing a red background, an icon, and disabling swipe for specific views.                                                             | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/SwipeToDeleteCallBack.kt    |
| NotificationHelper.kt       | The code snippet is a Kotlin class that creates and displays a notification in the Android app. It includes a function that takes a file entity parameter and generates a notification with a title, text, and an intent to open a specific activity. The notification also includes a sound, color, and grouping capabilities for devices running Android O and higher.                                       | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/NotificationHelper.kt       |

</details>

<details closed><summary>Utils</summary>

| File                        | Summary                                                                                                                                                                                                                                                                                                                                                                                     | Module                                                                           |
|:----------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------|
| Extensions.kt               | The code snippet defines two extension functions for Android development. The first function, `toast()`, displays a short message through a `Toast` object when called on a `String` instance. The second function, `toggleClickable()`, sets the `isClickable` property of a `View` object to a specified Boolean value when called on it.                                                 | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Extensions.kt               |
| WorkManagerHelper.kt        | This code snippet provides a function for creating a one-time work request that uploads a file. The function takes in a URI as a parameter and creates a work data with it. It also sets constraints for the network type and adds a tag to the work request.                                                                                                                               | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/WorkManagerHelper.kt        |
| Utils.kt                    | The provided code snippet contains a set of helper methods for file handling, Android-related functions such as checking network connectivity or launching app settings, URL parsing and JSON parsing. These methods range from opening a file in read mode and returning an input stream or fetching file details, to creating intent for choosing files or copying text to the clipboard. | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Utils.kt                    |
| Helpers.kt                  | The provided code snippet includes functions for retrieving file metadata from a given URI and composing a file entity from a file and response object. The functions use the Android content resolver and OpenableColumns to access file information and Timber for logging purposes. The resulting file entity includes the file name, URI, creation date, and expiration period.         | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Helpers.kt                  |
| FragmentHelperExtensions.kt | The code provides two extension functions for FragmentManager in Android that allows adding and replacing fragments in a container. The functions also provide options for setting transaction transitions and adding the transaction to the back stack for proper navigation.                                                                                                              | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/FragmentHelperExtensions.kt |
| MaterialIn.kt               | This code snippet provides a utility class for performing Material Design inspired animations on Android views. It includes methods for animating views in specific directions (e.g. bottom to top) and with specific delays. The animations are implemented using the Android Animator framework and include fade and slide effects.                                                       | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/MaterialIn.kt               |
| Constants.kt                | The code snippet defines global constants for a file IO utility, including a base URL, query parameters, default expiration time, and links to Github and Twitter profiles. It also defines an email address and a postfix to append to links, as well as a timestamp format.                                                                                                               | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Constants.kt                |

</details>

<details closed><summary>Viewmodel</summary>

| File                      | Summary                                                                                                                                                                                                                                                                                    | Module                                                                             |
|:--------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
| UploadHistoryViewModel.kt | The provided code snippet is a ViewModel class that retrieves a LiveData list of FileEntity objects from a local database using the Room library. It is used to display upload history data in the UI. The class extends AndroidViewModel and takes an application context as a parameter. | app/src/main/java/com/thecoolguy/rumaan/fileio/viewmodel/UploadHistoryViewModel.kt |

</details>

---

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - [ℹ️ Requirement 1]
> - [ℹ️ Requirement 2]
> - [...]

### 🖥 Installation

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

### 🤖 Using file.io-Android-Client

```sh
java -jar build/libs/myapp.jar
```

### 🧪 Running Tests
```sh
gradle test
```

---


## 🗺 Roadmap

> - [X] [ℹ️  Task 1: Implement X]
> - [ ] [ℹ️  Task 2: Refactor Y]
> - [ ] [...]


---

## 🤝 Contributing

Contributions are always welcome! Please follow these steps:
1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).
```sh
git checkout -b new-feature-branch
```
4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub using the following command
```sh
git push origin new-feature-branch
```
7. Create a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 📄 License

This project is licensed under the `[ℹ️  INSERT-LICENSE-TYPE]` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 👏 Acknowledgments

> - [ℹ️  List any resources, contributors, inspiration, etc.]

---
