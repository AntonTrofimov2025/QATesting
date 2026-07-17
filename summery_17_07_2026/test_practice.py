from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
import math

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def calc_exp(your_number: str) -> str:
    your_number = int(your_number)

    return str(math.log(abs(12 * math.sin(your_number))))

def test_expr(driver):
    driver.get('http://suninjuly.github.io/redirect_accept.html')
    (WebDriverWait(driver, 10)
     .until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.trollface.btn.btn-primary')))).click()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    number = WebDriverWait(driver, 10).until(
        lambda dr: dr.find_element(By.ID, 'input_value')
    ).text
    print(number)
    assert 'Math is real magic!' == driver.find_element(By.ID, 'simple_text').text.strip()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'answer'))).send_keys(calc_exp(number))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-primary'))).click()
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    assert 'Congrats, you\'ve passed the task! ' in alert.text
    alert.accept()

def test_sec_page(driver):
    driver.get('https://crossbrowsertesting.github.io/hover-menu.html')
    dropmenu = driver.find_element(By.CLASS_NAME, 'dropdown-toggle')
    ActionChains(driver).move_to_element(dropmenu).perform()
    sec_menu = driver.find_element(By.CSS_SELECTOR, '.secondary-dropdown > .dropdown-toggle')
    ActionChains(driver).move_to_element(sec_menu).perform()
    sec_action = driver.find_element(By.CSS_SELECTOR, '[onclick="handleSecondaryAction()"]')
    sec_action.click()
    assert 'Secondary Page' in driver.find_element(By.CSS_SELECTOR, '.jumbotron.secondary-clicked > h1').text

def test_drag_and_drop(driver):
    driver.get('https://crossbrowsertesting.github.io/drag-and-drop.html')
    drag = driver.find_element(By.ID, 'draggable')
    drop = driver.find_element(By.ID, 'droppable')
    ActionChains(driver).drag_and_drop(drag, drop).perform()
    assert 'Dropped!' in drop.find_element(By.TAG_NAME, 'p').text

def test_file(driver):
    driver.get('http://suninjuly.github.io/file_input.html')
    three_inputs = driver.find_elements(By.CSS_SELECTOR, '.form-group input')
    text = 'hel'
    for inp in three_inputs:
        inp.send_keys(text)
        text += 'lo'
    file_path = Path('C:\\', 'Users', 'ICH', 'Downloads', 'images.jpg')
    driver.find_element(By.ID, 'file').send_keys(str(file_path))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-primary'))).click()
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    assert "Congrats, you've passed the task!" in alert.text
    alert.accept()

