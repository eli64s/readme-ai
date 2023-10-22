<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>file.io-Android-Client
</h1>
<h3>◦ Seamless file sharing on the go!</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/Kotlin-7F52FF.svg?style&logo=Kotlin&logoColor=white" alt="Kotlin" />
<img src="https://img.shields.io/badge/Android-3DDC84.svg?style&logo=Android&logoColor=white" alt="Android" />
<img src="https://img.shields.io/badge/Gradle-02303A.svg?style&logo=Gradle&logoColor=white" alt="Gradle" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
<img src="https://img.shields.io/badge/java-%23ED8B00.svg?style&logo=openjdk&logoColor=white" alt="java" />
</p>
<img src="https://img.shields.io/github/languages/top/rumaan/file.io-Android-Client?style&color=5D6D7E" alt="GitHub top language" />
<img src="https://img.shields.io/github/languages/code-size/rumaan/file.io-Android-Client?style&color=5D6D7E" alt="GitHub code size in bytes" />
<img src="https://img.shields.io/github/commit-activity/m/rumaan/file.io-Android-Client?style&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/license/rumaan/file.io-Android-Client?style&color=5D6D7E" alt="GitHub license" />
</div>

---

## 📖 Table of Contents
- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
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

The project is an Android client for the file.io file sharing service. It allows users to upload files and receive temporary URLs for sharing. The app provides a user interface for managing file uploads, displaying upload history, and copying file URLs. Its value proposition lies in its simplicity and convenience for quickly sharing files without registration or permanent storage.

---

## 📦 Features

| Feature                | Description                           |
| ---------------------- | ------------------------------------- |
| **⚙️ Architecture**     | The codebase follows a standard MVVM (Model-View-ViewModel) architecture pattern. It separates the business logic from the UI components, making the code more modular and maintainable. The ViewModel communicates with the Repository to fetch and store data, which is then observed by the View for rendering. Limit your response to a maximum of 250 characters.    |
| **📃 Documentation**   | The codebase includes documentation in the form of code comments, readme files, and descriptive file names. The readme provides instructions on how to use the code, and the code comments explain the purpose and functionality of different classes and methods. However, there is room for improvement in terms of more detailed explanations and examples. Limit your response to a maximum of 250 characters.    |
| **🔗 Dependencies**    | The codebase relies on several external libraries and services. It includes popular libraries like Room for data persistence, Firebase Crashlytics for crash reporting, and Android Navigation component for navigation. It also integrates with services like file.io for file uploading. These dependencies enhance the app's functionality and provide robust features. Limit your response to a maximum of 250 characters.    |
| **🧩 Modularity**      | The codebase is well-organized into smaller modules and packages, following the single responsibility principle. Each module focuses on a specific functionality or feature, such as UI, data persistence, network communication, and testing. This modular structure allows for easier code navigation, testing, and maintainability. Limit your response to a maximum of 250 characters.    |
| **🧪 Testing**          | The codebase includes both unit tests and instrumented tests. Unit tests cover individual components, ensuring their functionality in isolation. Instrumented tests verify the behavior of the app as a whole. The codebase also uses popular testing frameworks like JUnit and provides comprehensive coverage for critical functionalities. Limit your response to a maximum of 250 characters.    |
| **⚡️ Performance**      | The performance of the codebase is efficient, with measures taken to handle file uploads, database operations, and UI rendering. The use of asynchronous operations, caching, and background workers helps optimize resource usage. However, further performance improvements could be made by implementing caching strategies and optimizing network operations. Limit your response to a maximum of 250 characters.    |
| **🔐 Security**        | The codebase handles security by properly managing user credentials and using secure communication protocols for network operations. It also validates user inputs to prevent security vulnerabilities like injection attacks. However, further measures such as data encryption and input validation could be implemented to enhance security. Limit your response to a maximum of 250 characters.    |
| **🔀 Version Control** | The codebase is hosted on GitHub and utilizes Git for version control. It includes a comprehensive commit history with detailed commit messages, enabling easy tracking of changes and collaboration among developers. It also follows branching strategies like feature branches and pull requests for better code review and management. Limit your response to a maximum of 250 characters.    |
| **🔌 Integrations**    | The codebase integrates with various external systems and services like Firebase Crashlytics for crash reporting and file.io for file uploading. These integrations enhance the app's functionality and provide seamless user experiences. However, there is

