from collidable import Collidable
from turtle import Turtle
import random
from screen_constants import *


class Ball(Collidable):
    def __init__(self, snake, score):
        self.eater_snake = snake
        self.score = score
        self.ball = Turtle(shape="circle")
        self.ball.penup()
        self.ball.color("white")
        self.ball.setx(random.randint(LEFT_EDGE + 20, RIGHT_EDGE - 20))
        self.ball.sety(random.randint(DOWN_EDGE + 20, UP_EDGE - 20))


    def change_position(self):
        self.ball.setx(random.randint(LEFT_EDGE + 20, RIGHT_EDGE - 20))
        self.ball.sety(random.randint(DOWN_EDGE + 20, UP_EDGE - 20))

    def check_hit(self):
        snake_head = self.eater_snake.get_head()
        x_differance = abs(snake_head.xcor() - self.ball.xcor())
        y_differance = abs(snake_head.ycor() - self.ball.ycor())
        if x_differance < 15 and y_differance < 15:
            self.hit()
            return True
        return False

    def hit(self):
        self.change_position()
        self.eater_snake.hit()
        self.score.update_score()

