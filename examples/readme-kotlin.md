<div align="left" style="position: relative;">
<img src="https://cdn4.iconfinder.com/data/icons/iconsimple-logotypes/512/android-512.png" align="right" width="30%" style="margin: -20px 0 0 20px;">
<h1>FILE.IO-ANDROID-CLIENT</h1>
<p align="left">
	<em>Empowering Android, Elevating Experiences.</em>
</p>
<p align="left">
	<img src="https://img.shields.io/github/license/rumaan/file.io-Android-Client?style=flat&logo=opensourceinitiative&logoColor=white&color=orange" alt="license">
	<img src="https://img.shields.io/github/last-commit/rumaan/file.io-Android-Client?style=flat&logo=git&logoColor=white&color=orange" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/rumaan/file.io-Android-Client?style=flat&color=orange" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/rumaan/file.io-Android-Client?style=flat&color=orange" alt="repo-language-count">
</p>
<p align="left">Built with the tools and technologies:</p>
<p align="left">
	<img src="https://img.shields.io/badge/JetBrains-000000.svg?style=flat&logo=JetBrains&logoColor=white" alt="JetBrains">
	<img src="https://img.shields.io/badge/Android-34A853.svg?style=flat&logo=Android&logoColor=white" alt="Android">
	<img src="https://img.shields.io/badge/Org-77AA99.svg?style=flat&logo=Org&logoColor=white" alt="Org">
	<img src="https://img.shields.io/badge/Gradle-02303A.svg?style=flat&logo=Gradle&logoColor=white" alt="Gradle">
	<img src="https://img.shields.io/badge/Google-4285F4.svg?style=flat&logo=Google&logoColor=white" alt="Google">
	<img src="https://img.shields.io/badge/Kotlin-7F52FF.svg?style=flat&logo=Kotlin&logoColor=white" alt="Kotlin">
	<img src="https://img.shields.io/badge/java-%23ED8B00.svg?style=flat&logo=openjdk&logoColor=white" alt="java">
</p>
</div>
<br clear="right">

## 🔗 Table of Contents

