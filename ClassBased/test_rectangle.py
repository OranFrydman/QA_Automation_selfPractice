
class TestCircle:
    def setup_method(self,method):
        print("---------------------------------------------")
        print(f"\n --- Setting up --- \n{method}\n")

    def teardown_method(self,method):
        print(f"\n----Tearing down ---- \n{method}")
        print("---------------------------------------------")

    def test_area(self,rectangle):
        assert rectangle.area() == 10

    def test_perimeter(self,rectangle):
        assert rectangle.perimeter() == 14

