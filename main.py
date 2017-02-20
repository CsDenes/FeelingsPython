#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 21:41:05 2017

@author: Denes
"""

import Preprocessing as p


videoFile = '/Users/Denes/Developer/Video/s1/'
frameDir = '/Users/Denes/Developer/Frames/'


import glob
files = glob.glob(videoFile + '*.mp4')
print (files)

#p.getVideoFrames(videoFile + 'an1.mp4', frameDir)


