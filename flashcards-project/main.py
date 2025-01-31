from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
flip_state = "German"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
    dict_data = data.to_dict(orient="records")
except FileNotFoundError:
    original_data = pandas.read_csv("data/german_words.csv")
    dict_data = original_data.to_dict(orient="records")
print(dict_data)


def next_card():
    global card, flip_state
    if not dict_data:
        canvas.itemconfig(card_title, text="All Done!", fill="black")
        canvas.itemconfig(card_text, text="You know all words!", fill="black")
        canvas.itemconfig(card_image, image=card_front_image)
        return

    card = random.choice(dict_data)

    canvas.itemconfig(card_image, image=card_front_image)
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_text, text=card["German"], fill="black")

    flip_state = "German"
    flip.place(x=350, y=600)


def flip_card():
    global flip_state, card
    if flip_state == "German":
        canvas.itemconfig(card_image, image=card_back_image)
        canvas.itemconfig(card_title, text="English", fill="white")
        canvas.itemconfig(card_text, text=card["English"], fill="white")
        flip_state = "English"
    else:
        canvas.itemconfig(card_image, image=card_front_image)
        canvas.itemconfig(card_title, text="German", fill="black")
        canvas.itemconfig(card_text, text=card["German"], fill="black")
        flip_state = "German"


def is_known():
    global dict_data, card
    dict_data.remove(card)
    new_data = pandas.DataFrame(dict_data)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flash!")
window.configure(bg=BACKGROUND_COLOR, width=1000, height=800, padx=50, pady=50)

card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="Welcome!", font=("Ariel", 40, "italic"))
card_text = canvas.create_text(400, 263, text="Click a button.", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

no_image = PhotoImage(file="images/wrong.png")
no_button = Button(image=no_image, highlightthickness=0, command=next_card)
no_button.grid(column=0, row=1)

yes_image = PhotoImage(file="images/right.png")
yes_button = Button(image=yes_image, highlightthickness=0, command=is_known)
yes_button.grid(column=1, row=1)

flip = Button(text="FLIP", bd=10, height=2, width=10, command=flip_card)

next_card()

window.mainloop()
