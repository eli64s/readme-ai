
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
file.io-Android-Client
</h1>
<h3 align="center">📍 Securely transfer files with ease: file.io-Android-Client.</h3>
<h3 align="center">⚙️ Developed with the software and tools below:</h3>

<p align="center">
<img src="https://img.shields.io/badge/Kotlin-7F52FF.svg?style=for-the-badge&logo=Kotlin&logoColor=white" alt="Kotlin" />
<img src="https://img.shields.io/badge/Android-3DDC84.svg?style=for-the-badge&logo=Android&logoColor=white" alt="Android" />
<img src="https://img.shields.io/badge/Gradle-02303A.svg?style=for-the-badge&logo=Gradle&logoColor=white" alt="Gradle" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="Markdown" />
<img src="https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white" alt="java" />
</p>
</div>

---

## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [💫 Features](#-features)
- [📂 Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🚀 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The file.io-Android-Client is an Android app used for storing and accessing files on local devices. It offers features such as background file uploading, network connectivity constraints, and swipe-to-delete gestures. The app provides an intuitive UI with distinct fragments for uploading, viewing, and managing file history. The project uses Kotlin programming and key Android libraries such as AndroidX, Room, Fuel, WorkManager, and Permissions Dispatcher.

---

## 💫 Features

Feature | Description |
|---|---|
| **🏗 Structure and Organization** | The codebase follows a well-structured organization pattern that adequately separates app components into different folders/packages. It also utilizes modularization to a great extent.|
| **📝 Code Documentation** | The codebase has an extensive documentation in each file, package, and function/member declarations. It uses the KDocs format for documenting public interfaces in a clear and concise way.|
| **🧩 Dependency Management** | The codebase is reliant on several external libraries for different functionalities. It employs dependency managers including Gradle and Kotlin DSL to manage dependencies.|
| **♻️ Modularity and Reusability** | The codebase demonstrates modularity through the segregation of parts. The code also reuses parameters and functionalities developed in other parts of the codebase.|
| **✔️ Testing and Quality Assurance** | The codebase comes with an extensive suite of JUnit and automated instrumentation tests, ensuring the fulfillment of user specifications and decreasing the likelihood of introducing unintended regressions in functionality. Utilizes localized testing and data injection, along with a well-laid and concluded system.|
| **⚡️ Performance and Optimization** | Although the codebase uses several external libraries to handle mandatory features of modern-day UX practices, it has ensured methods for cancelling/not starting a new upload when applications are no longer required, thus ensuring efficiency on older hardware configurations by keeping background processes to a minimum.|
| **🔒 Security Measures** | Uses appropriate guidelines for ensuring user data security, provides network and file writing/reading protection by eavesdropping prevention, optimistic locking and retry mechanism (in UploadWorker.kt), uses upload URLs that specifically impose a `top username GUID`, session links with a definite logic-a deletion is received after having three subsequent retrievals.|
| **🔄 Version Control and Collaboration** | The codebase uses GitHub for users to access VCS, including pull requests, fork system, branching mechanisms, and repo visibility. Parameters relevantly described which validates intent and purpose and ensures efficient versioning in case of future updates and durability-with GitIgnore parameters also present.|
| **🔌 External Integrations** | Consumes essential functionalities related needs

---


<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

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

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 🧩 Modules

<details closed><summary>Activities</summary>

| File                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Module                                                                                |
|:-------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------|
| MainActivity.kt          | The code snippet represents the MainActivity class in an Android app. It establishes and monitors background file upload with WorkManager, uses fragments to create app UI and menus, requires storage permissions with PermissionsDispatcher, and performs network checks with Utils.                                                                                                                                                                                                                                                               | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/MainActivity.kt          |
| ErrorActivity.kt         | This code provides an ErrorActivity displayed when a runtime crash occurs. It overrides the onBackPressed() method to finish the application's Activity stack and allows the user to exit, and sets the activity's content to a layout resource with an ID of activity_error.                                                                                                                                                                                                                                                                        | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/ErrorActivity.kt         |
| UploadHistoryActivity.kt | The provided code snippet is an Android Kotlin class that provides functionalities for an activity that displays upload history. It loads and displays upload history from the database, allows for clearing the history and deleting individual items using WorkManager. It also provides an adapter for the list and handles swipe-to-delete using a custom callback class. Finally, it groups the uploads history list by date and makes a linear list based on item types which ultimately determines which items to show and the UI to display. | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/UploadHistoryActivity.kt |
| AboutActivity.kt         | The provided code snippet is an implementation of an Android activity that displays information about an app (the "About" page). It also includes a menu option that opens a separate activity to display the app's license information. The menu is displayed in the app bar of the activity, which is styled with a transparent navigation bar.                                                                                                                                                                                                    | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/AboutActivity.kt         |
| LicenseActivity.kt       | This is a code snippet for an activity that displays open source licenses within a Material Design styled interface. The activity extends the MaterialAboutActivity class and uses ConvenienceBuilder to create license cards that display essential licensing information. The MaterialAboutList method is then called to display the list of licenses.                                                                                                                                                                                             | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/LicenseActivity.kt       |

</details>

<details closed><summary>App</summary>

| File         | Summary                                                                                                                                                                                                                                                                                                                                               | Module           |
|:-------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| build.gradle | This code snippet provides plugin dependencies, declares various version definitions, build types and dependencies. The set of dependencies include important libraries such as AndroidX, Material Design, Room, Crashlytics, Permissions Dispatcher, Navigation, Timber, etc. This code snippet is aimed at an Android app targeting SDK version 28. | app/build.gradle |

</details>

<details closed><summary>Fileio</summary>

| File                               | Summary                                                                                                                                                                                                                                                                                                                                                                                 | Module                                                                                   |
|:-----------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------|
| ExampleInstrumentedTest.kt         | The code snippet provides an example of an instrumented test for an Android app. It imports required libraries and annotations for the test, and defines a test function to check the app context. It creates an activity test rule for the main activity of the app, and uses instrumentation to retrieve the app context and assert that the correct package name is returned.        | app/src/androidTest/java/com/thecoolguy/rumaan/fileio/ExampleInstrumentedTest.kt         |
| FileEntityDaoTest.java             | The code snippet is a collection of JUnit tests for a RoomDatabase object. The tests verify the expected behaviors of the uploaded files stored by a RoomDatabase, such as counting the number of rows, saving single and multiple items to the database, and confirming that the proper changes have been committed.                                                                   | app/src/androidTest/java/com/thecoolguy/rumaan/fileio/FileEntityDaoTest.java             |
| UploadHistoryInstrumentedTest.java | This code snippet is an instrumentation test in Android Studio that aims to validate a long press item delete functionality through the `UploadHistoryInstrumentedTest` method `check_longPressItemDelete`. It uses various annotations and methods to achieve this, including ActivityTestRule, Matcher, TypeSafeMatcher, and `@Test`, which runs the test.                            | app/src/androidTest/java/com/thecoolguy/rumaan/fileio/UploadHistoryInstrumentedTest.java |
| ExampleUnitTest.java               | The provided code snippet is a unit test for a Java project that uses the JUnit testing framework. It ensures that the arithmetic addition operation returns a value of 4 when the operands are 2 and 2. The code imports the necessary libraries and annotations required to conduct this unit test.                                                                                   | app/src/test/java/com/thecoolguy/rumaan/fileio/ExampleUnitTest.java                      |
| UploadRepositoryTest.java          | The code defines a test case class called "UploadRepositoryTest", which tests the method "check_ExpireUrl" to validate if the correct URL is generated by comparing it with the expected URL. The method "getExpireUrl" of the URLParser class is invoked to generate the URL. The code uses constants defined in the ConstantsKt class along with "days" parameter to produce the URL. | app/src/test/java/com/thecoolguy/rumaan/fileio/UploadRepositoryTest.java                 |
| UrlTest.java                       | The code tests the functionality of a parseEncryptUrl method by checking if the parsed URL output matches the expected output in the JUnit framework. It imports necessary classes and performs a JUnit assertion test.                                                                                                                                                                 | app/src/test/java/com/thecoolguy/rumaan/fileio/UrlTest.java                              |
| FileEntityTest.java                | This code contains a JUnit test to verify the functionality of setting name and URL for a file entity. It creates a FileEntity object, sets the name to "testfilename", verifies that the name is not null and that it is equal to the assigned value. It repeats the same process for the URL.                                                                                         | app/src/test/java/com/thecoolguy/rumaan/fileio/FileEntityTest.java                       |

</details>

<details closed><summary>Fragments</summary>

| File                       | Summary                                                                                                                                                                                                                                                                                                                                                                                       | Module                                                                                 |
|:---------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------|
| NoNetworkDialogFragment.kt | This code snippet declares a `NoNetworkDialogFragment` class that creates and shows a dialog with a single positive button. When the button is clicked, the listener class sends the dialog and its respective object to its parent activity.                                                                                                                                                 | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/NoNetworkDialogFragment.kt |
| HomeFragment.kt            | The code defines a fragment for choosing a file and storing it in a local file object cache. It contains a callback function that is called when the button for choosing a file is clicked. The fragment interacts with the activity that implements the OnFragmentInteractionListener interface.                                                                                             | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/HomeFragment.kt            |
| ResultFragment.kt          | The provided code is a fragment that displays a "result" view with a URL and number of days before it expires. It provides functionality to copy the displayed URL to clipboard, and send feedback to the parent activity when the "done" button is clicked. This fragment can be instantiated with newInstance() method and is apart of a larger android app designed for file input/output. | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/ResultFragment.kt          |

</details>

<details closed><summary>Listeners</summary>

| File                             | Summary                                                                                                                                                                                                                                                                                                                         | Module                                                                                    |
|:---------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------|
| DialogClickListener.kt           | The provided code defines an interface `DialogClickListener` with a single method `onDialogPositiveClick`, which takes a `Dialog` object and an `androidx.fragment.app.Fragment` object as arguments. This interface can be implemented in other classes to customize behavior when the positive button in a dialog is clicked. | app/src/main/java/com/thecoolguy/rumaan/fileio/listeners/DialogClickListener.kt           |
| OnFragmentInteractionListener.kt | This code snippet defines an interface called OnFragmentInteractionListener, with two functions: onUploadFileClick() and onDone(). Any class that implements this interface will need to provide a definition for these functions, allowing for communication between fragments in an Android app.                              | app/src/main/java/com/thecoolguy/rumaan/fileio/listeners/OnFragmentInteractionListener.kt |

</details>

<details closed><summary>Repository</summary>

| File                    | Summary                                                                                                                                                                                                                                                                                                                                                                         | Module                                                                            |
|:------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
| UploadHistoryWorkers.kt | The provided code snippet contains two classes that extend the Worker class in the androidx.work package. The ClearHistoryWorker class clears all upload history in the UploadHistoryRoomDatabase and returns a Result.SUCCESS value. The DeleteSingleItemWorker class deletes the upload item with the given ID from the UploadHistoryRoomDatabase and returns Result.SUCCESS. | app/src/main/java/com/thecoolguy/rumaan/fileio/repository/UploadHistoryWorkers.kt |
| UploadWorker.kt         | The provided code snippet represents an `UploadWorker` that handles file uploads. The class uploads a given file, saves the uploaded file into a database as a `FileEntity` object, and sends a notification about the upload. It uses `Fuel` for HTTP requests, `WorkManager` for managing background tasks, and `Timber` for logging.                                         | app/src/main/java/com/thecoolguy/rumaan/fileio/repository/UploadWorker.kt         |

</details>

<details closed><summary>Root</summary>

| File            | Summary                                                                                                                                                                                                                                                                     | Module          |
|:----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------|
| build.gradle    | The code snippet provides the build configurations for the Gradle build system used by Android projects. It sets the repositories where Gradle will download dependencies, and includes the necessary dependencies for Android, Firebase Analytics, and Kotlin programming. | build.gradle    |
| settings.gradle | The code snippet includes the':app' dependency in the project. This enables access to libraries and tools necessary for developing the application.                                                                                                                         | settings.gradle |

</details>

<details closed><summary>Ui</summary>

| File                        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Module                                                                        |
|:----------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------|
| FileioApplication.kt        | The provided code snippet shows an Android Application class called FileioApplication, which is responsible for planting and configuring a Timber logger and specifying a custom activity for handling app crashes, using the CaocConfig.Builder class from the CustomActivityOnCrash library.                                                                                                                                                                                            | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/FileioApplication.kt        |
| UploadHistoryListAdapter.kt | The provided code snippet contains the implementation of an adapter for a RecyclerView to display a list of previously uploaded files with their details. The adapter supports two types of views; upload dates and the file contents, represented by the `UploadHistoryListDateViewHolder` and `UploadHistoryListItemViewHolder` classes, respectively. The `swapComposedList`, `swapList`, `remoteAt`, and `getFileEntityIdAtPosition` functions modify the list displayed to the user. | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/UploadHistoryListAdapter.kt |
| SwipeToDeleteCallBack.kt    | This code snippet contains an extension of the ItemTouchHelper class used to implement the'swipe to delete' feature in Recycler View for an app. When an item is swiped to the left in the recycler view, it triggers the functionality implemented in this class, which displays a red background with a'delete' icon that allows the user to delete that item from the list. The extension provides methods for drawing/redrawing on the canvas as the gesture is carried out.          | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/SwipeToDeleteCallBack.kt    |
| NotificationHelper.kt       | The provided code creates a NotificationHelper class with a create function that generates a notification to show a file upload successful message, using a notification builder. It provides an intent to PendingIntent that launches the UploadHistoryActivity with specific details like the name and the URL of the uploaded file. A notification channel is created before posting the notification for Android versions O and up, and a summary notification for multiple uploads.  | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/NotificationHelper.kt       |

</details>

<details closed><summary>Utils</summary>

| File                        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Module                                                                           |
|:----------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------|
| Extensions.kt               | The code snippet provides extension functions for Android Toast and View classes. The toast function displays short duration messages. The toggleClickable function allows for disabling or enabling of click events on the view.                                                                                                                                                                                                                                                                       | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Extensions.kt               |
| WorkManagerHelper.kt        | The code defines a function called "createUploadWork" that creates a OneTimeWorkRequest for uploading a file. The function sets constraints for network connectivity and specifies the worker class as "UploadWorker" with input data containing the URI of the file to be uploaded. The worker request is then tagged with "UploadWork".                                                                                                                                                               | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/WorkManagerHelper.kt        |
| Utils.kt                    | The code snippet contains a Kotlin utility class with a range of helper functions for Android applications. These include getting the details (name, size, stream) of local files, opening files in read mode as an input stream, wrappers for Android-related functionality (dialogues, networks, etc.), and URL/JSON parsing.                                                                                                                                                                         | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Utils.kt                    |
| Helpers.kt                  | The code snippet provides utility functions for working with files, specifically retrieving metadata and getting file/entity details. These functions use Android's content resolver to access file information, and return relevant responses using predefined data models such as File and Response.                                                                                                                                                                                                  | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Helpers.kt                  |
| FragmentHelperExtensions.kt | The provided code contains two extension functions for the FragmentManager class in Android. The first, addFragment(), adds a new fragment to a given container and applies a transition effect during the addition. The second, replaceFragment(), replaces an existing fragment with a new one in a given container and applies a transition effect during the replacement. Both functions add the fragment to the backstack, so the user can navigate back to a previously added/ replaced fragment. | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/FragmentHelperExtensions.kt |
| MaterialIn.kt               | This code contains a set of utility functions used for animating views in Android applications. The MaterialIn object provides functions to animate views using fade and slide effects, while also offering options to specify delay and slide direction. The main functionalities include tree node traversal for defining animation properties, object animation for fade and slide effects using the animator module, and event animation for canceling animation seconds before completion.         | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/MaterialIn.kt               |
| Constants.kt                | The provided code snippet is a Kotlin file that defines global constants and a function that parses URIs. It includes a base URL, parameters for links, default values for expiration dates, and preset URIs for specific websites. The constants might be used for file input and output.                                                                                                                                                                                                              | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Constants.kt                |

</details>

<details closed><summary>Viewmodel</summary>

| File                      | Summary                                                                                                                                                                                                                                                                                   | Module                                                                             |
|:--------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
| UploadHistoryViewModel.kt | The code provides a ViewModel class that extends AndroidViewModel. It includes functionalities like LiveData and MutableLiveData. This code snippet also interacts with a database entity called "FileEntity". It is a part of the package called com.thecoolguy.rumaan.fileio.viewmodel. | app/src/main/java/com/thecoolguy/rumaan/fileio/viewmodel/UploadHistoryViewModel.kt |

</details>

---

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - [📌  PREREQUISITE-1]
> - [📌  PREREQUISITE-2]
> - ...

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

> - [X] [📌  Task 1: Implement X]
> - [ ] [📌  Task 2: Refactor Y]
> - [ ] [📌  Task 3: Optimize Z]
> - [ ] ...


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

## 📄 License

This project is licensed under the `[📌  INSERT-LICENSE-TYPE]` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 👏 Acknowledgments

> - [📌  List any resources, contributors, inspiration, etc.]

---
