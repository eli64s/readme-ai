<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>MINIMAL-TODO</h1>
<h3>◦ Maximize productivity, minimize clutter!</h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat&logo=YAML&logoColor=white" alt="YAML" />
<img src="https://img.shields.io/badge/Gradle-02303A.svg?style=flat&logo=Gradle&logoColor=white" alt="Gradle" />
<img src="https://img.shields.io/badge/java-%23ED8B00.svg?style=flat&logo=openjdk&logoColor=white" alt="java" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style=flat&logo=JSON&logoColor=white" alt="JSON" />
</p>
<img src="https://img.shields.io/github/license/avjinder/Minimal-Todo?style=flat&color=5D6D7E" alt="GitHub license" />
<img src="https://img.shields.io/github/last-commit/avjinder/Minimal-Todo?style=flat&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/avjinder/Minimal-Todo?style=flat&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/languages/top/avjinder/Minimal-Todo?style=flat&color=5D6D7E" alt="GitHub top language" />
</div>

---

##  Table of Contents
- [ Table of Contents](#-table-of-contents)
- [ Overview](#-overview)
- [ Features](#-features)
- [ repository Structure](#-repository-structure)
- [ Modules](#modules)
- [ Getting Started](#-getting-started)
    - [ Installation](#-installation)
    - [ Running Minimal-Todo](#-running-Minimal-Todo)
    - [ Tests](#-tests)
- [ Roadmap](#-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

---


##  Overview

Minimal-Todo is an Android app that allows users to create a minimalistic to-do list. The app provides features such as adding new to-do items, setting reminders, and managing user preferences. It also includes utilities for data storage, notifications, and analytics integration. Overall, Minimal-Todo offers a simple and user-friendly interface for organizing tasks and staying productive.

---

##  Features

HTTPStatus Exception: 400

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

<details closed><summary>Root</summary>

| File                                                                                  | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---                                                                                   | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [build.gradle](https://github.com/avjinder/Minimal-Todo/blob/main/build.gradle)       | This code is a build file for an Android project called "Minimal-Todo". It includes dependencies for the Android Gradle plugin and the Google services plugin. It also includes the Butterknife plugin for view binding. The repositories section specifies where to find these dependencies.                                                                                                                                                                                                      |
| [gradlew.bat](https://github.com/avjinder/Minimal-Todo/blob/main/gradlew.bat)         | The code is a Windows batch script used to run Gradle commands for a specific project. It first checks for the presence of Java and sets up the environment variables. Then, it sets the classpath and executes Gradle with the provided command-line arguments. The script handles various Windows variants and provides error handling.                                                                                                                                                          |
| [settings.gradle](https://github.com/avjinder/Minimal-Todo/blob/main/settings.gradle) | The code adds the ":app" module to the project's settings.gradle file. This allows the project to include and build the app module within the overall project structure.                                                                                                                                                                                                                                                                                                                           |
| [.travis.yml](https://github.com/avjinder/Minimal-Todo/blob/main/.travis.yml)         | This is a configuration file for Travis CI, a continuous integration tool. It specifies the language as Android and defines the required components for building an Android project, such as platform tools and build tools. It also includes additional dependencies like Google Play services and repositories. The "before_script" section provides executable permissions to the gradlew script, and the "script" section specifies the command to build the project using the gradlew script. |

</details>

<details closed><summary>App</summary>

| File                                                                                                | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ---                                                                                                 | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [proguard-rules.pro](https://github.com/avjinder/Minimal-Todo/blob/main/app/proguard-rules.pro)     | The code is a ProGuard configuration file (.pro) for an Android app. It contains rules that specify how the code should be obfuscated and optimized during the build process. The file includes specific keep options for the project and also prevents warnings related to the use of Google libraries.                                                                                                                                                                                                                       |
| [build.gradle](https://github.com/avjinder/Minimal-Todo/blob/main/app/build.gradle)                 | The code in `app/build.gradle` is a configuration file for an Android application project. It specifies various settings, such as the application ID, minimum and target SDK versions, version code and name. It also includes dependencies for different libraries and plugins that the application needs, such as Google Play Services Analytics and support libraries for RecyclerView, design, and compatibility. Additionally, the code defines build types, signing configurations, lint options, and asset directories. |
| [google-services.json](https://github.com/avjinder/Minimal-Todo/blob/main/app/google-services.json) | The code provides a JSON representation of the configuration for the Minimal Todo app. It includes project information, client information, and status of various services like analytics, cloud messaging, app invites, Google sign-in, and ads. It also includes package names and tracking IDs for analytics.                                                                                                                                                                                                               |

</details>

<details closed><summary>Minimaltodo</summary>

| File                                                                                                                                                                             | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---                                                                                                                                                                              | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [TestStoreRetrieveData.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/TestStoreRetrieveData.java) | The code above is a set of test cases for the StoreRetrieveData class in the Minimal-Todo Android application. The test cases ensure the proper functionality of the data storage and retrieval process. The test cases include checking the preconditions of an empty data storage, writing items to the data storage, reading the items from the storage, comparing the retrieved items with the original test data, and testing the conversion of the test data into a JSONArray. |
| [ApplicationTest.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/ApplicationTest.java)             | The code is a basic test class for an Android application. It extends the ApplicationTestCase class and tests the Application class. It is part of a larger Android project called Minimal-Todo.                                                                                                                                                                                                                                                                                     |
| [TestTodoItem.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/TestTodoItem.java)                   | The code above contains JUnit tests for the functionality of the ToDoItem class. It includes tests for constructing a ToDoItem object with three parameters, marshaling ToDoItem objects to JSON, and unmarshaling JSON data to create ToDoItem objects. The tests verify that the expected properties of the ToDoItem object are correctly set and retrieved.                                                                                                                       |

</details>

<details closed><summary>Settings</summary>

| File                                                                                                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---                                                                                                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [SettingsFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Settings/SettingsFragment.java) | The code above is for the Settings Fragment in a to-do list app. It handles user preferences, such as enabling/disabling night mode. The fragment uses shared preferences to store and retrieve these settings, and it implements a listener to respond to changes in preferences. When the night mode preference is changed, it updates the theme and recreates the activity. The code also includes analytics integration to track the usage of night mode. |
| [SettingsActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Settings/SettingsActivity.java) | The code is for a Settings Activity in a to-do list app. It handles the creation of the activity layout and toolbar, sets the theme based on user preferences, configures the back button on the toolbar, and handles navigation to the parent activity when the back button is clicked. The code also includes functions to send analytics and to handle options selected in the toolbar menu.                                                               |

</details>

<details closed><summary>Reminder</summary>

| File                                                                                                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ---                                                                                                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [ReminderFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Reminder/ReminderFragment.java) | The code above is the implementation of the ReminderFragment class in the Minimal-Todo Android app. It represents the UI and functionality for the reminder feature in the app. The code handles setting up the layout and toolbar, retrieving and displaying the reminder item, allowing the user to remove the reminder, snooze options for the reminder, and saving changes to the reminder item.                                           |
| [ReminderActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Reminder/ReminderActivity.java) | The code is an Android application that includes a ReminderActivity class. The class extends the AppDefaultActivity class and overrides several methods, including onCreate, contentViewLayoutRes, and createInitialFragment. The onCreate method is empty, the contentViewLayoutRes method returns the layout resource ID for the reminder_layout, and the createInitialFragment method returns a new instance of the ReminderFragment class. |

</details>

<details closed><summary>About</summary>

| File                                                                                                                                                            | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---                                                                                                                                                             | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [AboutActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/About/AboutActivity.java) | The code is for the AboutActivity.java class in the Minimal-Todo app. It is responsible for displaying information about the app, such as the version number. The activity extends the AppDefaultActivity class and overrides the onCreate() method to set the theme and configure the toolbar. It also implements the createInitialFragment() method to create and display the AboutFragment. The onOptionsItemSelected() method handles the action when the user selects the home button in the toolbar. |
| [AboutFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/About/AboutFragment.java) | The code is a Java class that represents the About screen in a minimal todo application. It extends a base fragment class and overrides its methods to setup the view, set the app version, and handle user interactions. It also uses an AnalyticsApplication to send analytics data. The class has a static method to create a new instance of the AboutFragment.                                                                                                                                        |

</details>

<details closed><summary>Addtodo</summary>

| File                                                                                                                                                                  | Summary                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---                                                                                                                                                                   | ---                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [AddToDoFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AddToDo/AddToDoFragment.java) | The code is for the AddToDoFragment in an Android app called Minimal Todo. It includes functionality for adding a new to-do item, including setting a reminder date and time. It also includes features such as copying the to-do text to clipboard and displaying the last edited date.                                                                                                                            |
| [AddToDoActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AddToDo/AddToDoActivity.java) | The code represents an Android app that allows users to add tasks to a to-do list. The app contains an activity called "AddToDoActivity" which extends a parent activity called "AppDefaultActivity." The activity includes a method for creating the initial fragment and a method for setting the content view layout. The app also includes other files and directories related to building and running the app. |

</details>

<details closed><summary>Main</summary>

| File                                                                                                                                                                                                 | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---                                                                                                                                                                                                  | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [MainActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/MainActivity.java)                                         | This code is the main activity file for a minimal todo application. It sets up the toolbar, creates the initial fragment, and handles menu item selection, including intents for navigation to about and settings activities.                                                                                                                                                                                                                                            |
| [CustomRecyclerScrollViewListener.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/CustomRecyclerScrollViewListener.java) | This code represents a custom listener for a RecyclerView in an Android app. It tracks the scrolling distance of the RecyclerView and triggers events to show or hide certain elements based on the direction and magnitude of the scrolling motion.                                                                                                                                                                                                                     |
| [MainFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/MainFragment.java)                                         | The code is for a MainFragment class that extends the AppDefaultFragment class. It contains methods for creating a to-do list app interface, including a RecyclerView to display the to-do items, a FloatingActionButton for adding new items, and a CoordinatorLayout for displaying Snackbars. The code also includes methods for handling user interactions, such as adding and deleting items from the list, and saving and retrieving data using SharedPreferences. |

</details>

<details closed><summary>Analytics</summary>

| File                                                                                                                                                                              | Summary                                                                                                                                                                                                                                                                                                                                                     |
| ---                                                                                                                                                                               | ---                                                                                                                                                                                                                                                                                                                                                         |
| [AnalyticsApplication.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Analytics/AnalyticsApplication.java) | The code above is an Android application's Analytics module. It utilizes the Google Analytics framework to track and collect data about user interactions and behaviors within the app. It includes methods to send screen views, events, and custom parameters. The code also handles setting up the app tracker and defining the analytics configuration. |

</details>

<details closed><summary>Appdefault</summary>

| File                                                                                                                                                                           | Summary                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ---                                                                                                                                                                            | ---                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [AppDefaultFragment.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AppDefault/AppDefaultFragment.java) | The code is an abstract class that serves as a base for creating Fragments in an Android app. It defines a method that returns the layout resource ID for the Fragment's view, which is then inflated and returned in the onCreateView() method. The onDestroy() method is empty and can be overridden if needed. The purpose of this class is to provide a default implementation for creating Fragments with custom layouts. |
| [AppDefaultActivity.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AppDefault/AppDefaultActivity.java) | The code represents an abstract class called AppDefaultActivity, which extends AppCompatActivity. It sets up the initial fragment for the activity and handles the creation of the activity's layout and fragment. The specific layout and fragment to be used are determined by subclasses through the methods contentViewLayoutRes() and createInitialFragment().                                                            |

</details>

<details closed><summary>Utility</summary>

| File                                                                                                                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---                                                                                                                                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [TodoNotificationService.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/TodoNotificationService.java)     | The code is a utility class that handles notifications for a todo app. It extends the IntentService class and runs in the background. When triggered by an intent, it creates a notification with the provided todo text and UUID. The notification includes an action to open the reminder activity and a delete intent. The notification is then displayed using the NotificationManager.                                                                                                                                                                            |
| [ScrollingFABBehaviour.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ScrollingFABBehaviour.java)         | The code above is a custom behavior class called ScrollingFABBehaviour that extends the CoordinatorLayout.Behavior class. It is used to define the behavior of a FloatingActionButton (FAB) when scrolling in a CoordinatorLayout. The behavior includes handling dependency views such as Snackbar.SnackbarLayout and Toolbar. When a Snackbar is shown, the FAB is moved upwards, and when a Toolbar is scrolled, the FAB is moved downwards. The behavior of the FAB is determined by calculating the translation value based on the height of the dependent views. |
| [ToDoItem.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ToDoItem.java)                                   | The code defines a class called ToDoItem in the package com.example.avjindersinghsekhon.minimaltodo.Utility. This class represents a to-do item and contains various properties such as the to-do text, description, reminder status, color, date, and identifier. The class provides constructors, getter and setter methods, and methods to convert the object to JSON format and vice versa.                                                                                                                                                                        |
| [CustomTextInputLayout.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/CustomTextInputLayout.java)         | The code defines a class called CustomTextInputLayout, which extends the TextInputLayout class from the Android Support Library. The CustomTextInputLayout class provides a custom implementation for handling hints in an EditText field within a TextInputLayout. It overrides the addView method to store the hint value locally and the onDraw method to update the hint if it has changed programmatically. This allows for a consistent display of hints in the EditText field.                                                                                  |
| [StoreRetrieveData.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/StoreRetrieveData.java)                 | Exception:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Utils.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/Utils.java)                                         | The code provides a utility function called `getToolbarHeight` which retrieves the height of the toolbar in an Android application. It takes a `Context` as a parameter and returns the height as an integer value. The function uses the `obtainStyledAttributes` method to retrieve the toolbar's height from the application's theme resources. It then recycles the `TypedArray` to free the resources.                                                                                                                                                            |
| [DeleteNotificationService.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/DeleteNotificationService.java) | The code above defines a service in Android for deleting a notification. It retrieves a list of to-do items, finds a specific item based on an ID, removes it from the list, and saves the updated list. The service also updates a shared preference to indicate that a change in data has occurred.                                                                                                                                                                                                                                                                  |
| [ItemTouchHelperClass.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ItemTouchHelperClass.java)           | The code provided is a utility class called ItemTouchHelperClass, which extends the ItemTouchHelper.Callback class. This class is used to handle touch events for RecyclerView items. It provides functionalities such as enabling long press dragging, enabling item view swipe, defining movement flags (up, down, start, end), handling item movement, and handling item removal.                                                                                                                                                                                   |
| [PreferenceKeys.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/PreferenceKeys.java)                       | The code defines a class called PreferenceKeys that is used to access a preference key used in the Minimal-Todo app. The key is used to determine if the app is in night mode or not. The class has a constructor that takes a Resources object and sets the night_mode_pref_key using a string resource.                                                                                                                                                                                                                                                              |
| [RecyclerViewEmptySupport.java](https://github.com/avjinder/Minimal-Todo/blob/main/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/RecyclerViewEmptySupport.java)   | The code above defines a custom RecyclerView class called RecyclerViewEmptySupport. This class extends the existing RecyclerView class and adds functionality to display an empty view when the RecyclerView has no items to show. It includes methods to show the empty view, set the adapter for the RecyclerView, and specify an empty view to be displayed. It also includes an AdapterDataObserver that listens for changes in the adapter data and updates the empty view accordingly.                                                                           |

</details>

---

##  Getting Started

***Dependencies***

Please ensure you have the following dependencies installed on your system:

`- ℹ️ Dependency 1`

`- ℹ️ Dependency 2`

`- ℹ️ ...`

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
