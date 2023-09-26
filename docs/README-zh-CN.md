<div align="center">
    <h1 align="center">
        <img src="https://img.icons8.com/?size=512&id=55494&format=png" width="80" />
        <img src="https://img.icons8.com/?size=512&id=kTuxVYRKeKEY&format=png" width="80" />
        <br>README-AI
    </h1>
    <h3>◦ 生成美观且内容丰富的 <i>README</i> 文件</h3>
    <h3>◦ 使用 OpenAI 的 GPT 语言模型 API 开发</h3>
    <br>
    <p align="center">
        <img src="https://img.shields.io/badge/Markdown-000000.svg?stylee&logo=Markdown&logoColor=white" alt="Markdown" />
        <img src="https://img.shields.io/badge/OpenAI-412991.svg?stylee&logo=OpenAI&logoColor=white" alt="OpenAI" />
        <img src="https://img.shields.io/badge/Python-3776AB.svg?stylee&logo=Python&logoColor=white" alt="Python" />
        <img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?stylee&logo=Pytest&logoColor=white" alt="pytest" />
        <img src="https://img.shields.io/badge/Docker-2496ED.svg?style&logo=Docker&logoColor=white" alt="Docker" />
        <img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style&logo=GitHub-Actions&logoColor=white" alt="actions" />
    </p>
    <a href="https://pypi.org/project/readmeai/">
        <img src="https://img.shields.io/pypi/v/readmeai?color=5D6D7E&logo=pypi" alt="pypi-version" />
    </a>
    <a href="https://pypi.org/project/readmeai/">
        <img src="https://img.shields.io/pypi/pyversions/readmeai?color=5D6D7E&logo=python" alt="pypi-python-version" />
    </a>
    <a href="https://pypi.org/project/readmeai/">
        <img src="https://img.shields.io/pypi/dm/readmeai?color=5D6D7E" alt="pypi-downloads" />
    </a>
    <img src="https://img.shields.io/github/license/eli64s/readme-ai?color=5D6D7E" alt="github-license" />
</div>

---

## 📖 目录

