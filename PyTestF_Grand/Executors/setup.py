'''
Created on Nov 7, 2014

@author: mesharma
'''
import windowsSetup as WS
import os
import unittest
import utilities.LogUtil as LU
from appium import webdriver
import platform


def setup():
    os = platform.system()
    print "OS detected: ", os
    if os is "Windows":
        WS.stop_appium_server_windows()
        WS.start_appium_server_windows()   
    
    success = True
    desired_caps = {}
    desired_caps['appium-version'] = '1.0'
    desired_caps['deviceName'] = 'Android Emulator'
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4'
    desired_caps['appPackage'] = 'com.goodreads'
    desired_caps['appActivity'] = 'com.goodreads.android.activity.MainMenuActivity'
    desired_caps['app'] = 'C:/Android/goodreads-android-1.12.10.apk'
    desired_caps['autoLaunch'] = True
    driver =  webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait(60)
    return driver

def tearDown(driver):
    LU.logSpecialInfo("Shutting down")
    driver.quit()