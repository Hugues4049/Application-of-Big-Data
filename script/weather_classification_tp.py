

#Taken from : https://www.kaggle.com/datasets/utkarshsaxenadn/weather-classification-resnet152v2


# Common
import os
import keras
import numpy as np
import pandas as pd
from glob import glob
from tqdm import tqdm

# Data
from tensorflow.image import resize
from sklearn.model_selection import StratifiedShuffleSplit
from tensorflow.keras.utils import load_img, img_to_array

# Data Viz
import seaborn as sns
import matplotlib.pyplot as plt

# TL Model
from tensorflow.keras.applications import ResNet50, ResNet50V2, InceptionV3, Xception, ResNet152, ResNet152V2

# Model
from keras import Sequential
from keras.layers import Dense, GlobalAvgPool2D, Dropout
from keras.models import load_model

# Callbacks 
from keras.callbacks import EarlyStopping, ModelCheckpoint

# Model Performance
from sklearn.metrics import classification_report

# Model Viz
from tensorflow.keras.utils import plot_model




def load_image(path):
    '''
    Takes in path of the image and load it
    '''
    img = resize(img_to_array(load_img(path))/255., (256,256))
    return img


def load_data(img_paths):
    X = np.zeros(shape=(len(img_paths), 256,256,3))

    for i, path in tqdm(enumerate(img_paths), desc="Loading"):
        X[i] = load_image(path)
    
    return X



if __name__== "__main__":

    # Data and utilities

    #change working directory
    pathhh= os.getcwd()
    os.chdir(pathhh)
    
    # Cateories
    class_names = {0: 'cloudy', 1: 'foggy', 2: 'rainy', 3: 'shine', 4: 'sunrise'}
    # Load images
    image_paths = sorted(glob('/home/app/data_inputs/*.jpg'))
    images = load_data(image_paths)

    # Load model
    model_v3 = load_model('./ResNet152V2-Weather-Classification-03.h5')

    # Make Predictions
    preds = np.argmax(model_v3.predict(images), axis=-1)

    #Take the picture name from the path name 
    image_name = [val.split('/').pop(-1) for val in image_paths]

    #Associate prediction with class name
    pred = [class_names[list(preds)[i]] for i in range(len(preds))]

    #Create output file
    output = pd.DataFrame({'image_name':image_name, 'prediction_label':pred})
    output.to_csv('./home/app/data_outputs/Prediction_output{}.csv'.format(pd.datetime.now().strftime("%Y-%m-%d %Hh%Mm%Ss")),index=False) 

