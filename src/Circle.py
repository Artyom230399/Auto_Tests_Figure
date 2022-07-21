from src.Figure import Figure


class Circle(Figure):
    NAME = "Circle"

    def __init__(self, r):
        self.r = r

    #   Функция расчета периметра
    @property
    def perimeter(self):
        if self.r <= 0:
            return "raise ValueError"
        else:
            return 6 * self.r

    #   Функция расчета площади
    @property
    def area(self):
        if self.r <= 0:
            return "raise ValueError"
        else:
            return 3 * self.r ** 2

    def add_area(self, figure_2):
        if self.area == "raise ValueError" or figure_2 == "raise ValueError":
            return "raise ValueError"
        else:
            return self.area + figure_2.area

# circle = Circle(r=2)
#
#
# print(Circle.NAME)
# print(circle.perimeter)
# print(circle.area)
