import time
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html')
# jsAlert = driver.find_element(By.CSS_SELECTOR,"#content > div > ul > li:nth-child(1) > button")
# jsAlert.click()
# # to click on OK button
# driver.switch_to.alert.accept()
# alertText = driver.switch_to.alert.text
# resultElement = driver.find_element(By.ID,"result")
# resultText = resultElement.text
# if resultText == 'You successfully clicked an alert' and alertText == 'alertText':
#     print("Test case pass")
# else:
#     print('Test case fail')

# Testcase2

driver.find_element(By.CSS_SELECTOR,'#content > div > ul > li:nth-child(2) > button').click()
driver.switch_to.alert.accept()
confirmText = driver.switch_to.alert.text
confirmMessage = driver.find_element(By.ID,'result').text
if confirmMessage == 'You clicked: Ok' and confirmText == "I am a JS Confirm":
    print("Testcase pass")
else:
    print("Test case fail")


# Testcase 3
driver.find_element(By.CSS_SELECTOR,'#content > div > ul > li:nth-child(2) > button').click()
driver.switch_to.alert.dismiss()
confirmText = driver.switch_to.alert.text
confirmMessage = driver.find_element(By.ID,'result').text
if confirmMessage == 'You clicked: Cancel' and confirmText == "I am a JS Confirm":
    print("Testcase pass")
else:
    print("Test case fail")


# Testcase 4

driver.find_element(By.CSS_SELECTOR,"#content > div > ul > li:nth-child(3) > button").click()
driver.switch_to.alert.send_keys("chinmay")
promtText = driver.switch_to.alert.text
driver.switch_to.alert.accept()
#I am a JS prompt
promptMessage = driver.find_element(By.ID,'result').text
if promptMessage == 'You entered: chinmay' and promtText == 'I am a JS prompt':
    print("Test case pass")
else:
    print("Test case fail")

    