import time
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import  ActionChains
from datetime import datetime


def select_date(driver,month,year,date):
    driver.find_element(By.ID,'datepicker').click()

    # Selecting month and year
    while True :
        actualMonthYear = driver.find_element(By.CLASS_NAME,"datepicker-switch").text
        print(actualMonthYear)
        monthA,yearA = actualMonthYear.split(" ")
        print(month)
        print(year)
        if(monthA == month and yearA == year):
            time.sleep(3)
            break
        driver.find_element(By.CLASS_NAME ,"next").click()

        # Selecting the date
        elements = driver.find_elements(By.CLASS_NAME,'day')
        for day in elements:
            if day.text == date:
                day.click()
                break

driver = webdriver.Chrome()
driver.get("https://webdriveruniversity.com/Datepicker/index.html")

# current_date = datetime.now().date()
# date_string = current_date.strftime("%Y-%m-%d")
# actualD = date_string.split("-")
# date = int(actualD) + 3
# #2023-12-

select_date(driver,"June","2024",20)
driver.close()