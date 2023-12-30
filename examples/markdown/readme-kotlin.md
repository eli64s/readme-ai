<div align="left">
<h1><img src=https://img.icons8.com/external-tal-revivo-regular-tal-revivo/96/external-readme-is-a-easy-to-build-a-developer-hub-that-adapts-to-the-user-logo-regular-tal-revivo.png width="100" />
<br>FILE.IO-ANDROID-CLIENT</h1>
<h3>◦ Unlock the Power of Your Codebase!</h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="left">
<img src="https://img.shields.io/badge/Firebase-FFCA28.svg?style=plastic&logo=Firebase&logoColor=black" alt="Firebase" />
<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=plastic&logo=YAML&logoColor=white" alt="YAML" />
<img src="https://img.shields.io/badge/Kotlin-7F52FF.svg?style=plastic&logo=Kotlin&logoColor=white" alt="Kotlin" />
<img src="https://img.shields.io/badge/Org-77AA99.svg?style=plastic&logo=Org&logoColor=white" alt="Org" />
<img src="https://img.shields.io/badge/Google-4285F4.svg?style=plastic&logo=Google&logoColor=white" alt="Google" />

<img src="https://img.shields.io/badge/Android-3DDC84.svg?style=plastic&logo=Android&logoColor=white" alt="Android" />
<img src="https://img.shields.io/badge/GitHub-181717.svg?style=plastic&logo=GitHub&logoColor=white" alt="GitHub" />
<img src="https://img.shields.io/badge/Gradle-02303A.svg?style=plastic&logo=Gradle&logoColor=white" alt="Gradle" />
<img src="https://img.shields.io/badge/JetBrains-000000.svg?style=plastic&logo=JetBrains&logoColor=white" alt="JetBrains" />
<img src="https://img.shields.io/badge/java-%23ED8B00.svg?style=plastic&logo=openjdk&logoColor=white" alt="java" />
</p>
<img src="https://img.shields.io/github/license/rumaan/file.io-Android-Client?style=plastic&color=5D6D7E" alt="GitHub license" />
<img src="https://img.shields.io/github/last-commit/rumaan/file.io-Android-Client?style=plastic&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/rumaan/file.io-Android-Client?style=plastic&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/languages/top/rumaan/file.io-Android-Client?style=plastic&color=5D6D7E" alt="GitHub top language" />
</div>
<hr>

