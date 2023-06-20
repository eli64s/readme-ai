
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
file.io-Android-Client
</h1>
<h3>◦ Securely share files on-the-go with file.io Android!</h3>
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

The file.io-Android-Client repository contains an Android app that allows users to upload files to the file.io service and keep track of their upload history. The app utilizes WorkManager for background uploading and Room for local storage. It also includes features such as swipe-to-delete, clear upload history, and notifications. Overall, the app simplifies the file uploading process and provides a convenient way for users to manage and track their uploads.

---

## ⚙️ Features

Feature | Description |
|-----|-----|
| **🏗 Architecture** | The codebase follows the Model-View-ViewModel (MVVM) architectural pattern, separating concerns between data models, UI components, and the business logic. It also implements the Android Jetpack components such as LiveData and Room for efficient data management. |
| **📑 Documentation** | The codebase includes documentation in the form of code comments, describing the purpose and functionality of each class and method. README.md file also provides a brief overview of the project and instructions on how to set up and run the application. |
| **🧩 Dependencies** | The codebase utilizes various libraries such as Kotlin, Firebase Crashlytics, Room, Navigation, and Fuel. It also includes plugins for Google services and Fabric, and sets up dependencies for JUnit and Espresso testing frameworks. |
| **♻️ Modularity** | The codebase follows a modular approach, with each feature separated into different packages and classes, making it easier to maintain and modify. The use of interfaces and abstractions also helps in decoupling dependencies and promoting code reusability. |
| **✔️ Testing** | The codebase includes both unit tests and instrumentation tests, covering various features such as database operations, network connectivity, and UI interactions. The tests utilize frameworks such as JUnit, AndroidJUnit, and Espresso and follow best practices for testing, such as using the Arrange-Act-Assert (AAA) pattern. |
| **⚡️ Performance** | The codebase implements efficient data management techniques such as Room's caching and LiveData's observer pattern, reducing the need for multiple database queries and allowing for real-time updates. It also uses WorkManager to perform background tasks and notifications to inform the user of task completion. |
| **🔒 Security** | The codebase utilizes HTTPS for network communication and incorporates Firebase Crashlytics for crash reporting. It also includes functionality that ensures the confidentiality of uploaded files, such as expiring file links and using encryption. |
| **🔀 Version Control** | The codebase is hosted on GitHub and follows the Git version control system, allowing for efficient collaboration and history tracking. It also includes a gitignore file to exclude unnecessary files from versioning. |
| **🔌 Integrations** | The codebase includes integrations with Google services such as Firebase Crashlytics, as well as Fabric, a mobile app analytics platform. It also incorporates various Android Jetpack components and libraries such as Room, Navigation, and LiveData. |
| **📈 Scalability** | The codebase follows best practices such as modular architecture, efficient data management techniques, and code reusability, allowing for easy expansion and scalability. The use of WorkManager also ensures that long-running tasks do not affect the app's performance. |

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

| File                     | Summary                                                                                                                                                                                                                                                                                                                        | Module                                                                                |
|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------|
| MainActivity.kt          | This code defines the main activity of a file uploading app, implementing permission requests and utilizing WorkManager to upload files in the background. It also sets up fragments for different screens of the app, handles menu item clicks, and provides implementations for dialog and fragment interactions.            | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/MainActivity.kt          |
| ErrorActivity.kt         | The provided code snippet is an ErrorActivity class in an Android app that extends AppCompatActivity. The class is responsible for handling any runtime crashes in the app and displays a view defined in the activity_error layout resource file. It also includes a method to close the app when the back button is pressed. | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/ErrorActivity.kt         |
| UploadHistoryActivity.kt | The code defines the functionality of an activity that displays a list of upload history. The activity provides the option to clear the history, remove individual items, and handle swipe left to delete an item. It also groups the list based on date and displays it in a RecyclerView using a custom adapter.             | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/UploadHistoryActivity.kt |
| AboutActivity.kt         | The code snippet provides an implementation of an activity that displays information about the app. It inflates a menu layout, sets a transparent navigation theme, and provides an option to navigate to a license activity upon selecting a menu item.                                                                       | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/AboutActivity.kt         |
| LicenseActivity.kt       | HTTPStatusError: 429                                                                                                                                                                                                                                                                                                           | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/LicenseActivity.kt       |

</details>

<details closed><summary>App</summary>

| File         | Summary                                                                                                                                                                                                                                                                                                                                   | Module           |
|:-------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| build.gradle | This code snippet sets up an Android application using various plugins and dependencies such as Kotlin, Firebase Crashlytics, Room, Navigation, and Fuel. It also configures build types for release and debug modes, and includes test dependencies for AndroidJUnitRunner and Espresso. Finally, it applies the Google Services plugin. | app/build.gradle |

</details>

<details closed><summary>Fileio</summary>

