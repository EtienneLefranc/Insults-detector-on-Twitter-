import tweepy
from tweepy.api import API
from src.tweet_collect.credentials import *


def twitter_setup():
    """ On se connecte à l'API"""
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth)
    return api
