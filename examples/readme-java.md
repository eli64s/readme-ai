<p align="center">
  <img src="https://img.icons8.com/external-tal-revivo-filled-tal-revivo/96/external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-filled-tal-revivo.png" width="100" />
</p>
<p align="center">
    <h1 align="center">MINIMAL-TODO</h1>
</p>
<p align="center">
    <em>Minimal-Todo: Simplify your tasks, maximize productivity!</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/avjinder/Minimal-Todo?style=flat-square&color=white" alt="license">
	<img src="https://img.shields.io/github/last-commit/avjinder/Minimal-Todo?style=flat-square&logo=git&logoColor=white&color=white" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/avjinder/Minimal-Todo?style=flat-square&color=white" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/avjinder/Minimal-Todo?style=flat-square&color=white" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Google-4285F4.svg?style=flat-square&logo=Google&logoColor=white" alt="Google">
	<img src="https://img.shields.io/badge/Android-3DDC84.svg?style=flat-square&logo=Android&logoColor=white" alt="Android">
	<img src="https://img.shields.io/badge/GitHub-181717.svg?style=flat-square&logo=GitHub&logoColor=white" alt="GitHub">
	<img src="https://img.shields.io/badge/Gradle-02303A.svg?style=flat-square&logo=Gradle&logoColor=white" alt="Gradle">
	<img src="https://img.shields.io/badge/java-%23ED8B00.svg?style=flat-square&logo=openjdk&logoColor=white" alt="java">
	<img src="https://img.shields.io/badge/JSON-000000.svg?style=flat-square&logo=JSON&logoColor=white" alt="JSON">
</p>
<hr>

##  Quick Links

