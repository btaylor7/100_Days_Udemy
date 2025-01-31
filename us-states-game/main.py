import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()

had_answer = []

table = pandas.DataFrame(data)

def play_game():
    answer_state = screen.textinput(title="Name the States", prompt="Name as many as you can.?")
    while answer_state != "exit":
        answer_state = answer_state.strip().title()

        if answer_state.lower() in [state.lower() for state in state_list]:
            print(f"You got it! {answer_state} is in the list.")
            state_list.remove(answer_state)
            had_answer.append(answer_state)

            state_data = table[table["state"].str.lower() == answer_state.lower()]
            print(state_data)
            x = int(state_data["x"].values[0])
            y = int(state_data["y"].values[0])
            print(x, y)

            new_turtle = turtle.Turtle()
            new_turtle.hideturtle()
            new_turtle.penup()
            new_turtle.goto(x, y)
            new_turtle.write(answer_state)
        elif answer_state in had_answer:
            answer_state = screen.textinput(title="Name the States", prompt=f"You already had {answer_state}. Try again.")
            continue
        else:
            answer_state = screen.textinput(title="Name the States",prompt=f"That isn't a state (perhaps you misspelt it?) Try again.")
            continue

        answer_state = screen.textinput(title="Name the States", prompt="Name as many as you can.?")
        if answer_state is None:
            break


play_game()

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
#
# turtle.mainloop()