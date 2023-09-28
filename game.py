from turtle import Screen
from snake import Snake
from ball import  Ball
from score import Score

class Game():
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(600, 600)
        self.screen.bgcolor("black")
        self.screen.tracer(0)
        self.screen.listen()
        self.screen.title("Snake game!")

        self.snake = Snake()
        self.score = Score()
        self.ball = Ball(self.snake, self.score)

        self.screen.onkey(fun=self.snake.up, key="w")
        self.screen.onkey(fun=self.snake.down, key="s")
        self.screen.onkey(fun=self.snake.right, key="d")
        self.screen.onkey(fun=self.snake.left, key="a")
        self.screen.onkey(fun=self.screen.bye, key="p")
        self.screen.onkey(fun=self.replay, key="r")

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
        self.snake = Snake()
        self.score = Score()
        self.ball = Ball(self.snake, self.score)
        self.screen.onkey(fun=self.snake.up, key="w")
        self.screen.onkey(fun=self.snake.down, key="s")
        self.screen.onkey(fun=self.snake.right, key="d")
        self.screen.onkey(fun=self.snake.left, key="a")
        self.game_play()

    def __main__(self):
        self.game_play()






game = Game()
game.__main__()