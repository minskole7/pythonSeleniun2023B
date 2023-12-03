import time
from selenium import  webdriver
from selenium.webdriver.common.by import By

#<h2 name="contactme" class="section_header">CONTACT US</h2>
# <section id="contact_me">
#                 <div class="container">
#                   <div class="row">
#                     <div class="col-lg-12 text-center">
#                       <h2 name="contactme" class="section_header">CONTACT US</h2><br>
#                     </div>
#                   </div>
#                   <div class="row">
#                     <form action="contact_us.php" method="post" id="contact_form">
#                       <input name="first_name" type="text" class="feedback-input" placeholder="First Name">
#                       <input name="last_name" type="text" class="feedback-input" placeholder="Last Name">
#                       <input name="email" type="text" class="feedback-input" placeholder="Email Address">
#                       <textarea name="message" class="feedback-input" placeholder="Comments"></textarea><br>
#                       <div id="form_buttons" class="text-center">
#                         <input class="contact_button" type="reset" value="RESET">
#                         <input class="contact_button" type="submit" value="SUBMIT">
#                       </div>
#                     </form>
#                   </div>
#                   </div>
#               </section>

# Setup the browser
# opening the url

# Program 1
# id
driver = webdriver.Chrome()
# driver.get('https://webdriveruniversity.com/Contact-Us/contactus.html')
# section_we = driver.find_element(By.ID,'contact_me')
# avail = section_we.is_displayed()
# if avail:
#     print("test case passs")
# else:
#     print("test case fail")
#
#
# # Program 2
# #byClassName
# #classELement = driver.find_element(By.CLASS_NAME,"contact_us")
# classELements = driver.find_elements(By.CLASS_NAME,"contact_us")
# q1 = len(classELements)
# if( q1 == 2):
#     print("Test case pass")
# else:
#     print("Test case fail")
#
# # program 3
# #byTagName
# form_element = driver.find_element(By.TAG_NAME , 'form')
# if(form_element.is_displayed()):
#     print("Testcase pass")
# else:
#     print("Testcase fail")
#
# # Css selector
# # tagName[attribute = 'value']4
#
# byCss = driver.find_element(By.CSS_SELECTOR,'input[name="first_name"]')
# if(byCss.is_displayed()):
#     print("Testcase pass")
# else:
#     print("Testcase fail")
#
#
# # Xpath
# #//tagName[@attribute = 'value']
# byXpath = driver.find_element(By.XPATH,'//input[@name="first_name"]')
# if(byXpath.is_displayed()):
#     print("Testcase pass")
# else:
#     print("Testcase fail")
#

# LinkText
# driver.get('https://webdriveruniversity.com/')
# byLinkText = driver.find_element(By.LINK_TEXT, 'Cypress with Cucumber BDD - Beginner to Expert in 9 Hours!')
# if(byLinkText.is_displayed()):
#     print("Test case pass")
# else:
#     print('Test case fail')
#
#
# #Partial LinkText
# driver.get('https://webdriveruniversity.com/')
# byPLinkText = driver.find_element(By.PARTIAL_LINK_TEXT, 'Cypress with Cucumber BDD')
# if(byPLinkText.is_displayed()):
#     print("Test case pass")
# else:
#     print('Test case fail')


