from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://crossbrowsertesting.github.io/hover-menu.html')
    yield driver
    driver.quit()

def test_hover(driver):
    dropdown = driver.find_element(By.CSS_SELECTOR, '.dropdown-toggle')
    ActionChains(driver).move_to_element(dropdown).perform()
    secondary_menu = driver.find_element(By.CSS_SELECTOR, '.secondary-dropdown > .dropdown-toggle')
    ActionChains(driver).move_to_element(secondary_menu).perform()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[onclick="handleSecondaryAction()"]'))).click()
    assert 'Secondary Page' == driver.find_element(By.CSS_SELECTOR, '.jumbotron.secondary-clicked > h1').text