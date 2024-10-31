# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
#-----game configuration----
spot_color = "pink"
spot_size = 2
spot_shape = "circle"
score=0
font_setup=("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False
#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.up()
spot.color(spot_color)
score_writer= trtl.Turtle()
score_writer.up()
score_writer.goto(350,250)
score_writer.hideturtle()
counter =  trtl.Turtle()
counter.up()
counter.goto(-25,275)
counter.hideturtle()
#-----game functions--------
def spot_clicked(x, y):
    update_score()
    change_position()
def change_position():
    new_xpos=rand.randint(-400, 400)
    new_ypos=rand.randint(-300, 300)
    spot.goto(new_xpos, new_ypos)
def update_score():
    global score
    score+=1
    score_writer.clear()
    score_writer.write(score, font=font_setup)
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
#-----events----------------
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()