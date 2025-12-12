# import colorgram
#
# extracted_colours = colorgram.extract("image.jpg", 20)
# rgb_colours = []
#
# for colour in extracted_colours:
#     r = colour.rgb[0]
#     g = colour.rgb[1]
#     b = colour.rgb[2]
#     rgb_colours.append((r, g, b))
#
# print(rgb_colours)

# ABOVE USED TO EXTRACT COLOURS FROM IMAGE - REMOVED A FEW AND USED IN VARIABLE BELOW
import turtle as t
import random

t.colormode(255)
colour_list = [(236, 35, 108), (221, 231, 237), (145, 28, 66), (239, 75, 35), (7, 148, 95), (220, 171, 45), (183, 158, 47), (45, 191, 232), (28, 127, 194), (254, 223, 0), (125, 192, 78), (85, 27, 91), (243, 218, 56), (178, 40, 98), (44, 170, 114), (211, 132, 166), (206, 57, 35)]
jane = t.Turtle()
jane.penup()
jane.speed("fast")

start_pos = jane.setposition(-225, -180)

def random_colour():
    return random.choice(colour_list)

def create_hirst_painting():
    y = -180
    for row in range(10):

        for i in range(10):
            jane.dot(20, random_colour())
            jane.forward(50)

        y += 50
        jane.setposition((-225, y))


create_hirst_painting()

screen = t.Screen()
screen.exitonclick()