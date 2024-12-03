<div align="left">
    <img src="https://www.svgrepo.com/show/366569/application-x-java.svg" width="30%" align="left" style="margin-right: 15px"/>
    <div style="display: inline-block;">
        <h2 style="display: inline-block; vertical-align: middle; margin-top: 0;">MINIMAL-TODO</h2>
        <p>
	<em>Streamline Tasks, Empower Productivity!</em>
</p>
        <p>
	<img src="https://img.shields.io/github/license/avjinder/Minimal-Todo?style=plastic&logo=opensourceinitiative&logoColor=white&color=5D3FD3" alt="license">
	<img src="https://img.shields.io/github/last-commit/avjinder/Minimal-Todo?style=plastic&logo=git&logoColor=white&color=5D3FD3" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/avjinder/Minimal-Todo?style=plastic&color=5D3FD3" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/avjinder/Minimal-Todo?style=plastic&color=5D3FD3" alt="repo-language-count">
</p>
        <p>Tech Stack</p>
        <p>
	<img src="https://img.shields.io/badge/Android-34A853.svg?style=plastic&logo=Android&logoColor=white" alt="Android">
	<img src="https://img.shields.io/badge/Gradle-02303A.svg?style=plastic&logo=Gradle&logoColor=white" alt="Gradle">
	<img src="https://img.shields.io/badge/Google-4285F4.svg?style=plastic&logo=Google&logoColor=white" alt="Google">
	<img src="https://img.shields.io/badge/java-%23ED8B00.svg?style=plastic&logo=openjdk&logoColor=white" alt="java">
</p>
    </div>
</div>
<br clear="left"/>