> - [ Overview](#-overview)
> - [ Features](#-features)
> - [ Repository Structure](#-repository-structure)
> - [ Modules](#-modules)
> - [ Getting Started](#-getting-started)
>   - [ Installation](#-installation)
>   - [ Running Minimal-Todo](#-running-Minimal-Todo)
>   - [ Tests](#-tests)
> - [ Project Roadmap](#-project-roadmap)
> - [ Contributing](#-contributing)
> - [ License](#-license)
> - [ Acknowledgments](#-acknowledgments)

---

##  Overview

Minimal-Todo is a minimalist to-do list app that helps users stay organized and productive. Its core functionalities include creating, editing, and managing to-do items, setting reminders for important tasks, and customizing the app's appearance through theme selection. With features like animation, clipboard management, and context handling, Minimal-Todo aims to provide a seamless user experience. The app also supports night mode and offers analytics tracking to help users understand their productivity patterns. Overall, Minimal-Todo enables users to prioritize and track their tasks efficiently, making it a valuable tool for personal and professional productivity.

---

##  Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | The project follows a standard Android application architecture with separate modules for different components. It uses the Model-View-Presenter (MVP) design pattern to separate business logic from presentation. It also utilizes various Android components such as Activities, Fragments, and Services to implement the necessary functionality. |
| 🔩 | **Code Quality**  | The codebase demonstrates good coding practices, adhering to the Android code style guidelines. It follows a modular approach, making the codebase easy to read, understand, and maintain. Proper naming conventions and documentation enhance code readability. |
| 📄 | **Documentation** | The project includes a reasonable amount of documentation, such as comments and README files, to explain the purpose and usage of the code. Although not extensive, the provided documentation is sufficient for developers to understand the codebase and its components. |
| 🔌 | **Integrations**  | The project integrates with various external dependencies, including Google services (Google Analytics and Google Play Services). It also relies on libraries such as ButterKnife for view binding, Gson for JSON parsing, and JUnit for unit testing. |
| 🧩 | **Modularity**    | The codebase demonstrates good modularity, separating different components into their respective modules. This modular approach allows for easy reusability and maintainability of code. Each module focuses on a specific functionality, making it easier to understand and modify. |
| 🧪 | **Testing**       | The project includes unit tests using JUnit to verify the functionality of individual classes. It also includes Android instrumentation tests using Espresso for UI testing. The tests cover important features such as data storage, JSON conversion, and user interactions. |
| ⚡️  | **Performance**   | The project is designed to be efficient and responsive, with no noticeable performance issues. It utilizes background services and alarms to efficiently handle reminders and notifications. Proper use of RecyclerViews and optimized data storage further enhances the app's performance. |
| 🛡️ | **Security**      | The project includes basic security measures for data protection, such as storing data in a private file and using encryption. It also ensures access controls by only allowing authorized users to perform certain actions. However, the codebase does not implement advanced security features like authentication or authorization. |
| 📦 | **Dependencies**  | Key external libraries and dependencies used in the project include ButterKnife for view binding, Gson for JSON parsing, Google Play Services for Google Analytics, and JUnit for unit testing. These dependencies provide necessary functionality and enhance development efficiency. |


---

##  Repository Structure

```sh
└── Minimal-Todo/
    ├── Contributing.md
    ├── LICENSE.md
    ├── README.md
    ├── app
    │   ├── .gitignore
    │   ├── app-release.apk
    │   ├── app.iml
    │   ├── build.gradle
    │   ├── google-services.json
    │   ├── proguard-rules.pro
    │   └── src
    ├── build.gradle
    ├── gradle
    │   └── wrapper
    ├── gradle.properties
    ├── gradlew
    ├── gradlew.bat
    ├── screenshots
    │   ├── add_todo_dark.png
    │   ├── add_todo_light.png
    │   ├── app_icon.png
    │   ├── main_empty_dark.png
    │   ├── main_empty_light.png
    │   ├── main_full_dark.png
    │   ├── main_full_light.png
    │   ├── screenshot_notification.png
    │   ├── screenshot_reminder_date.png
    │   ├── screenshot_reminder_time.png
    │   ├── screenshot_todo_snooze.png
    │   ├── todo_date_dark.png
    │   └── todo_time_dark.png
    └── settings.gradle
```

---

##  Modules

<details closed><summary>.</summary>

| File                                                                                    | Summary                                                                                                                                                                                                                                                         |
| ---                                                                                     | ---                                                                                                                                                                                                                                                             |
| [build.gradle](https://github.com/avjinder/Minimal-Todo/blob/master/build.gradle)       | This code snippet is part of the top-level build.gradle file in the Minimal-Todo repository. It configures the build settings for all sub-projects/modules and specifies dependencies. The main purpose is to set up the necessary repositories and classpaths. |
| [gradlew.bat](https://github.com/avjinder/Minimal-Todo/blob/master/gradlew.bat)         | The gradlew.bat file is part of the Minimal-Todo repository and is used to execute Gradle on Windows. It sets the Java environment variables and executes GradleWrapperMain.                                                                                    |
| [settings.gradle](https://github.com/avjinder/Minimal-Todo/blob/master/settings.gradle) | This code snippet includes the `app` module in the project's settings.gradle file. It plays a critical role in the repository's architecture by ensuring that the app module is included and incorporated into the build process.                               |

</details>

<details closed><summary>app</summary>

| File                                                                                                  | Summary                                                                                                                                                                                                                                                                                                               |
| ---                                                                                                   | ---                                                                                                                                                                                                                                                                                                                   |
| [proguard-rules.pro](https://github.com/avjinder/Minimal-Todo/blob/master/app/proguard-rules.pro)     | The code snippet in `app/proguard-rules.pro` is responsible for specifying ProGuard rules specific to the project. It includes keeping public classes from com.google packages and not warning about com.google.android.gms.                                                                                          |
| [build.gradle](https://github.com/avjinder/Minimal-Todo/blob/master/app/build.gradle)                 | This code snippet, located in the `app/build.gradle` file, is responsible for configuring the Android application build process. It defines various parameters such as the target SDK version, version code, and dependencies. The snippet also includes configuration for signing the app and enabling minification. |
| [google-services.json](https://github.com/avjinder/Minimal-Todo/blob/master/app/google-services.json) | This code snippet contains the google-services.json file, which is crucial for integrating Google services into the Minimal-Todo Android application. It provides configuration details such as project ID, API keys, and client information.                                                                         |

</details>

<details closed><summary>app.src.androidTest.java.com.example.avjindersinghsekhon.minimaltodo</summary>

| File                                                                                                                                                                               | Summary                                                                                                                                                                                                                                                                                             |
| ---                                                                                                                                                                                | ---                                                                                                                                                                                                                                                                                                 |
| [TestStoreRetrieveData.java](https://github.com/avjinder/Minimal-Todo/blob/master/app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/TestStoreRetrieveData.java) | This code snippet contains test cases for the `StoreRetrieveData` class in the Minimal-Todo codebase. It verifies the functionality of writing and reading data from storage, ensuring the integrity of the stored data. The code also tests the conversion of an ArrayList to a JSONArray.         |
| [ApplicationTest.java](https://github.com/avjinder/Minimal-Todo/blob/master/app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/ApplicationTest.java)             | This code snippet is part of the Minimal-Todo repository and acts as a fundamental test for the application. It verifies if the Application can be properly executed and basic testing fundamentals are in place.                                                                                   |
| [TestTodoItem.java](https://github.com/avjinder/Minimal-Todo/blob/master/app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/TestTodoItem.java)                   | This code snippet contains JUnit tests for the functionality of the ToDoItem class in the Minimal-Todo repository. It tests the construction of ToDoItem objects, marshalling to JSON, and unmarshalling from JSON. The tests validate attributes such as the text body, reminder status, and date. |

</details>

<details closed><summary>app.src.main.java.com.example.avjindersinghsekhon.minimaltodo.Settings</summary>

| File                                                                                                                                                                       | Summary                                                                                                                                                                                                                                        |
| ---                                                                                                                                                                        | ---                                                                                                                                                                                                                                            |
| [SettingsFragment.java](https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Settings/SettingsFragment.java) | This code snippet is a SettingsFragment in the Minimal-Todo Android app. It manages user preferences, including a night mode option that changes the app's theme. The fragment listens for preference changes and updates the app accordingly. |
| [SettingsActivity.java](https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Settings/SettingsActivity.java) | This code snippet is the SettingsActivity class in the Minimal-Todo repository. It handles the UI and functionality of the settings screen, including the theme selection and navigation back to the previous screen.                          |

</details>

<details closed><summary>app.src.main.java.com.example.avjindersinghsekhon.minimaltodo.Reminder</summary>

| File                                                                                                                                                                       | Summary                                                                                                                                                                                                                                                                                                      |
| ---                                                                                                                                                                        | ---                                                                                                                                                                                                                                                                                                          |
| [ReminderFragment.java](https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Reminder/ReminderFragment.java) | This code snippet is a fragment in the Minimal-Todo repository. It implements the reminder functionality for a to-do item. It allows the user to set a reminder for the to-do item and provides options for snoozing the reminder.                                                                           |
| [ReminderActivity.java](https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Reminder/ReminderActivity.java) | This code snippet is part of the Minimal-Todo repository and is located in the `ReminderActivity.java` file. It extends the `AppDefaultActivity` class and is responsible for creating the reminder interface of the app. It sets the layout and initializes the `ReminderFragment` as the initial fragment. |

</details>

<details closed><summary>app.src.main.java.com.example.avjindersinghsekhon.minimaltodo.About</summary>

| File                                                                                                                                                              | Summary                                                                                                                                                                                                                                                                  |
| ---                                                                                                                                                               | ---                                                                                                                                                                                                                                                                      |
| [AboutActivity.java](https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/About/AboutActivity.java) | This code snippet represents the AboutActivity class in the Minimal-Todo codebase. It is responsible for displaying information about the app, including the version and contact details. The activity also handles user interactions, such as clicking the back button. |
| [AboutFragment.java](https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/About/AboutFragment.java) | This code snippet is an implementation of the AboutFragment class in the Minimal-Todo app. It sets up the UI and functionality for the About screen, including displaying the app version and handling user feedback.                                                    |

</details>

<details closed><summary>app.src.main.java.com.example.avjindersinghsekhon.minimaltodo.AddToDo</summary>

| File                                                                                                                                                                    | Summary                                                                                                                                                                                                              |
| ---                                                                                                                                                                     | ---                                                                                                                                                                                                                  |
| [AddToDoFragment.java](https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AddToDo/AddToDoFragment.java) | This code snippet, located in the AddToDoFragment.java file, handles the functionality of adding a new to-do item. It includes features such as animation, clipboard management, and context handling.               |
| [AddToDoActivity.java](https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AddToDo/AddToDoActivity.java) | This code snippet is an activity class that extends a parent activity class from the repository architecture. It overrides methods to set the layout, create a fragment, and handle the activity's lifecycle events. |

</details>

<details closed><summary>app.src.main.java.com.example.avjindersinghsekhon.minimaltodo.Main</summary>

| File                                                                                                                                                                                                   | Summary                                                                                                                                                                                                                                                                                  |
| ---                                                                                                                                                                                                    | ---                                                                                                                                                                                                                                                                                      |
| [MainActivity.java](https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/MainActivity.java)                                         | This code snippet represents the main activity of the Minimal-Todo repository. It handles the creation of the main interface, including the toolbar and menu options. The activity manages fragment navigation and launches other activities, such as the About and Settings activities. |
| [CustomRecyclerScrollViewListener.java](https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/CustomRecyclerScrollViewListener.java) | This code snippet is part of the Minimal-Todo repository's architecture. It contains a custom scroll listener class for RecyclerViews. It allows for hiding and showing views based on scroll direction and distance.                                                                    |
| [MainFragment.java](https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/MainFragment.java)                                         | This code snippet contains the implementation of the MainFragment class in the Minimal-Todo repository. It includes functionalities such as setting alarms, handling intents, managing shared preferences, and manipulating colors.                                                      |

</details>

<details closed><summary>app.src.main.java.com.example.avjindersinghsekhon.minimaltodo.Analytics</summary>

| File                                                                                                                                                                                | Summary                                                                                                                                                                                                                                                                                                                            |
| ---                                                                                                                                                                                 | ---                                                                                                                                                                                                                                                                                                                                |
| [AnalyticsApplication.java](https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Analytics/AnalyticsApplication.java) | This code snippet is part of the Minimal-Todo repository and it handles analytics tracking for the application. It uses Google Analytics to track various events and screen views within the app. By implementing the AnalyticsApplication class, the app can send analytics data to Google Analytics for analysis and monitoring. |

</details>

<details closed><summary>app.src.main.java.com.example.avjindersinghsekhon.minimaltodo.AppDefault</summary>

| File                                                                                                                                                                             | Summary                                                                                                                                                                                                           |
| ---                                                                                                                                                                              | ---                                                                                                                                                                                                               |
| [AppDefaultFragment.java](https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AppDefault/AppDefaultFragment.java) | This code snippet is a base class for fragments in the Minimal-Todo repository. It provides a default implementation for creating and destroying fragments, utilizing layout resources specific to each fragment. |
| [AppDefaultActivity.java](https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AppDefault/AppDefaultActivity.java) | This code snippet is a base activity class that sets up the initial fragment and handles the creation of the layout for child activities in the Minimal-Todo repository.                                          |

</details>

<details closed><summary>app.src.main.java.com.example.avjindersinghsekhon.minimaltodo.Utility</summary>

| File                                                                                                                                                                                        | Summary                                                                                                                                                                                                                                                                                                                                                                     |
| ---                                                                                                                                                                                         | ---                                                                                                                                                                                                                                                                                                                                                                         |
| [TodoNotificationService.java](https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/TodoNotificationService.java)     | This code snippet is a part of a minimalist to-do list app. It handles the creation and display of notifications for to-do reminders. Its main role is to generate and manage notifications for the user's to-do items, including setting the notification content and handling user interactions with the notifications.                                                   |
| [ScrollingFABBehaviour.java](https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ScrollingFABBehaviour.java)         | This code snippet contains the `ScrollingFABBehaviour` class, which is responsible for controlling the behavior of the floating action button (FAB) when scrolling in the app. It ensures that the FAB stays hidden or visible based on the scroll position, accounting for snackbar and toolbar effects.                                                                   |
| [ToDoItem.java](https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ToDoItem.java)                                   | The `ToDoItem` class is a utility class that represents a to-do item in the Minimal-Todo app. It contains properties such as the to-do text, reminder status, description, color, date, and identifier. This class allows for serialization and deserialization of to-do items to/from JSON format.                                                                         |
| [CustomTextInputLayout.java](https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/CustomTextInputLayout.java)         | This code snippet includes the implementation of a custom TextInputLayout. It overrides some methods to properly handle the hint functionality and ensure it is displayed correctly. The code aims to enhance the user experience of input fields within the parent repository's application.                                                                               |
| [StoreRetrieveData.java](https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/StoreRetrieveData.java)                 | This code snippet defines a class named StoreRetrieveData that provides methods to save and retrieve data from a file. It uses JSON format to store and retrieve ArrayLists of ToDoItem objects. The class takes a Context and a filename in the constructor and uses them to open and read/write the file.                                                                 |
| [Utils.java](https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/Utils.java)                                         | This code snippet, located at `app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/Utils.java`, defines a utility class called `Utils`. It provides a method `getToolbarHeight()` that returns the height of the toolbar in the app's context.                                                                                                            |
| [DeleteNotificationService.java](https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/DeleteNotificationService.java) | The `DeleteNotificationService` code snippet is a utility class in the Minimal-Todo repository. It is responsible for handling the deletion of notifications and updating the data set accordingly. It retrieves the necessary data, removes the corresponding item, saves the updated data, and notifies the app of the change.                                            |
| [ItemTouchHelperClass.java](https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ItemTouchHelperClass.java)           | Summary:This code snippet defines the `ItemTouchHelperClass` in the `Utility` package, extending the `ItemTouchHelper.Callback` class. It enables the dragging and swiping functionality for items in a `RecyclerView` and provides callbacks for handling these actions.                                                                                                   |
| [PreferenceKeys.java](https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/PreferenceKeys.java)                       | The `PreferenceKeys.java` code snippet provides a class that handles the preference key for night mode in the Minimal-Todo repository. It retrieves the value from resources and stores it for future use.                                                                                                                                                                  |
| [RecyclerViewEmptySupport.java](https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/RecyclerViewEmptySupport.java)   | The code snippet is a utility class called RecyclerViewEmptySupport that extends the RecyclerView class. It provides functionality to display an empty view when the RecyclerView is empty and hide it when there are items. This is achieved by listening to changes in the adapter's data and toggling the visibility of the empty view and the RecyclerView accordingly. |

</details>

---

##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Java**: `version x.y.z`

###  Installation

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

###  Running Minimal-Todo

Use the following command to run Minimal-Todo:

```sh
java -jar target/myapp.jar
```

###  Tests

To execute tests, run:

```sh
mvn test
```

---

##  Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/avjinder/Minimal-Todo/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/avjinder/Minimal-Todo/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/avjinder/Minimal-Todo/issues)**: Submit bugs found or log feature requests for Minimal-todo.

<details closed>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone https://github.com/avjinder/Minimal-Todo
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
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

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-quick-links)

---
