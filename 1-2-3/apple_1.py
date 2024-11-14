#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
pear_image = "pear.gif"
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.addshape(pear_image)
apple = trtl.Turtle()
apple.penup()
pear = trtl.Turtle()
wn.bgpic("background.gif")
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()
def apple_down(active_apple):
  x_coor = active_apple.xcor()
  y_coor = active_apple.ycor()
  active_apple.goto(x_coor, y_coor)
  apple.goto(0,-150)
def draw_pear(active_pear):
  active_pear.shape(pear_image)
  wn.update()
#-----function calls-----
draw_apple(apple)
draw_pear(pear)
apple_down(apple)
wn.mainloop()