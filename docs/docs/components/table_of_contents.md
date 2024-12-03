# Table of Contents *🚧 WIP*

A table of contents (TOC) helps users navigate through your README by providing a structured overview of all sections. README-AI offers various TOC styles to enhance readability and organization of your documentation.

## TOC Style Options

Use the `--toc-style` option to select from the following styles:

=== "BULLET"

    ## 🔗 Table of Contents

    - [Overview](https://github.com/eli64s/readme-ai/tree/main?tab=readme-ov-file#-overview)
    - [Features](https://github.com/eli64s/readme-ai/tree/main?tab=readme-ov-file#%EF%B8%8F-installation)
    - [Installation](https://github.com/eli64s/readme-ai/tree/main?tab=readme-ov-file#%EF%B8%8F-installation)
    - [Usage](https://github.com/eli64s/readme-ai/tree/main?tab=readme-ov-file#%EF%B8%8F-installation)
    - [Contributing](https://github.com/eli64s/readme-ai/tree/main?tab=readme-ov-file#%EF%B8%8F-installation)
    - [License](https://github.com/eli64s/readme-ai/tree/main?tab=readme-ov-file#%EF%B8%8F-installation)

    ---

=== "FOLD"

    *🚧 WIP*

=== "NUMBER"

    ## 🔗 Table of Contents

    1. [Overview](https://github.com/eli64s/readme-ai/tree/main?tab=readme-ov-file#-overview)
    2. [Features](https://github.com/eli64s/readme-ai/tree/main?tab=readme-ov-file#%EF%B8%8F-installation)
    3. [Installation](https://github.com/eli64s/readme-ai/tree/main?tab=readme-ov-file#%EF%B8%8F-installation)
    4. [Usage](https://github.com/eli64s/readme-ai/tree/main?tab=readme-ov-file#%EF%B8%8F-installation)
    5. [Contributing](https://github.com/eli64s/readme-ai/tree/main?tab=readme-ov-file#%EF%B8%8F-installation)
    6. [License](https://github.com/eli64s/readme-ai/tree/main?tab=readme-ov-file#%EF%B8%8F-installation)

    ---

=== "LINKS"

    *🚧 WIP*

=== "ROMAN"

    ## 🔗 Table of Contents

    I. [Overview](https://github.com/eli64s/readme-ai/tree/main?tab=readme-ov-file#-overview)<br>
    II. [Features](https://github.com/eli64s/readme-ai/tree/main?tab=readme-ov-file#%EF%B8%8F-installation)<br>
    III. [Installation](https://github.com/eli64s/readme-ai/tree/main?tab=readme-ov-file#%EF%B8%8F-installation)<br>
    IV. [Usage](https://github.com/eli64s/readme-ai/tree/main?tab=readme-ov-file#%EF%B8%8F-installation)<br>
    V. [Contributing](https://github.com/eli64s/readme-ai/tree/main?tab=readme-ov-file#%EF%B8%8F-installation)<br>
    VI. [License](https://github.com/eli64s/readme-ai/tree/main?tab=readme-ov-file#%EF%B8%8F-installation)<br>

    ---

## How It Works

README-AI automatically generates a table of contents based on the headers in your README file. The process involves:

1. **Section Detection**: Analyzes markdown headers (H1-H6) in your content
2. **Anchor Generation**: Creates anchor links by converting headers to URL-friendly format
3. **Style Application**: Formats the TOC according to your chosen style
4. **Hierarchy Preservation**: Maintains proper nesting of subsections (where applicable)

## Usage

Using the default *bullet* style:

```sh
readmeai --toc-style bullet --repository https://github.com/username/project
```

Using the *fold* style, which nests the index under a collapsible section:

```sh
readmeai --toc-style fold --repository https://github.com/username/project
```

Customizing the TOC with additional CLI options:

```sh
readmeai --toc-style number \
         --header-style modern \
         --badge-style flat \
         --repository https://github.com/username/project
```
