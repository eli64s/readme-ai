---
title: Project Logo
---

Your project's logo serves as its visual identity, creating an immediate and lasting impression on visitors. ReadmeAI provides a variety of SVG logo options designed to give your project a professional, distinctive appearance while ensuring consistent quality across different platforms and display sizes.

## Configuration

Add a logo to your README using the `--logo` flag:

```bash
readmeai --logo <style> --repository <url-or-path>
```

## Available Styles

=== "animated"

    A dynamic logo with subtle animation effects, perfect for adding visual interest.

    ```sh
    readmeai --logo animated --repository https://github.com/username/project
    ```

    **Example output:**

    <svg width="128" height="128" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <linearGradient id="animatedGradient" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" style="stop-color: #FF0000">
                    <animate attributeName="stop-color" values="#FF0000; #00FF00; #0000FF; #FF0000" dur="3s" repeatCount="indefinite" />
                </stop>
                <stop offset="100%" style="stop-color: #00FF00">
                    <animate attributeName="stop-color" values="#00FF00; #0000FF; #FF0000; #00FF00" dur="3s" repeatCount="indefinite" />
                </stop>
            </linearGradient>
        </defs>
        <path fill="url(#animatedGradient)" d="M6.345 5h2.1v6.533H6.993l.055-5.31-1.774 5.31H4.072l-1.805-5.31c.04.644.06 5.31.06 5.31H1V5h2.156s1.528 4.493 1.577 4.807L6.345 5zm6.71 3.617v-3.5H11.11v3.5H9.166l2.917 2.916L15 8.617h-1.945z" />
    </svg>

=== "aurora"

    A vibrant, colorful design inspired by the beauty of the Northern Lights.

    ```sh
    readmeai --logo aurora --repository https://github.com/username/project
    ```

    **Example output:**

    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="100" height="100">
        <defs>
            <linearGradient id="auroraGradient" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" style="stop-color: #00FF87" />
                <stop offset="33%" style="stop-color: #60EFFF" />
                <stop offset="66%" style="stop-color: #00FF87" />
                <stop offset="100%" style="stop-color: #533483" />
            </linearGradient>
        </defs>
        <path fill="url(#auroraGradient)"
            d="M 5 6 C 3.346 6 2 7.346 2 9 L 2 21 C 2 22.654 3.346 24 5 24 L 11.183594 23.980469 C 12.173594 23.980469 13.133031 24.290844 13.957031 24.839844 L 16 26.201172 L 18.042969 24.839844 C 18.866969 24.290844 19.826406 24 20.816406 24 L 27 24 C 28.654 24 30 22.654 30 21 L 30 9 C 30 7.346 28.654 6 27 6 L 20.816406 6 C 19.430406 6 18.086594 6.4077813 16.933594 7.1757812 L 16 7.7988281 L 15.066406 7.1757812 C 13.912406 6.4067813 12.570594 6 11.183594 6 L 5 6 z M 5 8 L 11.183594 8 C 12.173594 8 13.133031 8.2908438 13.957031 8.8398438 L 16 10.201172 L 18.042969 8.8398438 C 18.866969 8.2908438 19.826406 8 20.816406 8 L 27 8 C 27.552 8 28 8.449 28 9 L 28 21 C 28 21.551 27.552 22 27 22 L 20.816406 22 C 19.430406 22 18.086594 22.407781 16.933594 23.175781 L 16 23.798828 L 15.066406 23.175781 C 13.912406 22.406781 12.570594 22 11.183594 22 L 5 22 C 4.448 22 4 21.551 4 21 L 4 9 C 4 8.449 4.448 8 5 8 z M 6 12 L 6 14 L 14 14 L 14 12 L 6 12 z M 18 12 L 18 14 L 26 14 L 26 12 L 18 12 z M 6 16 L 6 18 L 14 18 L 14 16 L 6 16 z M 18 16 L 18 18 L 26 18 L 26 16 L 18 16 z" />
        <!-- <text x="16" y="35" text-anchor="middle" font-family="Arial" font-size="4" fill="#333">readme-ai</text> -->
    </svg>

