from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://suninjuly.github.io/huge_form.html')
    yield driver
    driver.quit()

def test_alert(driver):
    all_inputs = driver.find_elements(By.CSS_SELECTOR, 'input[type="text"]')
    for input_ in all_inputs:
        input_.send_keys('Hello')
    driver.find_element(By.CSS_SELECTOR, '.btn.btn-default').click()
    # assert "Congrats, you've passed the task!" in driver.switch_to.alert.text
    alert = WebDriverWait(driver, 15).until(EC.alert_is_present())
    assert "Congrats, you've passed the task!" in alert.text
    alert.accept()

