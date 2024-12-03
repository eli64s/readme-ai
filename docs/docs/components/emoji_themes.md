---
title: Emoji Theme Packs
---

# Emoji Theme Packs

Emoji theme packs allow you to add domain-specific emoji prefixes to your README section headers. This can be a nice touch for enhancing visual navigation and project context. Each theme provides a carefully curated set of emojis aligned with different technology domains and project types.

## Overview

Use the `--emojis` flag along with your chosen theme to add emoji prefixes:

```sh
readmeai --emojis <theme_name> --repository <repository_url_or_path>
```

## Available Themes

### Core Themes

=== ":octicons-mark-github-16: Default"

    Default theme *does not* include emojis. This is the default behavior when the `--emojis` flag is not set.

    ```sh
    readmeai --repository https://github.com/username/project
    ```

    !!! example "Output Preview"

        ### Table of Contents
        - [Overview](#overview)
        - [Features](#features)
        - [Project Structure](#project-structure)
            - [Project Index](#project-index)
        - [Getting Started](#getting-started)
            - [Prerequisites](#prerequisites)
            - [Installation](#installation)
            - [Usage](#usage)
            - [Testing](#testing)
        - [Roadmap](#roadmap)
        - [Contributing](#contributing)
        - [License](#license)
        - [Acknowledgments](#acknowledgments)

=== ":octicons-file-16: Minimal"

    Clean and simple emoji set.

    ```sh
    readmeai --emojis minimal --repository https://github.com/username/project
    ```

    !!! example "Output Preview"

        ```markdown
        ## 📄 Table of Contents
        ## ✨ Overview
        ## 📌 Features
        ## 📁 Project Structure
            ### 📑 Project Index
        ## 🚀 Getting Started
            ### 📋 Prerequisites
            ### ⚙️ Installation
            ### 💻 Usage
            ### 🧪 Testing
        ## 📈 Roadmap
        ## 🤝 Contributing
        ## 📜 License
        ## ✨ Acknowledgments
        ```

=== ":octicons-code-16: OSS"

    Open source and community focused emojis.

    ```sh
    readmeai --emojis oss --repository https://github.com/username/project
    ```

    !!! example "Output Preview"

        ```markdown
        ## 🌟 Table of Contents
        ## 💫 Overview
        ## ✨ Features
        ## 📁 Project Structure
            ### 📑 Project Index
        ## 🚀 Getting Started
            ### 📋 Prerequisites
            ### ⚙️ Installation
            ### 💻 Usage
            ### 🧪 Testing
        ## 👥 Community
            ### 🤝 Contributing
            ### 💭 Code of Conduct
            ### 🗣️ Discussions
            ### 🎯 Issues
        ## 📚 Documentation
            ### 📖 API Reference
            ### 📝 Tutorials
            ### 💡 Examples
        ## 📈 Roadmap
        ## ❤️ Contributors
        ## 📜 License
        ## ⭐ Acknowledgments
        ```

### Development Themes

=== ":material-api: API"

    API and microservices focused emojis.

    ```sh
    readmeai --emojis api --repository https://github.com/username/project
    ```

    !!! example "Output Preview"

        ```markdown
        ## 🔌 Table of Contents
        ## 🌐 Overview
        ## ⚡ Features
        ## 📁 Project Structure
            ### 📑 Project Index
        ## 🚀 Getting Started
            ### 📋 Prerequisites
            ### ⚙️ Installation
            ### 🔑 Authentication
            ### 🧪 Testing
        ## 📡 Endpoints
            ### 🔍 Queries
            ### 📝 Mutations
            ### 🔄 Subscriptions
            ### 🔒 Authorization
        ## ⚡ Performance
            ### 📊 Monitoring
            ### 🔍 Tracing
            ### 📈 Metrics
        ## 🛣️ Roadmap
        ## 🤝 Contributing
        ## 📜 License
        ## ⭐ Acknowledgments
        ```

=== ":material-web: Web"

    Web development focused emojis.

    ```sh
    readmeai --emojis web --repository https://github.com/username/project
    ```

    !!! example "Output Preview"

        ```markdown
        ## 🌐 Table of Contents
        ## 💻 Overview
        ## ✨ Features
        ## 📁 Project Structure
            ### 📑 Project Index
        ## 🚀 Getting Started
            ### 📋 Prerequisites
            ### ⚙️ Installation
            ### 🖥️ Development
            ### 🧪 Testing
        ## 🎨 Frontend
            ### 🧩 Components
            ### 🔄 State Management
            ### 🎯 Routing
            ### 📱 Responsive Design
        ## ⚡ Backend
            ### 🛢️ Database
            ### 🔌 API
            ### 🔐 Authentication
            ### 📡 WebSockets
        ## 📱 Mobile Support
        ## 🚀 Deployment
            ### 🔄 CI/CD
            ### 📊 Monitoring
            ### 🔒 Security
        ## 📈 Roadmap
        ## 🤝 Contributing
        ## 📜 License
        ## ⭐ Acknowledgments
        ```

=== ":material-cellphone: Mobile"

    Mobile development focused emojis.

    ```sh
    readmeai --emojis mobile --repository https://github.com/username/project
    ```

    !!! example "Output Preview"

        ```markdown
        ## 📱 Table of Contents
        ## 🌟 Overview
        ## ✨ Features
        ## 📁 Project Structure
            ### 📑 Project Index
        ## 🚀 Getting Started
            ### 📋 Prerequisites
            ### ⚙️ Installation
            ### 💻 Development
            ### 🧪 Testing
        ## 📱 Platforms
            ### 🤖 Android
            ### 🍎 iOS
            ### 🌐 Cross-Platform
        ## 🎨 UI/UX
            ### 🧩 Components
            ### 🎯 Navigation
            ### 🎨 Themes
            ### 📱 Responsive Design
        ## 📡 Backend
            ### 🔌 API Integration
            ### 💾 Data Storage
            ### 🔄 Sync
            ### 📶 Offline Support
        ## 📦 Distribution
            ### 🏗️ Build
            ### 📲 Deploy
            ### 🔄 Updates
        ## 📈 Analytics
        ## 🛣️ Roadmap
        ## 🤝 Contributing
        ## 📜 License
        ## ⭐ Acknowledgments
        ```

> [🚧 WORK IN PROGRESS] - Need to add the remaining theme examples.

## Configuration

### Command-Line Options

| Option | Description | Default |
| :----- | :---------- | :------ |
| `--emojis` | Specify emoji theme | `default` |

### Creating Custom Themes

You can create custom themes by adding them to your configuration:

> [🚧 WORK IN PROGRESS] - Feature currently under development.

<!--

```toml
[themes.custom]
name = "Custom Theme"
description = "Your custom theme description"

[[themes.custom.sections]]
title = "📚 Table of Contents"

[[themes.custom.sections]]
title = "🎯 Overview"
# ... add more sections
```

-->

## Best Practices

### When to Use Emojis

✅ Recommended for:
- Open source projects
- Developer documentation
- Technical blogs
- Community resources
- Educational content

❌ Not recommended for:
- Enterprise documentation
- Legal documents
- Compliance materials
- Formal specifications

### Theme Selection Guidelines

1. **Match Project Domain**
   - Choose themes that reflect your project's technology stack
   - Use domain-specific themes for specialized projects
   - Consider your target audience

2. **Maintain Consistency**
   - Use one theme throughout documentation
   - Keep emoji usage consistent
   - Follow theme patterns

3. **Ensure Readability**
   - Don't overuse emojis
   - Test readability across platforms
   - Consider color contrast

4. **Consider Platform Support**
   - Test emoji rendering
   - Check platform compatibility
   - Verify display across devices

## FAQs

??? question "Can I mix themes?"
    While possible, it's recommended to stick to one theme for consistency.

??? question "How do I preview themes?"
    Use the `--dry-run` flag to preview theme output without generating a README.

??? question "Can I disable emojis for specific sections?"
    Yes, use the `--no-emoji` flag for specific sections in custom themes.

<!--
## Tips and Tricks

1. **Theme Testing**
   ```sh
   readmeai --emojis <theme> --dry-run
   ```

2. **Custom Theme Creation**
   ```sh
   readmeai --emojis custom --theme-file path/to/theme.toml
   ```

3. **Section Override**
   ```sh
   readmeai --emojis <theme> --no-emoji-sections "overview,features"
   ```

!!! tip "Tip: Theme Preview"
    Use the `--preview` flag to see how your README will look with different themes before generating.

!!! warning "Platform Compatibility"
    Some platforms or markdown renderers may display emojis differently. Always test your documentation's appearance on target platforms.
-->

## See Also

- [Configuration Reference](cli_reference.md)
- [Header Styles Reference](components/headers.md)
- [Markdown Formatting Guide](guides/markdown.md)

---
