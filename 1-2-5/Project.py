# Import Statements
import turtle as trtl
import random as rand
# Variables
Lock = True
player_id = [1,2]
countdown = rand.randint(5000,30000)
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



wn=trtl.Screen()
wn.bgcolor('cyan')
wn.mainloop()