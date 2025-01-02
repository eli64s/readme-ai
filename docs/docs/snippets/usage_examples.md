<!-- --8<------ [start:basic] -->
```bash
# Generate a README with default settings
readmeai --repository https://github.com/username/project

# Generate with custom output location
readmeai --repository ./my-project --output custom_readme.md

# Use a specific LLM provider
readmeai --api openai --model gpt-4 --repository ./my-project
```
<!-- --8<------ [end:basic] -->

<!-- --8<------ [start:advanced] -->
```bash
# Customize appearance
readmeai --repository ./my-project \
    --badge-style flat-square \
    --badge-color blue \
    --header-style modern \
    --navigation-style roman \
    --emojis minimal

# Fine-tune LLM parameters
readmeai --repository ./my-project \
    --api openai \
    --model gpt-4 \
    --temperature 0.7 \
    --top-p 0.9 \
    --context-window 8192
```
<!-- --8<------ [end:advanced] -->

<!-- --8<------ [start:docker] -->
```bash
# Run with Docker
docker run -it --rm \
    -e OPENAI_API_KEY=$OPENAI_API_KEY \
    -v "$(pwd)":/app \
    zeroxeli/readme-ai:latest \
    --repository https://github.com/username/project
```
<!-- --8<------ [end:docker] -->
