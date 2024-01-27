## Options

| Flag (Long/Short) | Default | Description | Type | Status |
|-------------------|---------|-------------|------|--------|
| `--align`/`-a` | `center` | Set header text alignment (`left`, `center`). | String | Optional |
| `--api-key`/`-k` | `OPENAI_API_KEY` env var | Your GPT model API key. | String | Optional |
| `--badges`/`-b` | `default` | Badge style options for your README file. | String | Optional |
| `--emojis`/`-e` | `False` | Add emojis to section header tiles. | Boolean | Optional |
| `--image`/`-i` | `default` | Project logo image displayed in README header. | String | Optional |
| `--max-tokens` | `3899` | Max number of tokens that can be generated. | Integer | Optional |
| `--model`/`-m` | `gpt-3.5-turbo` | Select GPT model for content generation. | String | Optional |
| `--offline` | `False` | Generate a README without an API key. | Boolean | Optional |
| `--output`/`-o` | `readme-ai.md` | README output file name. | Path/String | Optional |
| `--repository`/`-r` | None | Repository URL or local path. | URL/String | Required |
| `--temperature`/`-t` | `0.8` | LLM API creativity level. | Float | Optional |
| `--template` | None | Choose README template. | String | <em>WIP</em> |
| `--language`/`-l` | `English (en)` | Language for content. | String | <em>WIP</em> |

<sub><em>WIP</em> = work in progress, or feature currently under development.<br>For additional command-line information, run <code>readmeai --help</code> in your terminal for more details about each option.</sub><br>

## Badges

Select your preferred badge icon style to display in your output file using the `--badges` flag. The default badge style displays basic metadata about your repository using shields.io badges. If you select another option, the `default` badges will be automatically included.

| **Options**      | **Preview** |
|------------------|----------|
| `default`        | ![license](https://img.shields.io/github/license/eli64s/readme-ai?flat&color=0080ff) ![last-commit](https://img.shields.io/github/last-commit/eli64s/readme-ai?flat&color=0080ff) ![languages](https://img.shields.io/github/languages/top/eli64s/readme-ai?flat&color=0080ff) ![language-count](https://img.shields.io/github/languages/count/eli64s/readme-ai?flat&color=0080ff) |
| `flat`           | ![flat](https://img.shields.io/badge/Python-3776AB.svg?&style=flat&logo=Python&logoColor=white) |
| `flat-square`    | ![flat-square](https://img.shields.io/badge/Python-3776AB.svg?&style=flat-square&logo=Python&logoColor=white) |
| `for-the-badge`  | ![for-the-badge](https://img.shields.io/badge/Python-3776AB.svg?&style=for-the-badge&logo=Python&logoColor=white) |
| `plastic`        | ![plastic](https://img.shields.io/badge/Python-3776AB.svg?&style=plastic&logo=Python&logoColor=white) |
| `skills`          | [![Skills](https://skillicons.dev/icons?i=py)](https://skillicons.dev) |
| `skills-light`    | [![Skills-Light](https://skillicons.dev/icons?i=py&theme=light)](https://skillicons.dev) |
| `social`         | ![social](https://img.shields.io/badge/Python-3776AB.svg?&style=social&logo=Python&logoColor=white) |

## Project Logo

Select an image to display in your README header section using the `--image` flag.

| **Options**   | **Preview** |
|---------------|----------------|
| **default**   | <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100"> |
| **black**     | <img src="https://img.icons8.com/external-tal-revivo-regular-tal-revivo/96/external-readme-is-a-easy-to-build-a-developer-hub-that-adapts-to-the-user-logo-regular-tal-revivo.png" width="100"> |
| **gradient** | <img src="https://img.icons8.com/?size=512&id=55494&format=png" width="100"> |
| **grey**      | <img src="https://img.icons8.com/external-tal-revivo-filled-tal-revivo/96/external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-filled-tal-revivo.png" width="100"> |
| **purple**    | <img src="https://img.icons8.com/external-tal-revivo-duo-tal-revivo/100/external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-duo-tal-revivo.png" width="100"> |
| **yellow**    | <img src="https://img.icons8.com/pulsar-color/96/markdown.png" width="100"> |
| **cloud** | <img src="https://cdn-icons-png.flaticon.com/512/6295/6295417.png" width="100"> |

To provide your own image, use the CLI option `--image custom` and you will be prompted to enter a URL to your image.

---
