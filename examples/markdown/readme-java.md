<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>MINIMAL-TODO</h1>
<h3>◦ Streamline your tasks with Minimal-Todo!</h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat-square&logo=YAML&logoColor=white" alt="YAML" />
<img src="https://img.shields.io/badge/Gradle-02303A.svg?style=flat-square&logo=Gradle&logoColor=white" alt="Gradle" />
<img src="https://img.shields.io/badge/java-%23ED8B00.svg?style=flat-square&logo=openjdk&logoColor=white" alt="java" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style=flat-square&logo=JSON&logoColor=white" alt="JSON" />
</p>
<img src="https://img.shields.io/github/license/avjinder/Minimal-Todo?style=flat-square&color=5D6D7E" alt="GitHub license" />
<img src="https://img.shields.io/github/last-commit/avjinder/Minimal-Todo?style=flat-square&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/avjinder/Minimal-Todo?style=flat-square&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/languages/top/avjinder/Minimal-Todo?style=flat-square&color=5D6D7E" alt="GitHub top language" />
</div>

---

## 📖 Table of Contents
- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [⚙️ Modules](#️-modules)
- [🚀 Getting Started](#-getting-started)
  - [🔧 Installation](#-installation)
  - [🤖 Running Minimal-Todo](#-running-minimal-todo)
  - [🧪 Tests](#-tests)
- [🛣 Project Roadmap](#-project-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The repository "Minimal-Todo" is an Android application project that provides a minimalistic to-do list app. It includes features like adding, deleting, and managing to-do items, setting reminders, and customizing app settings. The project utilizes various Android libraries, such as ButterKnife, Google Services, and ProGuard, to enhance functionality and optimize code. The codebase includes files for activities, fragments, utility classes, unit tests, and build configurations. The repository can serve as a starting point for developers looking to create their own minimal to-do list app or learn about Android app development.

---

## 📦 Features

|    | Feature            | Description                                                                                                        |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The repository follows a basic architecture for an Android app, with separate app modules for the main code and test cases. The main code is organized into different packages for activities, fragments, adapters, and utilities. The app uses the Model-View-Controller (MVC) design pattern, with activities acting as controllers and fragments as views.|
| 📄 | **Documentation**  | The repository lacks comprehensive documentation. There is a basic readme file, but further documentation explaining the design choices or how to contribute is missing. Improving documentation would be beneficial for developers looking to understand and contribute to the project. |
| 🔗 | **Dependencies**   | The repository has dependencies on external libraries and services. Some notable dependencies include Google Play Services for analytics and Firebase for data storage. These dependencies enhance the app's functionality and provide integration with external services. |
| 🧩 | **Modularity**     | The repository is moderately modular, with the code organized into different packages and classes. However, there is some coupling between fragments and activities, which could be improved to increase modularity. Extracting common functionality into separate modules or using a more modular architecture would enhance code reusability and maintainability.|
| 🧪 | **Testing**        | The repository includes a set of Android instrumented tests and unit tests. The instrumented tests are placed in the androidTest directory, while the unit tests are in the main directory. The tests cover some key functionalities, including data storage and UI interactions. However, there is potential to improve test coverage and use more advanced testing frameworks for better automation and reliability.|
| ⚡️  | **Performance**    | The codebase does not specifically address performance optimization. However, since this is a relatively simple app without complex operations, the performance is generally satisfactory. Proper use of background threads and asynchronous tasks can further enhance the app's responsiveness.|
| 🔐 | **Security**       | The repository does not have specific security measures, such as encryption or authentication for user data. However, it does implement Firebase authentication for user login/signup, which provides basic security measures. To ensure stronger security, additional measures like secure storage and API security could be implemented. |
| 🔀 | **Version Control**| The repository uses Git for version control and is hosted on GitHub. It includes a .travis.yml file for continuous integration. The commit history and branch management indicate a good understanding of version control practices. |
| 🔌 | **Integrations**   | The app integrates with Google Play Services for analytics, Firebase for data storage, and Firebase Authentication for user login/signup. These integrations enhance the app's functionality and provide seamless experiences for users. There are no indications of integration with external APIs or services. |
| 📶 | **Scalability**    | The codebase does not address scalability explicitly. However, since this is a small-scale app, it can handle typical usage scenarios without major issues. If there is a need for significant scalability in terms of user base or concurrent usage, optimizations in data storage and server communication may be required. Additionally, improving modularity can help future scalability by allowing easier addition of new features and components. |

---


## 📂 Repository Structure

```sh
└── ./
    ├── .travis.yml
    ├── app/
    │   ├── app-release.apk
    │   ├── build.gradle
    │   ├── google-services.json
    │   ├── proguard-rules.pro
    │   └── src/
    │       ├── androidTest/
    │       └── main/
    ├── build.gradle
    ├── gradle/
    │   └── wrapper/
    ├── gradlew.bat
    ├── screenshots/
    └── settings.gradle

```

---


## ⚙️ Modules

<details closed><summary>Root</summary>

| File                                                                                  | Summary                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---                                                                                   | ---                                                                                                                                                                                                                                                                                                                                                                                                         |
| [build.gradle](https://github.com/avjinder/Minimal-Todo/blob/main/build.gradle)       | The code is a build script file (build.gradle) that configures the build process for an Android application project. It includes dependencies for the Android Gradle plugin, Google Services plugin, and the ButterKnife Gradle plugin. It also specifies the repositories where the project should look for dependencies. This script is used to build all sub-projects or modules within the application. |
| [gradlew.bat](https://github.com/avjinder/Minimal-Todo/blob/main/gradlew.bat)         | The code is a Gradle startup script for Windows that sets up and executes the Gradle build tool. It first checks for the presence of Java and sets the Java executable path. Then, it sets the classpath and other JVM options before invoking the GradleWrapperMain class to execute Gradle.                                                                                                               |
| [settings.gradle](https://github.com/avjinder/Minimal-Todo/blob/main/settings.gradle) | The code in the settings.gradle file includes the app module in the project. This means that the app module is a part of the overall project structure and will be built and included in the final output.                                                                                                                                                                                                  |
| [.travis.yml](https://github.com/avjinder/Minimal-Todo/blob/main/.travis.yml)         | The code is a configuration file named ".travis.yml" that is used in a continuous integration environment. It specifies the language as Android and sets up the required components for building the project. The before_script section gives execution permission to the gradlew script, and the script section triggers the build process using the gradlew build command.                                |

</details>

<details closed><summary>App</summary>

| File                                                                                                | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---                                                                                                 | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [proguard-rules.pro](https://github.com/avjinder/Minimal-Todo/blob/main/app/proguard-rules.pro)     | The code is a proguard-rules.pro file, which is used for specifying ProGuard rules in an Android project. ProGuard is a tool that helps optimize and obfuscate the code, making it smaller and harder to reverse-engineer. In this file, specific ProGuard rules are added to keep certain Google classes and interfaces, while ignoring any warnings related to Google's services.                                                                                                   |
| [build.gradle](https://github.com/avjinder/Minimal-Todo/blob/main/app/build.gradle)                 | The code is configuring the build settings for an Android application. It applies two plugins:'com.android.application' and'com.google.gms.google-services'. The android block sets the compile and build tools versions, and defines the default configuration for the app. The buildTypes block specifies that minification is enabled for release builds and adds the proguard rules. The dependencies block includes various libraries for analytics, UI components, and support. |
| [google-services.json](https://github.com/avjinder/Minimal-Todo/blob/main/app/google-services.json) | The code represents the content of the "google-services.json" file, which is typically included in Android apps. This file contains information about the project, clients, and services associated with using Google Play services in the app. It includes project ID, project number, and client-specific details such as client ID, package name, and services status (e.g., analytics, cloud messaging, app invite, Google sign-in, and ads).                                     |

</details>

<details closed><summary>Minimaltodo</summary>

| File                                                                                                                                                                             | Summary                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---                                                                                                                                                                              | ---                                                                                                                                                                                                                                                                                                                                                                                                          |
| [TestStoreRetrieveData.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/TestStoreRetrieveData.java) | The code above is a unit test for the StoreRetrieveData class in the MinimalTodo app. It tests the functionalities of writing and reading data to/from a data storage. The test cases ensure that items can be successfully stored and retrieved from the storage, with the content being the same as what was stored. It also tests the conversion of an ArrayList to a JSONArray.                          |
| [ApplicationTest.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/ApplicationTest.java)             | The code represents a simple Android testing class named "ApplicationTest" located in the "app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo" directory. It extends the "ApplicationTestCase" class and is used for testing the application's fundamental functionality.                                                                                                                  |
| [TestTodoItem.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/TestTodoItem.java)                   | The code above is a set of JUnit tests for the functionality of the ToDoItem class in the MinimalTodo application. The tests verify the correctness of various features of the ToDoItem class, including the three-parameter constructor, marshalling and unmarshalling of ToDoItem objects to JSON, and the validity of the JSON generated. The tests ensure that the ToDoItem class functions as expected. |

</details>

<details closed><summary>Settings</summary>

| File                                                                                                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---                                                                                                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [SettingsFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Settings/SettingsFragment.java) | The code is a settings fragment for an application. It allows the user to adjust preferences through a PreferenceFragment. Specifically, it listens for changes in the night mode preference and updates the theme of the app accordingly. It also registers listeners for preference changes when the fragment is resumed and unregisters them when it is paused.                                                                               |
| [SettingsActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Settings/SettingsActivity.java) | The code is for a SettingsActivity class that extends AppCompatActivity. It sets the theme of the activity based on a preference value, inflates the layout file activity_settings.xml, and initializes the toolbar. It also sets a custom back arrow icon with white color, handles navigation to the parent activity when the back arrow is clicked, and replaces the content of the activity with a SettingsFragment using a FragmentManager. |

</details>

<details closed><summary>Reminder</summary>

| File                                                                                                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---                                                                                                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [ReminderFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Reminder/ReminderFragment.java) | The code is for the ReminderFragment class, which is a fragment used in an Android app for managing reminders. The code handles the display and functionality of the reminder details, such as the text, snooze options, and removal of the reminder. It also includes methods for saving the data and closing the app. The code uses various Android libraries and classes to implement the desired functionality. |
| [ReminderActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Reminder/ReminderActivity.java) | The code is a Java file for the ReminderActivity class. It extends the AppDefaultActivity class and overrides its methods. The onCreate() method initializes the activity. The contentViewLayoutRes() method returns the layout resource for the activity. The createInitialFragment() method creates and returns an instance of the ReminderFragment class.                                                        |

</details>

<details closed><summary>About</summary>

| File                                                                                                                                                            | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---                                                                                                                                                             | ---                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [AboutActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/About/AboutActivity.java) | The code is an Android activity class that represents an About page in an app. It extends a base activity class. The activity sets a custom theme based on user preferences, retrieves the app version from package information, and initializes the toolbar. It also overrides methods for creating the initial fragment, handling menu item selections (e.g., the back button), and specifying the layout resource for the activity. |
| [AboutFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/About/AboutFragment.java) | The code is for an AboutFragment class that extends AppDefaultFragment. It creates a fragment that displays information about the app, including the app version and a toolbar. It also includes a contact button that sends feedback to the AnalyticsApplication. The code sets the layout for the fragment and provides a static method to create a new instance of the fragment.                                                    |

</details>

<details closed><summary>Addtodo</summary>

| File                                                                                                                                                                  | Summary                                                                                                                                                                                                                                                                                                                                                                            |
| ---                                                                                                                                                                   | ---                                                                                                                                                                                                                                                                                                                                                                                |
| [AddToDoFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AddToDo/AddToDoFragment.java) | The AddToDoFragment.java code is a class that handles the functionality for adding a new to-do item in a minimal to-do list app. It includes features such as input validation, setting due dates and reminders, copying to-do details to the clipboard, and sending the to-do item. The code also includes integration with other app components like app defaults and analytics. |
| [AddToDoActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AddToDo/AddToDoActivity.java) | The code is an implementation of an activity called AddToDoActivity, which is a subclass of AppDefaultActivity. This activity sets the content view to activity_add_to_do layout and creates an instance of the AddToDoFragment. It also overrides the onResume method for any necessary operations and is deprecated with the @SuppressWarnings("deprecation") annotation.        |

</details>

<details closed><summary>Main</summary>

| File                                                                                                                                                                                                 | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---                                                                                                                                                                                                  | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [MainActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/MainActivity.java)                                         | This code represents the main activity of an Android app called MinimalToDo. It initializes the toolbar and sets the content view layout. It also handles the creation of the initial fragment, inflation of the options menu, and the handling of menu item selection, specifically for the "About Me" and "Preferences" options that start different activities.                                                                                                                                     |
| [CustomRecyclerScrollViewListener.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/CustomRecyclerScrollViewListener.java) | This code defines a custom scroll listener for a RecyclerView in an Android application. It keeps track of the scroll distance and the visibility state of the view. When the scroll distance exceeds a predefined minimum value, the view is hidden. When the scroll distance is less than the negative of the minimum value, the view is shown. The scroll listener also includes abstract methods to handle showing and hiding the view, allowing for customization based on specific requirements. |
| [MainFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/MainFragment.java)                                         | The code is for the MainFragment class, which is part of an Android app for managing to-do items. It includes functionalities such as displaying a list of to-do items, adding new items, deleting items, and updating the list when changes are made. The code also handles alarm notifications for reminders and provides options for customization through settings.                                                                                                                                |

</details>

<details closed><summary>Analytics</summary>

| File                                                                                                                                                                              | Summary                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---                                                                                                                                                                               | ---                                                                                                                                                                                                                                                                                                                                                                                                             |
| [AnalyticsApplication.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Analytics/AnalyticsApplication.java) | The code is a part of an Android application that handles analytics. It uses the Google Analytics library to track user behavior and app usage. The class initializes a tracker and provides methods to send different types of analytics events, such as screen views and custom events. The code also handles setting up the app's name, enabling exception reporting, and retrieving the app's version name. |

</details>

<details closed><summary>Appdefault</summary>

| File                                                                                                                                                                           | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---                                                                                                                                                                            | ---                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [AppDefaultFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AppDefault/AppDefaultFragment.java) | The code is a Java class that extends the Fragment class from the Android support library. It provides a skeleton implementation for creating a Fragment with a default layout.The onCreateView method is overridden, which inflates a layout using the LayoutInflater and the layoutRes method. The onDestroy method is also overridden.                                                                                                       |
| [AppDefaultActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AppDefault/AppDefaultActivity.java) | The code is an abstract class called "AppDefaultActivity" that extends the "AppCompatActivity" class. It sets up the initial fragment for the activity and displays it on the screen. The class also defines two abstract methods that need to be implemented by subclasses: "contentViewLayoutRes()" which returns the layout resource ID for the activity, and "createInitialFragment()" which returns the initial fragment for the activity. |

</details>

<details closed><summary>Utility</summary>

| File                                                                                                                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---                                                                                                                                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [TodoNotificationService.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/TodoNotificationService.java)     | The code represents a TodoNotificationService, which is a background service that handles the creation and display of notifications for a to-do list app. It extends the IntentService class to handle intents in a separate thread. The service receives a to-do text and a unique identifier, creates a notification with the given text and icon, sets up action intents for deleting the notification or opening the app, and finally notifies the user with the created notification.                                                                                            |
| [ScrollingFABBehaviour.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ScrollingFABBehaviour.java)         | The code provided is a class called ScrollingFABBehaviour that extends the CoordinatorLayout.Behavior class. This class is responsible for handling the behavior of a FloatingActionButton when it is used in a CoordinatorLayout. Specifically, this behavior allows the FloatingActionButton to respond to certain dependencies, such as Snackbars and Toolbars, and change its position or translation accordingly. This class contains methods for identifying the dependencies and manipulating the FloatingActionButton's position based on the position of these dependencies. |
| [ToDoItem.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ToDoItem.java)                                   | The code above defines a class called "ToDoItem" that represents a to-do item in a to-do list app. The class contains properties such as the to-do text, reminder status, description, color, date, and identifier. It also includes methods for constructing a to-do item, converting it to a JSON object, and retrieving and setting its properties. The class is intended to be used in the context of a minimalist to-do list app.                                                                                                                                                |
| [CustomTextInputLayout.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/CustomTextInputLayout.java)         | The code provided is a custom implementation of the TextInputLayout class in Android. It overrides the addView and onDraw methods to customize the behavior and appearance of the TextInputLayout. The main purpose of this class is to handle the hint text of an EditText within the TextInputLayout and make sure it is displayed properly.                                                                                                                                                                                                                                        |
| [StoreRetrieveData.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/StoreRetrieveData.java)                 | The code provides the functionality to store and retrieve data in the Android application. It includes methods to convert a list of ToDoItems into a JSONArray and save it to a file, as well as load the data from the file and return the corresponding list of ToDoItems.                                                                                                                                                                                                                                                                                                          |
| [Utils.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/Utils.java)                                         | The code is a utility class that provides a method for obtaining the height of the toolbar. It takes a Context object as a parameter and returns the toolbar height as an integer. The method uses TypedArray to retrieve the toolbar height from the theme attributes defined in the app's resources.                                                                                                                                                                                                                                                                                |
| [DeleteNotificationService.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/DeleteNotificationService.java) | The code defines a `DeleteNotificationService` class that extends `IntentService`. It is responsible for handling the deletion of a specific notification from a to-do list app. The service receives an intent with a todoID, and it retrieves the list of to-do items, searches for the item matching the todoID, removes it from the list, and saves the updated data. The code also includes helper methods for data manipulation and storage.                                                                                                                                    |
| [ItemTouchHelperClass.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ItemTouchHelperClass.java)           | The code defines a class called ItemTouchHelperClass, which extends the ItemTouchHelper.Callback class. This class is responsible for handling touch events for items in a RecyclerView. It includes methods for determining whether long press drag and item swipe actions are enabled, creating movement flags for drag and swipe gestures, and handling drag and swipe events. The class also includes an interface called ItemTouchHelperAdapter, which defines methods for notifying when an item has been moved or removed.                                                     |
| [PreferenceKeys.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/PreferenceKeys.java)                       | The code represents a utility class that handles preference keys. It contains a single member variable,'night_mode_pref_key', which is initialized with the value of a string resource'R.string.night_mode_pref_key' using the provided'Resources' object. This utility class is intended to be used in an Android application for managing and retrieving preference keys related to night mode settings.                                                                                                                                                                            |
| [RecyclerViewEmptySupport.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/RecyclerViewEmptySupport.java)   | The code above defines a custom RecyclerView class called RecyclerViewEmptySupport. This class extends the default RecyclerView and adds functionality to display an empty view when the RecyclerView has no items. It achieves this by overriding various methods in the AdapterDataObserver class and checking the item count of the adapter. It also provides a method to set an empty view to be shown when the RecyclerView is empty.                                                                                                                                            |

</details>

---

## 🚀 Getting Started

***Dependencies***

Please ensure you have the following dependencies installed on your system:

`- ℹ️ Dependency 1`

`- ℹ️ Dependency 2`

`- ℹ️ ...`

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


## 🛣 Project Roadmap

> - [X] `ℹ️  Task 1: Implement X`
> - [ ] `ℹ️  Task 2: Implement Y`
> - [ ] `ℹ️ ...`


---

## 🤝 Contributing

[**Discussions**](https://github.com/avjinder/Minimal-Todo/discussions)
  - Join the discussion here.

[**New Issue**](https://github.com/avjinder/Minimal-Todo/issues)
  - Report a bug or request a feature here.

[**Contributing Guidelines**](https://github.com/avjinder/Minimal-Todo/blob/main/CONTRIBUTING.md)

- Contributions are welcome! Please follow these steps:

1. Fork the project repository to your GitHub account.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive such as `new-feature-x` or `bugfix-issue-x`.
```sh
git checkout -b new-feature-x
```
4. Develop your changes locally.
5. Commit your updates with a clear explanation of the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub.
```sh
git push origin new-feature-x
```
7. Create a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
8. Once your pull request is reviewed, it will be merged into the main branch of the project repository.

---

## 📄 License


This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 👏 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#Top)

---
