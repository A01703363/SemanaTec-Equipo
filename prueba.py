"""
import turtle
import random

squares = input("How many squares should I draw (whole numbers): ")
squares_int = int(squares)

def pick_color():
    colors = ["blue","black","brown","yellow","green","orange","beige","turquoise","pink"]
    random.shuffle(colors)
    return colors[0]

random_color = pick_color()
print(random_color)

length = 400
x = -200
y = 200

for i in range(squares_int):
    turtle.fillcolor(random_color)
    turtle.pensize(5)
    turtle.penup()
    turtle.setx(x)
    turtle.sety(y)
    turtle.pendown()
    turtle.down()
    turtle.begin_fill()
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.end_fill()
    turtle.up()

length = length - 30
x = x + 15
y = y - 15
"""
import turtle, random

colors  = ["red","green","blue","orange","purple","pink","yellow"] # Make a list of colors to picvk from

turtle.width(10) #What does this line do?

length = 5

for count in range(100):
  color = random.choice(colors) #Choose a random color
  turtle.forward(length)
  turtle.right(135)
  turtle.color(color) # Why is color spelt like this?
  length = length + 5