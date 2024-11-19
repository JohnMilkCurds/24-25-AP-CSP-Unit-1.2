#   a123_apple_1.py
import turtle as trtl
import random as rand
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
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def reset_apple():
  if len(letters) > 0:
    new_x = rand.randint(-200, 200 )
    new_y = apple.ycor()
    new_letter = rand.randint(0, len(letters))
    draw_apple(apple, letters.pop(new_letter))
def draw_apple(apple, letter):
  apple.shape(apple_image)
  apple.color("white")
  apple.write(letter, font=("Arial", 40, "bold"))
  apple.goto(apple_letter_x_offset, apple_letter_y_offset)
  apple.showturtle()
  wn.update()
def drop_apple():
  apple.goto(apple.xcor(),ground_height)
  apple.clear()
  apple.hideturtle()
  reset_apple()




#-----function calls-----
draw_apple(apple,letters)
wn.onkeypress(drop_apple,"a")
wn.listen()
wn.mainloop()