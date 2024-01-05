<p align="center">
  <img src="https://img.icons8.com/external-tal-revivo-filled-tal-revivo/96/external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-filled-tal-revivo.png" width="100" />
</p>
<p align="center">
    <h1 align="center">MINIMAL-TODO</h1>
</p>
<p align="center">
    <em>Simplify and conquer with Minimal-Todo!</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/avjinder/Minimal-Todo?style=flat-square&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/avjinder/Minimal-Todo?style=flat-square&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/avjinder/Minimal-Todo?style=flat-square&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/avjinder/Minimal-Todo?style=flat-square&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat-square&logo=YAML&logoColor=white" alt="YAML">
	<img src="https://img.shields.io/badge/Google-4285F4.svg?style=flat-square&logo=Google&logoColor=white" alt="Google">
	<img src="https://img.shields.io/badge/Android-3DDC84.svg?style=flat-square&logo=Android&logoColor=white" alt="Android">
	<img src="https://img.shields.io/badge/GitHub-181717.svg?style=flat-square&logo=GitHub&logoColor=white" alt="GitHub">
	<img src="https://img.shields.io/badge/Gradle-02303A.svg?style=flat-square&logo=Gradle&logoColor=white" alt="Gradle">
	<img src="https://img.shields.io/badge/JSON-000000.svg?style=flat-square&logo=JSON&logoColor=white" alt="JSON">
	<img src="https://img.shields.io/badge/java-%23ED8B00.svg?style=flat-square&logo=openjdk&logoColor=white" alt="java">
	<img src="https://img.shields.io/badge/Markdown-000000.svg?style=flat-square&logo=Markdown&logoColor=white" alt="Markdown">
</p>
<hr>

