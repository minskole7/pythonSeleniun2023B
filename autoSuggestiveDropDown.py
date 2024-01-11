import time
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.get("https://webdriveruniversity.com/Autocomplete-TextField/autocomplete-textfield.html")

actualTitle = driver.title
expectedTitle = "WebDriver | Contact Us"
#assert  actualTitle == expectedTitle
if(actualTitle == expectedTitle):
    print("Testcase pass")
else:
    print("Test case fail")

driver.find_element(By.ID,"myInput").send_keys("A")
elements = driver.find_elements(By.CSS_SELECTOR, "#myInputautocomplete-list  > div")
for element in elements:
    if element.text == "Almond":
            element.click()
            driver.find_element(By.ID, "submit-button").click()
            if "Almond" in  driver.current_url:
                print("Testcase pass")
            else:
                print("Testcase fail")
            break


driver.find_element(By.ID,"myInput").clear()
driver.find_element(By.ID,"myInput").send_keys("G")
elements = driver.find_elements(By.CSS_SELECTOR, "#myInputautocomplete-list  > div")
for element in elements:
    if element.text == "Grapes":
            element.click()
            driver.find_element(By.ID, "submit-button").click()
            if "Grapes" in  driver.current_url:
                print("Testcase pass")
            else:
                print("Testcase fail")
            break


driver.close()











