import turtle
from turtle import Turtle, Screen

colors = [(77, 111, 155), (29, 7, 71), (139, 55, 82), (94, 49, 80), (68, 50, 98), (248, 247, 246), (59, 18, 67),
          (232, 238, 245)]
turtle.colormode(255)
turtle.bgcolor(77, 111, 155)
screen = Screen()
screen.setup(width= 1500, height = 800)

moon = Turtle()
moon.speed("fastest")
moon.pu()
moon.left(90)
moon.fd(175)
moon.fillcolor(231, 231, 231)
moon.begin_fill()
moon.circle(50)
moon.end_fill()


layer_1 = Turtle()
layer_1.speed("fastest")
layer_1.pu()
layer_1.goto(-300,-200)
layer_1.fillcolor(205,65,87)
layer_1.begin_fill()
layer_1.seth(60)
layer_1.fd(440)
layer_1.seth(300)
layer_1.fd(50)
layer_1.seth(60)
layer_1.fd(20)
layer_1.seth(300)
layer_1.fd(70)
layer_1.seth(60)
layer_1.fd(120)
layer_1.seth(300)
layer_1.fd(470)
layer_1.end_fill()

layer_2 = Turtle()
layer_2.speed("fastest")
layer_2.pu()
layer_2.goto(-770,-250)
layer_2.fillcolor(139,55,82)
layer_2.begin_fill()
layer_2.seth(60)
layer_2.fd(420)
layer_2.seth(300)
layer_2.fd(150)
layer_2.seth(60)
layer_2.fd(380)
layer_2.seth(300)
layer_2.fd(600)
layer_2.seth(0)
layer_2.fd(90)
layer_2.seth(60)
layer_2.fd(620)
layer_2.seth(300)
layer_2.fd(700)
layer_2.end_fill()

layer_3 = Turtle()
layer_3.speed("fastest")
layer_3.pu()
layer_3.fillcolor(94,49,80)
layer_3.goto(770,-400)
layer_3.begin_fill()
layer_3.seth(180)
layer_3.fd(1600)
layer_3.goto(-770,-20)
layer_3.seth(60)
layer_3.fd(70)
layer_3.seth(300)
layer_3.fd(200)
layer_3.seth(60)
layer_3.fd(220)
layer_3.seth(300)
layer_3.fd(200)
layer_3.seth(60)
layer_3.fd(180)
layer_3.seth(300)
layer_3.fd(350)
layer_3.seth(60)
layer_3.fd(300)
layer_3.seth(300)
layer_3.fd(200)
layer_3.seth(60)
layer_3.fd(200)
layer_3.seth(300)
layer_3.fd(300)
layer_3.seth(60)
layer_3.fd(400)
layer_3.seth(300)
layer_3.fd(500)
layer_3.end_fill()

layer_4 = Turtle()
layer_4.speed("fastest")
layer_4.pu()
layer_4.fillcolor(68,50,98)
layer_4.goto(-770,-400)
layer_4.begin_fill()
layer_4.seth(60)
layer_4.fd(300)
layer_4.seth(300)
layer_4.fd(300)
layer_4.seth(60)
layer_4.fd(300)
layer_4.seth(300)
layer_4.fd(300)
layer_4.seth(60)
layer_4.fd(300)
layer_4.seth(300)
layer_4.fd(300)
layer_4.seth(60)
layer_4.fd(300)
layer_4.seth(300)
layer_4.fd(300)
layer_4.seth(60)
layer_4.fd(300)
layer_4.seth(300)
layer_4.fd(300)
layer_4.seth(60)
layer_4.fd(300)
layer_4.seth(300)
layer_4.fd(300)
layer_4.seth(60)
layer_4.fd(300)
layer_4.seth(300)
layer_4.fd(300)
layer_4.end_fill()


layer_5 = Turtle()
layer_5.pu()
layer_5.speed("fastest")
layer_5.goto(-200,-400)
layer_5.fillcolor(59,18,67)
layer_5.begin_fill()
layer_5.seth(60)
layer_5.fd(200)
layer_5.seth(300)
layer_5.fd(200)
layer_5.seth(60)
layer_5.fd(200)
layer_5.seth(300)
layer_5.fd(200)
layer_5.end_fill()


layer_6 = Turtle()
layer_6.speed("fastest")
layer_6.pu()
layer_6.goto(770,-400)
layer_6.fillcolor(29,7,71)
layer_6.begin_fill()
layer_6.seth(180)
layer_6.fd(1600)
layer_6.goto(-770,-250)
layer_6.seth(70)
layer_6.fd(350)
layer_6.seth(290)
layer_6.fd(400)
layer_6.seth(70)
layer_6.fd(500)
layer_6.seth(290)
layer_6.fd(500)
layer_6.seth(320)
layer_6.fd(90)
layer_6.seth(0)
layer_6.fd(300)
layer_6.seth(30)
layer_6.circle(-500,30)
layer_6.seth(70)
layer_6.fd(600)
layer_6.seth(290)
layer_6.fd(800)
layer_6.end_fill()

bird = Turtle()
bird.pensize(3)
bird.pu()
bird.goto(-5,175)
bird.pd()
bird.seth(50)
bird.circle(-20,60)
bird.pu()
bird.goto(-5,175)
bird.seth(130)
bird.pd()
bird.circle(20,60)
bird.pu()
bird.goto(-50,175)
bird.pd()
bird.seth(50)
bird.circle(-20,60)
bird.pu()
bird.goto(-50,175)
bird.seth(130)
bird.pd()
bird.circle(20,60)
bird.pu()
bird.goto(-100,195)
bird.pd()
bird.seth(50)
bird.circle(-20,60)
bird.pu()
bird.goto(-100,195)
bird.seth(130)
bird.pd()
bird.circle(20,60)
bird.pu()
bird.goto(-55,195)
bird.pd()
bird.seth(50)
bird.circle(-20,60)
bird.pu()
bird.goto(-55,195)
bird.seth(130)
bird.pd()
bird.circle(20,60)
bird.ht()

screen.exitonclick()

