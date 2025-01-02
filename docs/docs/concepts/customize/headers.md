---
title: Header Styles
---

# Header Styles

ReadmeAI's header system helps you create visually appealing and professional project introductions. The header serves as your project's first impression, combining your project's identity, key metrics, and technical overview in a cohesive design.

## Configuration

Add a header style to your README using the `--header-style` flag:

```bash
readmeai --header-style <style> --repository <url-or-path>
```

## Available Styles

=== "classic"

    The traditional style offering a balanced, professional layout. This is the default choice that works well for most projects.

    ```bash
    readmeai --repository https://github.com/username/project
    ```

    **Example output:**

    <p align="center">
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="20%" alt="Project Logo">
    </p>
    <h1 align="center">Project Name</h1>
    <p align="center">
        <em>Project Description Here</em>
    </p>

    **Key Features:**

    - Centered layout for balanced presentation
    - Logo and title in vertical alignment
    - Clean separation of elements
    - Universal compatibility across platforms

=== "compact"

    A space-efficient design that places elements side by side, perfect for projects with limited README space.

    ```bash
    readmeai --header-style compact --repository https://github.com/username/project
    ```

    **Key Features:**

    - Left-aligned layout
    - Logo and title on same line
    - Condensed information display
    - Efficient use of vertical space

=== "modern"

    A contemporary design emphasizing asymmetric layout and visual hierarchy.

    ```bash
    readmeai --header-style modern --repository https://github.com/username/project
    ```

    **Key Features:**

    - Left-aligned text elements
    - Right-floating logo
    - Dynamic spacing relationships
    - Contemporary aesthetic appeal

=== "banner"

    A style utilizing scalable vector graphics for crisp, professional banners.

    ```bash
    readmeai --header-style svg --repository https://github.com/username/project
    ```

	**Example output:**

	<!-- HEADER STYLE: BANNER -->
	<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 100">
		<defs>
			<linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
				<stop offset="0%" style="stop-color:#2de530;stop-opacity:1" />
				<stop offset="50%" style="stop-color:#2de59f;stop-opacity:1" />
				<stop offset="100%" style="stop-color:#2dbde5;stop-opacity:1" />
			</linearGradient>
			<filter id="shadow">
				<feDropShadow dx="2.5" dy="2.5" stdDeviation="10" flood-opacity="0.5" />
			</filter>
			<pattern id="dots" width="20" height="20" patternUnits="userSpaceOnUse">
				<circle cx="3" cy="3" r="1.5" fill="rgba(255,255,255,0.1)" />
			</pattern>
		</defs>
		<rect width="100%" height="100%" fill="url(#bg)" rx="10" />
		<rect width="100%" height="100%" fill="url(#dots)" />
		<circle cx="16.0" cy="25.0" r="15.0" fill="rgba(255,255,255,0.2)" />
		<circle cx="184.0" cy="75.0" r="20.0" fill="rgba(255,255,255,0.2)" />
		<path d="M 100.0 12.5
				L 125.0 37.5
				L 75.0 37.5 Z" fill="rgba(255,255,255,0.2)" />
		<text x="100.0" y="50.0" font-family="Arial, sans-serif" font-size="40" font-weight="bold" text-anchor="middle" fill="#ffffff" filter="url(#shadow)">
			splitme-ai
		</text>
		<text x="100.0" y="75.0" font-family="Arial, sans-serif" font-size="8" text-anchor="middle" fill="rgba(255,255,255,0.9)">Empowering content clarity, one split at a time.</text></svg>

    **Key Features:**

    - Full-width banner support
    - Resolution-independent graphics
    - Gradient and effects capabilities
		- Randomized gradient colors
    - Professional branding potential

=== "console"

    A terminal-inspired design perfect for command-line tools and developer utilities.

    ```bash
    readmeai --header-style console --repository https://github.com/username/project
    ```

	**Example output:**

	<div align="left">

	```console
	██████ ██████   ██   ████   ██   ██ ██████          ██   ██████
	██  ██ ██      ████  ██  ██ ███ ███ ██             ████    ██
	██████ ████   ██  ██ ██  ██ ██ █ ██ ████   ██████ ██  ██   ██
	██ ██  ██     ██████ ██  ██ ██   ██ ██            ██████   ██
	██  ██ ██████ ██  ██ ████   ██   ██ ██████        ██  ██ ██████

	Your automated README generator for GitHub projects.

	```
	</div>

    **Key Features:**

    - ASCII art representation
    - Monospace font styling
    - Terminal-like appearance
    - No external image dependencies

