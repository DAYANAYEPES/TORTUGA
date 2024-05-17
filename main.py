import turtle

window = turtle.Screen()
window.bgcolor("black")
window.setup(width=700, height=700)

border = turtle.Turtle()
border.penup()
border.goto(-100, -100)
border.pendown()
border.pensize(4)

for i in range(4):
    border.forward(200)
    border.left(90)
border.hideturtle()

pulse = turtle.Turtle()
pulse.shape("turtle")
pulse.color("blue")
pulse.penup()
pulse.speed(0)
pulse.goto(0, 0)

pulse.dx = 3
pulse.dy = 2


x_limit = 100
y_limit = 100


def move_pulse():
    x, y = pulse.xcor(), pulse.ycor()

   
    if x + pulse.dx > x_limit or x + pulse.dx < -x_limit:
        pulse.dx *= -1

    if y + pulse.dy > y_limit or y + pulse.dy < -y_limit:
        pulse.dy *= -1

    pulse.setx(x + pulse.dx)
    pulse.sety(y + pulse.dy)

    window.ontimer(move_pulse, 10)
    
move_pulse()
turtle.mainloop()

