#!/usr/bin/env bash

set -euo pipefail
IFS=$'\n\t'

BASE_DIR="tmp/readmes"
mkdir -p "$BASE_DIR"

api_name="openai"
model_name="gpt-3.5-turbo"

repositories=(
    https://github.com/PiyushSuthar/github-readme-quotes
    https://github.com/pydantic/pydantic-ai
    # https://github.com/emcf/thepipe
    https://github.com/eli64s/readme-ai
    https://github.com/eli64s/readme-ai-streamlit
    https://github.com/jwills/buenavista
    https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript
    https://github.com/rumaan/file.io-Android-Client
    https://github.com/DownWithUp/CallMon
    https://github.com/olliefr/docker-gs-ping
    https://github.com/avjinder/Minimal-Todo
    https://github.com/FerrariDG/async-ml-inference
    # https://github.com/GokuMohandas/mlops-course
    https://gitlab.com/brettops/tools/badgie
    https://bitbucket.org/lusinabrian/tictac-ai
)

badge_styles=(
    flat
    flat-square
    for-the-badge
    plastic
)

logos=(
    ANIMATED
    AURORA
    BLUE
    GREEN
    ICE
    METALLIC
    MIDNIGHT
    ORANGE
    PURPLE
    RAINBOW
)

badge_colors=(
    0077cc # Strong blue
    1e90ff # Dodger blue
    4169e1 # Royal blue
    87ceeb # Sky blue
    663399 # Rebecca purple
    8a2be2 # Blue violet
    9370db # Medium purple
    b19cd9 # Light purple
    ffffff # Pure white
    f8f9fa # Almost white
    e9ecef # Light grey
    dee2e6 # Soft grey
    000080 # Navy
    191970 # Midnight blue
    1a237e # Dark royal blue
    0d47a1 # Deep blue
    2e7d32 # Forest green
    43a047 # Medium green
    66bb6a # Light green
    81c784 # Pale green
)

header_styles=(
    BANNER
    CLASSIC
    COMPACT
    CONSOLE
    MODERN
)

navigation_styles=(
    ACCORDION
    BULLET
    NUMBER
    ROMAN
)

emoji_themes=(
    default
    minimal
    ascension
    harmony
    monochrome
    unicode
    crystal
    earth
    fire
    forest
    nature
    rainbow
    solar
    water
    # fun
    # vintage
    # zen
    cosmic
    quantum
    prism
    atomic
    fibonacci
)

for ((i = 0; i < ${#repositories[@]}; i++)); do
    # Randomly select a repository
    repo_index=$((RANDOM % ${#repositories[@]}))
    repository="${repositories[$repo_index]}"

    # Extract repository name from URL
    if [[ $repository =~ github.com|gitlab.com|bitbucket.org ]]; then
        # Remove .git extension if present
        repo_name=$(echo "$repository" | sed 's/\.git$//')
        # Extract the last part of the path
        repo_name=$(basename "$repo_name")
        # Clean up any remaining special characters
        repo_name=$(echo "$repo_name" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9-]/-/g')
    else
        # Fallback for unknown repository types
        repo_name="readme-$(date +%s)"
    fi

    # Randomly select styles and themes
    random_badge="${badge_styles[$((RANDOM % ${#badge_styles[@]}))]}"
    random_logo="${logos[$((RANDOM % ${#logos[@]}))]}"
    random_badge_color="${badge_colors[$((RANDOM % ${#badge_colors[@]}))]}"
    random_header="${header_styles[$((RANDOM % ${#header_styles[@]}))]}"
    random_nav="${navigation_styles[$((RANDOM % ${#navigation_styles[@]}))]}"
    random_emoji="${emoji_themes[$((RANDOM % ${#emoji_themes[@]}))]}"

    # Generate random parameters for temperature and maximum tree depth
    temperature=$(awk -v min=0.1 -v max=1.1 'BEGIN{srand(); printf "%.3f", min+rand()*(max-min)}')
    tree_max_depth=$((RANDOM % 5 + 1))

    filename="$BASE_DIR/readme-$repo_name.md"

    # Construct single-line command using the 'readmeai' CLI
    cmd="readmeai"
    cmd+=" --repository '$repository'"
    cmd+=" --output '$filename'"
    cmd+=" --badge-style '$random_badge'"
    cmd+=" --badge-color '$random_badge_color'"
    cmd+=" --logo '$random_logo'"
    cmd+=" --header-style '$random_header'"
    cmd+=" --navigation-style '$random_nav'"
    cmd+=" --emojis '$random_emoji'"
    cmd+=" --temperature $temperature"
    cmd+=" --tree-max-depth $tree_max_depth"
    cmd+=" --api $api_name"
    cmd+=" --model $model_name"

    # Logging
    echo "----------------------------------------"
    echo "Generating README $((i + 1))/${#repositories[@]}: $filename"
    echo "Repository: $repository"
    echo "Badge Style: $random_badge"
    echo "Logo: $random_logo"
    echo "Temperature: $temperature"
    echo "Tree Depth: $tree_max_depth"
    echo "Command: $cmd"
    echo "----------------------------------------"

    # Execute command
    if eval "$cmd"; then
        echo "README generated successfully."
    else
        echo "Error generating README for $repository" >&2
        continue
    fi

    # Append formatted multi-line command to the README to reference in docs.
    {
        echo ""
        echo "<!-- README-AI COMMAND: -->"
        echo "<!--"
        echo '```sh'
        cat << EOF
readmeai \\
    --repository '$repository' \\
    --badge-style '$random_badge' \\
    --badge-color '$random_badge_color' \\
    --logo '$random_logo' \\
    --header-style '$random_header' \\
    --navigation-style '$random_nav' \\
    --emojis '$random_emoji' \\
    --temperature $temperature \\
    --tree-max-depth $tree_max_depth \\
    --api $api_name \\
    --model $model_name
EOF
        echo '```'
        echo "-->"
    } >> "$filename"

    sleep 2

generate_summary() {
    echo "----------------------------------------"
    TOTAL_READMES=$(ls -1q "$BASE_DIR" | wc -l)
    echo "Total READMEs generated: $TOTAL_READMES"
    for file in "$BASE_DIR"/*; do
        echo "Generated README: $file"
        echo "Last updated: $(stat -f "%Sm" -t "%Y-%m-%d %H:%M:%S" "$file")"
    done
    echo "----------------------------------------"
}

generate_summary

done
