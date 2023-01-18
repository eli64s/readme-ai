



![](https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg)
OpenAI Auto Markdown Docs
=========================




---


### Software and Packeges


[description]



![](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)



![](https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white)
![](https://img.shields.io/badge/CondaForge-000000.svg?style=for-the-badge&logo=Conda-Forge&logoColor=white)
![](https://img.shields.io/badge/prettier-1A2C34?style=for-the-badge&logo=prettier&logoColor=F7BA3E)
![](https://img.shields.io/badge/GitHub-181717.svg?style=for-the-badge&logo=GitHub&logoColor=white)
![](https://img.shields.io/badge/Shields.io-000000.svg?style=for-the-badge&logo=shieldsdotio&logoColor=white)






---



### Overview


[description]




---


### Prerequistes


[description]





---



![](https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg)
### Repository Structure


[description]





---



![](https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg)
### Modules [src]



***processor.py***
This Python script contains functions to clone a codebase from a given URL, create a temporary directory, and parse the codebase into a dictionary. The clone\_codebase() function clones the codebase from the given URL into the temporary directory created by the get\_tmpdir() function. The parse\_codebase() function then reads all the Python files in the codebase and stores them in a dictionary with the file path as the key and the file contents as the value.


***logger.py***
This Python script sets up a logger with a ColoredFormatter, which allows for different log levels to be printed in different colors. It also sets the log level to DEBUG, which will print all log messages.


***model.py***
This script uses the OpenAI API to generate a summary of a Python script. It takes in a dictionary of files and code as an argument and loops through each file and code. It then creates a prompt for the OpenAI API to generate a summary of the code. The script then stores the summary in a list and returns the list of summaries.


***builder.py***
This script creates an HTML page with information about OpenAI Auto Markdown Docs. It imports the Pandas library and reads a CSV file containing the names of scripts and their descriptions. It then creates an HTML page with a header, a section for software and packages, a section for the repository structure, and a section for the roadmap. It also includes images and badges for the software and packages.


***main.py***
This Python script uses the hydra library to set up a configuration file, then uses the pathlib library to create a directory for the output. It uses the markdownify library to convert HTML documents to markdown documents. It then uses the builder, logger, model, and processor modules to clone a codebase from a given URL, parse the codebase, convert the code to text, and create HTML and markdown documents. Finally, it logs a message that the code-to-language




---



### Roadmap


[description]





---



### Licenses


[description]





---