## 🔗 Quick Links
- [🔗 Quick Links](#-quick-links)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [🧩 Modules](#modules)
- [🚀 Getting Started](#-getting-started)
    - [⚙️ Installation](#-installation)
    - [🤖 Running Minimal-Todo](#-running-Minimal-Todo)
    - [🧪 Tests](#-tests)
- [🛠 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

Minimal-Todo is a lightweight Android application that allows users to manage their tasks efficiently. The project provides a user-friendly interface for creating, viewing, editing, and deleting tasks. Users can organize tasks by setting due dates and marking them as complete. The app also supports task prioritization and allows users to add detailed descriptions and labels to each task. With an intuitive design and simple functionality, Minimal-Todo aims to help users stay organized and increase productivity.

---

## 📦 Features

|    | Feature           | Description                                                                                                       |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**    | The codebase follows a typical Android app architecture using activities, fragments, and ViewModel for separation of concerns. It is not mentioned whether any specific design pattern was used.             |
| 📄 | **Documentation**  | The codebase lacks comprehensive documentation. Some important files like `proguard-rules.pro` and `google-services.json` are mentioned, but there is no specific mention of documentation quality. |
| 🔗 | **Dependencies**   | The codebase relies on libraries such as `com.android.tools.build:gradle`, `com.google.gms:google-services`, and `mavenCentral()`. The use of `google()` suggests usage of Google libraries. |
| 🧩 | **Modularity**     | The codebase is organized into smaller components such as activities, fragments, and ViewModel classes, which promote modularity and reusability to some extent. |
| 🧪 | **Testing**        | The codebase does not mention any specific testing strategies or tools, suggesting a lack of comprehensive testing.       |
| ⚡️ | **Performance**     | Without specific performance measurements, it is difficult to assess the system's performance. No specific optimizations or considerations are mentioned. |
| 🔐 | **Security**       | No specific security measures are mentioned in the codebase, suggesting a lack of specific security implementations. |
| 🔀 | **Version Control**| The codebase uses Git for version control, with a mention of ".travis.yml" suggesting the use of Travis CI for continuous integration. |
| 🔌 | **Integrations**   | The codebase does not mention any specific integrations with other systems or services. |
| 📶 | **Scalability**    | Without specific information, it is difficult to assess the system's scalability. The codebase structure does not explicitly mention any scalable architecture or strategies.           |

---

## 📂 Repository Structure

```sh
└── Minimal-Todo/
    ├── .travis.yml
    ├── app
    │   ├── app-release.apk
    │   ├── build.gradle
    │   ├── google-services.json
    │   ├── proguard-rules.pro
    │   └── src
    │       ├── androidTest
    │       └── main
    ├── build.gradle
    ├── gradle
    ├── gradlew.bat
    └── settings.gradle
```

---

## 🧩 Modules

<details closed><summary>.</summary>

| File                                                                                  | Summary                                                                                                                                                                                                                                                                                                             |
| ---                                                                                   | ---                                                                                                                                                                                                                                                                                                                 |
| [build.gradle](https://github.com/avjinder/Minimal-Todo/blob/main/build.gradle)       | This code snippet manages the build configuration of the parent repository. It includes dependencies and repositories for the sub-projects.                                                                                                                                                                         |
| [gradlew.bat](https://github.com/avjinder/Minimal-Todo/blob/main/gradlew.bat)         | This code snippet is a Gradle startup script for the Windows operating system. It sets up the necessary environment variables and executes the Gradle build tool for the parent repository.                                                                                                                         |
| [settings.gradle](https://github.com/avjinder/Minimal-Todo/blob/main/settings.gradle) | This code snippet serves as a crucial component in the parent repository's architecture. It achieves specific functionalities related to the app module. The codebase relies on certain dependencies and software, as mentioned in the settings.gradle file. Refer to the repository structure for further details. |
| [.travis.yml](https://github.com/avjinder/Minimal-Todo/blob/main/.travis.yml)         | The code snippet is a build script for an Android project. It sets up the required dependencies and builds the project using Gradle. It ensures that the project is built properly for the specified Android version and with the necessary tools.                                                                  |

</details>

<details closed><summary>app</summary>

| File                                                                                                | Summary                                                                                                                                                                                                                                                                                                                                               |
| ---                                                                                                 | ---                                                                                                                                                                                                                                                                                                                                                   |
| [proguard-rules.pro](https://github.com/avjinder/Minimal-Todo/blob/main/app/proguard-rules.pro)     | The code snippet in this repository contains ProGuard rules for an Android project. These rules specify which classes should be kept and which ones should be obfuscated during the build process. The main purpose of this code is to protect sensitive information and optimize the size of the final APK file.                                     |
| [build.gradle](https://github.com/avjinder/Minimal-Todo/blob/main/app/build.gradle)                 | This code snippet is a part of an Android application that uses various dependencies to implement features like analytics tracking, custom fonts, spinner menu, date/time picker, and material design components. It also configures the build settings and signing configuration for releasing the app.                                              |
| [google-services.json](https://github.com/avjinder/Minimal-Todo/blob/main/app/google-services.json) | This code snippet plays a critical role in the parent repository's architecture. It achieves important features related to project information, client information, and services, enabling analytics, messaging, sign-in, and ads functionalities. The codebase relies on the `google-services.json` file and follows a specific directory structure. |

</details>

<details closed><summary>app.src.androidTest.java.com.example.avjindersinghsekhon.minimaltodo</summary>

| File                                                                                                                                                                             | Summary                                                                                                                                                                                                                                                                                                                                                  |
| ---                                                                                                                                                                              | ---                                                                                                                                                                                                                                                                                                                                                      |
| [TestStoreRetrieveData.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/TestStoreRetrieveData.java) | This code snippet contains test cases for the `StoreRetrieveData` class in the MinimalToDo app. It tests the functionality to store and retrieve data from the app's storage. The tests check if the data is saved correctly and can be retrieved accurately. It also includes a test to ensure the conversion of data to a JSONArray works as intended. |
| [ApplicationTest.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/ApplicationTest.java)             | This code snippet is a test file (`ApplicationTest.java`) in the `com.example.avjindersinghsekhon.minimaltodo` package. It tests the application's fundamental functionality.                                                                                                                                                                            |
| [TestTodoItem.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/TestTodoItem.java)                   | The code snippet is a unit test for the ToDoItem class in the MinimalTodo application. It verifies the functionality of constructing a ToDoItem object, marshaling and unmarshaling it to JSON.                                                                                                                                                          |

</details>

<details closed><summary>app.src.main.java.com.example.avjindersinghsekhon.minimaltodo.Settings</summary>

| File                                                                                                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                                      |
| ---                                                                                                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                                          |
| [SettingsFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Settings/SettingsFragment.java) | The `SettingsFragment.java` file is a key component in the codebase. It handles user preferences and theme settings for the app. It listens for changes in preferences and updates the theme accordingly, utilizing the `SharedPreferences` and the `PreferenceKeys` class. The `SettingsFragment` communicates with the `MainFragment` and uses the `AnalyticsApplication`. |
| [SettingsActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Settings/SettingsActivity.java) | The code snippet is a key file in the Settings package of the repository. It handles the creation and behavior of the SettingsActivity, including setting the theme, displaying a toolbar, and navigating back to the parent activity.                                                                                                                                       |

</details>

<details closed><summary>app.src.main.java.com.example.avjindersinghsekhon.minimaltodo.Reminder</summary>

| File                                                                                                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                                    |
| ---                                                                                                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                                        |
| [ReminderFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Reminder/ReminderFragment.java) | The code snippet is a ReminderFragment class in the com.example.avjindersinghsekhon.minimaltodo.Reminder package. It handles the display and interaction of a reminder for a to-do item, allowing users to remove the reminder or snooze it for a specific duration. The class also saves the changes made to the reminder and closes the app after the changes are saved. |
| [ReminderActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Reminder/ReminderActivity.java) | The code snippet is a ReminderActivity class in the parent repository's architecture. It extends AppDefaultActivity and sets the layout for the activity. It also creates and returns an instance of the ReminderFragment.                                                                                                                                                 |

</details>

<details closed><summary>app.src.main.java.com.example.avjindersinghsekhon.minimaltodo.About</summary>

| File                                                                                                                                                            | Summary                                                                                                                                                                                                                                                  |
| ---                                                                                                                                                             | ---                                                                                                                                                                                                                                                      |
| [AboutActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/About/AboutActivity.java) | This code snippet represents the AboutActivity class in the parent repository. It is responsible for displaying information about the application, including the version, and handling the functionality of the toolbar in the About screen.             |
| [AboutFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/About/AboutFragment.java) | This code snippet is a part of the About feature in the codebase. It handles the creation and display of the About page, showing the app version and providing a contact option for user feedback. It also utilizes analytics for tracking user actions. |

</details>

<details closed><summary>app.src.main.java.com.example.avjindersinghsekhon.minimaltodo.AddToDo</summary>

| File                                                                                                                                                                  | Summary                                                                                                                                                                                                                                                                                                                                      |
| ---                                                                                                                                                                   | ---                                                                                                                                                                                                                                                                                                                                          |
| [AddToDoFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AddToDo/AddToDoFragment.java) | This code snippet is part of the parent repository's architecture and is located in the AddToDo package. It contains code for a fragment that allows users to add a new to-do item. The fragment includes various UI elements such as buttons, text fields, and switches, as well as functionality for handling user input and interactions. |
| [AddToDoActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AddToDo/AddToDoActivity.java) | This code snippet is the implementation of the AddToDoActivity class within the Minimal Todo app. It extends the AppDefaultActivity class and handles the creation of the activity, setting the content view, creating the initial fragment, and handling the onResume event.                                                                |

</details>

<details closed><summary>app.src.main.java.com.example.avjindersinghsekhon.minimaltodo.Main</summary>

| File                                                                                                                                                                                                 | Summary                                                                                                                                                                                                                                                                                                                     |
| ---                                                                                                                                                                                                  | ---                                                                                                                                                                                                                                                                                                                         |
| [MainActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/MainActivity.java)                                         | The code snippet is the `MainActivity` file in the `com.example.avjindersinghsekhon.minimaltodo.Main` package. It sets up the toolbar, handles menu items, and navigates to other activities.                                                                                                                               |
| [CustomRecyclerScrollViewListener.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/CustomRecyclerScrollViewListener.java) | Code snippet `CustomRecyclerScrollViewListener.java` is a part of the parent repository's architecture and provides functionality for hiding and showing elements in a RecyclerView based on the user's scroll behavior. It listens to scroll events and triggers the appropriate actions when the user scrolls up or down. |
| [MainFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/MainFragment.java)                                         | The code snippet is a key file in the `Main` package of the codebase. It manages the main screen of the app, including the layout, animation, and interaction logic with the user. The code also utilizes various dependencies and software.                                                                                |

</details>

<details closed><summary>app.src.main.java.com.example.avjindersinghsekhon.minimaltodo.Analytics</summary>

| File                                                                                                                                                                              | Summary                                                                                                                                                                                                                                                                                                                                             |
| ---                                                                                                                                                                               | ---                                                                                                                                                                                                                                                                                                                                                 |
| [AnalyticsApplication.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Analytics/AnalyticsApplication.java) | The `AnalyticsApplication` class in the codebase is responsible for managing the Google Analytics integration. It initializes the tracker and provides methods to send screen views and events to Google Analytics. The code retrieves the Analytics code from the `global_tracker` XML file and sets up the necessary configurations for tracking. |

</details>

<details closed><summary>app.src.main.java.com.example.avjindersinghsekhon.minimaltodo.AppDefault</summary>

| File                                                                                                                                                                           | Summary                                                                                                                                                                                                                 |
| ---                                                                                                                                                                            | ---                                                                                                                                                                                                                     |
| [AppDefaultFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AppDefault/AppDefaultFragment.java) | The code snippet is a base class for Fragments in the parent repository. It handles the inflation of the layout and provides a method to specify the layout resource.                                                   |
| [AppDefaultActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AppDefault/AppDefaultActivity.java) | This code snippet is an abstract activity class called AppDefaultActivity. It sets up the initial fragment and the content view layout for an Android app. It abstracts common functionality for activities in the app. |

</details>

<details closed><summary>app.src.main.java.com.example.avjindersinghsekhon.minimaltodo.Utility</summary>

| File                                                                                                                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                 |
| ---                                                                                                                                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                     |
| [TodoNotificationService.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/TodoNotificationService.java)     | This code snippet is a part of the parent repository's architecture and is responsible for handling and generating notifications for to-do tasks. It uses Android's NotificationManager and PendingIntent for creating and managing notifications.                                                                                                                      |
| [ScrollingFABBehaviour.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ScrollingFABBehaviour.java)         | This code snippet defines the behavior of a floating action button (FAB) in a scrolling view. It allows the FAB to move up and down based on the scroll position, and also handles the interaction with other UI elements like a snackbar or toolbar. The code is part of the parent repository's architecture for managing the FAB's behavior in a coordinated layout. |
| [ToDoItem.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ToDoItem.java)                                   | The `ToDoItem` class in the codebase is responsible for representing a to-do item with its properties such as title, description, reminder, color, date, and identifier. It offers methods to serialize the object to JSON and vice versa.                                                                                                                              |
| [CustomTextInputLayout.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/CustomTextInputLayout.java)         | The CustomTextInputLayout class in the com.example.avjindersinghsekhon.minimaltodo.Utility package extends the TextInputLayout class from the Android support library. It overrides the addView() and onDraw() methods to handle the hint behavior of EditText views within the layout.                                                                                 |
| [StoreRetrieveData.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/StoreRetrieveData.java)                 | This code snippet, located in `app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/StoreRetrieveData.java`, provides functionality for saving and loading data using JSON format. It handles file operations and performs serialization and deserialization of `ToDoItem` objects.                                                                    |
| [Utils.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/Utils.java)                                         | The code snippet in `Utils.java` provides a utility function `getToolbarHeight` that retrieves the height of the toolbar from the device's context. This is crucial for calculating layout dimensions in the parent repository's architecture.                                                                                                                          |
| [DeleteNotificationService.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/DeleteNotificationService.java) | This code snippet is a service that handles deleting a notification and updating the data set in the parent repository. It retrieves the necessary data, removes the specified item, saves the updated data, and notifies the parent repository of the data change.                                                                                                     |
| [ItemTouchHelperClass.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ItemTouchHelperClass.java)           | The ItemTouchHelperClass code snippet in the repository's Utility package defines the behavior for dragging and swiping items in a RecyclerView. It implements the ItemTouchHelper.Callback interface to handle movement and removal of items.                                                                                                                          |
| [PreferenceKeys.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/PreferenceKeys.java)                       | This code snippet defines the PreferenceKeys class, which holds a single field representing the key for a night mode preference setting. The key is obtained from a resources file.                                                                                                                                                                                     |
| [RecyclerViewEmptySupport.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/RecyclerViewEmptySupport.java)   | The `RecyclerViewEmptySupport` class is a key component in the repository. It manages the display of an empty view when a RecyclerView has no items. It extends the RecyclerView class and provides methods to set and show/hide the empty view.                                                                                                                        |

</details>

---

## 🚀 Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* Java: `► INSERT-VERSION-HERE`
* `► ...`
* `► ...`

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
Use the following command to run Minimal-Todo:
```sh
java -jar target/myapp.jar
```

### 🧪 Tests
To execute tests, run:
```sh
mvn test
```

---

## 🛠 Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/avjinder/Minimal-Todo/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/avjinder/Minimal-Todo/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/avjinder/Minimal-Todo/issues)**: Submit bugs found or log feature requests for Minimal-Todo.

<details closed>
<summary>Contributing Guidelines</summary>

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
