'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets at least three attributes
- Include a __str__ method in each class that prints out the attributes
    in a nicely formatted string.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Create at least two instances of each class.
- Once the objects are created, change some of their attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, card games, sports teams, trees, people etc...

'''

class Cat:

    def __init__(self, color, weight):
        self.color = color
        self.weight = weight

    def __str__(self):
        return f"this is a {self.color} Cat who weighs about {self.weight}lbs "

    def __add__(self, other):
        return self.weight + other

Zuko = Cat("black", 12)
Squishy = Cat("brown", 20)
print(Zuko + Squishy)