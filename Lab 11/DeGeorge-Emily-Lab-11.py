#!/usr/bin/env python
# coding: utf-8

# Build on your code using mine as reference (or if you find something else, cite it). Things to add to make it fully operational:
# 
# (1) Integrate a clickable button that will make a new question appear
# 
# (2) Figure out a system of keeping track of points. 
# 
# (3) Display how many questions the player got right after all the questions have been gone through 
# 
# Will be graded on completion. Do as best as you can & get as many elements as possible. If you can’t get parts to work, explain in a comment why & what you tried. If you look up other code, CITE IT!
# 

# In[71]:


# trivia game that utilizes radio buttons, has pt system and final score listed
# my next step would be fixing the print out of the questions themselves; fixing the typos when quotes are involved etc.

from tkinter import *
import requests
import json
from tkinter import font

# using open trivia database bc I kept getting TypeError for Tkinter
# https://www.freecodecamp.org/news/how-to-create-a-gui-quiz-application-using-tkinter-and-open-trivia-db/

url = 'https://opentdb.com/api.php?amount=1&type=multiple'
root = Tk()
root.geometry("700x500")
root.title("Trivia Game")

score = 0

def generate_question():
    global score
    text_box.delete(1.0, END)
    r = requests.get(url)
    data = r.json()
    question = data['results'][0]['question']
    answer_choices = data['results'][0]['incorrect_answers']
    correct_answer = data['results'][0]['correct_answer']
    answer_choices.append(correct_answer)
    text_box.insert(END, question)
    # will reset the radio buttons once you click new question
    # https://python.hotexamples.com/examples/Tkinter/Frame/winfo_children/python-frame-winfo_children-method-examples.html
    for widget in root.winfo_children():
        if isinstance(widget, Radiobutton):
            widget.destroy()
    create_radio_buttons(answer_choices)
    question_var.set(correct_answer)
    result_label.config(text="")
    if score < 5:
        score_label.config(text=f"Score: {score}")
    else:
        result_label.config(text=f"Game Over! You got {score} out of 5 questions right.")

def create_radio_buttons(choices):
    global answer_var
    answer_var = StringVar()
    # use none to make variable empty bc it currently doesnt exist
    # https://stackoverflow.com/questions/7338501/python-assign-value-if-none-exists
    answer_var.set(None)
    for choice in choices:
        radio_button = Radiobutton(root, text=choice, variable=answer_var, value=choice)
        radio_button.pack()

def check_answer():
    global score
    user_answer = answer_var.get()
    correct_answer = question_var.get()
    if user_answer == correct_answer:
        message = "Correct!"
        score += 1
    else:
        message = f"Incorrect. The correct answer is {correct_answer}."
    result_label.config(text=message)
    # once the player has answered 5 questions, the game is over and a message is displayed with the final score
    if score < 5:
        score_label.config(text=f"Score: {score}")
    else:
        generate_question()

question_var = StringVar()
text_box = Text(root, font="Elephant", height=10, width=50, bg="pink", padx=30, pady=50)
get_button = Button(root, text="Get a question", command=generate_question)
check_answer_button = Button(root, text="Check Answer", command=check_answer)
result_label = Label(root, text="", font="Helvetica 12 bold")
score_label = Label(root, text=f"Score: {score}", font="Helvetica 12 bold")

intro_label = Label(root, text="Trivia question here:")
intro_label.pack()
text_box.pack()
get_button.pack()
check_answer_button.pack()
result_label.pack()
score_label.pack()

root.mainloop()


# In[ ]:




