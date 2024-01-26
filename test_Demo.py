import pytest
import time
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

@pytest.mark.homePage
def test_verify_title_home():
    driver = webdriver.Chrome()
    driver.get("https://webdriveruniversity.com/")
    actualTitle = driver.title
    assert actualTitle == "WebDriverUniversity.com"
    driver.quit()

@pytest.mark.homePage
def test_verify_url_home():
    driver = webdriver.Chrome()
    driver.get("https://webdriveruniversity.com/")
    actualUrl = driver.current_url
    assert "university" in actualUrl

@pytest.mark.contactPage
def test_verify_contact_us():
    driver = webdriver.Chrome()
    driver.get("https://webdriveruniversity.com/Contact-Us/contactus.html")
    actualTitle = driver.title
    assert actualTitle == "WebDriver | Contact Us"
    driver.quit()

@pytest.mark.contactPage
def test_verify_url_contact_us():
    driver = webdriver.Chrome()
    driver.get("https://webdriveruniversity.com/Contact-Us/contactus.html")
    actualUrl = driver.current_url
    assert "contactus" in actualUrl
    driver.quit()




