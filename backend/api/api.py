import tweepy
from datetime import datetime, timezone
import pytz
import deepl


def get_keys():
    """
    APIキー等を取得する関数。tryは開発環境、exceptはHeroku上で実行される想定
    Herokuには別に環境変数を設定しておく必要がある
    """
    try:
        import config
        return {
            'DEEPL_API_KEY': config.DEEPL_API_KEY,
            'TWITTER_API_KEY': config.TWITTER_API_KEY,
            'TWITTER_API_KEY_SECRET': config.TWITTER_API_KEY_SECRET,
            'TWITTER_ACCESS_TOKEN': config.TWITTER_ACCESS_TOKEN,
            'TWITTER_ACCESS_TOKEN_SECRET': config.TWITTER_ACCESS_TOKEN_SECRET,
        }
    except ImportError:
        import os
        return {
            'DEEPL_API_KEY': os.environ['DEEPL_API_KEY'],
            'TWITTER_API_KEY': os.environ['TWITTER_API_KEY'],
            'TWITTER_API_KEY_SECRET': os.environ['TWITTER_API_KEY_SECRET'],
            'TWITTER_ACCESS_TOKEN': os.environ['TWITTER_ACCESS_TOKEN'],
            'TWITTER_ACCESS_TOKEN_SECRET': os.environ['TWITTER_ACCESS_TOKEN_SECRET'],
        }


class TwitterAPI():
    """
    TwitterのAPIを使って処理を行うメソッドをまとめたクラス
    コンストラクタの引数でAPIのキー等を受け取り認証を行う
    """
    def __init__(self, api_key, api_key_secret, access_token, access_token_secret):
        auth = tweepy.OAuthHandler(api_key, api_key_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth, wait_on_rate_limit=True)

    # UTCをJSTに変換する
    def _utc_to_jst(self, u_time):
        utc_time = datetime(u_time.year, u_time.month, u_time.day, u_time.hour,
                            u_time.minute, u_time.second, tzinfo=timezone.utc)
        jst_time = utc_time.astimezone(pytz.timezone('Asia/Tokyo'))
        str_time = jst_time.strftime('%Y-%m-%d-%H:%M:%S')
        return str_time

    # 検索ワード、言語、取得数を受け取って検索し、結果のデータを返す
    # 取得数はデフォルトで10ツイート
    def search(self, search_text, lang, get_number=10):
        result = tweepy.Cursor(
            self.api.search_tweets,
            q=search_text + ' -filter:retweets -filter:replies',
            lang=lang, tweet_mode='extended').items(get_number)

        tweet_list = []
        for tweet in result:
            tweet_list.append({
                'tweet_id': tweet.id,
                'tweet_created_at': self._utc_to_jst(tweet.created_at),
                'tweet_text': tweet.full_text,
                'tweet_favorite_count': tweet.favorite_count,
                'tweet_retweet_count': tweet.retweet_count,
                'user_id': tweet.user.id,
                'user_created_at': self._utc_to_jst(tweet.user.created_at),
                'user_name': tweet.user.name,
                'user_screen_name': tweet.user.screen_name,  # アカウント名
                'user_description': tweet.user.description,
                'user_friends_count': tweet.user.friends_count,  # フォロー数
                'user_followers_count': tweet.user.followers_count,
                'user_profile_image_url': tweet.user.profile_image_url,
                'user_profile_background_image_url': tweet.user.profile_background_image_url,
                'user_url': tweet.user.url,  # プロフィール記載のウェブサイト
            })

        return tweet_list


class DeeplAPI():
    """
    DeepLのAPIを使って処理を行うメソッドをまとめたクラス
    コンストラクタの引数でAPIのキーを受け取り認証を行う
    """
    def __init__(self, api_key):
        self.translator = deepl.Translator(api_key)

    # テキストと目的言語を受け取って翻訳し、訳文を返す
    def translate(self, source_text, target_lang):
        result = self.translator.translate_text(source_text, target_lang=target_lang) 
        translated_text = result.text

        return translated_text