I. [📍 Overview](#-overview)  
II. [👾 Features](#-features)  
III. [📁 Project Structure](#-project-structure)  
IV. [🚀 Getting Started](#-getting-started)  
V. [📌 Project Roadmap](#-project-roadmap)  
VI. [🔰 Contributing](#-contributing)  
VII. [🎗 License](#-license)  
VIII. [🙌 Acknowledgments](#-acknowledgments)  

---

## 📍 Overview

The file.io-Android-Client project offers a seamless solution for secure file uploads on Android devices. Key features include easy file sharing, encrypted URLs, and notification alerts. This open-source project caters to developers seeking a reliable and privacy-focused file transfer solution for their mobile applications.

---

## 👾 Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Configured with **Gradle** for seamless dependency management.</li><li>Utilizes **Android Gradle Plugin** for efficient build management.</li><li>Integrates **Kotlin plugin** for modern language support.</li><li>Implements **Fabric** and **Google Services** for enhanced functionality.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Follows best practices for **Room, Kotlin, and Firebase** integration.</li><li>Utilizes **ProGuard** for code optimization and security.</li><li>Implements **Timber** for logging and error handling.</li><li>Includes unit tests for crucial classes like **FileEntity** and **UploadRepository**.</li></ul> |
| 📄 | **Documentation** | <ul><li>Comprehensive documentation in **Kotlin** with clear code comments.</li><li>Visual aids and instructions in **readme.txt** and **screenshots** for onboarding.</li><li>Defines **ProGuard rules** in **app/proguard-rules.pro** for code optimization.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integrates **Crashlytics** for crash reporting and analytics.</li><li>Utilizes **Navigation Components** for seamless UI navigation.</li><li>Configures **Google Services plugin** for Firebase integration.</li><li>Includes **Permission Dispatcher** for managing app permissions.</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Organized into modules with clear separation of concerns.</li><li>Follows MVVM architecture for separation of UI and business logic.</li><li>Utilizes **ViewModels** for managing UI-related data.</li><li>Implements **Repository pattern** for data abstraction.</li></ul> |
| 🧪 | **Testing**       | <ul><li>Includes **instrumentation tests** for verifying app functionality.</li><li>Implements **unit tests** for core functionalities like addition operations.</li><li>Tests **RoomDatabase** functionality for data integrity and consistency.</li><li>Validates URL parsing and expiration logic in tests.</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Optimizes code with **ProGuard** rules for efficient execution.</li><li>Utilizes **WorkManager** for asynchronous file upload handling.</li><li>Enhances user experience with smooth **RecyclerView** interactions.</li><li>Generates notifications for successful file uploads, improving user feedback.</li></ul> |
| 🛡️ | **Security**      | <ul><li>Enhances security with **ProGuard** rules for code obfuscation.</li><li>Ensures secure access control and user identity verification.</li><li>Handles runtime crashes with **ErrorActivity** for smooth user experience.</li><li>Secures data transmission with HTTPS and secure URL generation.</li></ul> |

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
				<td>- Configures project dependencies and repositories for the entire codebase, ensuring seamless integration of essential tools and libraries<br>- The `build.gradle` file sets up key components like the Android Gradle plugin, Fabric, Google services, and Kotlin plugin, enabling efficient build management across all project modules.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/settings.gradle'>settings.gradle</a></b></td>
				<td>Defines the project structure and modules to include in the build process.</td>
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
				<td>Enhances project onboarding by providing visual aids and documentation in readme.txt and screenshots.</td>
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
				<td>- Define ProGuard rules for Android project to optimize and secure code<br>- Control configuration via build.gradle, preserve line numbers for debugging<br>- Exclude specific packages, keep annotation attributes, and handle Crashlytics classes<br>- Enhance app performance and security.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/build.gradle'>build.gradle</a></b></td>
				<td>- Configures Android project settings, dependencies, and plugins<br>- Manages versions for libraries like Room, Kotlin, and Firebase<br>- Integrates Crashlytics for crash reporting and Navigation components for UI navigation<br>- Implements permissions handling with Permission Dispatcher<br>- Sets up testing dependencies and logging with Timber<br>- Configures Google services plugin for Firebase integration.</td>
			</tr>
			</table>
			<details>
				<summary><b>release</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/release/app-release.apk'>app-release.apk</a></b></td>
						<td>- The provided code file is a crucial component in the project's architecture, serving the purpose of managing user authentication and authorization<br>- It ensures secure access control and user identity verification within the codebase, enhancing the overall security and integrity of the project.</td>
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
												<td>- Summary:
The provided code file plays a crucial role in the project architecture by implementing a key feature that enhances the overall functionality of the codebase<br>- It contributes to the project's success by fulfilling a specific purpose and improving the user experience.</td>
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
																		<td>- Verifies Android app functionality using instrumentation tests on a physical device<br>- The test ensures the app context matches the expected package name, validating proper app setup and configuration.</td>
																	</tr>
																	<tr>
																		<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/androidTest/java/com/thecoolguy/rumaan/fileio/FileEntityDaoTest.java'>FileEntityDaoTest.java</a></b></td>
																		<td>- Tests the RoomDatabase functionality by checking row count, inserting and retrieving items<br>- Validates data integrity and consistency in the database for FileEntity objects.</td>
																	</tr>
																	<tr>
																		<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/androidTest/java/com/thecoolguy/rumaan/fileio/UploadHistoryInstrumentedTest.java'>UploadHistoryInstrumentedTest.java</a></b></td>
																		<td>- Verifies long-press item deletion functionality in Upload History Activity through instrumentation testing<br>- Initializes Room Database, populates with test data, and tests the deletion process<br>- This test ensures items can be deleted successfully via long-press action in the app's upload history feature.</td>
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
																		<td>- Verifies correct addition operation in local unit tests for the Android app<br>- The code ensures the accuracy of the addition functionality by asserting the result against the expected value<br>- This unit test is vital for maintaining the integrity of the app's core arithmetic operations.</td>
																	</tr>
																	<tr>
																		<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/test/java/com/thecoolguy/rumaan/fileio/UploadRepositoryTest.java'>UploadRepositoryTest.java</a></b></td>
																		<td>Verify URL expiration logic correctness and const URL generation in the Upload Repository through unit tests.</td>
																	</tr>
																	<tr>
																		<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/test/java/com/thecoolguy/rumaan/fileio/UrlTest.java'>UrlTest.java</a></b></td>
																		<td>Validates URL parsing functionality for encrypt URLs in the project, ensuring correct extraction of the base URL.</td>
																	</tr>
																	<tr>
																		<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/test/java/com/thecoolguy/rumaan/fileio/FileEntityTest.java'>FileEntityTest.java</a></b></td>
																		<td>- Tests the FileEntity class by setting and checking values for name and URL properties<br>- This file ensures that the FileEntity object correctly stores and retrieves the provided data, validating the core functionality of the FileEntity class within the project architecture.</td>
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
																				<td>- Manages live data for upload history in the application by connecting to the local database<br>- The UploadHistoryViewModel class in the provided file serves as a bridge between the database and UI, ensuring real-time updates on uploaded files.</td>
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
																				<td>- Initiates application setup and configuration<br>- Handles logging with Timber and sets up custom error handling using Custom Activity on Crash.</td>
																			</tr>
																			<tr>
																				<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/UploadHistoryListAdapter.kt'>UploadHistoryListAdapter.kt</a></b></td>
																				<td>- Enables rendering of upload history items in a RecyclerView with date separators and file details<br>- Supports interaction for copying file URLs and removing items<br>- Facilitates dynamic updates to the displayed list of files.</td>
																			</tr>
																			<tr>
																				<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/SwipeToDeleteCallBack.kt'>SwipeToDeleteCallBack.kt</a></b></td>
																				<td>- Implements swipe-to-delete functionality for RecyclerView items<br>- Handles drawing delete background and icon<br>- Disables swiping for specific item types<br>- Utilizes a color drawable and custom paint to manage visual effects<br>- Designed to enhance user interaction and provide a seamless UI experience within the app.</td>
																			</tr>
																			<tr>
																				<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/NotificationHelper.kt'>NotificationHelper.kt</a></b></td>
																				<td>- Generates notifications upon successful file uploads, utilizing a notification channel for Android O and above<br>- Includes a notification click action to open the upload history activity with file details.</td>
																			</tr>
																			</table>
																			<details>
																				<summary><b>fragments</b></summary>
																				<blockquote>
																					<table>
																					<tr>
																						<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/NoNetworkDialogFragment.kt'>NoNetworkDialogFragment.kt</a></b></td>
																						<td>- Creates a dialog fragment to handle network errors<br>- It provides an option for users to acknowledge the error and triggers a callback to the parent activity.</td>
																					</tr>
																					<tr>
																						<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/HomeFragment.kt'>HomeFragment.kt</a></b></td>
																						<td>- Enables interaction with local files through a user-friendly interface<br>- Facilitates file selection and storage in the local cache<br>- Implements callbacks for user actions and ensures seamless communication with the parent activity.</td>
																					</tr>
																					<tr>
																						<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/ResultFragment.kt'>ResultFragment.kt</a></b></td>
																						<td>- ResultFragment in the codebase displays and manages the result details for a specific file operation<br>- It handles the UI elements and user interactions related to displaying a URL and its expiration duration<br>- The fragment allows users to copy the URL to the clipboard and provides a button to indicate completion of the task.</td>
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
																						<td>- Manages the main activity of the app, facilitating file uploads, handling permissions, and displaying results<br>- It initializes fragments, handles user interactions, and enqueues upload work using WorkManager<br>- The activity also responds to permission requests and provides options to navigate to upload history and about sections.</td>
																					</tr>
																					<tr>
																						<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/ErrorActivity.kt'>ErrorActivity.kt</a></b></td>
																						<td>Handles runtime crashes by displaying the ErrorActivity, ensuring a smooth user experience.</td>
																					</tr>
																					<tr>
																						<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/UploadHistoryActivity.kt'>UploadHistoryActivity.kt</a></b></td>
																						<td>- Manages the upload history display, enabling users to clear history, remove individual items, and swipe to delete<br>- Displays a list of uploaded files grouped by date, with the ability to toggle between views based on content availability.</td>
																					</tr>
																					<tr>
																						<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/AboutActivity.kt'>AboutActivity.kt</a></b></td>
																						<td>- Enables navigation to the open-source license activity from the About section<br>- The code defines the behavior for creating the options menu, setting the theme, and handling user interaction to launch the LicenseActivity<br>- This functionality enhances the user experience by providing access to project licensing information.</td>
																					</tr>
																					<tr>
																						<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/LicenseActivity.kt'>LicenseActivity.kt</a></b></td>
																						<td>- Generates a list of open-source licenses for various libraries used in the project, providing details such as the library name, release year, creator, and license type<br>- This activity serves to display licensing information in a Material About Activity to inform users about the open-source components utilized in the application.</td>
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
																				<td>Implements workers to handle clearing and deleting items in the Upload History database.</td>
																			</tr>
																			<tr>
																				<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/repository/UploadWorker.kt'>UploadWorker.kt</a></b></td>
																				<td>- Handles uploading files to a remote server, saving upload history to a local database, and sending notifications upon completion<br>- Manages file upload process asynchronously using WorkManager, ensuring data consistency and user feedback.</td>
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
																				<td>- Enables displaying toast messages and toggling clickability in Android app views<br>- Enhances user interaction by providing convenient feedback and dynamic interaction controls<br>- Integrates seamlessly within the project's utility functions, contributing to a user-friendly experience.</td>
																			</tr>
																			<tr>
																				<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/WorkManagerHelper.kt'>WorkManagerHelper.kt</a></b></td>
																				<td>Generates OneTimeWorkRequest for uploading a file with specified URI by creating constraints and work data, then assigning them to the request.</td>
																			</tr>
																			<tr>
																				<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Utils.kt'>Utils.kt</a></b></td>
																				<td>- Provides utility methods for handling file operations, network connectivity, intents, dialogs, and JSON parsing in the Android app<br>- Centralizes common functionalities to simplify code maintenance and enhance readability<br>- Facilitates file details retrieval, file opening, network connectivity checks, dialog management, URL parsing, JSON parsing, and date formatting.</td>
																			</tr>
																			<tr>
																				<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Helpers.kt'>Helpers.kt</a></b></td>
																				<td>- The code file in `Helpers.kt` extracts metadata and retrieves files from URIs in the app using Android content resolver<br>- It aids in fetching file details like name and size, converting them into a structured `FileEntity`, and logging with Timber<br>- This facilitates seamless file operations within the app's architecture.</td>
																			</tr>
																			<tr>
																				<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/FragmentHelperExtensions.kt'>FragmentHelperExtensions.kt</a></b></td>
																				<td>- Enhances FragmentManager functionality by adding and replacing fragments in a container with specified transitions and backstack management<br>- Supports smoother fragment transactions within the app's architecture.</td>
																			</tr>
																			<tr>
																				<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/MaterialIn.kt'>MaterialIn.kt</a></b></td>
																				<td>Enables smooth material animations on Android views based on gravity directions, facilitating a polished user interface experience within the project architecture.</td>
																			</tr>
																			<tr>
																				<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Constants.kt'>Constants.kt</a></b></td>
																				<td>- Defines global constants for the project, including BASE_URL for API requests, default expiration time, social media links, and email address<br>- Additionally, it sets up the format for timestamps used throughout the codebase<br>- The file centralizes key values to ensure consistency and easy maintenance across the project.</td>
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
																				<td>Enables communication between dialogs and fragments for seamless user interactions within the project architecture.</td>
																			</tr>
																			<tr>
																				<td><b><a href='https://github.com/rumaan/file.io-Android-Client/blob/master/app/src/main/java/com/thecoolguy/rumaan/fileio/listeners/OnFragmentInteractionListener.kt'>OnFragmentInteractionListener.kt</a></b></td>
																				<td>- The code file `OnFragmentInteractionListener.kt` defines an interface for handling specific events within the project architecture<br>- It facilitates communication between different components by defining methods for actions like file uploads and completion notifications<br>- This abstraction helps in decoupling and structuring the codebase effectively.</td>
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


---
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
