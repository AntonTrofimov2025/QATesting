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

def test_itch_in_blue_button(driver):
    driver.get('http://uitestingplayground.com/textinput')
    driver.find_element(By.ID, 'newButtonName').send_keys('ITCH')
    blue_button = driver.find_element(By.ID, 'updatingButton')
    blue_button.click()

    # assert 'ITCH' in blue_button.text # Works, but too simple approach and not reliable.
    (WebDriverWait(driver, 10)
            .until(EC.text_to_be_present_in_element
            ((By.ID, 'updatingButton'), 'ITCH')))

    assert blue_button.text == 'ITCH', 'ITCH unfortunately not appeared.'

def test_wait_till_all_images(driver):
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')

    # assert (WebDriverWait(driver, 10)              # Not reliable :'(
    #         .until(EC.visibility_of_element_located
    #         ((By.CSS_SELECTOR, '#image-container > img:nth-child(4)'))))

    # (WebDriverWait(driver, 10)             # Good, but another option below is better :)
    #         .until(lambda dr:
    #         len([image.is_displayed() for image in dr.find_elements(By.CSS_SELECTOR, '#image-container > img') if image.is_displayed()]
    #                             ) == 4))

    (WebDriverWait(driver, 10)       # Best way! Works x2 faster than the version above ;)
            .until(lambda dr:
            sum(1 for image in dr.find_elements(By.CSS_SELECTOR, '#image-container > img') if image.is_displayed()
                                ) == 4))

    attr_3rd_img = driver.find_element(By.CSS_SELECTOR, '#image-container > img:nth-child(3)').get_attribute('alt')

    assert attr_3rd_img == 'award', 'award unfortunately not appeared.'