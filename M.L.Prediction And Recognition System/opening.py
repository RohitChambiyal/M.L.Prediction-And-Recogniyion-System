#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 11:09:06 2019

@author: rohit
"""
 # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3

# Code to add widgets will go here...

print('Press 1 for digit Recognition');
print('Press 2 for Face Detection');
print('Press 3 for Image Matching');
print('Press 4 for Template Matching');
print('Press 5 for Motion Sensor');
x = int(input())
print(x)

if x ==1:    
    import recog
#import recog
if x ==2:    
    import face_detection
if x==3:
    import images_matching
if x==4:
    import template_matching
if x ==5:
    import motion_sensor

import os
import tkinter
from tkinter.filedialog import askopenfilename


top = tkinter.Tk()

#def runr():
       # recog.r()
    
#def runf():
      ##  face_detection.f()
    
#def runm():
     #   motion_sensor.m()
    #
#def runt():
   #     template_matching.t()
  #  
#def y():
 #       top.destroy()
    
top = tkinter.Tk()
#rec = tkinter.Button(top,text = 'Select File',command = runr)
#exi = tkinter.Button(top,text = 'Select s',command = y)

#fac = tkinter.Button(top,text = 'Face Recognition',command = runf)
#fac.place(x=10,y=10)

#mot = tkinter.Button(top,text = 'Motion Recognition',command = runm)
#mot.place(x=30,y=30)

#templ = tkinter.Button(top,text = 'Template Matching',command = runt)
#templ.place(x=50,y=50)




#rec.place(x=70,y=70)

#exi.place(x=90,y=90)
#top.mainloop()

#while 1:
 #   top.update_idletasks()
  #  top.update()
