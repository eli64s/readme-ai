
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
JobBoard-Fastapi
</h1>
<h3 align="center">📍 Empowering Developers - Accelerate Your Job Search with JobBoard-Fastapi.</h3>
<h3 align="center">🚀 Developed with the software and tools below.</h3>
<p align="center">

<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=for-the-badge&logo=Pytest&logoColor=white" alt="" />
<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=for-the-badge&logo=HTML5&logoColor=white" alt="pytest" />
<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=for-the-badge&logo=JavaScript&logoColor=black" alt="html" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="cfg" />

<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=for-the-badge&logo=FastAPI&logoColor=white" alt="md" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="js" />
<img src="https://img.shields.io/badge/precommit-FAB040.svg?style=for-the-badge&logo=pre-commit&logoColor=black" alt="passlib" />
<img src="https://img.shields.io/badge/Jinja-B41717.svg?style=for-the-badge&logo=Jinja&logoColor=white" alt="uvicorn" />
</p>

</div>

---
## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍Overview](#-introdcution)
- [🔮 Features](#-features)
- [⚙️ Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🏎💨 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [🪪 License](#-license)
- [📫 Contact](#-contact)
- [🙏 Acknowledgments](#-acknowledgments)

---

## 📍Overview

JobBoard-Fastapi is an open-source project that allows developers to quickly create a job board marketplace with Python and FastAPI. It provides an easy-to-use API with authentication and authorization support and

## 🔮 Feautres

> `[📌  INSERT-PROJECT-FEATURES]`

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## ⚙️ Project Structure

```bash
.
├── README.md
├── backend
│   ├── apis
│   │   ├── base.py
│   │   ├── utils.py
│   │   └── version1
│   │       ├── route_jobs.py
│   │       ├── route_login.py
│   │       └── route_users.py
│   ├── core
│   │   ├── config.py
│   │   ├── hashing.py
│   │   └── security.py
│   ├── db
│   │   ├── base.py
│   │   ├── base_class.py
│   │   ├── models
│   │   │   ├── jobs.py
│   │   │   └── users.py
│   │   ├── repository
│   │   │   ├── jobs.py
│   │   │   ├── login.py
│   │   │   └── users.py
│   │   ├── session.py
│   │   └── utils.py
│   ├── main.py
│   ├── requirements.txt
│   ├── schemas
│   │   ├── jobs.py
│   │   ├── tokens.py
│   │   └── users.py
│   ├── static
│   │   ├── images
│   │   │   ├── lite.gif
│   │   │   └── logo.png
│   │   └── js
│   │       └── autocomplete.js
│   ├── templates
│   │   ├── auth
│   │   │   └── login.html
│   │   ├── components
│   │   │   ├── alerts.html
│   │   │   ├── cards.html
│   │   │   └── navbar.html
│   │   ├── general_pages
│   │   │   └── homepage.html
│   │   ├── jobs
│   │   │   ├── create_job.html
│   │   │   ├── detail.html
│   │   │   └── show_jobs_to_delete.html
│   │   ├── shared
│   │   │   └── base.html
│   │   └── users
│   │       └── register.html
│   ├── tests
│   │   ├── conftest.py
│   │   ├── test_routes
│   │   │   ├── test_jobs.py
│   │   │   └── test_users.py
│   │   └── utils
│   │       └── users.py
│   └── webapps
│       ├── auth
│       │   ├── forms.py
│       │   └── route_login.py
│       ├── base.py
│       ├── jobs
│       │   ├── forms.py
│       │   └── route_jobs.py
│       └── users
│           ├── forms.py
│           └── route_users.py
└── setup.cfg

26 directories, 48 files
```
---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 💻 Modules
<details closed><summary>Apis</summary>

| File    | Summary                                                                                                                    | Module               |
|:--------|:---------------------------------------------------------------------------------------------------------------------------|:---------------------|
| base.py | This code creates an API router and includes three routes from the version1 API: route_users, route_jobs, and route_login. | backend/apis/base.py |

</details>

<details closed><summary>Auth</summary>

| File           | Summary                                                                                                                                                                              | Module                              |
|:---------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------|
| route_login.py | This code is a router for a login page. It imports a LoginForm from webapps. auth. forms, a login_for_access_token from apis. version1. route_login, and a get_db from db. session.  | backend/webapps/auth/route_login.py |
| forms.py       | This code creates a LoginForm class that is used to validate a user's login credentials. It takes a Request object as an argument and sets the username and password fields to None. | backend/webapps/auth/forms.py       |
| login.html     | This code is an HTML template for a login page. It includes a form for users to enter their email and password, as well as error and success messages.                               | backend/templates/auth/login.html   |

</details>

<details closed><summary>Backend</summary>

| File    | Summary                                                                                                                                                                                                           | Module          |
|:--------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------|
| main.py | This code creates a FastAPI application with a title and version from a settings file, includes two routers, configures static files, creates tables, and checks the database connection on startup and shutdown. | backend/main.py |

</details>

<details closed><summary>Components</summary>

| File        | Summary                                                                                                                                                                 | Module                                   |
|:------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------|
| navbar.html | This code creates a navigation bar with a logo, links to Home, Docs, Redoc, Account, and Jobs, and a search bar. It also includes a dropdown menu for Account and Jobs. | backend/templates/components/navbar.html |
| cards.html  | This code creates a card with a title, company, company URL, and a description. It also includes a button to read more about the card.                                  | backend/templates/components/cards.html  |
| alerts.html | This code checks if a variable "msg" is defined, and if it is, it displays a message in an alert box.                                                                   | backend/templates/components/alerts.html |

</details>

<details closed><summary>Core</summary>

| File        | Summary                                                                                                                                                                                                                    | Module                   |
|:------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------|
| config.py   | This code creates a class called Settings which stores environment variables and other settings for a project called Job Board.                                                                                            | backend/core/config.py   |
| security.py | This code creates an access token with a given set of data and an optional expiration time. It uses the datetime and timedelta modules to calculate the expiration time, and the jose and jwt modules to encode the token. | backend/core/security.py |
| hashing.py  | This code creates a Hasher class with two static methods, verify_password and get_password_hash. The CryptContext from the passlib library is used to securely hash and verify passwords using the bcrypt algorithm.       | backend/core/hashing.py  |

</details>

<details closed><summary>Db</summary>

| File          | Summary                                                                                                                                                                                                                      | Module                   |
|:--------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------|
| base_class.py | This code creates a Base class that can be used as a base for other classes in SQLAlchemy. It defines an id attribute and a __tablename__ attribute that is derived from the class name.                                     | backend/db/base_class.py |
| session.py    | This code imports the Generator type from the typing library, imports settings from the core. config library, creates an engine for a SQLite or other database depending on the settings, and creates a SessionLocal object. | backend/db/session.py    |
| base.py       | This code imports the Base class from the db. base_class module, as well as the Job and User classes from the db. models. jobs and db. models. users modules, respectively.                                                  | backend/db/base.py       |

</details>

<details closed><summary>General_pages</summary>

| File          | Summary                                                                                                                                          | Module                                        |
|:--------------|:-------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------|
| homepage.html | This code extends a shared base HTML template to create a job board page. It includes a title, content, and components such as alerts and cards. | backend/templates/general_pages/homepage.html |

</details>

<details closed><summary>Jobs</summary>

| File                     | Summary                                                                                                                                                                                                         | Module                                          |
|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------|
| forms.py                 | This code creates a JobCreateForm class which is used to validate job postings. It contains a constructor which initializes the request, errors, title, company, company_url, location, and description fields. | backend/webapps/jobs/forms.py                   |
| route_jobs.py            | This code is a FastAPI router for a job listing web application. It includes functions for creating, listing, retrieving, and searching for jobs, as well as a home page and job detail page.                   | backend/webapps/jobs/route_jobs.py              |
| create_job.html          | This code creates a form for creating a job post. It includes fields for the job title, company name, job post URL, job location, and job description.                                                          | backend/templates/jobs/create_job.html          |
| detail.html              | This code extends a shared base. html file and creates a block titled "Job Detail" with a table containing job information such as title, company, company URL, description, location, and date published.      | backend/templates/jobs/detail.html              |
| show_jobs_to_delete.html | This code extends a shared base. html file to create a page for deleting jobs. It includes a table of jobs with a delete button for each job, and a script to delete the job when the button is clicked.        | backend/templates/jobs/show_jobs_to_delete.html |

</details>

<details closed><summary>Models</summary>

| File     | Summary                                                                                                                                                                                     | Module                     |
|:---------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------|
| users.py | This code creates a User class that inherits from the Base class. It has attributes such as id, username, email, hashed_password, is_active, is_superuser, and jobs.                        | backend/db/models/users.py |
| jobs.py  | This code creates a Job class that inherits from the Base class. It has attributes such as title, company, company_url, location, description, date_posted, is_active, owner_id, and owner. | backend/db/models/jobs.py  |

</details>

<details closed><summary>Repository</summary>

| File     | Summary                                                                                                                                                                                                                                                                                   | Module                         |
|:---------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------|
| users.py | This code provides functions to create and retrieve a user from a database using SQLAlchemy. The create_new_user() function takes a UserCreate object and a Session object as parameters, hashes the user's password, and adds the user to the database.                                  | backend/db/repository/users.py |
| jobs.py  | This code provides functions to create, retrieve, list, update, delete, and search for jobs in a database. It imports the Job and JobCreate models from db. models. jobs and schemas. jobs, respectively, and uses the Session object from sqlalchemy. orm to interact with the database. | backend/db/repository/jobs.py  |
| login.py | This code defines a function that takes a username and a database session as parameters and returns a user object from the database based on the username.                                                                                                                                | backend/db/repository/login.py |

</details>

<details closed><summary>Schemas</summary>

| File      | Summary                                                                                                                                                                                                                            | Module                    |
|:----------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------|
| users.py  | This code creates two classes, UserCreate and ShowUser, which are used to create and show user information. UserCreate requires a username, email, and password, while ShowUser requires a username, email, and is_active boolean. | backend/schemas/users.py  |
| tokens.py | This code creates a class called Token which inherits from the BaseModel class from the pydantic library. The Token class has two attributes, access_token and token_type, both of which are strings.                              | backend/schemas/tokens.py |
| jobs.py   | This code creates two classes, JobCreate and ShowJob, which are both subclasses of JobBase. JobBase contains fields for title, company, company_url, location, description, and date_posted.                                       | backend/schemas/jobs.py   |

</details>

<details closed><summary>Shared</summary>

| File      | Summary                                                                                                                                                      | Module                             |
|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------|
| base.html | This code is a HTML document with a head and body section. It includes links to Bootstrap and jQuery libraries, as well as a custom script for autocomplete. | backend/templates/shared/base.html |

</details>

<details closed><summary>Users</summary>

| File           | Summary                                                                                                                                                                                                     | Module                                |
|:---------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------|
| forms.py       | This code creates a UserCreateForm class which is used to validate user input when creating a new user. It takes a Request object as an argument and sets the username, email, and password fields to None. | backend/webapps/users/forms.py        |
| route_users.py | This code creates a route for a user registration page, which allows a user to create an account with a username, email, and password.                                                                      | backend/webapps/users/route_users.py  |
| register.html  | This code is a template for a signup page, which includes a form for users to enter their username, email, and password. It also includes a block for displaying any errors that may occur.                 | backend/templates/users/register.html |

</details>

<details closed><summary>Version1</summary>

| File           | Summary                                                                                                                                                                                                                                                                      | Module                               |
|:---------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------|
| route_login.py | This code is a FastAPI router that provides a login endpoint for users to obtain an access token. It uses OAuth2PasswordBearerWithCookie to authenticate users, and creates an access token with a timedelta expiration.                                                     | backend/apis/version1/route_login.py |
| route_jobs.py  | This code is a FastAPI router for a job management system. It includes functions for creating, reading, updating, and deleting jobs, as well as an autocomplete function for searching jobs.                                                                                 | backend/apis/version1/route_jobs.py  |
| route_users.py | This code creates a router for a FastAPI application that allows users to create a new user. It uses the create_new_user function from the db. repository. users module to create the user, and the get_db function from the db. session module to get the database session. | backend/apis/version1/route_users.py |

</details>

<details closed><summary>Webapps</summary>

| File    | Summary                                                                                                                         | Module                  |
|:--------|:--------------------------------------------------------------------------------------------------------------------------------|:------------------------|
| base.py | This code creates an API router using the FastAPI library and includes three web application routes for jobs, users, and login. | backend/webapps/base.py |

</details>
<hr />

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> `[📌  INSERT-PROJECT-PREREQUISITES]`

### 💻 Installation

1. Clone the JobBoard-Fastapi repository:
```sh
git clone https://github.com/nofoobar/JobBoard-Fastapi
```

2. Change to the project directory:
```sh
cd JobBoard-Fastapi
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

### 🤖 Using JobBoard-Fastapi

```sh
python main.py
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
