class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        print("Площа фігури")


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def show(self):
        print(f"Коло: колір — {self.color}, радіус — {self.radius}")


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def show(self):
        print(f"Прямокутник: колір — {self.color}, ширина — {self.width}, висота — {self.height}")


circle = Circle("червоний", 5)
rectangle = Rectangle("синій", 10, 6)

circle.show()
rectangle.show()