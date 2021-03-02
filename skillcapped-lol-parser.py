import os
import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import io
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException
driver = webdriver.Chrome(ChromeDriverManager().install())
options = webdriver.ChromeOptions()

url = 'https:/better-skill-capped.com/'
links = []

#goes to website
driver.get(url)

#uncheck these lines if you do not want Commentaries and Videos, only Courses.

#uncheck Commentary checkbox
#driver.find_element_by_xpath(
#	"//div/div/div/section[2]/div/div[1]/nav[2]/div/div/div[2]/label/input"
#	).click()

#uncheck Video checkbox
#driver.find_element_by_xpath(
#	"//div/div/div/section[2]/div/div[1]/nav[2]/div/div/div[1]/label/input"
#	).click()

#loop over pages 
n = 90
for i in range(n):

	lnks=driver.find_elements_by_tag_name("a")
	for lnk in lnks:
		print(lnk.get_attribute("href"))

	time.sleep(2)

	driver.find_element_by_xpath(
		"//div/div/div/section[2]/div/div[2]/nav/button[2]"
		).click()

	time.sleep(2)