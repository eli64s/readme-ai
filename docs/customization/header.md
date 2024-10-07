---
title: "Header Templates"
---

# Header Templates

A *header* is the first section of a README file that typically contains the project's logo, name, slogan, and badges. It serves as an introduction to the project and provides context for its contents.

README-AI allows you to customize the style of the header in your generated README files by selecting from a set of predefined header templates. This feature lets you control the layout and appearance of your project's header section, including the alignment of logos, repository names, and additional badges or icons.

## CLI Usage for Header Styles

When using the `readmeai` CLI, you can define the header style using the `--header-style` option. This enables you to select from a variety of predefined styles.

### Supported Header Styles:

1. **Classic** (`classic`)
   - A traditional, centered layout with a large project logo, title, and badges. Default style if no header style is specified.

2. **Compact** (`compact`)
   - A space-efficient layout with the logo aligned to the left, followed by the project name and badges in a smaller footprint.

3. **Modern** (`modern`)
   - A sleek and modern look with the logo aligned to the right and a minimalistic header format.

## Example CLI Command

To generate a README file with the **Modern** header style, run the following command:

```bash
readmeai --repository ./my_project --header-style modern --output README.md
```

In this example:
- The `--repository` flag points to your local project directory or a remote repository.
- The `--header-style modern` flag specifies that the "Modern" header template should be used.
- The `--output README.md` flag sets the output file name to `README.md`.

### Another Example with Compact Header Style

To generate a README file with the **Compact** header style, run:

```bash
readmeai --repository ./my_project --header-style compact --output README.md
```

This will generate a more condensed version of the header, suitable for projects where you want to minimize the space taken by the header.

## Available Header Styles

```bash
-hs, --header-style [classic|compact|modern]
```

The `--header-style` option supports the following values:

- **classic**: Traditional centered header with logo and title.
- **compact**: Left-aligned logo and a compact project title.
- **modern**: Right-aligned logo with a modern aesthetic for the header.

<!--
## Customizing Header Alignment

Additionally, you can customize the alignment of the header sections using the `--align` option. Supported alignments are `center`, `left`, or `right`.

### Example Command with Alignment:

```bash
readmeai --repository ./my_project --header-style classic --align left --output README.md
```

This command sets the header style to **Classic** but aligns all the sections (logo, title, badges) to the left instead of the default center alignment.

## Project Logo Customization

You can also customize the logo displayed in the header using the `--image` option. Options include providing a custom URL, generating a logo with an LLM, or using one of the predefined themes (`black`, `blue`, `cloud`, `gradient`, etc.).

### Example Command with Logo:

```bash
readmeai --repository ./my_project --header-style modern --image CUSTOM --output README.md
```

In this case, the header will use the **Modern** style, and you will be prompted to provide a custom logo URL or local file path.

## Emoji Support for Headers

If you want to add emojis to your header titles (e.g., "## 📍 Overview"), use the `--emojis` option:

```bash
readmeai --repository ./my_project --header-style modern --emojis --output README.md
```

This will prepend relevant emojis to each section header, enhancing the visual appeal of your README file.

---

## How to Customize the Header

To customize the header template, you can initialize the `HeaderTemplate` class and pass your preferred style (`classic`, `compact`, or `modern`). Here's an example:

```python
from readmeai.templates.header import HeaderTemplate, HeaderStyleOptions

# Initialize the template with the desired style
header_template = HeaderTemplate(style=HeaderStyleOptions.MODERN)

# Data to render in the header
data = {
    "align": "center",
    "image": "https://example.com/logo.png",
    "image_width": "100px",
    "repo_name": "My Awesome Project",
    "slogan": "Building the future, one commit at a time.",
    "shields_icons": "<shields.io badge here>",
    "badges_tech_stack": "<badge icons here>",
}

# Render the template with the provided data
header_content = header_template.render(data)

# Output the rendered content
print(header_content)
```

## Adding a New Header Style

If you wish to add your own custom header style, simply extend the `HeaderStyleOptions` enum and the `HEADER_TEMPLATES` dictionary with your own template string. Ensure that your template follows the same format placeholders (`{repo_name}`, `{image}`, etc.) as the existing templates.

```python
class HeaderStyleOptions(enum.Enum):
    CLASSIC = "classic"
    COMPACT = "compact"
    MODERN = "modern"
    CUSTOM = "custom"  # Add new custom style here

HeaderTemplate.HEADER_TEMPLATES[HeaderStyleOptions.CUSTOM] = """\
# Custom header template here
"""
```

By customizing and extending the header templates, you can fully control the look and feel of your README header to match your project’s branding and style.

---
-->
