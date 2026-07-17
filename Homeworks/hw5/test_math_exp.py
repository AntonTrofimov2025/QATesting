from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest
import math


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def calc_exp(die_nummer_bitte: str) -> str:
    return str(math.log(abs(12 * math.sin(int(die_nummer_bitte)))))


def test_math_exp(driver):
    driver.get('https://suninjuly.github.io/math.html')
    value = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'input_value'))
    ).text
    print(value)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'answer'))
    ).send_keys(calc_exp(value))
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'robotCheckbox'))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'robotsRule'))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-default'))
    ).click()
    alert = WebDriverWait(driver, 10).until(
        EC.alert_is_present()
    )
    assert "Congrats, you've passed the task!" in alert.text
    alert.accept()

