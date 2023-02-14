from src.tweet_collect.api_connexion import twitter_setup


def test():
    assert twitter_setup() is not None
