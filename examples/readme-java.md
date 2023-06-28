
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
Minimal-Todo
</h1>
<h3>◦ Maximize productivity, minimize clutter!</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/Gradle-02303A.svg?style&logo=Gradle&logoColor=white" alt="Gradle" />
<img src="https://img.shields.io/badge/java-%23ED8B00.svg?style&logo=openjdk&logoColor=white" alt="java" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style&logo=JSON&logoColor=white" alt="JSON" />
</p>

![GitHub top language](https://img.shields.io/github/languages/top/avjinder/Minimal-Todo?style&color=5D6D7E)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/avjinder/Minimal-Todo?style&color=5D6D7E)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/avjinder/Minimal-Todo?style&color=5D6D7E)
![GitHub license](https://img.shields.io/github/license/avjinder/Minimal-Todo?style&color=5D6D7E)
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

The Minimal-Todo project is an Android app that allows users to create and manage a list of to-do items. It provides features such as creating and editing reminders, setting custom colors for items, and storing data locally. The app focuses on simplicity and minimalism, offering a clean and intuitive user interface. Its value proposition lies in its ability to help users stay organized and conveniently manage their tasks on their mobile devices.

---

## ⚙️ Features

| Feature                | Description                                                                                                                                             |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **⚙️ Architecture**    | The system follows the Model-View-Presenter (MVP) architectural pattern. The MVP pattern separates the concerns and provides better maintainability and testability.                                       |
| **📖 Documentation**   | The codebase includes some documentation in the form of comments, but it could be improved in terms of clarity and coverage.                                |
| **🔗 Dependencies**    | The project relies on external libraries like ButterKnife for view binding and Google services for various functionalities.                                |
| **🧩 Modularity**      | The system is well organized into smaller components like activities, fragments, and utility classes. The modular structure facilitates reusability and maintainability.                                    |
| **✔️ Testing**         | The codebase includes test classes that cover various use cases, such as data storage and manipulation. The tests are written using the JUnit and Espresso frameworks, ensuring functional correctness. |
| **⚡️ Performance**     | The system performs well, with no significant performance issues reported. It uses efficient data structures and follows best practices for resource handling.                                              |
| **🔐 Security**        | The system uses secure data storage methods and does not expose sensitive information. However, further measures, such as encryption, could enhance security.                                                   |
| **🔀 Version Control** | The system is version controlled using Git, and the codebase is hosted on GitHub. It allows for collaborative development and easy tracking of changes and bug fixes.                                            |
| **🔌 Integrations**    | The system integrates with Google Analytics to track user actions. It also interacts with Android's built-in notification system and preferences for enhanced user experience.                        |
| **📶 Scalability**     | The system's modular design and efficient resource handling make it capable of handling growth. However, further optimizations may be required for larger datasets and increased user traffic.                          |

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

<details closed><summary>Root</summary>

| File                                                                                  | Summary                                                                                                                                                                                                                                   |
| ---                                                                                   | ---                                                                                                                                                                                                                                       |
| [build.gradle](https://github.com/avjinder/Minimal-Todo/blob/main/build.gradle)       | The code snippet configures the build settings for an Android project, including adding dependencies, repositories, and plugins. It utilizes Gradle to manage the build process and includes support for Google services and ButterKnife. |
| [gradlew.bat](https://github.com/avjinder/Minimal-Todo/blob/main/gradlew.bat)         | This code snippet is a Gradle startup script for Windows that sets up the environment, finds Java, and executes Gradle with the specified command line arguments.                                                                         |
| [settings.gradle](https://github.com/avjinder/Minimal-Todo/blob/main/settings.gradle) | The provided code snippet includes the':app' module, indicating that it includes the main application code for the project.                                                                                                               |

</details>

<details closed><summary>App</summary>

| File                                                                                | Summary                                                                                                                                                                                                                                                                                                     |
| ---                                                                                 | ---                                                                                                                                                                                                                                                                                                         |
| [build.gradle](https://github.com/avjinder/Minimal-Todo/blob/main/app/build.gradle) | This code snippet sets up an Android application. It defines the app's configuration, including the application ID, version info, and minimum/target SDK versions. It configures the release build type with minification and proguard. It also sets up dependencies for various libraries used in the app. |

</details>

<details closed><summary>Minimaltodo</summary>

| File                                                                                                                                                                             | Summary                                                                                                                                                                                                                                                                 |
| ---                                                                                                                                                                              | ---                                                                                                                                                                                                                                                                     |
| [TestStoreRetrieveData.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/TestStoreRetrieveData.java) | The code snippet is a set of test cases for the StoreRetrieveData class. It tests the functionality of writing and reading data to/from storage, as well as the conversion of ArrayList to JSONArray.                                                                   |
| [ApplicationTest.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/ApplicationTest.java)             | This code snippet is an Android application testing class that extends the ApplicationTestCase class. It is used for fundamental testing of the application's functions and components.                                                                                 |
| [TestTodoItem.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/TestTodoItem.java)                   | This code snippet is a test class that verifies the functionality of the ToDoItem class. It includes tests for constructing a ToDoItem, marshalling to JSON, and unmarshalling from JSON. The tests verify that the correct data is set and retrieved in each scenario. |

</details>

<details closed><summary>Settings</summary>

| File                                                                                                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                                                   |
| ---                                                                                                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                                                       |
| [SettingsFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Settings/SettingsFragment.java) | The code snippet defines a SettingsFragment class that extends PreferenceFragment. It creates preferences layout from preferences_layout.xml file and initializes some variables. It listens for changes in shared preferences and handles the night mode preference by updating the theme and recreating the activity. It also registers and unregisters the preference change listener. |
| [SettingsActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Settings/SettingsActivity.java) | This code snippet is for a SettingsActivity class in an Android app. It sets the theme based on user preferences, sets up the toolbar with a back arrow, and displays the SettingsFragment. It also handles the home button click to navigate up.                                                                                                                                         |

</details>

<details closed><summary>Reminder</summary>

| File                                                                                                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                    |
| ---                                                                                                                                                                      | ---                                                                                                                                                                                                                                                                                                                                        |
| [ReminderFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Reminder/ReminderFragment.java) | This code snippet is for a ReminderFragment in a to-do list app. It handles the creation, editing, and removal of reminders for individual to-do items. It also provides options for snoozing reminders and saving data. The code includes functionality for setting the theme, handling button clicks, and navigating between activities. |
| [ReminderActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Reminder/ReminderActivity.java) | The provided code snippet is a class for the ReminderActivity in an Android app. It extends AppDefaultActivity and implements methods for creating the layout and initial fragment for the activity. The layout is set to reminder_layout and the initial fragment is created from the ReminderFragment class.                             |

</details>

<details closed><summary>About</summary>

| File                                                                                                                                                            | Summary                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---                                                                                                                                                             | ---                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [AboutActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/About/AboutActivity.java) | The provided code snippet represents an Android activity class called "AboutActivity." It is responsible for displaying information about the application. The activity includes functionality for retrieving and displaying the app version, setting the toolbar with a back arrow, handling menu item selection events, and navigating back to the parent activity. It also includes theme handling based on user preferences. |
| [AboutFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/About/AboutFragment.java) | This code snippet represents an implementation of an About Fragment in an Android app. It sets up the UI elements, such as a toolbar and contact me button, and sets the app version. It also initializes analytics functionality and sends events when the contact me button is clicked.                                                                                                                                        |

</details>

<details closed><summary>Addtodo</summary>

| File                                                                                                                                                                  | Summary                                                                                                                                                                                                                    |
| ---                                                                                                                                                                   | ---                                                                                                                                                                                                                        |
| [AddToDoActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AddToDo/AddToDoActivity.java) | The code snippet is for an Android activity called AddToDoActivity. It extends a custom AppDefaultActivity and overrides methods for handling the activity's creation, content view layout, and initial fragment creation. |

</details>

<details closed><summary>Main</summary>

| File                                                                                                                                                                                                 | Summary                                                                                                                                                                                                                                                                                                                                                                                       |
| ---                                                                                                                                                                                                  | ---                                                                                                                                                                                                                                                                                                                                                                                           |
| [MainActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/MainActivity.java)                                         | The code snippet is for the MainActivity of a Minimal Todo app. It sets up the toolbar, inflates the layout, creates the initial fragment, and handles menu item clicks for about me and preferences.                                                                                                                                                                                         |
| [CustomRecyclerScrollViewListener.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/CustomRecyclerScrollViewListener.java) | This code snippet defines an abstract class called CustomRecyclerScrollViewListener that extends RecyclerView.OnScrollListener. It implements scroll behavior for RecyclerView, allowing the hiding and showing of elements based on scroll distance. The abstract methods show() and hide() need to be implemented by subclasses to define specific actions when showing or hiding elements. |

</details>

<details closed><summary>Analytics</summary>

| File                                                                                                                                                                              | Summary                                                                                                                                                                                                                                                                                                                                                  |
| ---                                                                                                                                                                               | ---                                                                                                                                                                                                                                                                                                                                                      |
| [AnalyticsApplication.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Analytics/AnalyticsApplication.java) | This code snippet defines an Application class that implements Google Analytics. It tracks user actions and sends analytics events to the server. The class provides methods to send screen views and events with optional parameters like category, action, and label. It also sets up the analytics tracker with the app name and exception reporting. |

</details>

<details closed><summary>Appdefault</summary>

| File                                                                                                                                                                           | Summary                                                                                                                                                                                                                                                                                                   |
| ---                                                                                                                                                                            | ---                                                                                                                                                                                                                                                                                                       |
| [AppDefaultFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AppDefault/AppDefaultFragment.java) | The code snippet is a base class called AppDefaultFragment that extends the Fragment class. It provides a common implementation for onCreateView() and onDestroy() methods. The abstract method layoutRes() is used to get the layout resource for the fragment.                                          |
| [AppDefaultActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AppDefault/AppDefaultActivity.java) | The provided code snippet is a template for creating an activity in an Android app. It extends the AppCompatActivity class and sets the content view layout for the activity. It also provides methods to set up the initial fragment and define the layout resource and initial fragment for subclasses. |

</details>

<details closed><summary>Utility</summary>

| File                                                                                                                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                   |
| ---                                                                                                                                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                                                       |
| [TodoNotificationService.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/TodoNotificationService.java)     | The provided code snippet represents a service that generates and displays a notification. It receives a to-do text and a unique identifier as input, creates a notification with the to-do text as its content, and sets up a pending intent for handling the notification interactions. The service also includes a delete intent for deleting the notification.                                        |
| [ScrollingFABBehaviour.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ScrollingFABBehaviour.java)         | The code snippet defines a custom behavior for a FloatingActionButton in a CoordinatorLayout. It allows the FAB to react to changes in its dependent views (Snackbar and Toolbar) by adjusting its translation based on their positions.                                                                                                                                                                  |
| [ToDoItem.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ToDoItem.java)                                   | The provided code snippet is a class called ToDoItem. It represents a todo item with properties such as todo text, reminder status, description, color, date, and unique identifier. It has methods to initialize, serialize and deserialize the todo item as a JSON object.                                                                                                                              |
| [CustomTextInputLayout.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/CustomTextInputLayout.java)         | The provided code snippet is for a custom TextInputLayout widget that extends the original TextInputLayout from the support library. It overrides some methods, such as addView() and onDraw(), in order to handle the setting and resetting of hint values for EditTexts and ensure that the hint is displayed correctly. Overall, it customizes the behavior of TextInputLayout for specific use cases. |
| [StoreRetrieveData.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/StoreRetrieveData.java)                 | The code snippet provides a class called StoreRetrieveData which supports storing and retrieving data from a file in JSON format. It can convert a list of ToDoItems into a JSONArray, save it to a file, and load it back into an ArrayList. The class uses Android's Context for file operations.                                                                                                       |
| [Utils.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/Utils.java)                                         | The provided code defines a utility class that contains a method to obtain the toolbar height from the application's context. It retrieves the toolbar height by accessing the "actionBarSize" attribute from the app's theme resources. The method returns the obtained toolbar height.                                                                                                                  |
| [DeleteNotificationService.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/DeleteNotificationService.java) | The provided code is a service that deletes a notification identified by a UUID from a list of ToDoItems. It loads the list from storage, identifies the item to be deleted, removes it from the list, saves the updated list, and notifies the application that the data has changed.                                                                                                                    |
| [ItemTouchHelperClass.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ItemTouchHelperClass.java)           | This code snippet defines a class called `ItemTouchHelperClass` that extends `ItemTouchHelper.Callback`. It provides functionality for dragging and swiping items in a `RecyclerView`. It implements methods for moving items, removing items, and configuring the drag and swipe behaviors.                                                                                                              |
| [PreferenceKeys.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/PreferenceKeys.java)                       | The code snippet defines a class that manages the preferences keys used in the app. The main functionality is to retrieve and store the resource key for the night mode preference.                                                                                                                                                                                                                       |
| [RecyclerViewEmptySupport.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/RecyclerViewEmptySupport.java)   | The provided code snippet is a class called RecyclerViewEmptySupport. It extends the RecyclerView class and adds the functionality to display an empty view when the RecyclerView is empty. The class includes methods to show the empty view, set the empty view, and handle changes in the adapter data to show or hide the empty view accordingly.                                                     |

</details>

---

## 🚀 Getting Started

### ✔️ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - `ℹ️ Requirement 1`
> - `ℹ️ Requirement 2`
> - `ℹ️ ...`

### 💻 Installation

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

### 🎮 Using Minimal-Todo

```sh
java -jar target/myapp.jar
```

### 🧪 Running Tests
```sh
mvn test
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
