<div id="top" align="left">
   <h1>
      <img src="https://img.icons8.com/external-tal-revivo-regular-tal-revivo/96/external-readme-is-a-easy-to-build-a-developer-hub-that-adapts-to-the-user-logo-regular-tal-revivo.png" width="100">
      <br>
      MINIMAL-TODO
   </h1>
   <h3>◦ Seamless code management for exceptional efficiency.</h3>
   <h3>◦ Developed with the software and tools below.</h3>

<p align="left">
      <img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat-square&logo=YAML&logoColor=white" alt="YAML">
<img src="https://img.shields.io/badge/Google-4285F4.svg?style=flat-square&logo=Google&logoColor=white" alt="Google">
<img src="https://img.shields.io/badge/Android-3DDC84.svg?style=flat-square&logo=Android&logoColor=white" alt="Android">
<img src="https://img.shields.io/badge/GitHub-181717.svg?style=flat-square&logo=GitHub&logoColor=white" alt="GitHub">
<img src="https://img.shields.io/badge/Gradle-02303A.svg?style=flat-square&logo=Gradle&logoColor=white" alt="Gradle">
<img src="https://img.shields.io/badge/java-%23ED8B00.svg?style=flat-square&logo=openjdk&logoColor=white" alt="java">
<img src="https://img.shields.io/badge/JSON-000000.svg?style=flat-square&logo=JSON&logoColor=white" alt="JSON">
   </p>
   <img src="https://img.shields.io/github/license/avjinder/Minimal-Todo?style=flat-square&color=5D6D7E" alt="github-license">
   <img src="https://img.shields.io/github/last-commit/avjinder/Minimal-Todo?style=flat-square&color=5D6D7E" alt="github-last-commit">
   <img src="https://img.shields.io/github/commit-activity/m/avjinder/Minimal-Todo?style=flat-square&color=5D6D7E" alt="github-commit-activity">
   <img src="https://img.shields.io/github/languages/top/avjinder/Minimal-Todo?style=flat-square&color=5D6D7E" alt="github-top-language">
</div>

---

