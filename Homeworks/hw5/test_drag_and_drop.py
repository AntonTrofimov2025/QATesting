from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pytest

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://crossbrowsertesting.github.io/drag-and-drop.html')
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_dr_n_dr(driver):
    drag = driver.find_element(By.ID, 'draggable')
    drop = driver.find_element(By.ID, 'droppable')
    ActionChains(driver).drag_and_drop(drag, drop).perform()
    assert 'Dropped!' == drop.find_element(By.TAG_NAME, 'p').text

