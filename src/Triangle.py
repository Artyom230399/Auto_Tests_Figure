from Figure import FigureName
import math


class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    #   Функция расчета периметра
    def perimeter_triangle(self):
        if (self.a + self.b) > self.c and (self.a + self.c) > self.b and (
                self.c + self.b) > self.a and self.a > 0 and self.b > 0 and self.c > 0:
            p_tr = self.a + self.b + self.c
            print("Perimeter =", p_tr)
            return p_tr
        else:
            print("raise ValueError")

    #   Функция расчета площади
    def area_triangle(self):
        if (self.a + self.b) > self.c and (self.a + self.c) > self.b and (
                self.c + self.b) > self.a and self.a > 0 and self.b > 0 and self.c > 0:
            p_tr_2 = (self.a + self.b + self.c) / 2
            s_tr = math.sqrt(p_tr_2 * (p_tr_2 - self.a) * (p_tr_2 - self.b) * (p_tr_2 - self.c))
            print("Area =", s_tr)
            return s_tr
        else:
            print("raise ValueError")


triangle = Triangle(a=5, b=8, c=11)
triangle_name = FigureName(name="Triangle")

triangle_name.name_figure()  # Вывод имени фигуры
triangle.perimeter_triangle()  # Расчет периметра
triangle.area_triangle()  # Расчет площади
