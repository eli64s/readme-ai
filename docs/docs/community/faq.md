# Frequently Asked Questions

## General Questions

### Q: What is README-AI?
A: README-AI is a tool that automatically generates comprehensive README files for your projects using artificial intelligence.

### Q: Which AI models does README-AI support?
A: README-AI primarily uses OpenAI's GPT models, but there are ongoing efforts to add support for other models like Claude, Azure OpenAI, Cohere, and Llama2 (via Replicate).

## Installation and Setup

### Q: How do I install README-AI?
A: You can install README-AI using pip:
```
pip install readmeai
```
Alternatively, you can use Docker:
```
docker run -it -e OPENAI_API_KEY=your_key_here -v "$(pwd)":/app zeroxeli/readme-ai:latest
```

### Q: I'm getting an error when trying to install on Ubuntu. How can I fix it?
A: If you're encountering issues with conda environment creation, try using a virtual environment with pip instead. Ensure you have Python 3.8 or higher installed.

## Usage

### Q: How do I generate a README for my project?
A: Use the following command:
```
readmeai -o readme-ai.md -r https://github.com/your-username/your-repo
```
Replace the URL with your repository link.

### Q: Can I use README-AI with private repositories?
A: Yes, but you may need to provide authentication. For Bitbucket, use the format:
```
https://username:bitbucket_apikey@bitbucket.org/username/repo
```

### Q: Does README-AI work with GitLab repositories?
A: Yes, README-AI supports GitLab repositories. Use the same command format as with GitHub repos.

## Troubleshooting

### Q: I'm getting a "404 Not Found" error. What should I do?
A: Ensure your OpenAI API key is correct and has sufficient permissions. Also, check if you're using the correct API endpoint.

### Q: The script runs but doesn't generate a file. Why?
A: Check the permissions in your current directory. Ensure README-AI has write access to create the output file.

### Q: I'm seeing a "429 Too Many Requests" error. How can I resolve this?
A: This error occurs when you've exceeded the rate limit for the OpenAI API. Wait a while before trying again, or consider upgrading your API plan.

### Q: Why am I getting a "NotFound object is not iterable" error?
A: This error may occur if you're using an incompatible model. Ensure you're using a supported model like "gpt-3.5-turbo" or "gpt-4".

## Features and Customization

### Q: Can I use README-AI with languages other than English?
A: While README-AI primarily generates content in English, there are ongoing efforts to add internationalization (i18n) support for languages like Spanish and Italian.

### Q: Is it possible to use README-AI in Azure DevOps?
A: While there isn't native integration, you could potentially use README-AI as part of your Azure DevOps pipeline by incorporating it into your build or release process.

### Q: Can I customize the OpenAI endpoint or model used?
A: There are ongoing efforts to make the configuration more extensible, including options to specify different endpoints (like Azure OpenAI) and models.

## Contributing

### Q: How can I contribute to README-AI?
A: You can contribute by submitting pull requests on GitHub. Areas of contribution include adding support for new AI models, improving documentation, adding tests, and fixing bugs.

If you have any other questions or issues, please check the [GitHub repository](https://github.com/eli64s/readme-ai) or open a new issue for support.


<!--
**OpenAI API Key**

An OpenAI API account and API key are needed to use readme-ai. Get started by creating an account [here](https://platform.openai.com/docs/quickstart/account-setup). Once you have an account, you can create an API key on the [API settings page](https://platform.openai.com/api-keys).

> [!WARNING]
>
> Before using readme-ai, its essential to understand the potential risks and costs associated with using AI-powered tools.
>
> * **Review Sensitive Information**: Ensure all content in your repository is free of sensitive information before running the tool. This project does not remove sensitive data from your codebase, nor from the output README file.
>
> * **API Usage Costs**: The OpenAI API is not free and costs can accumulate quickly! You will be charged for each request made by readme-ai. Be sure to monitor API usage costs using the [OpenAI API Usage Dashboard](https://platform.openai.com/account/usage).
-->
