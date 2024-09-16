#TurtleGraphics.py
#Name: Jace Sanders
#Date: 9/16
#Assignment: Turtle

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)


def main():
    myTurtle = turtle.Turtle()
    # drawPolygon(myTurtle, 5) #draws a pentagon
hideturtle()
bob = turtle.Turtle()
def drawPentagon(myTurtle):
    for i in range(5):
        myTurtle.forward(100)
        myTurtle.left(72)
drawPentagon(bob)

    # drawPolygon(myTurtle, 8) #draws an octogon
hideturtle()
bob = turtle.Turtle()
def drawOctagon(myTurtle):
    for i in range(8):
        myTurtle.forward(50)
        myTurtle.left(45)
drawOctagon(bob)
    

    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
hideturtle()
bob = turtle.Turtle()
col = input("Enter color: ")
def drawSquare(myTurtle):
    for i in range(4):
        myTurtle.forward(100)
        myTurtle.right(90)
drawSquare(bob)
bob.penup()
bob.forward(50)
bob.pendown()
bob.begin_fill()
bob.fillcolor(col)
bob.right(90)
def drawSquare(myTurtle):
    for i in range(4):
        myTurtle.forward(50)
        myTurtle.left(90)
drawSquare(bob)
bob.end_fill()
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.
hideturtle()
bob = turtle.Turtle()
col = input("Enter color: ")
def drawSquare(myTurtle):
    for i in range(4):
        myTurtle.forward(100)
        myTurtle.right(90)
drawSquare(bob)
bob.fillcolor(col)
bob.begin_fill()
def drawSquare(myTurtle):
    for i in range(4):
        myTurtle.forward(50)
        myTurtle.right(90)
drawSquare(bob)
bob.end_fill()

    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
hideturtle()
def draw_square(t, size):
   for i in range(4):
       t.forward(size)
       t.left(90)
bob = turtle.Turtle()
sizevar = 1
for i in range(5):
   draw_square(bob, sizevar)
   sizevar += 20
   bob.penup()
   bob.backward(10)
   bob.right(90)
   bob.forward(10)
   bob.left(90)
   bob.pendown()

    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares
hideturtle()
def draw_square(t, size):
   for i in range(4):
       t.forward(size)
       t.left(90)
bob = turtle.Turtle()
sizevar = 1
for i in range(3):
   draw_square(bob, sizevar)
   sizevar += 20
   bob.penup()
   bob.backward(10)
   bob.right(90)
   bob.forward(10)
   bob.left(90)
   bob.pendown()

main()
