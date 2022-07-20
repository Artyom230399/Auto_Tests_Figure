from Figure import FigureName


class Rectangle:

    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    #   Функция расчета периметра
    def perimeter_rectangle(self):
        p_req = self.side_b + self.side_a + self.side_b + self.side_a
        print("Perimeter =", p_req)
        return p_req

    #   Функция расчета площади
    def area_rectangle(self):
        s_req = self.side_b * self.side_a
        print("Area =", s_req)
        return s_req


rectangle_name = FigureName(name="Rectangle")
rectangle = Rectangle(side_a=4, side_b=5)

rectangle_name.name_figure()  # Вывод имени фигуры
rectangle.perimeter_rectangle()  # Расчет периметра
rectangle.area_rectangle()  # Расчет площади
