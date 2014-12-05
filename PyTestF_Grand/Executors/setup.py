'''
Created on Nov 7, 2014

@author: mesharma
'''
import platform

import utilities.LogUtil as LU
import windowsSetup as WS, macSetup as MS
os = platform.system()

def launch_server():
    
    print "OS detected: ", os
    if os is "Windows":
        WS.stop_appium_server_windows()
        WS.start_appium_server_windows()  
    if os is "Darwin":
        MS.stop_appium_server_mac()
        MS.start_appium_server_mac() 

def setup():
    
    if os is "Windows":
        return WS.android_setup()
    if os is "MAC":
        return MS.mac_setup()
        
        
def tearDown(driver):
    LU.logSpecialInfo("Shutting down")
    driver.quit()