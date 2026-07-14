from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://suninjuly.github.io/file_input.html')
    yield driver
    driver.quit()

def test_file(driver):
    driver.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys('Igor')
    driver.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys('Iwanowich')
    driver.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys('igiv312312@yahoo.com')
    file_path = 'C:\\Users\\ICH\\Downloads\\images.jpg'
    driver.find_element(By.ID, 'file').send_keys(file_path)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-primary'))).click()
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    assert "Congrats, you've passed the task!" in alert.text
    alert.accept()

