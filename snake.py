from turtle import Turtle


class Snake:
    def __init__(self):
        self.list_of_turtles = []
        for _ in range(3):
            self.list_of_turtles.append(self.create_square())
        self.first_turtle = self.list_of_turtles[0]
            
    def move(self):
        for i, turtle in reversed(list(enumerate(self.list_of_turtles[1:]))):
            turtle.setposition(self.list_of_turtles[i].position())  # nie wiem dlaczego i, a nie i+1
        self.first_turtle.forward(20)

    def create_square(self):
        square = Turtle(shape="square")
        square.color("white")
        square.penup()
        square.speed("fastest")
        if self.list_of_turtles:
            x, y = self.list_of_turtles[len(self.list_of_turtles) - 1].position()
            square.setposition(x - 20, y)
            print(square.position())
        return square

    def turn_left(self):
        self.first_turtle.left(90)

    def turn_right(self):
        self.first_turtle.right(90)
