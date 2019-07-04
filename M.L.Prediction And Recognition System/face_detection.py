#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 23:19:11 2019

@author: rohit
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def f():
    facecascade = cv2.CascadeClassifier('haarcascadeface.xml')
    eyecascade = cv2.CascadeClassifier('haarcascadeeye.xml')
    cap = cv2.VideoCapture(0)
    
    while(1):
        ret , img = cap.read()
        gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
        faces = facecascade.detectMultiScale(gray , 1.3,5)
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+y,w+h),(255,0,0),2)
            roi_gray = gray[y:y+h,x:x+w]
            roi_color = gray[y:y+h,x:x+w]
            eyes = eyecascade.detectMultiScale(roi_gray)
            for(ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+ew),(0,255,0),2)
        cv2.imshow('img',img)
        k = cv2.waitKey(30) & 0xFF
        if(k ==27):
                break
    cap.release()
    cv2.destroyAllWindows()
f()
