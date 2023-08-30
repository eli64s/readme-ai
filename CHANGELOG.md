<!--
## [Unreleased]
### ➕ Added
### 🛠 Changed
### ⚙️ Deprecated
### 🗑 Removed
### 🐛 Bug Fixes
### 🛡 Security
-->

# Changelog

All notable changes to the *readme-ai* project will be documented in this file.

---

## [v0.0.6] - *2023-08-29*

### 🐛 Bug Fixes

- Corrected PyPI issue where the *readmeai* package was not being installed correctly.
  - The [conf](./readmeai/conf/) directory was not being included in the PyPI distribution as it was located in the project's root directory.
  - The tool now uses the [pkg_resources](https://setuptools.pypa.io/en/latest/pkg_resources.html#) module to access the *conf* directory from the *readmeai* package.

---

## [v0.0.5] - *2023-07-31*

### ➕ Added

- Add [.dockerignore](./.dockerignore) file to exclude unnecessary files from the Docker image.

### 🐛 Bug Fixes

- Missing html closing tags in README tables were causing the GitHub pages site to render incorrectly.
  - Added closing tags to fix the issue.
  - Additionally, restructured a few sections of the README.

### 🛡️ Security

- Refactor Dockerfile to adhere to best practices.
  - *Package Installation and Cleanup:* Clean up cache after installing packages with apt-get to reduce the image size.
  - *Non-root User Creation:* Introduce a non-root user within the container to limit permissions and enhance security.
    - Assign a specific user ID and group ID that don't have superuser privileges.
  - *File Permissions Management:* Explicitly manage file permissions to prevent potential security risks when the image operates in varied contexts.

---

## [v0.0.4] - *2023-07-30*

### ➕ Added

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

### ➕ Added

- Add [pydantic](https://pydantic-docs.helpmanual.io/) to validate the user's repository and api key inputs.
  - Validation was moved from *main.py* to *conf.py*.
- Update [README.md](./README.md) file contents.
  - Add Changelog section
  - Reformat HTML code blocks

### 🗑 Removed

- Remove [dacite](https://dacite.readthedocs.io/en/stable/) dependency now that *pydantic* is used for dataclass creation.

---

## [v0.0.2] - *2023-06-28*

### ➕ Added

- Add [CHANGELOG.md](./CHANGELOG.md) to track changes to the project.
- Add new directory [examples/video](./examples/video) to store mp4 videos to demonstrate the *readme-ai* tool.

### 🛠 Changed

- Update [Makefile](./Makefile) and [setup.sh](./setup/setup.sh) to use *poetry* for dependency management.

### 🗑 Removed

- 🔧 Remove [requirements.txt](./requirements.txt) from the installation and setup scripts.
- 📄 Remove outdated example README.md files from the [examples](./examples) directory.

---

## [v0.0.1] - *2023-06-28*

### ➕ Added
- Initial release of *readme-ai* v0.0.1

### 🛠 Changed

- Refine the markdown template structure to be more readable.

### 🐛 Bug Fixes

- Fix various exceptions occurring in [builder.py](./src/builder.py), [model.py](./src/model.py), and [preprocess.py](./src/preprocess.py).

### 🗑 Removed

- Remove `pandas` dependency from the project.

---
