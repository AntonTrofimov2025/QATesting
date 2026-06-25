import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

import pytest

current_path = os.path.dirname(os.path.abspath(__file__))
file_name = os.path.join(current_path, 'payment_options.png')

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.set_window_size(1280, 720)
    yield driver
    driver.quit()

def test_ich(driver):
    driver.get("https://itcareerhub.de/ru")
    payments = driver.find_element(By.XPATH,'//a[@class="tn-atom"]/div[@class="tn-atom__button-content"]/span')
    assert payments.text == "Способы оплаты", "The actual and expected results do not match."
    payments.click()
    sleep(2)
    driver.save_screenshot(file_name)
    sleep(1)

