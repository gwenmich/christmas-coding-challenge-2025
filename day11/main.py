import turtle
import turtle as t
import random

bob = t.Turtle()
t.colormode(255)

def random_rgb_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    bob.pencolor(r, g, b)


def create_shapes():
    i = 3

    while i < 11:

        for _ in range(i):
            bob.forward(100)
            bob.right(360 / i)

        random_rgb_colour()
        i += 1


def random_direction():
    directions = [0, 90, 180, 270]
    rand_direction = random.choice(directions)
    return rand_direction


def random_walk():
    bob.pensize(10)
    bob.speed("fast")

    for i in range(100):
        bob.setheading(random_direction())
        random_rgb_colour()
        bob.forward(50)


def create_spirograph():
    bob.speed("fastest")
    for i in range(72):
        random_rgb_colour()
        bob.circle(100)
        bob.right(5)



# create_shapes()
# random_walk()
# create_spirograph()
screen = t.Screen()
screen.exitonclick()