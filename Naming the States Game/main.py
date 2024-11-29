import turtle
import pandas as pd

# Load state data and create a list of state names
data = pd.read_csv('50_states.csv')
states_names = data["state"]
states_list = states_names.tolist()

# Set up screen and add map image
screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Set up turtle for writing state names
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

list_guessed_correctly = []

# Main game loop
while len(list_guessed_correctly) != 50:
    # Ask the user for a state name
    answer_state = (screen.textinput(
        title=f"{len(list_guessed_correctly)}/50 guessed correctly",
        prompt="What is another state's name?")).title()

    # Exit the game if "Exit" is typed
    if answer_state == "Exit":
        break

    # Check if the guess is correct and not already guessed
    if answer_state in states_list and answer_state not in list_guessed_correctly:
        index = states_list.index(answer_state)
        x_coordinate = data["x"][index]
        y_coordinate = data["y"][index]
        writer.goto(x_coordinate, y_coordinate)
        writer.write(answer_state)
        list_guessed_correctly.append(answer_state)

# Find states that were missed
missed_states = [state for state in states_list if state not in list_guessed_correctly]

# Display results and save missed states
if len(missed_states) == 0:
    print("You won!!!")
else:
    print(f"You missed the following states: \n{missed_states}")

new_data = pd.DataFrame(missed_states)
new_data.to_csv('missed_states_to_learn.csv')

# Keep the screen open
screen.mainloop()
