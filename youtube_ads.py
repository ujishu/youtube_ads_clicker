#Run script:
#DISPLAY=:99 xvfb-run python youtube_ads.py

# This is added in branch v0.1
import os
import sys
######
import time

from selenium import webdriver
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time
from xvfbwrapper import Xvfb

vdisplay = Xvfb(width=1280, height=740, colordepth=16)
vdisplay.start()

##########################################################
#Proxy search 

#Set proxy for Firefox
profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type", 1)
#profile.set_preference("network.proxy.http", '79.188.42.46')
#profile.set_preference("network.proxy.http_port", '8080')
profile.update_preferences()
driver = webdriver.Firefox(firefox_profile=profile)

####### IP checking ######
#driver.get('http://httpbin.org/ip')
#driver.save_screenshot('/home/ujishu/httpbin.org.png')
#print(driver.page_source.encode('utf-8'))

#binary = FirefoxBinary('/usr/lib64/tor-browser_en-US/Browser/firefox')
#binary = FirefoxBinary('/usr/lib64/firefox/firefox')
#driver = webdriver.Firefox("""firefox_binary=binary, timeout=30,""" executable_path='/usr/lib64/tor-browser_en-US/Browser/firefox')
driver = webdriver.Firefox(executable_path='/usr/lib64/tor-browser_en-US/Browser/firefox')
print('webdriver started')
driver.get('https://www.youtube.com/watch?v=zHdwaQ5Zc0E')

#driver.get('http://www.i.ua/')

time.sleep(20)
driver.save_screenshot('/home/eugenes/youtube_ads_clicker/20sec.png')

#click on Skip button (not work)
#if driver.find_element_by_css_selector('.videoAdUiSkipContainer .html5-stop-propagation'):
#	skip = driver.find_element_by_css_selector('.videoAdUiSkipContainer .html5-stop-propagation').click()

# need more test. not all ads clickable 
#############################################################
############### Find and click ads on page and video #######################
try:
#ad on video
	imageContainer = driver.find_element_by_css_selector('.image-container').click()
	print('Found ad on video')
except:
	print('ad on video not found, find_element_by_css_selector')
time.sleep(5)

try:
#ad on video
	imageContainer = driver.find_element_by_class_name('image-container').click()
	print('Found ad on video')
except:
	print('ad on video not found, find_element_by_class_name')
time.sleep(5)

try:
  #ad at right side, frame1
	frame1 = driver.find_element_by_id('google_ads_frame1').click()
	print('Found ad at right side')
except:
	print('ad at right side not found, find_element_by_id(google_ads_frame1')

try:
  #ad at right side, frame2
	frame2 = driver.find_element_by_id('google_ads_frame2').click()
	print('Found ad at right side')
except:
	print('ad at right side not found, find_element_by_id(google_ads_frame2')

try:
	textTitle = driver.find_element_by_css_selector('.text-title').click()
	print('Found .text-title')
except:
	print('text-title not found')

driver.save_screenshot('/home/eugenes/youtube_ads_clicker/beforeExit.png')

driver.quit()
print('Driver.quit')
vdisplay.stop()
print('display.stop()')


#################################################################

#if driver.is_element_present_by_css('.flash-container'):
#	vid_ad2 = driver.find_by_css('.flash-container').first.click()

#if driver.is_element_present_by_css('.rhbutton'):
#	ad_button_link = ad_button.find_link_by_partial_href('doubleclick.net').click()

#if driver.is_element_present_by_id('google_ads_frame2'):
#	frame2 = driver.find_by_id('google_ads_frame2').click()

#driver.quit()
