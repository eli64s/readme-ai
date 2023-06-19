
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
file.io-Android-Client
</h1>
<h3>◦ Secure file sharing, now in your palm.</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/Kotlin-7F52FF.svg?style=for-the-badge&logo=Kotlin&logoColor=white" alt="Kotlin" />
<img src="https://img.shields.io/badge/Android-3DDC84.svg?style=for-the-badge&logo=Android&logoColor=white" alt="Android" />
<img src="https://img.shields.io/badge/Gradle-02303A.svg?style=for-the-badge&logo=Gradle&logoColor=white" alt="Gradle" />
<img src="https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white" alt="java" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="Markdown" />
</p>
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

The File.io Android Client project is an Android-based application for uploading files to remote servers using the Fuel HTTP library. The app includes a user interface for selecting and uploading files, as well as background tasks for handling file uploads, notifications, and database storage. The app also includes features such as swipe-to-delete and grouping uploads by date, making it a useful tool for managing file uploads on the go. Overall, this project provides a convenient and efficient way to upload files from an Android device to a remote server.

---

## ⚙️ Features

Feature | Description |
|-----|-----|
| **🏗 Architecture** | The codebase follows the MVVM architecture pattern. Data is stored in a local Room database and accessed through ViewModel classes, with UI components observing LiveData objects. The codebase also uses Android WorkManager for background tasks and follows a single activity pattern. |
| **📑 Documentation** | The codebase has inline comments and descriptive variable and function names, making it easier for developers to understand the code. However, some files have limited documentation, and the README could be more descriptive. |
| **🧩 Dependencies** | The codebase uses a variety of dependencies for Android development, including Android architecture components, Fuel, Gson, Kotlin, and Timber. It also includes libraries for handling crashes (Fabric.io and Firebase Crashlytics), permission dispatching, and notification handling. |
| **♻️ Modularity** | The codebase is modular, with each module responsible for a specific task or feature, such as `repository`, `ui`, and `utils`. This enhances code organization and makes it easier to maintain the app. |
| **✔️ Testing** | The codebase includes both unit tests and instrumented tests. The unit tests are located in the `test` folder and test individual methods and classes. The instrumented tests are located in the `androidTest` folder and test features such as Room database, file upload, and UI components. However, some files have limited test coverage, and more tests could be added to ensure code quality. |
| **⚡️ Performance** | The codebase uses background tasks and WorkManager to handle long-running operations, such as file uploads and database clearing. It also includes caching to improve performance and minimize network usage. However, there is room for improvement in terms of optimizing network requests and reducing data usage. |
| **🔒 Security** | The codebase does not handle sensitive information, but it does include measures to ensure user privacy, such as file encryption and URL expirations. However, some files have limited security measures, and the codebase could benefit from a security audit to ensure it adheres to best practices. |
| **🔀 Version Control** | The codebase is hosted on GitHub and includes a history of commits and pull requests. It follows a branching strategy, with separate branches for feature development, bug fixes, and releases. However, some files have limited commit history, and the codebase could benefit from more consistent and descriptive commits. |
| **🔌 Integrations** | The codebase includes integrations with several third-party services, such as Fabric.io and Firebase Crashlytics for crash reporting, and Google Services for authentication and app indexing. It also includes integration with Material Design components. |
| **📈 Scalability** | The codebase is designed with scalability in mind, with a modular and layered architecture. It uses Android architecture components, such as ViewModel and LiveData

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

