from food import Food
from turtle import Screen, Turtle as t
from scoreboard import Scoreboard
# Movement F(n)
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

LEFT = 180
UP = 90
RIGHT = 0
DOWN = 270
DISTANCE = 20

class Snake:

    def __init__(self, screen):
        self.length = 0
        self.a = ["c"]
        self.list = []


        for x in range(0, 3):
            t1 = t(shape="square")
            t1.penup()
            t1.color("white")
            t1.goto(x*-20, 0)
            self.list.append(t1)
        # print(self.list)

    def forward(self):
        if self.a[0] == "b":
            return
        for x in range(len(self.list)-1, -1, -1):
            tur = self.list[x]

            if x == 0:
                tur.goto(tur.xcor(), tur.ycor()+20)
            else:
                tur.goto(self.list[x-1].pos())
        # screen.update()

        self.a[0] = "f"

    def back(self):
        if self.a[0] == "f":
            return

        for x in range(len(self.list)-1, -1, -1):
            tur = self.list[x]
            if x == 0:
                tur.goto(tur.xcor(), tur.ycor()-20)
            else:
                tur.goto(self.list[x-1].pos())
        self.a[0] = "b"

    def left(self):
        if self.a[0] == "r":
            return
        for x in range(len(self.list)-1, -1, -1):
            tur = self.list[x]
            if x == 0:
                tur.goto(tur.xcor()-20, tur.ycor())
            else:
                tur.goto(self.list[x-1].pos())

        self.a[0] = "l"

    def right(self):
        if self.a[0] == "l":
            return
        for x in range(len(self.list)-1, -1, -1):
            tur = self.list[x]
            if x == 0:
                tur.goto(tur.xcor()+20, tur.ycor())
            else:
                tur.goto(self.list[x-1].pos())

        self.a[0] = "r"

    def move(self):
        self.forward()

class USnake:

    def forward(self):
        lis = self.list[0]

        # north
        if self.heading == UP or self.heading == DOWN:
            return
        else:
            lis.setheading(UP)
            self.heading = UP

    def back(self):

        lis = self.list[0]

        # north
        if self.heading == DOWN or self.heading == UP:
            return
        else:
            lis.setheading(DOWN)
            self.heading = DOWN

    def left(self):
        lis = self.list[0]

        # left   or   right
        if self.heading ==  LEFT or self.heading == RIGHT:
            return
        else:
            lis.setheading(LEFT)
            self.heading = LEFT

    def right(self):
        lis = self.list[0]

        # left   or   right
        if self.heading ==  RIGHT or self.heading == LEFT:
            return
        else:
            lis.setheading(RIGHT)
            self.heading  = RIGHT

    def __init__(self, screen, scores):
        self.snack = Food(screen)
        self.list = []
        self.screen = screen
        self.screen.update()
        self.heading = RIGHT
        self.scores = scores

        for x in range(0, 3):
            t1 = t(shape="square")
            t1.penup()
            t1.color("white")
            t1.goto(x*-20, 0)
            self.list.append(t1)
        # print(self.list)

        # Setup screen to listen to this snake
        self.screen.listen()
        self.screen.onkey(key="Up",    fun=self.forward)
        self.screen.onkey(key="Down",  fun=self.back)
        self.screen.onkey(key="Left",  fun=self.left)
        self.screen.onkey(key="Right", fun=self.right)


    def move(self):
        for x in range( len(self.list)-1, 0, -1):
            if self.list[0].pos() == self.list[x-1].pos():
                print("You crashed You lost loser")
            lis = self.list[x]
            lis.goto(self.list[x-1].pos())
        lis = self.list[0]
        lis.forward(20)

        # check for collision
        if self.snack.is_collision(lis.xcor(), lis.ycor()):
            self.scores.inc_score()
            self.snack.move()
            add_clone = self.list[-1].clone()
            #add_clone.back(DISTANCE)
            self.screen.update()
            self.list.insert(len(self.list)-1, add_clone)



