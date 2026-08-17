import turtle

# 굵은 펜으로 눈과 얼굴 요소를 그리던 연습을 정리한 코드입니다.
turtle.pensize(50)
for x in (-150, 50):
    turtle.penup()
    turtle.goto(x, 50)
    turtle.pendown()
    turtle.circle(40, steps=100)

turtle.pensize(30)
turtle.penup()
turtle.goto(-50, -80)
turtle.pendown()
turtle.circle(60, steps=30)
turtle.done()