| File                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                         | Module                                                                                |
|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------|
| MainActivity.kt          | The provided code snippet is an implementation of an Android activity that allows the user to upload a file for storage. It initializes the activity's UI layout and handles user events, such as selecting a file, uploading it, and displaying progress and result information. The code also includes permission handling and network connectivity checks.                                                                   | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/MainActivity.kt          |
| ErrorActivity.kt         | The provided code snippet is an Android activity for handling runtime crashes. It displays an error layout and overrides the onBackPressed method to finish the activity and exit the app when back button is pressed.                                                                                                                                                                                                          | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/ErrorActivity.kt         |
| UploadHistoryActivity.kt | The provided code snippet is an implementation of an activity in an Android app that displays a list of uploaded files and allows the user to delete individual items or clear the entire history. The activity uses RecyclerView and ViewModel to handle data loading and displaying, and WorkManager to handle background work requests. It also uses swipe-to-delete functionality and animation to enhance user experience. | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/UploadHistoryActivity.kt |
| AboutActivity.kt         | The code snippet defines an AboutActivity that extends AppCompatActivity. It inflates the menu and sets up the toolbar with a display home as up button. It also processes clicks on the "Open Source" menu item and starts the LicenseActivity.                                                                                                                                                                                | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/AboutActivity.kt         |
| LicenseActivity.kt       | The code snippet is an implementation of the LicenseActivity class that extends the MaterialAboutActivity class. The class generates a list of open-source licenses for various libraries used in the application. The getMaterialAboutList function creates license cards for each library and returns them as a MaterialAboutList.                                                                                            | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/LicenseActivity.kt       |

</details>

<details closed><summary>App</summary>

| File         | Summary                                                                                                                                                                                                                                                                                                                                                                                          | Module           |
|:-------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| build.gradle | The provided code snippet specifies the plugins and dependencies used in an Android application. It includes plugins for Kotlin, Fabric, and permission dispatching, and dependencies for AndroidX libraries, Firebase Crashlytics, Android architecture components, Fuel, Gson, and Timber. It also sets build configurations for different build types and applies the Google Services plugin. | app/build.gradle |

</details>

<details closed><summary>Fileio</summary>

| File                               | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Module                                                                                   |
|:-----------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------|
| ExampleInstrumentedTest.kt         | This code snippet defines an Android instrumented test for a file I/O app, using JUnit and Espresso testing frameworks. The test verifies if the app's package name matches the expected one, using the AndroidJUnit4 test runner and the ActivityTestRule to launch the main activity. The test is annotated with @SmallTest, ensuring that it runs quickly and without any UI interactions.                                                           | app/src/androidTest/java/com/thecoolguy/rumaan/fileio/ExampleInstrumentedTest.kt         |
| FileEntityDaoTest.java             | The provided code snippet is a JUnit test class for testing the functionalities of a RoomDatabase that handles file uploads. It includes methods for testing count of rows, inserting and retrieving data, and saving multiple items. The test cases involve creating FileEntity objects with various attributes and asserting their properties against expected values. The test class uses the AndroidJUnit4 runner and is annotated with @LargeTest. | app/src/androidTest/java/com/thecoolguy/rumaan/fileio/FileEntityDaoTest.java             |
| UploadHistoryInstrumentedTest.java | The code snippet imports necessary classes, defines a Matcher and a Rule, and initializes a Room database with sample data for testing. The "check_longPressItemDelete" test function is currently empty and requires further implementation.                                                                                                                                                                                                           | app/src/androidTest/java/com/thecoolguy/rumaan/fileio/UploadHistoryInstrumentedTest.java |
| ExampleUnitTest.java               | This is a JUnit test class that verifies the correctness of the addition operation. In this case, it asserts that the sum of 2 and 2 is equal to 4. The test method is annotated with @Test, which indicates that it should be executed by the JUnit framework during testing.                                                                                                                                                                          | app/src/test/java/com/thecoolguy/rumaan/fileio/ExampleUnitTest.java                      |
| UploadRepositoryTest.java          | The code snippet is a unit test for a method in the UploadRepository class. The test checks whether the getExpireUrl method of the URLParser class returns the expected URL based on a given number of days. It also checks whether the URL constructed using the ConstantsKt class matches the expected URL.                                                                                                                                           | app/src/test/java/com/thecoolguy/rumaan/fileio/UploadRepositoryTest.java                 |
| UrlTest.java                       | The code snippet tests the functionality of a method named'parseEncryptUrl' which is part of the'URLParser' utility class. The method takes in a URL string with encrypted parameters and returns a URL string with decrypted parameters. The test case checks if the method accurately returns the expected URL string.                                                                                                                                | app/src/test/java/com/thecoolguy/rumaan/fileio/UrlTest.java                              |
| FileEntityTest.java                | The code snippet defines a JUnit test class for a FileEntity model, with two tests to set and check the name and URL values of the entity. It uses the "assertEquals" and "assertNotNull" assertion methods to ensure the values are correctly set and retrieved.                                                                                                                                                                                       | app/src/test/java/com/thecoolguy/rumaan/fileio/FileEntityTest.java                       |

