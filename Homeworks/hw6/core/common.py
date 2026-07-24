from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Common:

    class Locator:
        ITEMS_IN_CART_VALUE = '#shopping_cart_container > a > span'
        LOGOUT = 'logout_sidebar_link'
        BURGER_MENU = 'react-burger-menu-btn'
        RESET_STATE = 'reset_sidebar_link'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)


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

    def log_out(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, self.Locator.LOGOUT))).click()

    def burger_click(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, self.Locator.BURGER_MENU))).click()

    def reset_state(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, self.Locator.RESET_STATE))).click()

    def scroll_up_by(self, arg: int):
        self.actions.scroll_by_amount(0, -arg).perform()

    def scroll_down_by(self, y: int):
        self.actions.scroll_by_amount(0, y).perform()

