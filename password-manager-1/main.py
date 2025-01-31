from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_input = website_entry.get()
    email_input = email_entry.get()
    password_input = password_entry.get()

    if website_input == "" or email_input == "" or password_input == "":
        error_message()
    else:
        with open("data.txt", "a") as file:
            file.write(f"{website_input} | {email_input} | {password_input}\n")

    website_entry.delete(0,END)
    password_entry.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #

def error_message():
    messagebox.showinfo("Error!","Ensure you fill in all fields.")

window = Tk()
window.title("Password Manager")
window.config(padx=25,pady=25)

logo_img = PhotoImage(file="logo.png")
canvas = Canvas(height=200,width=200)
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)

website_label = Label(text="Website:")
website_label.grid(column=0,row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(string="robinsonbt.blue@gmail.com",index=0)

password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

password_entry = Entry(width=25,show="*")
password_entry.grid(column=1,row=3)

generate = Button(text="Generate Password",width=14,command=generate_password)
generate.grid(column=2,row=3)

add_button = Button(text="Add",width=36,command=save_password)
add_button.grid(column=1,row=4,columnspan=2)

window.mainloop()