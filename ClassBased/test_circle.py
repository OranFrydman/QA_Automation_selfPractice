import math

import pytest


class TestCircle:
    def setup_method(self,method):
        print("---------------------------------------------")
        print(f"\n --- Setting up --- \n{method}\n")

    def teardown_method(self,method):
        print(f"\n----Tearing down ---- \n{method}")
        print("---------------------------------------------")
    @pytest.mark.skip(reason="This test is useless now")
    def test_one(self):
        assert True
    @pytest.mark.circle
    def test_area_circle(self,circle):
        assert circle.area() == math.pi*circle.radius**2

    @pytest.mark.circle
    def test_perimeter_circle(self,circle):
        assert circle.perimeter() == math.pi*circle.radius*2

    @pytest.mark.circle
    def test_circle_is_not_rectangle_circle(self,circle,rectangle):
        assert circle != rectangle


    #run pytest -m circle to run the marked group