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
        pen.up()
  

class Rectangular(object):
    def __init__(self, bottomleft=(-20,-10), topright=(20,10),fillcolor="", pencolor="black"):
        """
        rectangle bottomleft point at(x,y) and topright point at(x,y)
        """
        self.bottomleft= bottomleft
        self.topright= topright
        self.fillcolor, self.pencolor = fillcolor, pencolor

    def __str__(self):
        return "Rectangle( Bottom-left-point:%s  Top-right-point%s )" % (self.bottomleft,self.topright)


    def draw(self, pen):
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

    def draw(self, pen):
        pen.goto(self.point1)
        pen.seth(0)
        pen.color(self.pencolor, self.fillcolor)# sets pen color and fill color
        pen.begin_fill()
        pen.down()#starts drawing
        
        pen.goto(self.point1)
        pen.goto(self.point2)
        pen.goto(self.point3)
        
        pen.goto(self.point1)#returns pen to original point
        pen.end_fill()
        pen.up()

def day():
    pen = turtle.Turtle()
    print()
    print("Day time drawing: ")#left side of vertical

    sun_lines = [Line((-350,230),(-250,230)), Line((-300,280),(-300,180)) ,Line((-335,260),(-270,198)), Line((-335,200),(-270,268))]
    for line in sun_lines:
        print (line)
        line.draw(pen)
    
    sun_circle = Circle((-300, 200), 30, 'yellow', 'black')
    sun_circle.draw(pen)
    print(sun_circle)

    roof_triangle= Triangle((-100.0,80),(-65,135),(-30,80),'grey')
    roof_triangle.draw(pen)
    print(roof_triangle)

    rectangle= Rectangular((-100,0),(-30,80),'green', 'black')
    rectangle.draw(pen)
    print(rectangle)

    window1_rectangle= Rectangular((-90,50),(-70,60),'lightblue', 'black')
    window1_rectangle.draw(pen)
    print(window1_rectangle)

    door_rectangle= Rectangular((-60,0),(-40,60),'grey', 'black')
    door_rectangle.draw(pen)
    print(door_rectangle)

    doorhandle_circle = Circle((-45, 30), 3, 'blue', 'black')
    doorhandle_circle.draw(pen)
    print(doorhandle_circle)

    tree_rectangle= Rectangular((-240,0),(-228,65),'brown', 'black')
    tree_rectangle.draw(pen)
    print(tree_rectangle)

    tree1_circle = Circle((-247, 60), 30, 'darkgreen', 'black')
    tree1_circle.draw(pen)
    print(tree1_circle)

    tree2_circle = Circle((-220, 60), 25, 'green', 'black')
    tree2_circle.draw(pen)
    print(tree2_circle)

    tree3_circle = Circle((-230, 85), 22, 'lightgreen', 'black')
    tree3_circle.draw(pen)
    print(tree3_circle)
    pen.hideturtle()

def night():
    pen = turtle.Turtle()
    print()
    print("Night time drawing: ")#Right side of vertical
    
    moon_circle = Circle((300, 200), 30, 'darkblue', 'black')
    moon_circle.draw(pen)
    print(moon_circle)

    darkroof_triangle= Triangle((100.0,80),(65,135),(30,80),'darkgrey')
    darkroof_triangle.draw(pen)
    print(darkroof_triangle)

    darkrectangle= Rectangular((100,0),(30,80),'darkgreen', 'black')
    darkrectangle.draw(pen)
    print(darkrectangle)

    darkwindow1_rectangle= Rectangular((90,50),(70,60),'yellow', 'black')
    darkwindow1_rectangle.draw(pen)
    print(darkwindow1_rectangle)

    darkdoor_rectangle= Rectangular((60,0),(40,60),'darkgrey', 'black')
    darkdoor_rectangle.draw(pen)
    print(darkdoor_rectangle)

    darkdoorhandle_circle = Circle((45, 30), 3, 'black', 'black')
    darkdoorhandle_circle.draw(pen)
    print(darkdoorhandle_circle)

    darktree_rectangle= Rectangular((240,0),(228,65),'black', 'black')
    darktree_rectangle.draw(pen)
    print(darktree_rectangle)

    darktree1_circle = Circle((247, 60), 30, 'darkgreen', 'black')
    darktree1_circle.draw(pen)
    print(darktree1_circle)

    darktree2_circle = Circle((220, 60), 25, 'black', 'black')
    darktree2_circle.draw(pen)
    print(darktree2_circle)

    darktree3_circle = Circle((230, 85), 22, 'darkgreen', 'black')
    darktree3_circle.draw(pen)
    print(darktree3_circle)
    pen.hideturtle()
        

def main():
    pen = turtle.Turtle()
    pen.hideturtle()# uncomment to hide the turtle
    lines = [Line((0,-250),(0,250)), Line((-350,0), (350,0), "brown")]
    print("Axis: Brown(Hor.) Black(Ver.)")
    for line in lines:
        print (line)
        line.draw(pen)

    day()
    night()

    pen.color("black")
    pen.up()
    pen.goto(0,-200)
    pen.down()
    pen.write("Mirror               Universes", True, align="center", font=("Arial",15,"normal"))
    pen.up()
    pen.goto(0,-245)
    pen.down()
    pen.write("Light                 Dark", True, align="center", font=("Arial",15,"normal"))
    
    #pen.reset()#uncomment to reset the screen when finished drawing (sets turtle to center of window)


main()
