import time

from selenium import  webdriver
from selenium.webdriver.common.by import By


# 25/11/2023
# arrangement
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/v1/index.html")

# actions
# reference for element
# <h1 id = "one" class = "two" name = "nm">Heading</h1>
# actual finding the element with id
# Webelements
#<input type="text" class="form_input" data-test="username" id="user-name" name="user-name" placeholder="Username" autocorrect="off" autocapitalize="none" value="">

username = driver.find_element("id",'user-name')
password = driver.find_element('id','password')
loginButton = driver.find_element("id","login-button")
logo = driver.find_element(By.CLASS_NAME,"login_logo")



# 1 method sendKeys()
# username.send_keys("standard_user")
# password.send_keys("secret_sauce")

# 2 click()
# loginButton.click()

# 3 clear()
# username.send_keys("standard_user")
# username.clear()

# get_attribute()
# str = logo.get_attribute("class")
# print(str)
#
# str2 = username.get_attribute("data-test")
# print(str2)












# assetion



