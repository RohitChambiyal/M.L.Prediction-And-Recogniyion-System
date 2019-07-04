#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 00:10:19 2019

@author: rohit
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tkinter
from tkinter.filedialog import askopenfilename
def t():
    tkinter.Tk().withdraw() # we don't want a full GUI,j so keep the root window from appearing
    file1 = askopenfilename()
    main_img = cv2.imread(file1) #'mainimg.jpg'
    main_gray = cv2.cvtColor(main_img,cv2.COLOR_BGR2GRAY)
    file2 = askopenfilename()
    template = cv2.imread(file2,0) #'matchimg.jpg'
    w,h= template.shape[::-1]
    res =cv2.matchTemplate(main_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(main_img,pt,(pt[0]+w , pt[1] + h),(0,255,255),2)
        print (pt[0] + w , pt[1] + h)
    #cv2.imshow('detected', main_img)
    plt.imshow(main_img)
    plt.show()
t()

