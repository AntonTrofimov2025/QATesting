from calculator import Calculator
import pytest

@pytest.fixture()
def calc():
    return Calculator()

@pytest.mark.skip(reason='Test is gonna be fixed later')
def test_sum_positive_numbers(calc):
    assert calc.sum(4, 5) == 9

@pytest.mark.skipif(condition="sys.version_info < (3,8)",
                    reason="Required Python 3.8 or newer")
def test_sum_negative_numbers(calc):
    assert calc.sum(-6, -10) == -16

@pytest.mark.xfail(strict=True, reason="Work on this method in progress")
def test_sum_positive_and_negative(calc):
    assert calc.sum(-6, 6) == 1 # Should be 0

def test_sum_floats(calc):
    assert round(calc.sum(5.6, 4.3), 1) == 9.9

def test_sum_with_zero(calc):
    assert calc.sum(10, 0) == 10

def test_division(calc):
    assert calc.div(10, 2) == 5

@pytest.mark.positive_test
def test_division_by_zero(calc):
    with pytest.raises(ArithmeticError, match="Impossible to divide by zero :\)"):
        calc.div(10, 0)

def test_avg_empty_list(calc):
    assert calc.avg([]) == 0

def test_avg_list(calc):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
    assert calc.avg(numbers) == 5

