#!/usr/bin/env bash

repositories=(
    "https://github.com/BerriAI/litellm"
    "https://github.com/eli64s/readme-ai"
    "https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript"
    "https://github.com/rumaan/file.io-Android-Client"
    "https://github.com/DownWithUp/CallMon"
    "https://github.com/olliefr/docker-gs-ping"
    "https://github.com/avjinder/Minimal-Todo"
    "https://github.com/FerrariDG/async-ml-inference"
    "https://github.com/GokuMohandas/mlops-course"
    "https://github.com/eli64s/pyflink-poc"
    "https://github.com/eli64s/readme-ai-streamlit"
)

filenames=(
    "readme-litellm.md"
    "readme-python.md"
    "readme-typescript.md"
    "readme-kotlin.md"
    "readme-rust-c.md"
    "readme-go.md"
    "readme-java.md"
    "readme-fastapi-redis.md"
    "readme-mlops.md"
    "readme-pyflink.md"
    "readme-streamlit.md"
)

badge_styles=("flat" "flat-square" "plastic" "for-the-badge" "skills" "skills-light")
image=("black" "blue" "grey" "purple" "white" "yellow")
align=("left" "center")

for index in "${!repositories[@]}"
do
    repo="${repositories[$index]}"
    filename="${filenames[$index]}"
    random_badge=${badge_styles[$RANDOM % ${#badge_styles[@]}]}
    image_style=${image[$RANDOM % ${#image[@]}]}
    alignment=${align[$RANDOM % ${#align[@]}]}
    rand_choice=$((RANDOM % 2))
    if [ $rand_choice -eq 1 ]; then
        python3 -m readmeai.cli.commands -o "$filename" -r "$repo" -b "$random_badge" -i "$image_style" -a "$alignment" -e
    else
        python3 -m readmeai.cli.commands -o "$filename" -r "$repo" -b "$random_badge" -i "$image_style" -a "$alignment"
    fi
done
