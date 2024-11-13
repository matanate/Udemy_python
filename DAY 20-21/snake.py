from turtle import Turtle

START_POS = [(0, 0), (-10, 0), (-10, 0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
BOARDER = 295


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        self.boarder()

    def create_snake(self):
        for pos in START_POS:
            self.add_segment(pos)

    def move(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[i].goto(self.snake_body[i - 1].pos())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def add_segment(self, position):
        snake_seg = Turtle("square")
        snake_seg.shapesize(stretch_len=0.5, stretch_wid=0.5)
        snake_seg.color("white")
        snake_seg.penup()
        snake_seg.goto(position)
        self.snake_body.append(snake_seg)

    def extend_snake(self):
        self.add_segment(self.snake_body[-1].pos())

    def boarder(self):
        boarder = Turtle()
        boarder.hideturtle()
        boarder.penup()
        boarder.color("yellow")
        boarder.goto(-BOARDER, -BOARDER)
        boarder.pendown()
        boarder.goto(-BOARDER, BOARDER)
        boarder.goto(BOARDER, BOARDER)
        boarder.goto(BOARDER, -BOARDER)
        boarder.goto(-BOARDER, -BOARDER)

    def reset_score(self):
        for seg in self.snake_body:
            seg.hideturtle()
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]
