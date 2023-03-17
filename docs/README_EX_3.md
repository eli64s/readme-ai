
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
JobBoard Fastapi
</h1>

> <h3 align="center">
>
> `[📌  INSERT-PROJECT-SUMMARY]`
>
> </h3>
> <h3 align="center">🚀 Developed using OpenAI's language model API and the software tools below.</h3>
> <p align="center">
> 
> ![fastapi](https://img.shields.io/badge/FastAPI-009688.svg?style=for-the-badge&logo=FastAPI&logoColor=white)
> ![pytest](https://img.shields.io/badge/Pytest-0A9EDC.svg?style=for-the-badge&logo=Pytest&logoColor=white)
> ![py](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)
> ![html](https://img.shields.io/badge/HTML5-E34F26.svg?style=for-the-badge&logo=HTML5&logoColor=white)
> ![markdown](https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white)
> </p>

</div>


---

## 📦 Table of Contents


- [📦 Table of Contents](#-table-of-contents)

- [👋 Introdcution](#-introdcution)

- [🔮 Features](#-features)

- [⚙️ Repository Structure](#repository-structure)

- [🧩 Modules](#modules)

- [🏎💨 Getting Started](#-getting-started)

- [🗺 Roadmap](#-roadmap)

- [🤝 Contributing](#-contributing)

- [🪪 License](#-license)

- [📫 Contact](#-contact)

- [🙏 Acknowledgments](#-acknowledgments)

---
## 👋 Introduction

This is a repository for the JobBoard-Fastapi project.

## 🔮 Feautres

- job board written in FastAPI with MySQL database

- Jobs can be searched by keyword, employer, or location

- Jobs can be filtered by job type (full-time, part-time, etc.), salary, or date posted

- Users can create an account to save jobs and receive job recommendations

- Employers can post jobs and view applications

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## ⚙️ Repository Structure
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

## 🧩 Modules


<details closed><summary>APIS</summary>

| File Name   | Summary                                                                                                                                                                    |
|:------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| utils.py    | This code creates a class called OAuth2PasswordBearerWithCookie which is a subclass of OAuth2. It allows for authentication using an access token from an httpOnly Cookie. |
| base.py     | This code creates an API router and includes three routes from the version1 API: route_users, route_jobs, and route_login.                                                 |

</details>

<details closed><summary>AUTH</summary>

| File Name      | Summary                                                                                                                                                                              |
|:---------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| route_login.py | This code is a router for a login page. It imports a LoginForm from webapps. auth. forms, a login_for_access_token from apis. version1. route_login, and a get_db from db. session.  |
| forms.py       | This code creates a LoginForm class that is used to validate a user's login credentials. It takes a Request object as an argument and sets the username and password fields to None. |

</details>

<details closed><summary>BACKEND</summary>

| File Name   | Summary                                                                                                                                                                                      |
|:------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| main.py     | This code creates a FastAPI application with an API router and web app router, configures static files, creates database tables, and checks the database connection on startup and shutdown. |

</details>

<details closed><summary>CORE</summary>

| File Name   | Summary                                                                                                                                                                                                                            |
|:------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| config.py   | This code creates a class called Settings which stores environment variables from a . env file. It also stores variables such as the project name, version, database URL, secret key, algorithm, and access token expiration time. |
| security.py | This code creates an access token with a given set of data and an optional expiration time. It uses the datetime and timedelta modules to calculate the expiration time, and the jose and jwt modules to encode the token.         |
| hashing.py  | This code creates a Hasher class with two static methods, verify_password and get_password_hash. The CryptContext from the passlib library is used to securely hash and verify passwords using the bcrypt algorithm.               |

</details>

<details closed><summary>DB</summary>

| File Name     | Summary                                                                                                                                                                                                              |
|:--------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| base_class.py | This code creates a base class for SQLAlchemy models, which provides a __tablename__ attribute based on the class name. It also provides an id attribute of type Any.                                                |
| session.py    | This code imports the Generator type from the typing library, imports settings from the core. config library, creates an engine from the SQLAlchemy library, and creates a sessionmaker from the SQLAlchemy library. |
| utils.py      | This code checks the connection status of a database using the SQLALCHEMY_DATABASE_URL. It will connect to the database if it is not connected and disconnect if it is connected.                                    |
| base.py       | This code imports the Base class from the db. base_class module, as well as the Job and User classes from the db. models. jobs and db. models. users modules, respectively.                                          |

</details>

<details closed><summary>JOBS</summary>

| File Name     | Summary                                                                                                                                                                                                                                                                |
|:--------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| forms.py      | This code creates a JobCreateForm class which is used to validate job postings. It contains a constructor which initializes the request, errors, title, company, company_url, location, and description fields.                                                        |
| route_jobs.py | This code imports various modules and functions to create a job posting website. It includes functions for creating, listing, retrieving, and searching for jobs, as well as functions for getting the current user from a token and for creating a template response. |

</details>

<details closed><summary>MODELS</summary>

| File Name   | Summary                                                                                                                                                                                     |
|:------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| users.py    | This code creates a User class that inherits from the Base class. It has attributes such as id, username, email, hashed_password, is_active, is_superuser, and jobs.                        |
| jobs.py     | This code creates a Job class that inherits from the Base class. It has attributes such as title, company, company_url, location, description, date_posted, is_active, owner_id, and owner. |

</details>

<details closed><summary>REPOSITORY</summary>

| File Name   | Summary                                                                                                                                                                                                                                                                                   |
|:------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| users.py    | This code provides functions to create and retrieve a user from a database using SQLAlchemy. The create_new_user() function takes a UserCreate object and a Session object as parameters, hashes the user's password, and adds the user to the database.                                  |
| jobs.py     | This code provides functions to create, retrieve, list, update, delete, and search for jobs in a database. It imports the Job and JobCreate models from db. models. jobs and schemas. jobs, respectively, and uses the Session object from sqlalchemy. orm to interact with the database. |
| login.py    | This code defines a function that takes a username and a database session as parameters and returns a user object from the database based on the username.                                                                                                                                |

</details>

<details closed><summary>SCHEMAS</summary>

| File Name   | Summary                                                                                                                                                                                                                                         |
|:------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| users.py    | This code creates two classes, UserCreate and ShowUser, which are used to create and show user information respectively. UserCreate requires a username, email, and password, while ShowUser requires a username, email, and is_active boolean. |
| tokens.py   | This code creates a class called Token which inherits from the BaseModel class from the pydantic library. The Token class has two attributes, access_token and token_type, both of which are strings.                                           |
| jobs.py     | This code creates a class JobBase which is used to store shared properties for a job such as title, company, company_url, location, description, and date_posted.                                                                               |

</details>

<details closed><summary>TEST_ROUTES</summary>

| File Name     | Summary                                                                                                                                                                                                                     |
|:--------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| test_users.py | This code creates a user with the username "testuser", email "testuser@nofoobar. com", and password "testing". It then checks that the response status code is 200, that the email is correct, and that the user is active. |
| test_jobs.py  | This code tests the functionality of a job posting API. It tests the ability to create, read, update, and delete job postings.                                                                                              |

</details>

<details closed><summary>TESTS</summary>

| File Name   | Summary                                                                                                                                                                                         |
|:------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| conftest.py | This code is a pytest fixture for a FastAPI application. It creates a fresh database on each test case, sets up a session, creates a TestClient, and provides a token header for a normal user. |

</details>

<details closed><summary>USERS</summary>

| File Name      | Summary                                                                                                                                                                                                                         |
|:---------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| forms.py       | This code creates a UserCreateForm class which is used to validate user input when creating a new user. It takes a Request object as an argument and has three attributes: username, email, and password.                       |
| route_users.py | This code creates a route for a user registration page. It uses a UserCreateForm to validate the user's input, and creates a new user in the database using the create_new_user function from the db. repository. users module. |

</details>

<details closed><summary>UTILS</summary>

| File Name   | Summary                                                                                                                                           |
|:------------|:--------------------------------------------------------------------------------------------------------------------------------------------------|
| users.py    | This code provides a function to generate an authentication token for a user with a given email. If the user does not exist, it is created first. |

</details>

<details closed><summary>VERSION1</summary>

| File Name      | Summary                                                                                                                                                                                                                                                                      |
|:---------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| route_login.py | This code is a FastAPI router for authenticating users and creating access tokens. It uses OAuth2PasswordBearerWithCookie to authenticate users, and creates an access token with a timedelta expiration.                                                                    |
| route_jobs.py  | This code is a FastAPI router for a job management system. It includes functions for creating, reading, updating, and deleting jobs, as well as an autocomplete function for searching jobs.                                                                                 |
| route_users.py | This code creates a router for a FastAPI application that allows users to create a new user. It uses the create_new_user function from the db. repository. users module to create the user, and the get_db function from the db. session module to get the database session. |

</details>

<details closed><summary>WEBAPPS</summary>

| File Name   | Summary                                                                                                                         |
|:------------|:--------------------------------------------------------------------------------------------------------------------------------|
| base.py     | This code creates an API router using the FastAPI library and includes three web application routes for jobs, users, and login. |

</details>
<hr />

## 🏎💨 Getting Started

### Prerequisites

Before you begin, ensure that you have the following prerequisites installed:


- `[📌  INSERT-PREREQUISITES-IF-NEEDED]`


### Installation

1. Clone the JobBoard Fastapi repository:


```sh
git clone https://github.com/nofoobar/JobBoard-Fastapi && cd JobBoard Fastapi
```

2. Create a new Conda environment and install the required dependencies:

```sh
conda env create -f setup/environment.yaml
conda activate JobBoard Fastapi
```

3. `[📌  insert-additional-steps]`


```sh
 #... 
```

### Running JobBoard Fastapi

```sh
# ... 
```

---

## 🗺 Roadmap

- [X] `[📌  INSERT-TASK-TODO]`
- [ ] `[📌  INSERT-TASK-TODO]`
- [ ] `[📌  INSERT-TASK-TODO]`

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

## 📫 Contact

If you have any questions or concerns, please open an issue on GitHub or contact the repo owner at `[📌  your-email@example.com]`


---

## 🙏 Acknowledgments

 `[📌  INSERT-DESCRIPTION]`

---
