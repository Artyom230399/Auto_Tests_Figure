from Figure import FigureName
import math


class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def triangle_check(self):
        if (self.a + self.b) > self.c and (self.a + self.c) > self.b and (
                self.c + self.b) > self.a and self.a > 0 and self.b > 0 and self.c > 0:
            pass
        else:
            print("raise ValueError")
            quit()

    #   Функция расчета периметра
    def perimeter_triangle(self):
        p_tr = self.a + self.b + self.c
        print("Perimeter =", p_tr)
        return p_tr

    #   Функция расчета площади
    def area_triangle(self):
        p_tr_2 = (self.a + self.b + self.c) / 2
        s_tr = math.sqrt(p_tr_2 * (p_tr_2 - self.a) * (p_tr_2 - self.b) * (p_tr_2 - self.c))
        print("Area =", s_tr)
        return s_tr


triangle = Triangle(a=5, b=8, c=111)
triangle_name = FigureName(name="Triangle")

triangle.triangle_check()  # Проверка треугольника на существование
triangle_name.name_figure()  # Вывод имени фигуры
triangle.perimeter_triangle()  # Расчет периметра
triangle.area_triangle()  # Расчет площади
