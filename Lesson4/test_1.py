from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_(driver):
    driver.get('https://the-internet.herokuapp.com/jqueryui/menu#')
    (WebDriverWait(driver, 5)
     .until(EC.element_to_be_clickable((By.ID, 'ui-id-3')))).click()

    (WebDriverWait(driver, 5)
     .until(EC.element_to_be_clickable((By.ID, 'ui-id-4')))).click()

    (WebDriverWait(driver, 5)
     .until(EC.element_to_be_clickable((By.ID, 'ui-id-5')))).click()

def test_2(driver):
    driver.get('https://the-internet.herokuapp.com/entry_ad')
    (WebDriverWait(driver, 5)
     .until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.modal-footer > p')))).click()

