from src.Dash.app import *
import os
from src.tweet_collect.tweet_data import import_tweets, dftrends
from src.tweet_analysis.rate_trends import trend_rate
import csv
import webbrowser
import datetime
from src.Dash.app import dash_graph


WOEID = {"Paris": 615702, "London": 44418,
         "New York": 2459115
         }  # Quelques exemples de WOEID


def find_data(date, lieu):
    folder = date+"_"+lieu
    f = open("Data/"+folder+"/tendances.csv", "r")
    fichier = csv.reader(f)
    for raw in fichier:
        trends_list = raw
    category = ["homophob", "racist", "sexist",
                "religion", "insult"]
    df = []
    for i in range(5):
        notes = []
        for trend in trends_list:
            dftrend = dftrends(folder, trend, lieu)
            test = dftrend[dftrend["insult"] > 10]
            if len(test) > 0:
                print(test)
            notes.append(trend_rate(dftrend, category[i]))
        df.append(pd.DataFrame(
            {"tendances": trends_list, "notes": notes}))
    return df


if __name__ == "__main__":
    date = str(datetime.datetime.now())[:10]
    donnees = []
    while True:
        entree = str(
            input("Souhaitez vous collecter les dernières tendances ? (oui/non): "))
        if entree == "oui":
            print("Collecte des tendances")
            for lieu in WOEID:
                import_tweets(lieu, date)
                donnees.append(find_data(date, lieu))
                print("Tweets collectés pour "+lieu)
            break
        elif entree == "non":
            if os.path.exists("Data/"+date+"_Paris"):
                print("Récupération des données")
                for lieu in WOEID:
                    donnees.append(find_data(date, lieu))
                break
            else:
                print(
                    "Vous n'avez récolté aucune donnée, il est impossible de continuer")
        else:
            print("Il y a une erreur dans la commande")
    webbrowser.open("http://127.0.0.1:8050/")
    dash_graph(donnees)
