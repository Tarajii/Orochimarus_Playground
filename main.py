import random
from scoreboard import Scoreboard as S
import time
from turtle import Screen, Turtle as t
from snake import Snake, USnake

list = []
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Orochimaru Game")
# screen.tracer(0)

a =  ["c"]

# Setup
scores = S()
snek = USnake(screen, scores)
screen.tracer(0)

# screen.onkey(key="w", fun=snek.forward)
# screen.onkey(key="a", fun=snek.left)
# screen.onkey(key="s", fun=snek.back)
# screen.onkey(key="d", fun=snek.right)

while abs(snek.list[0].xcor()) <= 300:
    screen.update()
    time.sleep(0.2)

    # while loop movement in snek class
    snek.move()

    if abs(snek.list[0].ycor()) >= 290 or abs(snek.list[0].xcor()) >= 290:
        over = t()
        over.color("white")
        over.write(f"Game Over", align = "center" ,font = ("Arial",30,"normal"))
        break

screen.exitonclick()