import turtle
import time
import sys


seconds=int(input("For how many Seconds you want to play  "))


wn=turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800,height=610)
wn.tracer(0)

#Paddle A

paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


#Paddle A

paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# Ball

#Paddle A

ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.3
ball.dy=0.3

#score
score_a=0
score_b=0

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0   Player B: 0",align="center",font=("Courier",18,"normal"))

#timerpen
timer=turtle.Turtle()
timer.speed(0)
timer.color("white")
timer.pendown
timer.hideturtle()
timer.goto(0,-260)
timer.write("Time: 0",align="center",font=("Courier",18,"normal"))


#Function
def paddle_a_up():
    y=paddle_a.ycor()
   
    if(y<=240):
        y+=20
    paddle_a.sety(y)


def paddle_a_down():
    y=paddle_a.ycor()
    if(y>=-220):
        y-=20
    paddle_a.sety(y)


def paddle_b_up():
    y=paddle_b.ycor()
   
    if(y<=240):
        y+=20
    paddle_b.sety(y)


def paddle_b_down():
    y=paddle_b.ycor()
    if(y>=-220):
        y-=20
    paddle_b.sety(y)


#keyboard binding

wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

starttime=time.time()

#Main game Loop
while True:
        wn.update()
        elapasedtime=time.time()-starttime
        elapasedtime=format(elapasedtime,",.0f")
        timer.clear()
        timer.write("Time: {} seconds".format(elapasedtime),align="center",font=("Courier",18,"normal"))
        endtime=int(elapasedtime)
        if(seconds==endtime):
             timer.clear()
             pen.clear()
             timer.goto(0,0)
             if score_a>score_b:
                    timer.write("Player A Wins\nExiting...",align="center",font=("Courier",20,"normal"))
             elif score_b>score_a:
                    timer.write("Player B Wins\nExiting...",align="center",font=("Courier",20,"normal"))
             else:
                    timer.write("Draw\nExiting...",align="center",font=("Courier",20,"normal"))
             time.sleep(10)
             break
            
        
        #move the ball
        ball.setx(ball.xcor()+ball.dx)
        ball.sety(ball.ycor()+ball.dy)


        #bordercheck
        if ball.ycor()>290:
            ball.sety(290)
            ball.dy*=-1

        if ball.ycor()<-290:
            ball.sety(-290)
            ball.dy*=-1
    
        if ball.xcor()>390:
            ball.goto(0,0)
            ball.dx*=-1

        if ball.xcor()<-390:
            ball.goto(0,0)
            ball.dx*=-1


        if(ball.xcor()>340 and ball.xcor()<350)and (ball.ycor()<paddle_b.ycor()+40 and ball.ycor()>paddle_b.ycor()-40):
            ball.setx(340)
            ball.dx*=-1
            score_b+=1
            pen.clear()
            pen.write("Player A: {}   Player B: {}".format(score_a,score_b),align="center",font=("Courier",18,"normal"))


        if(ball.xcor()<-340 and ball.xcor()>-350)and (ball.ycor()<paddle_a.ycor()+40 and ball.ycor()>paddle_a.ycor()-40):
            ball.setx(-340)
            ball.dx*=-1
            score_a+=1
            pen.clear()
            pen.write("Player A: {}   Player B: {}".format(score_a,score_b),align="center",font=("Courier",18,"normal"))
