from age_validator import AgeValidator
import pytest

@pytest.fixture()
def check():
    return AgeValidator()

def test_check_age_positive(check):
    assert check.is_adult(18) is True
    assert check.is_adult(18.2) is True

def test_check_age_negative(check):
    assert check.is_adult(17) is False
    assert check.is_adult(0) is False
    assert check.is_adult(-55) is False

