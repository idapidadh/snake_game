from turtle import Turtle
from game_coefficients import MOVE_DISTANCE

# The snake consist of multiple square-shaped turtles - each sized 20x20 pixels
# Starting snake will consist of 3 squares

# Below is a list of tuples with starting positions for the snake segments
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# The starting positions list is created as a constant
# Note to self: in Python the constants are named with all caps (=only capital letters)


UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        # Attribute: List for the segments once they are created
        self.segments = []
        # Method
        self.create_snake()
        # Attribute
        self.head = self.segments[0]

    def create_snake(self):
        # Creating and positioning the segments
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Ad segment to snake at given position"""
        segment = Turtle(shape="square")
        segment.color("white")
        # Snake segments must not draw while moving
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        """Extends snake with new segment at the end"""
        # get position of current last segment in snake. Note to self: in python, [-1] gives you last element on list
        position = self.segments[-1].position()
        # add new segment to same position as last segment.
        self.add_segment(position)


    def move(self):
        """Moves snake"""
        # for-looping through the segments in reverse order
        # Unseen keywords in range function are start, stop, step. SO: range(start=len(segments)-1, stop=0, step=-1
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

