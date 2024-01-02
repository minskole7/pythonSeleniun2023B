import time
from selenium import  webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://webdriveruniversity.com/IFrame/index.html')
#avail = driver.find_element(By.CSS_SELECTOR,"a[href='index.html']").is_displayed()

# index
# driver.switch_to.frame(0)

#name or Id
#driver.switch_to.frame('frame')

#byElement
e = driver.find_element(By.ID,"frame")
driver.switch_to.frame(e)
avail = driver.find_element(By.CSS_SELECTOR,"a[href='index.html']").is_displayed()
if(avail):
    print("Test case pass")
else:
    print("Test case fail")


driver.switch_to.default_content()
print(driver.title)


