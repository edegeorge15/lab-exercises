#!/usr/bin/env python
# coding: utf-8

# 1. Follow the 3rd Selenium tutorial on your own. Submit the correct code with comments explaining what each element is doing (5pts)
# 

# In[ ]:


#1

#importing modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#local path to file on my computer
PATH = "~/Documents/chromedriver_mac_arm64.zip"
driver = webdriver.Chrome(executable_path=PATH) #connecting to webdriver
driver.get("https://techwithtim.net")
 
link = driver.find_element("link text", "Python Programming")
link.click() #loads the main page and then clicks 
#the link and goes to Python Programming

#need to wait for the element to exist before we can click on it
#using try element
try:
    element = WebDriverWait(driver, 10).until( #waits for up to 10 seconds for 
        #the driver to find an element on the page -- Beginner Python Tutorials
    EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click() #goes to the next page
    
    element = WebDriverWait(driver, 10).until( #waits for up to 10 seconds for 
        #the driver to find an element on the page --get started button
    EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    element.click() #hits get started button
    
    driver.back() #goes back to the previous page
    driver.back()
    driver.back() #goes back to home page
    driver.forward() #goes forward a page
    driver.forward() 
    
except: #use except--don't want it to quit unless it doesn't work
    driver.quit() #quits whole tab


# In[2]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# 2. Take what we learned today & try to scrape another website. (5pts)
# 
# Use selenium to search https://www.wikipedia.org/ for the word “cat” and then scrape the url links to all the images on the page. Store those in a csv file. (Bonus 1pt can you add the https:// part of the url to the links so they are clickable)
# 

# In[10]:


from bs4 import BeautifulSoup
import requests
import html5lib
import csv
import pandas as pd

PATH = "~/Documents/chromedriver_mac_arm64.zip"
driver = webdriver.Chrome(executable_path=PATH)
driver.get("https://www.wikipedia.org/")
search = driver.find_element(By.ID, "searchInput") 
search.send_keys("cat")
search.send_keys(Keys.RETURN)


# In[11]:


csv_file = open("image_links.csv", "w", newline="", encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Cat Image URLs"])
source = requests.get("https://en.wikipedia.org/wiki/Cat").text
soup = BeautifulSoup(source, "lxml")


for element in soup.find_all("div", class_="thumbimage"):
    images = element.find("a", href=True).get("href")
    print("https://en.wikiquote.org" + images)     
    csv_writer.writerow([images])
    
csv_file.close()


# In[5]:


sheet = pd.read_csv("image_links.csv")
sheet


# In[ ]:




