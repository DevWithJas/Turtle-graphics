import turtle

turtle.bgcolor("purple")
turtle.speed(0)
turtle.hideturtle()

colors = ["yellow", "green", "blue", "red", "orange" ,"violet","indigo"]

for i in range(500):
    for c in colors:
        turtle.color(c)
        turtle.forward(i)
        turtle.left(91)
        turtle.tracer(10)

turtle.mainloop()
