
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
file.io-Android-Client
</h1>
<h3>◦ File.io on the go!</h3>
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

## 📒 Table of Contents
- [📒 Table of Contents](#-table-of-contents)
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

The file.io Android Client project is an Android application that allows users to upload files and generate temporary URLs for sharing. The core functionalities include file selection, uploading, storing upload history, and generating URLs with varying expiration dates. The value proposition of the project lies in its simplicity and convenience, providing an easy-to-use interface for file upload and sharing, along with features like history tracking and link expiration to enhance user control and privacy.

---

## ⚙️ Features

| Feature                | Description                                                                                                                                               |
| -----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| **⚙️ Architecture**    | The codebase follows the Model-View-ViewModel (MVVM) architecture, separating concerns and providing a clean and scalable structure.                         |
| **📖 Documentation**   | The repository has good documentation, including detailed summaries for each file, explaining their purpose and functionality.                              |
| **🔗 Dependencies**    | The project relies on various external libraries such as AppCompat, Room, Fuel, Gson, Timber, and WorkManager, enhancing functionality and performance. |
| **🧩 Modularity**      | The codebase is modular and organized into separate packages, each responsible for specific functionalities.                                           |
| **✔️ Testing**         | The codebase includes both unit tests and instrumented tests, covering key functionalities and ensuring code robustness.                                |
| **⚡️ Performance**     | The system demonstrates good performance, leveraging the Fuel library for efficient network operations and WorkManager for background task management. |
| **🔐 Security**        | The system takes steps to protect data by implementing encryption for URLs and adhering to best security practices in network operations.               |
| **🔀 Version Control** | The project uses Git for version control, providing a history of file changes, allowing for collaboration and easy rollbacks.                            |
| **🔌 Integrations**    | The system integrates with external services such as Firebase Crashlytics and Google Services, enhancing the functionalities and error tracking.     |
| **📶 Scalability**     | The system is designed with modularity in mind, allowing for easy addition of new features and scalability to handle increased user demand.              |

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

<details closed><summary>Root</summary>

| File                                                                                          | Summary                                                                                                                                                                                                                                                        |
| ---                                                                                           | ---                                                                                                                                                                                                                                                            |
| [build.gradle](https://github.com/rumaan/file.io-Android-Client/blob/main/build.gradle)       | This code snippet configures the build dependencies for an Android project. It includes dependencies for the Android Gradle plugin, Fabric, Google Services, and Kotlin. It also sets up the repositories to resolve these dependencies.                       |
| [settings.gradle](https://github.com/rumaan/file.io-Android-Client/blob/main/settings.gradle) | The provided code snippet includes the':app' module, which typically represents the main application module in an Android project. It encapsulates the core functionalities of the application, including user interface, data handling, and various features. |

</details>

<details closed><summary>App</summary>

| File                                                                                        | Summary                                                                                                                                                                                                                                                                                                                                                                                               |
| ---                                                                                         | ---                                                                                                                                                                                                                                                                                                                                                                                                   |
| [build.gradle](https://github.com/rumaan/file.io-Android-Client/blob/main/app/build.gradle) | The provided code snippet is a configuration file for an Android application. It includes plugins for Android development, Kotlin language support, and Fabric Crashlytics reporting. It sets up various dependencies for library and test handling, such as AppCompat, ConstraintLayout, Material Design, Room, Fuel, Gson, and Timber. It also integrates Firebase Crashlytics and Google Services. |

</details>

<details closed><summary>Fileio</summary>

| File                                                                                                                                                                                      | Summary                                                                                                                                                                                                                                                          |
| ---                                                                                                                                                                                       | ---                                                                                                                                                                                                                                                              |
| [ExampleInstrumentedTest.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/androidTest/java/com/thecoolguy/rumaan/fileio/ExampleInstrumentedTest.kt)                 | This code snippet is a test class for an Android application. It uses instrumentation testing to verify that the app's context matches the expected package name. The test is run on an Android device using the AndroidJUnit4 test runner.                      |
| [FileEntityDaoTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/androidTest/java/com/thecoolguy/rumaan/fileio/FileEntityDaoTest.java)                         | The provided code snippet is a JUnit test class for testing the functionalities of a Room Database. It includes tests to verify the insertion of items into the database, the counting of rows in the database, and retrieving multiple items from the database. |
| [UploadHistoryInstrumentedTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/androidTest/java/com/thecoolguy/rumaan/fileio/UploadHistoryInstrumentedTest.java) | This code snippet is an instrumented test for the UploadHistoryActivity class. It sets up a Room database, adds five items to the database, and has a test method to check the functionality of long-pressing and deleting an item in the activity.              |
| [ExampleUnitTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/test/java/com/thecoolguy/rumaan/fileio/ExampleUnitTest.java)                                    | The provided code snippet contains a unit test class called "ExampleUnitTest". It includes a single test method called "addition_isCorrect" that asserts whether the sum of 2 and 2 is equal to 4. The goal is to ensure that the addition operation is correct. |
| [UploadRepositoryTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/test/java/com/thecoolguy/rumaan/fileio/UploadRepositoryTest.java)                          | The provided code snippet is a unit test for the check_ExpireUrl function in the UploadRepository class. It tests whether the generated expire URL matches the expected URL with the provided days value and the URL with predefined constants.                  |
| [UrlTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/test/java/com/thecoolguy/rumaan/fileio/UrlTest.java)                                                    | The code snippet tests the functionality of a URL parser that is part of a file input/output package. It verifies if a given encrypted URL can be parsed correctly to obtain the base URL.                                                                       |
| [FileEntityTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/test/java/com/thecoolguy/rumaan/fileio/FileEntityTest.java)                                      | This code snippet is a unit test for the FileEntity class. It checks if the fileEntity object can correctly set and retrieve a name and URL property.                                                                                                            |

</details>

<details closed><summary>Viewmodel</summary>

| File                                                                                                                                                                       | Summary                                                                                                                                                                                                                                                                                                                  |
| ---                                                                                                                                                                        | ---                                                                                                                                                                                                                                                                                                                      |
| [UploadHistoryViewModel.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/viewmodel/UploadHistoryViewModel.kt) | This code snippet defines a ViewModel class named UploadHistoryViewModel that extends AndroidViewModel. It provides a LiveData object called uploadList, which contains a list of FileEntity objects retrieved from a Room database. The uploads are fetched and stored in uploadList when the ViewModel is initialized. |

</details>

<details closed><summary>Ui</summary>

| File                                                                                                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                               |
| ---                                                                                                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                                   |
| [FileioApplication.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/FileioApplication.kt)               | The provided code snippet is responsible for configuring the application and setting up necessary components such as Timber for logging and a custom activity for handling crashes. It extends the Application class and sets up Timber to log debug messages. It also sets up a custom error activity to handle crashes.                                             |
| [UploadHistoryListAdapter.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/UploadHistoryListAdapter.kt) | This code snippet defines a custom RecyclerView adapter called UploadHistoryListAdapter. It is used for displaying a list of uploaded files with their corresponding dates.The adapter handles different view types for displaying the dates and file items. It also provides methods for updating and manipulating the list of files.                                |
| [SwipeToDeleteCallBack.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/SwipeToDeleteCallBack.kt)       | The code snippet provides a SwipeToDeleteCallBack class that enables swipe-to-delete functionality in a RecyclerView. It draws a red background and a delete icon when the item is swiped, allowing the user to delete the item by swiping. The class also handles disabling swipes for specific view types.                                                          |
| [NotificationHelper.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/NotificationHelper.kt)             | This code snippet defines a NotificationHelper class that is responsible for creating and showing a notification for a successful file upload. It sets the notification's content and appearance, sets an intent for when the notification is clicked, creates a notification channel for devices running Android O and above, and finally displays the notification. |

</details>

<details closed><summary>Fragments</summary>

| File                                                                                                                                                                            | Summary                                                                                                                                                                                                                                                                                                   |
| ---                                                                                                                                                                             | ---                                                                                                                                                                                                                                                                                                       |
| [NoNetworkDialogFragment.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/NoNetworkDialogFragment.kt) | This code snippet defines a DialogFragment class called NoNetworkDialogFragment. It creates a dialog with a layout, listens for button clicks, and provides a callback to the parent activity using a DialogClickListener.                                                                                |
| [HomeFragment.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/HomeFragment.kt)                       | This code snippet represents a fragment in an Android app. It provides a button that triggers a callback to upload a chosen file. The fragment communicates with the activity using a listener interface. It also handles the creation and setup of the fragment's view.                                  |
| [ResultFragment.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/ResultFragment.kt)                   | The given code snippet is for a ResultFragment class in an Android application. It displays a URL and the number of days until it expires. It also provides a button to notify the listener that the task is done. Additionally, it allows the user to copy the URL to their clipboard by clicking on it. |

</details>

<details closed><summary>Activities</summary>

| File                                                                                                                                                                         | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---                                                                                                                                                                          | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [MainActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/MainActivity.kt)                   | The provided code snippet is for the MainActivity class in an Android application. It handles the main functionality of the app, including setting up the toolbar, handling menu options, fragment initialization, file selection, and uploading files using WorkManager.                                                                                                                                                                                                  |
| [ErrorActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/ErrorActivity.kt)                 | This code snippet defines an ErrorActivity class, which is an activity that is displayed in case of runtime crashes. It sets the layout for the activity and handles the back button event by finishing all activities in the app.                                                                                                                                                                                                                                         |
| [UploadHistoryActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/UploadHistoryActivity.kt) | This code snippet represents an activity in an Android app called UploadHistoryActivity. It includes functionalities such as creating options menu, handling menu clicks, clearing history, removing history items, animating and displaying a list of upload history items. It also supports swipe-to-delete functionality for the list items.                                                                                                                            |
| [AboutActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/AboutActivity.kt)                 | This code snippet represents an AboutActivity class in an Android app. It extends AppCompatActivity and includes functionalities such as creating a menu, setting a theme, displaying a toolbar, and handling menu item selection to start a new activity. The menu item "menu_open_source" opens the LicenseActivity.                                                                                                                                                     |
| [LicenseActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/LicenseActivity.kt)             | The provided code snippet is for a LicenseActivity class that extends MaterialAboutActivity. It overrides two methods to set the activity title and create a MaterialAboutList. The MaterialAboutList contains a list of license cards for different open-source libraries, each card displaying the library name, year, author, and license type. The list is returned by the getMaterialAboutList() method and used to populate the license information in the activity. |

</details>

<details closed><summary>Repository</summary>

| File                                                                                                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                  |
| ---                                                                                                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                      |
| [UploadHistoryWorkers.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/repository/UploadHistoryWorkers.kt) | The code snippet defines two Workers: ClearHistoryWorker and DeleteSingleItemWorker. ClearHistoryWorker clears all upload history in the database. DeleteSingleItemWorker deletes a specific item from the database based on its ID.                                                                                                                     |
| [UploadWorker.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/repository/UploadWorker.kt)                 | The provided code snippet is an implementation of a Worker class in an Android application. It handles file uploads using the Fuel HTTP library. The code retrieves a file from a Uri, uploads it to the specified endpoint, handles the upload progress, and saves the response data to a local database. It also sends a notification upon completion. |

</details>

<details closed><summary>Utils</summary>

| File                                                                                                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                                                                      |
| ---                                                                                                                                                                        | ---                                                                                                                                                                                                                                                                                                                                                                                          |
| [Extensions.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Extensions.kt)                             | This code snippet provides two extension functions: "toast" and "toggleClickable". The "toast" function displays a short toast message on the screen using the provided context. The "toggleClickable" function allows to enable or disable the clickability of a given view by setting its "isClickable" property.                                                                          |
| [WorkManagerHelper.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/WorkManagerHelper.kt)               | The code snippet provides a function, createUploadWork, that creates and configures a one-time work request for uploading a file. It sets the required network type as connected and passes the file URI as input data to the UploadWorker class. The work request is also tagged for easier identification.                                                                                 |
| [Utils.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Utils.kt)                                       | The provided code snippet is a collection of utility methods. It includes functions for retrieving file details, opening file streams, checking network connectivity, displaying dialogs, copying text to clipboard, parsing URLs, parsing JSON, and handling dates.                                                                                                                         |
| [Helpers.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Helpers.kt)                                   | This code snippet includes functions to retrieve and process file metadata, retrieve the file, and compose the file's information into a FileEntity object.                                                                                                                                                                                                                                  |
| [FragmentHelperExtensions.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/FragmentHelperExtensions.kt) | This code snippet provides extension functions for adding and replacing fragments in the Android FragmentManager. The addFragment function adds a fragment to a specified container with an optional tag, while the replaceFragment function replaces an existing fragment in the container with a new fragment. Both functions handle backstack management and define fragment transitions. |
| [MaterialIn.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/MaterialIn.kt)                             | The provided code snippet is a utility class for animating views in an Android app using material design transitions, specifically for the "material in" effect. It animates the views with fade and slide animations based on the specified delay and slide directions.                                                                                                                     |
| [Constants.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Constants.kt)                               | This code snippet defines global constants for a fileio utility package. It includes base URLs, expiration parameters, default values, and timestamp formats. It also provides URLs for the developer's GitHub and Twitter profiles, as well as an email address.                                                                                                                            |

</details>

<details closed><summary>Listeners</summary>

| File                                                                                                                                                                                     | Summary                                                                                                                                                                                                                                                                                                    |
| ---                                                                                                                                                                                      | ---                                                                                                                                                                                                                                                                                                        |
| [DialogClickListener.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/listeners/DialogClickListener.kt)                     | This code snippet defines an interface called `DialogClickListener` that has one method `onDialogPositiveClick`. This method takes in a `Dialog` object and a `Fragment` object as parameters. It is intended to be used as a listener for positive button click events in dialogs.                        |
| [OnFragmentInteractionListener.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/listeners/OnFragmentInteractionListener.kt) | The provided code snippet defines an interface "OnFragmentInteractionListener" that contains two functions: "onUploadFileClick()" and "onDone()". This interface serves as a listener for fragment interactions, allowing for the handling of events related to uploading files and completion of actions. |

</details>

---

## 🚀 Getting Started

### ✔️ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - `ℹ️ Requirement 1`
> - `ℹ️ Requirement 2`
> - `ℹ️ ...`

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

### 🎮 Using file.io-Android-Client

```sh
java -jar build/libs/myapp.jar
```

### 🧪 Running Tests
```sh
gradle test
```

---


## 🗺 Roadmap

> - [X] `ℹ️  Task 1: Implement X`
> - [ ] `ℹ️  Task 2: Refactor Y`
> - [ ] `ℹ️ ...`


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

This project is licensed under the `ℹ️  INSERT-LICENSE-TYPE` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 👏 Acknowledgments

> - `ℹ️  List any resources, contributors, inspiration, etc.`

---
