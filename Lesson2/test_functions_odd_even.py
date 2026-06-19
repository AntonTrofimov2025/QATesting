from even_odd import EvenOddChecker
import pytest

@pytest.fixture()
def check():
    return EvenOddChecker()

def test_even_positive(check):
    assert check.is_even(2) is True
    assert check.is_even(3) is False

def test_even_negative(check):
    assert check.is_even(-2) is True
    assert check.is_even(-3) is False

def test_odd(check):
    assert check.is_odd(3) is True
    assert check.is_odd(2) is False

