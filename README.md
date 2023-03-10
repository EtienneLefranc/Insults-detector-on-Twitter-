# CW2_vulgarity


<img src='./WorkingDocs/tousantiinsultes_copie.png' width="400" height="400">



## L'équipe

+ Lisa Lupi
+ Antoine Dieu
+ Etienne Lefranc
+ Ambroise Marché
+ Matthieu Scharffe
+ Quentin Echasseriau



## Description du projet


Ce projet s'inscrit dans les projets de deuxième semaine des Coding Weeks de CentraleSupélec. Le programme récupère les tweets et les tendances twitter actuelles grâce aux fonctionnalités de l’API twitter et des modules pythons associés et renvoie un histogramme qui compare le taux d’insultes associé à chaque tendance. Ce taux est donné sous la forme du nombre d'insultes pour cent tweets, le tout pondéré selon la vulgarité et trié par type d'insulte. Cet outil peut être intéressant pour détecter les sujets les plus polémiques.



## Le programme

### Comment utiliser le programme ?

Rien de plus simple, il suffit de faire tourner le programme du fichier *main.py* situé à la racine du repo. Lors de votre première utilisation le terminal vous invitera à collecter les tweets présents dans la base de données de twitter. Il faut écrire oui dans le terminal. Pour les utilisations suivantes, les tweets étant déjà chargés, il est préférable de répondre non pour réduire le temps de traitement. Pour terminer le programme il suffit de faire `ctrl + c` dans le terminal.

### Structuration du programme

On retrouve 5 dossiers à la racine du repo ainsi que le fichier *.gitignore*, qui permet de ne pas envoyer les identifiants d'accès à l'API twitter, ainsi que les dossiers pycache générés par python. <br/>
Dans **WorkingDocs**, sont placés les fichiers utiles au développement mais qui ne sont pas exploitables par le programme comme le logo de notre groupe. <br/>

**Data** contient les mots-clés ainsi que les hashtags liés à certaines tendances twitter actuelles.  <br/>     

**test** contient les différentes fonctions de test. <br/>

Le dossier **src** contient tous les packages : 
+ **Dash** contient le fichier app_dash.py dans lequel est écrit le code de la page dash qui permet d’afficher l’histogramme.                                 
+ **tweet_analysis** contient une base de données de plusieurs centaines d’insultes en français et en anglais que nous avons répertoriées ainsi que le code qui permet d’associer une note à chaque tweet (rate_trends.py).
+ **tweet_collect** contient les fichiers suivants :
    * *api_connexion.py* qui permet de se connecter à l’API twitter.
    * *collect_trends.py* qui permet de récupérer les tendances twitter actuelles ainsi que plusieurs informations les concernant.
    * *collect_tweets.py* qui permet de récupérer les 100 derniers tweets d’une tendance ainsi que les réponses à ces tweets.
    * *json_file.py* qui permet de transformer une liste de tweets en un fichier json puis en un panda dataframe.
    * *tweet_data.py* qui permet de créer un petit datafile pandas avec certaines infos sur les tweets.

Le fichier **main.py** contient finalement la version finale du programme qui permet de renvoyer l’histogramme des notes de positivité de chaque tendance twitter actuelle.<br/>

### Les différents modules utilisés

**Tweepy** 

Vous pouvez trouver [ici](https://docs.tweepy.org/en/stable/index.html) la documentation de la version 4.3.0 de tweepy. <br/>
On peut l'installer avec la commande suivante : <br/>

```
pip install tweepy
``` 

**Textblob**<br/>
[Documentation de Textblob](https://textblob.readthedocs.io/en/dev/index.html) <br/>
``` 
pip3 install textblob
``` 

**Pandas**

[Documentation de pandas](https://pandas.pydata.org/pandas-docs/stable/)<br/>

``` 
pip install pandas
``` 

**Dash**

[Documentation de dash](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwihoKbY8530AhUFz4UKHcljApUQFnoECA4QAQ&url=https%3A%2F%2Fdash.plotly.com%2F&usg=AOvVaw0wNZrQX3xdcgdsG5iLfv2L) 

``` 
pip install dash==1.6.0  # The core dash backend
pip install dash-daq==0.2.1  # DAQ components (newly open-sourced!)
``` 

**os** 

[Documentation](https://docs.python.org/fr/3/library/os.html) <br/>

**JSON**

On utilise le module [json](http://www.json.org/jsonfr.html) pour stocker les tweets
#   I n s u l t - d e t e c t o r - o n - T w i t t e r  
 #   I n s u l t s - d e t e c t o r - o n - T w i t t e r -  
 