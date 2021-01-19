from selenium import webdriver
#to get access to keys like enter,escape etc..
from selenium.webdriver.common.keys import Keys

#to make driver wait for search results to come up
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#to select action chains
from selenium.webdriver.common.action_chains import ActionChains


import time


driver = webdriver.Chrome()

driver.get("https://orteil.dashnet.org/cookieclicker/");

#implicitly wait
driver.implicitly_wait(20)

#accessing the cookie and the cookie count
cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")

items = [driver.find_element_by_id("productPrice"+str(i)) for i in range(1,-1,-1)]

actions = ActionChains(driver)

actions.click(cookie)

for i in range(1000):
	actions.perform()
	count = int(cookie_count.text.split(" ")[0])
	for item in items:
		value=int(item.text)
		if value<=count:
			upgrade_actions=ActionChains(driver)
			upgrade_actions.move_to_element(item)
			upgrade_actions.click()
			upgrade_actions.perform()

driver.quit()
