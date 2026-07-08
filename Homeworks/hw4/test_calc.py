from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
    yield driver
    driver.quit()

def test_15_after_45_seconds(driver):
    input_delay = driver.find_element(By.ID, 'delay')
    input_delay.clear()
    input_delay.send_keys('45')

    find_7 = driver.find_element(By.CSS_SELECTOR, '.keys > .btn:nth-child(1)')
    find_7.click()

    find_plus = driver.find_element(By.CSS_SELECTOR, '.keys > .btn:nth-child(4)')
    find_plus.click()

    find_8 = driver.find_element(By.CSS_SELECTOR, '.keys > .btn:nth-child(2)')
    find_8.click()

    find_equal = driver.find_element(By.CSS_SELECTOR, '.keys > .btn:nth-child(15)')
    find_equal.click()

    assert (WebDriverWait(driver, 45)
            .until(EC.text_to_be_present_in_element
                               ((By.CSS_SELECTOR, 'div.screen'), '15'))), "15 has not appeared :'("