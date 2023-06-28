#!/bin/bash

# Example repository URLs
repositories=(
    "https://github.com/GokuMohandas/mlops-course"
    "https://github.com/FerrariDG/async-ml-inference"
    "https://github.com/avjinder/Minimal-Todo"
    "https://github.com/olliefr/docker-gs-ping"
    "https://github.com/DownWithUp/CallMon"
    "https://github.com/rumaan/file.io-Android-Client"
    "https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript"
    "https://github.com/idosal/assistant-chat-gpt"
    "https://github.com/eli64s/readme-ai"
    "https://github.com/eli64s/flink-flow"
)

for repo in "${repositories[@]}"
do
    repo_name=$(basename $repo)
    python src/main.py -o "readme-$repo_name.md" -r "$repo"
done
