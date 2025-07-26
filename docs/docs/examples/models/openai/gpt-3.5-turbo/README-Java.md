<div id="top">

<!-- HEADER STYLE: ASCII -->
<div align="center">
<pre>
██   ██ ██████ ██   ██ ██████ ██   ██   ██   ██            ██████  ████  ████    ████
███ ███   ██   ███  ██   ██   ███ ███  ████  ██              ██   ██  ██ ██  ██ ██  ██
██ █ ██   ██   ██ █ ██   ██   ██ █ ██ ██  ██ ██     ██████   ██   ██  ██ ██  ██ ██  ██
██   ██   ██   ██  ███   ██   ██   ██ ██████ ██              ██   ██  ██ ██  ██ ██  ██
██   ██ ██████ ██   ██ ██████ ██   ██ ██  ██ ██████          ██    ████  ████    ████
</pre>
</div>
<div align="center">

<em>Effortless task management for maximum productivity and focus.</em>

<!-- BADGES -->
<img src="https://img.shields.io/github/license/avjinder/Minimal-Todo?style=plastic&logo=opensourceinitiative&logoColor=white&color=4169e1" alt="license">
<img src="https://img.shields.io/github/last-commit/avjinder/Minimal-Todo?style=plastic&logo=git&logoColor=white&color=4169e1" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/avjinder/Minimal-Todo?style=plastic&color=4169e1" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/avjinder/Minimal-Todo?style=plastic&color=4169e1" alt="repo-language-count">

<em>Technology Stack:</em>

<img src="https://img.shields.io/badge/Android-34A853.svg?style=plastic&logo=Android&logoColor=white" alt="Android">
<img src="https://img.shields.io/badge/Gradle-02303A.svg?style=plastic&logo=Gradle&logoColor=white" alt="Gradle">
<img src="https://img.shields.io/badge/Google-4285F4.svg?style=plastic&logo=Google&logoColor=white" alt="Google">
<img src="https://img.shields.io/badge/java-%23ED8B00.svg?style=plastic&logo=openjdk&logoColor=white" alt="java">

</div>
<br>

## ⬜ Table of Contents

