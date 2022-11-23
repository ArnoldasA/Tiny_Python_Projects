from tkinter import *
import read_cvs
import pandas
import random


window = Tk()
window.title("Flash Card App")
BACKGROUND_COLOR = "#B1DDC6"
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
current_card = {}
words_to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    words_to_learn = original_data.to_dict(orient="records")
else:
    words_to_learn = data.to_dict(orient="records")




def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)  # cancels the flip if we interacted with the window
    current_card = random.choice(words_to_learn)
    # print(current_card["French"])
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)  # our flip resets


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    words_to_learn.remove(current_card)  # If the user knows the word we remove it from the list of words
    data = pandas.DataFrame(words_to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()




flip_timer = window.after(3000, func=flip_card)

# UI
# Change to pack as this will solve all the issues
app_text = Label(window, text="French Flash Cards", font=("Garamond", 18), highlightthickness=0,
                 background=BACKGROUND_COLOR)
app_text.grid(column=1, row=0, columnspan=2)

# You can use canvas to create text and then assign its placement before declaring the grid to hold it
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 100, text="", font=("calibri", 45))
card_word = canvas.create_text(400, 263, text="", font=("calibri", 50))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=1, column=1, columnspan=2)
# Solution: column span was used , canvas text and padding on the window


# BTNS
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

# Close gap in the padding
right_btn = Button(image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, bd=0, command=is_known)
right_btn.grid(column=1, row=2)
wrong_btn = Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, bd=0, command=next_card)
wrong_btn.grid(column=2, row=2, )

# Pandas - retrieve the csv and populate your word with the csv word and title
next_card()

window.mainloop()
