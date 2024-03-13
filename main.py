from tkinter import *
import tkinter as tk
import random
import json

from tkinter import messagebox

def close_window():
    root.destroy()

# Create the main window
root = Tk()
root.title("Typing Speed Test")
root.geometry("800x460+300+100")
root.wm_resizable(False,False)

#Background
background_image = tk.PhotoImage(file="./assets/car.png").subsample(5)
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

#Start Button, initial timer and end of timer
def start_timer():
    global remaining_time
    remaining_time = 3  # Initial countdown time
    update_timer()

i=0
def update_timer():
    global remaining_time,i
    minutes = remaining_time // 60
    seconds = remaining_time % 60
    timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
    if remaining_time > 0:
        remaining_time -= 1
        root.after(1000, update_timer)
    elif remaining_time == 0:
        if i == 1:
            messagebox.showinfo("Writing over", "Time's up!")  # Display popup message
            timer_label.config(text="00:00")
        remaining_time = 60  # Reset remaining time
        i+=1
        if i<2:
            update_timer()
            timer_label.config(text="01:00")



button_image = PhotoImage(file="./assets/start_button.png").subsample(7)
second_button = PhotoImage(file="./assets/result_button.png").subsample(16)
timer_label = tk.Label(root, text="00:00", font=("Helvetica", 24))
timer_label.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

start_button = tk.Button(root, text="Start Timer!",fg="black", highlightthickness=1,font='Helvetica 18 bold' ,image=button_image, command=start_timer, compound=LEFT)
start_button.grid(row=0,column=0,padx=5, sticky="w")




#Story to type
random_number = random.randrange(1,5)
chosen_story = str(random_number)

with open('stories.json', 'r') as file:
    stories = json.load(file)
    TEXT = stories[chosen_story]
story = tk.Label(root, text=TEXT, fg = "white", font = ("Times",16), width=60, height=10,  wraplength=450).grid(row=0,column=3,pady=1)

#Textbox
textbox = Text(root, height=20, width=60,fg="orange",font=("Times", 16),wrap= WORD)
textbox.grid(row=1,column=3)


#Get result button when timer runs out
### it should not count interpunction signs, if a word is added by accident
### how do i make the program ignore it
def get_result():
    global written_text
    written_text = textbox.get("1.0", "end-1c").upper()
    split_text = written_text.split()
    story_text = TEXT.upper()
    split_story = story_text.split()
    z=0
    for i in range(len(split_text)):
        if split_text[i] == split_story[i]:
            z+=1

    y = "Number of words per minute is: "
    x = y + str(z)
    messagebox.showinfo("Your result:" , x)


result_button = tk.Button(root,text="Get Result!", fg="black", highlightthickness=1,font='Helvetica 18 bold' ,image=second_button,compound=LEFT,command=get_result)
result_button.grid(row=1,column=0,padx=5)


# Run the Tkinter event loop
root.mainloop()