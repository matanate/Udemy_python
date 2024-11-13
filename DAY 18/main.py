#import colorgram

#rgb_colors = []
#colors = colorgram.extract('image.jpg', 30)

#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r,g,b)
#    rgb_colors.append(new_color)

#print(rgb_colors)

import turtle as t
import random

color_list = [(134, 169, 201), (195, 163, 140), (63, 88, 136), (181, 153, 170), (119, 78, 99), (156, 76, 50), (55, 119, 94), (221, 229, 88), (138, 191, 149), (114, 116, 181), (44, 52, 103), (39, 47, 62), (176, 187, 212), (227, 134, 15), (174, 96, 114), (86, 50, 63), (57, 47, 56), (214, 181, 194), (109, 167, 72), (112, 38, 36), (42, 50, 47), (37, 34, 33), (215, 88, 49), (230, 174, 158), (170, 206, 173), (159, 204, 212)]

hirst = t.Turtle()
hirst.hideturtle()
hirst.speed(10)
t.colormode(255)

def draw_dot(size):
    hirst.pendown()
    hirst.dot(size, random.choice(color_list))
def move_next_dot(size, gap):
    hirst.penup()
    hirst.forward(size + gap)
def move_next_line(size, gap, rows):
    hirst.penup()
    hirst.goto(hirst.position()[0] - gap*(rows-1) - size*(rows-1), hirst.position()[1] + gap + size)

def hirst_paint(size, gap, rows, cols):
    hirst.penup()
    start_x = -((rows-1)/2) * (gap + size)
    start_y = -((cols-1)/2) * (gap + size)
    
    hirst.setpos(start_x, start_y)    
    for _ in range(0, cols):
        draw_dot(size)    
        for _ in range(0, rows-1):
            move_next_dot(size, gap)
            draw_dot(size)
        move_next_line(size, gap, rows)
    


hirst_paint(20,50,10,10)

screen = t.Screen()
screen.exitonclick()