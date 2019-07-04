#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 23:51:41 2019

@author: rohit
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tkinter
from tkinter.filedialog import askopenfilename
def i():
    tkinter.Tk().withdraw() # we don't want a full GUI,j so keep the root window from appearing
    file1 = askopenfilename()
    
    imo = cv2.imread(file1,0)
    file2 = askopenfilename()
    imt = cv2.imread(file2,0)
    #cv2.imshow('ori',imt)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    orb = cv2.ORB_create()
    #detector to detect
    keyp1, des1 = orb.detectAndCompute(imo,None)
    keyp2 , des2 = orb.detectAndCompute(imt,None)
    print(des1)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck =True)
    matches = bf.match(des1,des2)
    matches = sorted(matches, key = lambda x:x.distance)
    im3 = cv2.drawMatches(imo,keyp1, imt,keyp2,matches[:50],None,flags = 2)
    cv2.imshow('main',im3)
    #plt.imshow(im3)
    #plt.show()
i()