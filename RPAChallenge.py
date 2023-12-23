# In this python script we are going to take the python RPA challenge for automation Input Forms
# //----------------------------RPA CHALLENGE -INPUT FORMS -------------------------------//

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

excel = r"C:\Users\Mohan\Desktop\challenge.xlsx"
#read the excel file
df = pd.read_excel(excel)
driver = webdriver.Chrome()
url = "https://rpachallenge.com/"
driver.get(url)
time.sleep(2)
driver.maximize_window()


startbutton = driver.find_element(By.XPATH,"//button[normalize-space()='Start']").click()
print("Start button clicked...")

for index,row in df.iterrows():
    firstname1 = row['First Name']
    lastname1 = row['Last Name ']
    email1 = row['Email']
    companyname = row['Company Name']
    roleincompany1  = row['Role in Company']
    phonenumber1 = row['Phone Number']
    address1 = row['Address']
    driver.find_element(By.CSS_SELECTOR, "[ng-reflect-name=labelFirstName]").send_keys(firstname1)
    driver.find_element(By.CSS_SELECTOR, "[ng-reflect-name=labelLastName]").send_keys(lastname1)
    driver.find_element(By.CSS_SELECTOR, "[ng-reflect-name=labelEmail]").send_keys(email1)
    driver.find_element(By.CSS_SELECTOR, "[ng-reflect-name=labelCompanyName]").send_keys(companyname)
    driver.find_element(By.CSS_SELECTOR, "[ng-reflect-name=labelRole]").send_keys(roleincompany1)
    driver.find_element(By.CSS_SELECTOR, "[ng-reflect-name=labelPhone]").send_keys(phonenumber1)
    driver.find_element(By.CSS_SELECTOR, "[ng-reflect-name=labelAddress]").send_keys(address1)
    driver.find_element(By.XPATH, "//input[@value='Submit']").click()
    print("Submit button clicked")

# print("Enter first name for the once")
# driver.refresh()
# print("Page Refreshed...")
# time.sleep(3)
#
#
time.sleep(5)
driver.quit()
