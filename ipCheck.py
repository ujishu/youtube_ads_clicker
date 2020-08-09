from selenium import webdriver
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import os
import sys
from xvfbwrapper import Xvfb

vdisplay = Xvfb()
vdisplay.start()

driver = webdriver.Firefox()

driver.quit()
print('Driver.quit')
display.stop()
print('display.stop()')
