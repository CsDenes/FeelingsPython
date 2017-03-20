#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 21:41:05 2017

@author: Denes
"""

from Preprocessing import Preprocessing
import cv2
import glob
import re


videoFile = '/Volumes/Data/Diploma/Media/*'
frameDir = '/Volumes/Data/Diploma/Media/Training/'
preProcessing = Preprocessing()
videoFiles = glob.glob(videoFile)
for v in videoFiles:
    preProcessing.getVideoFrames(v, frameDir)





