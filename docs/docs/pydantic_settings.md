# Configuration Models and Enums

This page documents the data models and enums used for configuring the `readme-ai` CLI tool. These models are based on [Pydantic](https://pydantic-docs.helpmanual.io/), which allows for data parsing and validation through Python type annotations.

## Git Settings

`GitSettings` is used to represent and validate repository settings.

### Fields

- `repository`: A string or `Path` representing the location of the repository.
- `full_name`: An optional string denoting the full name of the repository in 'username/repo' format.
- `host`: An optional string representing the Git service host.
- `name`: An optional string for the repository name.
- `source`: An optional string representing the source Git service.

### Validators

Custom validators are used to ensure that the repository information is correct and that the `full_name`, `host`, `name`, and `source` fields are derived correctly from the `repository` field.

## CLI Settings

`CliSettings` manages the command-line interface options for the `readme-ai` application.

### Fields

- `emojis`: A boolean indicating whether to use emojis.
- `offline`: A boolean specifying if the tool should run in offline mode.

## File Settings

`FileSettings` defines paths related to different configurations and output.

### Fields

- `dependency_files`: The path to the file containing dependency configurations.
- `identifiers`: The path to the file with identifiers.
- `ignore_files`: The path to the file listing files to ignore.
- `language_names`: The path to the file with language names mapping.
- `language_setup`: The path to the file with language setup instructions.
- `output`: The path for the output file (e.g., `README.md`).
- `shields_icons`: The path to the file with shield icon configurations.
- `skill_icons`: The path to the file with skill icon configurations.

## Enums

The application uses several `Enum` classes to represent various configurations.

### GitService

`GitService` is an enum that includes:

- `LOCAL`: Local repository.
- `GITHUB`: GitHub repository.
- `GITLAB`: GitLab repository.
- `BITBUCKET`: Bitbucket repository.

Each service has properties for `api_url` and `file_url_template` to facilitate integration with the respective Git service.

### BadgeOptions

`BadgeOptions` represents the available styles for badges in the README files, such as:

- `DEFAULT`
- `FLAT`
- `FLAT_SQUARE`
- `FOR_THE_BADGE`
- `PLASTIC`
- `SKILLS`
- `SKILLS_LIGHT`
- `SOCIAL`

### ImageOptions

`ImageOptions` enumerates the available choices for images used in the README header, including:

- `CUSTOM`
- `DEFAULT`
- `BLACK`
- `GREY`
- `PURPLE`
- `YELLOW`
- `CLOUD`

---
