
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
Minimal-Todo
</h1>
<h3 align="center">📍 Maximize your productivity with Minimal-Todo on GitHub.</h3>
<h3 align="center">⚙️ Developed with the software and tools below:</h3>

<p align="center">
<img src="https://img.shields.io/badge/Gradle-02303A.svg?style=for-the-badge&logo=Gradle&logoColor=white" alt="Gradle" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="Markdown" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white" alt="JSON" />
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

The Minimal-Todo project is an Android application aimed at providing a simple, yet effective to-do list functionality with customizable themes. The project includes features such as adding and removing tasks, setting reminders, and snoozing, email feedback, analytics tracking, and support for different Android versions. The value proposition of this project lies in its minimalistic design and user-friendly interface, which makes it easy for users to manage their tasks efficiently.

---

## 💫 Features

Error generating file summary. Exception: 

---


<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

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

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 🧩 Modules

<details closed><summary>About</summary>

| File               | Summary                                                                                                                                                                                                                                                                                                                                                                                   | Module                                                                                 |
|:-------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------|
| AboutActivity.java | The code snippet defines an activity for displaying About information for an app. It retrieves the app's version and displays it, sets the theme based on user preference, and includes a toolbar with a back button. The activity also includes a fragment for displaying the details of the About information.                                                                          | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/About/AboutActivity.java |
| AboutFragment.java | The code defines the AboutFragment class that extends AppDefaultFragment. It contains a text view displaying the app's version and a toolbar. It also initializes Google Analytics to track user interactions, and implements a click listener on a "Contact Me" text view to send feedback. Finally, it provides a static factory method to create instances of the AboutFragment class. | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/About/AboutFragment.java |

</details>

<details closed><summary>Addtodo</summary>

| File                 | Summary                                                                                                                                                                                                                                                                               | Module                                                                                     |
|:---------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------|
| AddToDoFragment.java | Error generating file summary. Exception: Client error '400 Bad Request' for url 'https://api.openai.com/v1/chat/completions'                                                                                                                                                         | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AddToDo/AddToDoFragment.java |
|                      | For more information check: https://httpstatuses.com/400                                                                                                                                                                                                                              |                                                                                            |
| AddToDoActivity.java | The code defines an activity to add a new to-do item, which extends from a custom base activity. It sets the activity's layout to a specific XML file and initializes the fragment that will be displayed. Additionally, it overrides the onResume method of the base activity class. | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AddToDo/AddToDoActivity.java |

</details>

<details closed><summary>Analytics</summary>

| File                      | Summary                                                                                                                                                                                                                                                                                                                  | Module                                                                                            |
|:--------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------|
| AnalyticsApplication.java | The code defines an AnalyticsApplication class with methods for sending events and screen views to Google Analytics. It sets up a tracker using a unique tracking ID and includes functionality for reporting exceptions. The send() method tracks screen views and various events, such as category, action, and label. | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Analytics/AnalyticsApplication.java |

</details>

<details closed><summary>App</summary>

| File         | Summary                                                                                                                                                                                                                                                                                                                        | Module           |
|:-------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| build.gradle | The code snippet contains configuration settings for an Android application, including compile, build, and target versions, as well as dependencies such as Google Play Services, Material Design components, and date time picker's library. It also includes a signing configuration for the release build and lint options. | app/build.gradle |

</details>

<details closed><summary>Appdefault</summary>

| File                    | Summary                                                                                                                                                                                                                                                                                                                                                                                                                             | Module                                                                                           |
|:------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|
| AppDefaultFragment.java | The code snippet provides an abstract class called "AppDefaultFragment" that extends the Fragment class and contains a method called "onCreateView" which inflates a layout resource, as well as a method called "layoutRes" that must be overridden in child classes to provide a reference to a layout resource file. This abstract class provides a template for creating fragments with consistent functionality across an app. | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AppDefault/AppDefaultFragment.java |
| AppDefaultActivity.java | The code defines an abstract class, AppDefaultActivity, that extends AppCompatActivity. It includes methods to set the content view layout, set up an initial fragment, and create an initial fragment. The class is meant to be extended by other activities that can customize the content view and fragment.                                                                                                                     | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AppDefault/AppDefaultActivity.java |