=== "ascii"

    A text-art approach that creates visual interest without using images.

    ```bash
    readmeai --header-style ascii --repository https://github.com/username/project
    ```

    **Key Features:**

    - Pure text-based design
    - Universal compatibility
    - Retro aesthetic appeal
    - Minimal dependencies

=== "ascii_box"

    Similar to ASCII style but with a decorative border frame.

    ```bash
    readmeai --header-style ascii_box --repository https://github.com/username/project
    ```

    **Key Features:**

    - Bordered text-art design
    - Enhanced visual separation
    - Terminal-friendly format
    - Distinctive presentation

## Technical Details

!!! info "Header Generation Process"

    ReadmeAI processes your header style selection by:

    1. Analyzing repository metadata
    2. Gathering project assets (logo, badges)
    3. Applying style template rules
    4. Generating formatted markdown
    5. Integrating with badge system

!!! tip "Style Elements"

    Each header style manages these components:

    1. Project Identification
		- Repository name
		- Project description
		- Logo or icon

    2. Status Indicators
		- License badge
		- Last commit information
		- Language statistics
		- Custom metrics

    3. Technical Overview
		- Technology stack badges
		- Framework indicators
		- Tool integration status

## Advanced Usage

Combine header styles with other ReadmeAI features for custom documentation:

```bash
readmeai --header-style modern \
         --badge-style flat \
         --badge-color orange \
         --repository https://github.com/username/project
```

!!! note "Customization Options"

    Key parameters you can adjust:

    - Text alignment (left, center, right)
    - Logo size and position
    - Badge style integration
    - Color schemes
    - Component spacing

## Best Practices

When selecting and implementing a header style, consider these principles:

1. **Audience Alignment**: Choose a style that matches your audience's expectations and technical sophistication. For example, use the console style for developer tools and the modern style for web applications.

2. **Content Harmony**: Ensure your header style complements the rest of your documentation. The header should enhance, not overshadow, your content.

3. **Platform Compatibility**: Test your chosen style across different markdown renderers. Some platforms may handle certain styles differently, particularly with ASCII art or SVG content.

4. **Visual Hierarchy**: Arrange elements to guide readers naturally through your project's introduction. Important information should be immediately visible and clear.

5. **Maintenance Considerations**: Select a style that you can easily maintain and update. Simpler styles often require less maintenance than complex ones.

## Style Selection Guide

Consider these factors when choosing your header style:

- **Classic**: Best for traditional open-source projects needing a professional appearance
- **Compact**: Ideal for projects with space constraints or minimal documentation
- **Modern**: Suitable for contemporary web applications and design-focused projects
- **Console**: Perfect for command-line tools and developer utilities
- **SVG**: Excellent for projects requiring strong branding and visual impact
- **ASCII/ASCII_BOX**: Great for terminal-based applications or retro-styled projects

Each style has been carefully designed to serve specific documentation needs while maintaining professional standards and readability.

---

<!--
# Header Styles

A header template style determines how your project's header section is structured and displayed in the README file. README-AI offers several pre-designed header styles to help brand your project and create a professional appearance.

## Available Styles