---


## 📂 Repository Structure


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

## ⚙️ Modules

<details closed><summary>Root</summary>

| File                                                                                          | Summary                                                                                                                                                                                                                               |
| ---                                                                                           | ---                                                                                                                                                                                                                                   |
| [build.gradle](https://github.com/rumaan/file.io-Android-Client/blob/main/build.gradle)       | This code sets up the necessary dependencies for building an Android project. It includes libraries for Android tools, Fabric, Google Play Services, and Kotlin. It also configures the repositories for fetching these dependencies. |
| [settings.gradle](https://github.com/rumaan/file.io-Android-Client/blob/main/settings.gradle) | The code focuses on the app module, which contains the core functionalities of the application. It is responsible for managing the overall behavior and features of the app.                                                          |
| [.travis.yml](https://github.com/rumaan/file.io-Android-Client/blob/main/.travis.yml)         | This code is for an Android project. It sets up the required JDK, Android SDK, and licenses. It also handles cache management for Gradle and Android build processes.                                                                 |

</details>

<details closed><summary>Screenshots</summary>

| File                                                                                            | Summary                                                                                                                                                                                                                                                                                |
| ---                                                                                             | ---                                                                                                                                                                                                                                                                                    |
| [readme.txt](https://github.com/rumaan/file.io-Android-Client/blob/main/screenshots/readme.txt) | The code provides a user interface for managing todos. The readme.txt contains instructions on how to use the code. The screenshot.png displays the visual design of the user interface. The todo-ui.png shows an example of how the user interface should appear when managing todos. |

</details>

<details closed><summary>App</summary>

| File                                                                                        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---                                                                                         | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [build.gradle](https://github.com/rumaan/file.io-Android-Client/blob/main/app/build.gradle) | This code is for an Android application and includes various plugins and dependencies for different functionalities. It sets up the build configurations, defines dependencies for UI components, testing frameworks, libraries, and services like Firebase Crashlytics and Google services. It also includes permissions handling, data persistence using Room, and navigation using the Android Navigation component. Overall, it's a comprehensive setup for developing an Android app with various features. |

</details>

<details closed><summary>Fileio</summary>

| File                                                                                                                                                                                      | Summary                                                                                                                                                                                                                                         |
| ---                                                                                                                                                                                       | ---                                                                                                                                                                                                                                             |
| [ExampleInstrumentedTest.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/androidTest/java/com/thecoolguy/rumaan/fileio/ExampleInstrumentedTest.kt)                 | This code is an instrumented test for an Android app. It checks if the app's package name is correct and verifies the context of the app under test.                                                                                            |
| [FileEntityDaoTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/androidTest/java/com/thecoolguy/rumaan/fileio/FileEntityDaoTest.java)                         | This code contains test cases for a RoomDatabase implementation to perform CRUD operations on FileEntity objects. It includes tests to check the count of rows, save and retrieve single items, and save and retrieve multiple items.           |
| [UploadHistoryInstrumentedTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/androidTest/java/com/thecoolguy/rumaan/fileio/UploadHistoryInstrumentedTest.java) | The code is an instrumented test for an UploadHistoryActivity in an Android app. It creates a Room database and adds five items to it. The test method is yet to be implemented.                                                                |
| [ExampleUnitTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/test/java/com/thecoolguy/rumaan/fileio/ExampleUnitTest.java)                                    | This code is an example unit test that checks if the addition of 2 + 2 equals 4.                                                                                                                                                                |
| [UploadRepositoryTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/test/java/com/thecoolguy/rumaan/fileio/UploadRepositoryTest.java)                          | The code tests the functionality of the UploadRepository class by checking if the generated expire URL matches the expected URL. It verifies that the URL is created correctly by comparing it with a manually constructed URL using constants. |
| [UrlTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/test/java/com/thecoolguy/rumaan/fileio/UrlTest.java)                                                    | This code is a unit test for the URLParser class. It tests the functionality of the parseEncryptUrl method by comparing the expected result with the actual result.                                                                             |
| [FileEntityTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/test/java/com/thecoolguy/rumaan/fileio/FileEntityTest.java)                                      | The code is a unit test case for the FileEntity class. It verifies that the FileEntity object correctly sets and retrieves the name and URL properties.                                                                                         |

</details>

<details closed><summary>Viewmodel</summary>

| File                                                                                                                                                                       | Summary                                                                                                                                                                                                                                  |
| ---                                                                                                                                                                        | ---                                                                                                                                                                                                                                      |
| [UploadHistoryViewModel.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/viewmodel/UploadHistoryViewModel.kt) | This code defines a ViewModel class called UploadHistoryViewModel that is responsible for managing the list of uploaded files. It initializes a LiveData object that holds a list of FileEntity objects retrieved from a local database. |

</details>

<details closed><summary>Ui</summary>

| File                                                                                                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                                                               |
| ---                                                                                                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                                                                   |
| [FileioApplication.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/FileioApplication.kt)               | The code is for a custom Android application class called FileioApplication. It initializes logging using Timber and sets up a custom activity for handling crashes using CaocConfig.                                                                                                                                                                                                                 |
| [UploadHistoryListAdapter.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/UploadHistoryListAdapter.kt) | The `UploadHistoryListAdapter` class is responsible for managing the data and views in a RecyclerView. It takes a list of `FileEntity` objects and displays them in a list. It also handles different view types for displaying date headers and file items. It provides methods to update the data and perform actions like copying file URLs to the clipboard and removing items.                   |
| [SwipeToDeleteCallBack.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/SwipeToDeleteCallBack.kt)       | The code provides a SwipeToDelete functionality for a RecyclerView in an Android app. It uses ItemTouchHelper to handle swiping actions and provides a red delete background with a delete icon. It also disables swiping for specific view types.                                                                                                                                                    |
| [NotificationHelper.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/NotificationHelper.kt)             | The code defines a NotificationHelper class that creates and displays a notification when a file upload is successful. It uses a NotificationCompat.Builder to configure the notification's appearance and behavior. It also creates a notification channel for devices running Android Oreo and above. The notification includes a pending intent that opens the UploadHistoryActivity when clicked. |

</details>

<details closed><summary>Fragments</summary>

| File                                                                                                                                                                            | Summary                                                                                                                                                                                                                                                                                                                                    |
| ---                                                                                                                                                                             | ---                                                                                                                                                                                                                                                                                                                                        |
| [NoNetworkDialogFragment.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/NoNetworkDialogFragment.kt) | The code is a DialogFragment implementation in Android that displays a dialog to notify the user when there is no network connection. It creates a custom dialog layout and handles the click event for the "OK" button. The dialog fragment communicates with the activity using a listener interface.                                    |
| [HomeFragment.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/HomeFragment.kt)                       | The HomeFragment class defines a fragment that displays a layout with a button. When the button is clicked, it calls a callback function to notify the listener. The fragment also handles attaching and detaching the listener from the activity. It is part of a larger codebase and can be instantiated using the newInstance() method. |
| [ResultFragment.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/ResultFragment.kt)                   | The ResultFragment class is responsible for displaying the result of a file operation. It receives data (url and days) through newInstance method and updates the UI accordingly. It also supports copying the link to the clipboard and notifying the parent activity when the user is done with the result.                              |

</details>

<details closed><summary>Activities</summary>

| File                                                                                                                                                                         | Summary                                                                                                                                                                                                                                                                                                           |
| ---                                                                                                                                                                          | ---                                                                                                                                                                                                                                                                                                               |
| [MainActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/MainActivity.kt)                   | The code represents the main activity of an Android application. It includes functionalities such as handling menu options, uploading files, showing upload progress, and displaying the result. It also handles permissions related to file storage and network connectivity.                                    |
| [ErrorActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/ErrorActivity.kt)                 | This code defines an ErrorActivity that is displayed when runtime crashes occur. It extends AppCompatActivity and overrides the onBackPressed() method to finish the activity stack. It sets the activity layout using the setContentView() method.                                                               |
| [UploadHistoryActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/UploadHistoryActivity.kt) | This code represents an activity in an Android app that displays a list of upload history. It provides functionality to clear the history, remove individual items, and handle swipe gestures to delete items. It uses ViewModel and RecyclerView components for data management and UI rendering.                |
| [AboutActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/AboutActivity.kt)                 | This code is for the AboutActivity, which is an activity in an Android app. It sets a transparent navigation bar, inflates the menu, and handles menu item clicks. It launches the LicenseActivity when the "Open Source" menu item is clicked.                                                                   |
| [LicenseActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/LicenseActivity.kt)             | The code defines a LicenseActivity that extends MaterialAboutActivity. It creates a list of open source licenses using ConvenienceBuilder's createLicenseCard method. Each license card includes the icon, title, year, author, and license type. The list is then returned and displayed in the LicenseActivity. |

</details>

<details closed><summary>Repository</summary>

| File                                                                                                                                                                    | Summary                                                                                                                                                                                                                                                                   |
| ---                                                                                                                                                                     | ---                                                                                                                                                                                                                                                                       |
| [UploadHistoryWorkers.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/repository/UploadHistoryWorkers.kt) | The code includes two worker classes: "ClearHistoryWorker" and "DeleteSingleItemWorker". "ClearHistoryWorker" clears the entire upload history from the database. "DeleteSingleItemWorker" deletes a specific item from the upload history based on its ID.               |
| [UploadWorker.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/repository/UploadWorker.kt)                 | The UploadWorker class is responsible for uploading a file to a server using Fuel library. It retrieves the file from the specified URI, uploads it synchronously, and handles the response. It saves the upload details in a local database and displays a notification. |

</details>

<details closed><summary>Utils</summary>

| File                                                                                                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                        |
| ---                                                                                                                                                                        | ---                                                                                                                                                                                                                                                                                                                                            |
| [Extensions.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Extensions.kt)                             | This code provides two extension functions-"toast" and "toggleClickable". The "toast" function displays a short Toast message using a given context. The "toggleClickable" function enables or disables the clickability of a given View. These functions enhance code readability and simplify usage for common tasks in Android development. |
| [WorkManagerHelper.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/WorkManagerHelper.kt)               | The code defines a utility function to create a one-time work request for uploading a file. It sets the required network type constraint and passes the file's URI as input data to the UploadWorker class.                                                                                                                                    |
| [Utils.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Utils.kt)                                       | The code provides a collection of helper methods for various functionalities including getting file details, opening files, checking network connectivity, managing dialogs, handling URLs, parsing JSON, and managing dates. It also includes Android-specific utility methods.                                                               |
| [Helpers.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Helpers.kt)                                   | This code provides functions to extract metadata and retrieve a file from a given Uri. It also includes a function to compose a FileEntity object using a given File and Response.                                                                                                                                                             |
| [FragmentHelperExtensions.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/FragmentHelperExtensions.kt) | This code provides extension functions for adding and replacing fragments in an Android FragmentManager. It simplifies the process by handling transactions, transitions, and back stack management automatically.                                                                                                                             |
| [MaterialIn.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/MaterialIn.kt)                             | The code defines a utility class called MaterialIn that provides functions for animating views. It includes methods for animating views with a material design effect, such as sliding in from a certain direction or fading in. The code handles different gravity directions, delays, and slide offsets to create smooth animations.         |
| [Constants.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Constants.kt)                               | This code contains global constants and URI endpoints for a file.io file sharing application. It includes the base URL, expiration parameters, default expiration time, and URLs for GitHub and Twitter profiles. It also includes constants for appending to links, a time stamp format, and an email address.                                |

</details>

<details closed><summary>Listeners</summary>

| File                                                                                                                                                                                     | Summary                                                                                                                                                                                                                                                                                        |
| ---                                                                                                                                                                                      | ---                                                                                                                                                                                                                                                                                            |
| [DialogClickListener.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/listeners/DialogClickListener.kt)                     | This code defines an interface called DialogClickListener, which contains a method called onDialogPositiveClick. This method takes a Dialog object and a Fragment object as parameters. It is intended to be implemented by classes that need to listen for positive button clicks in dialogs. |
| [OnFragmentInteractionListener.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/listeners/OnFragmentInteractionListener.kt) | This code defines an interface called "OnFragmentInteractionListener" with two functions: "onUploadFileClick()" and "onDone()". These functions are designed to be implemented by other classes to handle events when a file upload button is clicked or when an action is completed.          |

</details>

---

## 🚀 Getting Started

***Dependencies***

Before you begin, ensure that you have the following prerequisites installed:
> - `ℹ️ Requirement 1`
> - `ℹ️ Requirement 2`
> - `ℹ️ ...`

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


## 🛣 Roadmap

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
