'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''
class car:

    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def __repr__(self):
        return f"the car is a {self.model} that is {self.year}'s old and can go {self.max_speed} mph"

    def speed_up(self):
        self.max_speed += 5

my_car = car("chevy", 2018, 120)
print(my_car)
my_car.speed_up()
print(my_car)