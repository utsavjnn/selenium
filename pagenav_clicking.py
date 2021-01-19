from selenium import webdriver
#to get access to keys like enter,escape etc..
from selenium.webdriver.common.keys import Keys

#to make driver wait for search results to come up
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


driver = webdriver.Chrome()

driver.get("https://www.google.com");

search = driver.find_element_by_name("q")
search.clear()#clears all the text already in the element
#to type whatever we want in search bar
search.send_keys("utsav jain NIT Jalandhar")
#now pressing enter
search.send_keys(Keys.RETURN)

try:
	element = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"ZS"))
		)
	element.click()	
	time.sleep(5)
	driver.back()
	driver.back()

except:
	driver.quit()

driver.quit()


