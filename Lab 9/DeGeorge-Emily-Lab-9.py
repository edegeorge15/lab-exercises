#!/usr/bin/env python
# coding: utf-8

# Part 1: Use this CSV of AirBNB data from NYC [original source]
# 

# In[24]:


import pandas as pd
import csv
import seaborn as sns

df = pd.read_csv("AB_NYC_2019 - AB_NYC_2019.csv")
df


# write in a comment what could be some uses for this dataset (1pt), 
# 

# In[ ]:


# this dataset could be used to determine locations where airbnbs are most common, and in addition you coud determine which locations have the highest ratings or prices
# you could use the availability in some way to display which listings are available for renting


# 
# use a seaborn map to find all the NaN values (1pt), 
# 

# In[17]:


cols = df.columns 
sns.heatmap(df[cols].isnull()) 


# replace those NaN values (1pt), 

# In[21]:


df["last_review"] = df["last_review"].fillna("No date given")
df["reviews_per_month"] = df["reviews_per_month"].fillna("No value specified")


# In[22]:


cols = df.columns
sns.heatmap(df[cols].isnull())


# isolate just the year from the last_review column (1pt),

# In[23]:


df.last_review = df.last_review.str[0:4] 
df.last_review


# and do one other thing with the dataset of your choosing (1pt)

# In[25]:



AirBNB = df["neighbourhood_group"]
AirBNB_dict = {}

for i in AirBNB:
    if i not in AirBNB_dict:
        AirBNB_dict[i] =1
    else:
        AirBNB_dict[i] += 1

print(AirBNB_dict)


# Part 2: Try and create your own parser for an API. If you are using an API for your project, build one for it; if you are not, choose an API that makes sense to you or is related to your project in some way. Include at least five functions for 1pt each. 

# In[15]:


import requests

API_KEY = "faf19df899dae2e309c7803df05c0ea3"
BASE_URL = "https://api.themoviedb.org/3/movie/"

def get_response(endpoint):
    response = requests.get(endpoint)
    return response.json()

def get_top_rated_movies():
    url = f"{BASE_URL}top_rated?api_key={API_KEY}&language=en-US"
    return get_response(url)["results"]

def get_movie_details(movie_id):
    url = f"{BASE_URL}{movie_id}?api_key={API_KEY}&language=en-US"
    return get_response(url)

def get_movie_credits(movie_id):
    url = f"{BASE_URL}{movie_id}/credits?api_key={API_KEY}&language=en-US"
    return get_response(url)["cast"]

def get_movie_trailer(movie_id):
    url = f"{BASE_URL}{movie_id}/videos?api_key={API_KEY}&language=en-US"
    trailers = get_response(url)["results"]
    return trailers[0]["key"] if trailers else None

def print_top_rated_movies():
    for movie in get_top_rated_movies():
        print(movie["title"], movie["vote_average"])

def print_movie_details(movie_id):
    details = get_movie_details(movie_id)
    print("Title:", details["title"])
    print("Overview:", details["overview"])
    print("Release date:", details["release_date"])
    print("Runtime:", details["runtime"], "minutes")
    print("Genres:", ", ".join(genre["name"] for genre in details["genres"]))

def print_movie_credits(movie_id):
    credits = get_movie_credits(movie_id)
    print("Cast:")
    for credit in credits:
        print(credit["name"], "as", credit["character"])

def print_movie_trailer(movie_id):
    trailer_key = get_movie_trailer(movie_id)
    if trailer_key:
        print("Trailer URL:", f"https://www.youtube.com/watch?v={trailer_key}")
    else:
        print("No trailer available.")

# only calling get_movie_details function for the movie Jack Reacher using the movie ID
get_movie_details("343611")

