from src.Figure import Figure


class Square(Figure):
    name = "Square"

    def __init__(self, side):
        if side <= 0:
            print('raise ValueError')
            quit()
        self.side = side

    #   Функция расчета периметра
    @property
    def perimeter(self):
        return self.side * 4

    #   Функция расчета площади
    @property
    def area(self):
        return self.side * self.side


square = Square(side=1)

print(Square.name)  # Вывод имени
print(square.perimeter)
print(square.area)
