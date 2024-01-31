## Command Line Interface

Run the `readmeai` command in your terminal with the following options to tailor your README file.

### CLI Options

| Option | Type | Description | Default Value  |
| ------ | ---- | ----------- | -------------- |
| `--align`, `-a` | String | Align the text in the README.md file's header. | `center` |
| `--badges`, `-b` | String | Badge icon style types for README.md badges. | ![badge-style](https://img.shields.io/badge/badge-style-0080ff) |
| `badge-color` | String | Badge color name or hex code. | ![badge-color](https://img.shields.io/badge/badge-color-0080ff) |
| `--emojis`, `-e` | Boolean | Adds emojis to the README.md file's header sections. | `False` |
| `--image`, `-i` | String | Project logo image displayed in the README file header. | `blue` |
| `🚧 --language` | String | Language for generating the README.md file. | `en` |
| `--max-tokens` | Integer | Maximum context window of the LLM API.  | `3899` |
| `--model`, `-m` | String | LLM API to use for text generation. | `gpt-3.5-turbo` |
| `--offline` | Boolean | Run CLI without a LLM API key. | `False` |
| `--output`, `-o` | String | Output file name for the README file. | `readme-ai.md` |
| `--repository`, `-r` | String | Repository URL or local directory path. | |
| `--temperature`, `-t` | Float | Sets the creativity level for content generation. | `1.0` |
| `🚧 --template` | String | README template style. | `default` |
| `--tree-depth` | Integer | Maximum depth of the directory tree structure. | `5` |
| `🚧 --vertex_ai` | Tuple (String) | Google Vertex AI configuration, requires location and project ID. | |
| `--help` | | Displays help information about the command and its options. | |

<sub><em><code>🚧 feature currently under development</code></em>

---

### Badges

The `--badges` option lets you select the style of the default badge set.
| **Style**      | **Preview** |
|------------------|----------|
| `default`        | ![license](https://img.shields.io/github/license/eli64s/readme-ai?flat&color=0080ff) ![last-commit](https://img.shields.io/github/last-commit/eli64s/readme-ai?flat&color=0080ff&logo=git&logoColor=white) ![languages](https://img.shields.io/github/languages/top/eli64s/readme-ai?flat&color=0080ff) ![language-count](https://img.shields.io/github/languages/count/eli64s/readme-ai?flat&color=0080ff) |
| `flat`           | ![flat](https://img.shields.io/badge/Python-3776AB.svg?&style=flat&logo=Python&logoColor=white) |
| `flat-square`    | ![flat-square](https://img.shields.io/badge/Python-3776AB.svg?&style=flat-square&logo=Python&logoColor=white) |
| `for-the-badge`  | ![for-the-badge](https://img.shields.io/badge/Python-3776AB.svg?&style=for-the-badge&logo=Python&logoColor=white) |
| `plastic`        | ![plastic](https://img.shields.io/badge/Python-3776AB.svg?&style=plastic&logo=Python&logoColor=white) |
| `skills`          | [![Skills](https://skillicons.dev/icons?i=py)](https://skillicons.dev) |
| `skills-light`    | [![Skills-Light](https://skillicons.dev/icons?i=py&theme=light)](https://skillicons.dev) |
| `social`         | ![social](https://img.shields.io/badge/Python-3776AB.svg?&style=social&logo=Python&logoColor=white) |


When providing the `--badges` option, readme-ai does two things:

1. Formats the default badge set to match the selection (i.e. flat, flat-square, etc.).
2. Generates an additional badge set representing your projects dependencies and tech stack (i.e. Python, Docker, etc.)

#### Example
>
> ```console
> $ readmeai --badges flat-square --repository https://github.com/eli64s/readme-ai
> ```
>
#### Output
>
> {... project logo ...}
>
> {... project name ...}
>
> {...project slogan...}
>
> <img src="https://img.shields.io/github/license/eli64s/readme-ai?style=flat-square&color=0080ff">
> <img src="https://img.shields.io/github/last-commit/eli64s/readme-ai?style=flat-square&color=0080ff&logo=git&logoColor=white">
> <img src="https://img.shields.io/github/languages/top/eli64s/readme-ai?style=flat-square&color=0080ff">
> <img src="https://img.shields.io/github/languages/count/eli64s/readme-ai?style=flat-square&color=0080ff">
>
> <br>
>
>	*Developed with the software and tools below.*
>
> <img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat-square&logo=GNU-Bash&logoColor=white">
> <img src="https://img.shields.io/badge/tqdm-FFC107.svg?style=flat-square&logo=tqdm&logoColor=black">
> <img src="https://img.shields.io/badge/Pydantic-E92063.svg?style=flat-square&logo=Pydantic&logoColor=white">
> <img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat-square&logo=YAML&logoColor=white" alt="YAML">
> <img src="https://img.shields.io/badge/Poetry-60A5FA.svg?style=flat-square&logo=Poetry&logoColor=white">
> <img src="https://img.shields.io/badge/OpenAI-412991.svg?style=flat-square&logo=OpenAI&logoColor=white">
> <br>
> <img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white">
> <img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=flat-square&logo=AIOHTTP&logoColor=white">
> <img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat-square&logo=Docker&logoColor=white">
> <img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=flat-square&logo=GitHub-Actions&logoColor=white">
> <img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat-square&logo=Pytest&logoColor=white">
>
> <br>
>
> {... end of header ...}
>

---

### Project Logo

Select a project logo using the `--image` option. The following options are available:

|  |  |  |
|---|---|---|
| `default` | `gradient` | `black` |
| <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100"> | <img src="https://img.icons8.com/?size=512&id=55494&format=png" width="100"> | <img src="https://img.icons8.com/external-tal-revivo-regular-tal-revivo/96/external-readme-is-a-easy-to-build-a-developer-hub-that-adapts-to-the-user-logo-regular-tal-revivo.png" width="100"> |
| `cloud` | `purple` | `grey` |
|<img src="https://cdn-icons-png.flaticon.com/512/6295/6295417.png" width="100"> | <img src="https://img.icons8.com/external-tal-revivo-duo-tal-revivo/100/external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-duo-tal-revivo.png" width="100"> | <img src="https://img.icons8.com/external-tal-revivo-filled-tal-revivo/96/external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-filled-tal-revivo.png" width="100"> |

<br>

Use the `--image custom` option to invoke a prompt to enter a custom image URL or path.

---
