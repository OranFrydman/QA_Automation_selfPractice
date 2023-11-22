import math


class Shape:

    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius

    def area(self):
        return math.pi*self.radius**2

    def perimeter(self):
        return math.pi*self.radius*2




class Rectangle(Shape):
    def __init__(self,side_length,width):
        self.side_length=side_length
        self.width = width

    def area(self):
        return self.side_length*self.width

    def perimeter(self):
        return (self.side_length*2)+(self.width*2)

class Square(Rectangle):
    def __init__(self,side_length):
        super().__init__(side_length,side_length)