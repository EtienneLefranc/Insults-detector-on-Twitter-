from src.tweet_collect.tweet_data import import_tweets
from main import find_data


def test():
    import_tweets(615702, '2021-11-16', 'Paris')
    assert find_data('2021-11-16_Paris', 'Paris') is not None