</details>

<details closed><summary>Main</summary>

| File                                  | Summary                                                                                                                                                                                                                                                                                                                                       | Module                                                                                                   |
|:--------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------|
| MainActivity.java                     | The code snippet provides the main activity for a minimal to-do application. It includes a toolbar with a menu containing options to navigate to the'About' and'Settings' screens. The activity also loads a fragment that displays the to-do list.                                                                                           | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/MainActivity.java                     |
| CustomRecyclerScrollViewListener.java | The provided code defines a custom RecyclerView scroll listener. It calculates the scroll distance and toggles the visibility of a view based on whether the user is scrolling up or down. The show() and hide() methods are abstract and must be implemented by the caller to specify what actions should be taken to show or hide the view. | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/CustomRecyclerScrollViewListener.java |
| MainFragment.java                     | Error generating file summary. Exception: Client error '400 Bad Request' for url 'https://api.openai.com/v1/chat/completions'                                                                                                                                                                                                                 | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/MainFragment.java                     |
|                                       | For more information check: https://httpstatuses.com/400                                                                                                                                                                                                                                                                                      |                                                                                                          |

</details>

<details closed><summary>Minimaltodo</summary>

| File                       | Summary                                                                                                                                                                                                                                                                                                                                                                                                                              | Module                                                                                          |
|:---------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------|
| TestStoreRetrieveData.java | This code snippet is a test suite written in Java for the StoreRetrieveData class, with the aim of testing its functionalities such as saving and retrieving ToDoItem objects to and from storage, checking the content and size of the stored data, and converting it to a JSON array. It also tests the precondition that the data storage is empty before any data is saved. The test suite is run within the MainActivity class. | app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/TestStoreRetrieveData.java |
| ApplicationTest.java       | The provided code snippet is a basic Android application test class that extends ApplicationTestCase and is used for testing the fundamental functionality of an Android application. It includes a constructor that calls the superclass constructor with an Application parameter. The test class doesn't include actual testing code and serves as a template to be used for testing specific application features.               | app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/ApplicationTest.java       |
| TestTodoItem.java          | This code includes a JUnit test class to verify the functionality of the ToDoItem class in the MinimalToDo Android app. It tests the object's three-parameter constructor, its ability to convert to and from JSON, and includes a helper function to set up the object. The code also includes a license agreement.                                                                                                                 | app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/TestTodoItem.java          |

</details>

<details closed><summary>Reminder</summary>

| File                  | Summary                                                                                                                                                                                                                                                                                                                           | Module                                                                                       |
|:----------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------|
| ReminderFragment.java | The provided code is a Java class that represents a ReminderFragment in an Android app. It retrieves data from local storage and populates views with the appropriate data. The fragment provides options to remove a reminder or snooze it for a certain amount of time. The class also handles saving data and closing the app. | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Reminder/ReminderFragment.java |
| ReminderActivity.java | The code snippet is an Android activity that extends another activity called AppDefaultActivity. Its purpose is to create a reminder fragment and display it using the layout resource file reminder_layout. This activity is designed to be a base class for showing reminders in an application.                                | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Reminder/ReminderActivity.java |

</details>

<details closed><summary>Root</summary>

| File            | Summary                                                                                                                                                                                                                                                                                                                                                                                                            | Module          |
|:----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------|
| build.gradle    | The provided code snippet is a basic Gradle build file for an Android project. It includes repository declarations, dependency configurations, and a plugin declaration for ButterKnife. The code is focused on setting up the necessary build tools and project dependencies.                                                                                                                                     | build.gradle    |
| gradlew.bat     | This code snippet is a Gradle startup script for Windows operating system that sets up the environment for running Gradle on Windows. It finds and sets the path to the Java executable and sets the classpath to the Gradle wrapper jar before executing the Gradle wrapper with the appropriate options and command-line arguments. It also handles error conditions and exits with the appropriate error codes. | gradlew.bat     |
| settings.gradle | The provided code snippet includes the app module in the project.                                                                                                                                                                                                                                                                                                                                                  | settings.gradle |

</details>

<details closed><summary>Settings</summary>

