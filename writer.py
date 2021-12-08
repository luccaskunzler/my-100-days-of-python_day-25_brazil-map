from turtle import Turtle
FONT_TEXT = ('Arial', 12, 'normal')
FONT_SCORE = ('Arial', 24, 'normal')


class Writer(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('black')

    def go_print(self,coordinates, string):
        self.goto(coordinates)
        self.write(string, align='left', font=FONT_TEXT)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.color('black')
        self.hideturtle()
        self.goto(0,320)
        self.print_score()

    def print_score(self):
        self.write(f"Your current score is {self.score}/27", align='center', font=FONT_SCORE)

    def update_score(self):
        self.clear()
        self.score += 1
        self.print_score()

    def congrats(self):
        self.clear()
        self.write("Congratulations! You finished the game!", align='center', font=FONT_SCORE)
        self.goto(0,300)
        self.write("Click in the screen to exit", align='center', font=FONT_TEXT)

    def good_bye(self):
        self.color('white')
        self.goto(0, 0)
        self.write("GOOD BYE", align='center', font=('Arial', 40, 'normal'))
        self.goto(0, -30)
        self.write("Thanks for playing", align='center', font=('Arial', 20, 'normal'))
        self.goto(0, -60)
        self.write("Click in the screen to exit", align='center', font=('Arial', 20, 'normal'))