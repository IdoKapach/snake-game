from turtle import Turtle


class Score():

    def __init__(self):
        self.points = 0
        self.presenter = Turtle()
        self.presenter.penup()
        self.presenter.hideturtle()
        self.presenter.goto(0, 240)
        self.presenter.color("white")
        self.presenter.write(arg=f"score: {self.points}", move=False, align="center", font=("arial", 22, "normal"))

    def update_score(self):
        self.points += 1
        self.presenter.clear()
        self.presenter.write(arg=f"score: {self.points}", move=False, align="center", font=("Verdana", 22, "normal"))


    def end_game(self):
        self.presenter.clear()
        self.presenter.goto(0, 0)
        self.presenter.write(arg=f"   GAME OVER!\n your final score: {self.points}",
                             move=False, align="center", font=("arial", 30, "normal"))
        announcer = Turtle()
        announcer.hideturtle()
        announcer.color("white")
        announcer.goto(0, -100)
        announcer.write(arg=f"press 'r' for restart and 'p' for exit",
                             move=False, align="center", font=("arial", 20, "normal"))

