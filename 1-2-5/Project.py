# Import Statements
import turtle as trtl
import random as rand

# Variables
#Background
cowboy1 = "cowboy.gif"
cowboy2 = "cowboy2.gif"
lock = True
wn=trtl.Screen()
wn.setup(width=558, height=345)
font_setup=("Arial", 20, "normal")
timer = rand.randint(3, 10)
timer_up = False
wn.setup(558,345)
wn.bgpic("background.gif")
#turtles
player1=trtl.Turtle()
player2=trtl.Turtle()
lazer1 = trtl.Turtle()
lazer2 = trtl.Turtle()
counter_display = trtl.Turtle()
counter_display.color("black")
counter_interval = 1000
#fake time
hour_list = ['1:','2:','3:','4:','5:','6:','7:','8:','9:','10:','11:','12:']
minute_list = ["01","02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58" "59", "60"]
day_list = ["AM", "PM"]
hour = rand.choice(hour_list)
minute = rand.choice(minute_list)
day = rand.choice(day_list)
wn.addshape(cowboy1)
wn.addshape(cowboy2)


# Turtle Setup
counter_display.speed(100)
counter_display.penup()
counter_display.goto(100,100)
counter_display.write("It's "+ hour + minute + " " + day, font = font_setup)
counter_display.goto(-50, 0)
counter_display.hideturtle()
#Player one
player1.speed(0)
player1.color('red')
player1.shape(cowboy1)
player1.penup()
player1.goto(-180,-90)
#Player two
player2.speed(0)
player2.color('blue')
player2.shape(cowboy2)
player2.shapesize(3.5)
player2.penup()
player2.goto(180,-90)
#Lazer 1
lazer1.speed(5)
lazer1.color('black')
lazer1.shape('square')
lazer1.shapesize(.5)
lazer1.penup()
lazer1.hideturtle()
lazer1.goto(-180,-90)
#Lazer 2
lazer2.speed(5)
lazer2.color('black')
lazer2.shape('square')
lazer2.shapesize(.5)
lazer2.penup()
lazer2.goto(180,-90)
lazer2.hideturtle()
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
    # Game Controls
def press_a():
    global lock
    if lock is False:
        lock = True
        lazer1.showturtle()
        lazer1.goto(190,-90)
        counter_display.clear()
        counter_display.write("PLAYER ONE WINS! Press space and try again!", font=font_setup)
def press_l():
    global lock
    if lock is False:
        lock = True
        lazer2.showturtle()
        lazer2.goto(-190,-90)
        counter_display.clear()
        counter_display.write("PLAYER TWO WINS! Press space and try again!", font=font_setup)
def press_space():
    global timer
    timer = rand.randint(5, 10)
    lazer1.goto(-180,-90)
    lazer2.goto(180,-90)
    lazer1.hideturtle()
    lazer2.hideturtle()
    wn.ontimer(countdown, counter_interval)
# Events
wn.ontimer(countdown, counter_interval)
wn.onkeypress(press_a,"a")
wn.onkeypress(press_l,"l")
wn.onkeypress(press_space,"space")
wn.listen()
wn.mainloop()
