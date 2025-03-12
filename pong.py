import turtle
import time

def platform_a_up():
    y = platform_a.ycor()
    y += 20
    platform_a.sety(y)

def platform_a_down():
    y = platform_a.ycor()
    y -= 20
    platform_a.sety(y)

def platform_b_up():
    y = platform_b.ycor()
    y += 20
    platform_b.sety(y)

def platform_b_down():
    y = platform_b.ycor()
    y -= 20
    platform_b.sety(y)

wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Platform A
platform_a = turtle.Turtle()
platform_a.speed(0)
platform_a.color("red")
platform_a.shape("square")
platform_a.shapesize(stretch_wid=7, stretch_len=1)
platform_a.penup()
platform_a.goto(-350,0)

#Platform B
platform_b = turtle.Turtle()
platform_b.speed(0)
platform_b.color("blue")
platform_b.shape("square")
platform_b.shapesize(stretch_wid=7, stretch_len=1)
platform_b.penup()
platform_b.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.color("white")
ball.shape("circle")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0,0)

#ScoreBoard
board = turtle.Turtle()
board.speed(0)
board.color("white")
board.penup()
board.hideturtle()
board.goto(0,280)
board.write(f"Player1 : 0 | Player2 : 0", align="center", font=("Arial",0,"normal"))

#Winner
winner = turtle.Turtle()
winner.speed(0)
winner.color("white")
winner.penup()
winner.hideturtle()
winner.goto(0,0)


#ball speed regulation dependent by device speed
speed = 0.03
ball.cx = 0.03
ball.cy = 0.03

wn.listen()
wn.onkeypress(platform_a_up, "w")
wn.onkeypress(platform_a_down, "s")
wn.onkeypress(platform_b_up, "Up")
wn.onkeypress(platform_b_down, "Down")
player1 = 0
player2 = 0

while True:
    wn.update()
    ball.setx(ball.xcor() + ball.cx)
    ball.sety(ball.ycor() + ball.cy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.cy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.cy *= -1

    if ball.xcor() > 390:
        ball.setx(390)
        ball.cx *= -1

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.cx *= -1
    
    if platform_a.ycor() > 230:
        platform_a.sety(230)

    if platform_a.ycor() < -230:
        platform_a.sety(-230)

    if platform_b.ycor() > 230:
        platform_b.sety(230)

    if platform_b.ycor() < -230:
        platform_b.sety(-230)

    if ball.xcor()>330 and ball.xcor()<350 and (ball.ycor() > platform_b.ycor()-70 and ball.ycor() < platform_b.ycor() + 70):
        ball.cx *= -1
        ball.cx *= 1.06
        ball.cy *= 1.06
    if ball.xcor()<-330 and ball.xcor()>-350 and (ball.ycor() > platform_a.ycor()-70 and ball.ycor() < platform_a.ycor() + 70):
        ball.cx *= -1
        ball.cx *= 1.06
        ball.cx *= 1.06
        
    if ball.xcor()>380:
        ball.goto(0,0)
        ball.cx *= -1
        player1+=1
        ball.cx = speed
        ball.cy = speed
        board.clear()
        board.write(f"Player1 : {player1} | Player2 : {player2}", align="center", font=("Arial",0,"normal"))
    
    if ball.xcor()<-380:
        ball.goto(0,0)
        ball.cx *= -1
        player2 += 1
        ball.cx = speed
        ball.cy = speed
        board.clear()
        board.write(f"Player1 : {player1} | Player2 : {player2}" , align="center", font=("Arial",0,"normal"))
    
    if player1>7 or player2 >7:
        
        if player1>player2:
            winner.write(f"Won Player 1", align="center", font=("Arial",50,"normal"))
        else:
            winner.write(f"Won Player 2", align="center", font=("Arial",50,"normal", ))
            board.write(f"Thanks for playing, If u want play again, restart game.", align="center", font=("Arial",0,"normal"))
            time.sleep(10)
