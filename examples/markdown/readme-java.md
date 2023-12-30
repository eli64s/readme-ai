<div align="left">
<h1><img src=https://img.icons8.com/external-tal-revivo-duo-tal-revivo/100/external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-duo-tal-revivo.png width="100" />
<br>MINIMAL-TODO</h1>
<h3>◦ Unleash the power of your code repository.</h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="left">
<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=plastic&logo=YAML&logoColor=white" alt="YAML" />
<img src="https://img.shields.io/badge/Google-4285F4.svg?style=plastic&logo=Google&logoColor=white" alt="Google" />
<img src="https://img.shields.io/badge/Android-3DDC84.svg?style=plastic&logo=Android&logoColor=white" alt="Android" />
<img src="https://img.shields.io/badge/GitHub-181717.svg?style=plastic&logo=GitHub&logoColor=white" alt="GitHub" />
<img src="https://img.shields.io/badge/Gradle-02303A.svg?style=plastic&logo=Gradle&logoColor=white" alt="Gradle" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style=plastic&logo=JSON&logoColor=white" alt="JSON" />
<img src="https://img.shields.io/badge/java-%23ED8B00.svg?style=plastic&logo=openjdk&logoColor=white" alt="java" />
</p>
<img src="https://img.shields.io/github/license/avjinder/Minimal-Todo?style=plastic&color=5D6D7E" alt="GitHub license" />
<img src="https://img.shields.io/github/last-commit/avjinder/Minimal-Todo?style=plastic&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/avjinder/Minimal-Todo?style=plastic&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/languages/top/avjinder/Minimal-Todo?style=plastic&color=5D6D7E" alt="GitHub top language" />
</div>
<hr>