| File                               | Summary                                                                                                                                                                                                                                                                                                                                                                               | Module                                                                                   |
|:-----------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------|
| ExampleInstrumentedTest.kt         | This code snippet is an example of an Android instrumentation test for a file IO application. It uses the JUnit framework and AndroidJUnit4 runner to test the MainActivity class. The test verifies that the app context has the expected package name. The test rule is implemented using the ActivityTestRule class.                                                               | app/src/androidTest/java/com/thecoolguy/rumaan/fileio/ExampleInstrumentedTest.kt         |
| FileEntityDaoTest.java             | The code is a set of JUnit tests for a RoomDatabase in an Android app. It tests the functionality to count the number of rows, insert and retrieve items, and save multiple items in the database. The code initializes and closes the in-memory database.                                                                                                                            | app/src/androidTest/java/com/thecoolguy/rumaan/fileio/FileEntityDaoTest.java             |
| UploadHistoryInstrumentedTest.java | The code snippet contains an instrumentation test for the UploadHistoryActivity class in an Android application. It sets up a Room database, populates it with test data, and provides a matcher function to check for a file's name in the database. The test itself is currently empty, but it is likely to test the deletion functionality of a list item when it is long-pressed. | app/src/androidTest/java/com/thecoolguy/rumaan/fileio/UploadHistoryInstrumentedTest.java |
| ExampleUnitTest.java               | This code defines a unit test for the addition_isCorrect method. It imports the necessary classes from the JUnit framework and uses the assertEquals method to check if the sum of 2 and 2 is equal to 4. This is a simple example of unit testing in Java.                                                                                                                           | app/src/test/java/com/thecoolguy/rumaan/fileio/ExampleUnitTest.java                      |
| UploadRepositoryTest.java          | The code tests the functionality of the `getExpireUrl()` method in the `UploadRepository` class that generates a file upload expiration URL. It compares the generated URL with a predefined URL string and also validates the URL against a constant base URL and URL query parameters. The test ensures that the `getExpireUrl()` method works correctly and consistently.          | app/src/test/java/com/thecoolguy/rumaan/fileio/UploadRepositoryTest.java                 |
| UrlTest.java                       | The code snippet is a JUnit test for the `parseEncryptUrl` method in the `Utils.URLParser` class. It checks if the method correctly extracts the URL without the `/dwnld` path from a given encrypted URL from the `file.io` service. The test asserts that the expected output matches the actual output.                                                                            | app/src/test/java/com/thecoolguy/rumaan/fileio/UrlTest.java                              |
| FileEntityTest.java                | The provided code snippet is a unit test for the FileEntity class in a file input/output package. The test ensures that the FileEntity's name and URL are properly set and get methods return the expected values. The test uses the JUnit testing framework.                                                                                                                         | app/src/test/java/com/thecoolguy/rumaan/fileio/FileEntityTest.java                       |

</details>

<details closed><summary>Fragments</summary>

| File                       | Summary                                                                                                                                                                                                                                                                                                                                                                                                          | Module                                                                                 |
|:---------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------|
| NoNetworkDialogFragment.kt | The code snippet defines a DialogFragment that shows an AlertDialog when there is no network connectivity. It inflates a layout file that contains a single button and sets a click listener on the button. The click listener triggers a callback function implemented in the parent activity through the DialogClickListener interface.                                                                        | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/NoNetworkDialogFragment.kt |
| HomeFragment.kt            | The provided code defines a fragment in an Android application that includes a button to choose a file and a listener to interact with other parts of the application. The primary functionality is to handle the user's selection of a file and store it in a local file object cache.                                                                                                                          | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/HomeFragment.kt            |
| ResultFragment.kt          | The provided code defines a ResultFragment class that extends the Fragment class and has a listener for fragment interactions. It also inflates a layout file and sets text values based on arguments passed into it. There are two TextViews and a Button that can be clicked to execute listener functions, and a companion object that creates a new instance of the ResultFragment with specified arguments. | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/ResultFragment.kt          |

</details>

<details closed><summary>Listeners</summary>

| File                             | Summary                                                                                                                                                                                                                                                                                  | Module                                                                                    |
|:---------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------|
| DialogClickListener.kt           | The code defines an interface called "DialogClickListener" that contains a method "onDialogPositiveClick" with two parameters: a Dialog and a Fragment. This interface is intended to be implemented by other classes that want to handle positive click events from a dialog box.       | app/src/main/java/com/thecoolguy/rumaan/fileio/listeners/DialogClickListener.kt           |
| OnFragmentInteractionListener.kt | This code snippet defines an interface named "OnFragmentInteractionListener" with two functions: "onUploadFileClick" and "onDone". This interface will be implemented by another class and will allow that class to respond to clicks on the "Upload File" button and the "Done" button. | app/src/main/java/com/thecoolguy/rumaan/fileio/listeners/OnFragmentInteractionListener.kt |

</details>

<details closed><summary>Repository</summary>

| File                    | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Module                                                                            |
|:------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
| UploadHistoryWorkers.kt | This code snippet contains two worker classes: ClearHistoryWorker and DeleteSingleItemWorker. The ClearHistoryWorker clears all items from the upload history database and returns a success result. The DeleteSingleItemWorker deletes a single item from the database based on an input ID and returns a success result.                                                                                                                                      | app/src/main/java/com/thecoolguy/rumaan/fileio/repository/UploadHistoryWorkers.kt |
| UploadWorker.kt         | The provided code snippet contains a Kotlin class UploadWorker, which extends the WorkManager's Worker class and includes methods for uploading files, saving results into the database, and posting notifications. It utilizes Fuel, a Kotlin HTTP client, and DatabaseHelper, a database helper class, to upload files and save results into the SQLite database. It also uses NotificationHelper to create notifications after the files have been uploaded. | app/src/main/java/com/thecoolguy/rumaan/fileio/repository/UploadWorker.kt         |

