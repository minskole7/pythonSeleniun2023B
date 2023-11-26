import time
from selenium import  webdriver
from selenium.webdriver.common.by import By


# Test case 1  (Arrangement)
driver = webdriver.Chrome()
driver.get("http://www.webdriveruniversity.com/Contact-Us/contactus.html")# locators
# Name
# Id
# ClassName
# Css selector
# tagName


# Webelements
first_name = driver.find_element(By.NAME,'first_name')
last_name = driver.find_element(By.NAME,'last_name')
email = driver.find_element(By.NAME,'email')
message = driver.find_element(By.NAME,'message')
submitButton = driver.find_element(By.CSS_SELECTOR,"input[type='submit']")
form  = driver.find_element(By.ID,'contact_form')

# WebElements  --> sendKeys() , click() , submit() , isdisplayed()
first_name.send_keys("chinmay")
last_name.send_keys("deshpande")
email.send_keys("chinmaydeshpande010@gmail.com")
message.send_keys("I am learning js")
form.submit()
#submitButton.click()
msg = driver.find_element(By.TAG_NAME , 'h1')

# assertion
avail = msg.is_displayed()
print(avail)


