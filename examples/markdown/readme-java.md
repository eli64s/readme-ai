<p align="left">
  <img src="https://img.icons8.com/external-tal-revivo-filled-tal-revivo/96/external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-filled-tal-revivo.png" width="100" />
</p>
<p align="left">
    <h1 align="left">MINIMAL-TODO</h1>
</p>
<p align="left">
    <em>Minimal-Todo: Simplify Your Task Management</em>
</p>
<p align="left">
	<!-- Shields.io badges not used with skill icons. --><p>
<p align="left">
		<em>Developed with the software and tools below</em>
</p>
<p align="left">
	<a href="https://skillicons.dev">
		<img src="https://skillicons.dev/icons?i=github,gradle,java,md&theme=light">
	</a>
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

Minimal-Todo is a lightweight Android application that helps users keep track of their tasks and to-do lists. The project's main purpose is to provide a simple and intuitive interface for managing tasks efficiently. The app allows users to create, update, and delete tasks, set due dates and priorities, and mark tasks as completed. It also includes features like search and filtering to help users organize and find tasks easily. Minimal-Todo's value proposition lies in its minimalist design and straightforward functionality, making it a practical choice for those seeking a hassle-free task management solution.

---

## 📦 Features

|    | Feature           | Description                                                                                                       |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**    | The architecture of the system is not explicitly mentioned in the repository. It appears to be a traditional Android app architecture with activities, fragments, and custom views. |
| 📄 | **Documentation**  | The repository lacks comprehensive documentation. There is a README.md file that provides basic setup instructions, but additional documentation is sparse. |
| 🔗 | **Dependencies**   | The repository relies on several external libraries such as Calligraphy, TextDrawable, and YAML. The specific versions and purposes of these dependencies are not explicitly mentioned. |
| 🧩 | **Modularity**     | The system is organized into smaller components like fragments, activities, and custom views. The separation of concerns could be improved by following a more structured architecture pattern. |
| 🧪 | **Testing**        | The repository does not include extensive testing. There are some basic unit tests and instrumented tests present in the `androidTest` directory, but the coverage is limited. |
| ⚡️ | **Performance**     | There is no specific information available regarding performance optimizations. The app's performance may depend on individual device configurations and the efficiency of implemented code. |
| 🔐 | **Security**       | The repository does not have explicit security measures mentioned. Basic security practices like secure data storage and network communication should be implemented for a production-level app. |
| 🔀 | **Version Control**| The repository uses Git for version control. The presence of a `.gitignore` file, `.travis.yml` for CI/CD with Travis CI, and multiple commits indicate the use of version control practices. |
| 🔌 | **Integrations**   | The system does not appear to have direct integrations with external systems or services. However, it utilizes external libraries for specific functionality, as mentioned in the dependencies section. |
| 📶 | **Scalability**    | The scalability of the system is not explicitly discussed in the repository. The app's performance and scalability may depend on the efficiency of implemented code and potential architecture improvements. |

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

