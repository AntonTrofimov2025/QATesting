from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Homeworks.hw6.core.common import Common

class CartPage(Common):

    class Locator(Common.Locator):
        CHECKOUT_BUTTON = 'checkout'

    def __init__(self, driver):
        super().__init__(driver)

    def assert_cart_page(self):
        self.wait.until(EC.url_contains('cart.html'))
        assert 'cart.html' in self.driver.current_url, \
            'Wrong url'

    def proceed_to_checkout(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, self.Locator.CHECKOUT_BUTTON))).click()