!!! example

    <p>Use the `--header-style` option to select from the following markdown header templates:</p>

    === "CLASSIC"

		By default, the `classic` header style is used, so no additional option is needed.

		<div class="usage-container">
		<h3>Usage:</h3>

		```sh
		readmeai --repository https://github.com/username/project
		```

		</div>

		<div class="output-container">
		<h3>Output:</h3>

		<p align="center">
		<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="20%" alt="README-AI-logo">
		</p>
		<p align="center">
			<h1 align="center">README-AI</h1>
		</p>
		<p align="center">
			<em>Where Documentation Meets Innovation!</em>
		</p>
		<p align="center">
			<img src="https://img.shields.io/github/license/eli64s/readme-ai?style=flat&logo=opensourceinitiative&logoColor=white&color=60A5FA" alt="license">
			<img src="https://img.shields.io/github/last-commit/eli64s/readme-ai?style=flat&logo=git&logoColor=white&color=60A5FA" alt="last-commit">
			<img src="https://img.shields.io/github/languages/top/eli64s/readme-ai?style=flat&color=60A5FA" alt="repo-top-language">
			<img src="https://img.shields.io/github/languages/count/eli64s/readme-ai?style=flat&color=60A5FA" alt="repo-language-count">
		</p>
		<p align="center">Tech Stack</p>
		<p align="center">
			<img src="https://img.shields.io/badge/precommit-FAB040.svg?style=flat&logo=pre-commit&logoColor=black" alt="precommit">
			<img src="https://img.shields.io/badge/Ruff-FCC21B.svg?style=flat&logo=Ruff&logoColor=black" alt="Ruff">
			<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
			<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat&logo=Pytest&logoColor=white" alt="Pytest">
			<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white" alt="Docker">
			<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
			<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=flat&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions">
			<br>
			<img src="https://img.shields.io/badge/Poetry-60A5FA.svg?style=flat&logo=Poetry&logoColor=white" alt="Poetry">
			<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=flat&logo=AIOHTTP&logoColor=white" alt="AIOHTTP">
			<img src="https://img.shields.io/badge/Material%20for%20MkDocs-526CFE.svg?style=flat&logo=Material-for-MkDocs&logoColor=white" alt="Material%20for%20MkDocs">
			<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=flat&logo=OpenAI&logoColor=white" alt="OpenAI">
			<img src="https://img.shields.io/badge/Google%20Gemini-8E75B2.svg?style=flat&logo=Google-Gemini&logoColor=white" alt="Google%20Gemini">
			<img src="https://img.shields.io/badge/Pydantic-E92063.svg?style=flat&logo=Pydantic&logoColor=white" alt="Pydantic">
		</p>
		</div>
		<hr>

		<div class="feature-container">

		<h3>Features:</h3>

		- left-aligned layout
		- logo and title on same line
		- classic design
		- suitable for most README files

		</div>

	=== "COMPACT"

		<div class="usage-container">
		<h3>Usage:</h3>

		```sh
		readmeai --header-style compact --repository https://github.com/username/project
		```

		</div>

		<div class="output-container">
		<h3>Output:</h3>

		<div align="left">
			<img src="https://img.freepik.com/premium-vector/bunch-balloons-icon-vector-illustration_444196-2020.jpg?w=360" width="15%" align="left" style="margin-right: 15px"/>
			<div style="display: inline-block;">
				<h2 style="display: inline-block; vertical-align: middle; margin-top: 0;">README-AI-STREAMLIT</h2>
				<p>
			<em>Streamlining README creation with AI magic!</em>
		</p>
				<p>
			<img src="https://img.shields.io/github/license/eli64s/readme-ai-streamlit?style=flat-square&logo=opensourceinitiative&logoColor=white&color=5D3FD3" alt="license">
			<img src="https://img.shields.io/github/last-commit/eli64s/readme-ai-streamlit?style=flat-square&logo=git&logoColor=white&color=5D3FD3" alt="last-commit">
			<img src="https://img.shields.io/github/languages/top/eli64s/readme-ai-streamlit?style=flat-square&color=5D3FD3" alt="repo-top-language">
			<img src="https://img.shields.io/github/languages/count/eli64s/readme-ai-streamlit?style=flat-square&color=5D3FD3" alt="repo-language-count">
		</p>
			<p>Tech Stack</p>
			<p>
			<img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=flat-square&logo=Streamlit&logoColor=white" alt="Streamlit">
			<img src="https://img.shields.io/badge/precommit-FAB040.svg?style=flat-square&logo=pre-commit&logoColor=black" alt="precommit">
			<img src="https://img.shields.io/badge/Ruff-FCC21B.svg?style=flat-square&logo=Ruff&logoColor=black" alt="Ruff">
			<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat-square&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
			<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat-square&logo=Pytest&logoColor=white" alt="Pytest">
			<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python">
			<img src="https://img.shields.io/badge/Poetry-60A5FA.svg?style=flat-square&logo=Poetry&logoColor=white" alt="Poetry">
		</p>
			</div>
		</div>
		</div>
		<br clear="left"/>
		<hr>

		<div class="feature-container">

		<h3>Features:</h3>

		- left-aligned layout
		- logo and title on same line
		- space-efficient design
		- perfect for smaller README files

		</div>


	=== "CONSOLE"

		<div class="usage-container">
		<h3>Usage:</h3>

		```sh
		readmeai --header-style console --repository https://github.com/username/project
		```

		</div>

		<div class="output-container">
		<h3>Output:</h3>

		<div align="left">

		```console
		██████ ██████   ██   ████   ██   ██ ██████          ██   ██████
		██  ██ ██      ████  ██  ██ ███ ███ ██             ████    ██
		██████ ████   ██  ██ ██  ██ ██ █ ██ ████   ██████ ██  ██   ██
		██ ██  ██     ██████ ██  ██ ██   ██ ██            ██████   ██
		██  ██ ██████ ██  ██ ████   ██   ██ ██████        ██  ██ ██████

		▷ Craft READMEs with AI magic!
		```

		</div>
		</div>

		<div class="feature-container">

		<h3>Features:</h3>

		- console-style ASCII art
		- minimal and retro design
		- no image dependencies
		- perfect for terminal-focused tools

		</div>


	=== "MODERN"

		<div class="usage-container">
		<h3>Usage:</h3>

		```sh
		readmeai --header-style modern --repository https://github.com/username/project
		```

		</div>

		<div class="output-container">
		<h3>Output:</h3>
		<div align="left" style="position: relative;">
		<img src="https://flink.apache.org/img/logo/png/1000/flink_squirrel_1000.png" align="right" width="30%" style="margin: -20px 0 0 20px;">
		<h1>PYFLINK-POC</h1>
		<p align="left">
			<em>Streamlining data flow with PyFlink power!</em>
		</p>
		<p align="left">
			<img src="https://img.shields.io/github/license/eli64s/pyflink-poc?style=flat&logo=opensourceinitiative&logoColor=white&color=E30B5C" alt="license">
			<img src="https://img.shields.io/github/last-commit/eli64s/pyflink-poc?style=flat&logo=git&logoColor=white&color=E30B5C" alt="last-commit">
			<img src="https://img.shields.io/github/languages/top/eli64s/pyflink-poc?style=flat&color=E30B5C" alt="repo-top-language">
			<img src="https://img.shields.io/github/languages/count/eli64s/pyflink-poc?style=flat&color=E30B5C" alt="repo-language-count">
		</p>
		<p align="left">Tech Stack</p>
		<p align="left">
			<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
			<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
			<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=flat&logo=AIOHTTP&logoColor=white" alt="AIOHTTP">
			<img src="https://img.shields.io/badge/pandas-150458.svg?style=flat&logo=pandas&logoColor=white" alt="pandas">
			<img src="https://img.shields.io/badge/Apache%20Kafka-231F20.svg?style=flat&logo=Apache-Kafka&logoColor=white" alt="Apache%20Kafka">
			<img src="https://img.shields.io/badge/Apache%20Flink-E6526F.svg?style=flat&logo=Apache-Flink&logoColor=white" alt="Apache%20Flink">
		</p>
		</div>
		</div>
		<br clear="right">
		<hr>

		<div class="feature-container">

		<h3>Features:</h3>

		- left-aligned text
		- logo floated to the right
		- contemporary asymmetric design
		- great for documentation sites

		</div>



	=== "SVG"

		<div class="usage-container">
		<h3>Usage:</h3>

		```sh
		readmeai --header-style svg --repository https://github.com/username/project
		```

		</div>

		<div class="output-container">
		<h3>Output:</h3>
		<p align="center">
			<img src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4KICAgIDxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB2aWV3Qm94PSIwIDAgODAwIDIwMCI+CiAgICAgICAgPGRlZnM+CiAgICAgICAgICAgIDxsaW5lYXJHcmFkaWVudCBpZD0iYmctZ3JhZGllbnQiIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICAgICAgICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3R5bGU9InN0b3AtY29sb3I6IzQxNThEMDtzdG9wLW9wYWNpdHk6MSIgLz4KICAgICAgICAgICAgICAgIDxzdG9wIG9mZnNldD0iNTAlIiBzdHlsZT0ic3RvcC1jb2xvcjojQzg1MEMwO3N0b3Atb3BhY2l0eToxIiAvPgogICAgICAgICAgICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdHlsZT0ic3RvcC1jb2xvcjojRkZDQzcwO3N0b3Atb3BhY2l0eToxIiAvPgogICAgICAgICAgICA8L2xpbmVhckdyYWRpZW50PgogICAgICAgICAgICA8ZmlsdGVyIGlkPSJzaGFkb3ciPgogICAgICAgICAgICAgICAgPGZlRHJvcFNoYWRvdyBkeD0iMCIgZHk9IjQiIHN0ZERldmlhdGlvbj0iNCIgZmxvb2Qtb3BhY2l0eT0iMC4yNSIgLz4KICAgICAgICAgICAgPC9maWx0ZXI+CiAgICAgICAgPC9kZWZzPgogICAgICAgIDxyZWN0IHdpZHRoPSI4MDAiIGhlaWdodD0iMjAwIiBmaWxsPSJ1cmwoI2JnLWdyYWRpZW50KSIgcng9IjE1IiByeT0iMTUiLz4KICAgICAgICA8dGV4dCB4PSI0MDAiIHk9IjEwMCIgZm9udC1mYW1pbHk9IkFyaWFsLCBzYW5zLXNlcmlmIiBmb250LXNpemU9IjQ4IgogICAgICAgIGZvbnQtd2VpZ2h0PSJib2xkIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBkb21pbmFudC1iYXNlbGluZT0ibWlkZGxlIgogICAgICAgIGZpbGw9IiNGRkZGRkYiIGZpbHRlcj0idXJsKCNzaGFkb3cpIj5SRUFETUUtQUk8L3RleHQ+CiAgICA8L3N2Zz4=" alt="readme-ai-banner" width="800">
		</p>
		<p align="center">
			<em><code>❯ REPLACE-ME</code></em>
		</p>
		<p align="center">
			<img src="https://img.shields.io/github/license/eli64s/readme-ai?style=flat-square&logo=opensourceinitiative&logoColor=white&color=2496ED" alt="license">
			<img src="https://img.shields.io/github/last-commit/eli64s/readme-ai?style=flat-square&logo=git&logoColor=white&color=2496ED" alt="last-commit">
			<img src="https://img.shields.io/github/languages/top/eli64s/readme-ai?style=flat-square&color=2496ED" alt="repo-top-language">
			<img src="https://img.shields.io/github/languages/count/eli64s/readme-ai?style=flat-square&color=2496ED" alt="repo-language-count">
		</p>
		<p align="center">Tech Stack</p>
		<p align="center">
			<img src="https://img.shields.io/badge/Anthropic-191919.svg?style=flat-square&logo=Anthropic&logoColor=white" alt="Anthropic">
			<img src="https://img.shields.io/badge/precommit-FAB040.svg?style=flat-square&logo=pre-commit&logoColor=black" alt="precommit">
			<img src="https://img.shields.io/badge/Ruff-FCC21B.svg?style=flat-square&logo=Ruff&logoColor=black" alt="Ruff">
			<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat-square&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
			<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat-square&logo=Pytest&logoColor=white" alt="Pytest">
			<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat-square&logo=Docker&logoColor=white" alt="Docker">
			<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python">
			<br>
			<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=flat-square&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions">
			<img src="https://img.shields.io/badge/Poetry-60A5FA.svg?style=flat-square&logo=Poetry&logoColor=white" alt="Poetry">
			<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=flat-square&logo=AIOHTTP&logoColor=white" alt="AIOHTTP">
			<img src="https://img.shields.io/badge/Material%20for%20MkDocs-526CFE.svg?style=flat-square&logo=Material-for-MkDocs&logoColor=white" alt="Material%20for%20MkDocs">
			<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=flat-square&logo=OpenAI&logoColor=white" alt="OpenAI">
			<img src="https://img.shields.io/badge/Google%20Gemini-8E75B2.svg?style=flat-square&logo=Google-Gemini&logoColor=white" alt="Google%20Gemini">
			<img src="https://img.shields.io/badge/Pydantic-E92063.svg?style=flat-square&logo=Pydantic&logoColor=white" alt="Pydantic">
		</p>
		</div>
		<br>
		<hr>

		<div class="feature-container">

		<h3>Features:</h3>

		- full-width SVG banner support
		- centered alignment
		- scalable vector graphics
		- ideal for custom branding

		</div>


	=== "ASCII"

		<div class="usage-container">
		<h3>Usage:</h3>

		```sh
		readmeai --header-style ascii --repository https://github.com/username/project
		```

		</div>

		<div class="output-container">
		<h3>Output:</h3>
		<div align="center">
		<pre>
		██████ ██████   ██   ████   ██   ██ ██████          ██   ██████
		██  ██ ██      ████  ██  ██ ███ ███ ██             ████    ██
		██████ ████   ██  ██ ██  ██ ██ █ ██ ████   ██████ ██  ██   ██
		██ ██  ██     ██████ ██  ██ ██   ██ ██            ██████   ██
		██  ██ ██████ ██  ██ ████   ██   ██ ██████        ██  ██ ██████
		</pre>
		</div>
		<p align="center">
			<em><code>❯ REPLACE-ME</code></em>
		</p>
		<p align="center">
			<img src="https://img.shields.io/github/license/eli64s/readme-ai?style=flat-square&logo=opensourceinitiative&logoColor=white&color=0bc5e2" alt="license">
			<img src="https://img.shields.io/github/last-commit/eli64s/readme-ai?style=flat-square&logo=git&logoColor=white&color=0bc5e2" alt="last-commit">
			<img src="https://img.shields.io/github/languages/top/eli64s/readme-ai?style=flat-square&color=0bc5e2" alt="repo-top-language">
			<img src="https://img.shields.io/github/languages/count/eli64s/readme-ai?style=flat-square&color=0bc5e2" alt="repo-language-count">
		</p>
		<p align="center">Tech Stack</p>
		<p align="center">
			<img src="https://img.shields.io/badge/Anthropic-191919.svg?style=flat-square&logo=Anthropic&logoColor=white" alt="Anthropic">
			<img src="https://img.shields.io/badge/precommit-FAB040.svg?style=flat-square&logo=pre-commit&logoColor=black" alt="precommit">
			<img src="https://img.shields.io/badge/Ruff-FCC21B.svg?style=flat-square&logo=Ruff&logoColor=black" alt="Ruff">
			<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat-square&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
			<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat-square&logo=Pytest&logoColor=white" alt="Pytest">
			<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat-square&logo=Docker&logoColor=white" alt="Docker">
			<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python">
			<br>
			<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=flat-square&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions">
			<img src="https://img.shields.io/badge/Poetry-60A5FA.svg?style=flat-square&logo=Poetry&logoColor=white" alt="Poetry">
			<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=flat-square&logo=AIOHTTP&logoColor=white" alt="AIOHTTP">
			<img src="https://img.shields.io/badge/Material%20for%20MkDocs-526CFE.svg?style=flat-square&logo=Material-for-MkDocs&logoColor=white" alt="Material%20for%20MkDocs">
			<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=flat-square&logo=OpenAI&logoColor=white" alt="OpenAI">
			<img src="https://img.shields.io/badge/Google%20Gemini-8E75B2.svg?style=flat-square&logo=Google-Gemini&logoColor=white" alt="Google%20Gemini">
			<img src="https://img.shields.io/badge/Pydantic-E92063.svg?style=flat-square&logo=Pydantic&logoColor=white" alt="Pydantic">
		</p>
		</div>
		<br>
		<hr>

		<div class="feature-container">

		<h3>Features:</h3>

		- text-based art logo
		- minimal and retro style
		- no image dependencies
		- good for terminal-focused tools

		</div>


	=== "ASCII_BOX"

		<div class="usage-container">
		<h3>Usage:</h3>

		```sh
		readmeai --header-style ascii_box --repository https://github.com/username/project
		```

		</div>

		<div class="output-container">
		<h3>Output:</h3>
		<div align="center">
		<pre>
		╔════════════════════════════════════════════════════════════════════╗
		║                                                                    ║
		║  ██████ ██████   ██   ████   ██   ██ ██████          ██   ██████   ║
		║  ██  ██ ██      ████  ██  ██ ███ ███ ██             ████    ██     ║
		║  ██████ ████   ██  ██ ██  ██ ██ █ ██ ████   ██████ ██  ██   ██     ║
		║  ██ ██  ██     ██████ ██  ██ ██   ██ ██            ██████   ██     ║
		║  ██  ██ ██████ ██  ██ ████   ██   ██ ██████        ██  ██ ██████   ║
		║                                                                    ║
		║                                                                    ║
		╚════════════════════════════════════════════════════════════════════╝
		</pre>
		</div>
		<p align="center">
			<em><code>❯ REPLACE-ME</code></em>
		</p>
		<p align="center">
			<img src="https://img.shields.io/github/license/eli64s/readme-ai?style=flat-square&logo=opensourceinitiative&logoColor=white&color=0bc5e2" alt="license">
			<img src="https://img.shields.io/github/last-commit/eli64s/readme-ai?style=flat-square&logo=git&logoColor=white&color=0bc5e2" alt="last-commit">
			<img src="https://img.shields.io/github/languages/top/eli64s/readme-ai?style=flat-square&color=0bc5e2" alt="repo-top-language">
			<img src="https://img.shields.io/github/languages/count/eli64s/readme-ai?style=flat-square&color=0bc5e2" alt="repo-language-count">
		</p>
		<p align="center">Tech Stack</p>
		<p align="center">
			<img src="https://img.shields.io/badge/Anthropic-191919.svg?style=flat-square&logo=Anthropic&logoColor=white" alt="Anthropic">
			<img src="https://img.shields.io/badge/precommit-FAB040.svg?style=flat-square&logo=pre-commit&logoColor=black" alt="precommit">
			<img src="https://img.shields.io/badge/Ruff-FCC21B.svg?style=flat-square&logo=Ruff&logoColor=black" alt="Ruff">
			<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat-square&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
			<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat-square&logo=Pytest&logoColor=white" alt="Pytest">
			<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat-square&logo=Docker&logoColor=white" alt="Docker">
			<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python">
			<br>
			<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=flat-square&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions">
			<img src="https://img.shields.io/badge/Poetry-60A5FA.svg?style=flat-square&logo=Poetry&logoColor=white" alt="Poetry">
			<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=flat-square&logo=AIOHTTP&logoColor=white" alt="AIOHTTP">
			<img src="https://img.shields.io/badge/Material%20for%20MkDocs-526CFE.svg?style=flat-square&logo=Material-for-MkDocs&logoColor=white" alt="Material%20for%20MkDocs">
			<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=flat-square&logo=OpenAI&logoColor=white" alt="OpenAI">
			<img src="https://img.shields.io/badge/Google%20Gemini-8E75B2.svg?style=flat-square&logo=Google-Gemini&logoColor=white" alt="Google%20Gemini">
			<img src="https://img.shields.io/badge/Pydantic-E92063.svg?style=flat-square&logo=Pydantic&logoColor=white" alt="Pydantic">
		</p>
		</div>
		<br>
		<hr>

		<div class="feature-container">

		<h3>Features:</h3>

		- text-based art logo
		- minimal and retro style
		- no image dependencies
		- good for terminal-focused tools

		</div>


