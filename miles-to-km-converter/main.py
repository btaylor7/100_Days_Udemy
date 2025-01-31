from tkinter import *

def calculate_answer():
    user_input = entry.get()  # Get the input from the user
    try:
        # Attempt to convert the input to a float and calculate the result
        answer = float(user_input) * 1.609344
        result["text"] = f"{answer:.2f}"  # Set the result label to show the answer, formatted to 2 decimal places
    except ValueError:
        # Handle the case where the input is not a valid number
        result["text"] = "Invalid input (numbers only)"  # Show error message if input is not a number

window = Tk()
window.title("Miles to Kilometres")
window.config(padx=20,pady=20)

entry = Entry(width=20)
entry.insert(END,"Enter number in miles here")
entry.grid(column=1,row=0)

def on_click(event):
    # If the placeholder text is still present, clear it when the entry is clicked
    if entry.get() == "Enter number in miles here":
        entry.delete(0, END)  # Clear the entry box

# Function to restore placeholder text if the entry is left empty
def on_focus_out(event):
    # If the entry is left empty, restore the placeholder text
    if entry.get() == "":  # Check if the entry box is empty
        entry.insert(END, "Enter number in miles here")  # Reinsert placeholder text

# Bind the focus-in and focus-out events to the functions
entry.bind("<FocusIn>", on_click)  # Trigger on_click when the entry gains focus (clicked)
entry.bind("<FocusOut>", on_focus_out)  # Trigger on_focus_out when the entry loses focus

miles = Label(text="miles")
miles.grid(column=2,row=0)

is_equal = Label(text="is equal to ")
is_equal.grid(column=0,row=1)

result = Label(text="0")
result.grid(column=1,row=1)

km_label = Label(text="kilometres")
km_label.grid(column=2,row=1)

button = Button(text="Calculate",command=calculate_answer)
button.grid(column=1,row=2)

#miles to km = miles*1.609344

window.mainloop()
