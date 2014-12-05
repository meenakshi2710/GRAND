'''
Created on Nov 7, 2014

@author: mesharma
'''
LOG_PREFIX ='TEST_INFO: '

def logSpecialInfo(info):
    #Log the error when an element is not found
    print "*****",  '%s ' % (info), "*****"

def logTimeout(timeout):
    #Log the error when an element is not found
    print LOG_PREFIX,  'There is a timeout failure, timeout was set to %s ' % (timeout)

def logTimeTaken(timeSpent, timeout):
    #Log the time taken for an element's property to be same as expected
    print  LOG_PREFIX, 'waited %s, timeout was set to %s' % (timeSpent, timeout)

def logStepInfo(info):
    #Log the steps required while debugging
    print LOG_PREFIX, 'Step %s is complete' % (info)

def logCustomInfo(info):
    #Log the steps required while debugging
    print LOG_PREFIX, '%s ' % (info)

def logSuccessInfo(info):
    #Log the message when the test case is successful
    print LOG_PREFIX, '***** Successfully executed test case : %s *****' % (info)