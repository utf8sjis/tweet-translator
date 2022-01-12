from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource

import config
from api import TwitterAPI


class SearchTweets(Resource):
    """
    リクエストのパラメータをもとにTwitterのAPIを叩き、
    取得した情報を整形して返す独自のAPI
    TwitterのAPIは自作のapiパッケージのモジュールから
    TwitterAPIクラスをインポートして使っている
    """
    def post(self):
        input_data = request.json

        twitter_api = TwitterAPI(config.TWITTER_API_KEY, config.TWITTER_API_KEY_SECRET,
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
    'search_tweets', __name__, url_prefix='/api/search')
search_tweets = Api(search_tweets_bp)
search_tweets.add_resource(SearchTweets, '')
