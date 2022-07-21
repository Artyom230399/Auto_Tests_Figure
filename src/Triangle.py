from src.Figure import Figure
import math


class Triangle(Figure):
    name = "Triangle"

    def __init__(self, a, b, c):
        if (a + b) < c or (a + c) < b or (c + b) < a or a < 0 or b < 0 or c < 0:
            print('raise ValueError')
            quit()
        self.a = a
        self.b = b
        self.c = c

    #   Функция расчета периметра
    @property
    def perimeter(self):
        return self.a + self.b + self.c

    #   Функция расчета площади
    @property
    def area(self):
        p_tr_2 = (self.a + self.b + self.c) / 2
        return math.sqrt(p_tr_2 * (p_tr_2 - self.a) * (p_tr_2 - self.b) * (p_tr_2 - self.c))


triangle = Triangle(a=5, b=8, c=11)

print(triangle.name)  # Вывод имени фигуры
print(triangle.perimeter)
print(triangle.area)
