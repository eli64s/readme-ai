
## Project Badges

The `--badge-style` option lets you select the style of the default badge set.

<table>
  <tr>
    <th style="text-align: left;">Style</th>
    <th style="text-align: center;">Preview</th>
  </tr>
  <tr>
    <td><strong>default</strong></td>
    <td align="center"><a href="https://img.shields.io/github/license/eli64s/readme-ai?flat&color=0080ff&logo=opensourceinitiative&logoColor=white" target="_blank"><img src="https://img.shields.io/github/license/eli64s/readme-ai?flat&color=0080ff&logo=opensourceinitiative&logoColor=white"></a> <a href="https://img.shields.io/github/last-commit/eli64s/readme-ai?flat&color=0080ff&logo=git&logoColor=white" target="_blank"><img src="https://img.shields.io/github/last-commit/eli64s/readme-ai?flat&color=0080ff&logo=git&logoColor=white"></a> <a href="https://img.shields.io/github/languages/top/eli64s/readme-ai?flat&color=0080ff" target="_blank"><img src="https://img.shields.io/github/languages/top/eli64s/readme-ai?flat&color=0080ff"></a> <a href="https://img.shields.io/github/languages/count/eli64s/readme-ai?flat&color=0080ff" target="_blank"><img src="https://img.shields.io/github/languages/count/eli64s/readme-ai?flat&color=0080ff"></a></td>
  </tr>
  <tr>
    <td><strong>flat</strong></td>
    <td align="center"><a href="https://img.shields.io/badge/Python-3776AB.svg?&style=flat&logo=Python&logoColor=white" target="_blank"><img src="https://img.shields.io/badge/Python-3776AB.svg?&style=flat&logo=Python&logoColor=white"></a></td>
  </tr>
  <tr>
    <td><strong>flat-square</strong></td>
    <td align="center"><a href="https://img.shields.io/badge/Python-3776AB.svg?&style=flat-square&logo=Python&logoColor=white" target="_blank"><img src="https://img.shields.io/badge/Python-3776AB.svg?&style=flat-square&logo=Python&logoColor=white"></a></td>
  </tr>
  <tr>
    <td><strong>for-the-badge</strong></td>
    <td align="center"><a href="https://img.shields.io/badge/Python-3776AB.svg?&style=for-the-badge&logo=Python&logoColor=white" target="_blank"><img src="https://img.shields.io/badge/Python-3776AB.svg?&style=for-the-badge&logo=Python&logoColor=white"></a></td>
  </tr>
  <tr>
    <td><strong>plastic</strong></td>
    <td align="center"><a href="https://img.shields.io/badge/Python-3776AB.svg?&style=plastic&logo=Python&logoColor=white" target="_blank"><img src="https://img.shields.io/badge/Python-3776AB.svg?&style=plastic&logo=Python&logoColor=white"></a></td>
  </tr>
  <tr>
    <td><strong>skills</strong></td>
    <td align="center"><a href="https://skillicons.dev/" target="_blank"><img src="https://skillicons.dev/icons?i=py" alt="Python Skill Icon"></a></td>
  </tr>
  <tr>
    <td><strong>skills-light</strong></td>
    <td align="center"><a href="https://skillicons.dev/" target="_blank"><img src="https://skillicons.dev/icons?i=py&theme=light" alt="Python Skill Light Icon"></a></td>
  </tr>
  <tr>
    <td><strong>social</strong></td>
    <td align="center"><a href="https://img.shields.io/badge/Python-3776AB.svg?&style=social&logo=Python&logoColor=white" target="_blank"><img src="https://img.shields.io/badge/Python-3776AB.svg?&style=social&logo=Python&logoColor=white"></a></td>
  </tr>
</table>

When providing the `--badge-style` option, readme-ai does two things:

1. Formats the default badge set to match the selection (i.e. flat, flat-square, etc.).
2. Generates an additional badge set representing your projects dependencies and tech stack (i.e. Python, Docker, etc.)

#### Example
>
> ```sh
> ❯ readmeai --badge-style flat-square --repository https://github.com/eli64s/readme-ai
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
> <img src="https://img.shields.io/github/license/eli64s/readme-ai?style=flat-square&color=0080ff&logo=opensourceinitiative&logoColor=white">
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
