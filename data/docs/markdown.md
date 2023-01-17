
![](https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg)

OpenAI Auto Markdown Docs
=========================
  
![](https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg)

Repository
----------
  
 ![](https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg)Modules (src)
-------------#### \_tmp/config\_template.pyThis script imports the pymongo library and creates variables for user credentials for the Twitter API and a client for a local MongoDB database. It also provides instructions for the user to paste their own Twitter credentials into the empty strings and save the file as config.py.

#### \_tmp/load\_database.pyThis Python script imports the TwitterStreamer class from the twitter\_streamer.py script and creates a MongoDB database called twitter\_data. It then defines a LoadDatabase class which has a load\_tweets method that is used as a callback function for each incoming tweet. This method appends each tweet to an empty list (the "buffer") and when the buffer is full (i.e. has reached the batch size), the tweets are dumped into the MongoDB database. The

#### \_tmp/twitter\_streamer.pyThis Python script uses the tweepy library to intercept real-time, streamed tweets. It authenticates the API keys and tokens using OAuthHandler, creates a custom StreamListener class to parse each tweet as it is intercepted, and uses the Stream class to filter incoming tweets by keywords and language. After each relevant tweet is intercepted and parsed, it is printed in the terminal. The keyword can be altered at the end of the script
