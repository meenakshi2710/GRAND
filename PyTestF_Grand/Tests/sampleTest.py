'''
Created on Nov 5, 2014

@author: mesharma
'''
import os
import unittest

from appium import webdriver
from time import sleep
import Pages.LandingPage as LP, Pages.UpdatesPage as UP
import utilities.LogUtil as LU
import Executors.setup as S
from xmlrunner import XMLTestRunner
import time

LU.logSpecialInfo("Test started")
driver = S.setup()

class SampleTest(unittest.TestCase):
    def test_tap(self):
        LU.logCustomInfo("inside tap method...")
        driver.find_element_by_xpath(LP.UpdatesLink).click()
        LU.logStepInfo("tap on updates")
        sleep(5)
        driver.find_element_by_xpath(UP.findFriendLink).click()
        LU.logStepInfo("tap on find your friends")
        LU.logSuccessInfo("tap")
        pass

'''if __name__ == '__main__':
    
    unittest.main()
    S.tearDown(driver)
'''    
suite = unittest.TestLoader().loadTestsFromTestCase(SampleTest)

result = XMLTestRunner(file("/Users/mesharma/Desktop/Android/pythonResults/testOut.xml", "w")).run(suite)
S.tearDown(driver)

