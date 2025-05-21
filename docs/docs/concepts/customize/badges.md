<!-- ---
title: Badges
---

## Overview

Badges are simple embeddable icons that display various metrics about your project, such as the number of stars, forks, languages used, CI/CD build status, test coverage, and license. They provide quick information to users and visitors.

Use the `--badge-style` option to customize your project's badges:

```sh
readmeai --badge-style <style_name> --repository <repository_url_or_path>
```

## Badge Types

### Default Badges
- License status
- Last commit timestamp
- Primary programming language
- Total languages count

### Project Badges
- Dependencies and frameworks
- Build status
- Test coverage
- Version information

## Available Styles

Use the `--badge-style` option to select from the following styles:

=== "Default"

    The default badge set includes the project `license`, `last commit`, `top language`, and `total languages`. The *project badge* set is not included. No additional options are required, as this is the default behavior.

    ```sh
    readmeai --repository https://github.com/username/project
    ```

    !!! example "Output Preview"

        ![Default Badge](https://img.shields.io/github/license/eli64s/readme-ai?flat&color=0080ff&logo=opensourceinitiative&logoColor=white)
        ![Default Badge](https://img.shields.io/github/last-commit/eli64s/readme-ai?flat&color=0080ff&logo=git&logoColor=white)
        ![Default Badge](https://img.shields.io/github/languages/top/eli64s/readme-ai?flat&color=0080ff)
        ![Default Badge](https://img.shields.io/github/languages/count/eli64s/readme-ai?flat&color=0080ff)

=== "Flat"

    ```sh
    readmeai --badge-style flat --repository https://github.com/username/project
    ```

    !!! example "Output Preview"

    ![Flat Badge](https://img.shields.io/badge/Python-3776AB.svg?&style=flat&logo=Python&logoColor=white)

=== "Flat-Square"

    ```sh
    readmeai --badge-style flat-square --repository https://github.com/username/project
    ```

    !!! example "Output Preview"

    ![Flat-Square Badge](https://img.shields.io/badge/Python-3776AB.svg?&style=flat-square&logo=Python&logoColor=white)

=== "For-The-Badge"

    ```sh
    readmeai --badge-style for-the-badge --repository https://github.com/username/project
    ```

    !!! example "Output Preview"

    ![For-the-Badge Badge](https://img.shields.io/badge/Python-3776AB.svg?&style=for-the-badge&logo=Python&logoColor=white)

=== "plastic"

    ```sh
    readmeai --badge-style plastic --repository https://github.com/username/project
    ```

    !!! example "Output Preview"

    ![Plastic Badge](https://img.shields.io/badge/Python-3776AB.svg?&style=plastic&logo=Python&logoColor=white)

=== "Skills"

    ```sh
    readmeai --badge-style skills --repository https://github.com/username/project
    ```

    !!! example "Output Preview"

    ![Skills Badge](https://skillicons.dev/icons?i=py)

=== "skills-light"

    ```sh
    readmeai --badge-style skills-light --repository https://github.com/username/project
    ```

    !!! example "Output Preview"

    ![Skills-Light Badge](https://skillicons.dev/icons?i=py&theme=light)

=== "social"

    ```sh
    readmeai --badge-style social --repository https://github.com/username/project
    ```

    !!! example "Output Preview"

    ![Social Badge](https://img.shields.io/badge/Python-3776AB.svg?&style=social&logo=Python&logoColor=FFD845)

## How It Works

README-AI automatically detects your project's dependencies and technologies during the repository ingestion process. It then uses these dependencies and technologies to generate a comprehensive list of relevant badges for your project.

When you provide the `--badge-style` option to the `readmeai` command, two sets of badges are generated:

1. **Default Metadata Badges**: The default set is always included in the generated README file. The default badges include the project `license`, `last commit`, `top language`, and `total languages`.
2. **Project Dependency Badges**: When the `--badge-style` argument is provided to the CLI, a second badge set is generated, representing the extracted dependencies and metadata from your codebase.

The badge sets are formatted in the README header and provide the reader with a quick overview of the project's key metrics and technologies.

## Examples

### Basic Usage
```sh
readmeai --badge-style flat --repository https://github.com/username/project
```

### Custom Colors
```sh
readmeai --badge-color orange --badge-style flat-square --repository https://github.com/username/project
```

### Combined Options

Next, let's combine the `--badge-color` and `--badge-style` options to generate a README with custom badge colors and styles.

```sh
readmeai --badge-color orange \
         --badge-style flat-square \
         --repository https://github.com/eli64s/readme-ai
```

!!! example "Output Preview"

    {{ PROJECT-NAME }}

    {{ PROJECT-DESCRIPTION }}

    ![License](https://img.shields.io/github/license/eli64s/readme-ai?style=flat-square&color=orange&logo=opensourceinitiative&logoColor=white)
    ![Last Commit](https://img.shields.io/github/last-commit/eli64s/readme-ai?style=flat-square&color=orange&logo=git&logoColor=white)
    ![Top Language](https://img.shields.io/github/languages/top/eli64s/readme-ai?style=flat-square&color=orange)
    ![Language Count](https://img.shields.io/github/languages/count/eli64s/readme-ai?style=flat-square&color=orange)

    Tech Stack

    ![pre-commit](https://img.shields.io/badge/precommit-FAB040.svg?style=flat-square&logo=pre-commit&logoColor=black)
    ![Ruff](https://img.shields.io/badge/Ruff-FCC21B.svg?style=flat-square&logo=Ruff&logoColor=black)
    ![GNU Bash](https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat-square&logo=GNU-Bash&logoColor=white)
    ![Pytest](https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat-square&logo=Pytest&logoColor=white)
    ![Docker](https://img.shields.io/badge/Docker-2496ED.svg?style=flat-square&logo=Docker&logoColor=white)
    ![Python](https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white)
    ![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=flat-square&logo=GitHub-Actions&logoColor=white)
    ![Poetry](https://img.shields.io/badge/Poetry-60A5FA.svg?style=flat-square&logo=Poetry&logoColor=white)
    ![AIOHTTP](https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=flat-square&logo=AIOHTTP&logoColor=white)
    ![Material for MkDocs](https://img.shields.io/badge/Material%20for%20MkDocs-526CFE.svg?style=flat-square&logo=Material-for-MkDocs&logoColor=white)
    ![OpenAI](https://img.shields.io/badge/OpenAI-412991.svg?style=flat-square&logo=OpenAI&logoColor=white)
    ![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2.svg?style=flat-square&logo=Google-Gemini&logoColor=white)
    ![Pydantic](https://img.shields.io/badge/Pydantic-E92063.svg?style=flat-square&logo=Pydantic&logoColor=white)

!!! note
        1. The badge color can be specified using a hex code or color name.
            a. `--badge-color orange`
            b. `--badge-color #0080ff`
        2. The `--badge-color` option only affects default badges, while `--badge-style` applies to all badges.

## Style Guidelines

### Best Practices

- **Complementary**: Choose a style that complements your project's overall design.
- **Relevancy**: Use badges to highlight relevant information about your project.
- **Overcrowding**: Too many can clutter your README and make it hard to read.
- **Customize**: Consider using custom badges for project-specific metrics.
- **Accuracy**: Ensure that all badge links are correct and up-to-date.
-->

# Badge Styles

ReadmeAI's badge system enhances your documentation by displaying key metrics and project information through visual indicators. These badges provide instant insights about your project's status, technologies, and characteristics.

## Configuration

Customize your project's badge appearance using the `--badge-style` flag:

```bash
readmeai --badge-style <style> --repository <url-or-path>
```

## Available Styles

=== "default"

    The standard badge set focusing on essential project metrics. This style requires no additional configuration.

    ```bash
    readmeai --repository https://github.com/username/project
    ```

    **Example output:**

    ![License](https://img.shields.io/github/license/eli64s/readme-ai?flat&color=0080ff&logo=opensourceinitiative&logoColor=white)
    ![Last Commit](https://img.shields.io/github/last-commit/eli64s/readme-ai?flat&color=0080ff&logo=git&logoColor=white)
    ![Top Language](https://img.shields.io/github/languages/top/eli64s/readme-ai?flat&color=0080ff)
    ![Language Count](https://img.shields.io/github/languages/count/eli64s/readme-ai?flat&color=0080ff)

=== "flat"

    A modern, clean design with straight edges and consistent height.

    ```bash
    readmeai --badge-style flat --repository https://github.com/username/project
    ```

    **Example output:**

    ![Python Badge](https://img.shields.io/badge/Python-3776AB.svg?&style=flat&logo=Python&logoColor=white)

=== "flat-square"

    Similar to flat style but with squared corners for a more geometric look.

    ```bash
    readmeai --badge-style flat-square --repository https://github.com/username/project
    ```

    **Example output:**

    ![Python Badge](https://img.shields.io/badge/Python-3776AB.svg?&style=flat-square&logo=Python&logoColor=white)

=== "for-the-badge"

    Bold, high-contrast badges with uppercase text for emphasis.

    ```bash
    readmeai --badge-style for-the-badge --repository https://github.com/username/project
    ```

    **Example output:**

    ![Python Badge](https://img.shields.io/badge/Python-3776AB.svg?&style=for-the-badge&logo=Python&logoColor=white)

=== "plastic"

    Badges with a subtle gradient and slight 3D effect.

    ```bash
    readmeai --badge-style plastic --repository https://github.com/username/project
    ```

    **Example output:**

    ![Python Badge](https://img.shields.io/badge/Python-3776AB.svg?&style=plastic&logo=Python&logoColor=white)

=== "skills"

    Minimalist icons representing programming languages and tools.

    ```bash
    readmeai --badge-style skills --repository https://github.com/username/project
    ```

    **Example output:**

    ![Skills Badge](https://skillicons.dev/icons?i=py)

=== "skills-light"

    Light-themed version of the skills style for bright backgrounds.

    ```bash
    readmeai --badge-style skills-light --repository https://github.com/username/project
    ```

    **Example output:**

    ![Skills Light Badge](https://skillicons.dev/icons?i=py&theme=light)

=== "social"

    Social media-inspired badges with counters and icons.

    ```bash
    readmeai --badge-style social --repository https://github.com/username/project
    ```

    **Example output:**

    ![Social Badge](https://img.shields.io/badge/Python-3776AB.svg?&style=social&logo=Python&logoColor=FFD845)

## Technical Details

!!! info "Badge Generation Process"

    ReadmeAI automatically analyzes your repository to:

    - Detect project dependencies and frameworks
    - Identify programming languages used
    - Extract license information
    - Monitor repository metrics
    - Generate appropriate badge sets

!!! tip "Badge Categories"

    The system generates two distinct sets of badges:

    1. Default Metadata Badges:
       - License status
       - Last commit timestamp
       - Primary programming language
       - Total languages count

    2. Project Technology Badges:
       - Dependencies and frameworks
       - Build status indicators
       - Test coverage metrics
       - Version information

## Advanced Usage

Combine badge styles with custom colors to create personalized documentation:

```bash
readmeai --badge-style flat-square \
         --badge-color orange \
         --repository https://github.com/username/project
```

!!! note "Color Customization"

    Badge colors can be specified using:
    - Color names (e.g., `orange`, `blue`)
    - Hex codes (e.g., `#0080ff`)

    The `--badge-color` option affects default badges only, while `--badge-style` applies to all badge types.

## Best Practices

When implementing badges in your documentation, consider these guidelines:

1. Visual Harmony: Choose badge styles that complement your project's overall design aesthetic.
2. Information Relevance: Include badges that provide meaningful insights about your project.
3. Layout Balance: Avoid overcrowding by selecting only the most important metrics to display.
4. Maintenance: Regularly verify that badge links remain active and display current information.
5. Consistency: Maintain a uniform style across all badges within your documentation.

## Service Attribution

The badge system integrates with several leading badge providers:

- Shields.io: Primary badge generation service
- Simple Icons: Icon library for technology badges
- GitHub Profile Badges: Repository metric indicators
- Markdown Badges: Extended badge collection
- Skill Icons: Programming language and tool icons

---
