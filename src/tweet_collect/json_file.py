import json
import pandas as pd


def tweetsToJson(tweets, file):
    """ tweets : liste de tweets
        filename : nom que l'on veut donner au fichier
        crée un fichier .json avec les tweets"""
    f = open("Data/"+file+".json", 'a')
    L = []
    for tweet in tweets:
        L.append(tweet._json)
    '''On récupère pour chaque tweet la partie que l'on peut stocker dans json'''
    json.dump(L, f)
    f.close()
    return


def jsonToDf(file):
    """ Transforme le contenu d'un fichier json f en un panda dataframe, f est ici le nom du fichier sous forme de chaîne de caractère"""
    """["id", "created_at", "text", "retweet_count",
         "favorite_count"] : quelques colonnes"""
    json_data = open("./Data/"+file+'.json', 'r', encoding="utf8")
    data_dict = json.load(json_data)
    data_tweet = pd.DataFrame(data_dict)
    return data_tweet