| File                  | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Module                                                                                       |
|:----------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------|
| SettingsFragment.java | This code provides functionality for the SettingsFragment, which extends PreferenceFragment and implements SharedPreferences.OnSharedPreferenceChangeListener. It loads the preferences layout, registers and unregisters a shared preference change listener for the activity, and listens for changes to the night mode preference. When the night mode preference is changed, it updates the saved theme and recreates the activity to apply the new theme. | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Settings/SettingsFragment.java |
| SettingsActivity.java | The code defines an activity for user settings in an Android app. It loads a theme based on the user's preference, sets up a toolbar with a back arrow, and displays a settings fragment within the activity. An analytics application is also implemented to track user activity.                                                                                                                                                                             | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Settings/SettingsActivity.java |

</details>

<details closed><summary>Utility</summary>

| File                           | Summary                                                                                                                                                                                                                                                                                                                                         | Module                                                                                               |
|:-------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------|
| TodoNotificationService.java   | The provided code snippet is an Android IntentService class for generating and displaying notifications for to-do tasks. It receives the to-do text and UUID via Intent, creates a notification, and uses a NotificationManager to display it. The notification can be clicked to launch the ReminderActivity, and deleted by swiping it away.  | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/TodoNotificationService.java   |
| ScrollingFABBehaviour.java     | This code provides a behavior for the FloatingActionButton that moves it up and down based on CoordinatorLayout dependencies such as Snackbar and Toolbar. When Snackbar is shown, the FAB moves up, and when the Toolbar is scrolled, the FAB moves down.                                                                                      | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ScrollingFABBehaviour.java     |
| ToDoItem.java                  | The code provides a ToDoItem class that contains the properties of a task, such as its text, description, reminder status, color, date, and identifier. It also allows for the serialization and deserialization of JSON objects to and from the class. Additionally, it includes getter and setter methods for each property.                  | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ToDoItem.java                  |
| CustomTextInputLayout.java     | The provided code snippet implements a custom TextInputLayout to allow for customization of the hint text on an EditText view. It includes methods to retrieve the current hint value, store the hint value locally, and update the hint value based on user input. Overall, the code aims to improve the user experience of the EditText view. | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/CustomTextInputLayout.java     |
| StoreRetrieveData.java         | This code snippet defines a class that facilitates storing and retrieving to-do list data using JSON files. It includes methods to convert ArrayLists of to-do items to JSONArrays and vice versa, save to JSON file, and load from JSON file. The class also handles exceptions when a file isn't found or when an I/O issue occurs.           | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/StoreRetrieveData.java         |
| Utils.java                     | The code snippet provides a utility function that returns the height of the toolbar of the activity's action bar. It retrieves the toolbar height by obtaining a styled attribute value for the action bar size, using the context of the activity. Finally, it recycles the TypedArray object to optimize system resources.                    | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/Utils.java                     |
| DeleteNotificationService.java | The provided code snippet is an Android IntentService that handles the deletion of a to-do item. It retrieves the to-do item ID from the intent, removes the corresponding item from the list of to-do items, and saves the updated list to a file. The service also updates a shared preference flag indicating that a change has occurred.    | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/DeleteNotificationService.java |
| ItemTouchHelperClass.java      | The code provides a class for implementing swipe and drag gestures on a RecyclerView using the ItemTouchHelper.Callback class. It includes methods for enabling/disabling long press drag and swipe, setting movement flags, handling movement and swipe actions, and a callback for when an item is moved or removed.                          | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ItemTouchHelperClass.java      |
| PreferenceKeys.java            | This code defines a class called PreferenceKeys that contains a public string variable called night_mode_pref_key. The constructor takes in a Resource object as parameter and uses it to initialize the night_mode_pref_key variable with the string value stored in the R.string.night_mode_pref_key resource ID.                             | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/PreferenceKeys.java            |
| RecyclerViewEmptySupport.java  | This code defines a custom RecyclerView class that enables the display of an empty view when there are no items to show. It listens to changes in the adapter's data and hides/shows the empty view accordingly. The user can set their preferred empty view by calling the setEmptyView method.                                                | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/RecyclerViewEmptySupport.java  |

</details>

---

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - [📌  PREREQUISITE-1]
> - [📌  PREREQUISITE-2]
> - ...

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
