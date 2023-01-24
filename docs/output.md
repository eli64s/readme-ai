<img
src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg"
width="100" />

ChatGPT Automated Markdown Docs

### https://github.com/eli64s/openai\_automated\_markdowns

![](https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white)
![](https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![](https://img.shields.io/badge/Pytest-0A9EDC.svg?style=for-the-badge&logo=Pytest&logoColor=white)
![](https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white)
![](https://img.shields.io/badge/HTML5-E34F26.svg?style=for-the-badge&logo=HTML5&logoColor=white)
![](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)
![](https://img.shields.io/badge/GitHub-181717.svg?style=for-the-badge&logo=GitHub&logoColor=white)

## Prerequisites

------------------------------------------------------------------------

## Usage

    # 1. Clone GitHub repository.
    git clone https://github.com/eli64s/openai_automated_markdowns && cd openai_automated_markdowns

    # 2. Setup conda virtual environment.
    make conda

    # 3. Run the model.
    bash scripts/run_model.sh

    None

### *SRC*

***processor.py***  
This script contains functions for cloning a git repository, getting
file extensions, creating a temporary directory, and parsing a directory
of python files. The clone\_codebase() function takes a URL as an
argument and clones the repository to a temporary directory, then
installs the requirements.txt file. The get\_file\_extensions() function
walks through the current working directory and returns a list of file
extensions. The get\_tmpdir() function creates a temporary directory if
it does not already exist, and

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
returns the contents as a dictionary. The third function, write\_file(),
writes a file to a given path. The fourth function, md(), converts HTML
to Markdown.

<!-- -->

***main.py***  
This Python script sets up a logger, clones a codebase from a given URL,
parses the codebase, creates a summary of the code, creates a list of
packages used, creates HTML and Markdown documentation, and writes the
documentation to the specified files.

------------------------------------------------------------------------

### Roadmap

\[description\]

------------------------------------------------------------------------

### Licenses

\[description\]