=== "blue"

    A classic blue design that conveys trust and reliability.

    ```sh
    readmeai --logo blue --repository https://github.com/username/project
    ```

    **Example output:**

    <svg width="128" height="128" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <!-- Creating an ocean-inspired gradient -->
            <linearGradient id="oceanGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#00BFFF" /> <!-- Deep Sky Blue -->
                <stop offset="25%" style="stop-color:#1E90FF" /> <!-- Dodger Blue -->
                <stop offset="50%" style="stop-color:#0000CD" /> <!-- Medium Blue -->
                <stop offset="75%" style="stop-color:#000080" /> <!-- Navy Blue -->
                <stop offset="100%" style="stop-color:#191970" /> <!-- Midnight Blue -->
            </linearGradient>
            <!-- Adding a subtle glow effect for depth -->
            <filter id="oceanGlow" x="-20%" y="-20%" width="140%" height="140%">
                <feGaussianBlur in="SourceGraphic" stdDeviation="0.5" />
                <feColorMatrix type="matrix" values="
                    0 0 0 0 0
                    0 0.5 1 0 0
                    1 0.5 0 0 0
                    0 0 0 1 0
                " />
            </filter>
        </defs>
        <!-- Background rectangle with gradient -->
        <rect x="2.5" y="7.955" width="27" height="16.091" style="fill:none;stroke:url(#oceanGradient);stroke-width:1.2" filter="url" />
        <!-- Markdown 'M' letter -->
        <polygon points="5.909 20.636 5.909 11.364 8.636 11.364 11.364 14.773 14.091 11.364 16.818 11.364 16.818 20.636 14.091 20.636 14.091 15.318 11.364 18.727 8.636 15.318 8.636 20.636 5.909 20.636" style="fill:url(#oceanGradient)" />
        <!-- Down arrow -->
        <polygon points="22.955 20.636 18.864 16.136 21.591 16.136 21.591 11.364 24.318 11.364 24.318 16.136 27.045 16.136 22.955 20.636" style="fill:url(#oceanGradient)" />
    </svg>

=== "green"

    A modern design featuring smooth color transitions.

    ```sh
    readmeai --logo green --repository https://github.com/username/project
    ```

    **Example output:**

    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="100" height="100">
        <defs>
            <linearGradient id="triColorGradient" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" style="stop-color: #03A9F4" />
                <stop offset="50%" style="stop-color: #39FF14" />
                <stop offset="100%" style="stop-color: #8F0AEA" />
            </linearGradient>
        </defs>
        <path fill="url(#triColorGradient)"
            d="M 5 6 C 3.346 6 2 7.346 2 9 L 2 21 C 2 22.654 3.346 24 5 24 L 11.183594 23.980469 C 12.173594 23.980469 13.133031 24.290844 13.957031 24.839844 L 16 26.201172 L 18.042969 24.839844 C 18.866969 24.290844 19.826406 24 20.816406 24 L 27 24 C 28.654 24 30 22.654 30 21 L 30 9 C 30 7.346 28.654 6 27 6 L 20.816406 6 C 19.430406 6 18.086594 6.4077813 16.933594 7.1757812 L 16 7.7988281 L 15.066406 7.1757812 C 13.912406 6.4067813 12.570594 6 11.183594 6 L 5 6 z M 5 8 L 11.183594 8 C 12.173594 8 13.133031 8.2908438 13.957031 8.8398438 L 16 10.201172 L 18.042969 8.8398438 C 18.866969 8.2908438 19.826406 8 20.816406 8 L 27 8 C 27.552 8 28 8.449 28 9 L 28 21 C 28 21.551 27.552 22 27 22 L 20.816406 22 C 19.430406 22 18.086594 22.407781 16.933594 23.175781 L 16 23.798828 L 15.066406 23.175781 C 13.912406 22.406781 12.570594 22 11.183594 22 L 5 22 C 4.448 22 4 21.551 4 21 L 4 9 C 4 8.449 4.448 8 5 8 z M 6 12 L 6 14 L 14 14 L 14 12 L 6 12 z M 18 12 L 18 14 L 26 14 L 26 12 L 18 12 z M 6 16 L 6 18 L 14 18 L 14 16 L 6 16 z M 18 16 L 18 18 L 26 18 L 26 16 L 18 16 z" />
        <!-- <text x="16" y="35" text-anchor="middle" font-family="Arial" font-size="4" fill="#333">readme-ai</text> -->
    </svg>


