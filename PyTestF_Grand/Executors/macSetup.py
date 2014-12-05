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
    pProcess = subprocess.Popen(command, shell=True)

    sleep(5)
    
def start_appium_server_mac():
    print "Launching Apppium server..."
    
    command = '/bin/sh /Applications/Appium.app/Contents/Resources/node/bin/node /Applications/Appium.app/Contents/Resources/node_modules/appium/bin/appium.js --address 0.0.0.0 --port 4723 --no-reset'
    pProcess = subprocess.Popen(command, shell=True)
    
    sleep(20)
    LU.logSpecialInfo("server launched...")   

def mac_setup():
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