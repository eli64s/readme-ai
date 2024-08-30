# Installation

Install `readmeai` using one of the following methods:

### Pip

```sh
pip install readmeai
```

### Pipx

[pipx](https://pipxproject.github.io/pipx/installation/) is recommended for installing Python CLI applications:

```sh
pipx install readmeai
```

### Docker

```sh
docker pull zeroxeli/readme-ai:latest
```

### From Source

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

For usage instructions, see the [Usage](usage/cli.md) documentation.
