#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 18:32:46 2017

@author: Denes
"""

#import image
faceimage = '/Users/Denes/Developer/FeelingsPython/output_face.jpg'
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
img = load_img(faceimage)  # this is a PIL image
x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)

#base64 coding
filename = '/Users/Denes/Developer/FeelingsPython/Base64Image.txt' 
results = ""
with open(filename) as inputfile:
    results = inputfile.readline()

import base64
results += "=" * ((4 - len(results) % 4) % 4)
imgdata = base64.b64decode(results)
filename = '/Users/Denes/Developer/FeelingsPython/img.png'  # I assume you have a way of picking unique filenames
with open(filename, 'wb') as f:
    f.write(imgdata)
    
    
#dirquerry
import glob
files = glob.glob(videoFile + '*.mp4')
for file in files:
    print(file[-7:-5])
print (files)

#resize
import PIL
from PIL import Image
img = Image.open('/Users/Denes/Developer/FeelingsPython/output_face.jpg')
img = img.resize((100, 100), PIL.Image.ANTIALIAS)
img.save('/Users/Denes/Developer/FeelingsPython/resized_image.jpg')