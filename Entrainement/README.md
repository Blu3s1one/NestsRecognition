# Entrainement
Notebook pour la création de Dataset et l'entrainement d'un réseau de neurone.


## Etape 1: Preparer les données
Les données doivent être au format suivant:

-Images: 1024x1024 px (si possible au format .jpg)
-Annotations au format .json avec les classes 'boxes' et 'labels'.

Attention: Si vos images ne font pas 1024x1024 px, vous devriez les faire passer dans Preprocessing.

Mettre les images dans Entrainement/Input et les json dans Annotation/Target

## Etape 2: Lancer le Notebook training_script.ipynb
Rentrer dans la définition des parametres les classes présentes dans le dataset. Préciser si le GPU doit être utiliser ou non (1 ou None). 

Lancer les cellules jusqu'à l'entraînement. Il peut prendre quelques minutes comme quelques jours, en fonction de la taille du dataset. Une barre de progression s'affiche au bout de quelques dizaines de secondes.

Les checkpoints s'enregistrent dans le dossier NestsRecognition, mais une fois l'entraînement fini, et après avoir lancé la cellule de test, n'oubliez pas de sauvegarder la dernière(et meilleure) version du model avec la dernière cellule du notebook. Les models sont stockés dans le dossier Entrainement/Models. 

Attention: vérifiez qu'il n'existe pas déjà de model portant le nom best_model.pt dans le dosier Entrainement/Models.


