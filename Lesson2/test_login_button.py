from login_button import LoginButton
import pytest

@pytest.fixture()
def check():
    return LoginButton()

def test_get_label(check):
    assert check.get_label() == 'Login'
    assert check.get_label() != 'Hellogin'

def test_enabled(check):
    assert check.is_enabled() is True

def test_enable(check):
    check.disable()
    check.enable()
    assert check.is_enabled() is True

def test_disable(check):
    check.disable()
    assert check.is_enabled() is False

