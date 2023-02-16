import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self, screen):
        super().__init__(shape="circle")

        self.color("red")
        self.penup()
        self.move()
        self.screen = screen

    def move(self):
        self.goto(random.randint(-290, 291), random.randint(-290, 291))

    def is_collision(self, x, y):
        ax = x
        ay = y

        bx = self.xcor()
        by = self.ycor()

        if abs(ax - bx) < 19 and abs(ay - by) < 19:
            print(f"We Collided Bitches!: ax:{ax} bx{bx} ay:{ay} by{by}")
            self.move()
            self.screen.update()
            return 1

        return 0
