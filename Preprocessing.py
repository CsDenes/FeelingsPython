#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 21:19:17 2017

@author: Denes
"""

import cv2


def getVideoFrames(videoFile,frameDir):
    vidcap = cv2.VideoCapture(videoFile)
    success,image = vidcap.read()
    count = 0
    success = True
    while success:
        success,image = vidcap.read()
        if success:
            print( 'Read a new frame: ', success)
            cv2.imwrite(frameDir + "frame%d.jpg" % count, image) # save frame as JPEG file
            count += 1
  

