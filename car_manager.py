from turtle import Turtle

from car import Car
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Car()
            car.move(self.car_speed)
            self.car_list.append(car)

    def next_level(self):
        self.car_speed += MOVE_INCREMENT

    def move_cars(self):
        for car in self.car_list:
            car.move(self.car_speed)

