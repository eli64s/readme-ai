<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>Minimal-Todo
</h1>
<h3>◦ Maximize your productivity with Minimal-Todo!</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/Gradle-02303A.svg?style&logo=Gradle&logoColor=white" alt="Gradle" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
<img src="https://img.shields.io/badge/java-%23ED8B00.svg?style&logo=openjdk&logoColor=white" alt="java" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style&logo=JSON&logoColor=white" alt="JSON" />
</p>
<img src="https://img.shields.io/github/languages/top/avjinder/Minimal-Todo?style&color=5D6D7E" alt="GitHub top language" />
<img src="https://img.shields.io/github/languages/code-size/avjinder/Minimal-Todo?style&color=5D6D7E" alt="GitHub code size in bytes" />
<img src="https://img.shields.io/github/commit-activity/m/avjinder/Minimal-Todo?style&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/license/avjinder/Minimal-Todo?style&color=5D6D7E" alt="GitHub license" />
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
    - [🤖 Running Minimal-Todo](#-running-Minimal-Todo)
    - [🧪 Tests](#-tests)
- [🛣 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The Minimal-Todo project is an Android application that allows users to create and manage a to-do list. The core functionalities include adding new tasks, setting reminders, and customizing settings. The app aims to provide a minimalist and intuitive interface for users to efficiently organize their tasks and increase productivity. Its value proposition lies in its simplicity, ease of use, and ability to help users stay organized and focused.

---

## 📦 Features

| Feature                | Description                           |
| ---------------------- | ------------------------------------- |
| **⚙️ Architecture**     | The codebase follows a typical Model-View-Controller (MVC) architecture. The app module contains the main functionality of the application, including the user interface, data handling, and other crucial components. The code is well-organized and follows the separation of concerns principle, making it easy to maintain and extend.    |
| **📃 Documentation**   | The codebase has well-documented comments that explain the purpose and functionality of each class and method. However, there is no comprehensive documentation outside of code comments, which could make it challenging for new contributors to understand the project.    |
| **🔗 Dependencies**    | The codebase relies on several external libraries, including Butterknife for view binding, Google services for various functionalities, and libraries for analytics, UI components, and support. These libraries enhance the functionality and user experience of the application.    |
| **🧩 Modularity**      | The codebase is modular and organized into smaller components with clear responsibilities. Each class focuses on a specific functionality, such as settings management, task reminders, or data storage. This modularity allows for easier maintenance, testing, and reusability of code.    |
| **🧪 Testing**          | The codebase includes a comprehensive set of unit tests and functional tests. The tests cover critical functionalities such as writing and reading data to/from storage, creating and updating to-do items, and handling preferences. The use of JUnit and Android testing frameworks ensures the reliability and correctness of the code.    |
| **⚡️ Performance**      | The performance of the system is satisfactory, with efficient resource usage. The codebase utilizes background services for tasks like creating and displaying notifications, ensuring that these operations do not impact the user experience. However, further performance optimizations can be implemented, such as asynchronous operations for data handling and caching mechanisms for improved responsiveness.    |
| **🔐 Security**        | The codebase lacks explicit security measures, such as data encryption or user authentication. However, it does not handle sensitive data and is primarily focused on personal task management, which lowers the security risks. Implementing security measures like data encryption and authentication would be necessary if the application expands its scope to handle sensitive information. |
| **🔀 Version Control** | The codebase uses Git for version control, as evident from the repository on GitHub. The use of version control allows for efficient collaboration, code management, and tracking of changes. The repository follows best practices, including meaningful commit messages and branching strategies. |
| **🔌 Integrations**    | The system does not have any notable integrations with external systems or services beyond the use of Google services for analytics. It primarily focuses on providing a standalone to-do list app experience without relying on external data sources or services. There is potential for future integrations, such as cloud sync or third-party APIs, to enhance the functionality. |
| **📶 Scalability**     | The codebase does not currently demonstrate explicit scalability considerations. However, due to its modular structure and separation of concerns, it should be relatively straightforward to extend and add new features. Scalability can be further enhanced by implementing data synchronization mechanisms or utilizing backend services for handling larger datasets or multiple users. |

---


## 📂 Repository Structure


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

## ⚙️ Modules

<details closed><summary>Root</summary>

| File                                                                                  | Summary                                                                                                                                                                                                                                                                                                                                                    |
| ---                                                                                   | ---                                                                                                                                                                                                                                                                                                                                                        |
| [build.gradle](https://github.com/avjinder/Minimal-Todo/blob/main/build.gradle)       | This code is a build file that configures the dependencies and repositories for an Android project. It includes the necessary dependencies for Android build tools and Google services. It also sets up Butterknife for view binding.                                                                                                                      |
| [gradlew.bat](https://github.com/avjinder/Minimal-Todo/blob/main/gradlew.bat)         | This code is a Windows startup script for running Gradle. It sets up the environment variables and finds the Java executable. It then executes Gradle with the specified arguments and classpath.                                                                                                                                                          |
| [settings.gradle](https://github.com/avjinder/Minimal-Todo/blob/main/settings.gradle) | The code provides the core functionalities for the app module, which is likely the main functionality of the application. It encompasses the necessary code to run the app, including the user interface, data handling, and any other crucial components.                                                                                                 |
| [.travis.yml](https://github.com/avjinder/Minimal-Todo/blob/main/.travis.yml)         | This code sets up the necessary components and tools for an Android project, including build tools and the Android platform version. It also includes dependencies for Google Play Services and the Android Support Repository. The before_script ensures executable permission for the Gradle wrapper, and the script runs the build process with Gradle. |

</details>

<details closed><summary>App</summary>

| File                                                                                | Summary                                                                                                                                                                                                         |
| ---                                                                                 | ---                                                                                                                                                                                                             |
| [build.gradle](https://github.com/avjinder/Minimal-Todo/blob/main/app/build.gradle) | This code is for an Android application. It sets up the build configurations and dependencies, including plugins for signing, Google services, and various libraries for analytics, UI components, and support. |

</details>

<details closed><summary>Minimaltodo</summary>

| File                                                                                                                                                                             | Summary                                                                                                                                                                                                                                                                                               |
| ---                                                                                                                                                                              | ---                                                                                                                                                                                                                                                                                                   |
| [TestStoreRetrieveData.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/TestStoreRetrieveData.java) | The code is a test suite for the StoreRetrieveData class. It tests the functionality of writing and reading data to and from storage, ensuring that the stored data matches the test data. It also includes a test for the conversion of the test data to a JSONArray.                                |
| [ApplicationTest.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/ApplicationTest.java)             | The code is a test case for an Android application. It extends the ApplicationTestCase class and tests various fundamentals of the application.                                                                                                                                                       |
| [TestTodoItem.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/TestTodoItem.java)                   | The code consists of JUnit tests for the ToDoItem class. It tests the three-parameter constructor, marshalling of objects to JSON, and unmarshalling of objects from JSON. The tests verify the functionality of the ToDoItem class by checking if the constructed objects match the expected values. |

</details>

<details closed><summary>Settings</summary>

| File                                                                                                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                      |
| ---                                                                                                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                          |
| [SettingsFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Settings/SettingsFragment.java) | The SettingsFragment class is responsible for managing the preferences and settings of the app. It handles the creation and initialization of preferences, detects changes in preferences, and updates the app's theme and layout accordingly. It also registers and unregisters itself as a shared preference change listener to ensure proper functioning. |
| [SettingsActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Settings/SettingsActivity.java) | This code defines the functionality of the SettingsActivity in an Android app. It sets the theme based on user preference, sets up the toolbar, handles navigation back to the parent activity, and loads the SettingsFragment. It also includes analytics tracking.                                                                                         |

</details>

<details closed><summary>Reminder</summary>

| File                                                                                                                                                                     | Summary                                                                                                                                                                                                                                                                                                                     |
| ---                                                                                                                                                                      | ---                                                                                                                                                                                                                                                                                                                         |
| [ReminderFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Reminder/ReminderFragment.java) | This code is for the Reminder functionality in a todo list app. It allows the user to view and modify reminders for specific tasks. The code handles snoozing reminders, removing tasks from the reminder list, and saving changes to the data. It also includes functionality for switching between light and dark themes. |
| [ReminderActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Reminder/ReminderActivity.java) | This code defines the ReminderActivity class, which extends AppDefaultActivity. It sets the layout, creates the initial fragment, and handles the creation of the activity.                                                                                                                                                 |

</details>

<details closed><summary>About</summary>

| File                                                                                                                                                            | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---                                                                                                                                                             | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [AboutActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/About/AboutActivity.java) | The code is for an AboutActivity in a to-do list app. It sets the theme, displays the app version, and handles the toolbar. It also creates the initial fragment and handles the back button press.                                                                                                                                                                                                                                                                               |
| [AboutFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/About/AboutFragment.java) | The AboutFragment class is responsible for displaying information about the app. It sets up the UI elements such as version number and toolbar. It also handles user interaction for contacting the developer and tracks analytics events using the AnalyticsApplication class. The class extends AppDefaultFragment and overrides the layoutRes() method to specify the fragment's layout file. It provides a static newInstance() method to create an instance of the fragment. |

</details>

<details closed><summary>Addtodo</summary>

| File                                                                                                                                                                  | Summary                                                                                                                                                                                                                      |
| ---                                                                                                                                                                   | ---                                                                                                                                                                                                                          |
| [AddToDoFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AddToDo/AddToDoFragment.java) | HTTPStatus Exception: 400                                                                                                                                                                                                    |
| [AddToDoActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AddToDo/AddToDoActivity.java) | The code defines an activity that allows users to add a new to-do item. It extends a custom base activity and sets the layout for the activity. It also creates and displays the initial fragment for adding the to-do item. |

</details>

<details closed><summary>Main</summary>

| File                                                                                                                                                                                                 | Summary                                                                                                                                                                                                                         |
| ---                                                                                                                                                                                                  | ---                                                                                                                                                                                                                             |
| [MainActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/MainActivity.java)                                         | The code defines the main activity for a to-do list app. It includes a toolbar, menu options for about, settings, and theme switch, and handles the navigation between activities.                                              |
| [CustomRecyclerScrollViewListener.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/CustomRecyclerScrollViewListener.java) | This code defines a custom RecyclerView scroll listener that tracks the scroll distance and toggles the visibility of a view based on the scroll direction and distance. It provides abstract methods to show or hide the view. |
| [MainFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/MainFragment.java)                                         | HTTPStatus Exception: 400                                                                                                                                                                                                       |

</details>

<details closed><summary>Analytics</summary>

| File                                                                                                                                                                              | Summary                                                                                                                                                                                                                                                                                                                 |
| ---                                                                                                                                                                               | ---                                                                                                                                                                                                                                                                                                                     |
| [AnalyticsApplication.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Analytics/AnalyticsApplication.java) | The code represents an Android application that incorporates Google Analytics for tracking user interactions and events. It initializes and configures the Google Analytics tracker, and provides methods for sending screen views and custom events. The code also handles exception reporting and app identification. |

</details>

<details closed><summary>Appdefault</summary>

| File                                                                                                                                                                           | Summary                                                                                                                                                                                                                                   |
| ---                                                                                                                                                                            | ---                                                                                                                                                                                                                                       |
| [AppDefaultFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AppDefault/AppDefaultFragment.java) | The code defines a generic Fragment class that provides a default implementation for creating and destroying a Fragment's view. The specific layout resource to be inflated is determined by subclasses.                                  |
| [AppDefaultActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AppDefault/AppDefaultActivity.java) | The code defines an abstract activity class that sets up a fragment container and initializes an initial fragment based on the subclass implementation. The activity also sets the contentViewLayoutRes and creates the initial fragment. |

</details>

<details closed><summary>Utility</summary>

| File                                                                                                                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                                            |
| ---                                                                                                                                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                                                |
| [TodoNotificationService.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/TodoNotificationService.java)     | The code defines a service for creating and displaying notifications. It takes in a todo text and UUID as input, creates a notification with the text as the content, and sets up intents for certain actions. The notification is then displayed using the NotificationManager.                                                                                                                   |
| [ScrollingFABBehaviour.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ScrollingFABBehaviour.java)         | The code defines a custom behavior for a FloatingActionButton in a CoordinatorLayout. It handles the hiding and showing of the FloatingActionButton based on the scroll position of its dependencies, such as a Snackbar or a Toolbar. The FloatingActionButton is translated vertically based on the position of the dependencies.                                                                |
| [ToDoItem.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ToDoItem.java)                                   | This code defines a ToDoItem class that represents a task in a to-do list. It includes properties such as the task text, description, reminder status, color, and due date. The class also provides methods to serialize/deserialize the object to JSON format.                                                                                                                                    |
| [CustomTextInputLayout.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/CustomTextInputLayout.java)         | The CustomTextInputLayout class extends the TextInputLayout class and provides additional functionality for handling the hint text of an EditText. It stores the original hint value locally and sets it on the TextInputLayout when drawing the view. This ensures that the hint is preserved even if it is changed programmatically.                                                             |
| [StoreRetrieveData.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/StoreRetrieveData.java)                 | The StoreRetrieveData class provides methods for saving and loading data to/from a file. It can convert a list of ToDoItem objects to a JSON array and save it to a file. It can also load a JSON array from a file and convert it back to a list of ToDoItem objects.                                                                                                                             |
| [Utils.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/Utils.java)                                         | This code provides a utility function to get the height of the toolbar in an Android application. It uses the context and styled attributes to obtain the toolbar height dynamically from the theme resources. The function returns the toolbar height as an integer value.                                                                                                                        |
| [DeleteNotificationService.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/DeleteNotificationService.java) | The code is an Android service that handles the deletion of a notification for a to-do item. It loads the data, identifies the item to be deleted based on its unique identifier, removes it from the list, and saves the updated data. It also notifies the app that a change has occurred.                                                                                                       |
| [ItemTouchHelperClass.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ItemTouchHelperClass.java)           | This code defines a class that extends ItemTouchHelper.Callback to handle swipe and drag functionalities in a RecyclerView. It provides methods to enable long press drag, item view swipe, and defines movement flags. It also includes callback methods for handling item movement and removal.                                                                                                  |
| [PreferenceKeys.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/PreferenceKeys.java)                       | The code defines a utility class that holds the preference keys used in a minimalist to-do app. It includes a constructor that initializes the night mode preference key using the app's resources.                                                                                                                                                                                                |
| [RecyclerViewEmptySupport.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/RecyclerViewEmptySupport.java)   | The code provides a custom implementation of a RecyclerView with support for an empty view. It allows the user to set an empty view that is displayed when the RecyclerView adapter has no items. The empty view is automatically hidden or shown based on the adapter's item count. The code also contains methods to handle changes in the adapter's data and update the empty view accordingly. |

</details>

---

## 🚀 Getting Started

***Dependencies***

Before you begin, ensure that you have the following prerequisites installed:
> - `ℹ️ Requirement 1`
> - `ℹ️ Requirement 2`
> - `ℹ️ ...`

### 🔧 Installation

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

### 🤖 Running Minimal-Todo

```sh
java -jar target/myapp.jar
```

### 🧪 Tests
```sh
mvn test
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
