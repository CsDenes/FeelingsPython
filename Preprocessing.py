#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 21:19:17 2017

@author: Denes
"""

import cv2
import glob
import re
import PIL
from PIL import Image



class Preprocessing:
    
    def imagePreprocessing(self, imageFile, imageDir):
        image = cv2.imread(imageFile)
        image = self.cropFace(image)
        image = self.resize(image)
        cv2.imwrite(imageDir+'testImage.png', image)
        return image
        
        
    countFrames = 0
    def getVideoFrames(self,videoFile,frameDir,cropFace = True, resize = True, framePerSec = 1):
        vidcap = cv2.VideoCapture(videoFile)
        success,image = vidcap.read()
        success = True
        while success:
            success,image = vidcap.read()
            if (self.countFrames % int(27 / framePerSec)) == 0:
                if success:
                    if cropFace:
                        image = self.cropFace(image)
                    if resize:
                        image = self.resize(image)
                    print( 'Read a new frame: ', success)
                    cv2.imwrite(frameDir +  re.search('/([a-z]*)[0-9]*.mp4',videoFile ).group(1) +   "%d.jpg" % self.countFrames, image) # save frame as JPEG file
                    print(self.countFrames)
            self.countFrames += 1
              
                

    def resize(self, img,x=100,y=100):
       img = cv2.resize(img, (x, y)) 
       return img
   
    def cropFace(self,img):
        haarfrontal = "/Users/Denes/Developer/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml"
        #import the xml files. here i am using frontal face and eye.
        face_cascade = cv2.CascadeClassifier(haarfrontal)
        faces = face_cascade.detectMultiScale(img, 1.3, 5) #detecting faces. lightning conditions may affect the output
        #searching for eyes only in faces. easy and efficient to search only in face rather than whole image
        face_color = img
        for (p,q,r,s) in faces:
            face_color = img[q:q+s, p:p+r] #cropping face in  color image
        return face_color
    
        
        
        
    
    



    