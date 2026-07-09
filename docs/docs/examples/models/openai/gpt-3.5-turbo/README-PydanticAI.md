<div id="top">

<!-- HEADER STYLE: COMPACT -->
<img src="../../../../../../readmeai/assets/logos/purple.svg" width="30%" align="left" style="margin-right: 15px">

# PYDANTIC-AI
<em>Empower your AI dreams with precision and ease.</em>

<!-- BADGES -->
<img src="https://img.shields.io/github/license/pydantic/pydantic-ai?style=for-the-badge&logo=opensourceinitiative&logoColor=white&color=0077cc" alt="license">
<img src="https://img.shields.io/github/last-commit/pydantic/pydantic-ai?style=for-the-badge&logo=git&logoColor=white&color=0077cc" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/pydantic/pydantic-ai?style=for-the-badge&color=0077cc" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/pydantic/pydantic-ai?style=for-the-badge&color=0077cc" alt="repo-language-count">

<em>Technology Stack:</em>

<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=for-the-badge&logo=HTML5&logoColor=white" alt="HTML5">
<img src="https://img.shields.io/badge/TOML-9C4121.svg?style=for-the-badge&logo=TOML&logoColor=white" alt="TOML">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/TypeScript-3178C6.svg?style=for-the-badge&logo=TypeScript&logoColor=white" alt="TypeScript">
<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=for-the-badge&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions">
<img src="https://img.shields.io/badge/uv-DE5FE9.svg?style=for-the-badge&logo=uv&logoColor=white" alt="uv">
<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=for-the-badge&logo=YAML&logoColor=white" alt="YAML">

<br clear="left"/>

## ⟡ Table of Contents