</details>

<details closed><summary>Root</summary>

| File            | Summary                                                                                                                                                                                                                     | Module          |
|:----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------|
| build.gradle    | This code snippet is a build script for a Gradle project. It includes dependencies for the Android build tools and libraries for Google services and Fabric. It also sets up repositories for Google, JCenter, and JitPack. | build.gradle    |
| settings.gradle | The provided code snippet includes the app module in the project. This module likely contains the main code and resources for the application.                                                                              | settings.gradle |

</details>

<details closed><summary>Ui</summary>

| File                        | Summary                                                                                                                                                                                                                                                                                                                                                                                                     | Module                                                                        |
|:----------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------|
| FileioApplication.kt        | The provided code is the base application class for a file I/O mobile app. It initializes the Timber logging library for logging purposes and sets up a custom error activity using the CustomActivityOnCrash library to handle app crashes.                                                                                                                                                                | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/FileioApplication.kt        |
| UploadHistoryListAdapter.kt | The provided code snippet contains an implementation of a RecyclerView Adapter used to display a list of upload history. It includes two ViewHolder classes for displaying dates and list items respectively, and supports different view types in order to display different layouts. It also provides functions for swapping and removing data in the list, as well as copying the file URL to clipboard. | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/UploadHistoryListAdapter.kt |
| SwipeToDeleteCallBack.kt    | The code defines a SwipeToDeleteCallBack class which is used to implement swipe-to-delete functionality in a RecyclerView. It draws a red background with a delete icon when a user swipes left and provides a callback when an item is swiped to be deleted. It also disables swiping for a specific view type.                                                                                            | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/SwipeToDeleteCallBack.kt    |
| NotificationHelper.kt       | HTTPStatusError: 429                                                                                                                                                                                                                                                                                                                                                                                        | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/NotificationHelper.kt       |

</details>

<details closed><summary>Utils</summary>

| File                        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                          | Module                                                                           |
|:----------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------|
| Extensions.kt               | This code provides two extension functions for Android: the first one shows a Toast message with a given text using the infix notation, and the second one sets the clickable property of a View to true or false. These functions can be used to simplify code and improve readability.                                                                                                                                         | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Extensions.kt               |
| WorkManagerHelper.kt        | The provided code snippet is a utility function that creates a one-time work request for uploading a file. It takes a URI string as input, constructs work data with it, sets constraints for network connectivity and adds a tag to the work request. This function is used to initiate the UploadWorker class.                                                                                                                 | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/WorkManagerHelper.kt        |
| Utils.kt                    | The code snippet provides a collection of helper methods packaged within the `Utils` object. It includes methods to retrieve file details, open file streams, check network connectivity, parse URLs and JSON, and perform date operations. The `Android` object provides additional methods specific to Android such as showing a dialog fragment and copying text to the clipboard.                                            | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Utils.kt                    |
| Helpers.kt                  | The provided code snippet contains three functions that deal with file handling in an Android app. The first function retrieves metadata of a file by querying its Uri. The second function returns a File object with useful information about the file. The third function composes a FileEntity object by combining a File object and a Response object.                                                                      | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Helpers.kt                  |
| FragmentHelperExtensions.kt | The code provides extension functions for the FragmentManager class in the androidx.fragment.app library. These functions are used to add or replace a fragment in a container with a specified ID, along with a tag. They also add the fragment transaction to the back stack and define animations for the fragment transitions.                                                                                               | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/FragmentHelperExtensions.kt |
| MaterialIn.kt               | The provided code snippet is a Kotlin object `MaterialIn` that contains functions for animating views using the Material Design "In" animation. The `animate` function takes a view and delay/slide directions as input, and initializes a call to the `initAnimation` function, which recursively adds animation to all child views. The `startAnimators` function is responsible for starting the animation on the given view. | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/MaterialIn.kt               |
| Constants.kt                | The code snippet provides global constants for the fileio utility package, including the base URL, expiration parameter, default expiration time, and social media URLs. It also includes a timestamp format and a constant for appending to the end of a link.                                                                                                                                                                  | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Constants.kt                |

</details>

<details closed><summary>Viewmodel</summary>

| File                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                              | Module                                                                             |
|:--------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
| UploadHistoryViewModel.kt | The provided code snippet is a Kotlin class that represents the ViewModel for managing the display of file upload history in an Android app. It inherits from the AndroidViewModel class and uses LiveData and MutableLiveData interfaces to store and observe data changes. It communicates with an UploadHistoryRoomDatabase object to provide access to a list of FileEntity objects representing uploaded files. | app/src/main/java/com/thecoolguy/rumaan/fileio/viewmodel/UploadHistoryViewModel.kt |

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
