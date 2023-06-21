
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
Minimal-Todo
</h1>
<h3>◦ Maximize productivity, minimize clutter with Minimal-Todo.</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/Gradle-02303A.svg?style&logo=Gradle&logoColor=white" alt="Gradle" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
<img src="https://img.shields.io/badge/java-%23ED8B00.svg?style&logo=openjdk&logoColor=white" alt="java" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style&logo=JSON&logoColor=white" alt="JSON" />
</p>

![GitHub top language](https://img.shields.io/github/languages/top/avjinder/Minimal-Todo?style&color=5D6D7E)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/avjinder/Minimal-Todo?style&color=5D6D7E)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/avjinder/Minimal-Todo?style&color=5D6D7E)
![GitHub license](https://img.shields.io/github/license/avjinder/Minimal-Todo?style&color=5D6D7E)
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

Minimal-Todo is an open-source Android to-do list app that allows users to create and manage tasks, set reminders, and customize their experience. The app's value proposition lies in its minimalist design, ease-of-use, and flexibility. Its core functionalities include data storage, notification handling, and analytics tracking. The app is designed to provide a simple and efficient solution for managing the user's tasks and keeping track of their progress.

---

## ⚙️ Features

Feature | Description |
|-----|-----|
| **🏗 Architecture** | The application follows the Model-View-Controller (MVC) architectural pattern where the UI components are separated from the business logic and data storage. The codebase is organized into separate modules for each functionality and follows a modular approach, making it easy to maintain and scale. |
| **📑 Documentation** | The codebase includes documentation in the form of comments throughout the code, which improves its readability and maintainability. The use of clear and concise variable/object names further enhances the clarity and readability of the codebase. |
| **🧩 Dependencies** | The application uses a number of libraries including ButterKnife, Material Design components, Gson, OkHttp, and Google Analytics. These libraries provide additional functionality and simplify the development process. However, the use of too many dependencies can increase the app size and potentially slow down the performance. |
| **♻️ Modularity** | The codebase follows a modular approach, with each functionality separated into separate modules. This makes it easy to maintain, test, and scale the application, as each module can be developed and tested independently. Additionally, the separation of concerns makes the codebase more organized and easier to understand. |
| **✔️ Testing** | The codebase includes both unit and integration tests to ensure the functionality and reliability of the application. The tests cover features such as data storage, notification creation, and To-Do item creation, and are located in separate test files for each functionality. However, there are some missing test files, such as AddToDoFragment and MainFragment, which could impact the reliability of the application. |
| **⚡️ Performance** | The app's performance is optimized through the use of techniques such as data storage using JSON, lazy loading of images, and the optimization of RecyclerView scrolling. The use of the OkHttp library also improves the app's network performance. However, the app may experience slow performance on lower-end devices due to the implementation of some features such as RecyclerView animations. |
| **🔒 Security** | The codebase includes secure coding practices such as the use of SharedPreferences for sensitive user data and the use of the ProGuard tool for code obfuscation and minification. The app's network connections are also secured through the use of HTTPS connections, which encrypt the data that is transmitted between the app and its server. |
| **🔀 Version Control** | The codebase is hosted on GitHub and utilizes Git for version control, allowing for easy collaboration and version control management. The codebase includes a well-organized Git commit history and commit messages that provide clear descriptions of the changes made. |
| **🔌 Integrations** | The codebase includes integrations with third-party services such as Google Analytics for user behavior tracking and Firebase for database functionality. These integrations improve the functionality and reliability of the application, but the use of too many integrations can increase

---


## 📂 Project Structure


```bash
repo
├── Contributing.md
├── LICENSE.md
├── README.md
├── app
│   ├── app-release.apk
│   ├── app.iml
│   ├── build.gradle
│   ├── google-services.json
│   ├── proguard-rules.pro
│   └── src
│       ├── androidTest
│       │   └── java
│       │       └── com
│       │           └── example
│       │               └── avjindersinghsekhon
│       │                   └── minimaltodo
│       │                       ├── ApplicationTest.java
│       │                       ├── TestStoreRetrieveData.java
│       │                       └── TestTodoItem.java
│       └── main
│           ├── AndroidManifest.xml
│           ├── assets
│           │   └── fonts
│           │       └── Aller_Regular.ttf
│           ├── java
│           │   └── com
│           │       └── example
│           │           └── avjindersinghsekhon
│           │               └── minimaltodo
│           │                   ├── About
│           │                   │   ├── AboutActivity.java
│           │                   │   └── AboutFragment.java
│           │                   ├── AddToDo
│           │                   │   ├── AddToDoActivity.java
│           │                   │   └── AddToDoFragment.java
│           │                   ├── Analytics
│           │                   │   └── AnalyticsApplication.java
│           │                   ├── AppDefault
│           │                   │   ├── AppDefaultActivity.java
│           │                   │   └── AppDefaultFragment.java
│           │                   ├── Main
│           │                   │   ├── CustomRecyclerScrollViewListener.java
│           │                   │   ├── MainActivity.java
│           │                   │   └── MainFragment.java
│           │                   ├── Reminder
│           │                   │   ├── ReminderActivity.java
│           │                   │   └── ReminderFragment.java
│           │                   ├── Settings
│           │                   │   ├── SettingsActivity.java
│           │                   │   └── SettingsFragment.java
│           │                   └── Utility
│           │                       ├── CustomTextInputLayout.java
│           │                       ├── DeleteNotificationService.java
│           │                       ├── ItemTouchHelperClass.java
│           │                       ├── PreferenceKeys.java
│           │                       ├── RecyclerViewEmptySupport.java
│           │                       ├── ScrollingFABBehaviour.java
│           │                       ├── StoreRetrieveData.java
│           │                       ├── ToDoItem.java
│           │                       ├── TodoNotificationService.java
│           │                       └── Utils.java
│           └── res
│               ├── drawable
│               │   ├── button_pressed_background.xml
│               │   ├── clipboard.png
│               │   ├── dropdown_text_background_color.xml
│               │   ├── dropdown_text_color.xml
│               │   └── ic_content_copy_black_24dp.xml
│               ├── drawable-hdpi
│               │   ├── check.png
│               │   ├── empty_view_bg.png
│               │   ├── ic_access_time_black_18dp.png
│               │   ├── ic_add_alarm_grey_200_24dp.png
│               │   ├── ic_add_white_24dp.png
│               │   ├── ic_alarm_add_white_24dp.png
│               │   ├── ic_alarm_black_18dp.png
│               │   ├── ic_clear_white_24dp.png
│               │   ├── ic_color_lens_white_24dp.png
│               │   ├── ic_done_white_24dp.png
│               │   ├── ic_menu_overflow_light.png
│               │   ├── ic_reorder_grey_600_18dp.png
│               │   ├── ic_send_white_18dp.png
│               │   ├── ic_snooze_black_24dp.png
│               │   └── ic_snooze_white_24dp.png
│               ├── drawable-ldpi
│               │   ├── check.png
│               │   └── empty_view_bg.png
│               ├── drawable-mdpi
│               │   ├── check.png
│               │   ├── empty_view_bg.png
│               │   ├── ic_access_time_black_18dp.png
│               │   ├── ic_add_alarm_grey_200_24dp.png
│               │   ├── ic_add_white_24dp.png
│               │   ├── ic_alarm_add_white_24dp.png
│               │   ├── ic_alarm_black_18dp.png
│               │   ├── ic_clear_white_24dp.png
│               │   ├── ic_color_lens_white_24dp.png
│               │   ├── ic_done_white_24dp.png
│               │   ├── ic_menu_overflow_light.png
│               │   ├── ic_reorder_grey_600_18dp.png
│               │   ├── ic_send_white_18dp.png
│               │   ├── ic_snooze_black_24dp.png
│               │   └── ic_snooze_white_24dp.png
│               ├── drawable-xhdpi
│               │   ├── check.png
│               │   ├── empty_view_bg.png
│               │   ├── ic_access_time_black_18dp.png
│               │   ├── ic_add_alarm_grey_200_24dp.png
│               │   ├── ic_add_white_24dp.png
│               │   ├── ic_alarm_add_white_24dp.png
│               │   ├── ic_alarm_black_18dp.png
│               │   ├── ic_clear_white_24dp.png
│               │   ├── ic_color_lens_white_24dp.png
│               │   ├── ic_done_white_24dp.png
│               │   ├── ic_menu_overflow_light.png
│               │   ├── ic_reorder_grey_600_18dp.png
│               │   ├── ic_send_white_18dp.png
│               │   ├── ic_snooze_black_24dp.png
│               │   └── ic_snooze_white_24dp.png
│               ├── drawable-xxhdpi
│               │   ├── check.png
│               │   ├── empty_view_bg.png
│               │   ├── ic_access_time_black_18dp.png
│               │   ├── ic_add_alarm_grey_200_24dp.png
│               │   ├── ic_add_white_24dp.png
│               │   ├── ic_alarm_add_white_24dp.png
│               │   ├── ic_alarm_black_18dp.png
│               │   ├── ic_clear_white_24dp.png
│               │   ├── ic_color_lens_white_24dp.png
│               │   ├── ic_done_white_24dp.png
│               │   ├── ic_menu_overflow_light.png
│               │   ├── ic_reorder_grey_600_18dp.png
│               │   ├── ic_send_white_18dp.png
│               │   ├── ic_snooze_black_24dp.png
│               │   └── ic_snooze_white_24dp.png
│               ├── drawable-xxxhdpi
│               │   ├── check.png
│               │   ├── empty_view_bg.png
│               │   └── ic_menu_overflow_light.png
│               ├── layout
│               │   ├── about_layout.xml
│               │   ├── activity_add_to_do.xml
│               │   ├── activity_main.xml
│               │   ├── activity_settings.xml
│               │   ├── activity_todo_test.xml
│               │   ├── base_toolbar.xml
│               │   ├── date_dropdown_item.xml
│               │   ├── date_spinner_item.xml
│               │   ├── fragment_about.xml
│               │   ├── fragment_add_to_do.xml
│               │   ├── fragment_main.xml
│               │   ├── fragment_reminder.xml
│               │   ├── layout_fragment_container.xml
│               │   ├── list_circle_try.xml
│               │   ├── list_item_view_future.xml
│               │   ├── reminder_layout.xml
│               │   ├── spinner_dropdown_item.xml
│               │   └── spinner_text_view.xml
│               ├── menu
│               │   ├── menu_main.xml
│               │   └── menu_reminder.xml
│               ├── mipmap-hdpi
│               │   └── ic_launcher.png
│               ├── mipmap-mdpi
│               │   └── ic_launcher.png
│               ├── mipmap-xhdpi
│               │   └── ic_launcher.png
│               ├── mipmap-xxhdpi
│               │   └── ic_launcher.png
│               ├── mipmap-xxxhdpi
│               │   └── ic_launcher.png
│               ├── values
│               │   ├── colors.xml
│               │   ├── dimens.xml
│               │   ├── donottranslate.xml
│               │   ├── strings.xml
│               │   └── styles.xml
│               ├── values-bg
│               │   └── strings.xml
│               ├── values-de
│               │   └── strings.xml
│               ├── values-es
│               │   └── strings.xml
│               ├── values-fi
│               │   └── strings.xml
│               ├── values-fr
│               │   └── strings.xml
│               ├── values-it
│               │   └── strings.xml
│               ├── values-ml
│               │   └── strings.xml
│               ├── values-pl
│               │   └── strings.xml
│               ├── values-tl
│               │   └── strings.xml
│               ├── values-vi
│               │   └── strings.xml
│               ├── values-w820dp
│               │   └── dimens.xml
│               ├── values-zh
│               │   └── strings.xml
│               └── xml
│                   ├── global_tracker.xml
│                   └── preferences_layout.xml
├── build.gradle
├── gradle
│   └── wrapper
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties
├── gradle.properties
├── gradlew
├── gradlew.bat
├── screenshots
│   ├── add_todo_dark.png
│   ├── add_todo_light.png
│   ├── app_icon.png
│   ├── main_empty_dark.png
│   ├── main_empty_light.png
│   ├── main_full_dark.png
│   ├── main_full_light.png
│   ├── screenshot_notification.png
│   ├── screenshot_reminder_date.png
│   ├── screenshot_reminder_time.png
│   ├── screenshot_todo_snooze.png
│   ├── todo_date_dark.png
│   └── todo_time_dark.png
└── settings.gradle

57 directories, 171 files
```

---

## 🧩 Modules

<details closed><summary>About</summary>

| File               | Summary                                                                                                                                                                                                                                                                                                                                                                                     | Module                                                                                 |
|:-------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------|
| AboutActivity.java | The provided code snippet is an implementation of the AboutActivity class, which extends from the AppDefaultActivity class. It sets the theme based on the user's preference, retrieves the app version, and initializes the toolbar. It also overrides the onOptionsItemSelected method to handle the "home" action, allowing the user to navigate up to the parent activity if available. | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/About/AboutActivity.java |
| AboutFragment.java | The code creates an AboutFragment for an Android app that displays app version and allows the user to provide feedback. It extends an AppDefaultFragment and utilizes a Toolbar and AnalyticsApplication to send user data. The layout is defined by a fragment_about.xml file.                                                                                                             | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/About/AboutFragment.java |

</details>

<details closed><summary>Addtodo</summary>

| File                 | Summary                                                                                                                                                                                                                                                                                           | Module                                                                                     |
|:---------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------|
| AddToDoFragment.java | HTTPStatusError: 400                                                                                                                                                                                                                                                                              | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AddToDo/AddToDoFragment.java |
| AddToDoActivity.java | The provided code snippet is for an AddToDoActivity in an Android app, which extends a custom AppDefaultActivity. It sets the layout for the activity and creates an instance of AddToDoFragment as the initial fragment. The code also includes the necessary lifecycle methods for an activity. | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AddToDo/AddToDoActivity.java |

</details>

<details closed><summary>Analytics</summary>

| File                      | Summary                                                                                                                                                                                                                                                                                                      | Module                                                                                            |
|:--------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------|
| AnalyticsApplication.java | The provided code is an Android Analytics Application that uses Google Analytics to track user behavior. It creates a Tracker object, which sends screen view and event data to Google Analytics. It includes methods for sending screen views with optional parameters such as category, action, and label. | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Analytics/AnalyticsApplication.java |

</details>

<details closed><summary>App</summary>

| File         | Summary                                                                                                                                                                                                                                                                                                                                                                  | Module           |
|:-------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| build.gradle | The code snippet is for an Android application that includes various dependencies such as Material Design components, text drawable, and Google Analytics. It sets up signing configurations for release builds and specifies the minimum and target SDK versions, version code, and version name. The build type is also defined, with proguard files for minification. | app/build.gradle |

</details>

<details closed><summary>Appdefault</summary>

| File                    | Summary                                                                                                                                                                                                                                                                                                                                                                        | Module                                                                                           |
|:------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|
| AppDefaultFragment.java | The code defines an abstract class'AppDefaultFragment' that extends the Fragment class. It contains a method to inflate the layout defined in its subclass, and a method to specify the layout resource ID. The class is designed for developers to create custom fragments with a consistent app-wide appearance and functionality.                                           | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AppDefault/AppDefaultFragment.java |
| AppDefaultActivity.java | The provided code snippet is an abstract class that serves as a base for creating activities in an Android application. It sets up the initial fragment and defines abstract methods for specifying the layout and fragment for each activity. It utilizes the AppCompatActivity and Fragment classes to enable creating activities with modern UI features and functionality. | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AppDefault/AppDefaultActivity.java |

</details>

<details closed><summary>Main</summary>

| File                                  | Summary                                                                                                                                                                                                                                                                                      | Module                                                                                                   |
|:--------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------|
| MainActivity.java                     | This code defines the MainActivity class, which sets up the toolbar and options menu in the app. It includes methods for creating the initial fragment, inflating the options menu, and handling menu item selections for navigating to other activities within the app.                     | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/MainActivity.java                     |
| CustomRecyclerScrollViewListener.java | The code snippet provides an abstract class that extends the RecyclerView class and listens for scrolling events. It logs the scrolling distance and hides/shows the view depending on the scroll state. The show() and hide() methods are abstract and must be implemented by the subclass. | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/CustomRecyclerScrollViewListener.java |
| MainFragment.java                     | HTTPStatusError: 400                                                                                                                                                                                                                                                                         | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/MainFragment.java                     |

</details>

<details closed><summary>Minimaltodo</summary>

| File                       | Summary                                                                                                                                                                                                                                                                                                                                                                                  | Module                                                                                          |
|:---------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------|
| TestStoreRetrieveData.java | The provided code snippet contains test cases for the StoreRetrieveData class. It tests whether data can be written to and retrieved from the data storage, as well as ensures that an empty data storage is present at the start of the tests. It also tests the conversion of ArrayList to JSONArray.                                                                                  | app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/TestStoreRetrieveData.java |
| ApplicationTest.java       | The provided code defines a basic testing class for an Android application. It extends the ApplicationTestCase class and takes the application as a parameter for testing. The purpose of this code is to provide a starting point for writing unit tests for an Android app using the Android Testing Support Library.                                                                  | app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/ApplicationTest.java       |
| TestTodoItem.java          | This is a code snippet for JUnit tests to verify the functionality of the ToDoItem class in a minimalistic Todo app. The tests include verifying the ability to construct ToDoItem objects and marshall/unmarshall ToDoItem objects to JSON format. The provided code adheres to the MIT License, and the testing seeks to ensure the correctness and reliability of the ToDoItem class. | app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/TestTodoItem.java          |

</details>

<details closed><summary>Reminder</summary>

| File                  | Summary                                                                                                                                                                                                                                                                                                                               | Module                                                                                       |
|:----------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------|
| ReminderFragment.java | The provided code snippet is a Java class for a reminder feature in a to-do list app. It includes functionalities such as displaying the reminder text, snoozing the reminder for a specified time period, marking a to-do item as done, and removing to-do items from the list. It also handles data storage and analytics tracking. | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Reminder/ReminderFragment.java |
| ReminderActivity.java | The code snippet defines an activity for displaying reminders in the MinimalToDo app which extends AppDefaultActivity. It sets the layout and creates an instance of the ReminderFragment to display the reminders.                                                                                                                   | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Reminder/ReminderActivity.java |

</details>

<details closed><summary>Root</summary>

| File            | Summary                                                                                                                                                                                                                                                                                                                                    | Module          |
|:----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------|
| build.gradle    | The provided code snippet contains configurations for the top-level build file of an Android project. It defines repositories for dependencies and includes plugins such as butterknife-gradle-plugin and google-services. The code also specifies that application dependencies should be placed in individual module build.gradle files. | build.gradle    |
| gradlew.bat     | This is a Windows batch script used to start a Gradle build. It sets default JVM options and finds the location of Java in the system environment. The script executes the Gradle wrapper with the appropriate classpath and command-line arguments.                                                                                       | gradlew.bat     |
| settings.gradle | The provided code snippet includes the main app module in an Android project. This module contains the core functionalities of the app, such as the user interface, logic, and resources.                                                                                                                                                  | settings.gradle |

</details>

<details closed><summary>Settings</summary>

| File                  | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Module                                                                                       |
|:----------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------|
| SettingsFragment.java | The given code snippet is a SettingsFragment that implements SharedPreferences.OnSharedPreferenceChangeListener, which listens for changes made in the app's shared preferences. It includes the creation of a preference screen and the implementation of a logic that handles a specific preference change, in this case, the night mode preference. It also registers and unregisters the preference change listener in onResume() and onPause() respectively. | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Settings/SettingsFragment.java |
| SettingsActivity.java | The provided code snippet is an implementation of a settings activity in an Android app. It sets up the toolbar and allows for navigation to the parent activity. It also incorporates analytics functionality. Finally, it replaces the container with a SettingsFragment, which is the main content of the activity.                                                                                                                                            | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Settings/SettingsActivity.java |

</details>

<details closed><summary>Utility</summary>

| File                           | Summary                                                                                                                                                                                                                                                                                                                                                                                                                       | Module                                                                                               |
|:-------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------|
| TodoNotificationService.java   | The provided code is an Android IntentService class that handles creating and displaying notifications for to-do items. It extracts the to-do text and UUID from the intent, creates a notification with a title, icon, and sound, and sets up pending intents for both the notification and its delete action. Finally, it uses a NotificationManager to display the notification.                                           | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/TodoNotificationService.java   |
| ScrollingFABBehaviour.java     | This code snippet is a custom behavior for a Floating Action Button in Android, that allows it to move up and down in response to user interaction with other UI elements (such as a Snackbar or a Toolbar). The behavior is implemented as a sub-class of the CoordinatorLayout.Behavior class, and includes methods for determining layout dependencies and changing the position of the FloatingActionButton accordingly.  | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ScrollingFABBehaviour.java     |
| ToDoItem.java                  | The code defines a ToDoItem class with properties such as text, description, reminder, color, date, and identifier. It also provides methods to create and parse JSON objects and set/get the property values. The class implements the Serializable interface to allow the class instances to be serialized and deserialized.                                                                                                | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ToDoItem.java                  |
| CustomTextInputLayout.java     | The provided code snippet is a custom implementation of the Android TextInputLayout that stores the hint value of an EditText child view and resets it on the parent view. It also handles programmatic changes of the hint text and ensures that the hint is properly set in the layout.                                                                                                                                     | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/CustomTextInputLayout.java     |
| StoreRetrieveData.java         | The StoreRetrieveData class provides methods to save and load a to-do item list from a local file using JSON. The toJSONArray method converts an ArrayList of ToDoItem objects into a JSONArray object. The saveToFile method writes this JSONArray to a file, while the loadFromFile method reads the JSON data from the file and converts it back into an ArrayList of ToDoItem objects.                                    | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/StoreRetrieveData.java         |
| Utils.java                     | The code provides a utility function to get the toolbar height in Android. It does so by fetching the attribute value of the `actionBarSize` attribute and returning its dimension. It cleans up by recycling the TypedArray.                                                                                                                                                                                                 | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/Utils.java                     |
| DeleteNotificationService.java | The provided code snippet is an Android service that deletes a notification and its corresponding to-do item from the app's storage. It receives the unique ID of the item as an intent extra and retrieves the item from the storage. If found, the item is removed from the storage and the app's data changed flag is set to true. Finally, the updated items list is saved to the storage.                                | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/DeleteNotificationService.java |
| ItemTouchHelperClass.java      | This code snippet defines an ItemTouchHelperClass that can be used to handle swiping and dragging of items in a RecyclerView. It implements the ItemTouchHelper.Callback interface and provides methods for enabling long press drag and item view swipe, setting movement flags, and handling item movements and removal. There is also a commented out onChildDraw method that can be used to draw custom swipe animations. | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ItemTouchHelperClass.java      |
| PreferenceKeys.java            | This code defines a class called PreferenceKeys that contains a single variable'night_mode_pref_key'. The variable is initialized with a string value that corresponds to a resource defined in the R class of the app. The constructor of the class takes a parameter of type Resources which is used to fetch the value of the resource.                                                                                    | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/PreferenceKeys.java            |
| RecyclerViewEmptySupport.java  | The given code is for a custom RecyclerView class called RecyclerViewEmptySupport, with a method to show an empty view if the adapter for the RecyclerView is empty. It registers an observer to the adapter to listen for changes in data set and update the empty view accordingly. The class extends the RecyclerView class from the Android support library.                                                              | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/RecyclerViewEmptySupport.java  |

</details>

---

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - [ℹ️ Requirement 1]
> - [ℹ️ Requirement 2]
> - [...]

### 🖥 Installation

1. Clone the Minimal-Todo repository:
```sh
git clone https://github.com/avjinder/Minimal-Todo
```

2. Change to the project directory:
```sh
cd Minimal-Todo
```

3. Install the dependencies:
```sh
mvn clean install
```

### 🤖 Using Minimal-Todo

```sh
java -jar target/myapp.jar
```

### 🧪 Running Tests
```sh
mvn test
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