## 🔗 Quick Links
- [🔗 Quick Links](#-quick-links)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [🧩 Modules](#modules)
- [🚀 Getting Started](#-getting-started)
    - [⚙️ Installation](#-installation)
    - [🤖 Running file.io-Android-Client](#-running-file.io-Android-Client)
    - [🧪 Tests](#-tests)
- [🚧 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

The code repository is an Android app that enables users to upload files to a server and manage their upload history. It provides features such as choosing and uploading files, displaying upload history, and viewing license information. The code includes activities, fragments, view models, and utilities for handling file uploads, managing database operations, and displaying notifications. It also includes unit tests and instrumented tests for various components. The repository structure consists of the `app` module, build configurations, Gradle files, and screenshots directory. The code relies on several dependencies, including Kotlin, AndroidX, Firebase, Fuel, and Room.

---

## 📦 Features

HTTPStatus Exception: 400

---

## 📂 Repository Structure

```sh
└── file.io-Android-Client/
    ├── .travis.yml
    ├── app/
    │   ├── build/
    │   │   └── outputs/
    │   ├── build.gradle
    │   ├── proguard-rules.pro
    │   ├── release/
    │   │   └── app-release.apk
    │   └── src/
    │       ├── androidTest/
    │       ├── main/
    │       └── test/
    ├── build.gradle
    ├── gradle/
    │   └── wrapper/
    ├── screenshots/
    │   ├── readme.txt
    └── settings.gradle

```

---


## 🧩 Modules

<details closed><summary>.</summary>

| File                                                                                          | Summary                                                                                                                                                                                                                                |
| ---                                                                                           | ---                                                                                                                                                                                                                                    |
| [build.gradle](https://github.com/rumaan/file.io-Android-Client/blob/main/build.gradle)       | The code snippet defines the repositories and dependencies for the Android application build process, including the Google Maven repository, JCenter, Fabric Maven, and Jitpack.                                                       |
| [settings.gradle](https://github.com/rumaan/file.io-Android-Client/blob/main/settings.gradle) | The code snippet adds the `app` module to the parent repository structure                                                                                                                                                              |
| [.travis.yml](https://github.com/rumaan/file.io-Android-Client/blob/main/.travis.yml)         | The code snippet, located in `.travis.yml`, defines the necessary configurations and dependencies for building and testing an Android project using Travis CI. It sets up the required Android SDK, licenses, and caching directories. |

</details>

<details closed><summary>screenshots</summary>

| File                                                                                            | Summary                                                                                                                          |
| ---                                                                                             | ---                                                                                                                              |
| [readme.txt](https://github.com/rumaan/file.io-Android-Client/blob/main/screenshots/readme.txt) | This code snippet is responsible for storing the README file and screenshots within the screenshots directory of the repository. |

</details>

<details closed><summary>app</summary>

| File                                                                                                    | Summary                                                                                                                                                                                                                                                                                                             |
| ---                                                                                                     | ---                                                                                                                                                                                                                                                                                                                 |
| [proguard-rules.pro](https://github.com/rumaan/file.io-Android-Client/blob/main/app/proguard-rules.pro) | The code snippet contains ProGuard rules for an Android app repository. It specifies configuration fileEntities, class keeping rules, warnings to ignore, and class obfuscation instructions. It also includes rules for Crashlytics.                                                                               |
| [build.gradle](https://github.com/rumaan/file.io-Android-Client/blob/main/app/build.gradle)             | This code snippet is located in the `app/build.gradle` file of the repository structure. It applies various Android and Kotlin plugins, defines Android configurations, builds different types (debug and release), and lists dependencies for the Android application. It also applies the Google Services plugin. |

</details>

<details closed><summary>app/src/androidTest/java/com/thecoolguy/rumaan/fileio</summary>

| File                                                                                                                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                   |
| ---                                                                                                                                                                                       | ---                                                                                                                                                                                                                                                                                                                                       |
| [ExampleInstrumentedTest.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/androidTest/java/com/thecoolguy/rumaan/fileio/ExampleInstrumentedTest.kt)                 | This code snippet contains an instrumented test that verifies the package name of the app under test. It uses the AndroidJUnit4 test runner and asserts that the package name matches the expected value.                                                                                                                                 |
| [FileEntityDaoTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/androidTest/java/com/thecoolguy/rumaan/fileio/FileEntityDaoTest.java)                         | The code snippet is responsible for testing the functionality of the FileEntityDao class in the app/src/androidTest/java/com/thecoolguy/rumaan/fileio package. It includes tests for counting the number of rows in the database, inserting and retrieving upload items, and saving multiple items and retrieving them from the database. |
| [UploadHistoryInstrumentedTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/androidTest/java/com/thecoolguy/rumaan/fileio/UploadHistoryInstrumentedTest.java) | The code snippet is an instrumented test for the Upload History functionality of the File.io Android Client app. It tests the deletion of items when long-pressed.                                                                                                                                                                        |

</details>

<details closed><summary>app/src/test/java/com/thecoolguy/rumaan/fileio</summary>

| File                                                                                                                                                             | Summary                                                                                                                                                                                                         |
| ---                                                                                                                                                              | ---                                                                                                                                                                                                             |
| [ExampleUnitTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/test/java/com/thecoolguy/rumaan/fileio/ExampleUnitTest.java)           | The code snippet is an example unit test in the parent repository that checks if addition works correctly, specifically 2 + 2 equals 4.                                                                         |
| [UploadRepositoryTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/test/java/com/thecoolguy/rumaan/fileio/UploadRepositoryTest.java) | This code snippet tests the functionality of the UploadRepository class by checking if the generated URL is correct when given a number of days.                                                                |
| [UrlTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/test/java/com/thecoolguy/rumaan/fileio/UrlTest.java)                           | Summary: The code snippet in the file UrlTest.java tests the functionality of the parseEncryptUrl method in the URLParser class. It checks if the method correctly extracts the base URL from an encrypted URL. |
| [FileEntityTest.java](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/test/java/com/thecoolguy/rumaan/fileio/FileEntityTest.java)             | The code snippet contains a test class FileEntityTest that tests the functionality of the FileEntity class. It checks if the name and url attributes of a FileEntity object can be set and retrieved correctly. |

</details>

<details closed><summary>app/src/main/java/com/thecoolguy/rumaan/fileio/viewmodel</summary>

| File                                                                                                                                                                       | Summary                                                                                                                                                                                                                                                                             |
| ---                                                                                                                                                                        | ---                                                                                                                                                                                                                                                                                 |
| [UploadHistoryViewModel.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/viewmodel/UploadHistoryViewModel.kt) | This code snippet defines the UploadHistoryViewModel, which is responsible for providing a LiveData object that holds a list of FileEntity objects representing the upload history. It initializes the uploadList variable by fetching the data from the UploadHistoryRoomDatabase. |

</details>

<details closed><summary>app/src/main/java/com/thecoolguy/rumaan/fileio/ui</summary>

| File                                                                                                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                                                 |
| ---                                                                                                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                                                     |
| [FileioApplication.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/FileioApplication.kt)               | The code snippet is a part of the File.io Android Client repository's architecture. It includes an Application class that sets up logging using Timber and handles custom activity on crash using CaocConfig.                                                                                                                                                                           |
| [UploadHistoryListAdapter.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/UploadHistoryListAdapter.kt) | The code snippet is a RecyclerView adapter for displaying upload history. It differentiates between date and content items, handles item click actions, and provides methods for updating and managing the list of items.                                                                                                                                                               |
| [SwipeToDeleteCallBack.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/SwipeToDeleteCallBack.kt)       | The code snippet defines a SwipeToDeleteCallBack class that handles swipe gestures on a RecyclerView. It provides functionality to display a delete icon and a red background when an item is swiped.                                                                                                                                                                                   |
| [NotificationHelper.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/NotificationHelper.kt)             | This code snippet is responsible for creating and displaying a notification when a file upload is successful. It uses the NotificationCompat and NotificationManagerCompat classes to set various properties of the notification, such as the icon, title, text, and intent. It also handles creating a notification channel for devices running Android Oreo (API level 26) and above. |

</details>

<details closed><summary>app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments</summary>

| File                                                                                                                                                                            | Summary                                                                                                                                                                                                                                                                                                                                                     |
| ---                                                                                                                                                                             | ---                                                                                                                                                                                                                                                                                                                                                         |
| [NoNetworkDialogFragment.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/NoNetworkDialogFragment.kt) | This code snippet defines the NoNetworkDialogFragment class, which creates a dialog fragment that displays a no network error message to the user. It also handles the click event for the OK button in the dialog.                                                                                                                                         |
| [HomeFragment.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/HomeFragment.kt)                       | This code snippet represents the implementation of the HomeFragment class in the Android app. It handles user interactions on the home screen, including choosing a file. It also manages the communication between the fragment and its parent activity.                                                                                                   |
| [ResultFragment.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/fragments/ResultFragment.kt)                   | This code snippet defines a fragment in an Android app which displays the result of a process. It includes UI elements such as text views, button, and handles user interactions like copying text to clipboard and displaying toast messages. The fragment can be instantiated with specific parameters using the companion object's `newInstance` method. |

</details>

<details closed><summary>app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities</summary>

| File                                                                                                                                                                         | Summary                                                                                                                                                                                                                                                                                     |
| ---                                                                                                                                                                          | ---                                                                                                                                                                                                                                                                                         |
| [MainActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/MainActivity.kt)                   | This code snippet represents the main activity of an Android app. It handles various UI interactions, such as choosing a file, uploading it, and displaying the result. It also manages permissions and fragments.                                                                          |
| [ErrorActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/ErrorActivity.kt)                 | This code snippet contains the implementation for an ErrorActivity class that is displayed when runtime crashes occur in the Android app. It handles the back button press and finishes the activity when pressed. It also sets the layout for the error activity.                          |
| [UploadHistoryActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/UploadHistoryActivity.kt) | This code snippet is responsible for creating and managing the Upload History activity in the Android application. It handles menu options, clearing history, removing individual history items, and displaying the list of upload history items.                                           |
| [AboutActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/AboutActivity.kt)                 | This code snippet defines an Activity class called AboutActivity that displays information about the app. It inflates a menu, sets a transparent navigation bar style, and handles menu item selections to start different activities.                                                      |
| [LicenseActivity.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/ui/activities/LicenseActivity.kt)             | The code snippet provides an implementation of a LicenseActivity class that extends MaterialAboutActivity. It generates a MaterialAboutList with license cards for various open-source libraries used in the parent repository. It also defines the activity title as Open Source Licenses. |

</details>

<details closed><summary>app/src/main/java/com/thecoolguy/rumaan/fileio/repository</summary>

| File                                                                                                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---                                                                                                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [UploadHistoryWorkers.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/repository/UploadHistoryWorkers.kt) | These code snippets are workers for deleting history items in the UploadHistoryRoomDatabase using asynchronous calls. The ClearHistoryWorker clears all items, while the DeleteSingleItemWorker deletes a specific item specified by its ID.                                                                                                                                                                                                                                                 |
| [UploadWorker.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/repository/UploadWorker.kt)                 | This code snippet defines the UploadWorker class, which extends the Worker class from the androidx.work package. It handles the uploading of a file to a server using the Fuel library. The file to be uploaded is retrieved from the specified URI, and the upload progress is logged. The response from the server is parsed and used to create a FileEntity object, which is then saved to a database. Finally, a notification is created to inform the user about the successful upload. |

</details>

<details closed><summary>app/src/main/java/com/thecoolguy/rumaan/fileio/utils</summary>

| File                                                                                                                                                                       | Summary                                                                                                                                                                                                               |
| ---                                                                                                                                                                        | ---                                                                                                                                                                                                                   |
| [Extensions.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Extensions.kt)                             | This code contains two extension functions. The first function displays a toast message using the given string and context. The second function toggles the clickability of a view based on a boolean value.          |
| [WorkManagerHelper.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/WorkManagerHelper.kt)               | The code snippet defines a function `createUploadWork(uri: String)` that creates a work request to upload a file. It sets constraints for network connectivity and input data for the worker.                         |
| [Utils.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Utils.kt)                                       | This code snippet provides a collection of helper methods for file operations, including getting file details, opening and reading files, checking network connectivity, managing dialogs, and parsing URLs and JSON. |
| [Helpers.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Helpers.kt)                                   | The code snippet provides utility functions for file operations, such as retrieving file metadata, fetching files from URI, and composing file entities.                                                              |
| [FragmentHelperExtensions.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/FragmentHelperExtensions.kt) | The code snippet provides extension functions for fragment management in an Android app. It includes functions to add and replace fragments within a specified container.                                             |
| [MaterialIn.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/MaterialIn.kt)                             | This code snippet provides the functionality to animate the views in a material design style. It includes animations for fading and sliding in from different directions.                                             |
| [Constants.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/utils/Constants.kt)                               | This code snippet contains global constants for the File.io Android Client application, including base URL, expiration parameters, default expiration weeks, and various URLs.                                        |

</details>

<details closed><summary>app/src/main/java/com/thecoolguy/rumaan/fileio/listeners</summary>

| File                                                                                                                                                                                     | Summary                                                                                                                                                                                                                                                            |
| ---                                                                                                                                                                                      | ---                                                                                                                                                                                                                                                                |
| [DialogClickListener.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/listeners/DialogClickListener.kt)                     | This code snippet defines an interface called DialogClickListener in the package com.thecoolguy.rumaan.fileio.listeners. It includes a function called onDialogPositiveClick which takes two parameters: a Dialog and a DialogFragment from androidx.fragment.app. |
| [OnFragmentInteractionListener.kt](https://github.com/rumaan/file.io-Android-Client/blob/main/app/src/main/java/com/thecoolguy/rumaan/fileio/listeners/OnFragmentInteractionListener.kt) | The provided code snippet contains an interface named OnFragmentInteractionListener which defines two functions: onUploadFileClick() and onDone().                                                                                                                 |

</details>

---

## 🚀 Getting Started

***Prerequisites***

Ensure you have the following dependencies installed on your system:

- `► INSERT-DEPENDENCY-1`
- `► INSERT-DEPENDENCY-2`
- `► INSERT-DEPENDENCY-3`

### ⚙️ Installation

1. Clone the file.io-Android-Client repository:
```sh
git clone https://github.com/rumaan/file.io-Android-Client
```

2. Change to the project directory:
```sh
cd file.io-Android-Client
```

3. Install the dependencies:
```sh
gradle build
```

### 🤖 Running file.io-Android-Client

```sh
java -jar build/libs/myapp.jar
```

### 🧪 Tests
```sh
gradle test
```

---


## 🚧 Project Roadmap

> - [X] `ℹ️  Task 1: Implement X`
> - [ ] `ℹ️  Task 2: Implement Y`
> - [ ] `ℹ️ ...`


---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/rumaan/file.io-Android-Client/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/rumaan/file.io-Android-Client/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/rumaan/file.io-Android-Client/issues)**: Submit bugs found or log feature requests for RUMAAN.

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

## 📄 License


This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 👏 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#Top)

---
