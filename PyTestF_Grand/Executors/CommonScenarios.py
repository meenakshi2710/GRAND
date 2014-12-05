'''
Created on Dec 2, 2014

@author: mesharma
'''
global pProcess
from Pages import LandingPage as LP, SignInPage as SIP
from selenium.webdriver.support.wait import WebDriverWait

def signInWithEmail(driver, email, password):
    SignInPageIdentifier =  driver.find_element_by_id(SIP.txtEmail)
    wait = WebDriverWait(driver,8)
    wait.until(lambda driver: SignInPageIdentifier.is_enabled())
       
    driver.find_element_by_id(SIP.txtEmail).send_keys(email)
    driver.find_element_by_id(SIP.txtPassword).send_keys(password)
    driver.find_element_by_id(SIP.btnSignIn).click()
        
    SignedInPageIdentifier =  driver.find_element_by_id(LP.btnMyFriends)
    wait = WebDriverWait(driver,8)
    wait.until(lambda driver: SignedInPageIdentifier.is_enabled())
    return driver
   
def signInWithFacebook(driver, email, password):
    SignInPageIdentifier =  driver.find_element_by_id(SIP.txtPageTitle)
    wait = WebDriverWait(driver,8)
    wait.until(lambda driver: SignInPageIdentifier.is_enabled())
    
    driver.find_element_by_id(SIP.btnSignInFacebook).click()
    
    FbSignInIdentifier = driver.find_element_by_id(SIP.txtFbEmail)
    wait = WebDriverWait(driver,8)
    wait.until(lambda driver: FbSignInIdentifier.is_enabled())
    
    driver.find_element_by_id(SIP.txtFbEmail).send_keys(email)
    driver.find_element_by_id(SIP.txtFbPassword).send_keys(password)
    driver.find_element_by_id(SIP.btnFbSignIn).click()
    
    SignedInPageIdentifier =  driver.find_element_by_id(LP.btnMyFriends)
    wait = WebDriverWait(driver,8)
    wait.until(lambda driver: SignedInPageIdentifier.is_enabled())
    
    return driver

def signInWithAmazon(driver):
    SignInPageIdentifier =  driver.find_element_by_id(SIP.txtPageTitle)
    wait = WebDriverWait(driver,8)
    wait.until(lambda driver: SignInPageIdentifier.is_enabled())
    
    #WebDriverWait.until(EC.visibility_of(SignInPageIdentifier))
    #TODO Implement amazon sign in
    
    
        
    driver.find_element_by_id(SIP.btnSginInAmazon).click()
    driver.implicitly_wait(15)
    return driver

def signOut(driver):
    driver.find_element_by_xpath(LP.lnkSignOut).click()
    return driver