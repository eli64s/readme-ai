# GitHub Theme-Aware Images Guide

## New Method (Recommended)

Use the HTML `<picture>` element to create theme-responsive images:

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/GiorgosXou/Random-stuff/main/Programming/StackOverflow/Answers/70200610_11465149/w.png">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/GiorgosXou/Random-stuff/main/Programming/StackOverflow/Answers/70200610_11465149/b.png">
  <img alt="Theme-aware image description" src="../../../../readmeai/static/logos/rainbow.svg">
</picture>
```

Render the image using the following Markdown syntax:

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/GiorgosXou/Random-stuff/main/Programming/StackOverflow/Answers/70200610_11465149/w.png">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/GiorgosXou/Random-stuff/main/Programming/StackOverflow/Answers/70200610_11465149/b.png">
  <img alt="Theme-aware image description" src="../../../../readmeai/assets/logos/rainbow.svg">
</picture>

**Key Benefits:**
- Officially supported method
- Better browser compatibility
- Proper fallback support

## Legacy Method (Deprecated)

The following approach using URL fragments is deprecated and will be removed:

```markdown
![Dark Mode Image](https://raw.githubusercontent.com/GiorgosXou/Random-stuff/main/Programming/StackOverflow/Answers/70200610_11465149/w.png#gh-dark-mode-only)
![Light Mode Image](https://raw.githubusercontent.com/GiorgosXou/Random-stuff/main/Programming/StackOverflow/Answers/70200610_11465149/b.png#gh-light-mode-only)
```

Render the image using the following Markdown syntax:

![Dark Mode Image](https://raw.githubusercontent.com/GiorgosXou/Random-stuff/main/Programming/StackOverflow/Answers/70200610_11465149/w.png#gh-dark-mode-only)
![Light Mode Image](https://raw.githubusercontent.com/GiorgosXou/Random-stuff/main/Programming/StackOverflow/Answers/70200610_11465149/b.png#gh-light-mode-only)

**HTML Version:**

```html
<img src="https://raw.githubusercontent.com/GiorgosXou/Random-stuff/main/Programming/StackOverflow/Answers/70200610_11465149/b.png#gh-light-mode-only">
<img src="https://raw.githubusercontent.com/GiorgosXou/Random-stuff/main/Programming/StackOverflow/Answers/70200610_11465149/w.png#gh-dark-mode-only">
```

Render the image using the following HTML syntax:

<img src="https://raw.githubusercontent.com/GiorgosXou/Random-stuff/main/Programming/StackOverflow/Answers/70200610_11465149/b.png#gh-light-mode-only">
<img src="https://raw.githubusercontent.com/GiorgosXou/Random-stuff/main/Programming/StackOverflow/Answers/70200610_11465149/w.png#gh-dark-mode-only">

## Best Practices

- Store images in GitHub repositories for reliable theme switching
- Provide meaningful alt text for accessibility
- Include a fallback image in the `<img>` tag
- Test images in both light and dark modes

## Requirements

- Images must be hosted on GitHub
- Use relative paths when possible
- Ensure image formats are web-compatible (PNG, JPG, GIF)

---
