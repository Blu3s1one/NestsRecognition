### Transformations des données géolocalisées en données utilisables pour l'annotation/entrainement/inférence

Les données sous la forme d'image TIF et de coordonnées géographiques sont inutilisables par les autres notebook, on fait donc la transformation de ces données en données utilisables avec ce notebook.

## Image TIF vers jpg

Mettre les images TIF dans le dossier Transformation/tif_to_jpg/tifs.

Lancer la cellule correspondante. Les résultats sont enregistrés dans Transformation/tif_to_jpg/jpg.

## Géolocalisation vers pixel

Mettre les images TIF et les json correspondant(portant le même nom) respectivement dans Transformation/world_to_pixel/tifs et Transformation/world_to_pixel/jsons.

Lancer la cellule correspondante. Les résultats sont enregistrés dans Transformation/world_to_pixel/output.

## Pixel vers géolocalisation

Mettre les images TIF et les jsons correspondant(portant le même nom) respectivement dans Transformation/pixel_to_world/tifs et Transformation/pixel_to_world/jsons.

Lancer la cellule correspondante. Les résultats sont enregistrés dans Transformation/pixel_to_world/output.
