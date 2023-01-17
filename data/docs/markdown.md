


![](https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg)OpenAI Auto Markdown Docs
=========================




---


### Software and Packeges


[description]


![](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)





---



![](https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg)
Repository Structure
--------------------

<
 ### Modules (src)




processor.py
This Python script contains functions to clone a codebase from a given URL, create a temporary directory, and parse the codebase into a dictionary. The clone\_codebase() function clones the codebase from the given URL and stores it in the temporary directory created by the get\_tmpdir() function. The parse\_codebase() function then reads the contents of each .py file in the codebase and stores it in a dictionary with the file path as the key.




logger.py
This Python script sets up a logger with a ColoredFormatter, which allows for different log levels to be printed in different colors. It also sets the log level to DEBUG.




model.py
This script uses the OpenAI API to generate a summary of a Python script. It takes in a dictionary of files and code as an argument and loops through each file and code. It then creates a prompt for the OpenAI API to generate a summary of the code. The script then stores the summary in a list and returns the list of summaries.




builder.py
This script imports the Pandas library and defines two strings containing HTML code. It then defines a function called create\_html() which reads a CSV file, iterates through the rows, and builds a string containing HTML code. Finally, it returns the HTML string which includes the two strings defined earlier.




main.py
This Python script uses the Hydra library to set up a configuration file for a code-to-language model. It uses the Pandas library to create a dataframe from the codebase, and the Markdownify library to convert the dataframe into HTML and Markdown documents. It then uses the Builder, Logger, and Model libraries to process the codebase, log the progress, and summarize the code. Finally, it writes the HTML and Markdown documents to the specified output directory.




---



### Roadmap


[description]





---

