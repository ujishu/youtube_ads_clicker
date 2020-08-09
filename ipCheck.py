from selenium import webdriver
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from xvfbwrapper import Xvfb

vdisplay = Xvfb()
vdisplay.start()

driver = webdriver.Firefox()



driver.quit()
print('Driver.quit')
display.stop()
print('display.stop()')

# Commit v0.1
# TEST
# 
