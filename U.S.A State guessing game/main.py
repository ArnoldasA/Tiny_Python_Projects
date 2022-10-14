import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list() # We can directly convert csvs to lists
guessed_states = []
number_of_guessed_states = 0
while len(guessed_states) != len(all_states):
    answer_state = screen.textinput(title=f"{number_of_guessed_states}/50 States Correct", prompt="What's another state?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_To_Learn.csv")
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state] # This code ensures that we go to the right state pos
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        guessed_states.append(answer_state)
        number_of_guessed_states = len(guessed_states)








# from the 50 states csv read - compare if your answer to the csv and then whatever the coordinate is - set the
# turtle to that
