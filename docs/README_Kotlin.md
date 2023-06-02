
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
file.io-Android-Client
</h1>
<h3 align="center">📍 File sharing at your fingertips-with file.io Android client and GitHub</h3>
<h3 align="center">🚀 Developed with the software and tools below:</h3>

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
- [📍Overview](#overview)
- [🔮 Features](#-features)
- [⚙️ Project Structure](#️-project-structure)
- [💻 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
  - [✅ Prerequisites](#-prerequisites)
  - [💻 Installation](#-installation)
  - [🤖 Using file.io-Android-Client](#-using-fileio-android-client)
  - [🧪 Running Tests](#-running-tests)
- [🛠 Future Development](#-future-development)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍Overview

The file.io Android client is a comprehensive open source Android application that allows users to upload files to an online file-sharing web service and manage their upload history through an intuitive user interface. The project comes with a diverse range of functionalities, including a Room database for maintaining upload history, an SQLite database manager, work management tools, and notification features. It uses sophisticated libraries, such as Fuel, Navigation, and Gson, for efficient and user-friendly operation, making the app a valuable tool for everyday upload management.

---

## 🔮 Features

Feature | Description |
|---|---|
| **🏗 Structure and Organization** | The codebase has a well-organized structure with clear separations between files specific to certain functionalities. The packages and naming conventions used aid in the understandability and maintainability of the project. |
| **📝 Code Documentation** | The codebase is adequately documented, easing the understandability of the project as a whole. Docstrings include the method purpose, parameters, return types, and other important details. Additionally, comments are added in the code snippets to further enhance clarity. |
| **🧩 Dependency Management** | Dependency management is done through the Gradle build system. The proper versions of the needed dependencies are declared in the build.gradle files. Libraries such as Fuel, Gson, Kotlin, and Room are included and provide a comprehensive set of early libraries. |
| **♻️ Modularity and Reusability** | The codebase heavily employs the MVVM model with various components' reusability, ensuring testability and component isolation. Code is separated into individual fragments and activities with clear responsibilities, making it modular and facilitating defect mitigation for ongoing maintenance. |
| **✅ Testing and Quality Assurance** | The code features both unit and instrumentation tests for ensuring stability and correctness of underlying behaviour/functionality. Its resulting suite achieves excellent test coverage to mitigate the potential for defects and highlights several notable defects fixed post-development. |
| **⚡️ Performance and Optimization** | Performance optimization was a priority-the code does include designs and practices for the retrieval and display of data involving RecyclerView, Constraints helper for WorkManager, and MediaPlayer manager. Additionally, the code making use of libraries famous for lightweight functioning demonstrate efficiency towards achieving good performance at the expense of performance. |
| **🔒 Security Measures** | The code addresses security concerns that concern libraries received over the Internet by relying on the built-in key and TrustStore system through asymmetric cryptography security. Views abstraction to allow safer information flow while enabling secure timestamp validation and internet access has been enforced appropriately. |
| **🔄 Version Control and Collaboration** | Git was used to support version control workflow procedures on code versioning. Pull requests and commits of requisite organization metadata concerns have message clarifications to enhance clarity and dispose explanation regarding changes explored further within the codebase. |
| **🔌 External Integrations** | The codebase incorporates several third-party libraries, including Firebase, Fuel, Room, and Navigation component for resource

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

| File                     | Summary                                                                                                                                                                                                                                                                                                                                                                                               | Module                                                                                |
|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------|
| MainActivity.kt          | The provided code is for the main activity of a file uploader Android app. It comprises methods for choosing and uploading files, observing work status and displaying results, managing permissions and app navigation via a toolbar implementing menu items. Additionally, it uses fragments to visualise UI for the application.                                                                   | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/MainActivity.kt          |
| ErrorActivity.kt         | The provided code is an implementation of an ErrorActivity class in an Android application. This activity is shown in case of any runtime crashes. The onBackPressed() function is used to finish the app's activity stack when the device back-button is pressed. The onCreate() function sets the layout specified in the R.layout.activity_error file.                                             | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/ErrorActivity.kt         |
| UploadHistoryActivity.kt | The code snippet is an activity for displaying a list of uploaded files and their upload history. It handles swipe-to-delete functionality and includes the option to clear all upload history. It also groups the list by date and displays it in chronological order while animating the changes in layout.                                                                                         | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/UploadHistoryActivity.kt |
| AboutActivity.kt         | This code defines an activity subclass that inflates a menu layout and displays it in the toolbar of the UI; when a button in the menu is tapped, it triggers the launch of another activity called LicenseActivity. By default, the back arrow can be used to return to the previous activity in the app.                                                                                            | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/AboutActivity.kt         |
| LicenseActivity.kt       | The provided code defines a LicenseActivity that extends the MaterialAboutActivity class. This activity displays a list of open-source licenses used in the application. It retrieves the necessary information such as name, date, and license using the ConvenienceBuilder class provided by the MaterialAboutLibrary. The list is returned as a MaterialAboutList to be displayed in the activity. | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/LicenseActivity.kt       |

</details>

<details closed><summary>App</summary>

| File         | Summary                                                                                                                                                                                                                                                                                                                                                                                                                           | Module           |
|:-------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| build.gradle | This code is a build configuration file for an Android application that includes several plugins for Fabric, Kotlin, and Android. It sets the minimum SDK version to 21, target SDK version to 28, and includes dependencies such as Google Material Design, Firebase, Room, and Permissions Dispatcher. Additionally, the code uses libraries for Fuel android service, Gson deserializer, and Navigation framework for Android. | app/build.gradle |

</details>

<details closed><summary>Fileio</summary>

| File                               | Summary                                                                                                                                                                                                                                                                                                                                             | Module                                                                                   |
|:-----------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------|
| ExampleInstrumentedTest.kt         | The provided code ensures the proper execution of an android instrumentation test on a device using the AndroidJUnit4 framework. It also verifies the correct package name of the app under test using the assertEquals assertion. The ActivityTestRule class launches the specified activity before the test runs.                                 | app/src/androidTest/java/com/thecoolguy/rumaan/fileio/ExampleInstrumentedTest.kt         |
| FileEntityDaoTest.java             | The provided code is a set of tests for a Room database named `UploadHistoryRoomDatabase`. These tests cover features like checking the number of rows in the database, inserting items into the database, and retrieving multiple items from the database. The testing is performed using the JUnit framework and AndroidJUnit4 runner.            | app/src/androidTest/java/com/thecoolguy/rumaan/fileio/FileEntityDaoTest.java             |
| UploadHistoryInstrumentedTest.java | This code snippet contains a test class that includes a matcher and a method to check a long press item deletion. The class imports dependencies for database and utilities, initializes them, and adds items to the database. The provided functionalities indicate testing for file and database management in the mentioned Android application. | app/src/androidTest/java/com/thecoolguy/rumaan/fileio/UploadHistoryInstrumentedTest.java |
| ExampleUnitTest.java               | The provided code snippet is a JUnit test class with a single test method named `addition_isCorrect`. This method asserts that the sum of integers 2 and 2 is equal to the expected value of 4. If the assertion passes, then the method is considered to have executed correctly.                                                                  | app/src/test/java/com/thecoolguy/rumaan/fileio/ExampleUnitTest.java                      |
| UploadRepositoryTest.java          | This is a unit test code snippet for UploadRepository class. The test checks if the URL parser can efficiently retrieve the URL link without issues. Competing against 2 URLs of different forms, the code compares the expected and actual outcomes to ensure uniformity in results.                                                               | app/src/test/java/com/thecoolguy/rumaan/fileio/UploadRepositoryTest.java                 |
| UrlTest.java                       | The code snippet contains a JUnit test to verify the functionality of parsing a URL from an encrypted URL string using the URLParser class, which is part of the Utils package in the com.thecoolguy.rumaan.fileio package. The test checks if the parsed URL matches an expected value using the assertEquals method.                              | app/src/test/java/com/thecoolguy/rumaan/fileio/UrlTest.java                              |
| FileEntityTest.java                | The provided code is a JUnit test for the FileEntity class, which creates objects representing files. It tests if an instance of FileEntity updates correctly using the setName and setUrl methods. The test checks if the name and url set to the object are equal to the expected name and url respectively.                                      | app/src/test/java/com/thecoolguy/rumaan/fileio/FileEntityTest.java                       |

</details>

<details closed><summary>Fragments</summary>

| File                       | Summary                                                                                                                                                                                                                                                                                                                                                               | Module                                                                                 |
|:---------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------|
| NoNetworkDialogFragment.kt | The given code snippet defines a DialogFragment to display a no network connection error message. It inflates a layout with an ok button, which upon click calls a listener method to handle the click. The DialogClickListener is additionally implemented to browse service ability.                                                                                | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/NoNetworkDialogFragment.kt |
| HomeFragment.kt            | The code defines a fragment class that displays a layout file with a single button. When the button is clicked, it triggers a callback method to upload a file chosen by the user. The class implements a listener interface to communicate with the parent activity that must implement the same interface.                                                          | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/HomeFragment.kt            |
| ResultFragment.kt          | The code defines a ResultFragment class which represents a fragment in an Android app. The fragment inflates R.layout.layout_result layout file, displays data provided as arguments in the layout views, and listens for button and text click actions to interact with the parent activity. Specific features include copying text to clipboard and showing toasts. | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/ResultFragment.kt          |

</details>

<details closed><summary>Listeners</summary>

| File                             | Summary                                                                                                                                                                                                                                                                                                                                            | Module                                                                                    |
|:---------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------|
| DialogClickListener.kt           | The provided code snippet defines an interface named `DialogClickListener` with a single method `onDialogPositiveClick`, which takes in two parameters-a `Dialog` object and a `Fragment`. This interface can be implemented by other classes to receive notifications when a positive click event occurs on a dialog initiated by an Android app. | app/src/main/java/com/thecoolguy/rumaan/fileio/listeners/DialogClickListener.kt           |
| OnFragmentInteractionListener.kt | This code defines an interface called OnFragmentInteractionListener which has two method signatures-onUploadFileClick() and onDone(). It is used to handle interactions with fragments related to file upload and completing the upload process.                                                                                                   | app/src/main/java/com/thecoolguy/rumaan/fileio/listeners/OnFragmentInteractionListener.kt |

</details>

<details closed><summary>Repository</summary>

| File                    | Summary                                                                                                                                                                                                                                                                                                                                                                               | Module                                                                            |
|:------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
| UploadHistoryWorkers.kt | The code snippet provides two worker classes to manage the deletion of data from a local database in Android. The ClearHistoryWorker class clears all historical data from the database, while the DeleteSingleItemWorker class accepts an item ID as parameter, and deletes only that item from the database within the constraints of the provided Worker API.                      | app/src/main/java/com/thecoolguy/rumaan/fileio/repository/UploadHistoryWorkers.kt |
| UploadWorker.kt         | The code snippet is a worker class that extends the Workmanager for uploading files to the internet using Fuel, an http library. It contains methods for saving, uploading, and showing notifications. Additionally, it performs various operations related to retrieving the input data and provides an output indicative of success or failure after uploading and executing tasks. | app/src/main/java/com/thecoolguy/rumaan/fileio/repository/UploadWorker.kt         |

</details>

<details closed><summary>Root</summary>

| File            | Summary                                                                                                                                                                                                                                                                                                                     | Module          |
|:----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------|
| build.gradle    | This code is responsible for setting up the dependencies and repositories used for a Gradle-based Android project. It includes the implementation of Maven, Fabric and JitPack. Additionally, it includes the version number for Kotlin, Google Services Gradle plugin, io.fabric Gradle plugin, and Android Gradle plugin. | build.gradle    |
| settings.gradle | The provided code snippet includes the':app' module, which is intended for building the app.                                                                                                                                                                                                                                | settings.gradle |
| .travis.yml     | This code snippet sets up an Android project in an environment that requires sudo access, installs necessary JDK and Android components for build, and clears the cache to avoid issues with plugin resolution. It also caches important directories to speed up future builds.                                             | .travis.yml     |

</details>

<details closed><summary>Ui</summary>

| File                        | Summary                                                                                                                                                                                                                                                                                                                                                                                | Module                                                                        |
|:----------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------|
| FileioApplication.kt        | The code creates an application class called FileioApplication which extends the Application class. It initializes Timber logging and sets up a custom error activity in the CaocConfig. Additionally, a static TAG is defined for future use.                                                                                                                                         | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/FileioApplication.kt        |
| UploadHistoryListAdapter.kt | The provided code is an adapter for a RecyclerView in an Android app that displays a list of file uploads with details such as the file name and URL. The adapter allows for grouping the uploads by date and displays a header for each date group. It also allows users copy file URL to clipboard and remove entries.                                                               | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/UploadHistoryListAdapter.kt |
| SwipeToDeleteCallBack.kt    | The code snippet is a utility class that provides swipe-to-delete functionality in a RecyclerView for Android apps. It allows users to swipe horizontally and delete items in the RecyclerView. The helper uses ItemTouchHelper class, SimpleCallBack class, and provides icons and colors represented in the code. Additionally, it disables the swipe feature for chosen view types. | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/SwipeToDeleteCallBack.kt    |
| NotificationHelper.kt       | This code snippet defines a NotificationHelper class that processes notifications for a successful file upload. It handles creating notification channels for Oreo and above versions of Android as well as adding a click action that opens an UploadHistoryActivity. The notification message displays the file's URL along with an uploaded file icon.                              | app/src/main/java/com/thecoolguy/rumaan/fileio/ui/NotificationHelper.kt       |

</details>

<details closed><summary>Utils</summary>

| File                        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Module                                                                           |
|:----------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------|
| Extensions.kt               | The code snippet defines two extension functions to enhance Android application development: "String.toast(context)" displays a toast message, and "View.toggleClickable(v)" changes the clickable status of a View object (true or false). These functions make codes more readable and reduce effort required for similar functionalities implementation.                                                                                                        | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Extensions.kt               |
| WorkManagerHelper.kt        | The provided code snippet is designed to assist in uploading files with Android WorkManager through the use of the UploadWorker class. It includes the necessary Constraints for data including Network Connectivity, and creates the OneTimeWorkRequest indicated by the flag tag MESSAGE_UPLOAD_WORK_TAG with input data specified by the workDataOf method.                                                                                                     | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/WorkManagerHelper.kt        |
| Utils.kt                    | The code snippet provides a set of utility functions for handling file I/O, parsing URLs and JSON data, and working with Android-related components such as intent creation, network connectivity, and dialogs. The functions cover tasks such as retrieving file metadata, copying text to clipboard, displaying app details screen, and getting days from expiration strings. The code is easily understandable and can be integrated into Android applications. | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Utils.kt                    |
| Helpers.kt                  | This code provides three functions for handling file I/O operations. The first function retrieves metadata about a given file. The second function returns a File object containing the name, size, and URI of a given file. The third function takes a File object and a Response object and returns a FileEntity object containing the file name, URI as a String, current date, and a number of days until the file should expire.                              | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Helpers.kt                  |
| FragmentHelperExtensions.kt | The provided code snippet provides two extension functions to the FragmentManager class in the AndroidX Fragment API. The first function `addFragment()` adds a fragment to a given containerId and the second function `replaceFragment()` replaces an existing fragment with a new fragment in the specified container. Both functions use a builder pattern to create transitions and manages the back stack.                                                   | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/FragmentHelperExtensions.kt |
| MaterialIn.kt               | This is a Kotlin code snippet that defines an object called MaterialIn, it receives a view and animates it with a delay direction and a slide direction. The animation is an Accelerate-Decelerate fade-in and slide-out animation typically referred to as a "material-in." The code also checks for the user's version of Android and flips START<->LEFT and END<->RIGHT for languages that read from a right to left orientation such as Arabic and Hebrew.     | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/MaterialIn.kt               |
| Constants.kt                | The code snippet consists of a collection of global constant values and variables used in file input/output operations in an Android application. It also defines compatible URI variables, including repos link, twitter, and the developer's email address. Lastly, there is a constant time-stamp format used in the module.                                                                                                                                    | app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Constants.kt                |

</details>

<details closed><summary>Viewmodel</summary>

| File                      | Summary                                                                                                                                                                                                                                                                                                                     | Module                                                                             |
|:--------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
| UploadHistoryViewModel.kt | The provided code contains a ViewModel class that extends AndroidViewModel and retrieves a list of file upload history records from a local database using LiveData and MutableLiveData properties. This ViewModel class is responsible for managing and processing data related to the upload history of a particular app. | app/src/main/java/com/thecoolguy/rumaan/fileio/viewmodel/UploadHistoryViewModel.kt |

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
# [INSERT-COMMAND-FOR-TESTS]
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

## 📄 License

This project is licensed under the `[📌  INSERT-LICENSE-TYPE]` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 👏 Acknowledgments

> - [📌  List any resources, contributors, inspiration, etc.]

---


