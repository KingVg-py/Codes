import turtle
import math


screen=turtle.getscreen()
screen.bgcolor("Cyan")

pen=turtle.Turtle()
pen.shape("triangle")
pen.speed(100)


size=float(input("What size should the tree be: "))

def tree_trunk():

 step1=(size**2)-((size/2)**2)
 trunksize=math.sqrt(step1)
 pen.up()
 pen.color("brown")
 pen.goto(0,0-trunksize)

 
 pen.down()

 #draws tree trunk
 pen.begin_fill()
 pen.setheading(0)
 pen.goto(size/6,0-trunksize)
 pen.right(90)
 pen.forward(size/2)
 pen.right(90)
 pen.forward(size/3)
 pen.right(90)
 pen.forward(size/2)
 pen.goto(0,0-trunksize)
 pen.end_fill()


def tree_leaves():

 leafsize=size
 pen.color("forest green")
 count=0

 pen.setheading(0)

 Xpos=0
 Ypos=0
 while count!=5:
     count=count+1

     pen.begin_fill()
     pen.up()
     pen.goto(Xpos,Ypos)

     pen.down()
     pen.right(60)
     pen.forward(leafsize)
     pen.right(120)
     pen.forward(leafsize)
     pen.right(120)
     pen.forward(leafsize)
     pen.end_fill()

     step1=(size**2)-((size/2)**2)
     step2=math.sqrt(step1)
     Ypos=Ypos+(step2/4)

     pen.setheading(0)

     leafsize=leafsize-(leafsize/4)


def star():
    Ypos=0
    for i in range (0,5):
        step1=(size**2)-((size/2)**2)
        step2=math.sqrt(step1)
        Ypos=Ypos+(step2/4)

        star_size=size-(size/1.5)
    
    pen.up()
    pen.goto(0+(star_size/2),Ypos-(star_size/3))

    
    pen.color("yellow")
    pen.down()

    pen.begin_fill()

    for z in range(0,5):
        pen.right(144)
        pen.forward(star_size)
        
    
    pen.end_fill()

def message():
    
    step1=(size**2)-((size/2)**2)
    pos=math.sqrt(step1)
    pen.up()
    pen.color("red")
    pen.goto(0-size/2,0-pos-size/1.3)

    pen.write("Merry Christmas!",font=(size*100))


tree_trunk()
tree_leaves()
star()
message()
       

        
