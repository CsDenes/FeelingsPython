#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 19:08:11 2017

@author: Denes
"""

import keras

print(keras.__version__)


import numpy as np
np.random.seed(123)  # for reproducibility

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils
import re
import glob
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from keras.models import model_from_yaml


def catToInt(x):
    return {
        'an': 0,
        'di': 1,
        'fe': 2,
        'ha': 3,
        'sa': 4,
        'su': 5,
    }[x]

frameDir = '/Volumes/Data/Diploma/Media/Training/*'
imageFiles = glob.glob(frameDir)
x = []
y = []
for i in imageFiles:
    img = load_img(i)
    newX = img_to_array(img) 
    newX = newX.reshape((1,) + newX.shape)  
    if len(x):
        x = np.concatenate((x,newX))
    else: 
        x = newX
    cat = re.search('/([a-z]*)[0-9]*.jpg',i).group(1)
    y.append(catToInt(cat))

x.shape
x = x.astype('float32')
x /= 255


x[0].shape



Y = np_utils.to_categorical(y, 6)

model = Sequential()
model.add(Convolution2D(32, 3, 3, activation='relu', input_shape=(100,100,3)))
print (model.output_shape)
model.add(Convolution2D(32, 3, 3, activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(6, activation='softmax'))


model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.fit(x, Y, batch_size=32, nb_epoch=10, verbose=1)




imageDir = '/Users/Denes/Desktop/testImage.png'
img = load_img(imageDir)
testX = img_to_array(img) 
testX = testX.reshape((1,) + testX.shape)
 
predict = model.predict(testX)

predict


scores = model.evaluate(x, Y, verbose=0)

print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))












#save model
model_yaml = model.to_yaml()
with open("model.yaml", "w") as yaml_file:
    yaml_file.write(model_yaml)
# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")

# load YAML and create model
yaml_file = open('model.yaml', 'r')
loaded_model_yaml = yaml_file.read()
yaml_file.close()
loaded_model = model_from_yaml(loaded_model_yaml)
# load weights into new model
yaml_file = open("model.h5", 'r')
loaded_model.load_weights(yaml_file)
print("Loaded model from disk")

loaded_model.predict(testX)


