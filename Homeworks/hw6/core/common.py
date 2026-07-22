from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Common:

    class Locator:
        ITEMS_IN_CART_VALUE = '#shopping_cart_container > a > span'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # def click_by_id(self, arg):
    #     self.wait.until(EC.element_to_be_clickable((By.ID, arg))).click()

    def fetch_cart_elements_quantity(self):
        return self.wait.until(
            lambda dr: dr.find_element(By.CSS_SELECTOR, self.Locator.ITEMS_IN_CART_VALUE)
        ).text

    def assert_elements_quantity_by_number(self, your_number: int):
        if not your_number or your_number <= 0:
            assert your_number <= 0
            return
        assert str(your_number) == self.fetch_cart_elements_quantity(), \
            'Wrong elements quantity.'