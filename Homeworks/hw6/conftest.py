import pytest
from selenium import webdriver
from Homeworks.hw6.pages.sauce_demo_page import AuthPage
from Homeworks.hw6.pages.inventory_page import InventoryPage
from Homeworks.hw6.pages.cart_page import CartPage
from Homeworks.hw6.pages.checkout_page import CheckoutPage
from Homeworks.hw6.core.common import Common
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def setup(request):
    chrome_options = Options()
    chrome_options.add_argument('--incognito')
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    request.cls.driver = driver
    request.cls.auth_page = AuthPage(driver)
    request.cls.auth_page.open()
    request.cls.common = Common(driver)
    request.cls.inventory_page = InventoryPage(driver)
    request.cls.cart_page = CartPage(driver)
    request.cls.checkout_page = CheckoutPage(driver)

    yield driver
    driver.quit()


