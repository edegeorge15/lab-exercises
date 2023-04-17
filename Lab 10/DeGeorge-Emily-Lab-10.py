#!/usr/bin/env python
# coding: utf-8

# GUI #1 (5pts)
# Using the quotes API, build a GUI that provides a drop-down menu of people randomly chosen from the API
# 
# I want a user to be able to pick from that list and receive a quote that corresponds to that person
# 
# Ideally, I want to be able to reset that menu & allow people to choose from a new list 

# In[1]:


import requests
from tkinter import *
from tkinter import font

root = Tk()
root.title("Quotes")
root.geometry("600x400")

# function to get a quote by a specific author
def get_quote_by_author(author, text_box):
    text_box.delete(0.0, END)
    r = requests.get(f"https://api.quotable.io/quotes?author={author}")
    data = r.json()
    if "results" in data:
        quote = data["results"][0]["content"]
        text_box.insert(END, quote)
        author_var.set(author)  # Update the value of author_var
    else:
        text_box.insert(END, "No quotes found for this author.")

# function to generate a new list of authors
def generate_authors():
    r = requests.get("https://api.quotable.io/authors?limit=50")
    data = r.json()
    authors = [author["name"] for author in data["results"]]
    return authors

# function to create a dropdown menu of authors
def create_dropdown_menu():
    global author_dropdown
    authors = generate_authors()
    author_var.set(authors[0])
    author_dropdown = OptionMenu(root, author_var, *authors)
    author_dropdown.pack()

# function to reset the dropdown menu and get a new quote
def reset():
    author_dropdown.pack_forget()
    create_dropdown_menu()
    get_quote_by_author(author_var.get(), text_box)

# initial setup
author_var = StringVar()
create_dropdown_menu()
text_box = Text(root, font= "Elephant", height=4, width=30, bg="light blue", padx=30, pady=50)
get_button = Button(root, text="click to get a quote", command=lambda:get_quote_by_author(author_var.get(), text_box))
reset_button = Button(root, text="reset", command=reset)

# packing the widgets
intro_label = Label(root, text="Here is an inspirational quote for you.")
intro_label.pack()
text_box.pack()
get_button.pack()
reset_button.pack()

root.mainloop()


# GUI #2 (5pts)
# Go back to the weather API we used a few weeks ago and build a GUI that displays the 7 day forecast. Model it off of the weather forecaster you typically use (like an app or weather.com) 
# Try using one widget we haven’t yet used in class – identify it with a comment  

# In[2]:


import requests
import tkinter as tk
from tkinter import font

# latitude and longitude coordinates for New York City (40.7128° N, 74.0060° W)
url = "https://api.weather.gov/gridpoints/OKX/33,37/forecast"

# function to get forecast data from the API
def get_forecast():
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        forecast_data = data["properties"]["periods"]
        update_forecast_gui(forecast_data)
    else:
        forecast_listbox.delete(0, END)
        forecast_listbox.insert(END, "Error fetching forecast data")

# function to update GUI with forecast data
def update_forecast_gui(forecast_data):
    forecast_listbox.delete(0, END)
    for period in forecast_data:
        period_str = f"{period['name']}: {period['detailedForecast']}"
        forecast_listbox.insert(END, period_str)


root = tk.Tk()
root.title("7-Day Forecast")
root.geometry("800x600")

# using a listbox widget
forecast_listbox = tk.Listbox(root, font=font.Font(size=14))
forecast_listbox.pack(fill="both", expand=True)

refresh_button = tk.Button(root, text="Refresh", command=get_forecast)
refresh_button.pack(side="bottom", pady=10)

get_forecast()

root.mainloop()


# In[ ]:




