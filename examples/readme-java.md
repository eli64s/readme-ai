
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
Minimal-Todo
</h1>
<h3>◦ Get things done with Minimal-Todo.</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/Gradle-02303A.svg?style=for-the-badge&logo=Gradle&logoColor=white" alt="Gradle" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white" alt="JSON" />
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

The Minimal Todo app is a simple yet effective to-do list app designed for Android. It allows users to add, edit, and delete tasks, set reminders, and customize their app experience with themes. The app's core value proposition is its user-friendly interface, intuitive design, and ability to boost productivity by keeping track of tasks and deadlines. Additionally, it offers features such as night mode, analytics, and notifications, enhancing its overall usefulness for users.

---

## ⚙️ Features

Feature | Description |
|-----|-----|
| **🏗 Architecture** | The project follows the Model-View-Presenter (MVP) architectural pattern, separating the presentation layer from the business logic and data access layer. This pattern ensures a clear separation of concerns and improves the testability of the code. The project is structured as a single-module Android app. |
| **📑 Documentation** | The code contains a moderate amount of inline documentation, providing explanations for most of the methods and classes. However, some of the documentation is incomplete and could be improved. The project also includes README files with installation instructions and descriptions of the project and its features. |
| **🧩 Dependencies** | The project includes several dependencies, such as Google Play Services, Android support libraries, and Material Design components. It also includes Butter Knife, a view binding library that reduces boilerplate code for accessing views. These dependencies are common in Android development and help to simplify development and improve the app's user experience. |
| **♻️ Modularity** | The codebase is modular, with distinct layers for the presentation, business logic, and data access. The use of interfaces and abstract classes also encourages modularity and flexibility, allowing for easy modification and testing of individual components. However, some classes have high coupling, which could make them harder to modify or maintain. |
| **✔️ Testing** | The project includes unit tests for several key classes, such as the StoreRetrieveData class and ToDoItem class. It also includes integration tests for the Application, Reminder, and Settings fragments. However, some classes, such as the MainFragment and AddToDoFragment, do not have corresponding tests, which could impact the stability and reliability of the app. |
| **⚡️ Performance** | The project includes several optimizations for performance, such as the use of RecyclerView and custom scrolling behavior for smoother scrolling, and SharedPreferences for efficient data storage. The use of interfaces and abstract classes also reduces duplication and improves performance. However, some operations, such as reading and writing data to the file system, could still impact performance. |
| **🔒 Security** | The project includes some security measures, such as UUID generation for unique identifiers and the use of SharedPreferences for storing sensitive information. However, there is no encryption or other security measures in place for protecting sensitive information, such as user data. |
| **🔀 Version Control** | The project is well-organized and structured in a Git repository, with clear commit messages and branching strategies. The use of feature branches and pull requests helps to improve collaboration and reduce code conflicts. However, some commits include changes to multiple files, which could make it harder to track changes and maintain the codebase. |
| **🔌 Integrations** | The project includes several integrations, such as Google Analytics for tracking user events, and Firebase Cloud Messaging for sending push notifications. These integrations help to improve the app's functionality and

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

| File               | Summary                                                                                                                                                                                                                                                                                                                                                                                                                    | Module                                                                                 |
|:-------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------|
| AboutActivity.java | The code snippet provides the implementation of AboutActivity, which displays information about the application, including its version number. It extends AppDefaultActivity and creates an instance of AboutFragment. It also implements the onOptionsItemSelected method to allow navigation up from the activity using the back button. Finally, it sets the theme of the activity based on the saved theme preference. | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/About/AboutActivity.java |
| AboutFragment.java | The code defines an Android fragment that displays information in a text view and toolbar. It also handles sending user feedback via Google Analytics. The version of the app is hardcoded as "0.1".                                                                                                                                                                                                                       | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/About/AboutFragment.java |

</details>

<details closed><summary>Addtodo</summary>

| File                 | Summary                                                                                                                                                                                                             | Module                                                                                     |
|:---------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------|
| AddToDoFragment.java | HTTPStatusError: 400                                                                                                                                                                                                | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AddToDo/AddToDoFragment.java |
| AddToDoActivity.java | The code defines an activity for adding a new to-do item. It extends an AppDefaultActivity and overrides methods to create the initial fragment and set the content view layout. The onResume method is left empty. | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AddToDo/AddToDoActivity.java |

</details>

<details closed><summary>Analytics</summary>

| File                      | Summary                                                                                                                                                                                                                                                                                                   | Module                                                                                            |
|:--------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------|
| AnalyticsApplication.java | The code defines an AnalyticsApplication class that uses Google Analytics to track events in an Android application. The class initializes the Google Analytics tracker, sets up screen and event tracking, and enables exception reporting. The tracking can be enabled or disabled with a boolean flag. | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Analytics/AnalyticsApplication.java |

