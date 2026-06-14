import turtle
turtle.Screen().bgcolor("blue")
sc = turtle.Screen()
sc.setup(400, 400)
turtle.title("welcome to turtle window")
board = turtle.Turtle()
for i in range (4):
    board.forward(100)
    board.left(90)
    i = i+1