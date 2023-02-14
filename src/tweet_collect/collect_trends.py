import tweepy
import json
from src.tweet_collect.api_connexion import twitter_setup
import pandas as pd

WOEID = {"Paris": 615702, "London": 44418,
         "New York": 2459115,
         "Royaume-Uni": 23424975,
         "États-Unis": 23424977,
         "Australie": 23424748,
         "Canada": 23424775,
         }  # Quelques exemples de WOEID

# La fonction trends(id_lieu) renvoie un dictionnaire dont les clés sont 'trends', 'as_of', 'created_at', 'locations'
# Par la suite on utilisera principalement trends(id_lieu)["trends"] qui est une liste de dictionnaires
# représentants chaque tendances, et dont les clés sont 'name', 'url', 'promoted_content', 'query', 'tweet_volume'


def trends(id_lieu):
    """ id_lieu : WOEID du lieu d'où 'on prend les tendances
        retourne un dictionnaire comme décrit ci-dessus"""
    api = twitter_setup()
    trends = api.get_place_trends(id=id_lieu)
    return trends[0]