</details>

<details closed><summary>Fragments</summary>

| File                       | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Module                                                                                 |
|:---------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------|
| NoNetworkDialogFragment.kt | The code defines a DialogFragment class that displays an alert dialog when there is no network connection. It uses a custom XML layout file and listens to a button click event to dismiss the dialog. The class also implements a DialogClickListener interface to communicate with the activity that launched the dialog.                                                                                                                                                                                                                                            | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/NoNetworkDialogFragment.kt |
| HomeFragment.kt            | The code defines a fragment that inflates a layout and handles the button click event. It also implements an interface to communicate with the parent activity. The fragment can be instantiated with parameters using the `newInstance()` static method.                                                                                                                                                                                                                                                                                                              | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/HomeFragment.kt            |
| ResultFragment.kt          | The provided code snippet includes a Kotlin class `ResultFragment` that extends the `Fragment` class. It inflates the `layout_result` XML file, receives arguments, and updates the UI elements `text_link`, `text_days`, and `btn_done` accordingly. Moreover, a click listener is set on the `linkText` view to copy the text to the clipboard and show a toast message. Finally, a companion object is created to define constants such as `PARAM_URL` and `PARAM_DAYS` and implement a factory method `newInstance` to create an instance of the `ResultFragment`. | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/ResultFragment.kt          |

</details>

<details closed><summary>Listeners</summary>

| File                             | Summary                                                                                                                                                                                                                                                                                               | Module                                                                                    |
|:---------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------|
| DialogClickListener.kt           | The provided code defines an interface named DialogClickListener, which has a single function named onDialogPositiveClick. This function takes in two parameters: a Dialog object and a Fragment object. This interface can be used to handle click events on a dialog box in an Android application. | app/src/main/java/com/thecoolguy/rumaan/fileio/listeners/DialogClickListener.kt           |
| OnFragmentInteractionListener.kt | The code snippet defines an interface named "OnFragmentInteractionListener" with two functions: "onUploadFileClick()" and "onDone()". These functions are intended to be implemented by other classes to handle events related to file uploads or completion of an action.                            | app/src/main/java/com/thecoolguy/rumaan/fileio/listeners/OnFragmentInteractionListener.kt |

</details>

<details closed><summary>Repository</summary>

| File                    | Summary                                                                                                                                                                                                                                                                                                                                                         | Module                                                                            |
|:------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
| UploadHistoryWorkers.kt | The code snippet provides two Worker classes-ClearHistoryWorker and DeleteSingleItemWorker-for handling background tasks. ClearHistoryWorker clears the entire upload history data from the database, while DeleteSingleItemWorker deletes a specific upload history item identified by an ID from the database.                                                | app/src/main/java/com/thecoolguy/rumaan/fileio/repository/UploadHistoryWorkers.kt |
| UploadWorker.kt         | The provided code snippet is for an Android WorkManager that is responsible for uploading files to a remote server using the Fuel HTTP library. The code defines a Worker that performs the file upload and handles notification and database storage. It also defines constants for output data keys and exposes a function for triggering the upload process. | app/src/main/java/com/thecoolguy/rumaan/fileio/repository/UploadWorker.kt         |

</details>

<details closed><summary>Root</summary>

| File            | Summary                                                                                                                                                                                                                                    | Module          |
|:----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------|
| build.gradle    | This code snippet is a build script for a Gradle project. It sets the Kotlin version and includes dependencies such as the Android Gradle plugin, Fabric.io, and Google Services. It also sets up repositories to be used by all projects. | build.gradle    |
| settings.gradle | This code snippet is a part of an Android project and includes the main app module. It provides the necessary configuration to build and run the app within the Android Studio environment.                                                | settings.gradle |

</details>

<details closed><summary>Ui</summary>

