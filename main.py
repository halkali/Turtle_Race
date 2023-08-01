import turtle
from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(height= 700, width= 900)

txt = turtle.textinput("Turtle", "who will be the winner:")

def rand():
    a = randint(10,20)
    return a

red = Turtle()
red.color("red")

blue = Turtle()
blue.color("blue")

green = Turtle()
green.color("green")

grey = Turtle()
grey.color("grey")

pink = Turtle()
pink.color("pink")

purple = Turtle()
purple.color("purple")

kap = [red,blue,green,grey,pink,purple]

y=-200
for i in kap:
    i.shape("turtle")
    i.speed("fastest")
    i.penup()
    i.goto(x=-420, y=y)
    y+=80

n = True
while n:
    for i in kap:

        if i.xcor() > 410.0:
            n = False
            if i.pencolor() == txt:
                print("you win!")
            else:
                print(f"you lose! the winner is {i.pencolor()}")
        else:
            i.forward(rand())














screen.exitonclick()

