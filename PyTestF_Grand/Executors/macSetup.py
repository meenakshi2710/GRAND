'''
Created on Dec 2, 2014

@author: mesharma
'''
import subprocess
import utilities.LogUtil as LU
global pProcess
from time import sleep
from appium import webdriver


def stop_appium_server_mac():
    LU.logSpecialInfo("cleaning up ports...")   
    
    command = 'killall node'
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    pProcess = subprocess.Popen(command, shell=True, startupinfo=startupinfo)

    sleep(5)
    
def start_appium_server_mac():
    print "Launching Apppium server..."
    
    command = '/bin/sh /Applications/Appium.app/Contents/Resources/node/bin/node /Applications/Appium.app/Contents/Resources/node_modules/appium/bin/appium.js --address 0.0.0.0 --port 4723 --no-reset'

    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    pProcess = subprocess.Popen(command, shell=True, startupinfo=startupinfo)
    
    sleep(20)
    LU.logSpecialInfo("server launched...")   

def mac_setup():
    #TODO