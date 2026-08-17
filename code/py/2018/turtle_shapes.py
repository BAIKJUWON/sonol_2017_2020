import turtle

# 삼각형부터 원에 가까운 다각형까지 그립니다.
for x, steps in [(-200, 3), (-100, 4), (0, 5), (100, 6), (200, 100)]:
    turtle.penup()
    turtle.goto(x, -50)
    turtle.pendown()
    turtle.circle(40, steps=steps)

turtle.done()