##  Quick Links
- [🔗 Quick Links](#-quick-links)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [🧩 Modules](#modules)
- [🚀 Getting Started](#-getting-started)
    - [⚙️ Installation](#-installation)
    - [🤖 Running Minimal-Todo](#-running-Minimal-Todo)
    - [🧪 Tests](#-tests)
- [🚧 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---

##  Overview

The code repository `Minimal-Todo` is an Android application that serves as a minimalistic to-do list. It provides the functionality to create, edit, and delete tasks, set reminders for tasks, and manage user preferences. The repository includes various classes and components such as activities, fragments, services, utilities, and test cases. It utilizes dependencies and libraries like Google Analytics, Calligraphy, MaterialDateTimePicker, and support packages. With an organized directory structure and well-maintained build configuration, the repository offers a reliable and scalable solution for managing to-do tasks efficiently.

---

##  Features

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

##  Repository Structure

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


##  Modules

<details closed><summary>.</summary>

| File                                                                                  | Summary                                                                                                                                                                                                                                                  |
| ---                                                                                   | ---                                                                                                                                                                                                                                                      |
| [build.gradle](https://github.com/avjinder/Minimal-Todo/blob/main/build.gradle)       | The code snippet in the build.gradle file is responsible for managing the dependencies and repositories used by the parent project and its sub-projects/modules. It includes the configuration options and dependencies needed for building the project. |
| [gradlew.bat](https://github.com/avjinder/Minimal-Todo/blob/main/gradlew.bat)         | The code snippet is a script that initializes and runs the Gradle build system for a Windows environment in the parent repository.                                                                                                                       |
| [settings.gradle](https://github.com/avjinder/Minimal-Todo/blob/main/settings.gradle) | The code snippet in the settings.gradle file includes the app module in the repository's build configuration.                                                                                                                                            |
| [.travis.yml](https://github.com/avjinder/Minimal-Todo/blob/main/.travis.yml)         | The code snippet, located in the `.travis.yml` file, sets up the Android environment, specifies required components and runs the `gradlew build` command to build the project.                                                                           |

</details>

<details closed><summary>app</summary>

| File                                                                                                | Summary                                                                                                                                                                                                                                                                                                                                                               |
| ---                                                                                                 | ---                                                                                                                                                                                                                                                                                                                                                                   |
| [proguard-rules.pro](https://github.com/avjinder/Minimal-Todo/blob/main/app/proguard-rules.pro)     | The code snippet in the file app/proguard-rules.pro includes project-specific ProGuard rules for an Android application. It specifies the flags, includes, and keeps certain classes needed for the project, particularly those related to Google services and WebView. It also instructs ProGuard to not warn about certain classes related to Google Play services. |
| [build.gradle](https://github.com/avjinder/Minimal-Todo/blob/main/app/build.gradle)                 | The code in the file `app/build.gradle` specifies the configuration and dependencies for an Android application. It sets the application ID, version, and target SDK, enables minification and proguard, and includes various libraries and support packages.                                                                                                         |
| [google-services.json](https://github.com/avjinder/Minimal-Todo/blob/main/app/google-services.json) | The code snippet at app/google-services.json stores client information, project details, and service statuses for an Android app.                                                                                                                                                                                                                                     |

</details>

<details closed><summary>app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo</summary>

| File                                                                                                                                                                             | Summary                                                                                                                                                                                                                           |
| ---                                                                                                                                                                              | ---                                                                                                                                                                                                                               |
| [TestStoreRetrieveData.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/TestStoreRetrieveData.java) | The code snippet contains test cases for the StoreRetrieveData class. It tests the functionality of writing and reading data to/from storage, as well as converting an ArrayList to a JSONArray.                                  |
| [ApplicationTest.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/ApplicationTest.java)             | The code snippet is a test case for the application class in the Minimal-Todo Android app. It tests the fundamentals of the application's functionality.                                                                          |
| [TestTodoItem.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/TestTodoItem.java)                   | This code snippet contains JUnit tests to verify the functionality of the ToDoItem class. It tests the three-parameter constructor, marshalling ToDoItem objects to JSON, and unmarshalling from JSON to create ToDoItem objects. |

</details>

<details closed><summary>app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Settings</summary>

| File                                                                                                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---                                                                                                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [SettingsFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Settings/SettingsFragment.java) | This code snippet defines the SettingsFragment class which is responsible for displaying and handling user preferences in the Minimal-Todo repository. It includes methods for creating the preference view, handling preference changes, and managing the lifecycle of the fragment.                                                                                                                                           |
| [SettingsActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Settings/SettingsActivity.java) | The code snippet is a Java file located at app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Settings/SettingsActivity.java. It is responsible for managing the settings activity within the Minimal-Todo repository. The activity includes functionalities such as sending analytics, setting the theme, displaying a toolbar with an option to navigate back, and replacing the content with a settings fragment. |

</details>

<details closed><summary>app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Reminder</summary>

| File                                                                                                                                                                     | Summary                                                                                                                                                             |
| ---                                                                                                                                                                      | ---                                                                                                                                                                 |
| [ReminderFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Reminder/ReminderFragment.java) | This code snippet is a part of the Reminder feature in the Minimal-Todo repository. It handles the creation and management of reminders for to-do items in the app. |
| [ReminderActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Reminder/ReminderActivity.java) | The code snippet is a reminder activity that extends a default activity. It sets the content layout and initializes a reminder fragment.                            |

</details>

<details closed><summary>app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/About</summary>

| File                                                                                                                                                            | Summary                                                                                                                                                                                                                           |
| ---                                                                                                                                                             | ---                                                                                                                                                                                                                               |
| [AboutActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/About/AboutActivity.java) | This code snippet is an Activity class that handles the About section of an Android app. It sets up the UI components, handles the toolbar, and provides navigation functionality.                                                |
| [AboutFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/About/AboutFragment.java) | The AboutFragment.java file in the app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/About/ directory is responsible for displaying information about the app's version and providing a way to contact the developer. |

</details>

<details closed><summary>app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AddToDo</summary>

| File                                                                                                                                                                  | Summary                                                                                                                                                                                                                                                   |
| ---                                                                                                                                                                   | ---                                                                                                                                                                                                                                                       |
| [AddToDoFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AddToDo/AddToDoFragment.java) | This code snippet is a part of the Minimal-Todo repository and is located at app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AddToDo/AddToDoFragment.java. It is responsible for adding a new task in the Minimal Todo app.                 |
| [AddToDoActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AddToDo/AddToDoActivity.java) | The code snippet represents the AddToDoActivity class in the Minimal-Todo repository. It extends the AppDefaultActivity class and includes methods for creating the initial fragment and setting the content view. It also overrides the onResume method. |

</details>

<details closed><summary>app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main</summary>

| File                                                                                                                                                                                                 | Summary                                                                                                                                                                                                                                                                               |
| ---                                                                                                                                                                                                  | ---                                                                                                                                                                                                                                                                                   |
| [MainActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/MainActivity.java)                                         | The code snippet represents the main activity of the Minimal-Todo Android app. It includes methods for creating the activity, inflating the menu, and handling menu item selection, which navigate to different activities.                                                           |
| [CustomRecyclerScrollViewListener.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/CustomRecyclerScrollViewListener.java) | This code snippet defines a custom scroll listener for a RecyclerView in an Android app. It keeps track of the scroll distance and determines whether to show or hide a view based on the scroll direction and distance.                                                              |
| [MainFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/MainFragment.java)                                         | The code snippet is located at `app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/MainFragment.java` within the repository structure. It imports the `AlarmManager` class and performs certain functionalities related to the main fragment of the Minimal Todo app. |

</details>

<details closed><summary>app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Analytics</summary>

| File                                                                                                                                                                              | Summary                                                                                                                                                                                                                     |
| ---                                                                                                                                                                               | ---                                                                                                                                                                                                                         |
| [AnalyticsApplication.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Analytics/AnalyticsApplication.java) | The code snippet is responsible for implementing analytics tracking in the Minimal-Todo Android application. It sets up and sends various types of analytics data, such as screen views and events, using Google Analytics. |

</details>

<details closed><summary>app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AppDefault</summary>

| File                                                                                                                                                                           | Summary                                                                                                                                                                                                                                                                                |
| ---                                                                                                                                                                            | ---                                                                                                                                                                                                                                                                                    |
| [AppDefaultFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AppDefault/AppDefaultFragment.java) | This code snippet defines the abstract class `AppDefaultFragment` which creates a fragment with a specified layout. It inflates the layout in the `onCreateView` method and returns the view. The layoutRes method should be implemented by subclasses to provide the layout resource. |
| [AppDefaultActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AppDefault/AppDefaultActivity.java) | This code defines the abstract class `AppDefaultActivity` which sets up the initial fragment and content view layout for child activities.                                                                                                                                             |

</details>

<details closed><summary>app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility</summary>

| File                                                                                                                                                                                      | Summary                                                                                                                                                                                                                                                                                                       |
| ---                                                                                                                                                                                       | ---                                                                                                                                                                                                                                                                                                           |
| [TodoNotificationService.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/TodoNotificationService.java)     | This code snippet defines a service that handles the creation of notifications for a to-do list app. It retrieves the to-do text and unique ID from an intent, creates a notification with the text, sets an activity to open when the notification is clicked, and handles the deletion of the notification. |
| [ScrollingFABBehaviour.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ScrollingFABBehaviour.java)         | This code snippet defines a behavior for a FloatingActionButton, which moves up and down based on scroll events in a CoordinatorLayout. The FloatingActionButton moves up when a Snackbar appears and moves down when a Toolbar is scrolled up.                                                               |
| [ToDoItem.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ToDoItem.java)                                   | The code snippet defines the `ToDoItem` class which represents a task in the Minimal-Todo repository. It includes properties like task text, description, reminder status, color, date, and identifier. It also provides methods to convert the task to JSON format and vice versa.                           |
| [CustomTextInputLayout.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/CustomTextInputLayout.java)         | This code snippet defines a custom implementation of the TextInputLayout class from the Android Support Library. It overrides methods for adding child views and drawing on the canvas. The main purpose is to manage the hint text of an EditText and ensure it is displayed correctly.                      |
| [StoreRetrieveData.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/StoreRetrieveData.java)                 | The code snippet provides functionality for storing and retrieving data for a to-do list application. It includes methods for converting the data to JSON format, saving it to a file, and loading the data from the file.                                                                                    |
| [Utils.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/Utils.java)                                         | The code snippet provides a utility function that retrieves the height of the toolbar from the app's resources. The function takes in a context and returns the toolbar height as an integer.                                                                                                                 |
| [DeleteNotificationService.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/DeleteNotificationService.java) | This code snippet contains the implementation of a service called DeleteNotificationService. It handles the deletion of a ToDoItem from a list and updates the data accordingly.                                                                                                                              |
| [ItemTouchHelperClass.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ItemTouchHelperClass.java)           | This code snippet defines a class called ItemTouchHelperClass, which extends ItemTouchHelper.Callback. It allows the user to drag and swipe items in a RecyclerView. It also provides callbacks for moving and removing items.                                                                                |
| [PreferenceKeys.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/PreferenceKeys.java)                       | This code snippet defines a class called PreferenceKeys. It takes in a Resources object and initializes a final String variable called night_mode_pref_key with a value from the resources file.                                                                                                              |
| [RecyclerViewEmptySupport.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/RecyclerViewEmptySupport.java)   | The code snippet defines a custom RecyclerView class called RecyclerViewEmptySupport. It provides functionality to display an empty view if the RecyclerView has no data items. The empty view is shown/hidden based on the adapter's item count.                                                             |

</details>

---

##  Getting Started

***Prerequisites***

Ensure you have the following dependencies installed on your system:

- `► INSERT-DEPENDENCY-1`
- `► INSERT-DEPENDENCY-2`
- `► INSERT-DEPENDENCY-3`

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

```sh
java -jar target/myapp.jar
```

###  Tests
```sh
mvn test
```

---


##  Project Roadmap

> - [X] `ℹ️  Task 1: Implement X`
> - [ ] `ℹ️  Task 2: Implement Y`
> - [ ] `ℹ️ ...`


---

##  Contributing

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

##  License


This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#Top)

---
