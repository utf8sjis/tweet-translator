import tweepy
from datetime import datetime, timezone
import pytz


class twitterAPI():
    def __init__(self, api_key, api_key_secret, access_token, access_token_secret):
        auth = tweepy.OAuthHandler(api_key, api_key_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth, wait_on_rate_limit=True)

    def _utc_to_jst(self, u_time):
        utc_time = datetime(u_time.year, u_time.month, u_time.day, u_time.hour,
                            u_time.minute, u_time.second, tzinfo=timezone.utc)
        jst_time = utc_time.astimezone(pytz.timezone('Asia/Tokyo'))
        str_time = jst_time.strftime('%Y-%m-%d-%H:%M:%S')
        return str_time

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
                'user_screen_name': tweet.user.screen_name,
                'user_description': tweet.user.description,
                'user_friends_count': tweet.user.friends_count,  # フォロー数
                'user_followers_count': tweet.user.followers_count,
                'user_profile_image_url': tweet.user.profile_image_url,
                'user_profile_background_image_url': tweet.user.profile_background_image_url,
                'user_url': tweet.user.url,  # アカウントのプロフィールのウェブサイト
            })

        return tweet_list
