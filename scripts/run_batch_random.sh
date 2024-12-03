#!/usr/bin/env bash

#version="0.5.0"
#run_date=$(date +"%Y%m%d")
filenames=(
    #"readme-litellm"
    #"readme-fal-js"
    gitlab
    bitbucket
    "readme-local"
    "readme-python"
    "readme-streamlit"
    "readme-postgres"
    "readme-typescript"
    "readme-kotlin"
    "readme-rust-c"
    "readme-go"
    "readme-java"
    "readme-fastapi-redis"
    "readme-mlops"
    "readme-gemini"
    "readme-offline"
)
repositories=(
    #"https://github.com/BerriAI/litellm"
    #"https://github.com/fal-ai/fal-js"
    https://gitlab.com/rohanrk/gitmate-2
    https://bitbucket.org/jwalton/opup
    "/Users/k01101011/Documents/GitHub/pyflink-poc"
    "https://github.com/eli64s/readme-ai"
    "https://github.com/eli64s/readme-ai-streamlit"
    "https://github.com/jwills/buenavista"
    "https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript"
    "https://github.com/rumaan/file.io-Android-Client"
    "https://github.com/DownWithUp/CallMon"
    "https://github.com/olliefr/docker-gs-ping"
    "https://github.com/avjinder/Minimal-Todo"
    "https://github.com/FerrariDG/async-ml-inference"
    "https://github.com/GokuMohandas/mlops-course"
    "https://github.com/eli64s/readme-ai"
    "https://github.com/eli64s/readme-ai-streamlit"
)
badge_styles=("flat" "flat-square" "plastic" "for-the-badge" "skills-light") # "skills" "skills-light")
image=("llm")
badge_color=("blue" "green" "cyan" "yellow" "orange" "violet" "purple" "blueviolet" "white" "black" "brightgreen" "ff69b4" "999999")
hs=("modern" "classic" "compact")
ts=("bullet" "number" "roman" "links" "fold")
e=("default" "oss" ""minimal" "nature" "fun" "space)

for index in "${!repositories[@]}"; do
    repo="${repositories[$index]}"
    filename="${filenames[$index]}.md" #_v${version}_${run_date}.md"
    random_badge=${badge_styles[$RANDOM % ${#badge_styles[@]}]}
    random_badge_color=${badge_color[$RANDOM % ${#badge_color[@]}]}
    image_style=${image[$RANDOM % ${#image[@]}]}
    header=${hs[$RANDOM % ${#hs[@]}]}
    toc=${ts[$RANDOM % ${#ts[@]}]}
    emoji=${e[$RANDOM % ${#e[@]}]}

    # cmd="python3 -m readmeai.cli.main --tree-depth 2 -o \"$filename\" -r \"$repo\""
    # cmd="pipx run readmeai -o \"$filename\" -r \"$repo\""
    cmd="poetry run readmeai --api openai --tree-depth 1 -o "$filename" -r "$repo""

    if [ "$random_badge" != "default" ]; then
        cmd+=" --badge-style \"$random_badge\""
    fi
    if [ "$image_style" != "blue" ]; then
        cmd+=" -i \"$image_style\""
    fi
    if [ "$emoji" != "default" ]; then
        cmd+=" --emojis \"$emoji\""
    fi
    if [ "hs" != "classic" ]; then
        cmd+=" --header-style \"$header\""
    fi
    if [ "ts" != "bullet" ]; then
        cmd+=" --toc-style \"$toc\""
    fi

    if [ "$random_badge_color" != "blue" ]; then
        cmd+=" --badge-color \"$random_badge_color\""
    fi

    eval $cmd

done
