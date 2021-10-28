import turtle
t = turtle.Turtle()
turtle.bgcolor('black')
t.speed(20)
t.color('red')
i = 200

while(i > 0):
    t.right(i)
    t.forward(i*3)
    
    i = i-1

turtle.done()
