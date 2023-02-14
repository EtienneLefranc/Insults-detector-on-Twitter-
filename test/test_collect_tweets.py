from src.tweet_collect.collect_tweets import collect


def test():
    assert collect('bonjour') is not None
