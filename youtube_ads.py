from selenium import webdriver
import time

#Proxy search 

#Set proxy for Firefox
#profile = webdriver.FirefoxProfile()
#profile.set_preference("network.proxy.type", 1)
#profile.set_preference("network.proxy.http", '79.188.42.46')
#profile.set_preference("network.proxy.http_port", '8080')
#profile.update_preferences()

#Set proxy for PhantomJS
service_args = ['--proxy=149.56.172.38:11219', '--proxy-type=socks5','--ignore-ssl-errors=true']
driver = webdriver.PhantomJS(executable_path='/home/ubuntu/phantomjs-2.1.1-linux-x86_64/bin/phantomjs' ,service_args=service_args)
driver.get('http://httpbin.org/ip')
print(driver.page_source.encode('utf-8'))

#driver = webdriver.Firefox(firefox_profile=profile)
#driver.set_window_size(1120, 550)
driver.get('https://www.youtube.com/watch?v=Q86vSrZdHzw')
#driver.implicitly_wait(17)
time.sleep(16)
#click on Skip button (not work)
#if driver.find_element_by_css_selector('.videoAdUiSkipContainer .html5-stop-propagation'):
#	skip = driver.find_element_by_css_selector('.videoAdUiSkipContainer .html5-stop-propagation').click()

# need more test. not all ads clickable 
# Find and click ads on page and video
try:
  #ad at right side
	frame1 = driver.find_element_by_id('google_ads_frame1').click()
	print('Found ad at right side')
except:
	print('ad at right side not found')

try:
#ad on video
	imageContainer = driver.find_element_by_css_selector('.image-container').click()
	print('Found ad on video')
except:
	print('ad on video not found')

try:
	textTitle = driver.find_element_by_css_selector('.text-title').click()
	print('Found .text-title')
except:
	print('text-title not found')


driver.quit()
print('Driver.quit')

#################################################################


#if driver.is_element_present_by_css('.flash-container'):
#	vid_ad2 = driver.find_by_css('.flash-container').first.click()

#if driver.is_element_present_by_css('.rhbutton'):
#	ad_button_link = ad_button.find_link_by_partial_href('doubleclick.net').click()

#if driver.is_element_present_by_id('google_ads_frame2'):
#	frame2 = driver.find_by_id('google_ads_frame2').click()

#driver.quit()
