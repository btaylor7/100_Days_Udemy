from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.current_heading = 0

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move_snake(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):  # Starts with 3, moves it to 2.
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.current_heading != 270:
            self.segments[0].setheading(90)#Head
            self.current_heading = 90

    def down(self):
        if self.current_heading != 90:
            self.segments[0].setheading(270)
            self.current_heading = 270

    def left(self):
        if self.current_heading !=0:
            self.segments[0].setheading(180)
            self.current_heading = 180

    def right(self):
        if self.current_heading != 180:
            self.segments[0].setheading(0)
            self.current_heading = 0

