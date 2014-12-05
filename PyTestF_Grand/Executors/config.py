'''
Created on Dec 2, 2014

@author: mesharma
'''
appiumVersion = '1.0'
deviceName = 'Android Emulator'
platformName = 'Android'
platformVersion = '4.4'
appPackage = 'com.goodreads'
appActivity = 'com.goodreads.android.activity.MainMenuActivity'
app = 'C:/Android/goodreads-android-1.12.10.apk'
appiumUrl = 'http://localhost:4723/wd/hub'

windowsServerStartCommand = 'cmd /c C:/Android/Appium/node.exe C:/Android/Appium/node_modules/appium/bin/appium.js --address 0.0.0.0 --port 4723 --no-reset'
windowsKillCommand = 'taskkill /F /IM node.exe'