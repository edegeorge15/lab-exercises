#!/usr/bin/env python
# coding: utf-8

# Scrape this IMDB website of the top 100 movies 
# 
# Isolate the title, the date of release, and one other element of your choosing. (3pts) Put the data into a csv. (2pts)

# In[3]:


from bs4 import BeautifulSoup
import requests
import html5lib
import csv
import pandas as pd


source = requests.get("https://www.imdb.com/list/ls055592025/").text
soup = BeautifulSoup(source, "lxml")
print(soup)


# In[7]:


section2 = soup.find("span", class_= "lister-item-year text-muted unbold")
print(section2.prettify())


# In[8]:


section3 = soup.find("span", class_= "runtime")
print(section3.prettify())


# In[25]:


#1 - IMDB web scrape

csv_file = open("imdb_scrape_final.csv", "w", newline="", encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Title", "Date of Release", "Runtime"])


for element in soup.find_all("div", class_="lister-item-content"):
    
    title = element.h3.a.text.strip()
    print(title)

    date_release = element.find("span", class_= "lister-item-year text-muted unbold").text.strip()
    print(date_release)
    
    runtime = element.find("span", class_= "runtime").text.strip()
    print(runtime)
    
    
    csv_writer.writerow([title, date_release, runtime])
    
csv_file.close()


# In[27]:


sheet1 = pd.read_csv("IMDB_scrape.csv")
sheet1 


# Scrape this Library of Congress search
# 
# Scrape the first 5 pages, grab the title, item description, and webpage hyperlink. (3pts) Put the data into a csv. (2pts)
# Bonus 2pts: figure out how to isolate the contributor name & item date (*updated bonus as I had originally read HTML incorrectly – Dr. G)
# 

# In[2]:


from bs4 import BeautifulSoup
import requests
import html5lib
import csv
import pandas as pd

library = requests.get(f"https://www.loc.gov/search/?q=cats&sp=1").text
soup = BeautifulSoup(library, "lxml")
print(soup)


# In[4]:


section = soup.find("div", class_= "description")
print(section.prettify())


# Bonus 2pts: figure out how to isolate the contributor name & item date (*updated bonus as I had originally read HTML incorrectly – Dr. G)

# In[ ]:


#2 - Library of Congress web scrape

new_csv = open("LOC_scrape.csv", "w", newline="", encoding="utf-8")
csv_writer = csv.writer(new_csv)
csv_writer.writerow(["Title", "Item Description", "Webpage Hyperlink"])

page = 1

while page != 6:
    library = requests.get(f"https://www.loc.gov/search/?q=cats&sp={page}.html").text
    soup = BeautifulSoup(library, "lxml")
    
    for element in soup.find_all("div", class_="item-description"):
        title = element.span.a.text.strip()
        description = element.find("span", class_= "item-description-abstract").text.strip()
        
        
        try:
            hyperlink = element.find("a", href=True).get("href")
        except AttributeError:
            hyperlink = "No data listed"
        
        csv_writer.writerow([title, description, hyperlink])
        
        page += 1
        
    
csv_file.close()


# In[4]:


sheet2 = pd.read_csv("LOC_scrape.csv")
sheet2


# In[ ]:




