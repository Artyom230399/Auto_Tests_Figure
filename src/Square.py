from Figure import FigureName


class Square:

    def __init__(self, side):
        self.side = side

    #   Функция расчета периметра
    def perimeter_square(self):
        p_sq = self.side * 4
        print("Perimeter =", p_sq)
        return p_sq

    #   Функция расчета площади
    def area_square(self):
        s_sq = self.side * self.side
        print("Area =", s_sq)
        return s_sq


square = Square(side=10)
square_name = FigureName(name="Square")

square_name.name_figure()  # Вывод имени фигуры
square.perimeter_square()  # Расчет периметра
square.area_square()  # Расчет площади
