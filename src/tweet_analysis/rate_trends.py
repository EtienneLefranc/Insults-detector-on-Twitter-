import pandas as pd
import textblob.classifiers
import csv


def get_insult(langue="fr"):
    "renvoie la liste des insultes du fichier Insultes.csv"
    with open('src/tweet_analysis/Insultes_'+langue+'.csv') as csv_file:
        insultes = csv.reader(csv_file, delimiter=',')
        L = []
        insultes_dict = {}
        for row in insultes:
            L.append(row[0])
            insultes_dict[row[0]] = [row[i] for i in range(1, 6)]
    return L, insultes_dict


def count_insult(text, insults, insultsdict):
    '''Fonction qui compte le nombre d'insultes dans un texte'''
    ''' insults : liste de mots insultants sous la forme d'une liste de chaînes de caractères
        text : texte dans lequel on compte les insultes'''
    dico = textblob.classifiers.basic_extractor(text, insults)
    score = [0, 0, 0, 0, 0]
    for elt in dico.keys():
        if dico[elt]:
            mot = elt[9:-1]
            score = [score[i]+int(insultsdict[mot][i]) for i in range(5)]
    return score


def add_insults_count(dataframe, langue):
    """prend en argument un dataframe de tweets et ajoute une colonne nb_insults avec
     le nombre d'insultes dans le tweet"""
    insultes, insultescat = get_insult(langue)
    dataframe = dataframe.assign(homophob=[0 for i in range(len(dataframe))])
    dataframe = dataframe.assign(racist=[0 for i in range(len(dataframe))])
    dataframe = dataframe.assign(sexist=[0 for i in range(len(dataframe))])
    dataframe = dataframe.assign(religion=[0 for i in range(len(dataframe))])
    dataframe = dataframe.assign(insult=[0 for i in range(len(dataframe))])
    dataframe = dataframe.assign(
        total_insults=[0 for i in range(len(dataframe))])
    for i in range(len(dataframe)):
        texte = str(dataframe.at[i, 'text']).lower()
        score = count_insult(texte, insultes, insultescat)
        dataframe.at[i, 'homophob'] = score[0]
        dataframe.at[i, 'racist'] = score[1]
        dataframe.at[i, 'sexist'] = score[2]
        dataframe.at[i, 'religion'] = score[3]
        dataframe.at[i, 'insult'] = score[4]
        dataframe.at[i, 'total_insults'] = sum(score)
    return dataframe


def trend_rate(dataframe, category):
    """Compte le nombre de tweets contenant des insultes dans un dataframe et en déduit une note"""
    return 100*dataframe[category].sum()/len(dataframe)
