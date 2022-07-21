from src.Figure import Figure


class Circle(Figure):
    name = "Circle"

    def __init__(self, r):
        if r <= 0:
            print("raise ValueError")
            quit()
        self.r = r

    #   Функция расчета периметра
    @property
    def perimeter(self):
        return 6.28 * self.r

    #   Функция расчета площади
    @property
    def area(self):
        return 3.14 * self.r ** 2


circle = Circle(r=6)

print(Circle.name)  # Вывод имени фигуры
print(circle.perimeter)
print(circle.area)
