'''
Created on Nov 5, 2014

@author: mesharma
'''
import unittest

from Pages import LandingPage as LP, SignUpPage as SUP
from utilities import LogUtil as LU, SignInTestInfo as STI
import Executors.setup as S
from Executors import CommonScenarios as CS
LU.logSpecialInfo("Test suite started")
from selenium.webdriver.support.wait import WebDriverWait
from xmlrunner import XMLTestRunner
from Executors import BasicActions as BA

class SignInTests(unittest.TestCase):

    def setUp(self):
        self.driver = S.setup()
    
    def tearDown(self):
        S.tearDown(self.driver)
            
    def test_SignInWithEmail(self):
        LU.logCustomInfo("Sign in with Email")
        self.driver.find_element_by_id(LP.lnkSignIn).click()
        self.driver = CS.signInWithEmail(self.driver, STI.getUserEmail(), STI.getUserPassword())
        
        LU.logStepInfo("tap on updates")
        self.driver.find_element_by_id(LP.btnUpdates).click()
        
        LU.logSuccessInfo("SignInWithEmail")
        pass

    def test_SignInWithFacebook(self):
        LU.logCustomInfo("Sign in with Facebook")
        trySignOut(self.driver)
        self.driver.find_element_by_id(LP.lnkSignIn).click()
        
        self.driver = CS.signInWithFacebook(self.driver, STI.getFbUserEmail(), STI.getFbUserPassword())
        
        LU.logStepInfo("tap on updates")
        self.driver.find_element_by_id(LP.btnUpdates).click()
        
        LU.logSuccessInfo("SignInWithFacebook")
        pass
   
    def test_SignInWithAmazon(self):
        LU.logCustomInfo("Sign in with Amazon")
        trySignOut(self.driver)
        
        self.driver.find_element_by_id(LP.lnkSignIn).click()
        self.driver = CS.signInWithAmazon(self.driver, STI.getAmazonUserEmail(), STI.getAmazonUserPassword())
         
        LU.logStepInfo("tap on updates")
        self.driver.find_element_by_id(LP.btnUpdates).click()
        
        LU.logSuccessInfo("SignInWithAmazon")
        pass
    
    def test_SignInFromSignUpView(self):
        LU.logCustomInfo("Sign in from Sign up view")
        self.driver.find_element_by_id(LP.lnkSignUp).click()
        
        SignUpPageIdentifier =  self.driver.find_element_by_id(SUP.txtName)
        wait = WebDriverWait(self.driver,8)
        wait.until(lambda driver: SignUpPageIdentifier.is_enabled())
    
        self.driver.find_element_by_id(SUP.btnSignIn).click()
        
        self.driver = CS.signInWithEmail(self.driver, STI.getUserEmail(), STI.getUserPassword())
        LU.logStepInfo("tap on updates")
        self.driver.find_element_by_id(LP.btnUpdates).click()
        
        LU.logSuccessInfo("SignInFromSignUpView")
        pass
'''
if __name__ == '__main__':
    S.launch_server()        
    unittest.main()
'''    
def trySignOut(driver):
    LU.logStepInfo("tap on Menu button")
    BA.pressBtnMenu(driver)
    
    #TODO - check for user signed in or not
    #wait = WebDriverWait(driver,2)
    #wait.until(lambda driver: driver.find_element_by_xpath(LP.lnkSignOut).is_enabled())
    LU.logCustomInfo("attempting to sign out")
    driver = CS.signOut(driver)
    
S.launch_server()        
suite = unittest.TestLoader().loadTestsFromTestCase(SignInTests)
result = XMLTestRunner(file("/Users/mesharma/Desktop/Android/pythonResults/testOut.xml", "w")).run(suite)

'''
    def test_tap(self):
        driver = S.setup()
        LU.logCustomInfo("inside tap method...")
        
        LandingPageIdentifier =  driver.find_element_by_id(LP.btnUpdates)
        
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.ID, LandingPageIdentifier)))
        
        sleep(5)
        driver.find_element_by_id(LP.btnUpdates).click()
        LU.logStepInfo("tap on updates")
        sleep(5)
        driver.find_element_by_id(UP.findFriendLink).click()
        LU.logStepInfo("tap on find your friends")
        
        LU.logSuccessInfo("tap")
        S.tearDown(driver)
        pass
'''    