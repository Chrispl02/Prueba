import os
from os import listdir
from os.path import isfile, join
from configparser import SafeConfigParser
import subprocess
from array import array
import time, glob
from ngitogrm import *

listngi = glob.glob('/home/christian/Datos.Vipir/ngi/2023.01.11/*.ngi')
rutaSAO = 'SAO_old/'
rutafiles = '/home/christian/Datos.Vipir/grm/'
onlyfiles = [f for f in listdir(rutafiles) if isfile(join(rutafiles, f))]
ngitogrm(listngi,rutafiles)
listgrm = glob.glob('/home/christian/Datos.Vipir/grm/*.GRM')
# DataInputPath=/home/christian/Datos.Viper/grm/
# artist5_saox
# sed -i '561s/.*/DataInputPath = \/home\/christian\/Datos.Vipir\/SAOfiles\//' /home/christian/SAOExplorer/SAOExplorer.ini
os.system("sed -i '561s/.*/DataInputPath = \/home\/christian\/Datos.Vipir\/grm\//' /home/christian/SAOExplorer/SAOExplorer.ini")
os.system('./SAO-X &')
time.sleep(1.5)
Window_ID = os.popen('xdotool search --name "SAOExplorer v 3.5.1"').read()
read_screen = os.popen('xdotool getdisplaygeometry').read()
screen_size = read_screen.split()
screen =   [int(x) for x in screen_size]
os.system("xdotool windowactivate " + str(Window_ID))
time.sleep(0.5)
os.system('xdotool key Right')
os.system('xdotool key Right')
os.system('xdotool key space')
os.system('xdotool type "'+onlyfiles[0]+'"')
os.system('xdotool key KP_Enter')
time.sleep(0.1)
os.system('xdotool mousemove '+str((310/1920)*screen[0])+' '+str((155/1080)*screen[1])+' click 1 ')
files = len([entry for entry in os.listdir(rutafiles) if os.path.isfile(os.path.join(rutafiles, entry))])
time.sleep(0.5)
for i in range(files+1):
    os.system('xdotool type "w"')
    time.sleep(0.5)
    os.system('xdotool type "x"')
time.sleep(1.5)
#os.system("sed -i '561s/.*/DataInputPath = \/home\/christian\/Datos.Vipir\/SAOfiles\//' /home/christian/SAOExplorer/SAOExplorer.ini")
os.system("xdotool windowactivate " + str(Window_ID))
os.system('xdotool mousemove '+str((1620/1920)*screen[0])+' '+str((155/1080)*screen[1])+' click 1 ')
time.sleep(0.5)
os.system('xdotool key KP_Enter')
os.system('xdotool key KP_Enter')
os.system("xdotool windowkill "+Window_ID)