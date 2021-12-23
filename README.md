# Détection de goélands nicheurs
Rendu d'un outil de deep learning pour l'annotation, l'entraînement et l'inférence dans le cadre de la détection d'oiseaux et de nids sur demande de Lorient Agglomération.

## Utilisation
Après avoir installé les prérequis, voici les différentes utilisations possibles de cet outil:

### Création de dataset (base de donnée pour apprentissage)
- Création des "bounding boxes" (rectangles entourant l'objet à détecter et description associée) avec le notebook Annotation.
- Transformation de données géoréféréncées (coordonnées longitude latitude) et d'images tifs en coordonnées pixel et en images jpg avec le notebook Transformation.
- Pré-processing des images jpg d'origine en images jpg de 1024x1024 px avec le notebook Preprocessing. 

### Entrainement
- Entrainement d'un modèle (réseau de neurones) sur un dataset déjà conçu (images jpg 1024x1024 px et fichiers json contenant les anntoations) avec le notebook Entrainement.

### Inférence
- Transformation des images TIF en images jpg avec le notebook Transformation.
- Exécution de prédictions sur des images jpg avec un modèle entrainé avec le notebook Entrainement.
- Transformation des prédictions pixel en prédiction géoréférencées avec les images tifs d'orgigine et le notebook Transformation.


## Prérequis
### Anaconda
[Installer sur Windows](https://www.anaconda.com/products/individual#windows)   (Ensuite lancer les commandes dans le terminal 'anaconda prompt')

[Installer sur Linux](https://docs.anaconda.com/anaconda/install/linux/)        (Ensuite lancer les commandes dans le terminal bash (présent de base))

## Préparation de l'environnement  
Une fois Anaconda installé, ouvrir le terminal puis lancer les commandes suivantes dans votre terminal(respecter l'ordre).
- `conda create -n <env_name>`
- `conda activate <env_name>`
- `conda install python=3.8`
- `cd C:\Users\tdelatouche\Documents\NestsRecognition-main` (remplacer par le chemin complet vers le dossier NestsRecognition si besoin)
- `pip install .`

Installer la dernière version de pytorch adaptée à votre OS, avec PIP: [pytorch.org](https://pytorch.org)

Installer GDAL pour python: lancer `conda install -c conda-forge gdal`  [Gdal::Anaconda.org](https://anaconda.org/conda-forge/gdal) pour plus d'informations

## Utilisation de l'environnement et de Jupyter notebook
Attention: il existe un fichier readme dans chaque dossier, à lire avant l'exécution des notebooks.
Une fois l'environnement préparé, à chaque utilisation des notebook il faudra:
- lancer le terminal
- `conda activate <env_name>`
- `jupyter notebook`
- chercher votre notebook (fichier .ipynb et l'ouvrir.

Une fois le Notebook ouvert, simplement exécuter les cellules (cliquer sur la cellule puis sur "RUN") dans l'ordre. Une cellule en cours d'exécution aura un astérix à gauche.

La plupart du temps les seuls choses à modifier se trouvent au début du notebook, dans les paramètres. Si une autre valeur est à modifier dans le notebook, ce sera précisé.

Pour fermer les notebook, fermer les fenêtres dans votre navigateur puis pour complêtement fermer jupyter notebook, taper CTRL+C dans le terminal.
