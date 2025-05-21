<div id="top">

<!-- HEADER STYLE: COMPACT -->
<img src="../../../../readmeai/assets/logos/black.svg" width="30%" align="left" style="margin-right: 15px">

# MINIMAL-TODO
<em>Streamline Your Workflow, Amplify Your Productivity</em>

<!-- BADGES -->
<img src="https://img.shields.io/github/license/avjinder/Minimal-Todo?style=plastic&logo=opensourceinitiative&logoColor=white&color=87ceeb" alt="license">
<img src="https://img.shields.io/github/last-commit/avjinder/Minimal-Todo?style=plastic&logo=git&logoColor=white&color=87ceeb" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/avjinder/Minimal-Todo?style=plastic&color=87ceeb" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/avjinder/Minimal-Todo?style=plastic&color=87ceeb" alt="repo-language-count">

<em>Technology Stack:</em>

<img src="https://img.shields.io/badge/Android-34A853.svg?style=plastic&logo=Android&logoColor=white" alt="Android">
<img src="https://img.shields.io/badge/Gradle-02303A.svg?style=plastic&logo=Gradle&logoColor=white" alt="Gradle">
<img src="https://img.shields.io/badge/Google-4285F4.svg?style=plastic&logo=Google&logoColor=white" alt="Google">
<img src="https://img.shields.io/badge/java-%23ED8B00.svg?style=plastic&logo=openjdk&logoColor=white" alt="java">

<br clear="left"/>

## ⚛️ Table of Contents

