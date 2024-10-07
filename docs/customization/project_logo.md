# Project Logo

A project logo is a visual representation of your project that appears at the top of your README file. It helps to brand your project and make it more recognizable. README-AI offers various options for adding a logo to your project's README.

## Logo Options

Use the `--image` option to select from the following logo styles:

=== "Blue"

    ![Blue Logo](https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg){: style="width:100px"}

=== "Gradient"

    ![Gradient Logo](https://img.icons8.com/?size=512&id=55494&format=png){: style="width:100px"}

=== "Black"

    ![Black Logo](https://img.icons8.com/external-tal-revivo-regular-tal-revivo/96/external-readme-is-a-easy-to-build-a-developer-hub-that-adapts-to-the-user-logo-regular-tal-revivo.png){: style="width:100px"}

=== "Cloud"

    ![Cloud Logo](https://cdn-icons-png.flaticon.com/512/6295/6295417.png){: style="width:100px"}

=== "Purple"

    ![Purple Logo](https://img.icons8.com/external-tal-revivo-duo-tal-revivo/100/external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-duo-tal-revivo.png){: style="width:100px"}

=== "Grey"

    ![Grey Logo](https://img.icons8.com/external-tal-revivo-filled-tal-revivo/96/external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-filled-tal-revivo.png){: style="width:100px"}

## How It Works

README-AI provides several ways to include a logo in your project's README:

1. **Default Images**: Choose from a set of pre-defined logos.
2. **Custom Images**: Use your own image by providing a URL or file path.
3. **LLM-Generated Images**: Generate a unique logo using AI (requires an LLM API).

The selected or generated logo will be placed at the top of your README file, helping to visually identify your project.

## Usage Examples

### Using a Default Image

To use one of the default images, specify the image name with the `--image` option:

```bash
readmeai --image gradient --repository https://github.com/username/project
```

### Using a Custom Image

To use a custom image, use the `--image custom` option:

```bash
readmeai --image custom --repository https://github.com/username/project
```

You will be prompted to provide an image file path or URL:

```console
Provide an image file path or URL:
```

### LLM Generated Logo

To generate a logo using an LLM API (e.g., OpenAI), use the `--image llm` option:

```bash
readmeai --image llm --api openai --repository https://github.com/username/project
```

This will generate a unique project logo using the specified LLM API.

## Example Output

Here's an example of how a generated README header might look with a logo:

!!! example

    === "Generated README Header with Logo"

        <p align="center">
        <img src="https://github.com/eli64s/readme-ai/blob/main/docs/assets/images/dalle/readme-ai.png?raw=true" width="200" alt="Project Logo">
        </p>
        <h1 align="center">Your Project Name</h1>
        <p align="center">
        Your project's tagline or brief description
        </p>
        <!-- Badges and other header content -->

## LLM-Generated Logo Example

Here's an example of a logo generated using the OpenAI DALL-E model:


<figure markdown>
  ![LLM Generated Logo](https://github.com/eli64s/readme-ai/blob/main/docs/assets/images/dalle/readme-ai.png?raw=true){ width="300" }
  <figcaption>Logo generated using OpenAI's DALL-E model</figcaption>
</figure>

## Tips for Using Project Logos

- Choose a logo that represents your project's purpose or theme.
- Ensure the logo is clear and recognizable even at smaller sizes.
- If using a custom image, make sure it's high quality and appropriately sized.
- When using LLM-generated logos, you may want to generate several options to choose from.
- Consider how the logo will look alongside your project's badges and other README content.
- If your project is part of a larger organization or ecosystem, consider using a logo that aligns with that branding.

!!! info "Note on LLM-Generated Logos"
The quality and relevance of LLM-generated logos can vary. It's a good idea to review and potentially edit the generated logo to ensure it meets your project's needs.
