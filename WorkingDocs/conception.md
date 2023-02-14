Le but est de repérer les sujets en tendance qui engendrent le plus de tweets contenant des insultes et ainsi de détecter les sujets les plus polémiques. <br/>

## Sprint1 : Collecte et stockage de données. <br/>
- [ ] **Fonctionnalité1** :<br/>
         collecter les tendances <br/>
- [ ] **Fonctionnalité2** : <br/>
         collecter les tweets se rapportant à ces tendances et les sauvegarder dans un fichier .json <br/>
- [ ] **Fonctionnalité3** : <br/>
         mettre ces données sous la forme d'un pandadataframe <br/>

## Sprint2 : Détection des insultes <br/>
- [ ] **Fonctionnalité4** : <br/>
         Créer un fichier insulte.txt <br/>
- [ ] **Fonctionnalité5** : <br/>
         Création d'une fonction detect_insult qui détecte si un tweet contient une insulte <br/>
- [ ] **Fonctionnalité6** : <br/>
         Mise en forme du pandadataframe avec les résultats de la détection <br/>

## Sprint3 : Présentation des résultats <br/>
- [ ] **Fonctionnalité5** : <br/>
         On donne la note défini ci-dessous au sujet à l'aide de la fonction rate_trends(pandadataframe): <br/>
             Note = nombre d'insultes sur les 100 derniers tweets pondéré par la "gravité" de chaque insulte <br/>
- [ ] **Fonctionnalité6** : <br/>
         On affiche les notes sur Dash pour les tendances <br/>


**MVP complété** <br/> 

## Sprint4 : Amélioration détection insultes <br/>
- [ ]  **Fonctionnalité7** : <br/>
         ajout de la fonctionnalité détection d'insulte pour l'anglais <br/>
- [ ]  **Fonctionnalité8** : <br/>
         Pondérer la note en fonction de la "vulgarité" des insultes et les catégoriser <br/>
