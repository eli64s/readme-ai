---
title: Navigation Styles
description: Create organized, accessible tables of contents for your documentation with ReadmeAI's navigation system. Choose from four different styles to match your project's needs.
---

ReadmeAI's navigation system helps create organized, accessible tables of contents for your documentation. Choose from four different styles to match your project's needs.

## Configuration

Add a navigation style to your README using the `--navigation-style` flag:

```sh
readmeai --navigation-style <style> --repository <url-or-path>
```

## Available Styles

=== "Bullet"

    The default style using markdown bullet points for clean hierarchical organization.

    ```sh
    readmeai -ns bullet -r https://github.com/username/project
    ```

    !!! example "Markdown Output"
        ```markdown
        ## Table of Contents

        - [Table of Contents](#table-of-contents)
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

        ---
        ```

    !!! example "Rendered Output"
        <div markdown="span">
        ## Table of Contents

        - [Table of Contents](#table-of-contents)
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

        ---
        </div>

=== "Number"

    Sequential numbering for easy section referencing, ideal for tutorials.

    ```sh
    readmeai -ns number -r https://github.com/username/project
    ```

    !!! example "Markdown Output"
        ```markdown

        ## Table of Contents
        1. [Table of Contents](#table-of-contents)
        2. [Overview](#overview)
        3. [Features](#features)
        4. [Project Structure](#project-structure)
            4.1. [Project Index](#project-index)
        5. [Getting Started](#getting-started)
            5.1. [Prerequisites](#prerequisites)
            5.2. [Installation](#installation)
            5.3. [Usage](#usage)
            5.4. [Testing](#testing)
        6. [Roadmap](#roadmap)
        7. [Contributing](#contributing)
        8. [License](#license)
        9. [Acknowledgments](#acknowledgments)

        ---
        ```

    !!! example "Rendered Output"
        <div markdown="span"><pre><code>
        ## Table of Contents

        10. [Table of Contents](#table-of-contents)
        11. [Overview](#overview)
        12. [Features](#features)
        13. [Project Structure](#project-structure)
            4.1. [Project Index](#project-index)
        14. [Getting Started](#getting-started)
            5.1. [Prerequisites](#prerequisites)
            5.2. [Installation](#installation)
            5.3. [Usage](#usage)
            5.4. [Testing](#testing)
        15. [Roadmap](#roadmap)
        16. [Contributing](#contributing)
        17. [License](#license)
        18. [Acknowledgments](#acknowledgments)

        ---
        </code></pre></div>

=== "Roman"

    Classical formatting with Roman numerals, suitable for formal documentation.

    ```sh
    readmeai -ns roman -r https://github.com/username/project
    ```

    !!! example "Markdown Output"
        ```markdown
        ## Table of Contents

        I. [Table of Contents](#table-of-contents)<br>
        II. [Overview](#overview)<br>
        III. [Features](#features)<br>
        IV. [Project Structure](#project-structure)<br>
        &nbsp;&nbsp;&nbsp;&nbsp;IV.a. [Project Index](#project-index)<br>
        V. [Getting Started](#getting-started)<br>
        &nbsp;&nbsp;&nbsp;&nbsp;V.a. [Prerequisites](#prerequisites)<br>
        &nbsp;&nbsp;&nbsp;&nbsp;V.b. [Installation](#installation)<br>
        &nbsp;&nbsp;&nbsp;&nbsp;V.c. [Usage](#usage)<br>
        &nbsp;&nbsp;&nbsp;&nbsp;V.d. [Testing](#testing)<br>
        VI. [Roadmap](#roadmap)<br>
        VII. [Contributing](#contributing)<br>
        VIII. [License](#license)<br>
        IX. [Acknowledgments](#acknowledgments)<br>

        ---
        ```

    !!! example "Rendered Output"
        <div markdown="span"><pre><code>
        ## Table of Contents

        I. [Table of Contents](#table-of-contents)<br>
        II. [Overview](#overview)<br>
        III. [Features](#features)<br>
        IV. [Project Structure](#project-structure)<br>
        &nbsp;&nbsp;&nbsp;&nbsp;IV.a. [Project Index](#project-index)<br>
        V. [Getting Started](#getting-started)<br>
        &nbsp;&nbsp;&nbsp;&nbsp;V.a. [Prerequisites](#prerequisites)<br>
        &nbsp;&nbsp;&nbsp;&nbsp;V.b. [Installation](#installation)<br>
        &nbsp;&nbsp;&nbsp;&nbsp;V.c. [Usage](#usage)<br>
        &nbsp;&nbsp;&nbsp;&nbsp;V.d. [Testing](#testing)<br>
        VI. [Roadmap](#roadmap)<br>
        VII. [Contributing](#contributing)<br>
        VIII. [License](#license)<br>
        IX. [Acknowledgments](#acknowledgments)<br>

        ---
        </code></pre></div>

=== "Accordion"

    Collapsible dropdown widget for a clean, compact table of contents.

    ```sh
    readmeai -ns accordion -r https://github.com/username/project
    ```

    !!! example "Markdown Output"
        ```markdown
        ## Table of Contents

        <details>
        <summary>Table of Contents</summary>

        - [Table of Contents](#table-of-contents)
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

        </details>
        ```

    !!! example "Rendered Output"
        <div markdown="span"><pre><code>
        ## Table of Contents

        <details>
        <summary>Table of Contents</summary>

        - [Table of Contents](#table-of-contents)
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

        </details>
        </code></pre></div>

=== "Adding Emojis"

    Select from a variety of emoji theme packs to prefix to your header sections:

    ```sh
    readmeai --emojis ascension --navigation-style bullet --repository https://github.com/username/project
    ```

    !!! example "Markdown Output"
        ```markdown
        ## 🔷 Table of Contents

        - [🔷 Table of Contents](#-table-of-contents)
        - [🌀 Overview](#-overview)
        - [🔶 Features](#-features)
        - [🔺 Project Structure](#-project-structure)
            - [🔹 Project Index](#-project-index)
        - [🔸 Getting Started](#-getting-started)
            - [① Prerequisites](#-prerequisites)
            - [② Installation](#-installation)
            - [③ Usage](#-usage)
            - [④ Testing](#-testing)
        - [🔳 Roadmap](#-roadmap)
        - [🔲 Contributing](#-contributing)
        - [◼ ️ License](#-license)
        - [✨ Acknowledgments](#-acknowledgments)

        ---
        ```

    !!! example "Rendered Output"
        <div markdown="span">
        ## 🔷 Table of Contents

        - [🔷 Table of Contents](#-table-of-contents)
        - [🌀 Overview](#-overview)
        - [🔶 Features](#-features)
        - [🔺 Project Structure](#-project-structure)
            - [🔹 Project Index](#-project-index)
        - [🔸 Getting Started](#-getting-started)
            - [① Prerequisites](#-prerequisites)
            - [② Installation](#-installation)
            - [③ Usage](#-usage)
            - [④ Testing](#-testing)
        - [🔳 Roadmap](#-roadmap)
        - [🔲 Contributing](#-contributing)
        - [◼ ️ License](#-license)
        - [✨ Acknowledgments](#-acknowledgments)

        ---
        </div>

---

## Technical Details

!!! info "Link Generation"

    README-AI generates GitHub-compatible anchor links by:

    - Converting headers to lowercase
    - Replacing spaces with hyphens
    - Removing special characters
    - Preserving emoji display while keeping clean anchors

!!! tip "Best Practices"

    - Use `bullet` style for clean and simple tables of contents
    - Use `accordion` style to hide the TOC in a dropdown widget
    - Use `number` or `roman` style for more formal documentation

## Advanced Usage

Combine navigation styles with other README-AI features to create customized documentation:

```sh
readmeai --navigation-style roman \
         --header-style modern \
         --emojis water \
         --repository https://github.com/username/project
```

---