I. [⟡ Table of Contents](#-table-of-contents)<br>
II. [◈ Overview](#-overview)<br>
III. [⟢ Features](#-features)<br>
IV. [◇ Project Structure](#-project-structure)<br>
&nbsp;&nbsp;&nbsp;&nbsp;IV.a. [◊ Project Index](#-project-index)<br>
V. [⟠ Getting Started](#-getting-started)<br>
&nbsp;&nbsp;&nbsp;&nbsp;V.a. [⟁ Prerequisites](#-prerequisites)<br>
&nbsp;&nbsp;&nbsp;&nbsp;V.b. [⟒ Installation](#-installation)<br>
&nbsp;&nbsp;&nbsp;&nbsp;V.c. [⟓ Usage](#-usage)<br>
&nbsp;&nbsp;&nbsp;&nbsp;V.d. [⌆ Testing](#-testing)<br>
VI. [⟲ Roadmap](#-roadmap)<br>
VII. [⏣ Contributing](#-contributing)<br>
VIII. [⟶ License](#-license)<br>
IX. [❈ Acknowledgments](#-acknowledgments)<br>

---

## ◈ Overview

**Why pydantic-ai?**

This project simplifies AI development with efficient task management, robust validation, and flexible tool execution capabilities. The core features include:

- **🔧 Efficient Task Management:** Streamline tasks like dependencies installation, code formatting, and testing.
- **🛡️ Robust Validation:** Easily generate Pydantic validators and JSON schemas for seamless data validation.
- **🔄 Flexible Tool Execution:** Enhance agents with context-specific functions for versatile tool execution.
- **🔍 Comprehensive Message Handling:** Define and validate result data accurately for seamless agent runs.

---

## ⟢ Features

|      | Component       | Details                              |
| :--- | :-------------- | :----------------------------------- |
| ⚙️  | **Architecture**  | <ul><li>Follows a clean, modular design pattern.</li><li>Utilizes Python type hints for clear data validation.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Consistent code formatting across files.</li><li>Uses static type checking with mypy.</li><li>Well-structured classes and functions.</li></ul> |
| 📄 | **Documentation** | <ul><li>README.md and code comments provide detailed explanations.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integrates with GitHub Actions for CI/CD processes.</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Separation of concerns through multiple modules.</li><li>Encourages code reusability.</li></ul> |
| 🧪 | **Testing**       | <ul><li>Comprehensive unit tests covering different scenarios.</li><li>Uses pytest for testing framework.</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Efficient data validation and serialization processes.</li></ul> |
| 🛡️ | **Security**      | <ul><li>Implements data validation to prevent common security vulnerabilities.</li></ul> |
| 📦 | **Dependencies**  | <ul><li>Logs dependencies in `requirements.txt` and `pyproject.toml`.</li></ul> |

---

## ◇ Project Structure

```sh
└── pydantic-ai/
    ├── .github
    ├── LICENSE
    ├── Makefile
    ├── README.md
    ├── docs
    ├── examples
    ├── mkdocs.insiders.yml
    ├── mkdocs.yml
    ├── pydantic_ai_slim
    ├── pyproject.toml
    ├── requirements.txt
    ├── tests
    ├── uprev.py
    └── uv.lock
```

### ◊ Project Index

<details open>
	<summary><b><code>PYDANTIC-AI/</code></b></summary>
	<!-- __root__ Submodule -->
	<details>
		<summary><b>__root__</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ __root__</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/mkdocs.yml'>mkdocs.yml</a></b></td>
					<td style='padding: 8px;'>Define PydanticAI project details and customize documentation framework using MkDocs theme.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/requirements.txt'>requirements.txt</a></b></td>
					<td style='padding: 8px;'>Ensure cloud build script workaround in requirements.txt.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/Makefile'>Makefile</a></b></td>
					<td style='padding: 8px;'>- Define, manage, and execute tasks with the Makefile<br>- The file provides commands to install dependencies, run code formatting, linting, type checking, testing, and generate coverage reports<br>- Use recipes like install for package setup, test for running tests, and docs for documentation builds<br>- Maximize efficiency by leveraging these predefined actions across the project architecture.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/pyproject.toml'>pyproject.toml</a></b></td>
					<td style='padding: 8px;'>Generate a README file to explain the purpose and use of the code in the projects architecture.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/mkdocs.insiders.yml'>mkdocs.insiders.yml</a></b></td>
					<td style='padding: 8px;'>- Enhances Markdown functionality for preview purposes by adding various extensions for improved rendering of tables, admonitions, attributes, code highlighting, emojis, and more<br>- Allows customizing fenced code blocks with specific formats and introduces tabbed content feature<br>- Additionally, enables task lists, alternative list numbering, and includes a preview extension for comprehensive Markdown editing experience.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/uprev.py'>uprev.py</a></b></td>
					<td style='padding: 8px;'>- Root, examples, and slim<br>- On success, trigger a make sync command for synchronization, notifying users of the changes made<br>- Capture and convey any errors in version references to maintain code integrity.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- pydantic_ai_slim Submodule -->
	<details>
		<summary><b>pydantic_ai_slim</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ pydantic_ai_slim</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/pydantic_ai_slim/pyproject.toml'>pyproject.toml</a></b></td>
					<td style='padding: 8px;'>- Define the foundational elements and requirements of the pydantic-ai-slim project to set the stage for project development and functionality<br>- Primarily, this includes specifying necessary dependencies, defining project metadata such as the name, version, and description, and noting optional dependencies for tailored functionality<br>- These aspects facilitate smooth project maintenance and usage.</td>
				</tr>
			</table>
			<!-- pydantic_ai Submodule -->
			<details>
				<summary><b>pydantic_ai</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ pydantic_ai_slim.pydantic_ai</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/pydantic_ai_slim/pydantic_ai/_pydantic.py'>_pydantic.py</a></b></td>
							<td style='padding: 8px;'>- Generates Pydantic validators and JSON schemas from functions in the codebase<br>- Handles function schemas, validates parameters, and builds schemas for function parameters<br>- Handles context checking and schema generation, providing a robust toolset for building validators and schemata.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/pydantic_ai_slim/pydantic_ai/tools.py'>tools.py</a></b></td>
							<td style='padding: 8px;'>- Define tools to enhance agents with context-specific functions by enabling tool execution within the agent’s workflow<br>- The <code>tools.py</code> file in <code>pydantic_ai_slim</code> manages various tool aspects, like preparation, execution, and error handling, ensuring seamless integration and adaptability to different agent requirements.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/pydantic_ai_slim/pydantic_ai/_result.py'>_result.py</a></b></td>
							<td style='padding: 8px;'>- Define and validate result data for agent runs, handling both async and sync functions<br>- Build flexible result schemas enabling unique tool responses<br>- Support tool validation to return validated data or retry messages<br>- Specialize in structuring responses accurately for seamless interaction with the Large Language Model (LLM).</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/pydantic_ai_slim/pydantic_ai/result.py'>result.py</a></b></td>
							<td style='padding: 8px;'>- Illustrating the foundation for result handling in a Pydantic AI model, the <code>result.py</code> file encapsulates critical structures and methods<br>- It defines the base classes for non-streamed and streamed run results, respectively ensuring comprehensive message history retrieval and error handling<br>- Emphasizing structured data validation and asynchronous streaming capabilities, it underpins robust AI model output management.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/pydantic_ai_slim/pydantic_ai/_system_prompt.py'>_system_prompt.py</a></b></td>
							<td style='padding: 8px;'>- Define a SystemPromptRunner class handling asynchronous prompts, featuring data validation and processing logic<br>- The class determines whether input requires context and executes the prompt accordingly, ensuring proper execution within the designated context.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/pydantic_ai_slim/pydantic_ai/_griffe.py'>_griffe.py</a></b></td>
							<td style='padding: 8px;'>- The code in <code>_griffe.py</code> extracts function and parameter descriptions from docstrings, enhancing documentation readability<br>- By analyzing docstrings using predefined patterns, it infers specific formatting styles like Google, Numpy, or Sphinx, improving documentation consistency and clarity across the codebase architecture.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/pydantic_ai_slim/pydantic_ai/agent.py'>agent.py</a></b></td>
							<td style='padding: 8px;'>- SummaryThe <code>agent.py</code> file in the <code>pydantic_ai</code> module of the project contributes a crucial component known as the <code>Agent</code><br>- This <code>Agent</code> class handles various functionalities like capturing run messages, managing end strategies, and dealing with tool definitions and their contexts<br>- It interfaces with tools, settings, and dependencies to execute tasks within the system<br>- The <code>Agent</code> plays a significant role in orchestrating the execution flow and behavior of the system, ensuring seamless interactions between different components<br>- It encapsulates the logic for preparing and running tools, handling tool results, and managing the overall tool execution process<br>- Additionally, the <code>Agent</code> integrates closely with log management functionalities provided by <code>logfire_api</code> for comprehensive monitoring and logging capabilities.This file is indispensable to the projects architecture, serving as a central element responsible for coordinating tool executions, managing run contexts, and facilitating interactions between various system components<br>- It encapsulates essential business logic and functionality crucial for the project's overall operation and smooth execution.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/pydantic_ai_slim/pydantic_ai/messages.py'>messages.py</a></b></td>
							<td style='padding: 8px;'>- It includes system/user prompts, tool returns, retry prompts, text responses, and tool calls<br>- This file structures and manages messages sent to and from models using Pydantic for serialization/deserialization.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/pydantic_ai_slim/pydantic_ai/settings.py'>settings.py</a></b></td>
							<td style='padding: 8px;'>- Define and merge ModelSettings for configuring multiple LLM models, specifying parameters like <code>max_tokens</code>, <code>temperature</code>, <code>top_p</code>, and <code>timeout</code> to customize model behavior<br>- The <code>merge_model_settings</code> function combines and prioritizes settings for flexibility in usage across various scenarios.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/pydantic_ai_slim/pydantic_ai/py.typed'>py.typed</a></b></td>
							<td style='padding: 8px;'>Enable static type checking support for Pydantic models in the AI Slim module to enhance codebase clarity and maintainability.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/pydantic_ai_slim/pydantic_ai/exceptions.py'>exceptions.py</a></b></td>
							<td style='padding: 8px;'>- Define exception classes for handling errors and unexpected behaviors during agent runs, including retry attempts, user errors, usage limit breaches, and unexpected model behaviors<br>- These classes provide detailed messages and handling mechanisms within the projects architecture, enhancing error management and user experience.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/pydantic_ai_slim/pydantic_ai/usage.py'>usage.py</a></b></td>
							<td style='padding: 8px;'>- Define usage limits and manage LLM usage with structured classes for requests, tokens, and tokens response in the AI model<br>- Calculate total tokens, increment usage, and integrate token checks within the model limits for efficient processing and controlled request flows.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/pydantic_ai_slim/pydantic_ai/_utils.py'>_utils.py</a></b></td>
							<td style='padding: 8px;'>- Defines utility functions for handling asynchronous operations and data structures, including debouncing async iterators and managing runtime tasks<br>- It also includes type guards for ensuring data integrity during runtime<br>- The code showcases a blend of concurrency and data validation, crucial for robust async workflows and dynamic data handling.</td>
						</tr>
					</table>
					<!-- models Submodule -->
					<details>
						<summary><b>models</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ pydantic_ai_slim.pydantic_ai.models</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/pydantic_ai_slim/pydantic_ai/models/vertexai.py'>vertexai.py</a></b></td>
									<td style='padding: 8px;'>- Define a Vertex AIModel that integrates Gemini via the VertexAI API, enabling model interactions<br>- It initializes model settings like project ID, region, and authentication, facilitating URL and authentication setup<br>- This model operationally retrieves and manages necessary credentials, ensuring secured model agent functions<br>- This functionality streamlines communication between models and Vertex AI.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/pydantic_ai_slim/pydantic_ai/models/mistral.py'>mistral.py</a></b></td>
									<td style='padding: 8px;'>- The <code>mistral.py</code> file in the <code>pydantic_ai_slim</code> module within the codebase orchestrates AI model interactions with varying kinds of responses, aiding in streamlining communication and task completion<br>- It leverages multiple data models, HTTP interactions, and specialized tools to handle responses effectively<br>- These functionalities are encapsulated within this file, promoting efficiency and reliability in handling AI-driven tasks within the larger architecture.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/pydantic_ai_slim/pydantic_ai/models/gemini.py'>gemini.py</a></b></td>
									<td style='padding: 8px;'>- Pydantic_ai_slim-gemini.pyThe <code>gemini.py</code> file in the <code>pydantic_ai_slim</code> codebase plays a crucial role in handling model messages, requests, and responses within the AI slim framework<br>- It orchestrates communication between various components such as model tools, user prompts, and system prompts<br>- This file encapsulates the logic for processing model behaviors, retry prompts, as well as system and user interactions<br>- Additionally, it includes functionalities for handling structured and text responses from model tools<br>- By leveraging the definitions and settings configured within this module, developers can ensure a seamless flow of information and actions within the AI system.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/pydantic_ai_slim/pydantic_ai/models/test.py'>test.py</a></b></td>
									<td style='padding: 8px;'>- Creates a testing-focused model within the projects architecture, making or modifying tool calls as needed<br>- The models design allows for specific tools to be called, defines custom result text or arguments, and manages data seeding<br>- It can also be influenced by external factors like function and result tools in previous runs, providing flexibility for testing scenarios and refining tool interactions.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/pydantic_ai_slim/pydantic_ai/models/groq.py'>groq.py</a></b></td>
									<td style='padding: 8px;'>- Describe how to use GroqModel to interact with the Groq API for chat completion<br>- Includes initializing with a model name, using existing clients for operations, and creating agent models<br>- The model supports requests and streaming responses, with tools for message mapping and processing structured and text responses effectively<br>- Understand the model from the provided details to improve usage and performance.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/pydantic_ai_slim/pydantic_ai/models/openai.py'>openai.py</a></b></td>
									<td style='padding: 8px;'>- The OpenAIModel file in the projects architecture serves as a crucial component for interacting with the OpenAI API<br>- It enables users to initialize and utilize OpenAI models, facilitating interactions with the API through various methods like <code>agent_model</code>, <code>request</code>, and <code>request_stream</code><br>- The file encapsulates essential functions for creating model responses and handling streamed responses, ensuring seamless communication with OpenAI models.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/pydantic_ai_slim/pydantic_ai/models/anthropic.py'>anthropic.py</a></b></td>
									<td style='padding: 8px;'>- Define an Anthropic model representing a specific class using the Anthropic API<br>- The class interacts with the API via an AsyncHTTPClient, allowing the user to initialize the model with various parameters like the model name or an API key<br>- Instances of this model can create agent models with specific tools for processing messages and generating responses<br>- The code supports handling both streamed and non-streamed responses from the Anthropic API.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/pydantic_ai_slim/pydantic_ai/models/ollama.py'>ollama.py</a></b></td>
									<td style='padding: 8px;'>- Achieve Ollama model initialization using the OpenAI API<br>- Interact with Ollama server through OpenAI Python client, utilizing predefined or custom model names<br>- Support various function tools and provide agent models with specified parameters<br>- Incorporate base URL, API key, and HTTP client flexibility for adaptive usage.</td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/pydantic_ai_slim/pydantic_ai/models/function.py'>function.py</a></b></td>
									<td style='padding: 8px;'>- Define a model handling local functions, the <code>FunctionModel</code> class enables calling functions for requests, supporting non-streamed and streamed data<br>- It also encapsulates agent information through <code>AgentInfo</code>, facilitating the execution of function tools<br>- The model governs text and structured response streams, reflecting an organized flow of tool calls and messages within the projects architecture.</td>
								</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<!-- examples Submodule -->
	<details>
		<summary><b>examples</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ examples</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/examples/pyproject.toml'>pyproject.toml</a></b></td>
					<td style='padding: 8px;'>- Outline the purpose and utilization of the provided <code>pyproject.toml</code> within the broader project structure<br>- Emphasizing its role in managing build settings, project metadata, and listed dependencies, the file encapsulates essential configurations and requirements critical for maintaining and running the <code>pydantic-ai-examples</code> project successfully.</td>
				</tr>
			</table>
			<!-- pydantic_ai_examples Submodule -->
			<details>
				<summary><b>pydantic_ai_examples</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ examples.pydantic_ai_examples</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/examples/pydantic_ai_examples/pydantic_model.py'>pydantic_model.py</a></b></td>
							<td style='padding: 8px;'>- Construct a Pydantic model from text input using PydanticAI<br>- The code invokes an Agent with a specified model, then executes it to analyze text for city and country<br>- Useful for showcasing text processing capabilities with minimal setup required.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/examples/pydantic_ai_examples/roulette_wheel.py'>roulette_wheel.py</a></b></td>
							<td style='padding: 8px;'>- Demonstrate utilizing PydanticAI to create a roulette game<br>- Develop an agent identifying winning number dependencies and implement a function checking if a bet wins<br>- Pre-configured retries and a system prompt enhance the user experience<br>- Ideal for simulating roulette scenarios with clear outcome distinctions.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/examples/pydantic_ai_examples/chat_app.ts'>chat_app.ts</a></b></td>
							<td style='padding: 8px;'>- Enhances chat experience by streaming and rendering messages in real-time<br>- Parses response text into structured messages and dynamically updates the conversation display<br>- Handles form submission for user messages, implementing asynchronous fetching and error handling<br>- Supports smooth scrolling and message element management for an interactive chat application.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/examples/pydantic_ai_examples/sql_gen.py'>sql_gen.py</a></b></td>
							<td style='padding: 8px;'>- Demonstrate how PydanticAI generates SQL queries from user requests based on a predefined PostgreSQL database schema<br>- The code outlines prompt examples and query responses, ensuring valid SQL outputs through result validation<br>- By utilizing Pydantic models and asyncio functionalities, this file showcases seamless query generation and execution with built-in error handling and database connection management.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/examples/pydantic_ai_examples/bank_support.py'>bank_support.py</a></b></td>
							<td style='padding: 8px;'>- Illustrating the supportive functionality within the banking domain, the code orchestrates customer interactions and risk assessment<br>- Leveraging PydanticAI, it structures customer support advice and operational actions such as blocking cards<br>- The codebase seamlessly integrates with database connections to personalize customer responses efficiently.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/examples/pydantic_ai_examples/flight_booking.py'>flight_booking.py</a></b></td>
							<td style='padding: 8px;'>- Guide the conversation flow and validate flight details meticulously to ensure a seamless user experience in finding and purchasing flights<br>- Use agents to extract necessary flight and seat information, intelligently handling scenarios like no available flights or uncertain seat preferences<br>- Contextualize interactions within a robust architecture for efficient delegation and execution of tasks.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/examples/pydantic_ai_examples/chat_app.html'>chat_app.html</a></b></td>
							<td style='padding: 8px;'>- Define the Chat App interface and behavior through an HTML template<br>- Included features are conversation display, user input, and AI response presentation<br>- Also, transpiles client-side TypeScript code for browser execution, ideal for showcasing but not recommended for production environments.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/examples/pydantic_ai_examples/chat_app.py'>chat_app.py</a></b></td>
							<td style='padding: 8px;'>- Gpt-4o, delivering a seamless conversational experience in real-time<br>- The application, while concise, enriches user engagement through practical dialogue functionality.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/examples/pydantic_ai_examples/rag.py'>rag.py</a></b></td>
							<td style='padding: 8px;'>- Demonstrate chat agent augmentation by leveraging vector search via Pydantic AI in the RAG example<br>- Interact with the agent for documentation-based queries to retrieve relevant sections<br>- Utility functions aid in building the search database<br>- Ensure smooth operation by adhering to the provided setup guidelines.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/examples/pydantic_ai_examples/stream_whales.py'>stream_whales.py</a></b></td>
							<td style='padding: 8px;'>- Stream structured responses about whales, validate them, and display in a dynamic table<br>- Uses GPT-4 to obtain details of 5 whale species<br>- Enables streaming of validated data with Rich for real-time visualization<br>- Supports error handling for missing responses<br>- Ideal for interactive data presentation with asynchronous processing.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/examples/pydantic_ai_examples/weather_agent.py'>weather_agent.py</a></b></td>
							<td style='padding: 8px;'>- Demonstrate PydanticAIs weather agent functionality by fetching weather data for multiple cities<br>- Utilizes <code>get_lat_lng</code> and <code>get_weather</code> tools to retrieve latitude, longitude, and weather information<br>- Define APIs keys for geocoding and weather services<br>- Performs call sequences for accurate responses<br>- Achieves precise weather details based on location input<br>- Ideal for enhancing conversational AI weather prediction capabilities.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/examples/pydantic_ai_examples/stream_markdown.py'>stream_markdown.py</a></b></td>
							<td style='padding: 8px;'>- Stream markdown from an agent using the rich library to display it<br>- The code sets up various models to try and their environment variables, then fetches and displays the markdown based on the selected model.Implemented within a modular project structure, this code seamlessly integrates with the larger Pydantic AI ecosystem for streamlined usage.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/examples/pydantic_ai_examples/__main__.py'>__main__.py</a></b></td>
							<td style='padding: 8px;'>- Facilitates easy copying of AI Python examples to a new directory using a straightforward CLI<br>- Enables running examples in place and copying all to a specified destination<br>- Includes options to display version information and useful help text<br>- Integrates well with Pydantic AI framework.</td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<!-- .github Submodule -->
	<details>
		<summary><b>.github</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ .github</b></code>
			<!-- workflows Submodule -->
			<details>
				<summary><b>workflows</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ .github.workflows</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/.github/workflows/stale.yml'>stale.yml</a></b></td>
							<td style='padding: 8px;'>- Automate closure of inactive issues with scheduled checks<br>- Implement issue management to maintain a healthy GitHub repository.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/.github/workflows/coverage.yaml'>coverage.yaml</a></b></td>
							<td style='padding: 8px;'>- Implement a GitHub Actions workflow to run Smokeshow on successful completions of the CI workflow<br>- It installs dependencies, downloads artifacts, uploads coverage reports with specified thresholds, and updates GitHub statuses.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/pydantic/pydantic-ai/blob/master/.github/workflows/ci.yml'>ci.yml</a></b></td>
							<td style='padding: 8px;'>- Detail how the CI workflow ensures code quality and consistency<br>- It orchestrates linting, type checking, and live testing, guaranteeing robust code<br>- The workflow validates changes, promotes quality assurance, and prepares releases<br>- This file stands at the core of maintaining a healthy codebase.</td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---

## ⟠ Getting Started

### ⟁ Prerequisites

This project requires the following dependencies:

- **Programming Language:** Python
- **Package Manager:** Pip, Uv

### ⟒ Installation

Build pydantic-ai from the source and install dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/pydantic/pydantic-ai
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd pydantic-ai
    ```

3. **Install the dependencies:**

<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![pip][pip-shield]][pip-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [pip-shield]: https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white -->
	<!-- [pip-link]: https://pypi.org/project/pip/ -->

	**Using [pip](https://pypi.org/project/pip/):**

	```sh
	❯ pip install -r requirements.txt
	```
<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![uv][uv-shield]][uv-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [uv-shield]: https://img.shields.io/badge/uv-DE5FE9.svg?style=for-the-badge&logo=uv&logoColor=white -->
	<!-- [uv-link]: https://docs.astral.sh/uv/ -->

	**Using [uv](https://docs.astral.sh/uv/):**

	```sh
	❯ uv sync --all-extras --dev
	```


### ⟓ Usage

Run the project with:

**Using [pip](https://pypi.org/project/pip/):**
```sh
python {entrypoint}
```
**Using [uv](https://docs.astral.sh/uv/):**
```sh
uv run python {entrypoint}
```

### ⌆ Testing

Pydantic-ai uses the {__test_framework__} test framework. Run the test suite with:

**Using [pip](https://pypi.org/project/pip/):**
```sh
pytest
```
**Using [uv](https://docs.astral.sh/uv/):**
```sh
uv run pytest tests/
```


---

## ⟲ Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## ⏣ Contributing

- **💬 [Join the Discussions](https://github.com/pydantic/pydantic-ai/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/pydantic/pydantic-ai/issues)**: Submit bugs found or log feature requests for the `pydantic-ai` project.
- **💡 [Submit Pull Requests](https://github.com/pydantic/pydantic-ai/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/pydantic/pydantic-ai
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/pydantic/pydantic-ai/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=pydantic/pydantic-ai">
   </a>
</p>
</details>

---

## ⟶ License

Pydantic-ai is protected under the [LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## ❈ Acknowledgments

- Credit `contributors`, `inspiration`, `references`, etc.

<div align="left"><a href="#top">⬆ Return</a></div>

---

<!-- README-AI COMMAND: -->
<!--
```sh
readmeai \
    --repository 'https://github.com/pydantic/pydantic-ai' \
    --output 'docs/docs/examples/generated/tmp/readme-pydantic-ai.md' \
    --badge-style 'for-the-badge' \
    --badge-color '0077cc' \
    --logo 'PURPLE' \
    --header-style 'COMPACT' \
    --navigation-style 'ROMAN' \
    --emojis 'unicode' \
    --temperature 1.044 \
    --tree-max-depth 1 \
    --api openai
```
-->
