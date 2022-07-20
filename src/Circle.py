from Figure import FigureName


class Circle:

    def __init__(self, r):
        self.r = r

    #   Функция расчета периметра
    def perimeter_circle(self):
        p_cir = 6.28 * self.r
        print(p_cir)
        return p_cir

    #   Функция расчета площади
    def area_circle(self):
        s_cir = 3.14 * self.r ** 2
        print(s_cir)
        return s_cir


circle = Circle(r=6)
circle_name = FigureName(name="Circle")

circle_name.name_figure()
circle.perimeter_circle()
circle.area_circle()
