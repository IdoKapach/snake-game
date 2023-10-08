from turtle import Screen
from snake import Snake
from ball import  Ball
from score import Score
from screen_constants import *
class Game():
    def __init__(self, color, screen):
        self.snake_color = color
        # self.screen = Screen()
        # self.screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
        # self.screen.bgcolor("black")
        # self.screen.tracer(0)
        # self.screen.listen()
        # self.screen.title("Snake game!")
        self.screen = screen

        self.snake = Snake(self.snake_color)
        self.score = Score()
        self.ball = Ball(self.snake, self.score)

        self.screen.onkey(fun=self.snake.up, key="Up")
        self.screen.onkey(fun=self.snake.down, key="Down")
        self.screen.onkey(fun=self.snake.right, key="Right")
        self.screen.onkey(fun=self.snake.left, key="Left")
        self.screen.onkey(fun=self.screen.bye, key="q")
        self.screen.onkey(fun=self.replay, key="space")

    def game_play(self):
        while True:
            self.snake.move_forward()
            self.ball.check_hit()
            self.screen.update()
            if self.snake.check_hit():
                break

        self.score.end_game()
        self.screen.exitonclick()

    def replay(self):
        self.screen.resetscreen()
        self.snake = Snake(self.snake_color)
        self.score = Score()
        self.ball = Ball(self.snake, self.score)
        self.screen.onkey(fun=self.snake.up, key="Up")
        self.screen.onkey(fun=self.snake.down, key="Down")
        self.screen.onkey(fun=self.snake.right, key="Right")
        self.screen.onkey(fun=self.snake.left, key="Left")
        self.game_play()

    def __main__(self):
        self.game_play()






