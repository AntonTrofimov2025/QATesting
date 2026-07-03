from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

import pytest

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('https://suninjuly.github.io/cats.html')
    yield driver
    driver.quit()

def test_cat_memes_header(driver):
    # cat_memes_text = driver.find_element(By.CSS_SELECTOR, '[class="jumbotron-heading"]')
    cat_memes_text = driver.find_element(By.CSS_SELECTOR, '.jumbotron-heading')
    assert 'Cat memes' == cat_memes_text.text

def test_9mins_in_1(driver):
    text_9mins = driver.find_element(By.CSS_SELECTOR, '.col-sm-4:nth-child(1)')
    text_9mins_small = text_9mins.find_element(By.TAG_NAME, 'small')
    assert '9 mins' == text_9mins_small.text

def test_i_love_u(driver):
    text_in_sixth_card = driver.find_element(By.CSS_SELECTOR, '.col-sm-4:nth-child(6)')
    text_in_sixth_card_p = text_in_sixth_card.find_element(By.TAG_NAME, 'p')
    assert 'I love you so much' == text_in_sixth_card_p.text

def test_album_text_near_photo(driver):
    album_in_photo = driver.find_element(By.CSS_SELECTOR, '[href="#"]')
    album_in_photo_strong = album_in_photo.find_element(By.TAG_NAME, 'strong')
    assert album_in_photo_strong.text == 'Cats album'

def test_1_is_displayed(driver):
    first_displayed = driver.find_element(By.CSS_SELECTOR, '.col-sm-4:nth-child(1)')
    assert first_displayed.is_displayed()

def test_cat_displayed(driver):
    # cat_display = driver.find_element(By.CSS_SELECTOR, '[src="images/lenin_cat.jpg"]')
    # cat_display = driver.find_element(By.CSS_SELECTOR, '.col-sm-4:nth-child(3) img')
    cat_display = driver.find_element(By.CSS_SELECTOR, '.col-sm-4:nth-child(3)')
    cat_display_img = cat_display.find_element(By.TAG_NAME, 'img')
    assert cat_display_img.is_displayed()

def test_camera_icon(driver):
    camera_photo = driver.find_element(By.TAG_NAME, 'svg')
    assert camera_photo.is_displayed()

def test_photo_icon_is_displayed(driver):
    cat_photo = driver.find_elements(By.CSS_SELECTOR, '.col-sm-4')
    for card in cat_photo:
        assert card.is_displayed()
    assert len(cat_photo)