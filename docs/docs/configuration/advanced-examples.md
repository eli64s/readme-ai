# Advanced Configurations (WIP)

The following examples demonstrate advanced configurations and options for generating READMEs with readme-ai.

## Generate README with Custom OpenAI API Parameters

```sh
readmeai --repository /path/to/project \
        --api openai \
        --model gpt-4-turbo
        --context-window 9999
        --temperature 0.1
        --rate-limit 20
```