| File                        | Summary                                                                                                                                                                                                                                                                                                                                                                                     | Module                                                                        |
|:----------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------|
| FileioApplication.kt        | The provided code snippet is an implementation of the FileioApplication class that extends the Application class in the Android framework. The class includes housekeeping for logs with the Timber library and configuration for a custom activity to handle app crashes with the CaocConfig library. The class also includes a companion object with a private constant for the tag name. | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/FileioApplication.kt        |
| UploadHistoryListAdapter.kt | The code defines a RecyclerView adapter for displaying a list of uploaded files, with the ability to group and display files by date and copy their URLs to the clipboard upon click. The adapter supports swapping the displayed list of files and removing files from the list. It also includes two ViewHolder inner classes to define the layout of date and file items in the list.    | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/UploadHistoryListAdapter.kt |
| SwipeToDeleteCallBack.kt    | The provided code defines an abstract class for implementing swipe-to-delete functionality in a RecyclerView in an Android app. It sets up a red delete background and an icon for swiping, and disables swiping for certain items. The class overrides necessary methods from the ItemTouchHelper.SimpleCallback class to properly implement the swipe-to-delete feature.                  | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/SwipeToDeleteCallBack.kt    |
| NotificationHelper.kt       | This code creates a notification on successful upload of a file. It sets up a notification channel and builder with appropriate settings, including the file name and URL. It also creates a pending intent to open the app's upload history activity when the notification is clicked.                                                                                                     | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/NotificationHelper.kt       |

</details>

<details closed><summary>Utils</summary>

| File                        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                       | Module                                                                           |
|:----------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------|
| Extensions.kt               | This code snippet provides two extension functions for Android development. The first creates a Toast message with a specified string and displays it on the screen. The second function toggles the clickability of a View based on a boolean input value. These functions aim to streamline common Android development tasks.                                                                                                               | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Extensions.kt               |
| WorkManagerHelper.kt        | This code snippet provides utility functions to create a OneTimeWorkRequest for uploading a file to a server. The createUploadWork function takes a file URI as input and sets constraints for the work request, requiring a network connection. The resulting OneTimeWorkRequest is tagged with a constant UPLOAD_WORK_TAG and includes an instance of the UploadWorker class.                                                               | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/WorkManagerHelper.kt        |
| Utils.kt                    | The provided code snippet contains a set of utility functions for handling file input/output and Android-related tasks. It includes functions for retrieving file details from a URI, opening file streams, checking network connectivity, showing fragments and dialogs, copying text to clipboard, and parsing file.io URLs and JSON responses. The code is organized into three wrapper classes: Utils, Android, and URLParser/JSONParser. | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Utils.kt                    |
| Helpers.kt                  | This code snippet provides utility functions for handling file operations in Android. The functions include methods for obtaining metadata and retrieving a file from a given URI. Additionally, there is a function to compose a `FileEntity` object from a `File` object and a `Response` object, with relevant information such as file name, URI, creation date, and expiration date.                                                     | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Helpers.kt                  |
| FragmentHelperExtensions.kt | The provided code snippet contains two extension functions for the FragmentManager class in the Android Jetpack library. These functions facilitate the addition and replacement of fragments in a container within an Android application, while also providing optional tag functionality. The addFragment function sets a close transition animation, and the replaceFragment function sets a fade transition animation.                   | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/FragmentHelperExtensions.kt |
| MaterialIn.kt               | The code snippet is a Kotlin object that provides a method to animate a view with a material design-like entrance effect. It converts gravity values to account for right-to-left layout and handles animations for both the parent view and child views. The animation includes a fade-in and slide-in effect with customizable delay and direction.                                                                                         | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/MaterialIn.kt               |
| Constants.kt                | The code snippet defines some constant values in the com.thecoolguy.rumaan.fileio.utils package, including a base URL, expire parameter, default expire weeks, and various URLs. It also includes a postfix for links, and a timestamp format. These constants are likely used throughout the application for consistency and ease of maintenance.                                                                                            | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Constants.kt                |

</details>

<details closed><summary>Viewmodel</summary>

| File                      | Summary                                                                                                                                                                                                                                                                                                                   | Module                                                                             |
|:--------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
| UploadHistoryViewModel.kt | The code creates a ViewModel for displaying a list of uploaded files in an Android application. It retrieves the list of files from a local database using LiveData and initializes it in the ViewModel's constructor. The ViewModel extends AndroidViewModel, allowing it to maintain data across configuration changes. | app/src/main/java/com/thecoolguy/rumaan/fileio/viewmodel/UploadHistoryViewModel.kt |

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
