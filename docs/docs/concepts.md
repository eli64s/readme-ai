<!--

# Core Concepts

Readme-ai is a tool for auto-generating README files for code repositories using AI. Here are some of its key concepts:

## Codebase Analysis

- Traverses the repository directory tree to build a code structure overview
- Extracts metadata like dependencies and languages used
- Analyzes characteristics to inform content generation

## Generative AI

- Uses GPT language models via the OpenAI API
- Structured prompts injected with repository details
- Generates sections like project overview and technical features
- Summarizes code files in markdown tables

## Customization

- Flexible configuration system
- CLI options to tweak badge icons, images, model settings
- Supports different badge styles like flat, plastic, skills
- Can provide custom images and set text align
- Edit prompt templates to influence content

## Modular Design

- Components and parsers decoupled from core logic
- Built using factory and strategy patterns
- Easily extend functionality with new parsers
- Abstracts services like file handling and git ops

## Asynchronous Workflows

- Leverages Python asyncio for non-blocking I/O
- Concurrent networking, disk and CPU bound tasks
- Manages OpenAI rate limits for optimal performance
- Resource management via async context managers

## Robustness

- Exponential backoff retry logic for resilience
- Caching frequently used responses
- Handles Unicode encoding errors gracefully
- Secure temp directories to isolate repository
- Configurable logging for debuggability

By leveraging these concepts and more, readme-ai aims to offer a flexible platform for auto-generating documentation to boost developer productivity.

---

README-AI is a tool for auto-generating detailed README files for software projects using AI. It utilizes several core concepts and components to analyze codebases and produce high-quality documentation.

## Codebase Analysis

README-AI performs an in-depth analysis of the provided codebase to extract key information.

- **File traversal**: Recursively traverse the codebase directory to identify all files. Special cases like ignoring certain files or handling GitHub workflows are handled programmatically.

- **Metadata extraction**: File metadata like name, path, content, language, dependencies etc. are extracted and stored. Popular dependency manifest formats are parsed to detect dependencies.

- **Content preprocessing**: File contents are tokenized to allow smarter content generation tailored to codebase complexity.

The output is a structured `FileData` object that encapsulates file details.

## LLM API Integration

Language Models like GPT-3 are leveraged to generate fluent text for documentation.

- **Modular design**: The LLM API client is abstracted into a separate `ModelHandler` class to allow swapping out different AI providers.

- **Prompt engineering**: Carefully crafted prompt templates are populated with codebase metadata to produce accurate, relevant content.

- **Batching & caching**: Requests are batched and caching used to optimize performance and costs. Exponential backoff retries handle errors.

Generated text is inserted into Markdown templates to build a full-fledged README.

## Configuration-driven

The tool relies extensively on configuration using Pydantic models.

- **Settings**: Central settings file with common constants and file paths. Helper configuration provides additional customization.

- **Validation**: Rigorous validations are performed on settings like repository URL to prevent errors.

- **Extensibility**: Adding new features or functionality requires minimal code changes due to config-driven design.

Overall, this promotes maintainability, testability and flexibility.

## Customizable Output

Users can customize the look and feel of the generated README by providing a range of CLI options.

- **Appearance**: Choose badge styles, header images, align options and more for unique styling.

- **Content**: Control language model behavior with parameters like temperature and max tokens. Toggle emojis in text.

- **Templates**: (WIP) Generate focused READMEs for domains like machine learning, webdev etc.

In summary, README-AI aims to simplify documentation through intelligent automation, while keeping the user in control.

---

-->

# Concepts

The readme-ai CLI tool provides several configurations that control how it operates and generates README.md files. We will explore these configurations and settings in detail in this document.

## Core Components

At the heart of the readme-ai CLI tool lies the main `AppConfig` class, responsible for storing all configuration settings related to the CLI. Additionally, there is a nested `AppConfigModel` class that extends Pydantic's `BaseModel` to add validation capabilities.

### AppConfig

The `AppConfig` class stores primary configuration categories, namely `cli`, `files`, `git`, `llm`, `md`, and `prompts`. Each category contains specific settings controlling various parts of the tool. Let's discuss each category individually.

#### Cli

