from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import pytest

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://itcareerhub.de/ru")
    yield driver
    driver.quit()

def test_is_display(driver):
    ich_logo = driver.find_element(By.CSS_SELECTOR, '[alt="IT Career Hub"]')
    assert ich_logo.is_displayed()

    programs = driver.find_element(By.CSS_SELECTOR, '[href="#submenu:more"]')
    programs_final = programs.find_element(By.TAG_NAME, 'span')
    assert programs_final.is_displayed()

    payments = driver.find_element(By.CSS_SELECTOR, '[href="#rec1921734713"] span')
    assert payments.is_displayed()

    about_us = driver.find_element(By.CSS_SELECTOR, '[href="#submenu:more2"] span')
    assert about_us.is_displayed()
    ActionChains(driver).move_to_element(about_us).perform()
    contacts = driver.find_element(By.CSS_SELECTOR, '[href="/ru/contact-us"]')
    assert contacts.is_displayed()

    reviews = driver.find_element(By.CSS_SELECTOR, '[href="/reviews"] span')
    assert reviews.is_displayed()

    blog = driver.find_element(By.CSS_SELECTOR, '[data-elem-id="176285426168494440"]')
    assert blog.is_displayed()

    change_ru = driver.find_element(By.CSS_SELECTOR, '[href = "/ru"]')
    assert change_ru.is_displayed()

    change_de = driver.find_element(By.CSS_SELECTOR, '[href="/"]')
    assert change_de.is_displayed()

    ActionChains(driver).move_to_element(about_us).perform()
    contacts.click()
    sleep(3)
    assert driver.current_url == 'https://itcareerhub.de/ru/contact-us'

    driver.set_window_size(640, 720)

    callback = driver.find_element(By.CSS_SELECTOR, '[data-elem-id="1754046238620"]')
    ActionChains(driver).scroll_by_amount(0, 450).perform()
    sleep(1)
    callback.click()
    sleep(1)
    assert "Запишитесь на " in driver.find_element(By.CSS_SELECTOR, '[field="tn_text_175871291756015470"]').text