## 🔗 Quick Links
- [🔗 Quick Links](#-quick-links)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [🧩 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
  - [⚙️ Installation](#️-installation)
  - [🤖 Running Minimal-Todo](#-running-minimal-todo)
  - [🧪 Tests](#-tests)
- [🚧 Project Roadmap](#-project-roadmap)
- [🤝 Contributing](#-contributing)
    - [*Contributing Guidelines*](#contributing-guidelines)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

The Minimal-Todo project is a powerful and user-friendly mobile application designed to help individuals stay organized by managing their to-do lists efficiently. With an intuitive user interface and streamlined features, it allows users to easily add, edit, and delete tasks, set reminders, and prioritize tasks based on importance. The app's value proposition lies in its simplicity, ensuring that users can stay on top of their tasks and achieve their goals effectively.

---

## 📦 Features

|    | Feature            | Description                                                                                                                                                          |
|----|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The repository follows a typical Android application architecture, with different components such as activities, fragments, services, and utility classes.     |
| 📄 | **Documentation**  | The codebase includes some documentation in the form of comments, but it could be more comprehensive and include more details about the functionality and usage.   |
| 🔗 | **Dependencies**   | The codebase relies on various external libraries, such as RecyclerView, Gson, Material Design components, Calligraphy, and Google Play services.                    |
| 🧩 | **Modularity**     | The system is organized into smaller components, such as activities, fragments, utilities, and tests, which follow the single responsibility principle.               |
| 🧪 | **Testing**        | The codebase includes unit tests and integration tests using JUnit and Espresso frameworks. It covers the functionality of key components and utility classes.       |
| ⚡️  | **Performance**    | The codebase does not explicitly address performance-related concerns. However, it uses common Android performance optimization techniques, such as ProGuard and minification. |
| 🔐 | **Security**       | The codebase does not have specific security measures implemented. However, general Android security best practices, such as secure data storage, can be followed.   |
| 🔀 | **Version Control**| The repository uses Git for version control, with commits, branches, and pull requests for managing changes.                                                       |
| 🔌 | **Integrations**   | The codebase integrates with various Android system services, such as AlarmManager and NotificationManager, as well as third-party libraries and Google Analytics. |
| 📶 | **Scalability**    | The codebase does not address scalability explicitly. However, it follows modular design principles, which can facilitate future enhancements and scalability.    |

---

## 📂 Repository Structure

```sh
└── Minimal-Todo/
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


## 🧩 Modules

<details closed><summary>.</summary>

| File                                                                                  | Summary                                                                                                                                                                                                                                                                                 |
| ---                                                                                   | ---                                                                                                                                                                                                                                                                                     |
| [build.gradle](https://github.com/avjinder/Minimal-Todo/blob/main/build.gradle)       | The code snippet defines the build configuration for the Minimal-Todo repository. It specifies software dependencies and repositories used for building the Android application, including Gradle and Google services.                                                                  |
| [gradlew.bat](https://github.com/avjinder/Minimal-Todo/blob/main/gradlew.bat)         | The code snippet is a Gradle startup script for Windows. It sets up the environment variables and executes Gradle tasks for the Minimal-Todo app. It plays a critical role in building and managing the app's dependencies and configuration.                                           |
| [settings.gradle](https://github.com/avjinder/Minimal-Todo/blob/main/settings.gradle) | The code snippet plays a critical role in the Minimal-Todo repository. It achieves its purpose by including the `:app` file, which is a key component of the project's architecture. The repository structure and dependencies information provides further context about the codebase. |
| [.travis.yml](https://github.com/avjinder/Minimal-Todo/blob/main/.travis.yml)         | The code snippet in the Minimal-Todo repository is responsible for building an Android app using Gradle. It sets up the necessary tools and dependencies, and executes the build script.                                                                                                |

</details>

<details closed><summary>app</summary>

| File                                                                                                | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---                                                                                                 | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [proguard-rules.pro](https://github.com/avjinder/Minimal-Todo/blob/main/app/proguard-rules.pro)     | The code snippet in the `proguard-rules.pro` file includes project-specific ProGuard rules, which are used for code obfuscation and optimization in the Android app. It keeps certain classes and methods from being removed or obfuscated, specifically those related to Google libraries (com.google).                                                                                                                                                         |
| [build.gradle](https://github.com/avjinder/Minimal-Todo/blob/main/app/build.gradle)                 | The code snippet is a part of the Minimal-Todo repository. It includes dependencies for Google Play Services Analytics, Calligraphy, Material Spinner, Material DateTimePicker, TextDrawable, RecyclerView, Design, AppCompat, and Support library v13. The code sets up the Android application with various configurations, applies plugins, defines key configurations for release builds, and sets the application ID, version, and min/target SDK versions. |
| [google-services.json](https://github.com/avjinder/Minimal-Todo/blob/main/app/google-services.json) | This code snippet within the Minimal-Todo repository manages Google services and dependencies for the Android app. It includes the `google-services.json` file and relevant configurations to enable analytics, cloud messaging, app invites, Google Sign-In, and ads services for the app.                                                                                                                                                                      |

</details>

<details closed><summary>app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo</summary>

| File                                                                                                                                                                             | Summary                                                                                                                                                                                                                                                                                                        |
| ---                                                                                                                                                                              | ---                                                                                                                                                                                                                                                                                                            |
| [TestStoreRetrieveData.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/TestStoreRetrieveData.java) | This code snippet contains test cases for the StoreRetrieveData class in the Minimal-Todo repository. It ensures that items can be stored and retrieved from the data storage correctly, and also tests the conversion of an ArrayList to a JSONArray.                                                         |
| [ApplicationTest.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/ApplicationTest.java)             | Summary: The code snippet is part of the Minimal-Todo repository, specifically in the `app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo` directory. It includes an ApplicationTest file that extends ApplicationTestCase and is used for testing Android applications.                     |
| [TestTodoItem.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/TestTodoItem.java)                   | This code snippet contains JUnit tests for the ToDoItem class in the Minimal-Todo repository. It verifies the functionality of constructing a ToDoItem object, marshalling and unmarshalling JSON data. The tests ensure correct behavior for text, reminder, date, and identifier properties of the ToDoItem. |

</details>

<details closed><summary>app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Settings</summary>

| File                                                                                                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                             |
| ---                                                                                                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                 |
| [SettingsFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Settings/SettingsFragment.java) | The `SettingsFragment.java` file in the `Minimal-Todo` repository is responsible for managing user preferences in the minimal to-do app. It allows users to change the night mode setting, which updates the theme of the app. The code utilizes shared preferences and registers listeners to handle preference changes and apply them to the app. |
| [SettingsActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Settings/SettingsActivity.java) | This code snippet contains the `SettingsActivity` class, which manages the settings screen in the Minimal-Todo app. It handles the creation of the activity, sets the theme based on user preferences, and provides navigation functionality for the back button in the toolbar.                                                                    |

</details>

<details closed><summary>app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Reminder</summary>

| File                                                                                                                                                                     | Summary                                                                                                                                                                                                                                                    |
| ---                                                                                                                                                                      | ---                                                                                                                                                                                                                                                        |
| [ReminderFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Reminder/ReminderFragment.java) | This code snippet represents the ReminderFragment within the Minimal-Todo repository. It implements a reminder feature with functionality to add, remove, and snooze to-do items. The code handles user interactions, theme preferences, and data storage. |
| [ReminderActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Reminder/ReminderActivity.java) | The code snippet in ReminderActivity.java is a key file in the Minimal-Todo repository. It extends AppDefaultActivity and is responsible for creating the layout and initializing the initial fragment for reminders.                                      |

</details>

<details closed><summary>app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/About</summary>

| File                                                                                                                                                            | Summary                                                                                                                                                                                                                                                              |
| ---                                                                                                                                                             | ---                                                                                                                                                                                                                                                                  |
| [AboutActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/About/AboutActivity.java) | The code snippet defines the AboutActivity class within the Minimal-Todo repository. It handles the creation and functionality of the About screen, including displaying the app version, setting the theme, and enabling navigation to the parent activity.         |
| [AboutFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/About/AboutFragment.java) | The code snippet is a part of the Minimal-Todo repository. It includes the AboutFragment file, which handles the creation and initialization of the About page in the app. The file sets up the UI elements and handles user interactions, such as sending feedback. |

</details>

<details closed><summary>app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AddToDo</summary>

| File                                                                                                                                                                  | Summary                                                                                                                                                                                                                                       |
| ---                                                                                                                                                                   | ---                                                                                                                                                                                                                                           |
| [AddToDoFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AddToDo/AddToDoFragment.java) | This code snippet, located in the app directory of the Minimal-Todo repository, is crucial in the parent repository's architecture. It accomplishes essential functionalities related to the app's build, configuration, and Android testing. |
| [AddToDoActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AddToDo/AddToDoActivity.java) | This code snippet is an activity class in the Minimal-Todo repository. It extends a default activity and sets the content view to the activity_add_to_do layout. It also creates an initial fragment and handles the onResume method.         |

</details>

<details closed><summary>app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main</summary>

| File                                                                                                                                                                                                 | Summary                                                                                                                                                                                                                                                                                                       |
| ---                                                                                                                                                                                                  | ---                                                                                                                                                                                                                                                                                                           |
| [MainActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/MainActivity.java)                                         | This code snippet, located in the `MainActivity.java` file, is a key part of the Minimal-Todo repository. It sets up the main activity for the app, including the toolbar and the navigation menu. It also handles menu item selection, allowing the user to navigate to different activities within the app. |
| [CustomRecyclerScrollViewListener.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/CustomRecyclerScrollViewListener.java) | This code snippet, `CustomRecyclerScrollViewListener`, is a key file in the `Minimal-Todo` repository. It implements a listener for scrolling events in a RecyclerView and provides methods to show or hide elements based on scroll distance.                                                                |
| [MainFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/MainFragment.java)                                         | This code snippet is part of a repository called Minimal-Todo. It contributes to the app's architecture and features related to building and releasing the application, handling dependencies, and defining the project's structure.                                                                          |

</details>

<details closed><summary>app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Analytics</summary>

| File                                                                                                                                                                              | Summary                                                                                                                                                                                                                                                                                                                   |
| ---                                                                                                                                                                               | ---                                                                                                                                                                                                                                                                                                                       |
| [AnalyticsApplication.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Analytics/AnalyticsApplication.java) | The `AnalyticsApplication.java` file in the `com.example.avjindersinghsekhon.minimaltodo.Analytics` package is responsible for handling analytics tracking in the Minimal-Todo app. It initializes a tracker, sets up analytics code, and provides methods for sending screen views and other events to Google Analytics. |

</details>

<details closed><summary>app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AppDefault</summary>

| File                                                                                                                                                                           | Summary                                                                                                                                                                                                                                                                   |
| ---                                                                                                                                                                            | ---                                                                                                                                                                                                                                                                       |
| [AppDefaultFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AppDefault/AppDefaultFragment.java) | This code snippet defines the base class for fragments in the Minimal Todo app. It provides a method to inflate the layout for the fragment and defines an abstract method for subclasses to specify the layout resource.                                                 |
| [AppDefaultActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AppDefault/AppDefaultActivity.java) | This code snippet is part of the Minimal-Todo repository. It provides an abstract base class for activities, handling the creation of the initial fragment and setting the content view layout. It ensures a consistent structure across different activities in the app. |

</details>

<details closed><summary>app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility</summary>

| File                                                                                                                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---                                                                                                                                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [TodoNotificationService.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/TodoNotificationService.java)     | The TodoNotificationService file in the Minimal-Todo repository is responsible for handling the creation and display of notifications related to a to-do item. It utilizes the Android Notification API to build and show notifications to the user. The service receives input from an intent and extracts the to-do text and UUID from it. It then creates a notification and sets up the necessary intents and actions. Finally, it uses the NotificationManager to display the notification to the user. |
| [ScrollingFABBehaviour.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ScrollingFABBehaviour.java)         | The code snippet is a custom behavior for a Floating Action Button (FAB) in a CoordinatorLayout. It allows the FAB to respond to the scroll position of Snackbar and Toolbar components, adjusting its position accordingly. The behavior is implemented using the CoordinatorLayout.Behavior class and its methods.                                                                                                                                                                                         |
| [ToDoItem.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ToDoItem.java)                                   | The `ToDoItem` class in the Minimal-Todo repository is a utility class that represents a single todo item. It encapsulates properties like the todo text, reminder status, description, color, and date. It provides methods for serialization/deserialization to JSON and includes unique identifiers for each item.                                                                                                                                                                                        |
| [CustomTextInputLayout.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/CustomTextInputLayout.java)         | The code snippet `CustomTextInputLayout.java` is a custom implementation of `TextInputLayout` that manages the hint of an `EditText` view. It ensures that the hint remains visible even if it changes programmatically. This code snippet enhances the functionality of the Minimal-Todo app, providing a more user-friendly input layout.                                                                                                                                                                  |
| [StoreRetrieveData.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/StoreRetrieveData.java)                 | This code snippet (`StoreRetrieveData.java`) in the Minimal-Todo repository is responsible for saving and loading `ToDoItem` data to and from a file on an Android device. It provides methods to convert `ToDoItem` objects to JSON, save the JSON to a file, and load the JSON from the file back into `ToDoItem` objects.                                                                                                                                                                                 |
| [Utils.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/Utils.java)                                         | The `Utils.java` file in the `com.example.avjindersinghsekhon.minimaltodo.Utility` package provides a method called `getToolbarHeight` that retrieves the toolbar height from the app's theme using the `context` parameter. The method uses the `TypedArray` class to obtain the styled attribute value for `actionBarSize` and returns it as the toolbar height. This code snippet contributes to the functionality of the main app by providing a utility method for obtaining the toolbar height.        |
| [DeleteNotificationService.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/DeleteNotificationService.java) | The code snippet represents the DeleteNotificationService class in the Minimal-Todo repository. It handles the deletion of ToDoItems in response to a notification. The class interacts with SharedPreferences and performs data storage and retrieval operations using StoreRetrieveData.                                                                                                                                                                                                                   |
| [ItemTouchHelperClass.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ItemTouchHelperClass.java)           | The `ItemTouchHelperClass` file in the `Utility` package of the Minimal-Todo repository is responsible for handling touch interactions with the RecyclerView in the app. It enables dragging and dropping items, as well as swipe-to-dismiss functionality.                                                                                                                                                                                                                                                  |
| [PreferenceKeys.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/PreferenceKeys.java)                       | The code snippet defines `PreferenceKeys` class that stores the key for the night mode preference. It is used to retrieve the night mode preference value from the resources file.                                                                                                                                                                                                                                                                                                                           |
| [RecyclerViewEmptySupport.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/RecyclerViewEmptySupport.java)   | The code snippet contains the `RecyclerViewEmptySupport` class, which extends the `RecyclerView` class. It provides a way to show an empty view when there is no data in the `RecyclerView`. The class includes methods to set and display the empty view.                                                                                                                                                                                                                                                   |

</details>

---

## 🚀 Getting Started

***Prerequisites***

Ensure you have the following dependencies installed on your system:

- `► INSERT-DEPENDENCY-1`
- `► INSERT-DEPENDENCY-2`
- `► ...`

### ⚙️ Installation

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


## 🚧 Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/avjinder/Minimal-Todo/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/avjinder/Minimal-Todo/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/avjinder/Minimal-Todo/issues)**: Submit bugs found or log feature requests for AVJINDER.

#### *Contributing Guidelines*

<details closed>
<summary>Click to expand</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone <your-forked-repo-url>
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear and concise message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

## 📄 License


This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 👏 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-quick-links)

---
