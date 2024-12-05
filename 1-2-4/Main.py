import turtle as trtl
import random as rand
# Initialize Variables
wn=trtl.Screen()
maze_painter= trtl.Turtle()
length = 15
path_width = 60
# Setup Turtle
maze_painter.speed(0)
maze_painter.pensize(5)
# Draw maze
# Process:
# Draw a line
# Turn left
# Increment Length
# Repeat
def draw_barrier():
    maze_painter.right(90)
    maze_painter.forward(path_width)
    maze_painter.backward(path_width)
    maze_painter.left(90)
for wall in range(21):
    index = rand.randint(0,(length - 10))
    rndm = rand.randint(0,(length - 10))
    maze_painter.left(90)
    maze_painter.forward(index)
    maze_painter.penup()
    maze_painter.forward(path_width)
    maze_painter.pendown()
    if wall > 5:
        draw_barrier()
    maze_painter.forward(length- path_width - index)
    maze_painter.forward(length)
    length+= 15
wn.listen()
wn.mainloop()