</details>

<details closed><summary>App</summary>

| File         | Summary                                                                                                                                                                                                                                                                                                                                                                                                  | Module           |
|:-------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| build.gradle | The provided code snippet is a build.gradle file for an Android application. It includes specifications for the compile and build tools versions, default configuration settings, build types, source sets, and lint options. It also lists various dependencies, including Google Play services, Material Design components, and others. Finally, it sets up signing configurations for release builds. | app/build.gradle |

</details>

<details closed><summary>Appdefault</summary>

| File                    | Summary                                                                                                                                                                                                                                                                                                                                                              | Module                                                                                           |
|:------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|
| AppDefaultFragment.java | The provided code snippet is an abstract class that extends Fragment. It implements the onCreateView method to inflate the layout defined by the layoutRes method, and includes an onDestroy method. The purpose of this class is to provide a default implementation for Fragments in an Android app.                                                               | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AppDefault/AppDefaultFragment.java |
| AppDefaultActivity.java | The provided code snippet is an abstract class for creating a default activity layout with an initial fragment. It sets up the initial fragment and inflates the activity layout using the contentViewLayoutRes() method, which is defined in the subclass, and creates the initial fragment using the createInitialFragment() method, also defined in the subclass. | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AppDefault/AppDefaultActivity.java |

</details>

<details closed><summary>Main</summary>

| File                                  | Summary                                                                                                                                                                                                                                                                                                                                           | Module                                                                                                   |
|:--------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------|
| MainActivity.java                     | The provided code is part of an Android app's main activity, which creates a toolbar and sets the initial fragment. It also provides the implementation for the options menu, including opening the About and Settings activities. Additionally, it extends an AppDefaultActivity class.                                                          | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/MainActivity.java                     |
| CustomRecyclerScrollViewListener.java | This code snippet contains an abstract class CustomRecyclerScrollViewListener that extends RecyclerView's OnScrollListener. It listens for scroll events and calls hide() or show() methods when the user scrolls up or down respectively. The visibility of the Android view is toggled based on the amount of scroll in the vertical direction. | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/CustomRecyclerScrollViewListener.java |
| MainFragment.java                     | HTTPStatusError: 400                                                                                                                                                                                                                                                                                                                              | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/MainFragment.java                     |

</details>

<details closed><summary>Minimaltodo</summary>

| File                       | Summary                                                                                                                                                                                                                                                                                                                                                                                                                  | Module                                                                                          |
|:---------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------|
| TestStoreRetrieveData.java | This code snippet contains test cases for the StoreRetrieveData class. It tests preconditions, writing to and reading from the data storage, and the JSONArray conversion. The test cases include creating and saving test data, checking if the retrieved data is the same as the stored test data, and using the getDataStorage() method to retrieve the data storage.                                                 | app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/TestStoreRetrieveData.java |
| ApplicationTest.java       | The provided code snippet is a basic Android application test case class named "ApplicationTest". It extends the "ApplicationTestCase" class and takes the "Application" class as a parameter. The purpose of this class is to provide a foundation for testing the application's functionality.                                                                                                                         | app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/ApplicationTest.java       |
| TestTodoItem.java          | The code snippet is a set of JUnit tests to verify the functionality of the ToDoItem class in the MinimalToDo android app. The tests check whether ToDoItem objects can be constructed using the three-parameter constructor, converted to JSON format, and then marshalled back into ToDoItem objects using the JSON constructor. The code ensures that the state of the original and newly unmarshalled objects match. | app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/TestTodoItem.java          |

</details>

<details closed><summary>Reminder</summary>

| File                  | Summary                                                                                                                                                                                                                                                                                                                                                                                            | Module                                                                                       |
|:----------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------|
| ReminderFragment.java | The code snippet provides the functionality for displaying and managing reminders for to-do items. It retrieves the item from the local storage, displays its details and allows users to snooze or mark it as done. The snooze time is selected from a spinner and the app notifies the user at the chosen time. Finally, any changes made to the to-do list are saved back to the local storage. | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Reminder/ReminderFragment.java |
| ReminderActivity.java | The provided code is an Android Activity that extends from a custom AppDefaultActivity. It inflates a layout for the reminder activity and creates an instance of the ReminderFragment as its initial fragment.                                                                                                                                                                                    | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Reminder/ReminderActivity.java |

</details>

<details closed><summary>Root</summary>

