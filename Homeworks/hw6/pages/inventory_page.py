from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)

    def assert_inventory_page(self):
        self.wait.until(EC.url_contains('inventory.html'))
        assert 'inventory.html' in self.driver.current_url, \
            'Wrong url'

    def scroll_up(self):
        self.actions.scroll_by_amount(0, -300).perform()

    def burger_click(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, 'react-burger-menu-btn'))).click()

    def reset_state(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, 'reset_sidebar_link'))).click()

    def add_many_cart_items(self, *args):
        for id_ in args:
            self.wait.until(EC.element_to_be_clickable((By.ID, id_))).click()

