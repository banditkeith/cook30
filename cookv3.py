# -coding: utf-8-
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchAttributeException
from selenium.common.exceptions import WebDriverException
import pickle
import os
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('ignore-ssl-errors')
dir_path = os.path.dirname(os.path.realpath(__file__))
chromedriver = dir_path + "/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chrome_options=options, executable_path= chromedriver)
#Select_dropdown = new_Select(driver.findElement(By.id("ELEMENT ID")));
#wait = WebDriverWait(driver, 3)

print("ESSKEETIT")
#driver.get('https://hidester.com/proxy')
#driver.find_element_by_xpath("""//*[@id="input"]""").send_keys("supremenewyork.com")
#driver.find_element_by_xpath("""//*[@id="hidester-form"]/div/div[2]/input[3]""").click()


driver.get('https://www.supremenewyork.com/shop/all/sweatshirts')

print("finding stuff..")
while True:
	try:
		driver.find_element_by_partial_link_text('Jet' and 'Violet').click()
	except (NoSuchElementException):
		driver.refresh()
		continue
	break


print("selecting size..")

while True:
	try:
		avail = driver.find_element_by_xpath("""//*[@id="s"]""")
		if avail.is_displayed():
			print("available..")
			driver.find_element_by_xpath("""//*[@id="s"]""").click()
			Select(driver.find_element_by_xpath("""//*[@id="s"]""")).select_by_visible_text("XLarge")
			driver.find_element_by_xpath("""//*[@id="add-remove-buttons"]/input""").click()
			pickle.dump(driver.get_cookies(), open("cookies.pk1", "wb"))
	except(NoSuchElementException):
		print("gimme a sec..")
		time.sleep(.2)
		#driver.get('https://www.supremenewyork.com/shop/all')
		continue
	break
	

#driver.get("https://supremenewyork.com/shop/all/shorts")

#print("finding stuff..")
#while True:
#	try:
#		driver.find_element_by_partial_link_text('Cargo' and 'Burgundy').click()
#	except (NoSuchElementException):
#		driver.refresh()
#		continue
#	break


#print("selecting size..")

#while True:
#	try:
#		avail = driver.find_element_by_xpath("""//*[@id="s"]""")
#		if avail.is_displayed():
#			print("available..")
#			driver.find_element_by_xpath("""//*[@id="s"]""").click()
#			Select(driver.find_element_by_xpath("""//*[@id="s"]""")).select_by_visible_text("34")
#			driver.find_element_by_xpath("""//*[@id="add-remove-buttons"]/input""").click()
#			pickle.dump(driver.get_cookies(), open("cookies.pk1", "wb"))
#	except(NoSuchElementException):
#		print("gimme a sec..")
#		time.sleep(.2)
#		#driver.get('https://www.supremenewyork.com/shop/all')
#		continue
#	break


print("checkout incoming..")
driver.get("https://supremenewyork.com/checkout")

#driver.find_element_by_xpath("""//*[@id="cart"]/a[2]""").click()

print("typing 4 u..")
driver.find_element_by_xpath("""//*[@id="order_billing_name"]""").send_keys("Keith Richards")#FULL NAME
#time.sleep(.12)
driver.find_element_by_xpath("""//*[@id="order_email"]""").send_keys("banditkeith.business@gmail.com")#EMAIL
#time.sleep(.10)
driver.find_element_by_xpath("""//*[@id="order_tel"]""").send_keys("910 775 3862")#PHONE
#time.sleep(.3)
driver.find_element_by_xpath("""//*[@id="bo"]""").send_keys("28 Ur Moms Pl")#ADDRESS
#time.sleep(.2)
driver.find_element_by_xpath("""//*[@id="order_billing_zip"]""").send_keys("28202")#ZIP CODE
#time.sleep(.10)
#driver.find_element_by_xpath("""//*[@id="order_billing_city"]""").send_keys("Concord")#CITY
#time.sleep(.2)
driver.find_element_by_xpath("""//*[@id="order_billing_state"]/option[38]""").click()
#card info
time.sleep(.10)
driver.find_element_by_xpath("""//*[@id="nnaerb"]""").send_keys("4554 3321 1123 5543")#CREDITCARD
#time.sleep(.1)
driver.find_element_by_xpath("""//*[@id="credit_card_month"]/option[2]""").click()#MONTH03
time.sleep(.2)
driver.find_element_by_xpath("""//*[@id="credit_card_year"]/option[3]""").click()#YEAR21
print("almost there..")
