from turtle import Turtle
import time
from collidable import Collidable
from screen_constants import *


STARTING_NUM_OF_RECTANGLES = 3
SNAKE_STEP = 20
class Snake(Collidable):
    def __init__(self, color):
        super().__init__()
        self.color = color
        self.time_per_iteration = 0.1
        self.rectangles_lst = []
        for i in range(STARTING_NUM_OF_RECTANGLES):
            rectangle = Turtle(shape="square")
            rectangle.color(self.color)
            rectangle.penup()
            self.rectangles_lst.append(rectangle)
        self.len = len(self.rectangles_lst)

    def add_rec(self):
        rectangle = Turtle(shape="square")
        rectangle.color(self.color)
        rectangle.penup()
        rectangle.goto(self.rectangles_lst[self.len - 1].xcor(), self.rectangles_lst[self.len - 1].ycor())
        self.rectangles_lst.append(rectangle)
        self.len += 1

    def move_forward(self):
        for i in range(self.len - 1, 0, -1):
            self.rectangles_lst[i].goto(self.rectangles_lst[i - 1].xcor(), self.rectangles_lst[i - 1].ycor())
        self.rectangles_lst[0].forward(SNAKE_STEP)
        time.sleep(self.time_per_iteration)

    def up(self):
        self.rectangles_lst[0].setheading(90)

    def down(self):
        self.rectangles_lst[0].setheading(270)

    def right(self):
        self.rectangles_lst[0].setheading(0)

    def left(self):
        self.rectangles_lst[0].setheading(180)

    def get_head(self):
        return self.rectangles_lst[0]

    def check_hit(self):
        # case 1 of hitting
        if not LEFT_EDGE < self.rectangles_lst[0].xcor() < RIGHT_EDGE:
            return True
        if not DOWN_EDGE < self.rectangles_lst[0].ycor() < UP_EDGE:
            return True
        # case 2 of hitting
        head = self.get_head()
        for rec in self.rectangles_lst[2:self.len]:
            x_differance = abs(head.xcor() - rec.xcor())
            y_differance = abs(head.ycor() - rec.ycor())
            if x_differance < 10 and y_differance < 10:
                return True
        return False

    def hit(self):
        self.add_rec()

