import turtle
turtle.title("Emoji")
sc = turtle.Screen()
sc.setup(400, 400)
root = turtle.Turtle()
root.penup()
root.setpos(5, -45)  # or goto
root.pendown()

root.begin_fill()
root.fillcolor("yellow")
root.circle(100)
root.end_fill()

root.up()
root.goto(-67, 20)
root.setheading(-120)
root.width(5)
root.down()
root.circle(80, -120)
root.setheading(60)
root.circle(80, -120)
root.fillcolor("black")


for i in range(-40, 105, 80):
    root.up()
    root.goto(i, 75)
    root.setheading(0)
    root.down()
    root.begin_fill()
    root.circle(10)
    root.end_fill()

turtle.mainloop()
