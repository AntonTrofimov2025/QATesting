from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:

    class Locator:
        CHECKOUT_BUTTON = 'checkout'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def assert_cart_page(self):
        self.wait.until(EC.url_contains('cart.html'))
        assert 'cart.html' in self.driver.current_url, \
            'Wrong url'

    def proceed_to_checkout(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, self.Locator.CHECKOUT_BUTTON))).click()