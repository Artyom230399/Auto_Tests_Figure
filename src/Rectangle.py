from src.Figure import Figure


class Rectangle(Figure):
    name = "Rectangle"

    def __init__(self, side_a, side_b):
        if side_a <= 0 or side_b <= 0:
            print("raise ValueError")
            quit()
        self.side_a = side_a
        self.side_b = side_b

    #   Функция расчета периметра
    @property
    def perimeter(self):
        return (self.side_b + self.side_a) * 2

    #   Функция расчета площади
    @property
    def area(self):
        return self.side_b * self.side_a


rectangle = Rectangle(side_a=4, side_b=5)

print(Rectangle.name)  # Вывод имени фигуры
print(rectangle.perimeter)
print(rectangle.area)
