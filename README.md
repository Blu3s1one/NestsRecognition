# NestsRecognition
Rendu d'un outil d'annotation, d'entraînement(Faster-RCNN) et d'inférence pour la détection d'oiseaux et de nids sur demande de Lorient Agglomération.

## Utilisation
Après avoir installé les prérequis, voici les différentes utilistions possible de cet outil:

### Création de dataset
- Annotation avec notebook Annotation.
- Transformation de données géoréféréncées et d'images tifs en coordonnées pixel et images jpg avec le notebook Transformation.
- Pré-processing des images jpg en images de 1024x1024 px avec le notebook Preprocessing. 

### Entrainement
- Entrainement d'un modèle sur un dataset déjà concu (images jpg 1024x1024 px et fichiers json contenant les anntoations) avec le notebook Entrainement.

### Inférence
- Transformation des images TIF en images jpg avec le notebook Transformation.
- Exécution de prédictions sur des images jpg avec un modèle entrainé avec le notebook Entrainement.
- Transformation des prédictions pixel en prédiction géoréférencées avec les images tifs d'orgigine et le notebook Transformation.


## Prérequis
### Anaconda
[Installer sur Windows](https://www.anaconda.com/products/individual#windows)   (Ensuite lancer les commandes dans l'invite de commande 'anaconda prompt')

[Installer sur Linux](https://docs.anaconda.com/anaconda/install/linux/)        (Ensuite lancer les commandes dans le terminal bash (présent de base))

## Préparation de l'environnement  
Une fois Anaconda installé, lancer les commandes suivantes dans votre invite de commande.
- `conda create -n <env_name>`
- `conda activate <env_name>`
- `conda install python=3.8`
- `cd NestsRecognition` (remplacer par le chemin complet vers le dossier NestsRecognition si besoin)
- `pip install .`

Installer la dernière version de pytorch adaptée à votre OS, avec PIP: [pytorch.org](https://pytorch.org)

Installer GDAL pour python: lancer `conda install -c conda-forge gdal`  [Gdal::Anaconda.org](https://anaconda.org/conda-forge/gdal) pour plus d'informations

## Utilisation de l'environnement et de Jupyter notebook
Attention: il existe un readme dans chaque dossier, à lire avant l'éxécution des notebooks.
Une fois l'environnement préparé, à chaque utilisation des notebook il faudra:
- lancer le terminal
- `conda activate <env_name>`
- `jupyter notebook`
- chercher votre notebook et l'ouvrir.

Une fois le Notebook ouvert, simplement éxecuter les cellules (cliquer sur la cellule puis sur "RUN") dans l'ordre. La plupart du temps les seuls choses à modifier se trouvent au début du notebook, dans les paramètres. Si une autre valeur est à modifier dans le notebook, ce sera précisé.
