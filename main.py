import time
import pandas
from turtle import Turtle, Screen
from writer import Writer, Score

screen = Screen()
screen.setup(width=681, height=750)
screen.title("Guess the names of Brazil States")
image = "./brazil.gif"
screen.addshape(image)
screen.tracer(0)

map = Turtle()
map.penup()
map.goto(0, 0)
map.shape(image)

writer = Writer()
current_score = Score()


data = pandas.read_csv("brazil_coordinates.csv")
# for row in data['Estado']:
#     writer.go_print((int(data['X'][data['Estado'] == row]), int(data['Y'][data['Estado'] == row])), str(row))
list_of_states = data['Estado'].to_list()

missing_states = list_of_states[:]
keep_playing = True
while current_score.score <= 26 and keep_playing:
    time.sleep(0.1)
    screen.update()
    user_input = screen.textinput("Name a State", "Example: Mar do Norte | No accents |\n Type 'exit' to leave")
    if user_input == "exit":
        keep_playing = False
        time.sleep(1)
        # cleans the screen, sets it to a black color so the good bye message can be printed
        screen.clear()
        screen.bgcolor('black')
        current_score.good_bye()
    elif user_input in list_of_states:
        if user_input == "Rio Grande do Norte":
            treated_input = "Rio Grande\n do Norte"
        else:
            treated_input = user_input
        current_state = data[data['Estado'] == treated_input]
        writer.go_print((int(current_state.X), int(current_state.Y)), treated_input)
        current_score.update_score()
        missing_states.remove(user_input)


if current_score.score == 27:
    current_score.congrats()

missing_states_dict = {
    'Estado':missing_states
}

missing_states_df = pandas.DataFrame(missing_states_dict)
missing_states_df.to_csv("missing_states.csv")
print(missing_states_df)

screen.exitonclick()

