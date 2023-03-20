#!/usr/bin/env python
# coding: utf-8

# # Lab 7

# In[62]:


import requests
import json

lat = "42.098701"
lon = "-75.912537"
genius = requests.get(f'https://api.weather.gov/points/{lat},{lon}')

json_file = genius.json()

forecast = json_file["properties"]["forecast"]
new_request = requests.get(forecast)

json = new_request.json()

specific_forecast = json["properties"]["periods"]

for i in specific_forecast:
    print(i["name"])
    print(i["temperature"])
    print(i["detailedForecast"])
    


# Use our weather data we covered in Monday’s class and covert those three elements (day, temp, description) into a CSV (1pt). 

# In[63]:


# converting weather data into CSV

import requests
import json
import csv

lat = "42.098701"
lon = "-75.912537"
genius = requests.get(f'https://api.weather.gov/points/{lat},{lon}')

json_file = genius.json()

forecast = json_file["properties"]["forecast"]
new_request = requests.get(forecast)

json_data = new_request.json()

specific_forecast = json_data["properties"]["periods"]

data_file = open("weather_data.csv", "w", newline="", encoding="utf-8")
csv_writer = csv.writer(data_file)
csv_writer.writerow(["Name", "Temperature", "Detailed Forecast"])

for i in specific_forecast:
    name = i["name"]
    temp = i["temperature"]
    detailed = i["detailedForecast"]
        
    csv_writer.writerow([name, temp, detailed])
        
data_file.close()


# In[7]:


sheet = pd.read_csv("weather_data.csv")
sheet


# Using the techniques covered in this slide deck, convert that CSV into a bar graph – y axis should be the temperature, x axis should be the day (3pts)

# In[5]:


from matplotlib import pyplot as plt
import numpy as np

names = []
temperatures = []

for i in specific_forecast:
    names.append(i["name"])
    temperatures.append(i["temperature"])

fig = plt.figure(figsize = (10, 7))

bar_width = .5
plt.bar(names, temperatures, width=bar_width)

plt.xlabel("Day")
plt.ylabel("Temperature")
plt.title("Weather data")


plt.show()


# Read through the documentation of this public holiday API. There are seven different calls listed there, use all seven of them. Use comments to explain how the API is working & what each call is accomplishing. (You’ll need to use country codes) (4pts). 

# In[78]:


#countryCode - get country info for the given country
# /api/v3/CountryInfo/{countryCode}

# AvailableCountries- get all available countries
# /api/v3/AvailableCountries

# LongWeekend - get long weekends for a given country
# /api/v3/LongWeekend/{year}/{countryCode}

# PublicHolidays - get public holidays
# /api/v3/PublicHolidays/{year}/{countryCode}

# IsTodayPublicHoliday - is today a public holiday
# /api/v3/IsTodayPublicHoliday/{countryCode}

# NextPublicHolidays - returns the upcoming public holidays for the next 365 days for the given country
# /api/v3/NextPublicHolidays/{countryCode}

# NextPublicHolidaysWorldwide - returns the upcoming public holidays for the next 7 days
# /api/v3/NextPublicHolidaysWorldwide

import requests
import json
    
url = "https://date.nager.at/api/v3"

# Making a GET request to the AvailableCountries to get a list of all available countries
response = requests.get(f"{url}/AvailableCountries")
countries = response.json()
countries


# In[77]:


# Making a GET request to the /CountryInfo/{countryCode}
# to get country info for the given country
country_code = 'us'
response = requests.get(f"{url}/CountryInfo/{country_code}")
info = response.json()
info


# In[76]:


# Making a GET request to the LongWeekend/{year}/{countryCode} 
#to get a list of long weekends for a given year and country code

response = requests.get(f"{url}/LongWeekend/{year}/{country_code}")
long_weekends = response.json()
long_weekends


# In[72]:


# Making a GET request to the PublicHolidays/{year}/{countryCode}
#to get a list of public holidays for a given year and country code

year = 2022
country_code = 'us'
response = requests.get(f"{url}/PublicHolidays/{year}/{country_code}")
holidays = response.json()
holidays


# In[82]:


# Making a GET request to /IsTodayPublicHoliday/{countryCode}
# to check if today is a public holiday

url = "https://date.nager.at/api/v3/IsTodayPublicHoliday/us?offset=0"
response = requests.get(url)
response


# In[74]:


# Making a GET request to the NextPublicHolidays/{countryCode}
#to return the upcoming public holidays for the next 365 days for the given country

country_code = 'gb' #united kingdom
response = requests.get(f"{url}/NextPublicHolidays/{country_code}")
next_holidays = response.json()
next_holidays


# In[75]:


# Making a GET request to the /NextPublicHolidaysWorldwide
# to return the upcoming public holidays for the next 7 days

response = requests.get(f"{url}/NextPublicHolidaysWorldwide")
next_worldwide = response.json()
next_worldwide


# Then I want you to build a program that gets public holiday info from 10 countries of your choosing in an efficient way.  Count the total number of holidays and store that info. (3pts) Be careful, some countries might not have holidays listed in the API!

# In[43]:


import requests
import json
import csv
import pandas as pd

url = "https://date.nager.at/api/v3"
country_codes = ['us', 'gb', 'ca', 'fr', 'de', 'au', 'nz', 'jp', 'cn', 'kr']

data_file = open("public_holidays.csv", "w", newline="", encoding="utf-8")
csv_writer = csv.writer(data_file)
csv_writer.writerow(["Country Code", "Total Holidays"])


for country_code in country_codes:
    url2 = f"{url}/PublicHolidays/2023/{country_code}"
    response = requests.get(url2)
    holidays = response.json()
    total_holidays = len(holidays)
    
    csv_writer.writerow([country_code, total_holidays])

data_file.close()


# In[46]:


sheet2 = pd.read_csv("public_holidays.csv")
sheet2


# Bonus (1pt) figure out how to make the days from the weather graph not crowd each other on the x axis. Comment the source you used 

# In[9]:


from matplotlib import pyplot as plt
import numpy as np

names = []
temperatures = []

for i in specific_forecast:
    names.append(i["name"])
    temperatures.append(i["temperature"])

fig = plt.figure(figsize = (10, 7))

plt.bar(names, temperatures)

plt.xlabel("Day")
plt.ylabel("Temperature")
plt.title("Weather data")

# source: https://stackoverflow.com/questions/10998621/rotate-axis-text-in-python-matplotlib
plt.xticks(rotation=45) # rotates the x-axis so that the strings are readable

plt.show()


# Bonus (2pts) create a bar graph to visualize the number of public holidays in the 10 countries you counted 

# In[45]:


import requests
import csv
import matplotlib.pyplot as plt

url = "https://date.nager.at/api/v3"
country_codes = ['us', 'gb', 'ca', 'fr', 'de', 'au', 'nz', 'jp', 'cn', 'kr']

countries = []
holiday_counts = []

for country_code in country_codes:
    url2 = f"{url}/PublicHolidays/2023/{country_code}"
    response = requests.get(url2)
    holidays = response.json()
    total_holidays = len(holidays)
    countries.append(country_code)
    holiday_counts.append(total_holidays)
    
    
fig = plt.figure(figsize = (10, 7))

plt.bar(countries, holiday_counts)
plt.xlabel("Country Code")
plt.ylabel("Number of Holidays")
plt.title("Number of Public Holidays in 2023")


plt.show()

