from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from game_coefficients import FOOD_COLLISION_BUFFER, WALL_COLLISION_BUFFER, TAIL_COLLISION_BUFFER

screen = Screen()
screen.setup(width=600, height=600)
# bgcolor = background color
screen.bgcolor("black")
screen.title("My snake game")
# Turning off tracer in order to control the screen update manually
# Tracer is a method in the Screen class.
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
# The arrows on the keyboard are represented by the following strings: "Up", "Down", "Left", "Right"
# snake methods are activated when the keys are pressed
# Eg. when "Up"-key is pressed, the method snake.up() is activated.
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    # Telling screen to refresh once all segments have gotten their new position.
    screen.update()
    # Setting the time between the screen being refreshed
    time.sleep(0.2)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < FOOD_COLLISION_BUFFER:
        food.refresh() # move food to new location
        scoreboard.increment_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 300 - WALL_COLLISION_BUFFER or snake.head.xcor() < -300 + WALL_COLLISION_BUFFER:
        game_is_on = False
    if snake.head.ycor() > 300 - WALL_COLLISION_BUFFER or snake.head.ycor() < -300 + WALL_COLLISION_BUFFER:
        game_is_on = False

    # Detect collision with tail
    for segment in snake.segments[1:]: # ommit head at pos 0 via slicing
        if snake.head.distance(segment) < TAIL_COLLISION_BUFFER:
            game_is_on = False
            break


scoreboard.game_over()
screen.exitonclick()

