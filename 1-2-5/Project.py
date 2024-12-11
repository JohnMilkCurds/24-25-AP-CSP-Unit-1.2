# Import Statements
import turtle as trtl
import random as rand
# Variables
Lock = True
player_id = [1,2]
countdown = rand.randint(5,10)
counter = trtl.Turtle()
counter_interval = 1000
countdown_up = False
player1=trtl.Turtle()
player2=trtl.Turtle()
# Turtle Setup
player1.speed(0)
player1.color('red')
player1.shape('circle')
player1.shapesize(5)
player1.penup()
player1.goto(-350,-200)
player2.speed(0)
player2.color('blue')
player2.shape('circle')
player2.shapesize(5)
player2.penup()
player2.goto(350,-200)
# Functions
def timer(countdown):
    if countdown == 0:
        counter.write("DRAW")
        countdown_up = True
    else:
        countdown -= 1
        counter.getscreen().ontimer(countdown, counter_interval)

    # Game

wn=trtl.Screen()
wn.ontimer(timer(countdown), counter_interval)
wn.bgcolor('cyan')
wn.mainloop()

'''
hour = ["1:", "2:", "3:", "4:", "5:", "6:", "7:", "8:", "9:","10:","11:","12:"]
minute = ["01","02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58" "59", "60"]
Day = ["AM", "PM"]
'''