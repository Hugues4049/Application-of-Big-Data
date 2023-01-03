# Application-of-Big-Data
## Industrialize a Datascience model through containerization <br />


## Opérations faites dans le Script python:
   Dans le script python, nous avons:
      -Supprimer les lignes de code pour la visualisation (pas utiles)
      -Introduit le chemain vers la source de données dans le conteneur (/home/app/data_inputs/*.jpg')
      -Charger le model resnet à partir de git lfs
      -Associer à chaque image un nom à partir de son chemain d'accès
      -Faire resortir le resultat des prédiction dans un dataframe avec en colonnes le nom des images et le label de la prediction associée
      -Convertir le dataframe en fichier CSV en temps réel qui va être télécharger grâce au mappage dans un dossier local.<br />

## Opérations faites dans le Dockerfile:
   Dans le Dockerfile, il a été question de trouver une image qui est en adéquation avec notre python (Ubuntu:focal pour python3.9)
   Copier le script python, les requirements et le modèle Resnet15 dans le containeur car seul eux devront être utiliser.
      -Creer deux dossier data_inputs et data_outputs dans le containeur pour les mapper avec les volumes créer en local
      -Installer python et pip dans le containeur
      -Modifier la commande d'entrer du conaineur (CMD ["python3","weather_classification_tp.py"])

      -Builder notre image avec la commande  
         "docker build -t imageprediction ." NB: notre image se nomme "imageprediction".
      -Lister les containeur lancer avec la commande 
         "docker ps -a" qui vous donnera l'ID du containeur, le nom de l'image le status de l'image la date de création etc...
      -Vous pouver supprimer les containeur avec 
         'docker system prune'
      -En suite lancer le containeur en lui demandant de mapper ses dossier (data_inputs et data_outputs) avec les dossier locaux pour ensuite excécuter le script python avec la commande 
         "docker  run -v /home/roland/Bureau/app_data/data_inputs:/home/app/data_inputs -v /home/roland/Bureau/app_data/data_outputs:/home/app/data_outputs  -i imageprediction" 
      NB: "/home/roland/Bureau/app_data/data_inputs:/home/app/data_inputs" est le chemin absolu du dossier contenant les images en local
      -Lister les volumes créer avec 
         "docker volume ls"
      -Inspecter ou supprimre le volume avec 
         "docker volume inspect <nom du volume>"
         "docker volume rm <nom du volume>"