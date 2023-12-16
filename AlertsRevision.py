import time
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Test case 1
# arrangement
# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# jsAlertE = driver.find_element(By.CSS_SELECTOR,'#content > div > ul > li:nth-child(1) > button')
# jsAlertE.click()
#
# # actions
# # Navigating the control to alert
# jsAlertText = driver.switch_to.alert.text
# driver.switch_to.alert.accept()
# # finding the element by ID
# resultE = driver.find_element(By.ID,'result')
# domText = resultE.text
#
# # assertion
# if jsAlertText  == "I am a JS Alert" and domText == 'You successfully clicked an alert':
#     print("Test case pass")
# else:
#     print("Test case fail")
# driver.close()

# Test case 2
# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# action
# confirmE = driver.find_element(By.XPATH,"//*[@id='content']/div/ul/li[2]/button")
# confirmE.click()
# confirmEText = driver.switch_to.alert.text
# driver.switch_to.alert.accept()
#
# # assertion
# resultE2 = driver.find_element(By.ID,'result')
# domText2 = resultE2.text
# print(resultE2)
# print(confirmEText)
#
# if domText2 == "You clicked: Ok" and confirmEText == "I am a JS Confirm":
#     print("Test case pass")
# else:
#     print("Test case fail")
# driver.close()

# Test case 3
# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
#
# confirmE = driver.find_element(By.XPATH,"//*[@id='content']/div/ul/li[2]/button")
# confirmE.click()
# confirmEText = driver.switch_to.alert.text
# driver.switch_to.alert.dismiss()
#
# # assertion
# resultE2 = driver.find_element(By.ID,'result')
# domText2 = resultE2.text
# print(resultE2)
# print(confirmEText)
# if domText2 == "You clicked: Cancel" and confirmEText == "I am a JS Confirm":
#     print("Test case pass")
# else:
#     print("Test case fail")
# driver.close()

# Test 4
# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# promptalertE = driver.find_element(By.CSS_SELECTOR,'#content > div > ul > li:nth-child(3) > button')
# promptalertE.click()
# promptAText = driver.switch_to.alert.text
# driver.switch_to.alert.send_keys("chinmay")
# driver.switch_to.alert.accept()
# textPrompt = driver.find_element(By.ID, "result").text
# if textPrompt == "You entered: chinmay" and promptAText == "I am a JS prompt":
#     print("Testcase pass")
# else:
#     print("Test case fail")


# Test case 5
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
promptalertE = driver.find_element(By.CSS_SELECTOR,'#content > div > ul > li:nth-child(3) > button')
promptalertE.click()
promptAText = driver.switch_to.alert.text
driver.switch_to.alert.send_keys("chinmay")
driver.switch_to.alert.dismiss()
textPrompt = driver.find_element(By.ID, "result").text
if textPrompt == "You entered: null" and promptAText == "I am a JS prompt":
    print("Testcase pass")
else:
    print("Test case fail")




