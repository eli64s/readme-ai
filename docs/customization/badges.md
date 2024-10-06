# Badges

A badge is a simple embeddable icon that displays various metrics such as the the number of stars or forks for a repository, languages used in the project, CI/CD build status, test coverage, the license of the project, and more. Badges are a great way to provide quick information about your project to users and visitors.

README-AI offers various badge styles to enhance your project's README. This guide explains how to use and customize these badges.

## Badge Styles

Use the `--badge-style` option to select from the following styles:

<div class="grid" markdown>

=== "default"
    ![Default Badge](https://img.shields.io/github/license/eli64s/readme-ai?flat&color=0080ff&logo=opensourceinitiative&logoColor=white)
    ![Default Badge](https://img.shields.io/github/last-commit/eli64s/readme-ai?flat&color=0080ff&logo=git&logoColor=white)
    ![Default Badge](https://img.shields.io/github/languages/top/eli64s/readme-ai?flat&color=0080ff)
    ![Default Badge](https://img.shields.io/github/languages/count/eli64s/readme-ai?flat&color=0080ff)

=== "flat"
    ![Flat Badge](https://img.shields.io/badge/Python-3776AB.svg?&style=flat&logo=Python&logoColor=white)

=== "flat-square"
    ![Flat-Square Badge](https://img.shields.io/badge/Python-3776AB.svg?&style=flat-square&logo=Python&logoColor=white)

=== "for-the-badge"
    ![For-the-Badge Badge](https://img.shields.io/badge/Python-3776AB.svg?&style=for-the-badge&logo=Python&logoColor=white)

=== "plastic"
    ![Plastic Badge](https://img.shields.io/badge/Python-3776AB.svg?&style=plastic&logo=Python&logoColor=white)

=== "skills"
    ![Skills Badge](https://skillicons.dev/icons?i=py)

=== "skills-light"
    ![Skills-Light Badge](https://skillicons.dev/icons?i=py&theme=light)

=== "social"
    ![Social Badge](https://img.shields.io/badge/Python-3776AB.svg?&style=social&logo=Python&logoColor=FFD845)

</div>

## How It Works

README-AI automatically detects your project's dependencies and technologies during the repository ingestion process. It then uses these dependencies and technologies to generate a comprehensive list of relevant badges for your project.

When you provide the `--badge-style` option to the `readmeai` command, two sets of badges are generated:

1. **Default Metadata Badges**: The default set is always included in the generated README file. The default badges includes the project `license`, `last commit`, `top language`, and `total languages`.
2. **Project Dependency Badges**: When the `--badge-style` argument is provided to the CLI, a second badge set is generated, representing the extracted dependencies and metadata from your codebase.

The badge sets are formatted in the README header, and provide the reader with a quick overview of the project's key metrics and technologies.

## Example Usage

Let's generate a README with custom badge colors and styles using the `--badge-color` and `--badge-style` options:

```bash
readmeai --badge-color orange
         --badge-style flat-square
         --repository https://github.com/eli64s/readme-ai
```

The command above generates a README with the following badge configuration:

<div class="grid cards" markdown>

-
    {{ start_of_header }}

    {{ project_logo }}

    {{ project_name }}

    {{ project_slogan }}

    <img src="https://img.shields.io/github/license/eli64s/readme-ai?style=flat-square&color=orange&logo=opensourceinitiative&logoColor=white">
    <img src="https://img.shields.io/github/last-commit/eli64s/readme-ai?style=flat-square&color=orange&logo=git&logoColor=white">
    <img src="https://img.shields.io/github/languages/top/eli64s/readme-ai?style=flat-square&color=orange">
    <img src="https://img.shields.io/github/languages/count/eli64s/readme-ai?style=flat-square&color=orange">
    <br>

    <em>Built with the tools and technologies:</em>

    <img src="https://img.shields.io/badge/precommit-FAB040.svg?style=flat-square&logo=pre-commit&logoColor=black" alt="precommit">
    <img src="https://img.shields.io/badge/Ruff-FCC21B.svg?style=flat-square&logo=Ruff&logoColor=black" alt="Ruff">
    <img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat-square&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
    <img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat-square&logo=Pytest&logoColor=white" alt="Pytest">
    <img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat-square&logo=Docker&logoColor=white" alt="Docker">
    <img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=flat-square&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions">
    <br>
    <img src="https://img.shields.io/badge/Poetry-60A5FA.svg?style=flat-square&logo=Poetry&logoColor=white" alt="Poetry">
    <img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=flat-square&logo=AIOHTTP&logoColor=white" alt="AIOHTTP">
    <img src="https://img.shields.io/badge/Material%20for%20MkDocs-526CFE.svg?style=flat-square&logo=Material-for-MkDocs&logoColor=white" alt="Material%20for%20MkDocs">
    <img src="https://img.shields.io/badge/OpenAI-412991.svg?style=flat-square&logo=OpenAI&logoColor=white" alt="OpenAI">
    <img src="https://img.shields.io/badge/Google%20Gemini-8E75B2.svg?style=flat-square&logo=Google-Gemini&logoColor=white" alt="Google%20Gemini">
    <img src="https://img.shields.io/badge/Pydantic-E92063.svg?style=flat-square&logo=Pydantic&logoColor=white" alt="Pydantic">
    <br>

    {{ end_of_header }}

</div>

!!! note
    The `--badge-color` option **only** modifies the default badge set, while the `--badge-style` option is applied to **both** the default and project dependency badges.

## Tips for Using Badges

- Choose a badge style that complements your project's overall design.
- Use badges to highlight relevant information about your project, such as license, build status, and test coverage.
- Don't overuse badges – too many can clutter your README and make it hard to read.
- Ensure that all badge links are correct and up-to-date.
- Consider using custom badges for project-specific information or metrics.

## References

Thank you to the following projects for providing the badges used in this project:

- [Shields.io](https://shields.io/)
- [Aveek-Saha/GitHub-Profile-Badges](https://github.com/Aveek-Saha/GitHub-Profile-Badges)
- [Ileriayo/Markdown-Badges](https://github.com/Ileriayo/markdown-badges)
- [tandpfun/skill-icons](https://github.com/tandpfun/skill-icons)

---
