from turtle import Turtle
from enum import Enum
import time

class Positions(Enum):
    DOWN = 0
    NORMAL = 1
    UP = 2
    NORMAL1 = 4

NUM_OF_RECTANGLES = 6
COLORS = ["white", "blue", "red", "yellow", "green"]
TIME_PER_ITERATION = 0.1

class Opening_snake():
    def __init__(self):
        self.rectangles_lst = []
        self.color_index = 0
        self.position_mode = Positions.NORMAL
        for i in range(NUM_OF_RECTANGLES):
            rectangle = Turtle(shape="square")
            rectangle.color(COLORS[self.color_index])
            rectangle.penup()
            rectangle.goto(x=-50 + i * 20, y=-20 + 20 * self.position_mode.value)
            self.rectangles_lst.append(rectangle)
        self.color_index = 0

    def change_color(self):
        self.color_index = (self.color_index + 1) % len(COLORS)
        for rec in self.rectangles_lst:
            rec.color(COLORS[self.color_index])

    def change_color_backwards(self):
        if self.color_index == 0:
            self.color_index = len(COLORS) - 1
        else:
            self.color_index = (self.color_index - 1) % len(COLORS)
        for rec in self.rectangles_lst:
            rec.color(COLORS[self.color_index])

    def move(self):
        # sets position_mode
        if self.position_mode == Positions.NORMAL:
            self.position_mode = Positions.UP
        elif self.position_mode == Positions.UP:
            self.position_mode = Positions.NORMAL1
        elif self.position_mode == Positions.NORMAL1:
            self.position_mode = Positions.DOWN
        elif self.position_mode == Positions.DOWN:
            self.position_mode = Positions.NORMAL
        # setting the y position of each of the rectangles according to position_mode
        for i in range(NUM_OF_RECTANGLES - 1, 0, -1):
            self.rectangles_lst[i].sety(self.rectangles_lst[i - 1].ycor())
        self.rectangles_lst[0].sety(-8 + 8 * (self.position_mode.value % 3))
        time.sleep(TIME_PER_ITERATION)

    def get_color(self):
        return COLORS[self.color_index]




