# Table of Contents (ToC) Templates

README-AI offers flexible options for generating a Table of Contents (ToC) in your README file, directly from the command line. You can specify different styles of ToC generation using the `--toc-style` option when running the CLI.

## CLI Usage for ToC Styles

When using the `readmeai` CLI, you can customize the Table of Contents by specifying one of the supported styles with the `--toc-style` flag.

### Supported ToC Styles:

1. **Bullet** (`bullet`)
   - Displays a simple bulleted list format for the Table of Contents.

2. **Fold** (`fold`)
   - Generates a collapsible Table of Contents. Users can click to expand the list of sections.

3. **Links** (`links`)
   - A quick link format that groups key sections under a "Quick Links" heading.

4. **Number** (`number`)
   - Numbers the sections in the Table of Contents for clear ordering and hierarchy.

5. **Roman** (`roman`)
   - Uses Roman numerals to number the sections, providing a classic and formal appearance.

## Example CLI Command

Here’s how to generate a README file with a **Numbered Table of Contents**:

```bash
readmeai --repository ./my_project --toc-style number --output README.md
```

In this example:
- The `--repository` flag specifies the local project directory.
- The `--toc-style number` flag sets the Table of Contents to use a numbered format.
- The `--output README.md` flag specifies the output file name.

### Another Example with Foldable ToC

To generate a README with a **Foldable Table of Contents**, run:

```bash
readmeai --repository ./my_project --toc-style fold --output README.md
```

This will create a ToC that is hidden by default, allowing users to expand it if needed.

## Available ToC Styles

```bash
-tc, --toc-style [bullet|fold|links|number|roman]
```

The `--toc-style` option supports the following values:

- **bullet**: Simple bullet list
- **fold**: Collapsible ToC
- **links**: Quick links format
- **number**: Numbered list of sections
- **roman**: Roman numeral list of sections

## Additional Customizations

You can further customize your README file with options like header styles (`--header-style`), logo image (`--image`), and badges (`--badge-style`).

---
