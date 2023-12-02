
import time
from selenium import  webdriver
from selenium.webdriver.common.by import By
# click()  into button
driver = webdriver.Chrome()
# Clicking on the element
# Testcase 1
# driver.get("https://www.webdriveruniversity.com/Contact-Us/contactus.html")
# driver.find_element(By.CSS_SELECTOR , "[name= 'first_name']").send_keys("chinmay")
# driver.find_element(By.CSS_SELECTOR , "[name= 'last_name']").send_keys("deshpande")
# driver.find_element(By.CSS_SELECTOR , "[name= 'email']").send_keys("chinmaydeshpande010@gmail.com")
# driver.find_element(By.CSS_SELECTOR , "[name= 'message']").send_keys("I am learning js")
# driver.find_element(By.CSS_SELECTOR,"[type='submit']").click() # click()
# avail = driver.find_element(By.TAG_NAME ,'h1').is_displayed()
# if avail:
#     print("Test case pass")
# else:
#     print("Test case fail")


# Test case 2
# type into input type box
# driver = webdriver.Chrome()
# driver.get("https://www.webdriveruniversity.com/Contact-Us/contactus.html")
# driver.find_element(By.CSS_SELECTOR , "[name= 'first_name']").send_keys("chinmay") # type
# driver.find_element(By.CSS_SELECTOR , "[name= 'last_name']").send_keys("deshpande")
# driver.find_element(By.CSS_SELECTOR , "[name= 'email']").send_keys("chinmaydeshpande010@gmail.com")
# driver.find_element(By.CSS_SELECTOR , "[name= 'message']").send_keys("I am learning js")
# driver.find_element(By.CSS_SELECTOR,"[type='submit']").click() # click()
# avail = driver.find_element(By.TAG_NAME ,'h1').is_displayed()
# if avail:
#     print("Test case pass")
# else:
#     print("Test case fail")

# Getting the text from the element

# driver = webdriver.Chrome()
# driver.get("https://www.webdriveruniversity.com/Contact-Us/contactus.html")
# actualText = driver.find_element(By.CSS_SELECTOR , '[name="contactme"]').text
# if(actualText == "CONTACT US"):
#     print("Test case pass")
# else:
#     print("Test case fail")

# Getting the attribute element
# Test case 4
# driver = webdriver.Chrome()
# driver.get("https://www.webdriveruniversity.com/Contact-Us/contactus.html")
# actualValue = driver.find_element(By.CSS_SELECTOR , '[name="contactme"]').get_attribute("class")
# if(actualValue == "section_header"):
#     print("Test case pass")
# else:
#     print("Test case fail")


# Clearing the input
# Test case 5
# driver = webdriver.Chrome()
# driver.get("https://www.webdriveruniversity.com/Contact-Us/contactus.html")
# firstName = driver.find_element(By.CSS_SELECTOR ,"[name='first_name']")
# firstName.send_keys("chinmay")
# firstName.clear()
# if firstName.text == "":
#     print("Test case pass")
# else:
#     print("Test case fail")


# Check if element is displayed
# Test case 6
# driver = webdriver.Chrome()
# driver.get("https://www.webdriveruniversity.com/Contact-Us/contactus.html")
# avail = driver.find_element(By.NAME , "first_name").is_displayed()
# if(avail):
#     print("Test case pass")
# else:
#     print("Test case fail")

# Test case 7
# Checking whether the element is enabled
driver = webdriver.Chrome()
driver.get("https://www.webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")
avail = driver.find_element(By.CSS_SELECTOR,"[value='cabbage']").is_enabled()
if(avail):
    print("Test case fail")
else:
    print("Test case pass")

# Check the radio button is checked
driver = webdriver.Chrome()
driver.get("https://www.webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")
avail = driver.find_element(By.CSS_SELECTOR,"[value='pumpkin']").is_selected()
if(avail):
    print("Test case pass")
else:
    print("Test case fail")


