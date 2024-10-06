#!/usr/bin/env bash

BASE_DIR=.
mkdir -p $BASE_DIR

https://github.com/emcf/thepipe
poetry run readmeai \
    --repository https://github.com/emcf/thepipe \
    --output $BASE_DIR/readme-chunking.md \
    --api openai \
    --badge-color FFA500 \
    --badge-style flat-square \
    --context-window 3999 \
    --header-style classic \
    --image llm


poetry run readmeai \
    --repository https://github.com/jwills/buenavista \
    --output $BASE_DIR/readme-postgres-gemini.md \
    --api gemini \
    --model gemini-1.5-pro \
    --badge-style flat-square \
    --badge-color yellow \
    --context-window 3999 \
    --header-style compact \
    --image custom -e \

# "https://raw.githubusercontent.com/wuchong/awesome-flink/master/flink_squirrel.png"
poetry run readmeai \
    --repository /Users/k01101011/Documents/GitHub/pyflink-poc \
    --output $BASE_DIR/readme-local.md \
    --api openai \
    --model gpt-3.5-turbo \
    --badge-style plastic \
    --context-window 3999 \
    --header-style classic \
    --image purple \
    --rate-limit 25 \
    --temperature 0.5 \
    --toc-style bullets \
    --tree-depth 2 \
    --emojis

poetry run readmeai \
    --repository https://github.com/eli64s/readme-ai \
    --output $BASE_DIR/readme-python.md \
    --api openai \
    --model gpt-3.5-turbo \
    --badge-color 526CFE \
    --badge-style flat \
    --context-window 3999 \
    --header-style compact \
    --image cloud \
    --rate-limit 25 \
    --temperature 0.5 \
    --toc-style fold \
    --tree-depth 1 \
    --align left \
    --emojis

# "https://www.svgrepo.com/show/395851/balloon.svg"
poetry run readmeai \
    --repository https://github.com/eli64s/readme-ai-streamlit \
    --output $BASE_DIR/readme-streamlit.md \
    --api openai \
    --model gpt-3.5-turbo \
    --badge-color FF4B4B \
    --badge-style flat-square \
    --context-window 3999 \
    --header-style classic \
    --image cloud \
    --rate-limit 25 \
    --temperature 0.5 \
    --toc-style bullet \
    --tree-depth 3 \

poetry run readmeai \
    --repository https://github.com/olliefr/docker-gs-ping \
    --output $BASE_DIR/readme-go.md \
    --api openai \
    --model gpt-3.5-turbo \
    --badge-color 00ADD8 \
    --badge-style for-the-badge \
    --context-window 3999 \
    --header-style modern \
    --image blue \
    --rate-limit 25 \
    --temperature 0.5 \
    --toc-style roman \
    --tree-depth 3 \
    --emojis

poetry run readmeai \
    --repository https://github.com/FerrariDG/async-ml-inference \
    --output $BASE_DIR/readme-fastapi-redis.md \
    --api openai \
    --model gpt-3.5-turbo \
    --badge-color 009688 \
    --badge-style flat-square \
    --context-window 3999 \
    --header-style classic \
    --image grey \
    --rate-limit 25 \
    --temperature 0.5 \
    --toc-style number \
    --tree-depth 2 \

# "https://miro.medium.com/v2/resize:fit:798/1*T-Wu9qBEXTpm9gXq2shQpg.png"
poetry run readmeai \
    --repository https://github.com/rumaan/file.io-Android-Client \
    --output $BASE_DIR/readme-kotlin.md \
    --api openai \
    --model gpt-3.5-turbo \
    --badge-color 009688 \
    --badge-style flat \
    --context-window 3999 \
    --header-style classic \
    --image black \
    --rate-limit 25 \
    --temperature 0.5 \
    --toc-style links \
    --tree-depth 2 \
    --emojis

poetry run readmeai \
    --repository https://github.com/PiyushSuthar/github-readme-quotes \
    --output $BASE_DIR/readme-vercel.md \
    --api openai \
    --model gpt-3.5-turbo \
    --badge-color 00ffe9 \
    --badge-style flat-square \
    --context-window 3999 \
    --header-style classic \
    --image llm \
    --rate-limit 19 \
    --temperature 0.7 \
    --toc-style roman \
    --tree-depth 3 \
    --emojis