---

## How It Works

README-AI provides several ways to customize your header style:

1. **Default Styles**: Choose from pre-defined header layouts
2. **Alignment Options**: Set text and image alignment
3. **Custom Sizing**: Adjust logo and image dimensions
4. **Badge Integration**: Incorporates shield badges and Tech Stack icons

The selected style will determine how your project's name, logo, description, and badges are arranged in the header section.

## Examples

### Using Classic Style

```sh
readmeai --header-style classic --repository https://github.com/username/project
```

### Using Modern Style with Custom Alignment

```sh
readmeai --header-style modern --align left --repository https://github.com/username/project
```

### Combining with Other Options

```sh
readmeai --header-style compact \
         --badge-style flat \
         --logo gradient \
         --repository https://github.com/username/project
```

## Tips for Using Header Styles

- **Classic**: Best for traditional open-source projects that need a professional look
- **Modern**: Great for documentation sites and projects with longer READMEs
- **Compact**: Ideal for smaller projects or when space is at a premium
- **SVG**: Perfect for projects that need custom branding or full-width banners
- **ASCII**: Good for terminal applications or when you want a retro feel

Consider these factors when choosing a header style:
- Your project's target audience
- The amount of content in your README
- Whether you have a custom logo or banner
- The overall aesthetic of your documentation
- How the style works with your chosen badge style

:warning: Some header styles may look different on different platforms or markdown renderers. It's a good idea to test how your chosen style looks on your target platform.


<!-- ## How to Customize the Header

To customize the header template, you can initialize the `HeaderTemplate` class and pass your preferred style (`classic`, `compact`, or `modern`). Here's an example:

```python
from readmeai.generators.headers import HeaderTemplate, HeaderStyleOptions

# Initialize the template with the desired style
header_template = HeaderTemplate(style=HeaderStyleOptions.MODERN)

# Data to render in the header
data = {
    "align": "center",
    "logo": "https://example.com/logo.png",
    "logo_size": "100px",
    "repo_name": "My Awesome Project",
    "tagline": "Building the future, one commit at a time.",
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
 -->
