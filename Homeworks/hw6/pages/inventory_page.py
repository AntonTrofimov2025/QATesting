from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class InventoryPage:

    class Locator:
        BACKPACK_BUTTON = "add-to-cart-sauce-labs-backpack"
        BOLT_SHIRT_BUTTON = "add-to-cart-sauce-labs-bolt-t-shirt"
        ONESIE_BUTTON = "add-to-cart-sauce-labs-onesie"
        BURGER_MENU = 'react-burger-menu-btn'
        RESET_STATE = 'reset_sidebar_link'
        CART_BUTTON = 'shopping_cart_link'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)

    def assert_inventory_page(self):
        self.wait.until(EC.url_contains('inventory.html'))
        assert 'inventory.html' in self.driver.current_url, \
            'Wrong url'

    def scroll_up_by(self, arg: int):
        self.actions.scroll_by_amount(0, -arg).perform()

    def burger_click(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, self.Locator.BURGER_MENU))).click()

    def reset_state(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, self.Locator.RESET_STATE))).click()

    def add_many_cart_items(self):
        for id_ in (self.Locator.BACKPACK_BUTTON,
                    self.Locator.BOLT_SHIRT_BUTTON,
                    self.Locator.ONESIE_BUTTON):
            self.wait.until(EC.element_to_be_clickable((By.ID, id_))).click()

    def add_backpack_to_cart(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, self.Locator.BACKPACK_BUTTON))).click()

    def click_cart_button(self):
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, self.Locator.CART_BUTTON))).click()



