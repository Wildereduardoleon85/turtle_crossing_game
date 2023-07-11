from turtle import Screen
from car_manager import CarManager
from player import Player
from score_board import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#737386")
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()

game_is_on = True
screen.onkeypress(player.move_up, "Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.print_game_over()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.reset_to_initial_position()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
