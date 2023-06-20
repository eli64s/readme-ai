#!/bin/bash

# Example repository URLs
repositories=(
    "https://github.com/iusztinpaul/energy-forecasting"
    "https://github.com/ajndkr/lanarky"
    "https://github.com/GokuMohandas/mlops-course"
    "https://github.com/FerrariDG/async-ml-inference"
    "https://github.com/avjinder/Minimal-Todo"
    "https://github.com/olliefr/docker-gs-ping"
    "https://github.com/DownWithUp/CallMon"
    "https://github.com/rumaan/file.io-Android-Client"
)

for repo in "${repositories[@]}"
do
    repo_name=$(basename $repo)
    python src/main.py -o "readme-$repo_name.md" -r "$repo"
done
