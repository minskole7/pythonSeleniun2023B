import time
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


# program 1
driver = webdriver.Chrome()
driver.get('https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html')
drop_element = driver.find_element(By.ID,"dropdowm-menu-1")
sel = Select(drop_element)
sel.select_by_index(1)
#sel.select_by_value("c#")
#sel.select_by_visible_text("C#")
if sel.first_selected_option.text == "C#":
    print("Testcase pass")
else:
    print("Testcase fail")

# program 2

checkBoxElement = driver.find_element(By.CSS_SELECTOR,"input[value='option-1']")
checkBoxElement.click()
avail = checkBoxElement.is_selected()
if avail:
    print("Testcase pass")
else:
    print("Test case fail")


checkBoxElement3 = driver.find_element(By.CSS_SELECTOR,"input[value='option-3']")
checkBoxElement3.click()
not_avail = checkBoxElement3.is_selected()
if not not_avail:
    print("Test case pass")
else:
    print('Test case fail')

# Testcase 3

green_button  = driver.find_element(By.CSS_SELECTOR , 'input[value = "green"]')
blue_button = driver.find_element(By.CSS_SELECTOR , 'input[value = "blue"]')
green_button.click()
avail = green_button.is_selected()
not_avail = blue_button.is_selected()
if avail and not not_avail:
    print("test case pass")
else:
    print("test case fail")


