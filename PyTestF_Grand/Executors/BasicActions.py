'''
Created on Dec 2, 2014

@author: mesharma
'''
import os
def pressBtnMenu(driver):
    '''driver.execute_script("mobile: keyevent", {"keycode": 1})'''
    os.system("adb shell input keyevent 82")

def pressBtnHome(driver):
    os.system("adb shell input keyevent 3")
    '''driver.execute_script("mobile: keyevent", {"keycode": 3})'''

def pressBtnBack(driver):
    os.system("adb shell input keyevent 4")
    '''driver.execute_script("mobile: keyevent", {"keycode": 4})'''

def pressBtnSearch(driver):
    os.system("adb shell input keyevent 84")
    '''driver.execute_script("mobile: keyevent", {"keycode": 84})'''
