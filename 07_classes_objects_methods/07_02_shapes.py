'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''

class rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc_area(self):
        return self.length * self.width

    def calc_perimeter(self):
        return 2*self.length + 2*self.width

class circle:
    pie = 3.1415

    def __init__(self, radius):
        self.radius = radius
        self.pie = 3.1415


    def calc_area(self):
        return self.pie * self.radius**2

    def calc_perimeter(self):
        return 2 * self.pie * self.radius*2



rect = rectangle(10,10)
cir = circle(1)

print(rect.calc_area(), rect.calc_perimeter())
print(cir.calc_area(), cir.calc_perimeter())
print(circle.pie)
