from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
#from xvfbwrapper import Xvfb #import virtual display
#vdisplay = Xvfb()
#vdisplay.start()
from pyvirtualdisplay import Display
display = Display(visible=0, size=(1024, 768))
display.start()

#Proxy search 

#Set proxy for Firefox
#profile = webdriver.FirefoxProfile()
#profile.set_preference("network.proxy.type", 1)
#profile.set_preference("network.proxy.http", '79.188.42.46')
#profile.set_preference("network.proxy.http_port", '8080')
#profile.update_preferences()
#driver = webdriver.Firefox(firefox_profile=profile)

############## PhantomJS ################################
#PhantomJS webdriver conf.
#dcap = dict(DesiredCapabilities.PHANTOMJS)
#dcap["phantomjs.page.settings.userAgent"] = (
#	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
#    "(KHTML, like Gecko) Chrome/15.0.87"
#)

#Set proxy for PhantomJS
#service_args = ['--proxy=176.37.38.90:80', '--proxy-type=http','--ignore-ssl-errors=true', '--ssl-protocol=any']
#service_args = []
#driver = webdriver.PhantomJS(
#	executable_path='/home/ujishu/phantomjs-2.1.1-linux-x86_64/bin/phantomjs' 
#	,service_args=service_args
#	,desired_capabilities=dcap
#)
#########################################################

####### IP checking ######
#driver.get('http://httpbin.org/ip')
#driver.save_screenshot('/home/ujishu/httpbin.org.png')
#print(driver.page_source.encode('utf-8'))
driver = webdriver.Firefox()
#driver.set_window_size(1024, 768)
driver.get('https://www.youtube.com/watch?v=_BI82YaqVU0')
#driver.get('http://www.i.ua/')
#driver.implicitly_wait(17)
time.sleep(20)
#print('time.sleep complete')
driver.save_screenshot('/home/ujishu/video.png')

#click on Skip button (not work)
#if driver.find_element_by_css_selector('.videoAdUiSkipContainer .html5-stop-propagation'):
#	skip = driver.find_element_by_css_selector('.videoAdUiSkipContainer .html5-stop-propagation').click()

# need more test. not all ads clickable 
# Find and click ads on page and video#############################################################
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


driver.quit()
print('Driver.quit')
display.stop()

#################################################################


#if driver.is_element_present_by_css('.flash-container'):
#	vid_ad2 = driver.find_by_css('.flash-container').first.click()

#if driver.is_element_present_by_css('.rhbutton'):
#	ad_button_link = ad_button.find_link_by_partial_href('doubleclick.net').click()

#if driver.is_element_present_by_id('google_ads_frame2'):
#	frame2 = driver.find_by_id('google_ads_frame2').click()

#driver.quit()
