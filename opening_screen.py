from turtle import Turtle, Screen
from screen_constants import *
from opening_snake import Opening_snake
from opening_announce import Opening_announce


class Opening_screen():

    def __init__(self, screen):
        self.snake = Opening_snake()
        self.announce = Opening_announce()
        self.screen = screen
        self.switch = "on"
        screen.listen()
        screen.onkey(key="Right", fun=self.snake.change_color)
        screen.onkey(key="Left", fun=self.snake.change_color_backwards)
        screen.onkey(key="space", fun=self.exit_opening)


    def run(self):
        while self.switch == "on":
            self.screen.update()
            self.snake.move()
        return self.snake.get_color()


    def exit_opening(self):
        self.switch = "off"



