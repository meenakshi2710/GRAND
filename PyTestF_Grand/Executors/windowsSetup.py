'''
Created on Dec 2, 2014

@author: mesharma
'''
import subprocess
from time import sleep

from appium import webdriver
import utilities.LogUtil as LU
global pProcess


def stop_appium_server_windows():
    LU.logSpecialInfo("cleaning up ports...")   
    
    command = 'taskkill /F /IM node.exe'
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    pProcess = subprocess.Popen(command, shell=True, startupinfo=startupinfo)

    sleep(5)
    
def start_appium_server_windows():
    print "Launching Apppium server..."
    
    command = 'cmd /c C:/AppiumSetup/Appium/node.exe C:/AppiumSetup/Appium/node_modules/appium/bin/appium.js --address 0.0.0.0 --port 4723 --no-reset'

    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    pProcess = subprocess.Popen(command, shell=True, startupinfo=startupinfo)
    
    sleep(20)
    LU.logSpecialInfo("server launched...")   

def android_setup():
    success = True
    desired_caps = {}
    desired_caps['appium-version'] = '1.0'
    desired_caps['deviceName'] = 'Android Emulator'
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4'
    desired_caps['appPackage'] = 'com.goodreads'
    desired_caps['appActivity'] = 'com.goodreads.android.activity.MainMenuActivity'
    desired_caps['app'] = 'C:/AppiumSetup/goodreads-android-1.12.10.apk'
    desired_caps['autoLaunch'] = True
    driver =  webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait(60)
    return driver