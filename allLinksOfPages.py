
import time
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()

# driver.get("https://webdriveruniversity.com/")
# time.sleep(3)
# # Test case 1
# #<a href = "https://www.facebook.com">Facebook</a>
# # total number of links
# links = driver.find_elements(By.CSS_SELECTOR,"a[href]")
# print("Total number of links :"+ str(len(links)))
# # total link address
# for link in links:
#     print(link.get_attribute("href"))
# # total link text
#     print(link.text)
#
# if(len(links) == 27):
#     print("test case pass")
# else:
#     print("test case fail")
#
# driver.close()

# test case 2
driver.get("https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")

# options = driver.find_elements(By.CSS_SELECTOR,'#dropdowm-menu-1 > option')
# print("Total options "+ str(len(options)))
# for option in options:
#     print(option.text)
# if(len(options) == 4):
#     print("Test case pass")
# else:
#     print("Test case fail")
# driver.quit()


#a = [11,22,33,44,33] ----> a.count(33)
#len(a)

dropdown = driver.find_element(By.CSS_SELECTOR,'#dropdowm-menu-1')
options = dropdown.find_elements(By.TAG_NAME,'option')
for option in options:
    print(option.text)
if(len(options) == 4):
    print("Test case pass")
else:
    print("Test case fail")

driver.close()