=== "ice"

    A fun, colorful design that evokes a sense of playfulness and creativity.

    ```sh
    readmeai --logo ice --repository https://github.com/username/project
    ```

    **Example output:**

    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="100" height="100">
        <defs>
            <linearGradient id="cyberGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color: #FF0080" />
                <stop offset="50%" style="stop-color: #00FFFF" />
                <stop offset="100%" style="stop-color: #7B00FF" />
            </linearGradient>
        </defs>
        <path fill="url(#cyberGradient)"
            d="M 5 6 C 3.346 6 2 7.346 2 9 L 2 21 C 2 22.654 3.346 24 5 24 L 11.183594 23.980469 C 12.173594 23.980469 13.133031 24.290844 13.957031 24.839844 L 16 26.201172 L 18.042969 24.839844 C 18.866969 24.290844 19.826406 24 20.816406 24 L 27 24 C 28.654 24 30 22.654 30 21 L 30 9 C 30 7.346 28.654 6 27 6 L 20.816406 6 C 19.430406 6 18.086594 6.4077813 16.933594 7.1757812 L 16 7.7988281 L 15.066406 7.1757812 C 13.912406 6.4067813 12.570594 6 11.183594 6 L 5 6 z M 5 8 L 11.183594 8 C 12.173594 8 13.133031 8.2908438 13.957031 8.8398438 L 16 10.201172 L 18.042969 8.8398438 C 18.866969 8.2908438 19.826406 8 20.816406 8 L 27 8 C 27.552 8 28 8.449 28 9 L 28 21 C 28 21.551 27.552 22 27 22 L 20.816406 22 C 19.430406 22 18.086594 22.407781 16.933594 23.175781 L 16 23.798828 L 15.066406 23.175781 C 13.912406 22.406781 12.570594 22 11.183594 22 L 5 22 C 4.448 22 4 21.551 4 21 L 4 9 C 4 8.449 4.448 8 5 8 z M 6 12 L 6 14 L 14 14 L 14 12 L 6 12 z M 18 12 L 18 14 L 26 14 L 26 12 L 18 12 z M 6 16 L 6 18 L 14 18 L 14 16 L 6 16 z M 18 16 L 18 18 L 26 18 L 26 16 L 18 16 z" />
        <!-- <text x="16" y="35" text-anchor="middle" font-family="Arial" font-size="4" fill="#333">readme-ai</text> -->
    </svg>

=== "metallic"

    A sophisticated design with a premium, metallic finish.

    ```sh
    readmeai --logo metallic --repository https://github.com/username/project
    ```

    **Example output:**

    <svg width="128" height="128" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <radialGradient id="metallicGradient" cx="50%" cy="50%" r="75%">
                <stop offset="0%" style="stop-color: #FFFFFF" />
                <stop offset="50%" style="stop-color: #B8B8B8" />
                <stop offset="75%" style="stop-color: #808080" />
                <stop offset="100%" style="stop-color: #404040" />
            </radialGradient>
        </defs>
        <path fill="url(#metallicGradient)" d="M6.345 5h2.1v6.533H6.993l.055-5.31-1.774 5.31H4.072l-1.805-5.31c.04.644.06 5.31.06 5.31H1V5h2.156s1.528 4.493 1.577 4.807L6.345 5zm6.71 3.617v-3.5H11.11v3.5H9.166l2.917 2.916L15 8.617h-1.945z" />
    </svg>