| File                                                                                  | Summary                                                                                                                                                                                                                                                                                                                     |
| ---                                                                                   | ---                                                                                                                                                                                                                                                                                                                         |
| [build.gradle](https://github.com/avjinder/Minimal-Todo/blob/main/build.gradle)       | This code snippet is a part of the Minimal-Todo repository. It configures the build and dependencies for the Android application, using Gradle for managing the project. The code ensures necessary plugins and repositories are included for successful compilation and execution of the app.                              |
| [gradlew.bat](https://github.com/avjinder/Minimal-Todo/blob/main/gradlew.bat)         | This code snippet is a Gradle startup script for the Windows operating system. It sets up the JVM options, finds the Java executable, and executes the Gradle build process. It is a critical component in the overall architecture of the repository as it facilitates the build and configuration of the project.         |
| [settings.gradle](https://github.com/avjinder/Minimal-Todo/blob/main/settings.gradle) | This code snippet is part of the Minimal-Todo repository. It plays a critical role in the main app's architecture. The code achieves specific functionalities listed in the `app/` directory and relies on dependencies and software mentioned in the `settings.gradle` file. Key files within the codebase include `:app`. |
| [.travis.yml](https://github.com/avjinder/Minimal-Todo/blob/main/.travis.yml)         | This code snippet is a part of the Minimal-Todo repository's architecture. It builds the Android app, utilizing various tools and dependencies specified in the codebase. The main goal is to successfully build the app using the provided configurations.                                                                 |

</details>

<details closed><summary>app</summary>

| File                                                                                                | Summary                                                                                                                                                                                                                                                                                                                                                            |
| ---                                                                                                 | ---                                                                                                                                                                                                                                                                                                                                                                |
| [proguard-rules.pro](https://github.com/avjinder/Minimal-Todo/blob/main/app/proguard-rules.pro)     | The code snippet in the `proguard-rules.pro` file contains project-specific ProGuard rules. It specifies the flags and options for code obfuscation and optimization when building the Android app. It includes rules for keeping certain classes and packages from being obfuscated. The file also includes rules for handling WebView and JavaScript interfaces. |
| [build.gradle](https://github.com/avjinder/Minimal-Todo/blob/main/app/build.gradle)                 | The code snippet in the app/build.gradle file configures the Android application, specifying its version, dependencies, and build settings. It includes libraries for analytics, UI components, and support for different Android versions.                                                                                                                        |
| [google-services.json](https://github.com/avjinder/Minimal-Todo/blob/main/app/google-services.json) | This code snippet, located in the app directory, includes the necessary configuration files and source code for the Minimal-Todo Android app. It uses the google-services.json file for dependencies and software integration. The codebase is part of the Minimal-Todo repository, which follows a specific directory structure.                                  |

</details>

<details closed><summary>app.src.androidTest.java.com.example.avjindersinghsekhon.minimaltodo</summary>

| File                                                                                                                                                                             | Summary                                                                                                                                                                                                                                                                                             |
| ---                                                                                                                                                                              | ---                                                                                                                                                                                                                                                                                                 |
| [TestStoreRetrieveData.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/TestStoreRetrieveData.java) | This code snippet contains test cases for the StoreRetrieveData class. It verifies the functionality of storing and retrieving data from a storage file, and also checks the conversion of data to JSON format.                                                                                     |
| [ApplicationTest.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/ApplicationTest.java)             | Summary: The code snippet in the `ApplicationTest.java` file is a test case that verifies the functionality of the `Application` class in the Minimal-Todo Android app. It is part of the parent repository's architecture and helps ensure the quality and reliability of the application.         |
| [TestTodoItem.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/TestTodoItem.java)                   | This code snippet contains JUnit tests that verify the functionality of the ToDoItem class. It checks if the ToDoItem object can be constructed using a three-parameter constructor, marshalled to JSON, and unmarshalled from JSON. The tests ensure that the object properties are set correctly. |

</details>

<details closed><summary>app.src.main.java.com.example.avjindersinghsekhon.minimaltodo.Settings</summary>

| File                                                                                                                                                                     | Summary                                                                                                                                                                                                                   |
| ---                                                                                                                                                                      | ---                                                                                                                                                                                                                       |
| [SettingsFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Settings/SettingsFragment.java) | This code snippet is a SettingsFragment class that handles user preferences in the Minimal-Todo Android app. It allows users to change the app's theme and uses Google Analytics to track Night Mode usage.               |
| [SettingsActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Settings/SettingsActivity.java) | This code snippet represents the SettingsActivity file within the Minimal-Todo repository. It is responsible for managing the settings screen of the Minimal Todo app, including theme selection and navigation handling. |

</details>

<details closed><summary>app.src.main.java.com.example.avjindersinghsekhon.minimaltodo.Reminder</summary>

| File                                                                                                                                                                     | Summary                                                                                                                                                                                                                                                                  |
| ---                                                                                                                                                                      | ---                                                                                                                                                                                                                                                                      |
| [ReminderFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Reminder/ReminderFragment.java) | This code snippet is a reminder fragment that handles the display and functionality of reminders in the Minimal-Todo app. It allows users to view, modify, and remove reminders. The code includes features like snooze options, saving data, and handling menu options. |
| [ReminderActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Reminder/ReminderActivity.java) | This code snippet is a key file in the Minimal-Todo repository. It handles the creation of reminder activities within the app, utilizing the ReminderFragment. It extends a base activity and sets the layout to reminder_layout.                                        |

</details>

<details closed><summary>app.src.main.java.com.example.avjindersinghsekhon.minimaltodo.About</summary>

| File                                                                                                                                                            | Summary                                                                                                                                                                                                                                                                                                                                                     |
| ---                                                                                                                                                             | ---                                                                                                                                                                                                                                                                                                                                                         |
| [AboutActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/About/AboutActivity.java) | This code snippet is part of an Android app's repository and is located in the `com.example.avjindersinghsekhon.minimaltodo.About` package. It represents the `AboutActivity` class, which is responsible for displaying information about the app, including its version and a toolbar. It also allows the user to navigate back to the previous activity. |
| [AboutFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/About/AboutFragment.java) | The code snippet is a part of the Minimal-Todo repository's architecture. It contains the AboutFragment.java file, which handles the display of app version, toolbar, and contact information. This code contributes to the user interface and analytics functionality of the app.                                                                          |

</details>

<details closed><summary>app.src.main.java.com.example.avjindersinghsekhon.minimaltodo.AddToDo</summary>

| File                                                                                                                                                                  | Summary                                                                                                                                                                                                |
| ---                                                                                                                                                                   | ---                                                                                                                                                                                                    |
| [AddToDoFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AddToDo/AddToDoFragment.java) | This code snippet is part of the Minimal-Todo repository and it consists of a Java class called AddToDoFragment. It handles the logic and user interface for adding new tasks in the Minimal Todo app. |
| [AddToDoActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AddToDo/AddToDoActivity.java) | The code snippet is an Android activity that adds a new to-do item. It extends AppDefaultActivity and sets up the layout and initial fragment for the to-do creation process.                          |

</details>

<details closed><summary>app.src.main.java.com.example.avjindersinghsekhon.minimaltodo.Main</summary>

| File                                                                                                                                                                                                 | Summary                                                                                                                                                                                                                                                                            |
| ---                                                                                                                                                                                                  | ---                                                                                                                                                                                                                                                                                |
| [MainActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/MainActivity.java)                                         | This code snippet is the main activity of the Minimal-Todo app. It handles the creation of the toolbar, menu options, and navigation to other activities like About and Settings.                                                                                                  |
| [CustomRecyclerScrollViewListener.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/CustomRecyclerScrollViewListener.java) | This code snippet is a custom implementation of a scroll listener for a RecyclerView. It enables hiding and showing of a view based on the scroll direction and distance. The code provides the ability to customize the actions to be performed when the view is shown or hidden. |
| [MainFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/MainFragment.java)                                         | The code snippet is a key file in the Minimal-Todo repository. It contains the main functionality and user interface elements for the app, including alarms, shared preferences, and a RecyclerView for displaying tasks.                                                          |

</details>

<details closed><summary>app.src.main.java.com.example.avjindersinghsekhon.minimaltodo.Analytics</summary>

| File                                                                                                                                                                              | Summary                                                                                                                                                                                                                                                                                                                                                               |
| ---                                                                                                                                                                               | ---                                                                                                                                                                                                                                                                                                                                                                   |
| [AnalyticsApplication.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Analytics/AnalyticsApplication.java) | The `AnalyticsApplication.java` file in the parent repository's `app` directory is responsible for handling analytics tracking within the Minimal Todo app. It initializes and manages the Google Analytics tracker, sets up analytics properties, and sends tracking events and screen views. The code also provides methods for sending customized tracking events. |

</details>

<details closed><summary>app.src.main.java.com.example.avjindersinghsekhon.minimaltodo.AppDefault</summary>

| File                                                                                                                                                                           | Summary                                                                                                                                                                                                                                                                                                                         |
| ---                                                                                                                                                                            | ---                                                                                                                                                                                                                                                                                                                             |
| [AppDefaultFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AppDefault/AppDefaultFragment.java) | This code snippet defines an abstract class called AppDefaultFragment that extends the Fragment class. It provides a method for inflating the layout of the fragment and a callback for when the fragment is destroyed. This class serves as a base class for implementing custom fragments within the Minimal-Todo repository. |
| [AppDefaultActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AppDefault/AppDefaultActivity.java) | The code snippet defines an abstract activity class, AppDefaultActivity, that sets up an initial fragment and handles the creation of a ContentViewLayoutRes. It is part of an Android repository structure for a Minimal Todo app.                                                                                             |

</details>

<details closed><summary>app.src.main.java.com.example.avjindersinghsekhon.minimaltodo.Utility</summary>

| File                                                                                                                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                |
| ---                                                                                                                                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                    |
| [TodoNotificationService.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/TodoNotificationService.java)     | The `TodoNotificationService` class in the `Utility` package is responsible for handling and displaying notifications for the Minimal-Todo app. It receives a todo item's text and unique identifier, and creates a notification with the provided content. The notification includes a title, small icon, and actions for opening the app and deleting the todo item. |
| [ScrollingFABBehaviour.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ScrollingFABBehaviour.java)         | The code snippet is an implementation of a custom behavior for a FloatingActionButton in a CoordinatorLayout. It allows the button to react to the scrolling of certain views, such as a Snackbar or a Toolbar, by animating its position.                                                                                                                             |
| [ToDoItem.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ToDoItem.java)                                   | This code snippet includes the ToDoItem class, which represents a single task in the Minimal-Todo app. It stores information such as the task text, description, reminder status, color, date, and identifier. The class provides methods for creating objects, converting to JSON, and accessing/updating task properties.                                            |
| [CustomTextInputLayout.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/CustomTextInputLayout.java)         | This code snippet is a custom implementation of the TextInputLayout class in Android. It ensures that the hint text is always visible, even after the EditText's hint is cleared. It overrides the onDraw method to achieve this behavior.                                                                                                                             |
| [StoreRetrieveData.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/StoreRetrieveData.java)                 | The `StoreRetrieveData` class in the `Utility` package of the codebase enables the saving and loading of `ToDoItem` objects to and from a file in the app's internal storage. It provides methods to convert the items to JSON format, save them to a file, and load them back into an `ArrayList`.                                                                    |
| [Utils.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/Utils.java)                                         | The code snippet in `Utils.java` retrieves the height of the toolbar in the app by accessing the theme attributes. This information is crucial for the parent repository's architecture as it determines layout calculations.                                                                                                                                          |
| [DeleteNotificationService.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/DeleteNotificationService.java) | This code snippet is a service that handles the deletion of a notification in the Minimal-Todo app. It retrieves the data, finds the corresponding notification, removes it, and saves the updated data. It also marks the data as changed for future use.                                                                                                             |
| [ItemTouchHelperClass.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ItemTouchHelperClass.java)           | The `ItemTouchHelperClass` in the `Utility` package is a crucial file in the Minimal-Todo repository. It provides functionality for dragging and swiping items in a RecyclerView. This code snippet enables the movement and removal of items within the application's UI.                                                                                             |
| [PreferenceKeys.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/PreferenceKeys.java)                       | This code snippet defines the key preference for night mode in the Minimal-Todo app. It retrieves the resource string for the night mode preference key. Its parent repository has a directory structure with various files and dependencies.                                                                                                                          |
| [RecyclerViewEmptySupport.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/RecyclerViewEmptySupport.java)   | The code snippet defines a custom RecyclerView class called RecyclerViewEmptySupport. It is responsible for displaying an empty view when the RecyclerView has no items. The class handles updating the visibility of the empty view based on changes in the adapter's data.                                                                                           |

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
