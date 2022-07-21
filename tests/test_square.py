from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Triangle import Triangle
from src.Square import Square
import pytest


#   Периметр
@pytest.mark.parametrize("input_side, exp", [
    (4, 16),
    (7, 49),
    (0, "raise ValueError"),
    (-1, "raise ValueError")
])
def test_area(input_side, exp):
    square = Square(input_side)
    assert square.area == exp


#   Площадь
@pytest.mark.parametrize("input_side, exp", [
    (5, 20),
    (3, 12),
    (0, "raise ValueError"),
    (-1, "raise ValueError")
])
def test_perimeter(input_side, exp):
    square = Square(input_side)
    assert square.perimeter == exp


#   Площадь квадрата + площадь круга
@pytest.mark.parametrize("input, input2, exp", [
    (2, 2, 16),
    (1, 1, 4),
    (0, 2, "raise ValueError"),
    (-1, 2, "raise ValueError")
])
def test_add_area_1(input, input2, exp):
    square = Square(input)
    circle = Circle(input2)
    assert square.add_area(figure_2=circle) == exp


#   Площадь квадрата + площадь прямоугольника
@pytest.mark.parametrize("input, input2, exp", [
    (2, (2, 4), 12),
    (0, (1, 2), 'raise ValueError'),
    (-1, (1, 2), "raise ValueError")
])
def test_add_area_2(input, input2, exp):
    square = Square(input)
    rectangle = Rectangle(side_a=input2[0], side_b=input2[1])
    assert square.add_area(figure_2=rectangle) == exp


#   Площадь квадрата + площадь треугольника
@pytest.mark.parametrize("input, input2, exp", [
    (2, (2, 4, 5), 7.799671038392666),
    (0, (1, 2, 2), 'raise ValueError'),
    (-1, (1, 2, 2), "raise ValueError")
])
def test_add_area_3(input, input2, exp):
    square = Square(input)
    triangle = Triangle(a=input2[0], b=input2[1], c=input2[2])
    assert square.add_area(figure_2=triangle) == exp
