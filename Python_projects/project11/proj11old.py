import random
import turtle
import time
from random import choice
from random import randrange

class Fishing(object):
    def Fish():
        #creating multiple types of object fish types and returning one of them
        Fish = ['Whale Shark','Jack','Blacktip Shark','Tarpon','Roosterfish','Yellowfin Tuna','Peacock Bass','Cubera Snapper','Barracuda','Snapper','Wahoo','Blue Marlin','Black Marlin','Striped Marlin','Sailfish','Dorado','Amberjack','Bluefin','Bonito','Corvina','Red Stripe Rockfish','Sierra Mackered','Grouper','Hammerhead Shark','Pompano']
        return choice(Fish)
    

class Carpet(object):
    def gotoandprint(x, y):
        turtle.goto(x, y)
        #time.sleep(10)
        print()
        print("Set hook:")
        print(turtle.xcor(), turtle.ycor())
        x=turtle.xcor()
        y=turtle.ycor()
        coordinate=[x,y]
        return coordinate

    def click_position(turtle):
        turtle.onscreenclick(Carpet.gotoandprint)
        x=turtle.xcor()
        y=turtle.ycor()
        return x,y
            
    def Draw_square(x,y,length_str):
        t=turtle
        t.title("Carpet fishing") #displays given text in turtle window(bar)
        #t.shape('Fish')
        t.penup()
        t.goto(x,y)
        t.pensize()
        t.setheading(0)
        #0:east,90:north,180:west,270:south
        t.pendown()
        t.speed(10)

        length=int(length_str)
        i=0
        for i in range(4):
            t.forward(length)
            t.left(90)
            i+=1
        t.penup()
        #t.ht()#hide turtle
        
    def Draw_carpet():
        while True:
            print("Type 'Q' or 'q' if you want to quit...")
            #try:
            squares=input("How wide would you like each grid square? (integer)")
            if squares=='Q' or squares== 'q':
                break
            width=input("How many grid squares wide is your carpet? (integer)")
            if width=='Q' or width== 'q':
                break
            length=input("How many grid squares long is your carpet? (integer)")
            if length=='Q' or length== 'q':
                break
            squares_int=int(squares)
            width_int=int(width)
            length_int=int(length)
            if width_int<0 or length_int<0 or squares_int<0:
                print("No negative values...")
            elif width_int==0 or length_int==0 or squares_int==0:
                print("Can't have a carpet of no width or no length or 0 width of a grid square")
            else:
                x=0#origin x value
                y=0
                
                lst_of_gridsquares=[]
                row_gridlst=[]

                k=0
                L=4
                for i in range(length_int):
                    for j in range(width_int):
                        Carpet.Draw_square(x,y,squares_int)
                        row_gridlst.append(x)
                        row_gridlst.append(y)
                        row_gridlst.append(x+squares_int)
                        row_gridlst.append(y+squares_int)
                        x+=squares_int#x change
                        turtle.goto(x,y) 
                    for h in range(length_int):
                        lst_of_gridsquares.append(row_gridlst[k:L])#appending a single squares x,y values from row_gridlst to lst_of_gridsquares
                        k+=4
                        L+=4
                        #print(row_gridlst[k:L])#That square in the row_gridlst
                        #print(lst_of_gridsquares)
                    row_gridlst=[]#setting that row's row_gridlst back to empty, doesn't need to be here to work correctly
                    k=0#setting the row_gridlst grab points for the square back to starting x value, only to be used when the row_gridlst is set back to empty, doesn't need to be here to work correctly
                    L=4#setting the row_gridlst grab points for the square back to starting x value, only to be used when the row_gridlst is set back to empty, doesn't need to be here to work correctly
                    y+=squares_int#y change
                    x=0#origin x value
                    turtle.goto(x,y)
                turtle.penup()
            print("Done Drawing Carpet...")
            break
        return lst_of_gridsquares

                        
            #except:
                #print("An error occured, please try again...")
                #pass

def main():
    grid_lst=Carpet.Draw_carpet()
    #print(grid_lst)#displays all the coordinate values that define the regions of grid squares

    fish=Fishing.Fish()
    #print(fish)#fish it chose
    #print(choice(fish))#shows how it picked what type fish
    random_index = randrange(0,len(grid_lst))#a.k.a fish square location, randomized

    
    cor_click=Carpet.click_position(turtle)
    fo=input("Click on the screen to set the hook for fishing, then enter ok")
    print(cor_click)
    x=grid_lst[random_index][0]
    y=grid_lst[random_index][1]
    b=grid_lst[random_index][2]
    a=grid_lst[random_index][3]
    print(x)
    print(y)
    print(b)
    print(a)

main()
