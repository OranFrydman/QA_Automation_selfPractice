import pytest
import shapes as shapes

def test_square_area(square):
    assert square.area() == square.side_length**2

@pytest.mark.parametrize("side_length,expected_area", [(5, 25), (3, 9), (4, 16), (9, 81)])
def test_multiple_square_areas(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area


@pytest.mark.parametrize("side_length,expected_perimeter",[(3,12),(2,8),(6,24)])
def test_multiple_square_perimeters(side_length,expected_perimeter):
    assert shapes.Square(side_length).perimeter() == expected_perimeter