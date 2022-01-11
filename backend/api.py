from flask import Blueprint, jsonify, request, session
from flask_restful import Api, Resource
import json

import config
from twitterAPI import twitterAPI
from deeplAPI import deeplAPI


# ツイッター
class SearchTweets(Resource):
    def post(self):
        input_data = request.json

        twitter_api = twitterAPI(config.TWITTER_API_KEY, config.TWITTER_API_KEY_SECRET,
                config.TWITTER_ACCESS_TOKEN, config.TWITTER_ACCESS_TOKEN_SECRET)
        tweet_list = twitter_api.search(
            input_data['searchWord'],
            input_data['searchLang'])
        result_data = [{
            'tweetId': tweet['tweet_id'],
            'userName': tweet['user_name'],
            'userScreenName': tweet['user_screen_name'],
            'tweetText': tweet['tweet_text'],
            'userProfileImageUrl': tweet['user_profile_image_url'],
        } for tweet in tweet_list]

        return jsonify(result_data)

search_tweets_bp = Blueprint(
    'search_tweets', __name__, url_prefix='/api/twitter/search')
search_tweets = Api(search_tweets_bp)
search_tweets.add_resource(SearchTweets, '')


# DeepL
class DeeplTranslate(Resource):
    def post(self):
        input_data = request.json
        
        deepl_api = deeplAPI(config.DEEPL_API_KEY)
        
        translated_text = deepl_api.translate(
            input_data['tweetText'],
            input_data['translateLang'])

        result_data = {
            'text': translated_text
        }

        return jsonify(result_data)

deepl_translate_bp = Blueprint(
    'deepl_translate', __name__, url_prefix='/api/deepl/translate')
deepl_translate = Api(deepl_translate_bp)
deepl_translate.add_resource(DeeplTranslate, '')
