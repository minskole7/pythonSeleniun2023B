# click --- selenium ??
# scroll --- selenium ??
# getAttibute --- selenium ??

import time
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.get('https://webdriveruniversity.com/')

# Test case 1
# e = driver.find_element(By.ID,"contact-us")
# # e.click()
# driver.execute_script("arguments[0].click()",e)
# time.sleep(5)

# Test case 2
# se = driver.find_element(By.ID,"popup-alerts")
# driver.execute_script("arguments[0].scrollIntoView(true)",se)
# time.sleep(5)


# Test case 3
# title = driver.execute_script("return document.title")
# if title == "WebDriverUniversity.com":
#     print("Test case pass")
# else:
#     print("Test case fail")
# driver.close()

# Test case 4
se = driver.find_element(By.ID,"popup-alerts")
driver.execute_script("arguments[0].setAttribute('data-cy','two')",se)
time.sleep(20)















# driver.quit()

