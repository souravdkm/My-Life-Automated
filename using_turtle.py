__author__ = 'Om Computers'

import turtle
import time


def drawSquare(someTurtle):
    for i in range(1,5):
        someTurtle.forward(100)
        someTurtle.right(90)

def drawArt():
    window = turtle.Screen()
    window.bgcolor("red")
    # Brad turtle draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    for i in range(1, 36):
        drawSquare(brad)
        brad.right(10)

    # angie turtle draws a circle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    window.exitonclick()

drawArt()