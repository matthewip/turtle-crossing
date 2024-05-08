import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()

car_manager = CarManager()

player = Player()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    screen.onkey(player.move_up, "Up")
    car_manager.generate_car()
    car_manager.move_cars()

    # Detect successful crossing
    if player.check_if_player_reached_end():
        player.go_to_start_position()
        car_manager.next_level()
        scoreboard.increase_level()

    # Detect collision between car and turtle
    for car in car_manager.car_list:
        if player.distance(car) < 23:
            # GAME OVER
            scoreboard.write_game_over()
            game_is_on = False

screen.exitonclick()
