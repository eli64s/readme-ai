# Table Alignment in Markdown

Markdown tables allow you to align the content within columns. You can align text to the left, center, or right of each column.

## Basic Table Syntax

Here's a reminder of the basic table syntax:

```markdown
| Header 1 | Header 2 | Header 3 |
| -------- | -------- | -------- |
| Row 1, Col 1 | Row 1, Col 2 | Row 1, Col 3 |
| Row 2, Col 1 | Row 2, Col 2 | Row 2, Col 3 |
```

## Alignment Syntax

To specify alignment, add colons (`:`) to the header row:

- Left-aligned: `:---` (default)
- Center-aligned: `:---:`
- Right-aligned: `---:`

## Example

Here's an example of a table with different alignments:

```markdown
| Left-aligned | Center-aligned | Right-aligned |
| :--- | :---: | ---: |
| Content | Content | Content |
| Left | Center | Right |
```

This will render as:

| Left-aligned | Center-aligned | Right-aligned |
| :--- | :---: | ---: |
| Content | Content | Content |
| Left | Center | Right |

## Mixed Alignment

You can mix and match alignments within the same table:

```markdown
| Product | Quantity | Price |
| :--- | :---: | ---: |
| Apple | 5 | $1.00 |
| Banana | 3 | $0.75 |
| Orange | 2 | $0.80 |
```

This will render as:

| Product | Quantity | Price |
| :--- | :---: | ---: |
| Apple | 5 | $1.00 |
| Banana | 3 | $0.75 |
| Orange | 2 | $0.80 |

## Best Practices

1. Use left alignment for textual content.
2. Use center alignment for headers or short content.
3. Use right alignment for numerical data, especially in financial tables.
4. Be consistent with your alignment choices throughout your document.

By using table alignment effectively, you can improve the readability and professional appearance of your Markdown tables.

---
