#!/usr/bin/env python
# coding: utf-8

# Go to https://www.binghamton-ny.gov/home
# Using an action chain – click the “Government” tab and click “Departments” in the top-left corner – use Xpaths to do this (4pts)
# 
# In a try/finally clause & WebDriverWait, click on the “Personnel/Civil Service” link, then click on the “Employment” link in the left menu – use Xpaths to do this (3pts)
# 
# Scrape the table of Job Openings – you can use Selenium or BeautifulSoup to do this (3pts)
# Put that data into a CSV file & read it with pandas (don’t forget to close the CSV file after you create it or it may not read in pandas!) 
# 

# In[22]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)



driver.get("https://www.binghamton-ny.gov/home")
menu = driver.find_element(By.XPATH, "//*[@id='dropdownrootitem3']/a")
submenu_dep = driver.find_element(By.XPATH, "//*[@id='dropdownrootitem3']/div/div/ul[1]/li/a")
actions = ActionChains(driver)
actions.move_to_element(menu)
actions.click(menu)
actions.click(submenu_dep)
actions.perform()

try:
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='leftNav_2_0_127']/ul/li/ul/li[14]/a[1]")))
    link.click()
    
    time.sleep(2)
    
    link2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='leftNav_1038_0_145']/ul/li/ul/li[14]/ul/li/a")))
    link2.click()
    
    time.sleep(2)
        
    rows=1+len(driver.find_elements(By.XPATH, "//*[@id='ColumnUserControl4']/div[2]/table/tbody/tr"))
    cols=len(driver.find_elements(By.XPATH, "//*[@id='ColumnUserControl4']/div[2]/table/tbody/th"))
    
    for r in range(2, rows+1):
         for p in range(1, cols+1):
            value = driver.find_elements(By.XPATH, "//*[@id='ColumnUserControl4']/div[2]/table/tbody/tr[“+str(r)+”]/td[“+str(p)+”]").text
            print(value, end='       ')  
            print()
    
    
finally:
    driver.quit()
    
    


# In[26]:


#scraping table using BeautifulSoup

import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.binghamton-ny.gov/government/departments/personnel-civil-service/employment"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table')
rows = table.find_all('tr')

#online help sourced from https://stackoverflow.com/questions/23377533/python-beautifulsoup-parsing-table
# and https://www.geeksforgeeks.org/scrape-table-from-website-using-python-selenium/
with open('Employment-Job-Openings.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    for row in rows:
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        writer.writerow(cols)


# In[ ]:


#scrap work-

#gov tab
(/*[@id="dropdownrootitem3"]/a)

#departments tab
(/*[@id="dropdownrootitem3"]/div/div/ul[1]/li/a)

#personnel/civil service link
(/*[@id="leftNav_2_0_127"]/ul/li/ul/li[14]/a[1])

#employment link
(/*[@id="leftNav_1038_0_145"]/ul/li/ul/li[14]/ul/li/a)

#job table
(/*[@id="ColumnUserControl4"]/div[2])
(/*[@id="ColumnUserControl4"]/div[2]/table)
(/*[@id="ColumnUserControl4"]/div[2]/table/tbody)

#job
(/*[@id="ColumnUserControl4"]/div[2]/table/tbody/tr[1]/td[1])