=== "midnight"

    A sleek, monochrome design that emphasizes clarity and professionalism.

    ```sh
    readmeai --logo midnight --repository https://github.com/username/project
    ```

    **Example output:**

    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <linearGradient id="navyBlackGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#1a2c4f;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#0a0a0a;stop-opacity:1" />
            </linearGradient>
        </defs>
        <path fill-rule="evenodd" clip-rule="evenodd" d="M4 5.5H9C10.1046 5.5 11 6.39543 11 7.5V16.5C11 17.0523 10.5523 17.5 10 17.5H4C3.44772 17.5 3 17.0523 3 16.5V6.5C3 5.94772 3.44772 5.5 4 5.5ZM14 19.5C13.6494 19.5 13.3128 19.4398 13 19.3293V19.5C13 20.0523 12.5523 20.5 12 20.5C11.4477 20.5 11 20.0523 11 19.5V19.3293C10.6872 19.4398 10.3506 19.5 10 19.5H4C2.34315 19.5 1 18.1569 1 16.5V6.5C1 4.84315 2.34315 3.5 4 3.5H9C10.1947 3.5 11.2671 4.02376 12 4.85418C12.7329 4.02376 13.8053 3.5 15 3.5H20C21.6569 3.5 23 4.84315 23 6.5V16.5C23 18.1569 21.6569 19.5 20 19.5H14ZM13 7.5V16.5C13 17.0523 13.4477 17.5 14 17.5H20C20.5523 17.5 21 17.0523 21 16.5V6.5C21 5.94772 20.5523 5.5 20 5.5H15C13.8954 5.5 13 6.39543 13 7.5ZM5 7.5H9V9.5H5V7.5ZM15 7.5H19V9.5H15V7.5ZM19 10.5H15V12.5H19V10.5ZM5 10.5H9V12.5H5V10.5ZM19 13.5H15V15.5H19V13.5ZM5 13.5H9V15.5H5V13.5Z" fill="url(#navyBlackGradient)" />
    </svg>

=== "orange"

    An energetic design that stands out while maintaining professionalism.

    ```sh
    readmeai --logo orange --repository https://github.com/username/project
    ```

    **Example output:**

    <svg width="128" height="128" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <linearGradient id="sunsetGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#FF6B6B"/>
                <stop offset="50%" style="stop-color:#FFB88C"/>
                <stop offset="100%" style="stop-color:#FFE66D"/>
            </linearGradient>
        </defs>
        <path fill="url(#sunsetGradient)" d="M854.6 288.7c6 6 9.4 14.1 9.4 22.6V928c0 17.7-14.3 32-32 32H192c-17.7 0-32-14.3-32-32V96c0-17.7 14.3-32 32-32h424.7c8.5 0 16.7 3.4 22.7 9.4l215.2 215.3zM790.2 326L602 137.8V326h188.2zM426.13 600.93l59.11 132.97a16 16 0 0 0 14.62 9.5h24.06a16 16 0 0 0 14.63-9.51l59.1-133.35V758a16 16 0 0 0 16.01 16H641a16 16 0 0 0 16-16V486a16 16 0 0 0-16-16h-34.75a16 16 0 0 0-14.67 9.62L512.1 662.2l-79.48-182.59a16 16 0 0 0-14.67-9.61H383a16 16 0 0 0-16 16v272a16 16 0 0 0 16 16h27.13a16 16 0 0 0 16-16V600.93z"/>
    </svg>

