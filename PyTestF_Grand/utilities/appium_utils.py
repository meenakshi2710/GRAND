import subprocess
from time import sleep as sleep
from appium import webdriver


class AppiumWrapper(object):
    """
        The appium server interface object, controlling starting and stopping the server process and the connection.
    """

    # singleton
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(AppiumWrapper, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def start_server2(self):
        """ not used, doesn't start server in teh newly opened window """
        #open a new terminal window
        txt = 'open -a Terminal .'
        new_window = subprocess.call(txt, shell=True)
        assert new_window == 'foo'
        new_window.call('appium --shell --port 4723')
        #cmd = 'appium --shell --port 4723'
        #retcode = subprocess.check_output(cmd, shell=True)

    def start_server(self):
        """
            If we are running the Appium server programmatically, the server needs to be started
            in a terminal process. The Popen object is saved to the class, and is passed to the test case
            via the connect() method. The process pid is used during cleanup to kill this process.

            TODO: write the server output to a file, so that if the run errors out, only the python
            stack trace is shown in the terminal window.
            TODO: check for a currently running appium process and kill it before trying to start a new one.

            :return: None
        """
        self.server = subprocess.Popen(args=['appium'], shell=True)
        sleep(2)

    def connect_to_freestanding_appium(self):
        """
            Connect to the separately started Appium app.

            :return: driver
        """
        self.driver = None

        #set up the appium server desired capabilities
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '19.1'
        desired_caps['deviceName'] = 'SOHO'
        desired_caps['appPackage'] = 'com.goodreads.kindle'
        desired_caps['appActivity'] = 'com.goodreads.kindle.ui.activity.SplashActivity'
        desired_caps['appWaitActivity'] = 'com.goodreads.kindle.ui.activity.SplashActivity'
        desired_caps['autoLaunch'] = True
        try:
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            sleep(6)
        except:
            raise
        return self.driver

    def connect_to_appium(self):
        """
            Connect to the appium server; the server has to be running before we try to connect to it.

            TODO: logic to control whether to use the command line server instantiation or teh free-standing appium app.
            TODO: logic to handle dynamic device names.

            :return: tuple, self.driver (the webdriver instance) and self.server (the appium server instance).
        """
        self.driver = None

        #set up the appium server desired capabilities
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '19.1'
        desired_caps['deviceName'] = 'SOHO'
        desired_caps['appPackage'] = 'com.goodreads.kindle'
        desired_caps['appActivity'] = 'com.goodreads.kindle.ui.activity.SplashActivity'
        desired_caps['appWaitActivity'] = 'com.goodreads.kindle.ui.activity.SplashActivity'
        desired_caps['autoLaunch'] = True
        self.start_server()
        try:
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            sleep(4)
        except:
            print('appium server pid = %s' % self.server.pid)
            self.kill_server()
            raise
        return self.driver, self.server

    def disconnect_from_appium(self, kill=True):
        """
            Disconnect from the appium server.

            :kill: if True, call kill_server(). Defaults to True.
            :return: None
        """
        self.driver.quit()
        print('---> server dis-connected')
        if kill:
            self.kill_server()

    def kill_server(self):
        """
            Stop the appium server process by calling its terminate()( method. Just in case, also make another
            subprocess to kill the server's pid.
\
            :return: None
        """
        self.server.terminate()
        doublecheck = subprocess.Popen(args='kill %s' % str(self.server.pid), shell=True)
        doublecheck.terminate()
        print('---> server killed')

    def is_device_testable(self):
        """
            Currently, we must manually turn device on swipe to open the screen.

            TODO: 1. programmatically check whether device is on, and if possible, turn it on if it's off. connect()
                     will fail if the device is off.
                  2. check whether the lock screen needs to be open, and swipe it open if needed.
                  WebDriverException: Message: A new session could not be created. (Original error: Screen did not unlock)


                  3. check whether there's a password lock, and enter it if needed.
                  4. check whether the device is registered.
        """
        pass

