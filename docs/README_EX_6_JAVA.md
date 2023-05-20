
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
Minimal-Todo
</h1>
<h3 align="center">📍 Less is More with Minimal-Todo!</h3>
<h3 align="center">🚀 Developed with the software and tools below.</h3>
<p align="center">

<img src="https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white" alt="properties" />
<img src="https://img.shields.io/badge/Gradle-02303A.svg?style=for-the-badge&logo=Gradle&logoColor=white" alt="json" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white" alt="" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="iml" />
</p>

</div>

---
## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍Overview](#overview)
- [🔮 Feautres](#-feautres)
- [⚙️ Project Structure](#️-project-structure)
- [💻 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
  - [✅ Prerequisites](#-prerequisites)
  - [💻 Installation](#-installation)
  - [🤖 Using Minimal-Todo](#-using-minimal-todo)
  - [🧪 Running Tests](#-running-tests)
- [🛠 Future Development](#-future-development)
- [🤝 Contributing](#-contributing)
- [🪪 License](#-license)
- [🙏 Acknowledgments](#-acknowledgments)

---

## 📍Overview

Minimal-Todo is an open-source, minimalistic to-do app that allows users to quickly and easily keep track of tasks and organize their day. It provides an easy-to-use, clean interface with drag and drop functionality for reordering lists, and supports synchronization across multiple devices.

## 🔮 Feautres

> `[📌  INSERT-PROJECT-FEATURES]`

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## ⚙️ Project Structure

```bash
repo
├── Contributing.md
├── LICENSE.md
├── README.md
├── app
│   ├── app-release.apk
│   ├── app.iml
│   ├── build.gradle
│   ├── google-services.json
│   ├── proguard-rules.pro
│   └── src
│       ├── androidTest
│       │   └── java
│       │       └── com
│       │           └── example
│       │               └── avjindersinghsekhon
│       │                   └── minimaltodo
│       │                       ├── ApplicationTest.java
│       │                       ├── TestStoreRetrieveData.java
│       │                       └── TestTodoItem.java
│       └── main
│           ├── AndroidManifest.xml
│           ├── assets
│           │   └── fonts
│           │       └── Aller_Regular.ttf
│           ├── java
│           │   └── com
│           │       └── example
│           │           └── avjindersinghsekhon
│           │               └── minimaltodo
│           │                   ├── About
│           │                   │   ├── AboutActivity.java
│           │                   │   └── AboutFragment.java
│           │                   ├── AddToDo
│           │                   │   ├── AddToDoActivity.java
│           │                   │   └── AddToDoFragment.java
│           │                   ├── Analytics
│           │                   │   └── AnalyticsApplication.java
│           │                   ├── AppDefault
│           │                   │   ├── AppDefaultActivity.java
│           │                   │   └── AppDefaultFragment.java
│           │                   ├── Main
│           │                   │   ├── CustomRecyclerScrollViewListener.java
│           │                   │   ├── MainActivity.java
│           │                   │   └── MainFragment.java
│           │                   ├── Reminder
│           │                   │   ├── ReminderActivity.java
│           │                   │   └── ReminderFragment.java
│           │                   ├── Settings
│           │                   │   ├── SettingsActivity.java
│           │                   │   └── SettingsFragment.java
│           │                   └── Utility
│           │                       ├── CustomTextInputLayout.java
│           │                       ├── DeleteNotificationService.java
│           │                       ├── ItemTouchHelperClass.java
│           │                       ├── PreferenceKeys.java
│           │                       ├── RecyclerViewEmptySupport.java
│           │                       ├── ScrollingFABBehaviour.java
│           │                       ├── StoreRetrieveData.java
│           │                       ├── ToDoItem.java
│           │                       ├── TodoNotificationService.java
│           │                       └── Utils.java
│           └── res
│               ├── drawable
│               │   ├── button_pressed_background.xml
│               │   ├── clipboard.png
│               │   ├── dropdown_text_background_color.xml
│               │   ├── dropdown_text_color.xml
│               │   └── ic_content_copy_black_24dp.xml
│               ├── drawable-hdpi
│               │   ├── check.png
│               │   ├── empty_view_bg.png
│               │   ├── ic_access_time_black_18dp.png
│               │   ├── ic_add_alarm_grey_200_24dp.png
│               │   ├── ic_add_white_24dp.png
│               │   ├── ic_alarm_add_white_24dp.png
│               │   ├── ic_alarm_black_18dp.png
│               │   ├── ic_clear_white_24dp.png
│               │   ├── ic_color_lens_white_24dp.png
│               │   ├── ic_done_white_24dp.png
│               │   ├── ic_menu_overflow_light.png
│               │   ├── ic_reorder_grey_600_18dp.png
│               │   ├── ic_send_white_18dp.png
│               │   ├── ic_snooze_black_24dp.png
│               │   └── ic_snooze_white_24dp.png
│               ├── drawable-ldpi
│               │   ├── check.png
│               │   └── empty_view_bg.png
│               ├── drawable-mdpi
│               │   ├── check.png
│               │   ├── empty_view_bg.png
│               │   ├── ic_access_time_black_18dp.png
│               │   ├── ic_add_alarm_grey_200_24dp.png
│               │   ├── ic_add_white_24dp.png
│               │   ├── ic_alarm_add_white_24dp.png
│               │   ├── ic_alarm_black_18dp.png
│               │   ├── ic_clear_white_24dp.png
│               │   ├── ic_color_lens_white_24dp.png
│               │   ├── ic_done_white_24dp.png
│               │   ├── ic_menu_overflow_light.png
│               │   ├── ic_reorder_grey_600_18dp.png
│               │   ├── ic_send_white_18dp.png
│               │   ├── ic_snooze_black_24dp.png
│               │   └── ic_snooze_white_24dp.png
│               ├── drawable-xhdpi
│               │   ├── check.png
│               │   ├── empty_view_bg.png
│               │   ├── ic_access_time_black_18dp.png
│               │   ├── ic_add_alarm_grey_200_24dp.png
│               │   ├── ic_add_white_24dp.png
│               │   ├── ic_alarm_add_white_24dp.png
│               │   ├── ic_alarm_black_18dp.png
│               │   ├── ic_clear_white_24dp.png
│               │   ├── ic_color_lens_white_24dp.png
│               │   ├── ic_done_white_24dp.png
│               │   ├── ic_menu_overflow_light.png
│               │   ├── ic_reorder_grey_600_18dp.png
│               │   ├── ic_send_white_18dp.png
│               │   ├── ic_snooze_black_24dp.png
│               │   └── ic_snooze_white_24dp.png
│               ├── drawable-xxhdpi
│               │   ├── check.png
│               │   ├── empty_view_bg.png
│               │   ├── ic_access_time_black_18dp.png
│               │   ├── ic_add_alarm_grey_200_24dp.png
│               │   ├── ic_add_white_24dp.png
│               │   ├── ic_alarm_add_white_24dp.png
│               │   ├── ic_alarm_black_18dp.png
│               │   ├── ic_clear_white_24dp.png
│               │   ├── ic_color_lens_white_24dp.png
│               │   ├── ic_done_white_24dp.png
│               │   ├── ic_menu_overflow_light.png
│               │   ├── ic_reorder_grey_600_18dp.png
│               │   ├── ic_send_white_18dp.png
│               │   ├── ic_snooze_black_24dp.png
│               │   └── ic_snooze_white_24dp.png
│               ├── drawable-xxxhdpi
│               │   ├── check.png
│               │   ├── empty_view_bg.png
│               │   └── ic_menu_overflow_light.png
│               ├── layout
│               │   ├── about_layout.xml
│               │   ├── activity_add_to_do.xml
│               │   ├── activity_main.xml
│               │   ├── activity_settings.xml
│               │   ├── activity_todo_test.xml
│               │   ├── base_toolbar.xml
│               │   ├── date_dropdown_item.xml
│               │   ├── date_spinner_item.xml
│               │   ├── fragment_about.xml
│               │   ├── fragment_add_to_do.xml
│               │   ├── fragment_main.xml
│               │   ├── fragment_reminder.xml
│               │   ├── layout_fragment_container.xml
│               │   ├── list_circle_try.xml
│               │   ├── list_item_view_future.xml
│               │   ├── reminder_layout.xml
│               │   ├── spinner_dropdown_item.xml
│               │   └── spinner_text_view.xml
│               ├── menu
│               │   ├── menu_main.xml
│               │   └── menu_reminder.xml
│               ├── mipmap-hdpi
│               │   └── ic_launcher.png
│               ├── mipmap-mdpi
│               │   └── ic_launcher.png
│               ├── mipmap-xhdpi
│               │   └── ic_launcher.png
│               ├── mipmap-xxhdpi
│               │   └── ic_launcher.png
│               ├── mipmap-xxxhdpi
│               │   └── ic_launcher.png
│               ├── values
│               │   ├── colors.xml
│               │   ├── dimens.xml
│               │   ├── donottranslate.xml
│               │   ├── strings.xml
│               │   └── styles.xml
│               ├── values-bg
│               │   └── strings.xml
│               ├── values-de
│               │   └── strings.xml
│               ├── values-es
│               │   └── strings.xml
│               ├── values-fi
│               │   └── strings.xml
│               ├── values-fr
│               │   └── strings.xml
│               ├── values-it
│               │   └── strings.xml
│               ├── values-ml
│               │   └── strings.xml
│               ├── values-pl
│               │   └── strings.xml
│               ├── values-tl
│               │   └── strings.xml
│               ├── values-vi
│               │   └── strings.xml
│               ├── values-w820dp
│               │   └── dimens.xml
│               ├── values-zh
│               │   └── strings.xml
│               └── xml
│                   ├── global_tracker.xml
│                   └── preferences_layout.xml
├── build.gradle
├── gradle
│   └── wrapper
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties
├── gradle.properties
├── gradlew
├── gradlew.bat
├── screenshots
│   ├── add_todo_dark.png
│   ├── add_todo_light.png
│   ├── app_icon.png
│   ├── main_empty_dark.png
│   ├── main_empty_light.png
│   ├── main_full_dark.png
│   ├── main_full_light.png
│   ├── screenshot_notification.png
│   ├── screenshot_reminder_date.png
│   ├── screenshot_reminder_time.png
│   ├── screenshot_todo_snooze.png
│   ├── todo_date_dark.png
│   └── todo_time_dark.png
└── settings.gradle

57 directories, 171 files
```
---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 💻 Modules
<details closed><summary>About</summary>

| File               | Summary                                                                                                                                                                                                                                                                     | Module                                                                                 |
|:-------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------|
| AboutActivity.java | This code is for the AboutActivity class in the MinimalTodo app. It is responsible for setting up the AboutFragment, which displays information about the app, such as the version number. It also sets up the toolbar and handles the navigation back to the MainFragment. | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/About/AboutActivity.java |
| AboutFragment.java | This code is for the AboutFragment of the MinimalTodo app. It sets up the layout for the AboutFragment, including the version number, toolbar, and contact me button. It also sets up an onClickListener for the contact me button.                                         | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/About/AboutFragment.java |

</details>

<details closed><summary>Addtodo</summary>

| File                 | Summary                                                                                                                                                                                                                                                                          | Module                                                                                     |
|:---------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------|
| AddToDoFragment.java | Error fetching summary.                                                                                                                                                                                                                                                          | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AddToDo/AddToDoFragment.java |
| AddToDoActivity.java | This code is for the AddToDoActivity class in the com. example. avjindersinghsekhon. minimaltodo package. It extends the AppDefaultActivity class and overrides the onCreate, contentViewLayoutRes, createInitialFragment, and onResume methods. It also imports the android. os | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AddToDo/AddToDoActivity.java |

</details>

<details closed><summary>Analytics</summary>

| File                      | Summary                                                                                                                                                                                                          | Module                                                                                            |
|:--------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------|
| AnalyticsApplication.java | This code is a class that implements Google Analytics for an Android application. It contains methods to send events and screens to the Google Analytics server, as well as a method to get the default tracker. | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Analytics/AnalyticsApplication.java |

</details>

<details closed><summary>App</summary>

| File               | Summary                                                                                                                                                                                             | Module                 |
|:-------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------|
| app.iml            | Error fetching summary.                                                                                                                                                                             | app/app.iml            |
| proguard-rules.pro | This code provides ProGuard rules for an Android project, including rules for WebViews and Google classes. It also specifies to not warn about Google classes.                                      | app/proguard-rules.pro |
| build.gradle       | This code applies the Android and Google services plugins, sets up signing configurations, compiles the SDK version, sets up build types, and adds dependencies for libraries and support packages. | app/build.gradle       |
| app-release.apk    | This code is an error message indicating that a file could not be decoded because it is not a text or UTF-8 file.                                                                                   | app/app-release.apk    |

</details>

<details closed><summary>Appdefault</summary>

| File                    | Summary                                                                                                                                                                                                                                                                                                                  | Module                                                                                           |
|:------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|
| AppDefaultFragment.java | This code is a fragment class from the MinimalTodo app. It provides a basic framework for creating a fragment, including an abstract layoutRes ( ) method that must be implemented by the subclass. It also provides an onCreateView ( ) method to inflate the layout and an onDestroy ( ) method to clean up resources. | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AppDefault/AppDefaultFragment.java |
| AppDefaultActivity.java | This code is an abstract class for an AppCompatActivity that sets up an initial Fragment and sets the content view layout.                                                                                                                                                                                               | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/AppDefault/AppDefaultActivity.java |

</details>

<details closed><summary>Drawable</summary>

| File                               | Summary                                                                                                                                                                                                                                           | Module                                                       |
|:-----------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------|
| dropdown_text_color.xml            | This code is an XML selector that sets the color of an item when it is pressed to the color specified in the " icons " color resource, and sets the color to the color specified in the " secondary_text " color resource when it is not pressed. | app/src/main/res/drawable/dropdown_text_color.xml            |
| dropdown_text_background_color.xml | This code is an XML selector that defines the drawable for a button when it is pressed and when it is not pressed. It sets the drawable to @color / primary_light when pressed and @color / icons when not pressed.                               | app/src/main/res/drawable/dropdown_text_background_color.xml |
| ic_content_copy_black_24dp.xml     | This code creates a vector graphic with a width of 24dp, a height of 24dp, a viewport width of 24. 0, and a viewport height of 24. 0. The graphic is filled with a color of # FF000000 and contains a path data of " M16, 1L4, 1c-1.              | app/src/main/res/drawable/ic_content_copy_black_24dp.xml     |
| button_pressed_background.xml      | This code is an XML selector that sets the drawable color of an item to either @color / primary_dark or @color / primary depending on whether the item is pressed or not.                                                                         | app/src/main/res/drawable/button_pressed_background.xml      |

</details>

<details closed><summary>Layout</summary>

| File                          | Summary                                                                                                                                                                                                                                                                                                                      | Module                                                |
|:------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------|
| fragment_main.xml             | This code creates a LinearLayout with a CoordinatorLayout, an ImageView, a TextView, a RecyclerViewEmptySupport, and a FloatingActionButton. The layout is set to match the parent size and is vertically oriented with gravity centered. The FloatingActionButton is anchored to the bottom right of the CoordinatorLayout. | app/src/main/res/layout/fragment_main.xml             |
| activity_settings.xml         | This code creates a RelativeLayout with a Toolbar and a LinearLayout. The Toolbar is set to the actionBarSize and the colorPrimary, and the LinearLayout is set to match the parent 's width and height.                                                                                                                     | app/src/main/res/layout/activity_settings.xml         |
| fragment_about.xml            | This code creates a LinearLayout with an ImageView, four TextViews, and various attributes to adjust the layout and text. The ImageView displays an icon, the TextViews display the app name, version, author, and contact information.                                                                                      | app/src/main/res/layout/fragment_about.xml            |
| base_toolbar.xml              | This code creates an Android Toolbar with a background color of the primary color and a minimum height of the action bar size. The layout width is set to match the parent and the layout height is set to wrap the content.                                                                                                 | app/src/main/res/layout/base_toolbar.xml              |
| fragment_add_to_do.xml        | This code creates a LinearLayout with a toolbar, two EditTexts, a SwitchCompat, a Button, and a FloatingActionButton. It is used to create a to - do list with a title, description, reminder, and date.                                                                                                                     | app/src/main/res/layout/fragment_add_to_do.xml        |
| date_spinner_item.xml         | This code creates a TextView element with a text size of 12sp, ellipsize of marquee, layout height and width of wrap_content and match_parent respectively, and a text color of secondary_text. The style is set to spinnerItemStyle.                                                                                        | app/src/main/res/layout/date_spinner_item.xml         |
| fragment_reminder.xml         | This code is a RelativeLayout XML file for an Android app. It includes a toolbar, a TextView, a Button, and a LinearLayout with a TextView and a MaterialSpinner. All strings are stored in the string. xml file.                                                                                                            | app/src/main/res/layout/fragment_reminder.xml         |
| list_item_view_future.xml     | This code creates a LinearLayout with an ImageView and two TextViews, all with various attributes such as layout_width, layout_height, textColor, and textSize. The background color is set to @color / icons and the orientation is horizontal. The ImageView has a source of @drawable / ic_reorder                        | app/src/main/res/layout/list_item_view_future.xml     |
| reminder_layout.xml           | This code creates a FrameLayout in an Android application with an i d of " fragment_container " and a width and height that match the parent.                                                                                                                                                                                | app/src/main/res/layout/reminder_layout.xml           |
| activity_add_to_do.xml        | This code creates a LinearLayout with a vertical orientation that takes up the full width and height of the parent view. It also includes a layout fragment container. The layout changes are animated.                                                                                                                      | app/src/main/res/layout/activity_add_to_do.xml        |
| spinner_text_view.xml         | This code creates a TextView element in an Android application with a text color of secondary_text, a text size of 16sp, gravity of start|center, ellipsize of end, and a layout height and width of wrap_content and match_parent respectively.                                                                             | app/src/main/res/layout/spinner_text_view.xml         |
| spinner_dropdown_item.xml     | This code creates a TextView element with attributes such as text color, text size, gravity, padding, ellipsize, and layout height and width. The style is set to the spinnerDropDownItemStyle.                                                                                                                              | app/src/main/res/layout/spinner_dropdown_item.xml     |
| layout_fragment_container.xml | This code creates a FrameLayout in an Android application with a width and height that match the parent view. It also assigns an ID of " fragment_container " to the FrameLayout.                                                                                                                                            | app/src/main/res/layout/layout_fragment_container.xml |
| list_circle_try.xml           | This code creates a LinearLayout with an ImageView and a RelativeLayout containing two TextViews. The ImageView has a margin of 16dp and a width and height of 45dp. The RelativeLayout has a margin of 16dp, a weight of 5, and a width of 0dp. The two TextViews have different text                                       | app/src/main/res/layout/list_circle_try.xml           |
| activity_main.xml             | This code creates a LinearLayout with an AppBarLayout containing two included layouts, one for a toolbar and one for a fragment container. The layout has a width and height of " match_parent " and an orientation of " vertical ".                                                                                         | app/src/main/res/layout/activity_main.xml             |
| about_layout.xml              | This code creates a LinearLayout with a base toolbar and a fragment container, both of which are included from other layouts. The LinearLayout is set to match the parent size and have a vertical orientation, with gravity centered and top.                                                                               | app/src/main/res/layout/about_layout.xml              |
| date_dropdown_item.xml        | This code creates a TextView element with attributes such as text, text size, padding, text color, background, and style. The text is set to " Gender " and the text size is set to 14sp. The padding is set to 8dp on the top and bottom, and 16dp on the left. The text color and                                          | app/src/main/res/layout/date_dropdown_item.xml        |
| activity_todo_test.xml        | This code creates a LinearLayout with a toolbar, an EditText, a SwitchCompat, and a FloatingActionButton. It also includes a TextInputLayout and two EditTexts for entering a date and time. The layout is set to animate layout changes and is set to match the parent 's width and height.                                 | app/src/main/res/layout/activity_todo_test.xml        |

</details>

<details closed><summary>Main</summary>

| File                                  | Summary                                                                                                                                                                                                                                                                                                 | Module                                                                                                   |
|:--------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------|
| AndroidManifest.xml                   | This code is an XML manifest for an Android app. It includes permissions for internet and network access, as well as activities, services, and a theme. It is used to define the structure of the app and the components it contains.                                                                   | app/src/main/AndroidManifest.xml                                                                         |
| MainActivity.java                     | This code is for the MainActivity class of the MinimalTodo app. It contains methods to create the activity, set the toolbar, create the initial fragment, and handle menu item selections. It also contains a switch statement to handle the selection of the About, Preferences, and Theme menu items. | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/MainActivity.java                     |
| CustomRecyclerScrollViewListener.java | This code is an abstract class that extends the RecyclerView. OnScrollListener class. It contains methods to show and hide the view when the user scrolls, and keeps track of the scroll distance.                                                                                                      | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/CustomRecyclerScrollViewListener.java |
| MainFragment.java                     | Error fetching summary.                                                                                                                                                                                                                                                                                 | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Main/MainFragment.java                     |

</details>

<details closed><summary>Menu</summary>

| File              | Summary                                                                                                                                                                                                                 | Module                                  |
|:------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------|
| menu_main.xml     | This code creates a menu with two items, one for preferences and one for about. It is written in XML and is used in an Android application.                                                                             | app/src/main/res/menu/menu_main.xml     |
| menu_reminder.xml | This code creates an XML menu item with an icon, title, and action. The item has an ID of " toDoReminderDoneMenuItem " and the icon is a white checkmark. The title is set to a string resource labeled " done_label ". | app/src/main/res/menu/menu_reminder.xml |

</details>

<details closed><summary>Minimaltodo</summary>

| File                       | Summary                                                                                                                                                                                                                                              | Module                                                                                          |
|:---------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------|
| TestStoreRetrieveData.java | This test case is for the StoreRetrieveData class which is used to store and retrieve data from a file. It tests the functionality of the class by writing and reading data to and from the file, as well as converting an ArrayList to a JSONArray. | app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/TestStoreRetrieveData.java |
| ApplicationTest.java       | This code is a test class for an Android application, which extends the Application class and is used to test the fundamentals of the application.                                                                                                   | app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/ApplicationTest.java       |
| TestTodoItem.java          | This JUnit test verifies the functionality of the ToDoItem class, which is used to create and store ToDo items. It tests the three parameter constructor, object marshalling to JSON, and object unmarshalling from JSON.                            | app/src/androidTest/java/com/example/avjindersinghsekhon/minimaltodo/TestTodoItem.java          |

</details>

<details closed><summary>Reminder</summary>

| File                  | Summary                                                                                                                                                                                                                                                                | Module                                                                                       |
|:----------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------|
| ReminderFragment.java | This code is a fragment for a reminder activity in an Android app. It contains functions for setting a reminder, removing a reminder, and snoozing a reminder. It also contains functions for changing the theme of the app, saving data, and closing the app.         | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Reminder/ReminderFragment.java |
| ReminderActivity.java | This code is for the ReminderActivity class which extends the AppDefaultActivity class. It contains the onCreate ( ) and contentViewLayoutRes ( ) methods, as well as the createInitialFragment ( ) method which creates a new instance of the ReminderFragment class. | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Reminder/ReminderActivity.java |

</details>

<details closed><summary>Root</summary>

| File            | Summary                                                                                                                                                                                                                                                                                                                         | Module          |
|:----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------|
| gradlew         | This code is a UNIX start up script for Gradle, a build automation system. It sets up the environment for the application, including setting the JAVA_HOME variable, increasing the maximum file descriptors, and setting the application name and icon. It then executes the GradleWrapperMain class with the given arguments. | gradlew         |
| build.gradle    | This code is a top - level build file that provides configuration options for all sub - projects / modules. It includes repositories for jcenter ( ), mavenCentral ( ), and Google, as well as dependencies for classpath ' com. android. tools. build: gradle: 3. 2. 1 ', classpath ' com. google. g                           | build.gradle    |
| gradlew.bat     | This code is a Windows startup script for Gradle, a build automation system. It sets up the command line, finds the Java executable, and executes Gradle with the given command line arguments. It also sets up the classpath and default JVM options. Finally, it sets the GRADLE_EXIT_CONSOLE variable                        | gradlew.bat     |
| settings.gradle | This code includes the ': app ' module, which is a part of the Android application development framework. It provides access to the application 's resources, such as activities, services, and content providers. It also allows developers to create and manage the application 's components.                                | settings.gradle |

</details>

<details closed><summary>Settings</summary>

| File                  | Summary                                                                                                                                                                                                               | Module                                                                                       |
|:----------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------|
| SettingsFragment.java | This code is a PreferenceFragment class that allows users to change the night mode setting of the application. It also sends analytics data to the AnalyticsApplication class when the night mode setting is changed. | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Settings/SettingsFragment.java |
| SettingsActivity.java | This code is for the SettingsActivity class in an Android app. It sets up the activity, including the toolbar, and replaces the content with the SettingsFragment. It also handles the navigation back button.        | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Settings/SettingsActivity.java |

</details>

<details closed><summary>Utility</summary>

| File                           | Summary                                                                                                                                                                                                                                                                                              | Module                                                                                               |
|:-------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------|
| TodoNotificationService.java   | This code is a utility class for a to - do list app. It creates a notification with the to - do item 's text and a pending intent to open the reminder activity. It also includes a delete intent to delete the notification.                                                                        | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/TodoNotificationService.java   |
| ScrollingFABBehaviour.java     | This code is a ScrollingFABBehaviour class from the package com. example. avjindersinghsekhon. minimaltodo. Utility. It is used to control the behavior of a FloatingActionButton when scrolling a Toolbar or Snackbar. It adjusts the position of the FloatingActionButton based on                 | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ScrollingFABBehaviour.java     |
| ToDoItem.java                  | This code is a Java class that creates a ToDoItem object with properties such as text, description, reminder, color, date, and identifier. It also includes methods to convert the object to and from a JSONObject.                                                                                  | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ToDoItem.java                  |
| CustomTextInputLayout.java     | This code is a custom TextInputLayout class which extends the TextInputLayout class. It stores the hint value of an EditText and sets it when the layout is laid out. It also checks if the hint has been changed programmatically and updates the hint accordingly.                                 | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/CustomTextInputLayout.java     |
| StoreRetrieveData.java         | This code is a utility class for the MinimalTodo app. It provides methods to save and retrieve ToDoItem objects from a file, using JSONArray and JSONObject.                                                                                                                                         | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/StoreRetrieveData.java         |
| Utils.java                     | This code is a utility class from the MinimalTodo package that provides a method to get the toolbar height from the current context.                                                                                                                                                                 | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/Utils.java                     |
| DeleteNotificationService.java | This code is a service that deletes a ToDoItem from a list of ToDoItems. It handles the intent, retrieves the ToDoItem 's UUID, loads the data, removes the item, saves the data, and destroys the service.                                                                                          | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/DeleteNotificationService.java |
| ItemTouchHelperClass.java      | This code is a class that extends the ItemTouchHelper. Callback class to provide an interface for the user to move and remove items from a RecyclerView. It provides methods to enable long press drag and swipe to remove items, as well as methods to move and remove items from the RecyclerView. | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/ItemTouchHelperClass.java      |
| PreferenceKeys.java            | This code creates a class called PreferenceKeys which stores a string value for the night_mode_pref_key. The value is retrieved from the resources file.                                                                                                                                             | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/PreferenceKeys.java            |
| RecyclerViewEmptySupport.java  | This code is a custom RecyclerView class that allows for an empty view to be set and displayed when the adapter has no items. It also has an AdapterDataObserver that will show the empty view when the adapter 's item count is 0.                                                                  | app/src/main/java/com/example/avjindersinghsekhon/minimaltodo/Utility/RecyclerViewEmptySupport.java  |

</details>

<details closed><summary>Values</summary>

| File               | Summary                                                                                                                                                                                                                                                                                             | Module                                     |
|:-------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------|
| colors.xml         | This code is an XML file containing a list of colors and their hexadecimal values. It includes colors such as amber, red, primary, secondary, divider, light primary, and more.                                                                                                                     | app/src/main/res/values/colors.xml         |
| dimens.xml         | This code is an XML file that defines the default screen margins for an Android app, according to the Android Design guidelines. The horizontal margin is 16dp and the vertical margin is 16dp.                                                                                                     | app/src/main/res/values/dimens.xml         |
| donottranslate.xml | This code is an XML file containing three strings: an email address, a key for a night mode preference, and an example string.                                                                                                                                                                      | app/src/main/res/values/donottranslate.xml |
| styles.xml         | This code is an XML file that defines various styles for an application, including customizing the theme, colors, and text appearance. It also includes styles for a toolbar, popup menu, checkbox, and switch.                                                                                     | app/src/main/res/values/styles.xml         |
| strings.xml        | This code is an XML file containing strings for a minimalistic to - do list app. It includes strings for the app name, settings, no to - dos, title, remind me, choose date, choose time, about, app version, contact me, made by, done label, date reminder default, date error check again, night | app/src/main/res/values/strings.xml        |

</details>

<details closed><summary>Values-bg</summary>

| File        | Summary                                                                                                                                         | Module                                 |
|:------------|:------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------|
| strings.xml | This code is an XML file containing strings of text used in an app called " Minimal ". The strings are used for labels, messages, and settings. | app/src/main/res/values-bg/strings.xml |

</details>

<details closed><summary>Values-de</summary>

| File        | Summary                                                                                                                                                                                                                                                                                                  | Module                                 |
|:------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------|
| strings.xml | This code is an XML file containing strings for a minimalistic To Do list app. It includes strings for the app name, settings, no to dos, title, remind me, choose date, choose time, remind date and time, about, app version, contact me, made by, done label, date reminder default, date error check | app/src/main/res/values-de/strings.xml |

</details>

<details closed><summary>Values-es</summary>

| File        | Summary                                                                                                                                                                                                                                                                            | Module                                 |
|:------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------|
| strings.xml | This code is an XML file containing strings for a minimalistic To - Do app. It includes strings for the app name, settings, no to - dos, title, remind me, choose date, choose time, remind date and time, about, app version, contact me, made by, done label, snooze options, sn | app/src/main/res/values-es/strings.xml |

</details>

<details closed><summary>Values-fi</summary>

| File        | Summary                                                                                                                                                                                                                                                                                    | Module                                 |
|:------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------|
| strings.xml | This code is an XML file containing strings for a minimalistic app. It includes strings for app name, settings, to - dos, title, reminder, date, time, about, version, contact, done label, date reminder default, date error check again, night mode, snooze options, snooze, and remove. | app/src/main/res/values-fi/strings.xml |

</details>

<details closed><summary>Values-fr</summary>

| File        | Summary                                                                                                                                                                                                                                                                                          | Module                                 |
|:------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------|
| strings.xml | This code is an XML file containing strings for a minimalistic to - do list app. It includes strings for the app name, settings, no to - dos, title, remind me, choose date, choose time, remind date and time, about, app version, contact me, made by, done label, date reminder default, date | app/src/main/res/values-fr/strings.xml |

</details>

<details closed><summary>Values-it</summary>

| File        | Summary                                                                                                                                                                                                                           | Module                                 |
|:------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------|
| strings.xml | Questo codice definisce le stringhe e le string - array necessarie per un'applicazione chiamata Minimal. Include stringhe come " app_name ", " action_settings ", " no_to_dos ", " title ", " remind_me ", " choose_date ", " cho | app/src/main/res/values-it/strings.xml |

</details>

<details closed><summary>Values-ml</summary>

| File        | Summary                                                                                                                                                                                                                                                                              | Module                                 |
|:------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------|
| strings.xml | This code is an XML file containing strings of text in the Malayalam language. It is used to create a to - do list app, with strings for the app name, settings, no to - dos, title, remind me, choose date, choose time, remind date and time, about, app version, contact me, made | app/src/main/res/values-ml/strings.xml |

</details>

<details closed><summary>Values-pl</summary>

| File        | Summary                                                                                                                                                                                              | Module                                 |
|:------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------|
| strings.xml | This code is an XML file containing strings for a minimalistic app. It includes strings for app name, settings, reminders, dates, times, about, contact, done label, night mode, and snooze options. | app/src/main/res/values-pl/strings.xml |

</details>

<details closed><summary>Values-tl</summary>

| File        | Summary                                                                                                                                                                        | Module                                 |
|:------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------|
| strings.xml | Ang code na ito ay naglalaman ng mga string na naglalarawan ng mga pangalan ng app, mga setting, mga pagpapaalala, mga petsa at oras, mga detalye tungkol sa app, at mga error | app/src/main/res/values-tl/strings.xml |

</details>

<details closed><summary>Values-vi</summary>

| File        | Summary                                                                                                                                                                                                                                                                                            | Module                                 |
|:------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------|
| strings.xml | This code is an XML file containing strings for a minimalistic to - do list app. It includes strings for app name, settings, no to - dos, title, remind me, choose date, choose time, remind date and time, about, app version, contact me, made by, done label, date reminder default, date error | app/src/main/res/values-vi/strings.xml |

</details>

<details closed><summary>Values-w820dp</summary>

| File       | Summary                                                                                                                                                    | Module                                    |
|:-----------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------|
| dimens.xml | This code is an example of customizing the dimensions of a screen with more than 820dp of available width. It sets the activity horizontal margin to 64dp. | app/src/main/res/values-w820dp/dimens.xml |

</details>

<details closed><summary>Values-zh</summary>

| File        | Summary                                                                                                                                                                                                                                                                                          | Module                                 |
|:------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------|
| strings.xml | This code is an XML file containing strings for a minimalistic to - do list app. It includes strings for the app name, settings, no to - dos, title, remind me, choose date, choose time, remind date and time, about, app version, contact me, made by, done label, date reminder default, date | app/src/main/res/values-zh/strings.xml |

</details>

<details closed><summary>Wrapper</summary>

| File               | Summary                                                                                                           | Module                            |
|:-------------------|:------------------------------------------------------------------------------------------------------------------|:----------------------------------|
| gradle-wrapper.jar | This code is an error message indicating that a file could not be decoded because it is not a text or UTF-8 file. | gradle/wrapper/gradle-wrapper.jar |

</details>

<details closed><summary>Xml</summary>

| File                   | Summary                                                                                                                                                                                                                                                              | Module                                      |
|:-----------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------|
| preferences_layout.xml | This code creates a checkbox preference in an Android app that allows users to toggle between night mode on and off. When night mode is on, a summary will appear to indicate this, and when it is off, a different summary will appear.                             | app/src/main/res/xml/preferences_layout.xml |
| global_tracker.xml     | This code is an XML file that sets up analytics tracking for an app. It includes the tracking ID, sample frequency, session timeout, and alternate screen names for activities. It also enables automatic activity measurement and reporting of uncaught exceptions. | app/src/main/res/xml/global_tracker.xml     |

</details>
<hr />

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> `[📌  INSERT-PROJECT-PREREQUISITES]`

### 💻 Installation

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
mvn clean install || gradle build
```

### 🤖 Using Minimal-Todo

```sh
java -jar target/myapp.jar
```

### 🧪 Running Tests
```sh
#run tests
```

<hr />

## 🛠 Future Development
- [X] [📌  COMPLETED-TASK]
- [ ] [📌  INSERT-TASK]
- [ ] [📌  INSERT-TASK]


---

## 🤝 Contributing
Contributions are always welcome! Please follow these steps:
1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).
```sh
git checkout -b new-feature-branch
```
4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub using the following command
```sh
git push origin new-feature-branch
```
7. Create a pull request to the original repository.
Open a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 🪪 License

This project is licensed under the `[📌  INSERT-LICENSE-TYPE]` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 🙏 Acknowledgments

[📌  INSERT-DESCRIPTION]


---
