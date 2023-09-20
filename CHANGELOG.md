<!--

## [v0.0.0] - *2023-01-01*
### 🐛 Bug Fixes
### 🛠 Changes
### ✨ Features
### 🗑 Removed
### 🔐 Security
### 🧹 Chore
### ⚙️ Deprecated

-->

# Changelog

All notable changes to the *readme-ai* project will be documented in this file.

---

## [v0.1.0] - *2023-09-20*
### ✨ Features

-  Deploy *readme-ai* on Streamlit Community Cloud.

---
## [v0.0.9] - *2023-09-19*

### 🧹 Chore

- Update README file to enhance project documentation.
  - Add [Configuration](https://github.com/eli64s/readme-ai/blob/main/README.md#-configuration) section to provide context for customizing the tool.
  - Simplify [Getting Started](https://github.com/eli64s/readme-ai/blob/main/README.md#-getting-started) section install and run instructions.
  - Update [Roadmap](https://github.com/eli64s/readme-ai/blob/main/README.md#-roadmap) section with latest project goals.

---

## [v0.0.8] - *2023-09-18*

### 🐛 Bug Fixes

- Update file parsing logic in [parse.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/parse.py) and [preprocess.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/preprocess.py) for codebases containing the following dependency files (issue [#37](https://github.com/eli64s/readme-ai/issues/37)).
  - *CMakeLists.txt*
  - *Makefile.am*
  - *configure.ac*
- Credit to [@mooujarrar](https://github.com/mooujarrar) for the help in solving this issue!
### 🔐 Security

- Bump [gitpython](https://github.com/gitpython-developers/GitPython) module to version *3.1.36* to address security vulnerability (Dependabot Alert [#5](https://github.com/eli64s/readme-ai/security/dependabot/5) and issue [#43](https://github.com/eli64s/readme-ai/issues/43)).

---

## [v0.0.7] - *2023-08-30*

⚠️ Release v0.0.7 addresses a security vulnerability cloning git repositories via the *GitPython* package on Windows systems. This vulnerability could allow arbitrary command execution if code is run from a directory containing a malicious `git.exe` or `git` executable.

### 🔐 Security
#### *Arbitrary Command Execution Mitigation*

- Dependabot Alert [#3](https://github.com/eli64s/readme-ai/security/dependabot/3): GitPython untrusted search path on Windows systems leading to arbitrary code execution.
- The previous git clone implementation sets the `env` argument to the path of the git executable in the current working directory. This poses a security risk as the code is susceptible to running arbitrary `git` commands from a malicious repository.
    ```python
    git.Repo.clone_from(repo_path, temp_dir, depth=1)
    ```
- Updated the `env` argument to explicitly set the absolute path of the git executable. This ensures that the git executable used to clone the repository is the one thats installed in the system path, and not the one located in the current working directory.
    ```python
    git.Repo.clone_from(repo_path, temp_dir, depth=1, env=git_exec_path)
    ```
### ✨ Features and Enhancements

#### *Code Modularity*

- Introduced three methods to help isolate the Git executable discovery and validation logic.
  - `find_git_executable()`: Determines the absolute path of the Git executable.
  - `validate_git_executable()`: Validates the found Git executable path.
  - `validate_file_permissions()`: Validates the file permissions of the cloned repository.

#### *File Permission Checks*

- For Unix systems, added checks to ensure the permissions of the cloned repository are set to `0o700`. This is a best practice for secure temporary directories and prevents unauthorized users from accessing the directory.

⚠️ These updates aim to mitigate the vulnerbility raised in Dependabot alert [#3](https://github.com/eli64s/readme-ai/security/dependabot/3). Users are advised to update *readme-ai* to the latest version, i.e ```pip install --upgrade readmeai```. Please be mindful of this vulnerability and use caution when cloning repositories from untrusted sources, especially for Windows users.

---

## [v0.0.6] - *2023-08-29*

### 🐛 Bug Fixes

- Corrected PyPI issue where the *readmeai* package was not being installed correctly.
  - The [conf](./readmeai/conf/) directory was not being included in the PyPI distribution as it was located in the project's root directory.
  - The tool now uses the [pkg_resources](https://setuptools.pypa.io/en/latest/pkg_resources.html#) module to access the *conf* directory from the *readmeai* package.

---

## [v0.0.5] - *2023-07-31*

### ✨ Features and Enhancements

- Add [.dockerignore](./.dockerignore) file to exclude unnecessary files from the Docker image.

### 🐛 Bug Fixes

- Missing html closing tags in README tables were causing the GitHub pages site to render incorrectly.
  - Added closing tags to fix the issue.
  - Additionally, restructured a few sections of the README.

### 🔐 Security

- Refactor Dockerfile to adhere to best practices.
  - *Package Installation and Cleanup:* Clean up cache after installing packages with apt-get to reduce the image size.
  - *Non-root User Creation:* Introduce a non-root user within the container to limit permissions and enhance security.
    - Assign a specific user ID and group ID that don't have superuser privileges.
  - *File Permissions Management:* Explicitly manage file permissions to prevent potential security risks when the image operates in varied contexts.

---

## [v0.0.4] - *2023-07-30*

### ✨ Features and Enhancements

- Publish *readme-ai* CLI to PyPI under the module name [readmeai](https://pypi.org/project/readmeai/).
  - Refactored the codebase to use [Click](https://click.palletsprojects.com/en/8.1.x/), migrating from argparse.
  - Update directory name from *src* to *readmeai* to match PyPI module name.
  - Update [readmeai](./readmeai/) modules to use relative imports.
  - Update metadata and dependency details in the [pyproject.toml](./pyproject.toml) file.
- Update [README.md](./README.md) documentation.
  - Add *PyPI* package badges at the top of the README.
  - Include instructions for downloading and running the *readme-ai* CLI from PyPI.
- Add helper script [update_image.sh](./scripts/update_image.sh) to push the latest image to Docker Hub.

### 🐛 Bug Fixes

- Update Dockerfile commands
  - Add line to install the *tree* command in order to generate the repository tree structure in the README.
  - Update installation to use the latest *readmeai* distribution from PyPI.

### 🗑 Removed

- Removed *setup.py* script from the project root directory.
  - Poetry is used for package management via [pyproject.toml](./pyproject.toml). Thus, *setup.py* is no longer needed.

---

## [v0.0.3] - *2023-06-29*

### ✨ Features and Enhancements

- Add [pydantic](https://pydantic-docs.helpmanual.io/) to validate the user's repository and api key inputs.
  - Validation was moved from *main.py* to *conf.py*.
- Update [README.md](./README.md) file contents.
  - Add Changelog section
  - Reformat HTML code blocks

### 🗑 Removed

- Remove [dacite](https://dacite.readthedocs.io/en/stable/) dependency now that *pydantic* is used for dataclass creation.

---

## [v0.0.2] - *2023-06-28*

### ✨ Features and Enhancements

- Add [CHANGELOG.md](./CHANGELOG.md) to track changes to the project.
- Add new directory [examples/video](./examples/video) to store mp4 videos to demonstrate the *readme-ai* tool.

### 🛠 Changes

- Update [Makefile](./Makefile) and [setup.sh](./setup/setup.sh) to use *poetry* for dependency management.

### 🗑 Removed

- 🔧 Remove [requirements.txt](./requirements.txt) from the installation and setup scripts.
- 📄 Remove outdated example README.md files from the [examples](./examples) directory.

---

## [v0.0.1] - *2023-06-28*

### ✨ Features and Enhancements
- Initial release of *readme-ai* v0.0.1

### 🛠 Changes

- Refine the markdown template structure to be more readable.

### 🐛 Bug Fixes

- Fix various exceptions occurring in [builder.py](./src/builder.py), [model.py](./src/model.py), and [preprocess.py](./src/preprocess.py).

### 🗑 Removed

- Remove `pandas` dependency from the project.

---
