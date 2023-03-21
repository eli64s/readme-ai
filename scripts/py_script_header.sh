#!/bin/bash

GH_USERNAME=$(git config user.name) 

# Function to remove all strings and comments before the first line of code or import statements
function remove_header {
  # Get the line number of the first line of code or import statements
  FIRST_LINE=$(grep -m 1 -n -v -e "^$\|^[[:space:]]*\#\|^[\t ]*\"" "$1" | cut -d ':' -f 1)

  # Remove all lines before the first line of code or import statements
  sed -i '' -e "1,$((FIRST_LINE - 1))d" "$1"
}

# Check if the folder path is provided
if [ -z "$1" ]; then
  echo "Error: Please provide a folder path."
  exit 1
fi

FOLDER_PATH="$1"
SCRIPT_NAME=$(basename "$0")

# Change to the specified directory
cd "$FOLDER_PATH" || { echo "Error: Failed to change to directory $FOLDER_PATH"; exit 2; }

# Iterate through all the .py files in the folder
shopt -s nullglob
for file in *.py; do
  # Remove header from the file
  remove_header "$file"

  # Create a temporary file
  TEMP_FILE=$(mktemp)

  # Add the new header to the temporary file
  {
    echo "#!/usr/bin/env python3"
    echo
    echo '"""'
    echo "Script: $file"
    echo
    echo "Updated: $(date +'%Y-%m-%d %T')"
    echo "Author: $GH_USERNAME"
    echo '"""'
    echo
  } > "$TEMP_FILE"

  # Append the file content to the temporary file
  cat "$file" >> "$TEMP_FILE"

  # Replace the original file with the temporary file
  mv "$TEMP_FILE" "$file"
done
