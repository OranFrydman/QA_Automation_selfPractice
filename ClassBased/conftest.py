
import pytest
import shapes as shapes
import math
@pytest.fixture
def rectangle():
    return shapes.Rectangle(5,2)

@pytest.fixture
def square():
    return shapes.Square(5)

@pytest.fixture
def circle():
    return shapes.Circle(5)