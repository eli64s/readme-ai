#!/usr/bin/env bash

version="0.4.992"
run_date=$(date +"%Y%m%d")
filenames=(
    #"readme-litellm"
    #"readme-fal-js"
    "readme-postgres"
    "readme-python"
    "readme-typescript"
    "readme-kotlin"
    "readme-rust-c"
    "readme-go"
    "readme-java"
    "readme-fastapi-redis"
    "readme-mlops"
    "readme-pyflink"
    "readme-streamlit"
)
repositories=(
    #"https://github.com/BerriAI/litellm"
    #"https://github.com/fal-ai/fal-js"
    "https://github.com/jwills/buenavista"
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
align=("left" "center")
badge_styles=("default" "flat" "flat-square" "plastic" "for-the-badge" "skills" "skills-light")
image=("default" "black" "cloud" "gradient" "grey" "purple" "yellow")

for index in "${!repositories[@]}"; do
    repo="${repositories[$index]}"
    filename="${filenames[$index]}_v${version}_${run_date}.md"
    random_badge=${badge_styles[$RANDOM % ${#badge_styles[@]}]}
    image_style=${image[$RANDOM % ${#image[@]}]}
    alignment=${align[$RANDOM % ${#align[@]}]}
    rand_choice=$((RANDOM % 2))

    cmd="python3 -m readmeai.cli.commands -o \"$filename\" -r \"$repo\""

    if [ "$random_badge" != "default" ]; then
        cmd+=" -b \"$random_badge\""
    fi
    if [ "$image_style" != "default" ]; then
        cmd+=" -i \"$image_style\""
    fi
    if [ "$alignment" != "center" ]; then # Assuming 'center' is the default alignment
        cmd+=" -a \"$alignment\""
    fi
    if [ $rand_choice -eq 1 ]; then
        cmd+=" -e"
    fi

    eval $cmd
done
