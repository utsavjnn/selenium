from selenium import webdriver
#to get access to keys like enter,escape etc..
from selenium.webdriver.common.keys import Keys

#to make driver wait for search results to come up
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


driver = webdriver.Chrome()

driver.get("https://www.techwithtim.net/");

print(driver.title);

#whenever searchin for an element in html
#keep preference to be
#1. id
#2. name
#3. class

search = driver.find_element_by_name("s")

#to type whatever we want in search bar
search.send_keys("test")
#now pressing enter
search.send_keys(Keys.RETURN)

try:
	main = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.ID,"main"))
		)
	articles=main.find_elements_by_tag_name("article")
	for article in articles:
		header = article.find_element_by_class_name("entry-summary")
		print(header.text)

finally:
	driver.quit()

#print(search.text)


#driver.quit(); #closes entire chrome window driver.close()-->closes the tab