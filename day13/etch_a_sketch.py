import turtle as t

tim = t.Turtle()
screen = t.Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def rotate_right():
    tim.right(10)

def rotate_left():
    tim.left(10)


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(rotate_right, "d")
screen.onkey(rotate_left, "a")
screen.onkey(screen.resetscreen, "c")
screen.exitonclick()