- [⬜ Table of Contents](#-table-of-contents)
- [◽ Overview](#-overview)
- [⚪ Features](#-features)
- [◻ ️ Project Structure](#-project-structure)
    - [⬚ Project Index](#-project-index)
- [▫ ️ Getting Started](#-getting-started)
    - [⬛ Prerequisites](#-prerequisites)
    - [◾ Installation](#-installation)
    - [⚫ Usage](#-usage)
    - [◼ ️ Testing](#-testing)
- [🔲 Roadmap](#-roadmap)
- [🔳 Contributing](#-contributing)
- [⬛ License](#-license)
- [✧ Acknowledgments](#-acknowledgments)

---

## ◽ Overview

**Why Minimal-Todo?**

This project simplifies Android app development by offering efficient build configurations and comprehensive testing capabilities. The core features include:

- **🔒 Secure Code Optimization:** Enhance app security and performance with ProGuard rules.
- **🛠️ Efficient Build Setup:** Streamline development workflow with optimized build configurations.
- **🧪 Comprehensive Testing:** Ensure data integrity and core functionality through robust testing.
- **🎨 User-Friendly Settings:** Customize app themes and preferences seamlessly.

---

## ⚪ Features

|      | Component       | Details                              |
| :--- | :-------------- | :----------------------------------- |
| ⚙️  | **Architecture**  | <ul><li>Follows MVP (Model-View-Presenter) architecture pattern</li><li>Clear separation of concerns between data, presentation, and business logic</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Consistent coding style and formatting</li><li>Uses meaningful variable and function names</li></ul> |
| 📄 | **Documentation** | <ul><li>Minimal inline comments within code</li><li>Lacks comprehensive external documentation</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integrates with Gradle for build automation</li><li>Uses ProGuard for code obfuscation</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Organized project structure with separate modules for features</li><li>Reusable components and utilities</li></ul> |
| 🧪 | **Testing**       | <ul><li>Includes unit tests for critical components</li><li>Uses JUnit and Mockito for testing</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Efficient handling of data retrieval and processing</li><li>Smooth UI interactions with minimal lag</li></ul> |
| 🛡️ | **Security**      | <ul><li>Implements basic security measures like code obfuscation</li><li>No evident security vulnerabilities in the codebase</li></ul> |
| 📦 | **Dependencies**  | <ul><li>Relies on standard Android dependencies like 'com.android.support:appcompat-v7'</li><li>Uses third-party libraries for additional functionality</li></ul> |

---

## ◻️ Project Structure

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

### ⬚ Project Index

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
					<td style='padding: 8px;'>- Define common build configurations and dependencies for all sub-projects<br>- Set up repositories for jcenter, mavenCentral, and Google<br>- Include classpaths for Gradle, Google Services, and ButterKnife<br>- Ensure proper dependency management in individual module build.gradle files.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/gradlew.bat'>gradlew.bat</a></b></td>
					<td style='padding: 8px;'>- Facilitates Gradle setup and execution on Windows systems by locating Java and running Gradle tasks with specified options<br>- Handles JAVA_HOME configuration and command-line arguments for seamless Gradle operations.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/settings.gradle'>settings.gradle</a></b></td>
					<td style='padding: 8px;'>Define the project structure by including the app module in the settings.gradle file.</td>
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
					<td style='padding: 8px;'>- Define project-specific ProGuard rules to optimize and secure the Android app by specifying classes to keep and avoid warnings<br>- These rules enhance app performance and protect sensitive code during the build process.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/build.gradle'>build.gradle</a></b></td>
					<td style='padding: 8px;'>- Configure Android application settings, including version details, dependencies, and build configurations<br>- Set up signing configurations and integrate Google services<br>- This file plays a crucial role in defining the apps behavior, appearance, and functionality within the Android ecosystem.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/app-release.apk'>app-release.apk</a></b></td>
					<td style='padding: 8px;'>- The <code>app-re</code> file in the project serves as a crucial component within the application architecture<br>- It plays a pivotal role in managing and orchestrating various functionalities within the app<br>- By leveraging the capabilities of this file, the codebase can efficiently handle key processes and ensure seamless interactions across different modules<br>- Its implementation significantly contributes to the overall robustness and effectiveness of the applications architecture.</td>
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
																			<td style='padding: 8px;'>- TestStoreRetrieveData validates data storage functionality by writing and reading items, ensuring data integrity<br>- It also tests JSON array conversion<br>- This file sets up test data, saves and retrieves items, and confirms content match<br>- The class guarantees proper data handling within the application.</td>
																		</tr>
																		<tr style='border-bottom: 1px solid #eee;'>
																			<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/ApplicationTest.java'>ApplicationTest.java</a></b></td>
																			<td style='padding: 8px;'>- Test the Android applications core functionality by extending the ApplicationTestCase class in the provided file<br>- This test ensures that the application behaves as expected under various scenarios.</td>
																		</tr>
																		<tr style='border-bottom: 1px solid #eee;'>
																			<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/TestTodoItem.java'>TestTodoItem.java</a></b></td>
																			<td style='padding: 8px;'>- Verify functionality of ToDoItem class through JUnit tests<br>- Test construction using a three-parameter constructor, marshalling ToDoItem objects to JSON, and unmarshalling from JSON data<br>- Ensure accuracy in text, reminder status, and date<br>- Maintain integrity of ToDoItem attributes during object creation and JSON conversion.</td>
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
																					<td style='padding: 8px;'>- Manage user preferences and settings within the application<br>- Detect changes in preferences, such as night mode selection, and dynamically update the apps theme accordingly<br>- Utilizes SharedPreferences for data persistence and integrates with Google Analytics for tracking user interactions<br>- This fragment enhances user experience by providing customizable visual options.</td>
																				</tr>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Settings/SettingsActivity.java'>SettingsActivity.java</a></b></td>
																					<td style='padding: 8px;'>- Manage settings and themes for the Minimal Todo app<br>- Control the apps appearance based on user preferences, offering both light and dark themes<br>- Enable navigation back to the main screen using a customized toolbar<br>- Integrate analytics tracking for user interactions within the settings activity.</td>
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
																					<td style='padding: 8px;'>- Handles displaying and managing reminders for to-do items<br>- Allows users to remove to-dos, set snooze options, and mark tasks as done with time adjustments<br>- Implements data saving and app closing functionalities.</td>
																				</tr>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Reminder/ReminderActivity.java'>ReminderActivity.java</a></b></td>
																					<td style='padding: 8px;'>- Create ReminderActivity to handle Reminder feature<br>- Extends AppDefaultActivity to set layout and initialize fragment<br>- ReminderFragment is instantiated as the initial fragment.</td>
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
																					<td style='padding: 8px;'>- Implement the AboutActivity class to manage the About sections functionality within the app<br>- It handles displaying app version information, setting the theme based on user preferences, and enabling navigation back to the main screen<br>- This class extends AppDefaultActivity and integrates with the apps toolbar and fragments for a seamless user experience.</td>
																				</tr>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/About/AboutFragment.java'>AboutFragment.java</a></b></td>
																					<td style='padding: 8px;'>- Describe the purpose and use of the AboutFragment.java file within the project architecture<br>- The file implements an About screen, displaying app version information and contact details<br>- It integrates with Analytics for tracking user interactions<br>- This fragment serves as a key component for providing essential app information and feedback options to users.</td>
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
																					<td style='padding: 8px;'>- The AddToDoFragment.java file in the project is responsible for managing the user interface and interactions related to adding a new to-do item<br>- It handles various user inputs such as text entry, date selection, and priority setting<br>- Additionally, it provides functionality for sharing to-do items and managing reminders<br>- This file plays a crucial role in enhancing the user experience by facilitating the seamless addition of tasks to the to-do list within the application.By encapsulating the logic for creating and managing new to-do items, the AddToDoFragment.java file contributes significantly to the overall functionality of the to-do application<br>- It ensures a smooth and intuitive process for users to input and organize their tasks effectively.</td>
																				</tr>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AddToDo/AddToDoActivity.java'>AddToDoActivity.java</a></b></td>
																					<td style='padding: 8px;'>- AddToDoActivity extends AppDefaultActivity, handling the creation of a new to-do item<br>- It sets the content view layout and initializes the AddToDoFragment<br>- This file plays a crucial role in the apps architecture by managing the addition of new to-dos seamlessly within the apps flow.</td>
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
																					<td style='padding: 8px;'>- Implementing the main activity for the project, MainActivity.java sets up the apps primary interface and navigation<br>- It includes functionalities like setting up the toolbar, handling menu creation, and managing item selections to navigate to different sections of the app, such as About and Settings<br>- This file plays a crucial role in defining the user interaction flow within the application.</td>
																				</tr>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/CustomRecyclerScrollViewListener.java'>CustomRecyclerScrollViewListener.java</a></b></td>
																					<td style='padding: 8px;'>- Implement a custom scroll listener for RecyclerView that toggles visibility based on scroll direction<br>- Logs show/hide actions and scroll distances<br>- The listener abstracts methods for showing and hiding content.</td>
																				</tr>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/MainFragment.java'>MainFragment.java</a></b></td>
																					<td style='padding: 8px;'>- The <code>MainFragment.java</code> file in the projects architecture is responsible for managing the main user interface components and interactions within the Minimal Todo application<br>- It handles the display of tasks, animations, and user interactions such as adding new tasks and marking tasks as complete<br>- Additionally, it integrates with system components like <code>AlarmManager</code> for task reminders and <code>SharedPreferences</code> for storing user preferences<br>- This file plays a crucial role in providing a seamless and intuitive task management experience to the users of the Minimal Todo app.### Project Structure:``<code>sh{app}└── src └── main └── java └── com └── example └── avjindersinghsekhon └── minimaltodo └── Main └── MainFragment.java</code>`<code>By encapsulating the core functionalities related to task management and user interactions, </code>MainFragment.java` contributes significantly to the overall user experience and functionality of the Minimal Todo application.</td>
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
																					<td style='padding: 8px;'>- Implement analytics tracking for the Minimal app using Google Analytics, allowing for monitoring user interactions and behavior<br>- The <code>AnalyticsApplication.java</code> file initializes and configures the Google Analytics tracker, enabling the app to send screen views and events data for analysis.</td>
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
																					<td style='padding: 8px;'>- Define a base fragment for app screens, handling view creation and destruction<br>- This abstract class sets the layout resource for child fragments to inflate, ensuring consistency across the apps UI components.</td>
																				</tr>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AppDefault/AppDefaultActivity.java'>AppDefaultActivity.java</a></b></td>
																					<td style='padding: 8px;'>- Define a base activity handling initial fragment setup in the apps default package<br>- It sets the content view and initializes the first fragment if none exists, aiding in consistent app flow.</td>
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
																					<td style='padding: 8px;'>- Generate and display notifications for to-do items in the Android app, triggering reminders for tasks<br>- The <code>TodoNotificationService</code> class handles notification creation and management, ensuring timely alerts for users.</td>
																				</tr>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ScrollingFABBehaviour.java'>ScrollingFABBehaviour.java</a></b></td>
																					<td style='padding: 8px;'>- Implement a CoordinatorLayout behavior for a FloatingActionButton that adjusts its position based on scrolling actions with Snackbars and Toolbars<br>- This enhances the user experience by ensuring the FloatingActionButton remains visible and accessible during interactions within the apps UI components.</td>
																				</tr>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ToDoItem.java'>ToDoItem.java</a></b></td>
																					<td style='padding: 8px;'>- Define and manage ToDo items with text, description, reminder status, color, date, and unique identifier<br>- Serialize and deserialize data to/from JSON format<br>- This class encapsulates ToDo item properties for efficient handling within the application.</td>
																				</tr>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/CustomTextInputLayout.java'>CustomTextInputLayout.java</a></b></td>
																					<td style='padding: 8px;'>- CustomTextInputLayout in the Utility package manages hint behavior for EditText within a TextInputLayout<br>- It ensures that hints are correctly displayed and updated, addressing issues with hint visibility and changes<br>- This class enhances the user experience by maintaining hint consistency and clarity in the apps input fields.</td>
																				</tr>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/StoreRetrieveData.java'>StoreRetrieveData.java</a></b></td>
																					<td style='padding: 8px;'>- Manage storing and retrieving data for ToDo items within the Android app<br>- Utilizes JSON format for data serialization<br>- Allows saving ToDo items to a file and loading them back when needed<br>- Handles file operations to maintain users task list across app sessions.</td>
																				</tr>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/Utils.java'>Utils.java</a></b></td>
																					<td style='padding: 8px;'>Calculate the toolbar height for the Android apps UI using the provided context.</td>
																				</tr>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/DeleteNotificationService.java'>DeleteNotificationService.java</a></b></td>
																					<td style='padding: 8px;'>- DeleteNotificationService manages the deletion of specific to-do items within the app<br>- It retrieves the to-do item to be deleted, removes it from the list of items, and updates the data<br>- This service ensures that the apps data remains synchronized and up to date after a to-do item is deleted.</td>
																				</tr>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ItemTouchHelperClass.java'>ItemTouchHelperClass.java</a></b></td>
																					<td style='padding: 8px;'>- Implement drag-and-swipe functionality for RecyclerView items<br>- Enable users to reorder items through drag-and-drop and dismiss them with swipe gestures<br>- This class facilitates smooth interaction within the apps task list, enhancing user experience.</td>
																				</tr>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/PreferenceKeys.java'>PreferenceKeys.java</a></b></td>
																					<td style='padding: 8px;'>Define and initialize preference keys for night mode in the projects utility package.</td>
																				</tr>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='https://github.com/avjinder/Minimal-Todo/blob/master/app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/RecyclerViewEmptySupport.java'>RecyclerViewEmptySupport.java</a></b></td>
																					<td style='padding: 8px;'>- Implement a RecyclerView subclass to display an empty view when the adapter has no data<br>- The class provides methods to set the empty view and handles visibility based on adapter content.</td>
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

## ▫️ Getting Started

### ⬛ Prerequisites

This project requires the following dependencies:

- **Programming Language:** Java
- **Package Manager:** Gradle

### ◾ Installation

Build Minimal-Todo from the source and install dependencies:

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


### ⚫ Usage

Run the project with:

**Using [gradle](https://gradle.org/):**
```sh
gradle run
```

### ◼️ Testing

Minimal-todo uses the {__test_framework__} test framework. Run the test suite with:

**Using [gradle](https://gradle.org/):**
```sh
gradle test
```


---

## 🔲 Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🔳 Contributing

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

## ⬛ License

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
    --output 'docs/docs/examples/generated/tmp/readme-minimal-todo.md' \
    --badge-style 'plastic' \
    --badge-color '4169e1' \
    --logo 'METALLIC' \
    --header-style 'ASCII' \
    --navigation-style 'BULLET' \
    --emojis 'monochrome' \
    --temperature 0.414 \
    --tree-max-depth 3 \
    --api openai
```
-->
