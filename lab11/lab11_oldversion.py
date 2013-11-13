import math
import turtle
import string

class Line(object):
    """Line class"""
    def __init__(self, beg = (0.0, 0.0), end = (50.0, 0.0),pencolor = "black"):
        """
        create a line starting from the coordinates given by beg to
        the coordinates given by end
        """
        self.pencolor = pencolor
        self.beg = beg
        self.end = end
        self.tag = "Line"

    def __str__(self):
        return "%s(%s,%s)" % (self.tag,self.beg,self.end)

    def draw(self,pen):
        """draw the line using the provided pen"""
        pen.pencolor(self.pencolor)
        if pen.pos() != self.beg:
            pen.up()
            pen.goto(self.beg)
        pen.down()
        pen.goto(self.end)

class Circle(object):
    """Circle class"""
    
    def __init__(self, center = (0.0,0.0), r=50.0,fillcolor="", pencolor="black"):
        """
        circle with center (x,y) and radius r
        """
        self.center = center
        self.radius = r
        self.fillcolor, self.pencolor = fillcolor, pencolor

    def __str__(self):
        return "Circle( center:%s radius:%.1f )" % (self.center,self.radius)


    def draw(self, pen):
        pen.seth(0)
        pen.color(self.pencolor, self.fillcolor)
        if pen.pos() != self.center:
            pen.up()
            pen.goto(self.center)
            pen.down()
        if self.fillcolor: pen.begin_fill() #?????????? this if doesn't do anything????
        pen.circle(self.radius)
        pen.end_fill()
  

class Rectangular(object):
    def __init__(self, bottomleft=(-20.0,-10.0), topright=(20.0,10.0),fillcolor="", pencolor="black"):
        """
        rectangle bottomleft point at(x,y) and topright point at(x,y)
        """
        self.bottomleft= bottomleft
        self.topright= topright
        self.fillcolor, self.pencolor = fillcolor, pencolor

    def __str__(self):
        return "Rectangle( Bottom-left-point:%s  Top-right-point%s )" % (self.bottomleft,self.topright)


    def draw(self, pen):#draw starting from a center value???
        pen.goto(self.bottomleft)
        pen.seth(0)
        pen.color(self.pencolor, self.fillcolor)# sets pen color and fill color
        pen.begin_fill()
        pen.down()#starts drawing
        
        x=0#bottomleft x (x-value)
        y=0#bottomleft y (y-value)
        j=0#topright j (x-value)
        k=0#topright k (y-value)
        (x,y)=self.bottomleft#sets (x,y) to the coordinates given by the argument(bottom-left-point) passed by parameter
        (j,k)=self.topright#sets (j,k) to the coordinates top-right-point
        pen.setx(j)#moves pen by setting its current x value to the specified value j(subsequently top-right-points x value away from (0,0)
        pen.sety(k)
        pen.setx(x)
        pen.sety(y)
        pen.end_fill()
        pen.up()
        

class Triangle(object):
    def __init__( self, point1=(-50.0,0.0), point2=(0.0,50.0), point3=(50.0,0.0),fillcolor="blue", pencolor="black"):
        """
        Initialize an object of type Triangle with three points intialized.
        """
        self.point1=point1
        self.point2=point2
        self.point3=point3
        
        self.fillcolor, self.pencolor = fillcolor, pencolor
    def __str__(self):
        return "Triangle( point1:%s  point2:%s  point3:%s)" % (self.point1,self.point2,self.point3)
    
    def draw(self, pen, center = (0.0,0.0)):#draw starting from a center value
        pen.goto(center)#!
        pen.seth(0)
        pen.color(self.pencolor, self.fillcolor)# sets pen color and fill color
        pen.begin_fill()
        pen.down()#starts drawing
        (x,y)=center#!
        (a,b)=self.point1
        a=a-x
        b=b-y
        pen.goto((a,b))
        (c,d)=self.point2
        c=c+x
        d=d+y
        pen.goto((c,d))
        (e,f)=self.point3
        e=e+x
        f=f+y
        pen.goto((e,f))
        pen.goto((a,b))#returns pen to original point
        pen.end_fill()
        pen.up()
        

        

def main():
    pen = turtle.Turtle()
    
    lines = [Line((0,-250),(0,250)), Line((-350,0), (350,0), "red")]

    for line in lines:
        print (line)
        line.draw(pen)
    print

    circle = Circle((15.0, 20.0), 60, 'blue', 'black')
    circle.draw(pen)
    print(circle)

    rectangle= Rectangular((50.0,40.0),(20.0,10.0),'red', 'red')
    rectangle.draw(pen)
    print(rectangle)
    
    triangle= Triangle((-50.0,0.0),(0.0,50.0),(50.0,0.0),'green')
    triangle.draw(pen,(0.0,.0))
    triangle.draw(pen,(0.0,-50.0))#broken triangle
    print(triangle)
    #pen.hideturtle()   # uncomment to hide the turtle


main()
