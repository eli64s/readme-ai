# README-AI Execution Flow

## Repository Preprocessing

- User provides a repository URL or local path to command line interface.

- The provided arguments are validated.

- Repository is cloned to a temporary directory.

- File tree structure is generated from the cloned content.
   - Displayed in the output file.
   - Provides context to the language model.

```sh
└── readmeai/
    ├── Dockerfile
    ├── Makefile
    ├── poetry.lock
    ├── pyproject.toml
    ├── readmeai/
    │   ├── cli/
    │   │   ├── commands.py
    │   │   └── options.py
    │   ├── config/
    │   │   ├── __Init__.py
    │   │   └── settings.py
    │   ├── core/
    │   │   ├── factory.py
    │   │   ├── logger.py
    │   │   ├── model.py
    │   │   ├── parser.py
    │   │   ├── preprocess.py
    │   │   └── tokens.py
    │   ├── main.py
    │   ├── markdown/
    │   │   ├── badges.py
    │   │   ├── headers.py
    │   │   ├── quickstart.py
    │   │   ├── tables.py
    │   │   ├── template.py
    │   │   └── tree.py
    │   ├── services/
    │   │   └── version_control.py
    │   ├── settings/
    │   │   ├── config.toml
    │   │   ├── dependency_files.toml
    │   │   ├── identifiers.toml
    │   │   ├── ignore_files.toml
    │   │   ├── language_names.toml
    │   │   └── language_setup.toml
    │   └── utils/
    │       └── utils.py
   ```

- Repo contents and metadata are extracted in the [preprocess.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/core/preprocess.py) script. This script then returns two data structures in [main.py](https://github.com/eli64s/readme-ai/blob/main/readmeai/main.py#L81) used for a variety of purposes downstream. This includes a list of dependencies and a file contents dictionary.

### *Dependencies List*

A list of project dependencies is genereated from scanning each file and its content during preprocessing. The list includes the dependencies and packages fround in the codebase files (e.g. `requirements.txt`, `package.json`, `poetry.lock`, etc.), programming languges used, platforms i.e. Docker, and any other relevant information.

> Dependencies List Example:
```python
dependencies = ['poetry.lock', 'pandas', 'click', 'sh' 'pytest', 'python', 'streamlit', 'numpy']
```

The list is used downstream for a variety of purposes, including generating the badges rendered in the output file, and also injected into prompts to give the LLM additional context of the repository.


### *File Contents Dictionary*

A dictionary of file paths and contents is generated from the repository.

> File Contents Dictionary Example:
```json
{
   "file_path": "my_root_directory/my_subdirectory/my_file.py",
   "file_content_string": "import numpy as np\n\n\ndef my_function():\n    return np.random.rand(1)\n",
}
```

This structure is first used to generate the file summaries at the individual file level. The file summaries are then used to generate three additional README.md sections.

## OpenAI API Model

### *File Summaries*

The program invokes OpenAI API and begins processing the file contents dictionary. First, the code summary prompt is built, injecting the file path and contents into the prompt. Additionally, the prompt is embedded with the directory tree structure to provide context to the LLM about the current file.

> Code Summary Prompt Example:
```toml
summaries = """Offer a comprehensive summary <= 80 words that encapsulates the core functionalities of the code below. Aim for precision and conciseness in your explanation, ensuring a fine balance between detail and brevity.\nDirectory Tree: {0}\nPath: {1}\nCode:\n{2}\n"""
```

After the prompt is created, we check if the prompt exceeds the model's maximum tokenn limit. If true, the prompt is truncated to the maximum and sent to the API.

> The current default max is 4000 tokens for the `gpt-3.5-turbo` engine.

This is not ideal, but from what I've seen, the model is able to generate a decent summary even with a truncated prompt. We are looking at ways to enhance context and accuracy, considering tools like [LangChain](https://python.langchain.com/docs/get_started/introduction) and [LlamaIndex](https://gpt-index.readthedocs.io/en/stable/index.html).

### *Architecture Section*

> I was also wondering how you create the architecture section as that would be very hard without sending all the files at once? Any experience or pointers would be greatly appreciated.

The prompt I use to generate the arcitecture table is located in the project settings file [here](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/config.toml#L31) and is as follows:

```toml
features = """Hello! Analyze the repository {0} and following the instructions below to generate a comprehensive list of features.
Please provide a comprehensive technical analysis of the codebase and its components.
Consider the codebase as a whole and highlight the key characteristics, design patterns, architectural decisions, and any other noteworthy elements.
Generate your response as a Markdown table with the following columns:

|    | Feature            | Description                                                                                                        |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | Analyze the structural design of the system here. Limit your response to a maximum of 200 characters.             |
| 📄 | **Documentation**  | Discuss the quality and comprehensiveness of the documentation here. Limit your response to a maximum of 200 characters.|
| 🔗 | **Dependencies**   | Examine the external libraries or other systems that this system relies on here. Limit your response to a maximum of 200 characters.|
| 🧩 | **Modularity**     | Discuss the system's organization into smaller, interchangeable components here. Limit your response to a maximum of 200 characters.|
| 🧪 | **Testing**        | Evaluate the system's testing strategies and tools here. Limit your response to a maximum of 200 characters.       |
| ⚡️  | **Performance**    | Analyze how well the system performs, considering speed, efficiency, and resource usage here. Limit your response to a maximum of 200 characters.|
| 🔐 | **Security**       | Assess the measures the system uses to protect data and maintain functionality here. Limit your response to a maximum of 200 characters.|
| 🔀 | **Version Control**| Discuss the system's version control strategies and tools here. Limit your response to a maximum of 200 characters.|
| 🔌 | **Integrations**   | Evaluate how the system interacts with other systems and services here. Limit your response to a maximum of 200 characters.|
| 📶 | **Scalability**    | Analyze the system's ability to handle growth here. Limit your response to a maximum of 200 characters.           |

Repository Details:
\nDirectory Tree: {1}\nDependencies: {2}\nCode Summaries: {3}\n
"""
```

The prompt has four `{}` placeholders with data injected as we did previously. This includes the repository URL, directory tree, dependencies list, and the code summaries dictionary generated in the preprocessing step.

The prompt is very specific in its instructions, explicity telling the LLM to generate a Markdown table with the specified columns and giving a 200 character limit for each row of the table.

---
