from opening_screen import Opening_screen
from game import Game
from turtle import Screen
from screen_constants import *

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
screen.title("Snake game!")

opening = Opening_screen(screen)
color = opening.run()
screen.resetscreen()
game = Game(color, screen)
game.game_play()




screen.exitonclick()

