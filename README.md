# Application-of-Big-Data
Industrialize a Datascience model through containerization <br />


## TO DO
   -> Aicha
   [ ] Transform notebook to script python <br /> -> Aubain and Aicha
   [ ] Create DockerFile with require dependencies <br /> -> Arthur
   [ ] A volume mapping on an input directory in the local filesyste <br /> ?
   [ ] A volume mapping on an output directoryin the local filesystem <br /> 
   [ ] At "docker run" command: <br />  -> Aicha
        * Python script should run <br />  
        * Load every images in input directory and make predictions <br /> -> Aicha
        * Finallyprovide a CSV file (with timestamp in filename) in output directory with "image_name,prediction_label" as columns <br />

## Opérations faites:
   Dans le Dockerfile, il a été question de trouver une image qui est en adéquation avec mon python (Ubuntu:focal pour python3.9)
   Copier le script python, les requiements et le modèle Resnet dans le containeur car seul eux devront être utiliser dans le containeur
   Creer deux dossier data_inputs et data_outputs dans le containeur pour les mapper avec les volumes créer en local
   Installer python et pip dans le containeur
   Modifier la commande d'entrer du conaineur (CMD ["python3","weather_classification_tp.py"])

   Builder notre image avec la commande  
      "docker build -t imageprediction ." NB: mon image se nomme "imageprediction".
   Lister les containeur lancer avec la commande 
      "docker ps -a" qui vous donnera l'ID du containeur, le nom de l'image le status de l'image la date de création etc...
   Vous pouver supprimer les containeur avec 
      'docker prune'
   En suite creer les volumes et les mapper avec le containeur 
      "docker  run  -v /Bureau/app_data/data_inputs:/home/app/data_inputs -d -i imageprediction"
   Lister les volumes créer avec 
      "docker volume ls"
   Inspecter ou supprimre le volume avec 
      "docker volume inspect <nom du volume>"
      "docker volume rm <nom du volume>"