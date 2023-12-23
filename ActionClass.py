import time
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import  ActionChains


driver = webdriver.Chrome()
driver.get('https://webdriveruniversity.com/Actions/index.html')

# Test case 1 - Double click
# e = ActionChains(driver)
# db = driver.find_element(By.ID,'double-click')
# e.double_click(db).perform()
# db = driver.find_element(By.ID,'double-click')
# if "div-double-click double" in db.get_attribute("class"):
#     print('test case pass ')
# else:
#     print('test case fail')
# driver.close()


# Test case 2 - Drag and Drop
# e = ActionChains(driver)
# src = driver.find_element(By.ID,"draggable")
# destination = driver.find_element(By.ID,"droppable")
# print(destination.text)
# e.drag_and_drop(src,destination).perform()
# destination = driver.find_element(By.ID,"droppable")
# if destination.text == "Dropped!":
#     print("Test case pass")
# else:
#     print("Testcase fail")
# driver.close()


# Test case 3 - click and hold
# Well done! keep holding that click now.....
# e = ActionChains(driver)
# e2 = driver.find_element(By.ID,'click-box')
# e.click_and_hold(e2).perform()
# e2 = driver.find_element(By.ID,'click-box')
# if 'Well done! keep holding that click now.....' in e2.text:
#     print('Test case pass')
# else:
#     print("Testcase fail")

#Test case 4
# e = ActionChains(driver)
# moveToElement = driver.find_element(By.CSS_SELECTOR,"#div-hover > div.dropdown.hover > button")
# e.move_to_element(moveToElement).perform()
# avail = driver.find_element(By.CSS_SELECTOR,"#div-hover > div.dropdown.hover > div > a").is_displayed()
# if(avail):
#     print("text case pass")
# else:
#     print("test case fail")