from simple_math import SimpleMath
import pytest

@pytest.fixture()
def calc():
    return SimpleMath()

@pytest.mark.square
def test_square_positive(calc):
    assert calc.square(2) == 4

@pytest.mark.square
def test_square_negative(calc):
    assert calc.square(-4) == 16

@pytest.mark.cube
def test_cube_negative(calc):
    assert calc.cube(-3) == -27

@pytest.mark.cube
def test_cube_positive(calc):
    assert calc.cube(3) == 27

@pytest.mark.mul
def test_multiply_positive_and_zero(calc):
    assert calc.mul(6, 0) == 0

@pytest.mark.mul
def test_multiply_positive(calc):
    assert calc.mul(7, 7) == 49

@pytest.mark.mul
def test_multiply_negative(calc):
    assert calc.mul(-5, -8) == 40

@pytest.mark.div
def test_division_zero(calc):
    with pytest.raises(ArithmeticError, match="Division by zero is impossible!!"):
        calc.div(5, 0)

@pytest.mark.div
def test_division_positive(calc):
    assert calc.div(16, 4) == 4

@pytest.mark.div
def test_division_float(calc):
    assert calc.div(4.5, 2) == pytest.approx(2.25)

@pytest.mark.div
def test_division_negative(calc):
    assert calc.div(8, -2) == -4