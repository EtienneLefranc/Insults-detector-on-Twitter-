import pandas as pd
from src.tweet_collect.collect_trends import trends
from src.tweet_collect.collect_tweets import collect, collect_replies
from src.tweet_collect.json_file import tweetsToJson, jsonToDf
from src.tweet_analysis.rate_trends import add_insults_count
import os
import csv
import datetime

WOEID = {"Paris": 615702, "London": 44418,
         "New York": 2459115
         }  # Quelques exemples de WOEID

LANGUES = {"Paris": "fr", "London": "en",
           "New York": "en"
           }


def rename_file(texte):
    result = ""
    for car in texte:
        if car in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ #":
            result += car
        elif car in "éèê":
            result += "e"
        elif car == "àâ":
            result += "a"
        elif car == "ç":
            result += "c"
    return result


def import_tweets(lieu, date):
    woeid = WOEID[lieu]

    """On collecte d'abord les tendances, puis on crée un dossier dans Data avec la date du jour.
        On récupère ensuite tous les tweets pour chaque tendance qu'on stocke dans un fichier dont le nom est
        la tendance."""
    trendsdict = trends(woeid)
    current_trends = trendsdict["trends"]
    if os.path.exists("Data/"+date+"_"+lieu):
        print("Tweets déjà importé aujourd'hui à "+lieu)
        return
    os.makedirs("Data/"+date+"_"+lieu)
    name_list = []
    for trend in current_trends:
        query = trend["query"]
        name = rename_file(trend["name"])
        name_list.append(name)
        file = date+"_"+lieu+"/"+name
        tweets = collect(query, LANGUES[lieu])
        df = pd.DataFrame(tweets)
        tweetsToJson(tweets, file)
    with open('Data/'+date+"_"+lieu+'/tendances.csv', 'w', newline='') as fichiercsv:
        writer = csv.writer(fichiercsv)
        writer.writerow(name_list)


def dftrends(folder, file, lieu):
    """Crée un petit datafile pandas avec certaines infos sur les tweets"""
    df = jsonToDf(folder+"/"+file)
    df = df[['id', 'created_at', 'user', 'text',
             'retweet_count', 'favorite_count']]
    df = df.assign(name=file)
    df = add_insults_count(df, LANGUES[lieu])
    return df
