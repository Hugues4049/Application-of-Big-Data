# Application-of-Big-Data
Industrialize a Datascience model through containerization


## TO DO
   [ ] Transform notebook to script python 
   [ ] Create DockerFile with require dependencies
   [ ] A volume mapping on an input directory in the local filesystem
   [ ] A volume mapping on an output directoryin the local filesystem
   [ ] At "docker run" command:
        • Python script should run
        • Load every images in input directory and make predictions
        • Finallyprovide a CSV file (with timestamp in filename) in output directory with "image_name,prediction_label" as columns
