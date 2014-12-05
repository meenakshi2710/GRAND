'''
Created on Dec 2, 2014

@author: mesharma
'''
import subprocess
import utilities.LogUtil as LU
global pProcess
from time import sleep

def stop_appium_server_windows():
    LU.logSpecialInfo("cleaning up ports...")   
    
    command = 'taskkill /F /IM node.exe'
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    pProcess = subprocess.Popen(command, shell=True, startupinfo=startupinfo)

    sleep(5)
    
def start_appium_server_windows():
    print "Launching Apppium server..."
    
    command = 'cmd /c C:/Users//mesharma/Desktop/Android/Appium/node.exe C:/Users/mesharma/Desktop/Android/Appium/node_modules/appium/bin/appium.js --address 0.0.0.0 --port 4723 --no-reset'

    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    pProcess = subprocess.Popen(command, shell=True, startupinfo=startupinfo)
    
    sleep(20)
    LU.logSpecialInfo("server launched...")   
     