=== "purple"

    A rich, creative design that suggests innovation and uniqueness.

    ```sh
    readmeai --logo purple --repository https://github.com/username/project
    ```

    **Example output:**

    <svg width="128" height="128" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style="color: blueviolet;">
        <path fill-rule="evenodd" clip-rule="evenodd" d="M4 5.5H9C10.1046 5.5 11 6.39543 11 7.5V16.5C11 17.0523 10.5523 17.5 10 17.5H4C3.44772 17.5
            3 17.0523 3 16.5V6.5C3 5.94772 3.44772 5.5 4 5.5ZM14 19.5C13.6494 19.5 13.3128 19.4398 13
            19.3293V19.5C13 20.0523 12.5523 20.5 12 20.5C11.4477 20.5 11 20.0523 11 19.5V19.3293C10.6872
            19.4398 10.3506 19.5 10 19.5H4C2.34315 19.5 1 18.1569 1 16.5V6.5C1 4.84315 2.34315 3.5 4 3.5H9C10.1947
            3.5 11.2671 4.02376 12 4.85418C12.7329 4.02376 13.8053 3.5 15 3.5H20C21.6569 3.5 23 4.84315 23
            6.5V16.5C23 18.1569 21.6569 19.5 20 19.5H14ZM13 7.5V16.5C13 17.0523 13.4477 17.5 14 17.5H20C20.5523
            17.5 21 17.0523 21 16.5V6.5C21 5.94772 20.5523 5.5 20 5.5H15C13.8954 5.5 13 6.39543 13 7.5ZM5
            7.5H9V9.5H5V7.5ZM15 7.5H19V9.5H15V7.5ZM19 10.5H15V12.5H19V10.5ZM5 10.5H9V12.5H5V10.5ZM19
            13.5H15V15.5H19V13.5ZM5 13.5H9V15.5H5V13.5Z" fill="currentColor" />
    </svg>

=== "rainbow"

    A vibrant, multi-colored design celebrating diversity and creativity.

    ```sh
    readmeai --logo rainbow --repository https://github.com/username/project
    ```

    **Example output:**

    <svg width="128" height="128" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <linearGradient id="rainbowGradient" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" style="stop-color: #FF0000"/> <!-- Red -->
                <stop offset="16.67%" style="stop-color: #FF7F00"/> <!-- Orange -->
                <stop offset="33.33%" style="stop-color: #FFFF00"/> <!-- Yellow -->
                <stop offset="50%" style="stop-color: #00FF00"/> <!-- Green -->
                <stop offset="66.67%" style="stop-color: #0000FF"/> <!-- Blue -->
                <stop offset="83.33%" style="stop-color: #4B0082"/> <!-- Indigo -->
                <stop offset="100%" style="stop-color: #8F00FF"/> <!-- Violet -->
            </linearGradient>
        </defs>
        <path fill="url(#rainbowGradient)" d="M6.345 5h2.1v6.533H6.993l.055-5.31-1.774 5.31H4.072l-1.805-5.31c.04.644.06 5.31.06 5.31H1V5h2.156s1.528 4.493 1.577 4.807L6.345 5zm6.71 3.617v-3.5H11.11v3.5H9.166l2.917 2.916L15 8.617h-1.945z"/>
    </svg>

