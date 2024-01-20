

import time
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import FluentWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome()
driver.get("https://webdriveruniversity.com/Autocomplete-TextField/autocomplete-textfield.html")

# static wait
# time.sleep(5)

#implicit wait (dynamic)
driver.implicitly_wait(10);
e = driver.find_element(By.CSS_SELECTOR,'h2[name="contactme"]')

# # explicit wait
# alertIsPresent()
# elementSelectionStateToBe()
# elementToBeClickable()
# elementToBeSelected()
# frameToBeAvaliableAndSwitchToIt()
# invisibilityOfTheElementLocated()
# invisibilityOfElementWithText()
# presenceOfAllElementsLocatedBy()
# presenceOfElementLocated()
# textToBePresentInElement()
# textToBePresentInElementLocated()
# textToBePresentInElementValue()
# titleIs()
# titleContains()
# visibilityOf()
# visibilityOfAllElements()
# visibilityOfAllElementsLocatedBy()
# visibilityOfElementLocated()

# explicit wait
wait = WebDriverWait(driver,12)
wait.until(expected_conditions.visibility_of_element_located(By.CSS_SELECTOR,'h2[name="contactme"]'));

# Fluent wait
wait = FluentWait(driver,timeout = 30,poll_frequency = 5 ,ignored_exceptions=[NoSuchElementException])
wait.until(expected_conditions.element_to_be_clickable(By.CSS_SELECTOR,"h2[name='contactme']"))