<details><summary>Table of Contents</summary>

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🤖 Usage](#🤖-usage)
  - [🧪 Testing](#🧪-testing)
- [📌 Roadmap](#-project-roadmap)
- [🔰 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

</details>
<hr>

## 📍 Overview

Minimal-Todo is a streamlined task management app simplifying daily organization. Its clean interface and intuitive features, like reminders and color-coding, enhance productivity. Ideal for busy professionals seeking efficient task tracking. Centralize your to-dos with ease for a clutter-free schedule.

---

## 👾 Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Uses **Java** as the primary language with **Gradle** as the build system.</li><li>Organized project structure with modules defined in **settings.gradle** for efficient management.</li><li>Integration of crucial services like **Google services** configured in **google-services.json**.</li><li>Optimizes code efficiency and security through **ProGuard** rules in **app/proguard-rules.pro**.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>**27 Java files** emphasizing clean, maintainable code.</li><li>Consistent **build configurations** and dependencies management in **build.gradle**.</li><li>Incorporates automated **testing** with **gradle test** command in the codebase.</li><li>Utilizes **Butter Knife plugin** for streamlined view injections.</li></ul> |
| 📄 | **Documentation** | <ul><li>Comprehensive documentation in **Java** with **27 files** covering various components.</li><li>Usage of **Gradle** for managing build commands, as shown in the **install_commands** and **test_commands** details.</li><li>Clear instructions for setup and execution using **Gradle** commands such as **gradle build** and **gradle run**.</li><li>**API references** and **usage guidelines** embedded within code files for easy navigation.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integration of **Google services** through **google-services.json** for enhanced app functionalities.</li><li>Utilizes **Butter Knife plugin** for seamless view injections and binding.</li><li>Integrates **ProGuard** rules in **app/proguard-rules.pro** for code optimization and security.</li><li>**Gradle** build system integration for handling dependencies and project configurations.</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Well-structured project with modules defined in **settings.gradle** for modularity.</li><li>Encapsulates functionalities within separate **Java files** for easy navigation and maintenance.</li><li>Utilizes **fragments** for modular UI components, enhancing reusability.</li><li>**Utilities** like **StoreRetrieveData** and **ItemTouchHelperClass** promote code modularity and extensibility.</li></ul> |
| 🧪 | **Testing**       | <ul><li>Comprehensive **Android** app testing with files like **TestStoreRetrieveData** and **ApplicationTest**.</li><li>Tests key functionalities like data storage operations and app behavior validation.</li><li>**Ensures data integrity** by verifying JSON conversion and task handling in **TestTodoItem**.</li><li>**Utilizes** **Gradle** framework for running tests in a structured manner.</li></ul> |

---

## 📁 Project Structure

```sh
└── Minimal-Todo/
    ├── Contributing.md
    ├── LICENSE.md
    ├── README.md
    ├── app
    ├── build.gradle
    ├── gradle
    ├── gradle.properties
    ├── gradlew
    ├── gradlew.bat
    ├── screenshots
    └── settings.gradle
```


### 📂 Project Index
<details open>
	<summary><b><code>MINIMAL-TODO/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/build.gradle'>build.gradle</a></b></td>
				<td>- Configure common build options and dependencies across all modules in the project, including repositories like jcenter and Google, using the build.gradle file<br>- This file manages top-level configurations for sub-projects/modules such as Android tools, Google services, and Butter Knife plugin, ensuring consistent settings for the entire codebase architecture.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/gradlew.bat'>gradlew.bat</a></b></td>
				<td>Initialize Gradle setup on Windows by locating Java and setting necessary environment variables for the project to run smoothly.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/settings.gradle'>settings.gradle</a></b></td>
				<td>- Defines project modules for Gradle build system, specifically including the 'app' module<br>- Organizes project structure by specifying which modules are part of the build<br>- Helps Gradle manage dependencies and build configurations for different modules within the project.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- app Submodule -->
		<summary><b>app</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/proguard-rules.pro'>proguard-rules.pro</a></b></td>
				<td>- Define and maintain project-specific ProGuard rules to optimize and secure the Android app's code<br>- Refine the default ProGuard flags with tailored settings for Google libraries and avoid warnings for specific classes<br>- Ensure that the app's code remains efficient and protected during the build process.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/build.gradle'>build.gradle</a></b></td>
				<td>- Configure Android application settings, dependencies, and build types to support the project's functionality and integrate necessary plugins for smooth operation.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/google-services.json'>google-services.json</a></b></td>
				<td>- Define Google services configuration for Android apps in the provided JSON file<br>- The file specifies project info, clients, and associated services such as analytics and cloud messaging<br>- It serves as a crucial configuration file for integrating Google services into the Android app architecture.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/app-release.apk'>app-release.apk</a></b></td>
				<td>- Summary:
The provided code file serves as a critical component within the project's architecture, facilitating seamless communication and integration between various modules<br>- It plays a pivotal role in orchestrating data flow and enhancing the overall functionality of the codebase.</td>
			</tr>
			</table>
			<details>
				<summary><b>src</b></summary>
				<blockquote>
					<details>
						<summary><b>androidTest</b></summary>
						<blockquote>
							<details>
								<summary><b>java</b></summary>
								<blockquote>
									<details>
										<summary><b>com</b></summary>
										<blockquote>
											<details>
												<summary><b>example</b></summary>
												<blockquote>
													<details>
														<summary><b>avjindersinghsekhon</b></summary>
														<blockquote>
															<details>
																<summary><b>minimaltodo</b></summary>
																<blockquote>
																	<table>
																	<tr>
																		<td><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/TestStoreRetrieveData.java'>TestStoreRetrieveData.java</a></b></td>
																		<td>- Verifies and ensures data integrity by writing and reading items to/from storage in the app<br>- It confirms the correct storage and retrieval of data items, validates JSONArray conversion, and guarantees the accuracy of data in storage<br>- The code is vital for maintaining the reliability of data operations within the app's functionality.</td>
																	</tr>
																	<tr>
																		<td><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/ApplicationTest.java'>ApplicationTest.java</a></b></td>
																		<td>- Tests the Android application's fundamental functionality by extending the ApplicationTestCase class<br>- This class helps validate the core behavior of the application, ensuring proper functionality before deployment.</td>
																	</tr>
																	<tr>
																		<td><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/TestTodoItem.java'>TestTodoItem.java</a></b></td>
																		<td>Verifies and tests functionality of ToDoItem class, ensuring construction and marshalling of objects to JSON, as well as unmarshalling from JSON data.</td>
																	</tr>
																	</table>
																</blockquote>
															</details>
														</blockquote>
													</details>
												</blockquote>
											</details>
										</blockquote>
									</details>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>main</b></summary>
						<blockquote>
							<details>
								<summary><b>java</b></summary>
								<blockquote>
									<details>
										<summary><b>com</b></summary>
										<blockquote>
											<details>
												<summary><b>example</b></summary>
												<blockquote>
													<details>
														<summary><b>avjindersinghsekhon</b></summary>
														<blockquote>
															<details>
																<summary><b>minimaltodo</b></summary>
																<blockquote>
																	<details>
																		<summary><b>Settings</b></summary>
																		<blockquote>
																			<table>
																			<tr>
																				<td><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Settings/SettingsFragment.java'>SettingsFragment.java</a></b></td>
																				<td>- Manages user settings and preferences, including a night mode feature, for the mobile app<br>- Captures user selection changes and triggers interface updates accordingly<br>- Enables customization of app themes and analytics tracking for user behavior insights<br>- Centralizes and organizes user preferences for a seamless user experience.</td>
																			</tr>
																			<tr>
																				<td><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Settings/SettingsActivity.java'>SettingsActivity.java</a></b></td>
																				<td>- Implements the SettingsActivity class in the app structure<br>- Manages settings presentation and navigation, including theme configuration and back navigation actions, providing a seamless user experience within the application's settings section.</td>
																			</tr>
																			</table>
																		</blockquote>
																	</details>
																	<details>
																		<summary><b>Reminder</b></summary>
																		<blockquote>
																			<table>
																			<tr>
																				<td><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Reminder/ReminderFragment.java'>ReminderFragment.java</a></b></td>
																				<td>- Implements a ReminderFragment in the app to handle reminders for to-do items<br>- Allows users to view and manage reminders, including snoozing and marking tasks as done<br>- Handles theme preferences, data storage, and notification services<br>- Includes functionalities for modifying reminder timings and updating to-do items.</td>
																			</tr>
																			<tr>
																				<td><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Reminder/ReminderActivity.java'>ReminderActivity.java</a></b></td>
																				<td>Generates the reminder UI layout and initializes the initial fragment for the Minimal Todo app.</td>
																			</tr>
																			</table>
																		</blockquote>
																	</details>
																	<details>
																		<summary><b>About</b></summary>
																		<blockquote>
																			<table>
																			<tr>
																				<td><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/About/AboutActivity.java'>AboutActivity.java</a></b></td>
																				<td>- Handle the creation and display of the About section in the Minimal Todo app, including version information and contact details<br>- This code ensures proper theming, toolbar setup, and navigation functionalities for a cohesive user experience within the app's architecture.</td>
																			</tr>
																			<tr>
																				<td><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/About/AboutFragment.java'>AboutFragment.java</a></b></td>
																				<td>- Manages display of app information, version, and feedback contact in the About section of the project<br>- Utilizes the AppDefaultFragment superclass to ensure consistent UI across the app<br>- Interacts with the AnalyticsApplication to track user actions for analytics purposes.</td>
																			</tr>
																			</table>
																		</blockquote>
																	</details>
																	<details>
																		<summary><b>AddToDo</b></summary>
																		<blockquote>
																			<table>
																			<tr>
																				<td><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AddToDo/AddToDoFragment.java'>AddToDoFragment.java</a></b></td>
																				<td>- The provided code file `AddToDoFragment.java` in the `AddToDo` package is responsible for managing the user interface related to adding a new to-do item in the MinimalToDo project<br>- It handles user input, interactions, and transitions within the add to-do functionality<br>- This fragment is crucial for enabling users to efficiently create and manage their tasks within the application.</td>
																			</tr>
																			<tr>
																				<td><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AddToDo/AddToDoActivity.java'>AddToDoActivity.java</a></b></td>
																				<td>- Enables adding to-dos via a user-friendly interface<br>- Extends the base activity to set up the layout and initial fragment<br>- Implementations for onCreate, contentViewLayoutRes, createInitialFragment, and onResume maintain the seamless flow for users.</td>
																			</tr>
																			</table>
																		</blockquote>
																	</details>
																	<details>
																		<summary><b>Main</b></summary>
																		<blockquote>
																			<table>
																			<tr>
																				<td><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/MainActivity.java'>MainActivity.java</a></b></td>
																				<td>- Defines the main screen behavior of the app, handling toolbar setup, menu creation, and item selection actions<br>- It navigates to other activities like About and Settings when corresponding menu items are selected.</td>
																			</tr>
																			<tr>
																				<td><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/CustomRecyclerScrollViewListener.java'>CustomRecyclerScrollViewListener.java</a></b></td>
																				<td>- Implements a scroll listener for RecyclerView to toggle visibility of elements based on scroll direction<br>- Integrates show and hide actions to manage view visibility dynamically during scrolling.</td>
																			</tr>
																			<tr>
																				<td><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/MainFragment.java'>MainFragment.java</a></b></td>
																				<td>- The MainFragment.java file in the project serves as a central component responsible for managing the user interface elements and interactions within the application<br>- It coordinates the display of tasks, animations, and user feedback mechanisms, ensuring a seamless user experience<br>- This file encapsulates the key functionalities of the main screen of the app, facilitating efficient task management and user engagement.</td>
																			</tr>
																			</table>
																		</blockquote>
																	</details>
																	<details>
																		<summary><b>Analytics</b></summary>
																		<blockquote>
																			<table>
																			<tr>
																				<td><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Analytics/AnalyticsApplication.java'>AnalyticsApplication.java</a></b></td>
																				<td>- Facilitates sending analytics data to Google Analytics by tracking screen views and events in the Android application<br>- Manages the creation and configuration of a Google Analytics tracker, ensuring proper reporting of user interactions and app usage for data-driven insights.</td>
																			</tr>
																			</table>
																		</blockquote>
																	</details>
																	<details>
																		<summary><b>AppDefault</b></summary>
																		<blockquote>
																			<table>
																			<tr>
																				<td><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AppDefault/AppDefaultFragment.java'>AppDefaultFragment.java</a></b></td>
																				<td>Generates default fragments in the project architecture to maintain a consistent layout across different screens.</td>
																			</tr>
																			<tr>
																				<td><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AppDefault/AppDefaultActivity.java'>AppDefaultActivity.java</a></b></td>
																				<td>- Defines a template for activities in the app, setting up the initial fragment and content view layout<br>- The abstract class specifies methods to define layout and create the first fragment, binding the core structure of app screens to maintain consistency across activities.</td>
																			</tr>
																			</table>
																		</blockquote>
																	</details>
																	<details>
																		<summary><b>Utility</b></summary>
																		<blockquote>
																			<table>
																			<tr>
																				<td><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/TodoNotificationService.java'>TodoNotificationService.java</a></b></td>
																				<td>- Manages creation and display of notifications for to-do items, including handling user interactions<br>- Uses Android's NotificationManager to show notifications with title and icon<br>- Enables users to interact with notifications for reminders and deletion<br>- Key components include IntentService and Notification.Builder for seamless notification handling within the app's architecture.</td>
																			</tr>
																			<tr>
																				<td><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ScrollingFABBehaviour.java'>ScrollingFABBehaviour.java</a></b></td>
																				<td>- Enables floating action button behavior based on scrolling events in the app's UI, ensuring its position corresponds to toolbar movements<br>- Decides the floating button view adjustment by detecting interactions with various UI components like Snackbar and Toolbar.</td>
																			</tr>
																			<tr>
																				<td><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ToDoItem.java'>ToDoItem.java</a></b></td>
																				<td>- Defines a data model for to-do items with text, description, reminder, color, date, and identifier properties<br>- Supports conversion to/from JSON format<br>- Allows setting and getting text, description, reminder status, color, date, and identifier.</td>
																			</tr>
																			<tr>
																				<td><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/CustomTextInputLayout.java'>CustomTextInputLayout.java</a></b></td>
																				<td>- Enhances TextInputLayout behavior to preserve hint value when EditText is added<br>- Resets hint if changed programmatically for consistent display<br>- Improves user experience by maintaining hint visibility, avoiding loss of information.</td>
																			</tr>
																			<tr>
																				<td><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/StoreRetrieveData.java'>StoreRetrieveData.java</a></b></td>
																				<td>- Manages storage and retrieval of ToDoItems using JSON serialization for the MinimalToDo app<br>- Handles saving items to a file and loading them back into the app, supporting basic file I/O operations and JSON parsing with error handling.</td>
																			</tr>
																			<tr>
																				<td><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/Utils.java'>Utils.java</a></b></td>
																				<td>Calculates toolbar height for the Android app's UI based on specified action bar size attribute in the project's utility class.</td>
																			</tr>
																			<tr>
																				<td><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/DeleteNotificationService.java'>DeleteNotificationService.java</a></b></td>
																				<td>- Handles deleting notification-triggered to-do items by retrieving, updating, and saving data in shared preferences<br>- Manages a list of to-do items, identifies the item to delete, and saves the updated list<br>- Maintains a notification service for to-do items in the Minimal ToDo app, ensuring data integrity and accurate deletion operations.</td>
																			</tr>
																			<tr>
																				<td><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ItemTouchHelperClass.java'>ItemTouchHelperClass.java</a></b></td>
																				<td>- Enables drag-and-drop and swipe functionalities for RecyclerView items, facilitating reordering and deletion<br>- This class acts as a mediator, allowing seamless interaction between user actions and the RecyclerView adapter, enhancing the user experience within the to-do list app.</td>
																			</tr>
																			<tr>
																				<td><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/PreferenceKeys.java'>PreferenceKeys.java</a></b></td>
																				<td>Defines preference keys for the project settings, facilitating easy access to the night mode preference key stored in resources.</td>
																			</tr>
																			<tr>
																				<td><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/RecyclerViewEmptySupport.java'>RecyclerViewEmptySupport.java</a></b></td>
																				<td>- Enables a RecyclerView to display an empty view when no items are present<br>- Automatically shows or hides the empty view based on the adapter's item count<br>- Integrated with observer methods to handle changes in data set<br>- Enhances user experience by providing visual feedback in empty states, contributing to a more informative UI.</td>
																			</tr>
																			</table>
																		</blockquote>
																	</details>
																</blockquote>
															</details>
														</blockquote>
													</details>
												</blockquote>
											</details>
										</blockquote>
									</details>
								</blockquote>
							</details>
						</blockquote>
					</details>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---
## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with Minimal-Todo, ensure your runtime environment meets the following requirements:

- **Programming Language:** Java
- **Package Manager:** Gradle


### ⚙️ Installation

Install Minimal-Todo using one of the following methods:

**Build from source:**

1. Clone the Minimal-Todo repository:
```sh
❯ git clone https://github.com/avjinder/Minimal-Todo
```

2. Navigate to the project directory:
```sh
❯ cd Minimal-Todo
```

3. Install the project dependencies:


**Using `gradle`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Gradle-02303A.svg?style={badge_style}&logo=gradle&logoColor=white" />](https://gradle.org/)

```sh
❯ gradle build
```




### 🤖 Usage
Run Minimal-Todo using the following command:
**Using `gradle`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Gradle-02303A.svg?style={badge_style}&logo=gradle&logoColor=white" />](https://gradle.org/)

```sh
❯ gradle run
```


### 🧪 Testing
Run the test suite using the following command:
**Using `gradle`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Gradle-02303A.svg?style={badge_style}&logo=gradle&logoColor=white" />](https://gradle.org/)

```sh
❯ gradle test
```


---
## 📌 Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/avjinder/Minimal-Todo/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/avjinder/Minimal-Todo/issues)**: Submit bugs found or log feature requests for the `Minimal-Todo` project.
- **💡 [Submit Pull Requests](https://github.com/avjinder/Minimal-Todo/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
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
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/avjinder/Minimal-Todo/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=avjinder/Minimal-Todo">
   </a>
</p>
</details>

---

## 🎗 License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 🙌 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---
