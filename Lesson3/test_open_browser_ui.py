from sys import executable

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from time import sleep
import pytest
# import os


@pytest.fixture
def driver():
    # service = Service("/Users/romansurkov/Documents/chromedriver-mac-arm64/chromedriver")
    # options = Options()
    # driver = webdriver.Chrome(service=service, options=options)
    # service = Service()
    # driver = webdriver.Firefox(service=service)
    driver = webdriver.Firefox()
    driver.maximize_window()
    # driver.set_window_size(640, 460)
    # driver = webdriver.Chrome(service=service)
    # driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

# BAD STYLE
# def test_about_page(driver):
#     driver.get("https://itcareerhub.de/ru")
#     sleep(3)
#     about_link = driver.find_element(By.LINK_TEXT, "О нас")
#     about_link.click()
#     sleep(3)

def test_about_page(driver):
    driver.get("https://itcareerhub.de/ru")
    sleep(1)
    about_link = driver.find_element(By.XPATH, '//a[@href="#submenu:more2"]/div/span')
    assert about_link.text == 'О нас', "The actual and expected results do not match."
    about_link.click()
    sleep(1)

# <a class="tn-atom t794__tm-link" href="#submenu:more2" data-tooltip-menu-id="2183881603">
# <div class="tn-atom__button-content"> <span class="tn-atom__button-text">О нас</span> </div>
# <span class="tn-atom__button-border"></span> </a>

# <i class="bicon bicon-times" aria-hidden="true"></i>
# <i class="icon bicon bicon-bars" aria-hidden="true"></i>

def test_about_page_xpath(driver):
    driver.get("https://www.berlin.de/")
    sleep(1)
    bar_link = driver.find_element(By.CSS_SELECTOR, "i.icon.bicon.bicon-bars")
    bar_link.click()
    menu_link = driver.find_element(By.XPATH, '//h2[@class="heading"]/span[text()="Menü"]')
    assert menu_link.is_displayed(), "The menu is not on the screen."
    sleep(1)
    # close_link = driver.find_element(By.XPATH, "//span[text()='Schließen: Menü']/..") IT WORKS!! :DD
    # close_link = driver.find_element(By.XPATH, '//div[@class="overlay__header"]/h2[@class="heading"]/../button/span[text()="Schließen: Menü"]/..') ALSO WORKS!! :D
    close_link = driver.find_element(By.XPATH,'//div[@class="overlay__header"]/h2[@class="heading"]/../button[./span[@class="aural" and text()="Schließen: Menü"]]')
    # close_link = driver.find_element(By.XPATH, '//i[@class="bicon bicon-times"]/parent::button') Not working :\
    close_link.click()
    sleep(1)
    assert not menu_link.is_displayed(), "The menu is still on the screen."
    # close_link = driver.find_element(By.XPATH, '//button[./i[@class="bicon bicon-times" and @aria-hidden="true"]]') NOT INTERACTABLE :'((
    # close_link.send_keys(Keys.ENTER)
    # close_link = driver.find_element(By.CSS_SELECTOR, 'button.close-button.js-button-overlay-close') NOT INTERACTABLE :'((
    sleep(1)
    driver.refresh()
    sleep(1)
    driver.get("https://www.google.de")
    sleep(1)
    driver.back()
    sleep(2)
    driver.forward()
    sleep(1)
    accept_link = driver.find_element(By.ID, "L2AGLb")
    accept_link.click()
    driver.refresh()
    sleep(2)

def test_berlin(driver):
    driver.get("https://itcareerhub.de/ru")
    # driver.refresh()
    driver.get("https://www.berlin.de")
    driver.save_screenshot("./Lesson3/berlin_s.png")
    driver.refresh()
    sleep(1)
    driver.back()
    sleep(1)
    driver.forward()
    driver.refresh()
    sleep(1)

# def test_berlin(driver):
#     driver.get("https://itcareerhub.de/ru")
#     driver.refresh()
#     driver.get("https://itcareerhub.de/ru/contact-us")
#     driver.save_screenshot("https://optim.tildacdn.net/tild6631-3437-4338-b639-313064353439/-/format/webp/image_792.png.webp")
#     sleep(2)
#     driver.refresh()
#     driver.back()
#     sleep(2)
#     driver.forward()
#     driver.refresh()
#     sleep(2)