The `cli` category holds boolean settings related to the CLI itself, primarily `emojis` and `offline`. The `emojis` flag determines whether emojis appear alongside the section titles within the README.md file. Meanwhile, activating the `offline` flag enables the generation of a README.md file without requiring API calls, providing placeholders where LLM-generated content would normally go.

#### Files

The `files` category manages various file paths used in the application. Specific properties include `dependency_files`, `identifiers`, `ignore_files`, `language_names`, `language_setup`, `output`, `shieldsio_icons`, and `skill_icons`. All these fields hold either absolute file paths or relative references to files managed by the application.

#### Git

The `git` category captures the necessary repository settings, ensuring correct interaction between the readme-ai CLI tool and the target repository. Properties consist of `repository`, `full_name`, `host`, `name`, and `source`. The latter three optional fields get populated during validation performed by the `RepositoryValidator` class.

#### Llm

The `llm` category houses settings pertinent to the LLM API employed by the tool. Fields like `content`, `endpoint`, `encoding`, `model`, `temperature`, `tokens`, `tokens_max`, and `rate_limit` define the behavior of the LLM API during execution.

#### Md

The `md` category groups together Markdown template blocks utilized in constructing the final README.md file. Examples include `align`, `default`, `badge_color`, `badge_style`, `badges_software`, `badges_shields`, `badges_skills`, `contribute`, `features`, `header`, `image`, `modules`, `modules_widget`, `overview`, `quickstart`, `slogan`, `tables`, `toc`, `tree`, among others.

#### Prompts

Finally, the `prompts` category maintains the prompt templates critical in generating appropriate text for the README.md file. Included fields cover `features`, `overview`, `slogan`, and `summaries`.

### Config Helper

The `ConfigHelper` class plays a crucial role as a helper module for managing extra configuration files beyond the primary `AppConfigModel`. Using a secondary `FileHandler` object, the `ConfigHelper` loads multiple configuration files simultaneously, merging them seamlessly into the existing configuration hierarchy.

#### Dependency Files

Dependency files referenced within the `dependency_files` property indicate external configuration files holding important values affecting the overall behavior of the readme-ai CLI tool. When present, the `ConfigHelper` consolidates these dependencies within a dedicated field called `dependency_files`.

#### Ignore Files

Similarly, ignore files listed in the `ignore_files` property specify particular patterns matching files to exclude during certain operations carried out by the readme-ai CLI tool. Analogous to the `dependency_files` treatment, `ignore_files` gets combined into a corresponding field within the `ConfigHelper` class.

#### Language Names

`language_names` consists of mappings associating specific programming languages with human-friendly labels presented in the README.md file. For instance, a label such as "Python" could correspond to the programming language identifier "py".

#### Language Setup

Lastly, `language_setup` comprises instructions describing how to initialize diverse environments supporting various programming languages. By combining these directives, developers can effortlessly prepare suitable platforms for executing code samples featured in the README.md file.

## Validators

Validators serve as specialized utility functions tasked with verifying consistency across distinct elements comprising the larger configuration schema. They perform checks ranging from presence confirmation to compatibility assessment, guaranteeing reliable interactions amongst interconnected entities.

### RepositoryValidator

One prominent validator is the `RepositoryValidator` class, responsible for examining fundamental attributes linked to a given repository. Notably, it ensures correct population of fields like `full_name`, `host`, `name`, and `source` depending on the supplied `repository` value. Furthermore, the `RepositoryValidator` performs mandatory sanity checks concerning the availability and accessibility of the designated repository prior to proceeding with subsequent stages of the configuration process.

## Enums

Enums, short for enumerations, constitute a collection of symbolic names representing distinct constant values. Within the readme-ai CLI tool, enums play an integral part in standardizing choices offered to end-users interacting with the CLI. Three notable enums stand out:

### GitService

`GitService` offers a concise means of specifying popular Git hosting services utilizing descriptive terms familiar to most developers. Supported options include Local, GitHub, GitLab, and Bitbucket.

### BadgeOptions

`BadgeOptions` presents a range of possible styles applicable to README.md file badges. Choices vary from plain representations to visually rich alternatives adorned with gradients and borders.

### ImageOptions

Lastly, `ImageOptions` delineates an array of plausible project logo candidates, facilitating easy selection of appealing visual assets accompanying the README.md file header. Users enjoy the convenience of choosing between preset imagery or supplying custom URLs pointing towards alternative logos.

---
