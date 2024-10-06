<p align="center">
  <img src="https://img.icons8.com/external-tal-revivo-regular-tal-revivo/96/external-readme-is-a-easy-to-build-a-developer-hub-that-adapts-to-the-user-logo-regular-tal-revivo.png" width="20%" alt="FILE.IO-ANDROID-CLIENT-logo">
</p>
<p align="center">
    <h1 align="center">FILE.IO-ANDROID-CLIENT</h1>
</p>
<p align="center">
    <em>Unleash seamless Android file magic!</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/rumaan/file.io-Android-Client?style=flat&logo=opensourceinitiative&logoColor=white&color=009688" alt="license">
	<img src="https://img.shields.io/github/last-commit/rumaan/file.io-Android-Client?style=flat&logo=git&logoColor=white&color=009688" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/rumaan/file.io-Android-Client?style=flat&color=009688" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/rumaan/file.io-Android-Client?style=flat&color=009688" alt="repo-language-count">
</p>
<p align="center">
		<em>Built with the tools and technologies:</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/JetBrains-000000.svg?style=flat&logo=JetBrains&logoColor=white" alt="JetBrains">
	<img src="https://img.shields.io/badge/Android-34A853.svg?style=flat&logo=Android&logoColor=white" alt="Android">
	<img src="https://img.shields.io/badge/Org-77AA99.svg?style=flat&logo=Org&logoColor=white" alt="Org">
	<img src="https://img.shields.io/badge/Gradle-02303A.svg?style=flat&logo=Gradle&logoColor=white" alt="Gradle">
	<img src="https://img.shields.io/badge/Google-4285F4.svg?style=flat&logo=Google&logoColor=white" alt="Google">
	<img src="https://img.shields.io/badge/Kotlin-7F52FF.svg?style=flat&logo=Kotlin&logoColor=white" alt="Kotlin">
	<img src="https://img.shields.io/badge/java-%23ED8B00.svg?style=flat&logo=openjdk&logoColor=white" alt="java">

</p>
<br>

