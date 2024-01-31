The steps below outline the process of generating a README using the CLI.

1. The user provides a GitHub repository URL to the CLI.
2. The input is sanitized and validated.
3. The codebase is cloned into the temporary directory.
4. Each file in the codebase is parsed and metadata is extracted.
5. The metadata is injected into prompt templates and sent to OpenAI's API.
6. The generated content is injected into markdown code blocks and written to the README.


The diagram below shows the high-level architecture of the project.

<div align="left">
    <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/images/how-it-works.png" alt="Architecture" width="350" />
</div>

---
