# Annotation
Notebook pour l'annotation des images. 

## Etape 1: Préparer les images
Mettre les images JPG (de n'importe quelle taille) dans le fichier Input.

## Etape 2: Lancer le notebook
Dans le Notebook, executer simplement les cellules jusqu'à l'affichage de Napari. Une fois la première image visible, lancer la cellule correspondant à la création de classe. Créer ensuite des box sur Napari, puis passer à l'image suivante ou précédente en appuyant respectivement sur 'N' et 'B'. Relancer la cellule de création de classe pour chaque nouvelle image.

Attention: Ne pas ajouter de classe sur une image où aucune box n'est à faire pour cette classe, sinon Napari risque de planter au changement d'image. Si vous le faites par erreur, vous pouvez supprimer la classe sur napari.

## Etape 3: Enregistrer les images
Lancer la cellule d'enregistrement des annotations qui iront dans le dossier Output. Il existe 2 cellules pour faire cela: la première enregistre les annotations pour' l'image actuellement affichée sur napari, et l'autre enregistre toutes les annotations faites depuis l'ouverture de Napari. 

Attention: Ne pas fermer Napari sans avoir enregistrer les annotations.

