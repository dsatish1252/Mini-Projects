from turtle import Turtle


POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.inst = []
        self.create_snake()
        self.first = self.inst[0]

    def create_snake(self):
        for i in POS:
            self.addon(i)

    def addon(self, i):
        dany = Turtle("square")
        dany.color("white")
        dany.penup()
        dany.goto(i)
        self.inst.append(dany)

    def extend(self):
        self.addon(self.inst[-1].position())

    def move(self):
        for i in range(len(self.inst) - 1, 0, -1):
            new_x = self.inst[i - 1].xcor()
            new_y = self.inst[i - 1].ycor()
            self.inst[i].goto(new_x, new_y)
        self.inst[0].forward(MOVE)

    def up(self):
        if self.first.heading() != DOWN:
            self.first.setheading(UP)

    def down(self):
        if self.first.heading() != UP:
            self.first.setheading(DOWN)

    def left(self):
        if self.first.heading() != RIGHT:
            self.first.setheading(LEFT)

    def right(self):
        if self.first.heading() != LEFT:
            self.first.setheading(RIGHT)

    def se_pos(self):
        for i in self.inst:
            i.goto(700, 700)
        self.inst.clear()
        self.create_snake()
        self.first = self.inst[0]
