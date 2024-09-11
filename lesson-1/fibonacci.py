import turtle

n1 = 0
n2 = 1

screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.tracer(0, 0)

t = turtle.Turtle()
t.color("white")
t.width(2)

def make_arc(size):
    for _ in range(90):
        t.forward(size / 10000)
        t.right(1)

def fib(depth = 100):
    global n1, n2

    make_arc(n2)
    if depth == 0:
        return

    n1, n2 = n2, n1 + n2
    fib(depth - 1)

fib(500)

screen.update()
screen.exitonclick()