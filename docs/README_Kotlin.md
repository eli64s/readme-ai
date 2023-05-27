
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
file.io-Android-Client
</h1>
<h3 align="center">📍 Get File.io on the Go - The Android Client for Seamless File Sharing!</h3>
<h3 align="center">🚀 Developed with the software and tools below:</h3>
<p align="center">

<img src="https://img.shields.io/badge/Kotlin-7F52FF.svg?style=for-the-badge&logo=Kotlin&logoColor=white" alt="Kotlin" />
<img src="https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white" alt="java" />
<img src="https://img.shields.io/badge/Gradle-02303A.svg?style=for-the-badge&logo=Gradle&logoColor=white" alt="Gradle" />
<img src="https://img.shields.io/badge/Android-3DDC84.svg?style=for-the-badge&logo=Android&logoColor=white" alt="Android" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="Markdown" />
</p>

</div>

---

## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍Overview](#overview)
- [🔮 Features](#-feautres)
  - [Distinctive Features](#distinctive-features)
- [⚙️ Project Structure](#️-project-structure)
- [💻 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
  - [✅ Prerequisites](#-prerequisites)
  - [💻 Installation](#-installation)
  - [🤖 Using file.io-Android-Client](#-using-fileio-android-client)
  - [🧪 Running Tests](#-running-tests)
- [🛠 Future Development](#-future-development)
- [🤝 Contributing](#-contributing)
- [🪪 License](#-license)
- [🙏 Acknowledgments](#-acknowledgments)

---


## 📍Overview

The file.io-Android-Client GitHub project is a great tool for those looking to quickly and easily share files with others. It provides users with an easy to use interface, allowing them to select a file from their device and upload it to the file.io server, and receive a URL with an expiration time. The project is also optimized for security and performance, with logging and error handling built in. Additionally, the project includes a variety of tools to manage and manipulate files, such as ProGuard rules, and a host of other helpful features. All in all, the file.io-Android-Client project is a great choice for those looking for a convenient and secure way to share files.

---

## 🔮 Features

### Distinctive Features

1. **User-Centered Design Elements:** The project utilizes a range of user-centered design elements to ensure a seamless user experience. This includes features such as a RecyclerView adapter for the upload history list, a swipe-to-delete gesture for items in the list, a dialog fragment with a positive click listener for error messages, and an activity for displaying open source licenses. 
2. **Android Application Architecture:** The project is built on an Android application architecture which includes a ViewModel to manage the upload history, a Fragment for file selection, an Activity for displaying the result with the given URL, and a WorkManager to handle file uploads.
3. **Utilities and Extensions:** The project includes a range of utilities and extensions to simplify development and ensure accuracy. This includes functions to parse file.io URLs and JSON responses, an animation utility for Android views, Toast infix functions, and functions for dealing with local file details and file input streams. 
4. **Code Documentation:** The project is well documented, providing clear and concise descriptions for each code script. This allows developers to quickly understand the purpose of each code script and its relation to the overall project. 
5. **WhiteSource Integration:** The project includes a configuration file which enables the integration of WhiteSource, allowing for a repository scan and setting the vulnerability check conclusion level to "failure". 
6. **CI/CD Pipelines:** The project uses CircleCI for continuous integration and deployment of the Android application, allowing for quick and accurate delivery of the application. 
7. **Testing:** The project includes a range of tests for verifying the correctness of the application, including unit tests for addition operations, instrumented tests for activities, and repository tests for checking the functionality of the UploadRepository class.

---


<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## ⚙️ Project Structure


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

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 💻 Modules

<details closed><summary>Activities</summary>

| File                     | Summary                                                                                                                                                                                                                                                                                                                                                                                           | Module                                                                                |
|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------|
| MainActivity.kt          | This code script is for an Android activity which allows users to upload files from their device, and receive a URL for the file. It handles permissions, file selection, menu creation, and displaying the result with a given URL. It also has error handling and logging for debugging.                                                                                                        | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/MainActivity.kt          |
| ErrorActivity.kt         | This code script is an Activity class for a Runtime Error page which allows for the application to be closed when the back button is pressed.                                                                                                                                                                                                                                                     | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/ErrorActivity.kt         |
| UploadHistoryActivity.kt | This code script is for an activity in an Android app that displays a list of uploads from a database. It handles user interactions such as swiping to delete an item from the list, and also provides a menu option to clear the entire history of uploads from the database.                                                                                                                    | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/UploadHistoryActivity.kt |
| AboutActivity.kt         | This code script creates an activity which provides options for the user such as an open source menu item which triggers a LicenseActivity. It also provides a toolbar and enables the user to go back home.                                                                                                                                                                                      | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/AboutActivity.kt         |
| LicenseActivity.kt       | This script is for a LicenseActivity class used to display open source licenses for components such as AOSP Support Libraries, Architecture Components, MaterialAboutLibrary, Fuel, NumberProgressBar, Permission Dispatcher, and CustomActivityOnCrash. It imports AppCompatResources, MaterialAboutLibrary, and OpenSourceLicense classes to create MaterialAboutList objects for each license. | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/LicenseActivity.kt       |

</details>

<details closed><summary>App</summary>

| File               | Summary                                                                                                                                                                                                                                                                                                                                  | Module                 |
|:-------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------|
| proguard-rules.pro | This code script provides ProGuard rules and instructions for configuring an Android project, including how to preserve line number information for debugging and hide the original source file name. Specific classes and attributes are identified for preservation, and warnings for certain classes are suppressed.                  | app/proguard-rules.pro |
| build.gradle       | This code script is a build configuration for an Android application, applying multiple plugins and specifying a range of dependencies for libraries, testing, navigation, and other services. It also configures the build types, including minification and proguard rules, as well as the versioning information for the application. | app/build.gradle       |

</details>

<details closed><summary>Debug</summary>

| File          | Summary                                                                                                          | Module                                    |
|:--------------|:-----------------------------------------------------------------------------------------------------------------|:------------------------------------------|
| app-debug.apk | This code script is unable to decode the content of a file because it is either non-text or not in UTF-8 format. | app/build/outputs/apk/debug/app-debug.apk |

</details>

<details closed><summary>Fileio</summary>

| File                               | Summary                                                                                                                                                                                                                                                                                               | Module                                                                                   |
|:-----------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------|
| ExampleInstrumentedTest.kt         | This code script performs a test of the MainActivity within the package "com.thecoolguy.rumaan.fileio" using AndroidJUnit4. It verifies the application context of the test to ensure accuracy.                                                                                                       | app/src/androidTest/java/com/thecoolguy/rumaan/fileio/ExampleInstrumentedTest.kt         |
| FileEntityDaoTest.java             | This code script tests the UploadHistoryRoomDatabase class by creating and inserting file entities, and by checking the number of rows in the database. It checks for nulls in both the file entity object and the database object, and also verifies that multiple items can be saved and retrieved. | app/src/androidTest/java/com/thecoolguy/rumaan/fileio/FileEntityDaoTest.java             |
| UploadHistoryInstrumentedTest.java | This code script is a test for checking the functionality of the UploadHistoryActivity and contains methods for creating a database of FileEntities, checking the file name of the entities, and deleting items from the database.                                                                    | app/src/androidTest/java/com/thecoolguy/rumaan/fileio/UploadHistoryInstrumentedTest.java |
| ExampleUnitTest.java               | This code script is a unit test which verifies the correctness of an addition operation, making sure that 2 + 2 = 4.                                                                                                                                                                                  | app/src/test/java/com/thecoolguy/rumaan/fileio/ExampleUnitTest.java                      |
| UploadRepositoryTest.java          | This code script tests the functionality of an UploadRepository class, by checking that the "expireUrl" method is producing the expected results by comparing the generated URL to a predefined URL and constants from a separate file.                                                               | app/src/test/java/com/thecoolguy/rumaan/fileio/UploadRepositoryTest.java                 |
| UrlTest.java                       | This code script tests the URL parsing utility from the "Utils" package, which takes an encrypted URL and returns only the base URL. The expected output is then checked against the actual output, ensuring that the utility works properly.                                                         | app/src/test/java/com/thecoolguy/rumaan/fileio/UrlTest.java                              |
| FileEntityTest.java                | This code script tests the FileEntity class in the com.thecoolguy.rumaan.fileio package by setting and asserting values for its name and URL fields.                                                                                                                                                  | app/src/test/java/com/thecoolguy/rumaan/fileio/FileEntityTest.java                       |

</details>

<details closed><summary>Fragments</summary>

| File                       | Summary                                                                                                                                                                                                                                         | Module                                                                                 |
|:---------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------|
| NoNetworkDialogFragment.kt | This code script defines a DialogFragment that displays an error message when there is no internet connection. When the "OK" button is clicked, it triggers a positive DialogClickListener which is implemented by the activity.                | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/NoNetworkDialogFragment.kt |
| HomeFragment.kt            | This code script is a fragment class that creates a view for the user to choose a file from their device. It implements an OnFragmentInteractionListener interface to handle the interaction when the file is chosen.                           | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/HomeFragment.kt            |
| ResultFragment.kt          | This code script is a Fragment class for displaying the download URL and expiration time for a file, with a button for dismissing the fragment. It listens for user interaction events and includes a feature to copy the URL to the clipboard. | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/ResultFragment.kt          |

</details>

<details closed><summary>Gradle</summary>

| File      | Summary                                                                                                        | Module           |
|:----------|:---------------------------------------------------------------------------------------------------------------|:-----------------|
| .DS_Store | This code script attempts to decode content that is neither text nor encoded in UTF-8, but is unable to do so. | gradle/.DS_Store |

</details>

<details closed><summary>Listeners</summary>

| File                             | Summary                                                                                                                                                                                           | Module                                                                                    |
|:---------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------|
| DialogClickListener.kt           | This code script outlines an interface for a DialogClickListener, providing a function to be called when a dialog has a positive click, taking the dialog and a Fragment as parameters.           | app/src/main/java/com/thecoolguy/rumaan/fileio/listeners/DialogClickListener.kt           |
| OnFragmentInteractionListener.kt | This script defines an interface, "OnFragmentInteractionListener", which provides two methods: "onUploadFileClick" and "onDone". These methods provide a means to interact with a given fragment. | app/src/main/java/com/thecoolguy/rumaan/fileio/listeners/OnFragmentInteractionListener.kt |

</details>

<details closed><summary>Release</summary>

| File            | Summary                                                                  | Module                      |
|:----------------|:-------------------------------------------------------------------------|:----------------------------|
| app-release.apk | This script is unable to read content from a non-text or non-UTF-8 file. | app/release/app-release.apk |

</details>

<details closed><summary>Repository</summary>

| File                    | Summary                                                                                                                                                                                                                                                                           | Module                                                                            |
|:------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
| UploadHistoryWorkers.kt | This code script implements two classes that are used to clear and delete items from the UploadHistoryRoomDatabase. The ClearHistoryWorker class clears all items from the database while the DeleteSingleItemWorker class deletes an item from the database based on a given id. | app/src/main/java/com/thecoolguy/rumaan/fileio/repository/UploadHistoryWorkers.kt |
| UploadWorker.kt         | This code script is for a WorkManager that handles file uploads. It takes a file Uri as input and returns a link and expiration date of the uploaded file. It also saves the result in a database and sends a notification about the upload.                                      | app/src/main/java/com/thecoolguy/rumaan/fileio/repository/UploadWorker.kt         |

</details>

<details closed><summary>Root</summary>

| File            | Summary                                                                                                                                                                                                                                                                        | Module          |
|:----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------|
| .whitesource    | This configuration file enables the integration of WhiteSource, enabling a repository scan and setting the vulnerability check conclusion level to "failure".                                                                                                                  | .whitesource    |
| gradlew         | This script sets up an environment for running Gradle on UN*X systems. It sets up the APP_HOME directory, JVM options, and converts paths to Windows format for Cygwin. It then passes these arguments to the Java command to run Gradle with the given application arguments. | gradlew         |
| build.gradle    | This code script sets up the buildscript and allprojects repositories, including external sources from Google, jCenter, Fabric, and JitPack, and adds the necessary dependencies for the Gradle build, Android tools, Fabric, Google Services, and Kotlin.                     | build.gradle    |
| settings.gradle | This code script includes the':app' module, allowing access to the main application functionality.                                                                                                                                                                             | settings.gradle |

</details>

<details closed><summary>Ui</summary>

| File                        | Summary                                                                                                                                                                                                                                                                                              | Module                                                                        |
|:----------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------|
| FileioApplication.kt        | This script defines an application class that provides logging and error handling features. Timber.DebugTree() is used for housekeeping of logs, and CaocConfig.Builder.create() is used to create a custom activity for errors.                                                                     | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/FileioApplication.kt        |
| UploadHistoryListAdapter.kt | This code script is for an adapter for a RecyclerView in an Android app. It provides the necessary functions to populate and manage the view items and their associated data. It includes functions to swap the list of items, remove items, and copy URL links to the clipboard.                    | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/UploadHistoryListAdapter.kt |
| SwipeToDeleteCallBack.kt    | This code script provides a SwipeToDeleteCallBack class which implements the ItemTouchHelper.SimpleCallback class. It sets up a left swipe gesture to delete items from a RecyclerView. It also handles the drawing of a delete icon and a red background when the user initiates the delete action. | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/SwipeToDeleteCallBack.kt    |
| NotificationHelper.kt       | This code script defines a NotificationHelper companion object for creating a notification for a successful file upload. It sets up an intent, notification builder, and a notification channel for Android versions O and up before posting the notification.                                       | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/NotificationHelper.kt       |

</details>

<details closed><summary>Utils</summary>

| File                        | Summary                                                                                                                                                                                                                                                                                                                        | Module                                                                           |
|:----------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------|
| Extensions.kt               | This code script offers two infix functions, one for displaying a Toast message with a context as a parameter, and another for toggling the clickable status of a View with a boolean value as a parameter.                                                                                                                    | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Extensions.kt               |
| WorkManagerHelper.kt        | This code script creates a OneTimeWorkRequest that sets constraints on a network type and input data, and adds a tag in order to upload a file specified by a given URI using the UploadWorker class.                                                                                                                          | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/WorkManagerHelper.kt        |
| Utils.kt                    | This code script provides a collection of helper methods for dealing with local file details, file input streams, network connectivity, Android dialog fragments, and more. It also contains utilities to parse file.io URLs and JSON responses, as well as a method to get the current date.                                  | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Utils.kt                    |
| Helpers.kt                  | This code script contains functions to get meta data (name and size) from a file, retrieve the file, and assemble the file into a FileEntity object with additional fields (date and days to expiry).                                                                                                                          | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Helpers.kt                  |
| FragmentHelperExtensions.kt | This code script provides two functions for adding and replacing fragments in an Android application. Both functions include a container ID, fragment, and optional tag, with each having a different transition animation. The code also adds the fragment to the back stack with the specified tag.                          | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/FragmentHelperExtensions.kt |
| MaterialIn.kt               | This code script provides an animation utility for Android views. It provides support for MaterialIn animations with custom delay and slide directions, while also handling different layout directions (RTL/LTR). It animates the view's alpha and translation, and includes interpolators for acceleration and deceleration. | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/MaterialIn.kt               |
| Constants.kt                | This code script is a global constants file used to store URLs, email address and other constants related to File I/O. It includes a base URL, expiration parameter, query symbol, default expiration in weeks, GitHub and Twitter URLs, an email address, postfix, and a time stamp format.                                   | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Constants.kt                |

</details>

<details closed><summary>Viewmodel</summary>

| File                      | Summary                                                                                                                                                                                                         | Module                                                                             |
|:--------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
| UploadHistoryViewModel.kt | This code script defines a ViewModel class that manages the upload history of a file-sharing application. It retrieves the list of uploaded files from a RoomDatabase and stores the data in a LiveData object. | app/src/main/java/com/thecoolguy/rumaan/fileio/viewmodel/UploadHistoryViewModel.kt |

</details>

<details closed><summary>Wrapper</summary>

| File               | Summary                                                                                             | Module                            |
|:-------------------|:----------------------------------------------------------------------------------------------------|:----------------------------------|
| gradle-wrapper.jar | This code script is unable to process a file that does not contain text or is not encoded in UTF-8. | gradle/wrapper/gradle-wrapper.jar |

</details>

<hr />

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> `[📌  INSERT-PROJECT-PREREQUISITES]`

### 💻 Installation

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
#run tests
```

<hr />


## 🛠 Future Development
- [X] [📌  COMPLETED-TASK]
- [ ] [📌  INSERT-TASK]
- [ ] [📌  INSERT-TASK]


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
7. Create a pull request to the original repository.
Open a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 🪪 License

This project is licensed under the `[📌  INSERT-LICENSE-TYPE]` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 🙏 Acknowledgments

[📌  INSERT-DESCRIPTION]


---