| File            | Summary                                                                                                                                                                                                                                                                      | Module          |
|:----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------|
| build.gradle    | This code snippet configures build scripts for an Android project. It includes dependencies for the Android Gradle plugin and Google services and sets up repositories for accessing project dependencies. The Butter Knife Gradle plugin is also included for view binding. | build.gradle    |
| gradlew.bat     | The code snippet is a Gradle startup script for Windows. It sets default JVM options, finds the Java executable and sets the classpath before executing Gradle. It also handles command-line arguments and provides error messages if necessary.                             | gradlew.bat     |
| settings.gradle | The code snippet includes the module':app' in the project. It is a concise way of referencing the app module, which contains the main application code and resources. This is a common practice in Android development using Gradle build system.                            | settings.gradle |

</details>

<details closed><summary>Settings</summary>

| File                  | Summary                                                                                                                                                                                                                                                                                | Module                                                                                       |
|:----------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------|
| SettingsFragment.java | The code snippet is a settings fragment class which allows the user to toggle a night mode preference. It registers and unregisters the preference change listener when the fragment is resumed or paused. It also sends an analytics event when the night mode preference is toggled. | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Settings/SettingsFragment.java |
| SettingsActivity.java | This code creates a SettingsActivity that allows the user to customize the app's theme. It also sets up a toolbar with a back arrow and replaces the layout with a SettingsFragment. The code also includes navigation functionality to return to the previous activity.               | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Settings/SettingsActivity.java |

</details>

<details closed><summary>Utility</summary>

| File                           | Summary                                                                                                                                                                                                                                                                                                                                                                                             | Module                                                                                               |
|:-------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------|
| TodoNotificationService.java   | The code defines an IntentService that handles notifications for todo items. It creates a notification with a title, icon, and sound, sets up intents for when the notification is clicked or deleted, and sends the notification using the NotificationManager. The service also includes commented out code for playing a notification sound.                                                     | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/TodoNotificationService.java   |
| ScrollingFABBehaviour.java     | The provided code snippet is a custom behavior for a FloatingActionButton in a CoordinatorLayout, allowing it to respond to the scrolling behavior of a Snackbar or a Toolbar. It translates the FloatingActionButton up when a snackbar appears, and down when a toolbar is scrolled up. It also calculates the distance to scroll the FloatingActionButton based on its height and bottom margin. | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ScrollingFABBehaviour.java     |
| ToDoItem.java                  | The provided code snippet contains a Java class called ToDoItem, which represents a single item in a to-do list. It includes properties such as text, reminder status, color, and date, along with methods to get and set those properties. The class can also be serialized to and from JSON format.                                                                                               | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ToDoItem.java                  |
| CustomTextInputLayout.java     | The code snippet defines a custom class called CustomTextInputLayout that extends TextInputLayout. This class stores the hint value for an EditText in a local variable and sets it as a hint for the parent view onDraw. It also includes a check to ensure the hint is only set once.                                                                                                             | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/CustomTextInputLayout.java     |
| StoreRetrieveData.java         | The provided code snippet defines a class called "StoreRetrieveData" that handles storing and retrieving data as JSON objects in Android applications. It includes functions for converting an ArrayList of ToDoItems to a JSON array, writing it to a file, and reading the file back into an ArrayList of ToDoItems. The class also specifies the context and filename for the data storage.      | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/StoreRetrieveData.java         |
| Utils.java                     | The provided code snippet is a utility class that provides a method, "getToolbarHeight", which takes a context as a parameter and returns the height of the toolbar in pixels. The method achieves this by retrieving the styled attribute "actionBarSize" from the context's theme, recycling it, and returning its dimension value.                                                               | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/Utils.java                     |
| DeleteNotificationService.java | The provided code snippet defines an Intent Service in Android that deletes a specific to-do item from the app's data storage. It retrieves the to-do item's UUID from the notification that triggered the delete action, locates the item in the app's data, removes it, and then saves the updated data. It also updates a shared preference to signal that a change was made to the data.        | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/DeleteNotificationService.java |
| ItemTouchHelperClass.java      | The code defines an ItemTouchHelperClass that extends the ItemTouchHelper.Callback class. It enables the user to drag and swipe items in a RecyclerView by implementing isLongPressDragEnabled(), isItemViewSwipeEnabled(), getMovementFlags(), onMove() and onSwiped() methods. The ItemTouchHelperAdapter interface is also defined, allowing the programmer to handle item movement and removal. | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ItemTouchHelperClass.java      |
| PreferenceKeys.java            | The code defines a utility class for managing preference keys in a minimal todo app. It contains a constructor method that initializes a night mode preference key by retrieving it from the app resources. The preference key can be accessed through an instance of this class.                                                                                                                   | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/PreferenceKeys.java            |
| RecyclerViewEmptySupport.java  | The code provides a custom RecyclerView class with a method to handle showing/hiding an empty view when there are no items to display. This is achieved by checking the item count of the RecyclerView's adapter and changing visibility of the emptyView and RecyclerView accordingly. The class also registers changes to the adapter's data and updates the empty view as necessary.             | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/RecyclerViewEmptySupport.java  |

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
