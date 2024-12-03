import turtle as trtl
import random as rand

# Initialize Variables
wn=trtl.Screen()
maze_painter= trtl.Turtle()
length = 10
path_width = 50
# Setup Turtle
maze_painter.speed(0)
maze_painter.pensize(5)
# Draw maze
# Process:
# Draw a line
# Turn left
# Increment Length
# Repeat
def draw_barrier_2():
    maze_painter.left(90)
    maze_painter.forward(path_width)
    maze_painter.backward(path_width)
    maze_painter.right(90)
def draw_barrier():
    maze_painter.right(90)
    maze_painter.forward(path_width)
    maze_painter.backward(path_width)
    maze_painter.left(90)
def wall_randomness():
    if randomness == 1:
        draw_barrier()
    elif randomness == 2:
        draw_barrier()
    elif randomness == 3:
        maze_painter.right(360)
for wall in range(30):
    randomness = rand.randint(1, 3)
    maze_painter.left(90)
    if randomness == 1:
        maze_painter.penup()
    if randomness == 2:
        maze_painter.right(360)
    if randomness == 3:
        maze_painter.penup()
    maze_painter.forward(path_width)
    if randomness == 1 or randomness == 3:
        maze_painter.pendown()
    wall_randomness()
    maze_painter.forward(length- path_width - length/3)
    maze_painter.forward(length)
    length+= 15














wn.listen()
wn.mainloop()