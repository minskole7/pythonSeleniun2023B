
import time
from selenium import  webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://webdriveruniversity.com/Data-Table/index.html")




# total number of rows
rows = driver.find_elements(By.XPATH,'//*[@id="t01"]/tbody/tr')
totalRows = len(rows)
print(totalRows)
# total number of columns

columns = driver.find_elements(By.XPATH,'//*[@id="t01"]/tbody/tr[2]/td')
totalColumns = len(columns)
print(totalColumns)


# Test case 1
# Iterate over every row and add the age to get the average
total = 0
for i in range(2,totalRows+1):
    age = driver.find_element(By.XPATH, f'//*[@id="t01"]/tbody/tr[{i}]/td[3]'.format()).text
    total = total + int(age)

print(total/totalRows)
if(total == 159):
    print('Test case pass')
else:
    print('Test case fail')

total = 0
for i in range(2,totalRows+1):
    age = driver.find_element(By.XPATH, f'//*[@id="t02"]/tbody/tr[{i}]/td[3]').text
    total = total + int(age)

print(total/totalRows)
if(total == 163):
    print('Test case pass')
else:
    print('Test case fail')

# Test case 2
# verify the user present with firstName michael
for i in range(2,totalRows+1):
    firtName = driver.find_element(By.XPATH, f'//*[@id="t01"]/tbody/tr[{i}]/td[1]').text
    if firtName == "Michael":
        print("Test case pass, michael found")
        break







#
#
# def getTotal(id,expectedTotal):
#     for i in range(2, totalRows + 1):
#         age = driver.find_element(By.XPATH, f'//*[@id="t0{id}"]/tbody/tr[{i}]/td[3]'.format()).text
#         total = total + int(age)
#
#     print(total / totalRows)
#     if (total == expectedTotal):
#         print('Test case pass')
#     else:
#         print('Test case fail')
#
# getTotal(1,159)
# getTotal(2,163)