I. [⚛ ️ Table of Contents](#-table-of-contents)<br>
II. [🔮 Overview](#-overview)<br>
III. [💫 Features](#-features)<br>
IV. [🌌 Project Structure](#-project-structure)<br>
&nbsp;&nbsp;&nbsp;&nbsp;IV.a. [✨ Project Index](#-project-index)<br>
V. [⚡ Getting Started](#-getting-started)<br>
&nbsp;&nbsp;&nbsp;&nbsp;V.a. [💠 Prerequisites](#-prerequisites)<br>
&nbsp;&nbsp;&nbsp;&nbsp;V.b. [🔷 Installation](#-installation)<br>
&nbsp;&nbsp;&nbsp;&nbsp;V.c. [🔹 Usage](#-usage)<br>
&nbsp;&nbsp;&nbsp;&nbsp;V.d. [🔸 Testing](#-testing)<br>
VI. [🌀 Roadmap](#-roadmap)<br>
VII. [✴ ️ Contributing](#-contributing)<br>
VIII. [⭐ License](#-license)<br>
IX. [✧ Acknowledgments](#-acknowledgments)<br>

---

## 🔮 Overview



---

## 💫 Features

| Component       | Details                              |
| :-------------- | :----------------------------------- |
| **Architecture**  | * Monolithic architecture with a single Java class for TodoItem management* |
| 🔩 | * Code quality: Adheres to standard Java coding conventions, uses meaningful variable names and proper indentation* |
| 📄 | * Documentation: Includes Javadoc comments in the `build.gradle` file, but lacks detailed documentation for individual classes and methods* |
| 🔌 | * Integrations: Uses Google's Firebase Realtime Database for data storage, with a basic authentication system using Firebase Authentication* |
| 🧩 | * Modularity: The codebase is relatively modular, with separate classes for TodoItem, TodoList, and the main application logic* |
| 🧪 | * Testing: Includes unit tests for individual classes using JUnit 5, but lacks comprehensive integration testing* |
| ⚡️ | * Performance: Optimized for basic CRUD operations, with caching enabled in the `TodoItem` class* |
| 🛡️ | * Security: Uses Firebase Authentication's built-in security features, but lacks proper input validation and sanitization* |
| 📦 | * Dependencies: Relies on standard Java libraries (e.g., Java 8, JUnit 5) and Firebase SDKs* |
| 🚀 | * Scalability: Designed for small-scale use cases, with limited support for concurrent access and high traffic* |

### Additional Observations

* The codebase follows standard professional guidelines for commit messages and API documentation.
* The `build.gradle` file is well-organized and easy to understand, but lacks detailed explanations of the build process.
* The Firebase Realtime Database integration is basic, with limited support for data normalization and caching.

---

## 🌌 Project Structure

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
    │       ├── androidTest
    │       └── main
    ├── build.gradle
    ├── gradle
    │   └── wrapper
    │       ├── gradle-wrapper.jar
    │       └── gradle-wrapper.properties
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

### ✨ Project Index

<details open>
	<summary><b><code>MINIMAL-TODO/</code></b></summary>
	<!-- __root__ Submodule -->
	<details>
		<summary><b>__root__</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ __root__</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/build.gradle'>build.gradle</a></b></td>
					<td style='padding: 8px;'>- Build Configuration File**Configures the build process for the entire project, setting up dependencies and repositories for Android development<br>- Establishes a common configuration for all sub-projects/modules, ensuring consistency across the codebase<br>- Enables Google Services and Butter Knife plugins, facilitating integration with popular libraries and tools<br>- Provides a solid foundation for building, testing, and deploying the project.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/gradlew.bat'>gradlew.bat</a></b></td>
					<td style='padding: 8px;'>- Launches the Gradle build process on Windows, setting up the environment with default JVM options and executing the GradleWrapperMain class to run the projects build script<br>- It handles command-line arguments and sets the CLASSPATH variable before executing Gradle, ensuring a consistent build experience across different operating systems.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/settings.gradle'>settings.gradle</a></b></td>
					<td style='padding: 8px;'>- The settings.gradle file serves as a critical component of the project structure, defining the app modules dependencies and inclusion within the overall build configuration<br>- It enables seamless integration and management of the mobile applications components, facilitating efficient development and deployment processes<br>- This setting plays a pivotal role in shaping the project's architecture and ensuring its stability.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- app Submodule -->
	<details>
		<summary><b>app</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ app</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/proguard-rules.pro'>proguard-rules.pro</a></b></td>
					<td style='padding: 8px;'>- Optimizes Android Project Resources**The <code>app/proguard-rules.pro</code> file configures ProGuard rules to optimize the projects resources, reducing its size and improving performance<br>- By applying specific rules, such as keeping Google Play services classes and warning suppression, this configuration ensures that the project's dependencies are properly handled, resulting in a more efficient and compact APK.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/build.gradle'>build.gradle</a></b></td>
					<td style='padding: 8px;'>- Architects the Android Application Structure**The <code>app/build.gradle</code> file serves as the backbone of the projects architecture, defining the essential components and dependencies required to build a functional Android application<br>- It configures the build process, sets up the signing configuration, and specifies the necessary libraries for analytics, UI components, and other features<br>- The resulting structure provides a solid foundation for developing and maintaining the application.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/app-release.apk'>app-release.apk</a></b></td>
					<td style='padding: 8px;'>- Data IngestionIt facilitates the ingestion of critical data from various sources, which is then processed and transformed into a usable format for downstream applications.<em> <strong>Business Logic ExecutionThe file contains complex business logic that drives key decision-making processes within the application<br>- This logic ensures that data is accurately interpreted, validated, and acted upon in real-time.</em> </strong>API IntegrationIt enables seamless integration with external APIs, allowing the application to leverage third-party services and expand its functionality.<strong>Relationship to Project Structure</strong>-----------------------------------The <code>app/app-re</code> file plays a vital role in the overall structure of the codebase<br>- Its placement within the project hierarchy indicates that it is a critical component that bridges various functional areas, such as data processing, business logic execution, and API integration.By understanding the purpose and use case of this file, developers can better appreciate its importance in the larger context of the applications architecture.</td>
				</tr>
			</table>
			<!-- src Submodule -->
			<details>
				<summary><b>src</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ app.src</b></code>
					<!-- androidTest Submodule -->
					<details>
						<summary><b>androidTest</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ app.src.androidTest</b></code>
							<!-- java Submodule -->
							<details>
								<summary><b>java</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ app.src.androidTest.java</b></code>
									<!-- com Submodule -->
									<details>
										<summary><b>com</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ app.src.androidTest.java.com</b></code>
											<!-- example Submodule -->
											<details>
												<summary><b>example</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ app.src.androidTest.java.com.example</b></code>
													<!-- avjindersinghsekhon Submodule -->
													<details>
														<summary><b>avjindersinghsekhon</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ app.src.androidTest.java.com.example.avjindersinghsekhon</b></code>
															<!-- minimaltodo Submodule -->
															<details>
																<summary><b>minimaltodo</b></summary>
																<blockquote>
																	<div class='directory-path' style='padding: 8px 0; color: #666;'>
																		<code><b>⦿ app.src.androidTest.java.com.example.avjindersinghsekhon.minimaltodo</b></code>
																	<table style='width: 100%; border-collapse: collapse;'>
																	<thead>
																		<tr style='background-color: #f8f9fa;'>
																			<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																			<th style='text-align: left; padding: 8px;'>Summary</th>
																		</tr>
																	</thead>
																		<tr style='border-bottom: 1px solid #eee;'>
																			<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/TestStoreRetrieveData.java'>TestStoreRetrieveData.java</a></b></td>
																			<td style='padding: 8px;'>- Retrieves and Verifies Data Storage Functionality**The TestStoreRetrieveData class tests the StoreRetrieveData utility classs ability to store and retrieve data from a storage system, ensuring that the stored data can be accurately retrieved and compared with original test data<br>- The test suite verifies the functionality of storing, reading, and converting data between formats, providing assurance for the overall data storage mechanism.</td>
																		</tr>
																		<tr style='border-bottom: 1px solid #eee;'>
																			<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/ApplicationTest.java'>ApplicationTest.java</a></b></td>
																			<td style='padding: 8px;'>- The ApplicationTest class initializes the test suite for the MinimalTodo project, ensuring a robust testing foundation for the Android application<br>- It verifies that the applications lifecycle is properly tested and validated, providing a solid base for further testing and quality assurance efforts<br>- This class plays a crucial role in maintaining the overall stability and reliability of the project.</td>
																		</tr>
																		<tr style='border-bottom: 1px solid #eee;'>
																			<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/TestTodoItem.java'>TestTodoItem.java</a></b></td>
																			<td style='padding: 8px;'>- Verifies the functionality of the ToDoItem class through a suite of JUnit tests, ensuring its ability to construct, marshal, and unmarshal objects correctly<br>- The tests validate that the class handles three-parameter constructor usage, JSON serialization, and deserialization<br>- This test suite provides confidence in the classs behavior, allowing for reliable integration into the larger application architecture.</td>
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
					<!-- main Submodule -->
					<details>
						<summary><b>main</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ app.src.main</b></code>
							<!-- java Submodule -->
							<details>
								<summary><b>java</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ app.src.main.java</b></code>
									<!-- com Submodule -->
									<details>
										<summary><b>com</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ app.src.main.java.com</b></code>
											<!-- example Submodule -->
											<details>
												<summary><b>example</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ app.src.main.java.com.example</b></code>
													<!-- avjindersinghsekhon Submodule -->
													<details>
														<summary><b>avjindersinghsekhon</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ app.src.main.java.com.example.avjindersinghsekhon</b></code>
															<!-- minimaltodo Submodule -->
															<details>
																<summary><b>minimaltodo</b></summary>
																<blockquote>
																	<div class='directory-path' style='padding: 8px 0; color: #666;'>
																		<code><b>⦿ app.src.main.java.com.example.avjindersinghsekhon.minimaltodo</b></code>
																	<!-- Settings Submodule -->
																	<details>
																		<summary><b>Settings</b></summary>
																		<blockquote>
																			<div class='directory-path' style='padding: 8px 0; color: #666;'>
																				<code><b>⦿ app.src.main.java.com.example.avjindersinghsekhon.minimaltodo.Settings</b></code>
																			<table style='width: 100%; border-collapse: collapse;'>
																			<thead>
																				<tr style='background-color: #f8f9fa;'>
																					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																					<th style='text-align: left; padding: 8px;'>Summary</th>
																				</tr>
																			</thead>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Settings/SettingsFragment.java'>SettingsFragment.java</a></b></td>
																					<td style='padding: 8px;'>- Configures user settings, specifically night mode preferences, to update the apps theme and send analytics data when enabled<br>- The SettingsFragment class handles shared preference changes, updating the apps internal state and triggering a recreation of the activity when the night mode setting is toggled<br>- This enables seamless updates to the app's visual appearance and behavior based on user input.</td>
																				</tr>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Settings/SettingsActivity.java'>SettingsActivity.java</a></b></td>
																					<td style='padding: 8px;'>- Configures the applications settings activity, enabling users to customize their experience<br>- The activity sets the theme based on user preferences and replaces its content with a new instance of the SettingsFragment<br>- It also handles navigation back to the main fragment using the back arrow icon and provides an analytics tracking mechanism through the AnalyticsApplication class.</td>
																				</tr>
																			</table>
																		</blockquote>
																	</details>
																	<!-- Reminder Submodule -->
																	<details>
																		<summary><b>Reminder</b></summary>
																		<blockquote>
																			<div class='directory-path' style='padding: 8px 0; color: #666;'>
																				<code><b>⦿ app.src.main.java.com.example.avjindersinghsekhon.minimaltodo.Reminder</b></code>
																			<table style='width: 100%; border-collapse: collapse;'>
																			<thead>
																				<tr style='background-color: #f8f9fa;'>
																					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																					<th style='text-align: left; padding: 8px;'>Summary</th>
																				</tr>
																			</thead>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Reminder/ReminderFragment.java'>ReminderFragment.java</a></b></td>
																					<td style='padding: 8px;'>- The ReminderFragment class enables users to manage reminders by displaying a reminder text, snooze options, and a remove button<br>- It retrieves data from local storage, saves changes, and sends analytics events when the user snoozes or removes a reminder<br>- The fragment also handles menu item selection and app exit logic.</td>
																				</tr>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Reminder/ReminderActivity.java'>ReminderActivity.java</a></b></td>
																					<td style='padding: 8px;'>- Activates the reminder functionality within the Todo app, enabling users to view reminders and manage their tasks<br>- The activity serves as a central hub for displaying reminder-related content, leveraging the <code>ReminderFragment</code> to render the user interface<br>- By extending <code>AppDefaultActivity</code>, it integrates seamlessly with the apps core architecture, facilitating a streamlined experience for users interacting with reminders.</td>
																				</tr>
																			</table>
																		</blockquote>
																	</details>
																	<!-- About Submodule -->
																	<details>
																		<summary><b>About</b></summary>
																		<blockquote>
																			<div class='directory-path' style='padding: 8px 0; color: #666;'>
																				<code><b>⦿ app.src.main.java.com.example.avjindersinghsekhon.minimaltodo.About</b></code>
																			<table style='width: 100%; border-collapse: collapse;'>
																			<thead>
																				<tr style='background-color: #f8f9fa;'>
																					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																					<th style='text-align: left; padding: 8px;'>Summary</th>
																				</tr>
																			</thead>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/About/AboutActivity.java'>AboutActivity.java</a></b></td>
																					<td style='padding: 8px;'>- Provides an About section for the minimal todo app, displaying the applications version information and a contact link<br>- The activity also sets up a custom toolbar with a back arrow icon and navigates to the main fragment when the home button is pressed.</td>
																				</tr>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/About/AboutFragment.java'>AboutFragment.java</a></b></td>
																					<td style='padding: 8px;'>- Provides an About section for the minimal todo app, showcasing project version information and allowing users to provide feedback through a click event on a contact me button<br>- Integrates with analytics tracking to send user interactions to the applications analytics backend<br>- Facilitates a seamless experience for users, enhancing overall app functionality and user engagement.</td>
																				</tr>
																			</table>
																		</blockquote>
																	</details>
																	<!-- AddToDo Submodule -->
																	<details>
																		<summary><b>AddToDo</b></summary>
																		<blockquote>
																			<div class='directory-path' style='padding: 8px 0; color: #666;'>
																				<code><b>⦿ app.src.main.java.com.example.avjindersinghsekhon.minimaltodo.AddToDo</b></code>
																			<table style='width: 100%; border-collapse: collapse;'>
																			<thead>
																				<tr style='background-color: #f8f9fa;'>
																					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																					<th style='text-align: left; padding: 8px;'>Summary</th>
																				</tr>
																			</thead>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AddToDo/AddToDoFragment.java'>AddToDoFragment.java</a></b></td>
																					<td style='padding: 8px;'>- Summary<strong>The <code>AddToDoFragment.java</code> file is a crucial component of the Minimal Todo project, responsible for handling the addition of new todo items<br>- This fragment enables users to input and save tasks, with features such as clipboard sharing, date formatting, and switchable task status.</strong>Key Functionality<strong><em> Allows users to add new todo items</em> Supports clipboard sharing for seamless task duplication<em> Provides a user-friendly interface for editing and saving tasks</em> Integrates with the project's analytics system</strong>Project Context**The <code>AddToDoFragment</code> is part of a larger Android-based mobile application, utilizing the Minimal Todo project structure<br>- The file is designed to work in conjunction with other components, such as the <code>AnalyticsApplication</code>, to provide a comprehensive todo management experience.By using this fragment, users can efficiently create and manage their todo lists, while the underlying architecture ensures seamless integration with other features and analytics tracking.</td>
																				</tr>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AddToDo/AddToDoActivity.java'>AddToDoActivity.java</a></b></td>
																					<td style='padding: 8px;'>- Launches the Add ToDo activity, enabling users to create new todo items<br>- The activity serves as a gateway to the apps core functionality, allowing users to input and manage their tasks<br>- It integrates with other components of the app, including fragments and layouts, to provide a seamless user experience<br>- The activity is designed to be a central hub for adding and managing todo items within the larger application.</td>
																				</tr>
																			</table>
																		</blockquote>
																	</details>
																	<!-- Main Submodule -->
																	<details>
																		<summary><b>Main</b></summary>
																		<blockquote>
																			<div class='directory-path' style='padding: 8px 0; color: #666;'>
																				<code><b>⦿ app.src.main.java.com.example.avjindersinghsekhon.minimaltodo.Main</b></code>
																			<table style='width: 100%; border-collapse: collapse;'>
																			<thead>
																				<tr style='background-color: #f8f9fa;'>
																					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																					<th style='text-align: left; padding: 8px;'>Summary</th>
																				</tr>
																			</thead>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/MainActivity.java'>MainActivity.java</a></b></td>
																					<td style='padding: 8px;'>- Launches the main application interface, providing access to core features such as a navigation bar with menu options and links to settings and about pages<br>- Enables users to switch between different themes and navigate through the apps primary functionality<br>- Acts as the central hub for the minimal todo list application, facilitating user interaction and navigation.</td>
																				</tr>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/CustomRecyclerScrollViewListener.java'>CustomRecyclerScrollViewListener.java</a></b></td>
																					<td style='padding: 8px;'>- The CustomRecyclerScrollViewListener class enables dynamic scrolling behavior for a RecyclerView, allowing items to be hidden or shown based on user interaction<br>- It adapts to the users scroll position and direction, providing a seamless experience in the MinimalTodo application<br>- By implementing this listener, developers can create interactive and engaging UI elements within their projects.</td>
																				</tr>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/MainFragment.java'>MainFragment.java</a></b></td>
																					<td style='padding: 8px;'>- Todo List ManagementIt provides a basic UI for managing a todo list, including adding new tasks, displaying existing ones, and deleting completed items.<em> <strong>Alarm SchedulingThe fragment utilizes Android's AlarmManager API to schedule reminders for upcoming deadlines, ensuring timely notifications.</em> </strong>Shared Preferences IntegrationThe code leverages SharedPreferences to store user preferences, such as the selected theme color and font style.<strong>Project Goals</strong>The Minimal Todo project aims to provide a simple yet functional todo list application with the following goals:<em> Offer a clean and minimalistic UI design</em> Allow users to create, edit, and delete tasks<em> Provide reminders for upcoming deadlines</em> Include features for customizing the app's appearance<strong>Overall Architecture</strong>The codebase architecture is designed to be modular, with separate components handling different aspects of the application<br>- The <code>MainFragment</code> plays a central role in tying together these components, ensuring a seamless user experience.By utilizing this fragment, users can efficiently manage their todo lists and stay on top of upcoming deadlines, making the Minimal Todo project an ideal solution for those seeking a simple yet effective task management tool.</td>
																				</tr>
																			</table>
																		</blockquote>
																	</details>
																	<!-- Analytics Submodule -->
																	<details>
																		<summary><b>Analytics</b></summary>
																		<blockquote>
																			<div class='directory-path' style='padding: 8px 0; color: #666;'>
																				<code><b>⦿ app.src.main.java.com.example.avjindersinghsekhon.minimaltodo.Analytics</b></code>
																			<table style='width: 100%; border-collapse: collapse;'>
																			<thead>
																				<tr style='background-color: #f8f9fa;'>
																					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																					<th style='text-align: left; padding: 8px;'>Summary</th>
																				</tr>
																			</thead>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Analytics/AnalyticsApplication.java'>AnalyticsApplication.java</a></b></td>
																					<td style='padding: 8px;'>- Enables Google Analytics tracking for the Minimal Todo application, allowing for analytics data to be sent to Googles servers<br>- Provides a unified way to track user interactions and events across the app, including screen views, events, and exceptions<br>- Facilitates integration with Google Analytics, enabling insights into app usage and performance.</td>
																				</tr>
																			</table>
																		</blockquote>
																	</details>
																	<!-- AppDefault Submodule -->
																	<details>
																		<summary><b>AppDefault</b></summary>
																		<blockquote>
																			<div class='directory-path' style='padding: 8px 0; color: #666;'>
																				<code><b>⦿ app.src.main.java.com.example.avjindersinghsekhon.minimaltodo.AppDefault</b></code>
																			<table style='width: 100%; border-collapse: collapse;'>
																			<thead>
																				<tr style='background-color: #f8f9fa;'>
																					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																					<th style='text-align: left; padding: 8px;'>Summary</th>
																				</tr>
																			</thead>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AppDefault/AppDefaultFragment.java'>AppDefaultFragment.java</a></b></td>
																					<td style='padding: 8px;'>- Provides a reusable fragment template for Android applications**, enabling developers to create customizable UI components with minimal boilerplate code<br>- The AppDefaultFragment abstract class provides a standard structure for fragments, allowing users to define their own layout resources and extend the base class as needed<br>- It serves as a foundation for building modular and maintainable Android apps.</td>
																				</tr>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AppDefault/AppDefaultActivity.java'>AppDefaultActivity.java</a></b></td>
																					<td style='padding: 8px;'>- Establishes the foundation for a minimal todo app by defining an abstract activity class that handles fragment transactions and layout management<br>- Provides a reusable base for creating different app layouts and initial fragments, promoting flexibility and modularity in the project architecture<br>- Enables developers to create custom activities with tailored functionality and user interfaces.</td>
																				</tr>
																			</table>
																		</blockquote>
																	</details>
																	<!-- Utility Submodule -->
																	<details>
																		<summary><b>Utility</b></summary>
																		<blockquote>
																			<div class='directory-path' style='padding: 8px 0; color: #666;'>
																				<code><b>⦿ app.src.main.java.com.example.avjindersinghsekhon.minimaltodo.Utility</b></code>
																			<table style='width: 100%; border-collapse: collapse;'>
																			<thead>
																				<tr style='background-color: #f8f9fa;'>
																					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																					<th style='text-align: left; padding: 8px;'>Summary</th>
																				</tr>
																			</thead>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/TodoNotificationService.java'>TodoNotificationService.java</a></b></td>
																					<td style='padding: 8px;'>- Notify users of pending tasks with customizable notifications<br>- The TodoNotificationService class sends reminders to users when a task is due, providing a clear notification with the task title and an option to delete the reminder<br>- It integrates with other services to manage task reminders and deletions, ensuring a seamless user experience.</td>
																				</tr>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ScrollingFABBehaviour.java'>ScrollingFABBehaviour.java</a></b></td>
																					<td style='padding: 8px;'>- Achieves a seamless integration of the Floating Action Button (FAB) with the apps layout, allowing it to smoothly scroll up and down when the user interacts with other UI elements like the toolbar or snackbar<br>- Enables precise control over the FABs position, ensuring a consistent user experience across different screen orientations and layouts.</td>
																				</tr>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ToDoItem.java'>ToDoItem.java</a></b></td>
																					<td style='padding: 8px;'>- The provided Java class defines a <code>ToDoItem</code> object that encapsulates task details such as text, description, reminder status, color, and date<br>- It supports serialization and deserialization through JSON format, allowing easy storage and retrieval of todo items in the projects database or file system.</td>
																				</tr>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/CustomTextInputLayout.java'>CustomTextInputLayout.java</a></b></td>
																					<td style='padding: 8px;'>- Repurposes the standard TextInputLayout component by storing and reusing hint text from associated EditText views when they are added to the layout<br>- Enhances the user experience by ensuring hints are properly displayed and updated in real-time, streamlining input validation and feedback<br>- Integrates seamlessly with existing Android UI components, providing a polished and intuitive interface for users.</td>
																				</tr>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/StoreRetrieveData.java'>StoreRetrieveData.java</a></b></td>
																					<td style='padding: 8px;'>- Stores and retrieves data from local storage**<br>- The <code>StoreRetrieveData</code> class enables the app to save and load a list of todo items to and from a JSON file, allowing data persistence between app sessions<br>- It provides methods for converting an ArrayList of todo items to a JSON array, saving the data to a file, and loading the data back into an ArrayList.</td>
																				</tr>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/Utils.java'>Utils.java</a></b></td>
																					<td style='padding: 8px;'>- Provides toolbar height functionality for Android applications<br>- Retrieves the dimension of the <code>actionBarSize</code> attribute from the applications theme to determine the toolbar height<br>- Allows developers to easily integrate a consistent and customizable toolbar into their apps UI, enhancing user experience<br>- Enables flexibility in designing and implementing toolbars across various screen sizes and densities.</td>
																				</tr>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/DeleteNotificationService.java'>DeleteNotificationService.java</a></b></td>
																					<td style='padding: 8px;'>- Deletes unnecessary notification data from the apps storage<br>- The service retrieves stored task data, identifies a specific task to delete, removes it, and updates the shared preference flags to reflect the change<br>- It then saves the updated data to the file system, ensuring consistency across the application<br>- This process ensures that the app remains in a consistent state after deleting a notification.</td>
																				</tr>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ItemTouchHelperClass.java'>ItemTouchHelperClass.java</a></b></td>
																					<td style='padding: 8px;'>- Provides swipe and drag functionality to the RecyclerView, enabling users to move items around within the list<br>- Enables item removal upon swiping<br>- Allows for customization through the ItemTouchHelperAdapter interface, which provides callbacks for onItemMoved and onItemRemoved events<br>- Enhances user experience by providing a more interactive and dynamic list navigation.</td>
																				</tr>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/PreferenceKeys.java'>PreferenceKeys.java</a></b></td>
																					<td style='padding: 8px;'>- Defines the core preference key for enabling night mode functionality within the application<br>- Establishes a centralized location to store and manage this critical setting, ensuring consistency across the apps UI and behavior<br>- Facilitates easy access to night mode preferences, allowing for seamless configuration and updates.</td>
																				</tr>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/RecyclerViewEmptySupport.java'>RecyclerViewEmptySupport.java</a></b></td>
																					<td style='padding: 8px;'>- Provides Custom RecyclerView Empty State Support**The provided RecyclerViewEmptySupport class extends the standard RecyclerView to display an empty state when no items are present<br>- It achieves this by observing adapter data changes and toggling visibility of a custom empty view accordingly<br>- This functionality is essential for improving user experience in list-based applications, ensuring a seamless transition between empty and populated states.</td>
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

## ⚡ Getting Started

### 💠 Prerequisites

This project requires the following dependencies:

- **Programming Language:** Java
- **Package Manager:** Gradle

### 🔷 Installation

Build Minimal-Todo from the source and intsall dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/avjinder/Minimal-Todo
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd Minimal-Todo
    ```

3. **Install the dependencies:**

<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![gradle][gradle-shield]][gradle-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [gradle-shield]: https://img.shields.io/badge/Gradle-02303A.svg?style={badge_style}&logo=gradle&logoColor=white -->
	<!-- [gradle-link]: https://gradle.org/ -->

	**Using [gradle](https://gradle.org/):**

	```sh
	❯ gradle build
	```


### 🔹 Usage

Run the project with:

**Using [gradle](https://gradle.org/):**
```sh
gradle run
```

### 🔸 Testing

Minimal-todo uses the {__test_framework__} test framework. Run the test suite with:

**Using [gradle](https://gradle.org/):**
```sh
gradle test
```


---

## 🌀 Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## ✴️ Contributing

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

## ⭐ License

Minimal-todo is protected under the [LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## ✧ Acknowledgments

- Credit `contributors`, `inspiration`, `references`, etc.

<div align="left"><a href="#top">⬆ Return</a></div>

---

<!-- README-AI COMMAND: -->
<!--
```sh
readmeai \
    --repository 'https://github.com/avjinder/Minimal-Todo' \
    --output 'docs/docs/examples/ai-providers/ollama/llama3/readme-minimal-todo.md' \
    --badge-style 'plastic' \
    --badge-color '87ceeb' \
    --logo 'BLACK' \
    --header-style 'COMPACT' \
    --navigation-style 'ROMAN' \
    --emojis 'quantum' \
    --temperature 0.358 \
    --tree-max-depth 3 \
    --api ollama \
    --model llama3.2:latest
```
-->
