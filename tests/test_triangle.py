from src.Triangle import Triangle
import pytest


#   Площадь
@pytest.mark.parametrize("input_side, exp", [
    ((4, 5, 3), 6),
    ((7, 6, 5), 14.696938456699069),
    ((1, 2, 2), 0.9682458365518543),
    ((2, 2, 111), "raise ValueError"),
    ((0, 0, 0), "raise ValueError"),
    ((-1, 5, 0), "raise ValueError"),
    ((2, 0, -1), "raise ValueError")
])
def test_area(input_side, exp):
    triangle = Triangle(a=input_side[0], b=input_side[1], c=input_side[2])
    assert triangle.area == exp


#   Периметр
@pytest.mark.parametrize("input_side, exp", [
    ((4, 5, 3), 12),
    ((7, 6, 5), 18),
    ((1, 2, 2), 5),
    ((2, 2, 111), "raise ValueError"),
    ((0, 0, 0), "raise ValueError"),
    ((-1, 5, 0), "raise ValueError"),
    ((2, 0, -1), "raise ValueError")
])
def test_perimeter(input_side, exp):
    triangle = Triangle(a=input_side[0], b=input_side[1], c=input_side[2])
    assert triangle.perimeter == exp
