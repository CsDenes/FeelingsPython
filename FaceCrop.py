#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 22:55:39 2017

@author: Denes
"""

#import numpy as np
import cv2
#import PIL

haarfrontal = "/Users/Denes/Developer/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml"
eyeshaar = "/Users/Denes/Developer/opencv-master/data/haarcascades/haarcascade_eye.xml"
#import the xml files. here i am using frontal face and eye.
face_cascade = cv2.CascadeClassifier(haarfrontal)
eye_cascade = cv2.CascadeClassifier(eyeshaar)

img= cv2.imread('frame0.jpg') #reading the image
gray_img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converting into gratscale(algos work with grayscale images)

faces = face_cascade.detectMultiScale(img, 1.3, 5) #detecting faces. lightning conditions may affect the output
print (faces) #just printing to console. this will print boundary points of detected face(s)

#searching for eyes only in faces. easy and efficient to search only in face rather than whole image
for (p,q,r,s) in faces:
 cv2.rectangle(img,(p,q),(p+r,q+s),(150,125,0),2)        #drawing a rectangle indicating face
 face_gray = gray_img[q:q+s, p:p+r] #cropping   face in gray image
 face_color = img[q:q+s, p:p+r] #cropping face in  color image
 cv2.imwrite("output_face.jpg", face_color)
 eyes = eye_cascade.detectMultiScale(face_gray)  #searching for eyes in grayscale img
 for (ep,eq,er,es) in eyes:
  cv2.rectangle(face_color,(ep,eq),(ep+er,eq+es), (100,210,150),2) #for each eye drawing rectangle

#cv2.imshow("output", img)
#cv2.waitKey(0) #showing the img

#this only takes a image and shows the faces in the image. It dont modifies the image.
#if you want to save the resulted image use this...
cv2.imwrite("output.jpg", img)