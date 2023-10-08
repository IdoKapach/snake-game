import turtle

class Opening_announce(turtle.Turtle):
    def __init__(self):
        super(Opening_announce, self).__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 150)
        self.write(arg=f"welcome to snake game!\nchoose your snake's color",
                   move=False, align="center", font=("arial", 27, "normal"))

