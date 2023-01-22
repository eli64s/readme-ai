<img
src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg"
width="80" />

# openai\_automated\_markdowns

------------------------------------------------------------------------

### Software and Packages

\[description\]

![](https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white)
![](https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![](https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white)
![](https://img.shields.io/badge/HTML5-E34F26.svg?style=for-the-badge&logo=HTML5&logoColor=white)
![](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)
![](https://img.shields.io/badge/GitHub-181717.svg?style=for-the-badge&logo=GitHub&logoColor=white)

------------------------------------------------------------------------

### Overview

\[description\]

------------------------------------------------------------------------

### Prerequistes

\[description\]

------------------------------------------------------------------------

<img
src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg"
width="80" />

### Repository Structure

\[description\]

------------------------------------------------------------------------

<img
src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg"
width="80" />

### Modules

### *SRC*

***processor.py***  
This Python script contains functions related to managing a codebase.
The get\_requirements() function uses the pipreqs library to generate a
requirements.txt file for the project. The get\_tmpdir() function
returns a temporary directory path, deleting and recreating it if it
already exists. The clone\_codebase() function clones a git repository
and installs the requirements.txt file. Finally, the parse\_codebase()
function parses a directory of python files and returns a dictionary of

<!-- -->

***logger.py***  
This Python script sets up a logger with a ColoredFormatter, which
allows for different log levels to be printed in different colors. It
also sets the log level to DEBUG.

<!-- -->

***model.py***  
This script uses the OpenAI API to summarize the code in a specified
GitHub repository. It takes in a language model and a dictionary of
files and code, and returns a dictionary of file names and summaries. It
skips the \_\_init\_\_ file and uses the OpenAI Completion API to
generate summaries for each file.

<!-- -->

***builder.py***  
This script is used to create an HTML file from a CSV file. It imports
the Pandas library and a custom utils library. It defines two functions:
get\_pkg\_icons() and create\_html(). The get\_pkg\_icons() function
takes a path to a JSON file and returns a dictionary of icons. The
create\_html() function takes a configuration object, a list of badges,
a name, and a path to a CSV file. It creates a header for the HTML

<!-- -->

***utils.py***  
This Python script contains four functions. The first function,
get\_pkgs\_list(), reads a requirements.txt file and returns a list of
packages. The second function, read\_json(), reads a json file and
returns its contents as a dictionary. The third function, write\_file(),
writes a file to a given path. The fourth function, markdownify(),
converts a string to markdown.

<!-- -->

***main.py***  
This Python script is used to generate a Markdown documentation from a
codebase. It uses the Hydra library to read a configuration file, clones
the codebase from a given URL, parses the codebase, and converts the
code into text. It then creates a Pandas DataFrame with the file names
and summaries, and saves it to a CSV file. It also creates a list of
packages used in the codebase, creates a header with badges, and creates
an HTML file

------------------------------------------------------------------------

### Roadmap

\[description\]

------------------------------------------------------------------------

### Licenses

\[description\]

------------------------------------------------------------------------