=== "terminal"

    A tech-focused design that pays homage to command-line interfaces.

    ```sh
    readmeai --logo terminal --repository https://github.com/username/project
    ```

    **Example output:**

    <svg width="128" height="128" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">
        <defs>
        <linearGradient id="terminalGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#4B0082;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#8A2BE2;stop-opacity:1" />
        </linearGradient>
        <filter id="blur">
            <feGaussianBlur in="SourceGraphic" stdDeviation="0.3" />
        </filter>
        </defs>
        <rect x="4" y="65.048" width="504" height="381.896" fill="url(#terminalGradient)"/>
        <g>
        <path style="fill:#AAC1CE;" d="M512,61.048H0v389.904h512V61.048z M504,69.048v373.904H8V69.048H504"/>
        <rect x="3" y="126.848" style="fill:#AAC1CE;" width="505.84" height="8"/>
        </g>
        <circle style="fill:#E04F5F;" cx="48.08" cy="98.504" r="12.584"/>
        <circle style="fill:#25B6D2;" cx="89.312" cy="98.504" r="12.584"/>
        <circle style="fill:#32BEA6;" cx="130.568" cy="98.504" r="12.584"/>
        <!-- Background terminal text -->
        <text x="20" y="180" style="fill:#ffffff20;font-family:monospace;font-size:12px;filter:url(#blur)">
        <tspan x="20" dy="0">Initializing readmeai...</tspan>
        <tspan x="20" dy="20">Loading dependencies...</tspan>
        <tspan x="20" dy="20">Running analyzer...</tspan>
        <tspan x="20" dy="20">Processing markdown...</tspan>
        <tspan x="20" dy="20">Generating documentation...</tspan>
        </text>
        <!-- Main command text -->
        <text x="50%" y="55%" style="fill:#ffffff;font-family:monospace;font-size:55px;font-weight:bold;text-anchor:middle">
        $ readme-ai
        </text>
    </svg>

## Technical Details

!!! info "Logo Implementation"

    ReadmeAI implements logos through:

    1. Vector-Based SVG Format
        - Scalable to any size without quality loss
        - Small file size for fast loading
        - Crisp display on all screen resolutions
        - Accessible and semantic markup

    2. Consistent Positioning
        - Automatically centered alignment
        - Responsive sizing
        - Proper spacing with surrounding elements
        - Clear visual hierarchy

## Advanced Usage

### Custom Logo Integration

You can use your own logo by providing a custom path:

```bash
readmeai --logo custom \
         --repository https://github.com/username/project
```

You will be prompted to provide the image path or URL:

1. Provide a local file path:
    ```console
    Provide an image file path or URL: /path/to/your/logo.svg
    ```

2. Provide a URL:
    ```console
    Provide an image file path or URL: https://example.com/logo.png
    ```

### AI-Generated Logos

For unique, project-specific logos, use the LLM option:

```bash
readmeai --logo llm \
         --api openai \
         --repository https://github.com/username/project
```

This feature is only available using the OpenAI API, powered by DALL·E 3 text-to-image model. The prompt used can be viewed [here](https://github.com/eli64s/readme-ai/blob/main/readmeai/config/settings/prompts.toml).

!!! note "AI Logo Generation"

    When using AI-generated logos:

    - Results may vary in quality and relevance
    - Multiple generations might be needed
    - Review and potentially edit the output
    - Consider the project's specific needs

## Best Practices

When selecting and implementing a project logo, consider these guidelines:

1. **Brand Alignment**: Choose a logo style that reflects your project's purpose and values. For example, use the terminal style for developer tools or the rainbow style for community-focused projects.

2. **Visual Impact**: Ensure your logo is clear and recognizable at different sizes. SVG formats help maintain quality across various displays.

3. **Context Awareness**: Consider how your logo will appear alongside other README elements like badges and headers.

4. **Color Psychology**: Different colors convey different messages:
    - Blue suggests reliability and professionalism
    - Orange conveys energy and creativity
    - Purple represents innovation and uniqueness
    - Black emphasizes elegance and simplicity

5. **Technical Considerations**: Take advantage of SVG benefits:
    - Vector-based scaling
    - Small file sizes
    - Animation capabilities
    - Accessibility features

## Style Selection Guide

Consider these factors when choosing your logo style:

- **animated**: Best for modern web applications wanting to add visual interest
- **black/metallic**: Ideal for professional business tools and enterprise projects
- **blue**: Perfect for traditional technology and development tools
- **gradient/rainbow**: Suitable for creative and innovative applications
- **orange/purple**: Great for standing out while maintaining professionalism
- **terminal**: Excellent for command-line tools and developer utilities

Each style has been carefully crafted to serve different project needs while maintaining professional standards and technical excellence.

---
