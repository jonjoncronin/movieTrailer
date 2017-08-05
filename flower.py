import turtle
import math

def draw_triangle(sprite):
    sprite.forward(60*math.sqrt(3))
    sprite.left(150)
    sprite.forward(120)
    sprite.left(120)
    sprite.forward(60)
    sprite.left(90)
    
def draw_art() :    
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.color("white")
    brad.speed(20)
    brad.left(90)
    brad.forward(300)
    for i in range(1,37):
        draw_triangle(brad) 
        brad.left(10)

    window.exitonclick()

draw_art()