- [📖 目录](#-目录)
- [📍 概述](#-概述)
- [🎈 演示](#-演示)
- [🤖 功能](#-功能)
- [👩‍💻 使用](#-使用)
  - [🛠 安装](#-安装)
  - [⚙️ 配置](#️-配置)
  - [🚀 运行 *README-AI*](#-运行-readme-ai)
  - [🧪 测试](#-测试)
- [🛣 路线图](#-路线图)
- [📒 更新日志](#-更新日志)
- [🤝 贡献](#-贡献)
- [📄 许可证](#-许可证)
- [👏 致谢](#-致谢)

---

## 📍 概述

*README-AI* 是一个强大的命令行工具，用于为您的软件和数据项目生成强大的 README.md 文件。只需提供远程仓库 URL 或代码库路径，该工具即可利用 OpenAI 的 GPT 语言模型 API 为您的整个项目自动生成文档。

**🎯 动机**

简化编写和维护高质量项目文档的过程，提高开发者的生产力和工作流程。*readme-ai* 的最终目标是提高开源软件的采用和可用性，使所有技能水平的人都能更好地理解复杂的代码库，并轻松使用开源工具。

**⚠️ 免责声明**

该项目目前正在开发中，并有固定的配置。虽然 *readme-ai* 为文档提供了极好的起点，但重要的是要审查 OpenAI API 生成的所有文本，以确保它准确代表了您的代码库。

---

## 🎈 演示

***命令行界面***

‣ 通过 PyPI、Docker 等在终端中运行 <i>readme-ai</i>！

[cli-demo](https://github.com/eli64s/readme-ai/assets/43382407/645c2336-6ea7-444c-a927-5450930c5255)

<br>

***Streamlit 社区云***

‣ 在浏览器中直接使用 *readme-ai*！无需安装，无需编码！

[streamlit-demo](https://github.com/eli64s/readme-ai/assets/43382407/e8260e78-b684-4e72-941c-b3046b90c452)

---

## 🤖 功能

<details>
    <summary>
        <h2><br>❶ 项目徽章</h2>
    </summary>
    <table>
        <tr>
            <td>
                <h4><i>项目口号和徽章</i></h4>
                <p>
                    ‣ 通过<a href="https://github.com/eli64s/readme-ai/blob/main/readmeai/conf/conf.toml#L56">提示</a>OpenAI的GPT引擎生成突出显示您的项目的口号。
                </p>
                <p>
                    ‣ 使用<a href="https://shields.io/">Shields.io</a>徽章可视化代码库依赖项和元数据。
                </p>
            </td>
        </tr>
        <tr>
            <td>
                <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/badges.png" alt="badges" />
            </td>
        </tr>
    </table>
</details>
<details>
    <summary>
        <h2><br>❷ 代码库文档</h2>
    </summary>
    <table>
        <tr>
            <h4><i>目录树和文件摘要</i></h4>
            <p>
                ‣ 使用自定义树功能可视化您的项目的目录结构。
            </p>
            <p>
                ‣ OpenAI的<i>GPT</i>模型总结了代码库中的每个文件。
            </p>
        </tr>
        <tr>
            <td align="center">
                <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/repository-tree.png" alt="repository-tree" />
            </td>
            <td align="center">
                <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/code-summaries.png" alt="code-summaries" />
            </td>
        </tr>
    </table>
</details>
<details>
    <summary>
        <h2><br>❸ 概述和功能表</h2>
    </summary>
    <table>
        <tr>
            <td>
                <h4><i>提示文本生成</i></h4>
                <p>
                    ‣ 使用<a href="https://github.com/eli64s/readme-ai/blob/main/readmeai/conf/conf.toml#L31">详细提示</a>生成概述段落和功能表，其中嵌入了项目元数据。
                </p>
            </td>
        </tr>
        <tr>
            <td>
                <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/feature-table.png" alt="feature-table" />
            </td>
        </tr>
    </table>
</details>
<details>
    <summary>
        <h2><br>❹ 动态使用说明</h2>
    </summary>
    <table>
        <tr>
            <td>
                <h4><i>安装、运行和测试</i></h4>
                <p>
                    ‣ 生成安装、运行和测试您的项目的说明。通过识别代码库的主要语言并参考我们的<a href="https://github.com/eli64s/readme-ai/blob/main/readmeai/conf/language_setup.toml">language_setup.toml</a>配置文件来创建说明。
                </p>
            </td>
        </tr>
        <tr>
            <td>
                <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/usage-instructions.png" alt="usage-instructions" />
            </td>
        </tr>
    </table>
</details>
<details>
    <summary>
        <h2><br>❺ 贡献指南等等！</i></h2>
    </summary>
    <table>
        <tr>
            <td>
                <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/roadmap.png" alt="roadmap" />
            </td>
        </tr>
        <br>
        <tr>
            <td>
                <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/license.png" alt="license" />
            </td>
        </tr>
    </table>
</details>
<details>
    <summary>
        <h2><br>❻ 自定义模板 - 即将推出！</h2>
    </summary>
    <p>‣ 开发CLI选项，让用户从多种README风格中选择</p>
    <p>‣ 适用于数据、机器学习、网络开发等用例的模板！</p>
</details>
<details>
    <summary>
        <h2><br>❼ 示例README文件</h2>
    </summary>
    <table>
        <thead>
            <tr>
                <th></th>
                <th>输出文件</th>
                <th>仓库</th>
                <th>语言</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>1️⃣</td>
                <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/readme-python.md">readme-python.md</a></td>
                <td><a href="https://github.com/eli64s/readme-ai">readme-ai</a></td>
                <td>Python</td>
            </tr>
            <tr>
                <td>2️⃣</td>
                <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/readme-typescript.md">readme-typescript.md</a></td>
                <td><a href="https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript">chatgpt-app-react-typescript</a></td>
                <td>TypeScript, React</td>
            </tr>
            <tr>
                <td>3️⃣</td>
                <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/readme-javascript.md">readme-javascript.md</a></td>
                <td><a href="https://github.com/idosal/assistant-chat-gpt-javascript">assistant-chat-gpt-javascript</a></td>
                <td>JavaScript, React</td>
            </tr>
            <tr>
                <td>4️⃣</td>
                <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/readme-kotlin.md">readme-kotlin.md</a></td>
                <td><a href="https://github.com/rumaan/file.io-Android-Client">file.io-android-client</a></td>
                <td>Kotlin, Java, Android</td>
            </tr>
            <tr>
                <td>5️⃣</td>
                <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/readme-rust-c.md">readme-rust-c.md</a></td>
                <td><a href="https://github.com/DownWithUp/CallMon">rust-c-app</a></td>
                <td>C, Rust</td>
            </tr>
            <tr>
                <td>6️⃣</td>
                <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/readme-go.md">readme-go.md</a></td>
                <td><a href="https://github.com/olliefr/docker-gs-ping">go-docker-app</a></td>
                <td>Go</td>
            </tr>
            <tr>
                <td>7️⃣</td>
                <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/readme-java.md">readme-java.md</a></td>
                <td><a href="https://github.com/avjinder/Minimal-Todo">java-minimal-todo</a></td>
                <td>Java</td>
            </tr>
            <tr>
                <td>8️⃣</td>
                <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/readme-fastapi-redis.md">readme-fastapi-redis.md</a></td>
                <td><a href="https://github.com/FerrariDG/async-ml-inference">async-ml-inference</a></td>
                <td>Python, FastAPI, Redis</td>
            </tr>
            <tr>
                <td>9️⃣</td>
                <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/readme-mlops.md">readme-mlops.md</a></td>
                <td><a href="https://github.com/GokuMohandas/mlops-course">mlops-course</a></td>
                <td>Python, Jupyter</td>
            </tr>
            <tr>
                <td>🔟</td>
                <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/readme-pyflink.md">readme-pyflink.md</a></td>
                <td><a href="https://github.com/eli64s/flink-flow">flink-flow</a></td>
                <td>PyFlink</td>
            </tr>
        </tbody>
    </table>
</details>

<p align="right">
    <a href="#top"><b>🔝 返回</b></a>
</p>

---

## 👩‍💻 使用

***依赖***

请确保您的系统上已安装以下依赖：

- *Python 版本 3.9 或更高*
- *包管理器（例如 pip、conda、poetry）或 Docker*
- *OpenAI API 付费账户和 API 密钥*

<br>

***仓库***

使用 *readme-ai* 需要一个远程仓库 URL 或本地项目目录的路径。目前支持以下类型的仓库：
- *GitHub*
- *GitLab*
- *文件系统*

<br>

***OpenAI API***

使用 *readme-ai* 需要 OpenAI API 账户和 API 密钥。以下步骤概述了此过程：

<details closed><summary>🔐 OpenAI API - 设置指南</summary>

1. 访问 [OpenAI 网站](https://platform.openai.com/)。
2. 点击“免费注册”按钮。
3. 用您的信息填写注册表格，并同意服务条款。
4. 登录后，点击“API”标签。
5. 按照指南创建新的 API 密钥。
6. 复制 API 密钥并将其保管在安全的地方。

</details>

<details closed><summary>⚠️ OpenAI API - 警告性准则</summary>

1. **审核敏感信息**：在运行应用程序之前，请确保您的仓库中的所有内容都不包含敏感信息。请注意，*readme-ai* 不会从 README 文件中过滤出敏感数据，也不会修改您仓库中的任何文件。

2. **API 使用成本**：OpenAI API 是收费的，每个请求都会产生费用。成本可能会迅速累积，因此了解您的使用情况至关重要。您可以通过访问 [OpenAI API 使用仪表板](https://platform.openai.com/account/usage) 来监控您的 API 使用情况和相关成本。

3. **推荐付费账户**：强烈建议设置 OpenAI 的付费账户，以避免潜在问题。如果没有文件支付方式，您的 API 使用将被限制到基础 GPT-3 模型。这种限制可能会导致 README 文件生成不够准确，并可能由于请求限制而导致 API 错误。

4. **运行时间考虑**：README 文件的生成通常不到一分钟。如果过程超过几分钟（例如，3 分钟），建议终止 *readme-ai*，以防止过长的处理时间。

</details>

---

### 🛠 安装

***使用 Pip***

Pip 是大多数用户推荐的安装方法。


```sh
pip install --upgrade readmeai
```
<br>

***使用 Docker***

对于希望在容器化环境中运行应用程序的用户，推荐使用 Docker。

```sh
docker pull zeroxeli/readme-ai:latest
```

<br>
<details><summary><b><i>手动安装</i></b></summary>
<br>

1️⃣ 克隆 readme-ai 仓库。
```sh
git clone https://github.com/eli64s/readme-ai
```

2️⃣ 导航至 readme-ai 目录。

```sh
cd readme-ai
```

3️⃣ 使用下面的方法之一安装依赖。

***使用 Bash***
```sh
bash setup/setup.sh
```

***使用 Conda***
```sh
conda create -n readmeai python=3.9 -y && \
conda activate readmeai && \
pip install -r requirements.txt
```

***使用 Poetry***
```sh
poetry install
```

</details>

---

### ⚙️ 配置

<br>

***命令行参数***

要生成 *README.md* 文件，请在终端中使用 `readmeai` 命令，以及下面的参数。

| 短标记 | 长标记           | 描述                                               | 状态         |
|--------|------------------|----------------------------------------------------|--------------|
| `-k`   | `--api-key`      | 您的 OpenAI API 密钥。                             | 可选         |
| `-c`   | `--encoding`     | 编码规定了文本是如何转换成令牌的。                  | 可选         |
| `-e`   | `--engine`       | OpenAI GPT 语言模型引擎 (gpt-3.5-turbo)            | 可选         |
| `-f`   | `--offline-mode` | 离线运行，不调用 OpenAI API。                      | 可选         |
| `-o`   | `--output`       | 您的 README.md 文件的输出路径。                     | 可选         |
| `-r`   | `--repository`   | 您的代码仓库的 URL 或路径。                         | 必填         |
| `-t`   | `--temperature`  | 模型的温度（随机性）。                             | 可选         |
| `-l`   | `--language`     | README 文件中所写文本的语言。                       | 即将推出！   |
| `-s`   | `--style`        | 要使用的 README 模板格式。(即将推出！)             | 即将推出！   |

<br>

***自定义设置***

要自定义 README 文件生成过程，您可以修改 [配置文件：](https://github.com/eli64s/readme-ai/blob/main/readmeai/conf/conf.toml) 中的以下部分：

- [*api*](https://github.com/eli64s/readme-ai/blob/main/readmeai/conf/conf.toml#L2) - OpenAI 语言模型 API 配置设置。
- [*git*](https://github.com/eli64s/readme-ai/blob/main/readmeai/conf/conf.toml#L12) - 如果未提供仓库，则使用默认的 git 仓库设置。
- [*paths*](https://github.com/eli64s/readme-ai/blob/main/readmeai/conf/conf.toml#L17) - *readme-ai* 应用程序使用的目录路径和文件。
- [*prompts*](https://github.com/eli64s/readme-ai/blob/main/readmeai/conf/conf.toml#L26) - 用于生成 README 文件的大型语言模型提示。
- [*md*](https://github.com/eli64s/readme-ai/blob/main/readmeai/conf/conf.toml#L59) - 用于构建 README 文件的动态 Markdown 部分代码模板。

---

### 🚀 运行 *README-AI*

<br>

***使用 Streamlit***

通过 Streamlit Community Cloud 直接在您的浏览器中使用该应用程序。

- [🛸 带我去 Streamlit 的 *readme-ai* ！](https://readmeai.streamlit.app/)

<br>

***使用 Pip***

```sh
# 选项 1: 使用所有必需的命令行参数运行 readmeai 命令。
readmeai --api-key "YOUR_API_KEY" --output readme-ai.md --repository https://github.com/eli64s/readme-ai
```
```sh
# 选项 2: 使用环境变量设置 OpenAI API 密钥运行 readmeai 命令。
export OPENAI_API_KEY="YOUR_API_KEY"
readmeai -o readme-ai.md -r https://github.com/eli64s/readme-ai
```

<br>

***使用 Docker***

```sh
# 选项 1: 使用所有必需的命令行参数运行 Docker 容器。
docker run -it \
-e OPENAI_API_KEY="YOUR_API_KEY" \
-v "$(pwd)":/app zeroxeli/readme-ai:latest \
readmeai -o readme-ai.md -r https://github.com/eli64s/readme-ai
```
```sh
# 选项 2: 使用环境变量设置 OpenAI API 密钥运行 Docker 容器。
export OPENAI_API_KEY="YOUR_API_KEY"
docker run -it \
-e OPENAI_API_KEY=$OPENAI_API_KEY

 \
-v "$(pwd)":/app zeroxeli/readme-ai:latest \
readmeai -o readme-ai.md -r https://github.com/eli64s/readme-ai
```

<br>

<details><summary><b><i>手动运行</i></b></summary>

<br>

***使用 Conda***
```sh
conda activate readmeai
export OPENAI_API_KEY="YOUR_API_KEY"
python readmeai/main.py -o readme-ai.md -r https://github.com/eli64s/readme-ai
```

<br>

***使用 Poetry***
```sh
poetry shell
export OPENAI_API_KEY="YOUR_API_KEY"
poetry run python readmeai/main.py -o readme-ai.md -r https://github.com/eli64s/readme-ai
```

</details>

---

### 🧪 测试

使用下面的命令执行测试套件。

```sh
bash scripts/test.sh
```

---

## 🛣 路线图

- [X] 通过 PyPI 发布项目作为 Python 库，并在 Docker Hub 上发布 Docker 镜像。
  - [*PyPI - readmeai*](https://pypi.org/project/readmeai/)
  - [*Docker Hub - readme-ai*](https://hub.docker.com/repository/docker/zeroxeli/readme-ai/general)
- [X] 整合并部署带有 Streamlit 的应用，为使用该工具提供简单的用户界面。
  - [*Streamlit Community Cloud - readmeai*](https://readmeai.streamlit.app/)
- [ ] 开发 GitHub Actions 脚本，当推送新代码时自动更新 README 文件。
- [ ] 为各种用例（例如，数据，web-dev，最小化等）设计 README 输出模板。
- [ ] 添加生成任何语言的 README 文件的支持（例如，CN，ES，FR，JA，KO，RU）。

---

## 📒 更新日志

[更新日志](https://github.com/eli64s/readme-ai/blob/main/CHANGELOG.md)

---

## 🤝 贡献

[贡献指南](https://github.com/eli64s/readme-ai/blob/main/CONTRIBUTING.md)

---

## 📄 许可证

[MIT](https://github.com/eli64s/readme-ai/blob/main/LICENSE)

---

## 👏 致谢

*徽章*
  - [Shields.io](https://shields.io/)
  - [Aveek-Saha/GitHub-Profile-Badges](https://github.com/Aveek-Saha/GitHub-Profile-Badges)
  - [Ileriayo/Markdown-Badges](https://github.com/Ileriayo/markdown-badges)

<p align="right">
  <a href="#top"><b>🔝 返回 </b></a>
</p>

---
