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


def catToInt(x):
    return {
        'an': 0,
        'b': 1,
    }[x]

frameDir = '/Volumes/Data/Diploma/Media/Training/*'
imageFiles = glob.glob(frameDir)
x = []
y = []
for i in imageFiles:
    img = load_img(i)  # this is a PIL image
    x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
    x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)
    x = np.concatenate((x,x))
    cat = re.search('/([a-z]*)[0-9]*.jpg',i).group(1)
    y.append(catToInt(cat))

x = x.astype('float32')
x /= 255



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
predict = model.predict(x)

scores = model.evaluate(x, Y, verbose=0)

print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))


