

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() > other.area()
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented

    def __repr__(self):
        return f"Rectangle: Width: {self.width} Height {self.height}"

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area() == other.area()


rectangle1 = Rectangle(10, 20)
rectangle2 = Rectangle(15, 20)

rectangle2.is_square()

print(rectangle2==rectangle1)
