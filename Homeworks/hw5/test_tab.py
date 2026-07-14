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
    driver.get('http://suninjuly.github.io/redirect_accept.html')
    yield driver
    driver.quit()

def calc_exp(x: int) -> int | float:
    return math.log(abs(12 * math.sin(x)))

def test_open_tab(driver):
    (WebDriverWait(driver, 10)
     .until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.trollface.btn.btn-primary')))).click()
    tabs = driver.window_handles
    print(tabs)
    driver.switch_to.window(tabs[1])
    target_number = int(driver.find_element(By.ID, 'input_value').text)
    driver.find_element(By.ID, 'answer').send_keys(str(calc_exp(target_number)))
    driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    assert "Congrats, you've passed the task! " in alert.text
    alert.accept()

