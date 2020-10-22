from turtle import forward, left, right, exitonclick, speed

a = 20

speed(0)

# 4 ctverce vedle sebe
for _ in range(4):
    for _ in range(4):
        forward(a)
        left(90)
    left(90)

forward(100)


# Kyticka z sestiuhelniku
for i in range(6):
    for j in range(6):
        forward(a)
        left(60)
    forward(a)
    right(60)

