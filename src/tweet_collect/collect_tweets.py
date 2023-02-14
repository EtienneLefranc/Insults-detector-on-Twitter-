from src.tweet_collect.api_connexion import twitter_setup


def collect(query, langue="fr"):
    connexion = twitter_setup()
    tweets = connexion.search_tweets(
        query, lang=langue, count=100)
    return tweets


def collect_replies(tweet):
    connexion = twitter_setup()
    user = tweet['user']
    name = user['screen_name']
    id = tweet['id']
    L = []
    tweets = connexion.search_tweets('to : '+name, count=3)
    for replies in tweets:
        if replies.in_reply_to_status_id == id:
            L.append(replies._json)
    return L
