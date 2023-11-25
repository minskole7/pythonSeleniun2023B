from selenium import  webdriver
# arrangement
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/v1/index.html")
# actions
driver.find_element("id","user-name").send_keys("standard_user")
driver.find_element("id","password").send_keys("secret_sauce")
driver.find_element("id",'login-button').click()


# assertion
actual_title = driver.title
print(actual_title)
if(actual_title.startswith("Swag")):
    print("testcase pass")
else:
    print("testcase fail")