## 🔗 Quick Links

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🤖 Usage](#🤖-usage)
  - [🧪 Testing](#🧪-testing)
- [📌 Project Roadmap](#-project-roadmap)
- [🔰 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

The file.io-Android-Client project offers seamless file upload and management on Android devices. Users can easily upload files, view upload history, and copy shareable links. This open-source app enhances file handling efficiency for individuals seeking a user-friendly file-sharing solution.

---

## 👾 Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Follows a **MVVM** architecture pattern, separating concerns for improved maintainability.</li><li>Utilizes **Room Database** for efficient data storage and retrieval.</li><li>Integrates **WorkManager** for background tasks handling.</li><li>Employs **Dependency Injection** using **Dagger** for better code organization.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Consistent **Kotlin** coding style across the codebase.</li><li>Includes **Unit Tests** for critical functionalities.</li><li>Utilizes **ProGuard** for code obfuscation and optimization.</li><li>Follows **SOLID principles** for robust and maintainable code.</li></ul> |
| 📄 | **Documentation** | <ul><li>Comprehensive **README** file providing setup instructions and project overview.</li><li>Inline comments for **code readability** and understanding.</li><li>Usage of **KDoc** for documenting functions and classes.</li><li>Clear **ProGuard rules** for code protection.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>**Firebase** integration for analytics and crash reporting.</li><li>**Room Database** integration for local data storage.</li><li>**WorkManager** integration for background tasks.</li><li>**Fuel library** for making HTTP requests.</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Organized **package structure** for easy navigation and maintenance.</li><li>Separation of concerns using **ViewModels** and **Repositories**.</li><li>**Extensive use of extensions** to enhance functionality and maintain code cleanliness.</li><li>**Helper classes** for reusable functionalities.</li></ul> |
| 🧪 | **Testing**       | <ul><li>**Instrumented tests** for UI components and database operations.</li><li>**Unit tests** for business logic and data manipulation.</li><li>**Test classes** covering various components of the app.</li><li>**Mockito** for mocking dependencies in tests.</li></ul> |
| ⚡️  | **Performance**   | <ul><li>**Optimized RecyclerView** for smooth scrolling and performance.</li><li>**Efficient data retrieval** from Room Database for quick access.</li><li>**Asynchronous tasks** using WorkManager for improved responsiveness.</li><li>**ProGuard** configuration for code optimization.</li></ul> |
| 🛡️ | **Security**      | <ul><li>**ProGuard rules** for code obfuscation and protection.</li><li>**Secure HTTP requests** using **Fuel library**.</li><li>**Secure Room Database** operations for data integrity.</li><li>**Handling sensitive data** securely within the app.</li></ul> |

---

## 📁 Project Structure

```sh
└── file.io-Android-Client/
    ├── LICENSE
    ├── README.md
    ├── app
    │   ├── .gitignore
    │   ├── build
    │   ├── build.gradle
    │   ├── proguard-rules.pro
    │   ├── release
    │   └── src
    ├── build.gradle
    ├── gradle
    │   ├── .DS_Store
    │   └── wrapper
    ├── gradle.properties
    ├── gradlew
    ├── screenshots
    │   ├── readme.txt
    │   ├── screen1.png
    │   ├── screen2.png
    │   ├── screenshot.png
    │   └── todo-ui.png
    └── settings.gradle
```


### 📂 Project Index
<details open>
	<summary><b><code>FILE.IO-ANDROID-CLIENT/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/build.gradle'>build.gradle</a></b></td>
				<td>Configure project dependencies and repositories for Android app build using Gradle.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/settings.gradle'>settings.gradle</a></b></td>
				<td>- Defines project modules for build configuration and dependency management within the codebase architecture<br>- The "settings.gradle" file specifies the inclusion of the ":app" module, organizing the project structure and facilitating seamless integration of different components.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- screenshots Submodule -->
		<summary><b>screenshots</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/screenshots/readme.txt'>readme.txt</a></b></td>
				<td>- Facilitates project setup and configuration by providing a visual guide and essential instructions in the README file<br>- Helps users navigate the project structure and understand how to interact with the codebase effectively.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- app Submodule -->
		<summary><b>app</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/proguard-rules.pro'>proguard-rules.pro</a></b></td>
				<td>- Specifies project-specific ProGuard rules to optimize and secure the Android app during the build process<br>- Controls configuration file entities and preserves line number information for debugging stack traces<br>- Includes rules for Crashlytics integration and hides original source file names.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/build.gradle'>build.gradle</a></b></td>
				<td>- Configures Android project settings, dependencies, and plugins for the application<br>- Sets up build types, defines dependencies for various libraries, including Room, Firebase, and Gson<br>- Implements plugins for Crashlytics, Kotlin, and navigation components<br>- Handles permissions using Permission Dispatcher and includes testing dependencies.</td>
			</tr>
			</table>
			<details>
				<summary><b>release</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/release/app-release.apk'>app-release.apk</a></b></td>
						<td>- The provided code file serves as a crucial component within the project architecture, facilitating seamless integration and interaction between various modules<br>- It plays a key role in enhancing the overall functionality and performance of the codebase, contributing significantly to the project's success.</td>
					</tr>
					</table>
				</blockquote>
			</details>
			<details>
				<summary><b>build</b></summary>
				<blockquote>
					<details>
						<summary><b>outputs</b></summary>
						<blockquote>
							<details>
								<summary><b>apk</b></summary>
								<blockquote>
									<details>
										<summary><b>debug</b></summary>
										<blockquote>
											<table>
											<tr>
												<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/build/outputs/apk/debug/app-debug.apk'>app-debug.apk</a></b></td>
												<td>- The code file provided serves as a crucial component within the project structure, contributing to the overall architecture by enabling seamless communication between different modules<br>- It plays a key role in enhancing the project's functionality and ensuring efficient data flow throughout the system.</td>
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
												<summary><b>thecoolguy</b></summary>
												<blockquote>
													<details>
														<summary><b>rumaan</b></summary>
														<blockquote>
															<details>
																<summary><b>fileio</b></summary>
																<blockquote>
																	<table>
																	<tr>
																		<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/androidTest/java/com/thecoolguy/rumaan/fileio/ExampleInstrumentedTest.kt'>ExampleInstrumentedTest.kt</a></b></td>
																		<td>- Verifies app context on an Android device using Instrumented Test<br>- Executes on AndroidJUnit4 with a SmallTest filter<br>- Utilizes ActivityTestRule for MainActivity<br>- Validates app package name against expected value<br>- Ideal for ensuring correct context setup in Android testing environments.</td>
																	</tr>
																	<tr>
																		<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/androidTest/java/com/thecoolguy/rumaan/fileio/FileEntityDaoTest.java'>FileEntityDaoTest.java</a></b></td>
																		<td>- Tests the functionality of the RoomDatabase by checking the count of rows, inserting and retrieving items, and saving multiple items<br>- Verifies proper object creation and database operations, ensuring data integrity and consistency in the UploadHistoryRoomDatabase.</td>
																	</tr>
																	<tr>
																		<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/androidTest/java/com/thecoolguy/rumaan/fileio/UploadHistoryInstrumentedTest.java'>UploadHistoryInstrumentedTest.java</a></b></td>
																		<td>- Implements instrumented tests for uploading history activity, utilizing Room database for data storage<br>- Populates the database with sample items for testing purposes<br>- Includes a method to match file entities by name.</td>
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
						<summary><b>test</b></summary>
						<blockquote>
							<details>
								<summary><b>java</b></summary>
								<blockquote>
									<details>
										<summary><b>com</b></summary>
										<blockquote>
											<details>
												<summary><b>thecoolguy</b></summary>
												<blockquote>
													<details>
														<summary><b>rumaan</b></summary>
														<blockquote>
															<details>
																<summary><b>fileio</b></summary>
																<blockquote>
																	<table>
																	<tr>
																		<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/test/java/com/thecoolguy/rumaan/fileio/ExampleUnitTest.java'>ExampleUnitTest.java</a></b></td>
																		<td>Tests addition functionality to ensure correctness on the development machine.</td>
																	</tr>
																	<tr>
																		<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/test/java/com/thecoolguy/rumaan/fileio/UploadRepositoryTest.java'>UploadRepositoryTest.java</a></b></td>
																		<td>Test the expiration URL generation functionality ensuring correctness and consistency with defined constants in the codebase.</td>
																	</tr>
																	<tr>
																		<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/test/java/com/thecoolguy/rumaan/fileio/UrlTest.java'>UrlTest.java</a></b></td>
																		<td>- Tests URL parsing functionality to ensure proper extraction of the base URL from an encrypted URL<br>- This validation guarantees accurate handling of file download links within the project architecture.</td>
																	</tr>
																	<tr>
																		<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/test/java/com/thecoolguy/rumaan/fileio/FileEntityTest.java'>FileEntityTest.java</a></b></td>
																		<td>Validates FileEntity attributes setting functionality through unit tests.</td>
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
												<summary><b>thecoolguy</b></summary>
												<blockquote>
													<details>
														<summary><b>rumaan</b></summary>
														<blockquote>
															<details>
																<summary><b>fileio</b></summary>
																<blockquote>
																	<details>
																		<summary><b>viewmodel</b></summary>
																		<blockquote>
																			<table>
																			<tr>
																				<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/viewmodel/UploadHistoryViewModel.kt'>UploadHistoryViewModel.kt</a></b></td>
																				<td>- Manages live data of file upload history through a ViewModel linked to a Room Database<br>- Initializes LiveData with a list of file entities from the database, facilitating seamless data interaction in the app.</td>
																			</tr>
																			</table>
																		</blockquote>
																	</details>
																	<details>
																		<summary><b>ui</b></summary>
																		<blockquote>
																			<table>
																			<tr>
																				<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/FileioApplication.kt'>FileioApplication.kt</a></b></td>
																				<td>- Initializes application-wide configurations for logging and error handling in the Android app<br>- Sets up Timber for logging and configures a custom activity to handle crashes<br>- This class acts as the base for the application, providing essential setup during the app's lifecycle.</td>
																			</tr>
																			<tr>
																				<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/UploadHistoryListAdapter.kt'>UploadHistoryListAdapter.kt</a></b></td>
																				<td>- Enables displaying and managing upload history in a RecyclerView by populating different types of views based on the data content<br>- Supports viewing file details and copying URLs to the clipboard<br>- Facilitates swapping and removing items in the list.</td>
																			</tr>
																			<tr>
																				<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/SwipeToDeleteCallBack.kt'>SwipeToDeleteCallBack.kt</a></b></td>
																				<td>- Implements swipe-to-delete functionality for RecyclerView items in the app UI, allowing users to remove items with a left swipe gesture<br>- The code defines visual elements like delete icons and backgrounds, enhancing the user experience by providing a visual cue for item deletion.</td>
																			</tr>
																			<tr>
																				<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/NotificationHelper.kt'>NotificationHelper.kt</a></b></td>
																				<td>- Generates notifications to inform users about successful file uploads<br>- Handles notification creation and channel setup for devices running Android Oreo and above<br>- Utilizes pending intents to enable interaction with the notification<br>- Enhances user experience by providing timely feedback on completed file uploads.</td>
																			</tr>
																			</table>
																			<details>
																				<summary><b>fragments</b></summary>
																				<blockquote>
																					<table>
																					<tr>
																						<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/NoNetworkDialogFragment.kt'>NoNetworkDialogFragment.kt</a></b></td>
																						<td>- Implement a dialog fragment handling network connectivity issues, allowing users to interact with an error message<br>- The fragment facilitates user actions through an 'OK' button, triggering responses via a dialog click listener.</td>
																					</tr>
																					<tr>
																						<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/HomeFragment.kt'>HomeFragment.kt</a></b></td>
																						<td>- Implements a fragment for choosing and uploading files, handling user interactions, and communication with the parent activity<br>- The HomeFragment class encapsulates file selection logic and UI elements for a seamless user experience within the app's architecture.</td>
																					</tr>
																					<tr>
																						<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/ResultFragment.kt'>ResultFragment.kt</a></b></td>
																						<td>- Enables displaying and interacting with result data, such as URLs and expiration days, in the app<br>- Allows users to copy links to the clipboard and trigger actions upon completion.</td>
																					</tr>
																					</table>
																				</blockquote>
																			</details>
																			<details>
																				<summary><b>activities</b></summary>
																				<blockquote>
																					<table>
																					<tr>
																						<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/MainActivity.kt'>MainActivity.kt</a></b></td>
																						<td>- The MainActivity file orchestrates file uploads, navigation, and permission handling within the app<br>- It integrates with WorkManager for background tasks, displays results, and manages fragments for user interaction<br>- This central activity drives the core functionality and user experience of the application.</td>
																					</tr>
																					<tr>
																						<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/ErrorActivity.kt'>ErrorActivity.kt</a></b></td>
																						<td>- Handles runtime crashes by displaying an error screen<br>- The ErrorActivity class in the provided file extends AppCompatActivity and overrides onBackPressed() to finish the activity<br>- It sets the content view to activity_error layout in onCreate().</td>
																					</tr>
																					<tr>
																						<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/UploadHistoryActivity.kt'>UploadHistoryActivity.kt</a></b></td>
																						<td>- Manages the upload history display, allowing users to clear history and delete individual items<br>- Provides visual feedback on item removal and dynamically updates the list view based on chronological order<br>- Utilizes WorkManager for background tasks and RecyclerView for swipe-to-delete functionality.</td>
																					</tr>
																					<tr>
																						<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/AboutActivity.kt'>AboutActivity.kt</a></b></td>
																						<td>Manages the About section UI and navigation in the app, allowing users to view open-source licenses.</td>
																					</tr>
																					<tr>
																						<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/LicenseActivity.kt'>LicenseActivity.kt</a></b></td>
																						<td>- Generates a Material About list displaying open-source licenses for various libraries used in the project<br>- The LicenseActivity file constructs license cards with details like library name, author, and license type<br>- This activity helps users view and understand the open-source licenses associated with the project's dependencies.</td>
																					</tr>
																					</table>
																				</blockquote>
																			</details>
																		</blockquote>
																	</details>
																	<details>
																		<summary><b>repository</b></summary>
																		<blockquote>
																			<table>
																			<tr>
																				<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/repository/UploadHistoryWorkers.kt'>UploadHistoryWorkers.kt</a></b></td>
																				<td>- These worker classes in the provided file handle clearing and deleting upload history items in the database<br>- They are responsible for executing background tasks asynchronously to manage the upload history data effectively within the application architecture.</td>
																			</tr>
																			<tr>
																				<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/repository/UploadWorker.kt'>UploadWorker.kt</a></b></td>
																				<td>- Handles uploading files to a remote server, saving upload history to a local database, and notifying users upon completion<br>- Utilizes WorkManager for asynchronous tasks and Fuel library for HTTP requests<br>- The code ensures synchronous requests within a Worker Thread for accurate progress tracking.</td>
																			</tr>
																			</table>
																		</blockquote>
																	</details>
																	<details>
																		<summary><b>utils</b></summary>
																		<blockquote>
																			<table>
																			<tr>
																				<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Extensions.kt'>Extensions.kt</a></b></td>
																				<td>Enables adding toast messages and toggling clickable behavior to strings and views in the Android app.</td>
																			</tr>
																			<tr>
																				<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/WorkManagerHelper.kt'>WorkManagerHelper.kt</a></b></td>
																				<td>Generates OneTimeWorkRequest for uploading files with specified constraints and data, tagged as 'UploadWork'.</td>
																			</tr>
																			<tr>
																				<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Utils.kt'>Utils.kt</a></b></td>
																				<td>- Facilitates Android file handling, network connectivity checks, and dialog management<br>- Includes methods for retrieving file details, opening files, and creating intents<br>- Offers functionalities for network status checks, dialog display, clipboard operations, and app settings navigation<br>- Additionally, provides URL parsing and JSON parsing utilities.</td>
																			</tr>
																			<tr>
																				<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Helpers.kt'>Helpers.kt</a></b></td>
																				<td>- The code file in `Helpers.kt` provides functions to extract metadata and create file entities based on user-selected files<br>- It handles retrieving file names, sizes, and composing file entities with additional data for the project's file management system.</td>
																			</tr>
																			<tr>
																				<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/FragmentHelperExtensions.kt'>FragmentHelperExtensions.kt</a></b></td>
																				<td>- Enhances FragmentManager functionality by simplifying fragment transactions<br>- The code provides extension functions to easily add or replace fragments in a container, managing transitions and back stack behavior<br>- This improves code readability and maintainability in the app's architecture, promoting efficient navigation and user experience.</td>
																			</tr>
																			<tr>
																				<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/MaterialIn.kt'>MaterialIn.kt</a></b></td>
																				<td>- Enables smooth material animation effects on specified views by applying fade and slide transitions based on gravity directions<br>- The code orchestrates animations with precise timing and movement offsets, enhancing the user interface with visually appealing interactions.</td>
																			</tr>
																			<tr>
																				<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Constants.kt'>Constants.kt</a></b></td>
																				<td>- Defines global constants for the project, including BASE_URL, EXPIRE_PARAM, DEFAULT_EXPIRE_WEEKS, GITHUB_URL, TWITTER_URL, EMAIL, POSTFIX, and TIME_STAMP_FORMAT<br>- These constants play a crucial role in maintaining consistency and reusability across the codebase architecture.</td>
																			</tr>
																			</table>
																		</blockquote>
																	</details>
																	<details>
																		<summary><b>listeners</b></summary>
																		<blockquote>
																			<table>
																			<tr>
																				<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/listeners/DialogClickListener.kt'>DialogClickListener.kt</a></b></td>
																				<td>Enables handling positive dialog button clicks within the project's file I/O module.</td>
																			</tr>
																			<tr>
																				<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/listeners/OnFragmentInteractionListener.kt'>OnFragmentInteractionListener.kt</a></b></td>
																				<td>Defines an interface for handling fragment interactions in the project.</td>
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

Before getting started with file.io-Android-Client, ensure your runtime environment meets the following requirements:

- **Programming Language:** Kotlin
- **Package Manager:** Gradle


### ⚙️ Installation

Install file.io-Android-Client using one of the following methods:

**Build from source:**

1. Clone the file.io-Android-Client repository:
```sh
❯ git clone https://github.com/rumaan/file.io-Android-Client
```

2. Navigate to the project directory:
```sh
❯ cd file.io-Android-Client
```

3. Install the project dependencies:


**Using `gradle`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Kotlin-0095D5.svg?style={badge_style}&logo=kotlin&logoColor=white" />](https://kotlinlang.org/)

```sh
❯ gradle build
```




### 🤖 Usage
Run file.io-Android-Client using the following command:
**Using `gradle`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Kotlin-0095D5.svg?style={badge_style}&logo=kotlin&logoColor=white" />](https://kotlinlang.org/)

```sh
❯ gradle run
```


### 🧪 Testing
Run the test suite using the following command:
**Using `gradle`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Kotlin-0095D5.svg?style={badge_style}&logo=kotlin&logoColor=white" />](https://kotlinlang.org/)

```sh
❯ gradle test
```


## 📌 Project Roadmap
- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/rumaan/file.io-Android-Client/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/rumaan/file.io-Android-Client/issues)**: Submit bugs found or log feature requests for the `file.io-Android-Client` project.
- **💡 [Submit Pull Requests](https://github.com/rumaan/file.io-Android-Client/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/rumaan/file.io-Android-Client
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
   <a href="https://github.com{/rumaan/file.io-Android-Client/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=rumaan/file.io-Android-Client">
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
