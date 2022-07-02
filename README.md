# Tweet Translator
This is a simple SPA that uses the Twitter API and DeepL API to search for tweets and translate them in one screen.

![](/tweet-translator.gif)

# Usage

Place a .env file like the one below with your API keys in the root directory of tweet-translator.

```
DEEPL_API_KEY="*** DeepL API Authorization Key ***"
TWITTER_API_KEY="*** Twitter API Key ***"
TWITTER_API_KEY_SECRET="*** Twitter API Key Secret ***"
TWITTER_ACCESS_TOKEN="*** Twitter Access Token ***"
TWITTER_ACCESS_TOKEN_SECRET="*** Twitter Access Token Secret ***"
```

Run the following pipenv command.

```
pipenv install
pipenv run start
```
