import turtle
import random

turtle.Screen()
turtle.hideturtle()
turtle.penup()


class Sierpinski:

    def __init__(self):
        self.d1x = random.randint(0, 300)
        self.d1y = random.randint(0, 300)
        self.d2x = random.randint(0, 300)
        self.d2y = random.randint(0, 300)
        self.d3x = random.randint(0, 300)
        self.d3y = random.randint(0, 300)
        self.dRx = random.randint(0, 300)
        self.dRy = random.randint(0, 300)

    def triangle(self):
        turtle.goto(self.d1x, self.d1y)
        turtle.dot(5)

        turtle.goto(self.d2x, self.d2y)
        turtle.dot(5)

        turtle.goto(self.d3x, self.d3y)
        turtle.dot(5)

    def random_dot(self):
        turtle.goto(self.dRx, self.dRy)
        turtle.dot(5)

    def sierpinski(self):
        while True:
            corner = random.randint(0, 2)

            if corner == 0:
                self.dRx = (self.d1x + self.dRx) / 2
                self.dRy = (self.d1y + self.dRy) / 2
                turtle.goto(self.dRx, self.dRy)
                turtle.dot(5)
            elif corner == 1:
                self.dRx = (self.d2x + self.dRx) / 2
                self.dRy = (self.d2y + self.dRy) / 2
                turtle.goto(self.dRx, self.dRy)
                turtle.dot(5)
            elif corner == 2:
                self.dRx = (self.d3x + self.dRx) / 2
                self.dRy = (self.d3y + self.dRy) / 2
                turtle.goto(self.dRx, self.dRy)
                turtle.dot(5)


sierpinskiTriangle = Sierpinski()
sierpinskiTriangle.triangle()
sierpinskiTriangle.random_dot()
sierpinskiTriangle.sierpinski()
turtle.done()
