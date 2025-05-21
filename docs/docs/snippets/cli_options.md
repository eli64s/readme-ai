<!-- --8<------ [start:options] -->
```console
Usage: readmeai [OPTIONS]

  Entry point for the readme-ai CLI application.

Options:
  -V, --version                   Show the version and exit.
  -a, --align [center|left|right]
                                  align for the README.md file header
                                  sections.
  --api [anthropic|gemini|ollama|openai|offline]
                                  LLM API service provider to power the README
                                  file generation.
  -bc, --badge-color TEXT         Primary color (hex code or name) to use for
                                  the badge icons.
  -bs, --badge-style [default|flat|flat-square|for-the-badge|plastic|skills|skills-light|social]
                                  Visual style of the badge icons used in the
                                  README file.
  --base-url TEXT                 Base URL for the LLM API service.
  -cw, --context-window INTEGER   Maximum number of tokens to use for the
                                  model's context window.
  -e, --emojis [default|minimal|ascension|fibonacci|harmony|prism|quantum|monochrome|unicode|atomic|cosmic|crystal|earth|fire|forest|nature|water|gradient|rainbow|solar|fun|vintage|zen|random]
                                  Emoji theme 'packs' for customizing header
                                  section titles.
  -hs, --header-style [ASCII|ASCII_BOX|BANNER|CLASSIC|CLEAN|COMPACT|CONSOLE|MODERN]
                                  README header style template options.
  -l, --logo [ANIMATED|BLACK|BLUE|GRADIENT|ORANGE|METALLIC|PURPLE|RAINBOW|TERMINAL|CUSTOM|LLM]
                                  Project logo for the README file.
  -ls, --logo-size TEXT           Project logo size.
  -m, --model TEXT                LLM API model to power the README file
                                  generation.
  -ns, --navigation-style [ACCORDION|BULLET|NUMBER|ROMAN]
                                  Navigation menu styles for the README table
                                  of contents.
  -o, --output TEXT               Output file path for the generated README
                                  file.
  -rl, --rate-limit INTEGER RANGE
                                  Number of requests per minute for the LLM
                                  API service.  [1<=x<=25]
  -r, --repository TEXT           Provide a repository URL (GitHub, GitLab,
                                  BitBucket) or local path.  [required]
  -sm, --system-message TEXT      System message to display in the README
                                  file.
  -t, --temperature FLOAT RANGE   Increasing temperature yields more
                                  randomness in text generation.  [x<=2.0]
  --top-p FLOAT RANGE             Top-p sampling probability for the model's
                                  generation.  [0.0<=x<=1.0]
  -td, --tree-max-depth INTEGER   Maximum depth of the directory tree
                                  generated for the README file.
  --help                          Show this message and exit.
```
<!-- --8<------ [end:options] -->
