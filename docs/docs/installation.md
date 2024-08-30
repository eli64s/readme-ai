# Installation

Readme-ai can be installed using several methods. Choose the one that best fits your workflow.

## Prerequisites

- Python 3.9+
- Package manager/Container: `pip`, `pipx`, `docker`

## Using pip

```sh
pip install readmeai
```

## Using pipx

[pipx](https://pipxproject.github.io/pipx/installation/) is recommended for installing Python CLI applications:

```sh
pipx install readmeai
```

## Using Docker

```sh
docker pull zeroxeli/readme-ai:latest
```

## From source

1. Clone the repository:
   ```sh
   git clone https://github.com/eli64s/readme-ai
   cd readme-ai
   ```

2. Install using one of the following methods:

   Using bash:
   ```sh
   bash setup/setup.sh
   ```

   Using poetry:
   ```sh
   poetry install
   ```

After installation, verify that readme-ai is correctly installed by running:

```sh
readmeai --version
```

For usage instructions, see the [Usage](usage.md) guide.
