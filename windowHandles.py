import time
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('https://webdriveruniversity.com/')
first_window = driver.current_window_handle
print(first_window)
contact_link = driver.find_element(By.ID,"contact-us")
contact_link.click()

# all handles
# ['673F3A570868EB13F0D0D2F9AE6C9A50', '19DEED59F6BB8C149155A5134DEA3F0A']
listWindows  = driver.window_handles
print(list)

for handle in listWindows:
    if handle != first_window:
        driver.switch_to.window(handle)

contactE = driver.find_element(By.NAME , "contactme")
if contactE.is_displayed():
    print("Testcase pass")
else:
    print("Test case fail")

driver.close()

# monday - 9:30pm