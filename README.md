# Tweet Translator
This is a simple SPA that uses the Twitter API and DeepL API to search for tweets and translate them in one screen.

![](/tweet-translator.gif)

It is implemented on the assumption that it will be deployed to Heroku.

# Usage

Place a file (config.py) like the one below with the API key in the backend directory.

```python
DEEPL_API_KEY = '*** DeepL API Authorization Key ***'
TWITTER_API_KEY = '*** Twitter API Key ***'
TWITTER_API_KEY_SECRET = '*** Twitter API Key Secret ***'
TWITTER_ACCESS_TOKEN = '*** Twitter Access Token ***'
TWITTER_ACCESS_TOKEN_SECRET = '*** Twitter Access Token Secret ***'
```

```
├─ backend
│    └─ config.py
```

To try it in local, run the following pipenv command.

```
pipenv install
pipenv run start
```
