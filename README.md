# NestsRecognition
Rendu d'un outil d'annotation, d'entraînement(Faster-RCNN) et d'inférence pour la détection d'oiseaux et de nids sur demande de Lorient Agglomération.

## Prérequis
### Anaconda
[Windows](https://www.anaconda.com/products/individual#windows)   (Ensuite lancer les commandes dans l'invite de commande 'anaconda prompt')

[Linux](https://docs.anaconda.com/anaconda/install/linux/)        (Ensuite lancer les commandes dans le terminal bash (présent de base))

## Préparation de l'environnement  
Une fois Anaconda installé, lancer les commandes suivantes dans votre invite de commande.
- `conda create -n <env_name>`
- `conda activate <env_name>`
- `conda install python=3.8`
- `cd NestsRecognition` (remplacer par le chemin complet vers le dossier NestsRecognition si besoin)
- `pip install .`

Installer la dernière version de pytorch adaptée à votre OS: [pytorch.org](https://pytorch.org)
Installer GDAL pour python: [gdal avec conda](https://anaconda.org/conda-forge/gdal)

## Utilisation de l'environnement et de Jupyter notebook
Une fois l'environnement préparé, à chaque utilisation des notebook il faudra:
- lancer le terminal
- `conda activate <env_name>`
- `jupyter notebook`
- chercher votre notebook et l'ouvrir.
