"""src/md_helper.py"""
import re
from pathlib import Path

base_path = Path.cwd()
main_file_path = f"{base_path}/docs/markdown/readme.md"
new_content_file_path = f"{base_path}/docs/markdown/tables.md"

# The header after which we want to insert the new content
header_to_insert_after = "### Features"

# Read the content of the main file
with open(main_file_path, "r") as main_file:
    main_content = main_file.read()

# Read the content of the new content file
with open(new_content_file_path, "r") as new_content_file:
    new_content = new_content_file.read()

# Split the main content into sections based on headers
sections = re.split(r'(^#+.*$)', main_content, flags=re.MULTILINE)

# Find the index of the header to insert after
header_index = -1
for i in range(len(sections)):
    if sections[i].strip() == header_to_insert_after:
        header_index = i
        break

# If the header was found, insert the new content after it
if header_index >= 0:
    sections[header_index+2:header_index+2] = [new_content]

# Combine the sections into a single Markdown string
markdown_text = "".join(sections)

# Write the updated Markdown content to the main file
with open(main_file_path, "w") as main_file:
    main_file.write(markdown_text)
markdown_text