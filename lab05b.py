import turtle
import time
import random
def draw_circle(x,y,red,green,blue,radius,pen):
    pen.goto(x, y)
    pen.color(red,green,blue)
    pen.begin_fill()
    turtle.circle(radius)
    pen.end_fill()
    pen.hideturtle()
    return;

def bullseye(x,y,pen):
    draw_circle(x,y,0,0,1,100,pen)
    draw_circle(x,y+20,1,1,1,80,pen)
    draw_circle(x,y+40,0,1,0,60,pen)
    draw_circle(x,y+60,1,1,1,40,pen)
    draw_circle(x,y+80,1,0,0,20,pen)    
    
