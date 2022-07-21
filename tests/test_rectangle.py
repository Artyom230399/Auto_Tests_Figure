from src.Rectangle import Rectangle
import pytest


#   Площадь
@pytest.mark.parametrize("input_side, exp", [
    ((4, 5), 20),
    ((7, 2), 14),
    ((0, 2), "raise ValueError"),
    ((2, 0), "raise ValueError"),
    ((0, 0), "raise ValueError"),
    ((-1, 5), "raise ValueError"),
    ((3, -1), "raise ValueError")
])
def test_area(input_side, exp):
    rectangle = Rectangle(side_a=input_side[0], side_b=input_side[1])
    assert rectangle.area == exp


#   Периметр
@pytest.mark.parametrize("input_side, exp", [
    ((4, 5), 18),
    ((7, 5), 24),
    ((0, 2), "raise ValueError"),
    ((2, 0), "raise ValueError"),
    ((0, 0), "raise ValueError"),
    ((-1, 5), "raise ValueError"),
    ((3, -1), "raise ValueError")
])
def test_perimeter(input_side, exp):
    rectangle = Rectangle(side_a=input_side[0], side_b=input_side[1])
    assert rectangle.perimeter == exp
