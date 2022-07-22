# from Circle import Circle
from src.Figure import Figure


class Square(Figure):
    NAME = "Square"

    def __init__(self, side):
        self.side = side

    #   Функция расчета периметра
    @property
    def perimeter(self):
        if self.side <= 0:
            return "raise ValueError"
        else:
            return self.side * 4

    #   Функция расчета площади
    @property
    def area(self):
        if self.side <= 0:
            return "raise ValueError"
        else:
            return self.side * self.side

    def add_area(self, figure_2):
        if self.area == "raise ValueError" or figure_2 == "raise ValueError":
            return "raise ValueError"
        else:
            return self.area + figure_2.area

# square = Square(side=1)
# circle = Circle(r=2)
#
# print(Square.NAME)
# print(square.perimeter)
# print(square.area)
# print(square.add_area(circle))
