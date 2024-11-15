#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
ground_height= -200
apple_letter_x_offset = 15
apple_letter_y_offset = 35
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
apple = trtl.Turtle()
apple.penup()
wn.bgpic("background.gif")



#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple():
  apple.shape(apple_image)
  apple.color("white")
  apple.write("A", font=("Arial", 40, "bold"))
  apple.goto(apple_letter_x_offset, apple_letter_y_offset)
  wn.update()
def drop_apple():
  apple.goto(apple.xcor(),ground_height)



#-----function calls-----
draw_apple()
wn.onkeypress(drop_apple, "a")
wn.listen()
wn.mainloop()