# Import Statements
import turtle as trtl
import random as rand
from itertools import count

# Variables
lock = True
player_id = [1,2]
timer = rand.randint(5,10)
wn=trtl.Screen()
wn.setup(width=558, height=345)
counter_display = trtl.Turtle()
counter_interval = 1000
font_setup=("Arial", 20, "normal")
timer_up = False
player1=trtl.Turtle()
player2=trtl.Turtle()
lazer1 = trtl.Turtle()
lazer2 = trtl.Turtle()
wn.setup(558,345)
wn.bgpic("background.gif")
# Turtle Setup
player1.speed(0)
player1.color('red')
player1.shape('circle')
player1.shapesize(3.5)
player1.penup()
player1.goto(-230,-120)
player2.speed(0)
player2.color('blue')
player2.shape('circle')
player2.shapesize(3.5)
player2.penup()
player2.goto(230,-120)
lazer1.speed(5)
lazer1.color('red')
lazer1.shape('square')
lazer1.shapesize(.5)
lazer1.penup()
lazer1.goto(-230,-120)
lazer1.pendown()
lazer2.speed(5)
lazer2.color('blue')
lazer2.shape('square')
lazer2.shapesize(.5)
lazer2.penup()
lazer2.goto(230,-120)
lazer2.pendown()

# Functions
def countdown():
    global timer, timer_up, lock
    counter_display.clear()
    if timer <= 0:
        counter_display.write("DRAW", font=font_setup)
        timer_up = True
        lock = False
    else:
        timer -= 1
        counter_display.getscreen().ontimer(countdown, counter_interval)
    # Game
def press_a():
    if lock == False:
        lazer1.goto(350,-200)
        counter_display.clear()
        counter_display.write("PLAYER ONE WINS", font=font_setup)
def press_l():
    if lock == False:
        lazer1.goto(350,-200)
        counter_display.clear()
        counter_display.write("PLAYER TWO WINS", font=font_setup)

wn.ontimer(countdown, counter_interval)
wn.onkeypress(press_a,"a")
wn.onkeypress(press_l,"l")
wn.listen()
wn.mainloop()


'''
hour = ["1:", "2:", "3:", "4:", "5:", "6:", "7:", "8:", "9:","10:","11:","12:"]
minute = ["01","02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58" "59", "60"]
Day = ["AM", "PM"]
'''