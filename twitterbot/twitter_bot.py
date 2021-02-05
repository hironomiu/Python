import tweepy
import configparser

message = "Tweetを入力してください！"


def get_authentication():
    config_ini = configparser.ConfigParser()
    config_ini.read('config.ini', encoding='utf-8')
    auth = tweepy.OAuthHandler(
        config_ini['DEFAULT']['api_key'], config_ini['DEFAULT']['api_key_secret'])
    auth.set_access_token(config_ini['DEFAULT']['access_token'],
                          config_ini['DEFAULT']['access_token_secret'])
    return auth


auth = get_authentication()
api = tweepy.API(auth)
print(message)
text = input()
api.update_status(text)
