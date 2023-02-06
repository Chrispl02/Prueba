#!/usr/bin/env python3ubuntu
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 11:14:19 2023

@author: christianpl
"""

import os
from os import listdir
from os.path import isfile, join
import pyautogui as auto
import time, glob
from ngitogrm import *
#import pyperclip xw 
#import subprocess
#from subprocess import Popen, PIPE
listgrm = glob.glob('/home/christian/Datos.Vipir/ngi/2023.01.11/*.ngi')
rutaSAO = 'SAO_old/'
rutafiles = '/home/christian/Datos.Vipir/grm/'
onlyfiles = [f for f in listdir(rutafiles) if isfile(join(rutafiles, f))]
ngitogrm(listgrm,rutafiles)
# bot1 = os.system('cd'+rutaSAO+'&')
bot1 = os.system('./SAO-X &')
time.sleep(0.5)
bot2 = os.system('wmctrl -a SAOExplorer v 3.6.1')
time.sleep(1.5)
auto.press('right', interval=0.1) 
auto.press('right', interval=0.1) 
auto.press('space')
#pyperclip.copy("2023.01.11JM91J_2023011000303.GRM")
#auto.hotkey("ctrl", "v")
auto.write("2023.01.11JM91J.2023011000303.GRM")
auto.press('enter', interval=1)
os.system('wmctrl -a SAOExplorer v 3.6.1')
#auto.locateCenterOnScreen('Ionogram.png', grayscale=True, confidence=.1)
auto.click(309,155,clicks=1,interval=1,button="left")
files = len([entry for entry in os.listdir(rutafiles) if os.path.isfile(os.path.join(rutafiles, entry))])
for i in range(files):
    auto.write("w")
    time.sleep(1.5)
    auto.press("space")
    time.sleep(1)
    auto.write("x")
    time.sleep(0.5)
    
    
