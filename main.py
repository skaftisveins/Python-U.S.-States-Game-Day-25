import pandas
import turtle

STOP_GAME = "Exit"

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.bgcolor("black")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read 50_states.csv
data = pandas.read_csv("50_states.csv")

# Geta all the states in state column and convert it to a list
all_states = data.state.to_list()
# Keep track of correct guessed states
guessed_states = []

running = True

while running:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/{len(all_states)} States Correct", prompt="What's another state's name?").title()

    def check_answer(guess, answer):
        """Return the guess and map the state name on screen if the guess matches any of the 50 states"""
        if (guess == None):
            return
        if (guess in answer):
            guessed_states.append(guess)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == guess]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(guess)
            return guess

    check_answer(answer_state, all_states)

    # List Comprehension
    # new_list = [new_item for n in numbers]

    def is_still_playing(guess):
        if (guess == STOP_GAME):
            missing_states = [state for state in all_states if state not in guessed_states]
            # missing_states = []
            # for state in all_states:
            #     if state not in guessed_states:
            # missing_states.append(state)
            learn_data = pandas.DataFrame(missing_states)
            learn_data.to_csv("States_to_learn.csv")

            running == False
            return guess

    is_still_playing(answer_state)

    if len(guessed_states) == 50:
        running == False


