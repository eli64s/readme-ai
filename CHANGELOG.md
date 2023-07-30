<!--
## [Unreleased]
### Added
### Changed
### Deprecated
### Removed
### Fixed
### Security
-->

# Changelog

All notable changes to this project will be documented in this file.

---

## [v0.0.1] - *2023-06-28*

### Added
- 📍 Initial release of *readme-ai* v0.0.1
### Changed

- 📜 Refine the markdown template structure to be more readable.
### Fixed

- 🔩 Fix various exceptions occuring in [builder.py](./src/builder.py), [model.py](./src/model.py), and [preprocess.py](./src/preprocess.py).

### Removed

- 🐼 Remove `pandas` dependency from the project.

---

## [v0.0.2] - *2023-06-28*

### Added

- 📃 Add [CHANGELOG.md](./CHANGELOG.md) to track changes to the project.
- 📼 Add new directory [examples/video](./examples/video) to store mp4 videos to demonstrate the *readme-ai* tool.

### Changed

- 🖋 Update [Makefile](./Makefile) and [setup.sh](./setup/setup.sh) to use *poetry* for dependency management.

### Removed

- 🔧 Remove [requirements.txt](./requirements.txt) from the installation and setup scripts.
- 📄 Remove outdated example README.md files from the [examples](./examples) directory.

---

## [v0.0.3] - *2023-06-29*

### Added

- 🪄 Add [pydantic](https://pydantic-docs.helpmanual.io/) to validate the user's repository and api key inputs.
  - Validation was moved from *main.py* to *conf.py*.
- 📖 Update [README.md](./README.md) file contents.
  - Add Changelog section
  - Reformat HTML code blocks

### Removed

- 📦 Remove [dacite](https://dacite.readthedocs.io/en/stable/) dependency now that *pydantic* is used for dataclass creation.

---

## [v0.0.4] - *2023-07-29*

### Added

- ⚙️ Add script to handle custom exceptions [exceptions.py](./src/exceptions.py).
- 📖 Update [README.md](./README.md) file contents.
  - Modify docker commands to use the tag `readme-ai:0.0.4`.

### Fixed

- 🐳 Update Dockerfile with the latest dependencies + *tree* command installation.

---
