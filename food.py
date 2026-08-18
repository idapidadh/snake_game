from turtle import Turtle
import random
from game_coefficients import MOVE_DISTANCE, FOOD_DIAMETER

# stretch factor to get food size set in game_coefficients (turtle is 20x20 by default)
STRETCH_FACTOR = FOOD_DIAMETER / 20

# class Food inherits from Turtle class
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # turtle is normally 20x20. So stretching length/width by half to get 10x10
        self.shapesize(stretch_len=STRETCH_FACTOR, stretch_wid=STRETCH_FACTOR)
        self.color("blue")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        # create food in random location on screen (both x and y are -300 to +300)
        # subtract MOVE_DISTANCE from x and y boundaries to avoid having food right on the edge
        random_x = random.randint(-300 + MOVE_DISTANCE, 300 - MOVE_DISTANCE)
        random_y = random.randint(-300 + MOVE_DISTANCE, 300 - MOVE_DISTANCE)
        self.goto(random_x, random_y)
