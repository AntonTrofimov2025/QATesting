from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Homeworks.hw6.core.common import Common

class InventoryPage(Common):

    class Locator(Common.Locator):
        BACKPACK_BUTTON = "add-to-cart-sauce-labs-backpack"
        BOLT_SHIRT_BUTTON = "add-to-cart-sauce-labs-bolt-t-shirt"
        ONESIE_BUTTON = "add-to-cart-sauce-labs-onesie"
        CART_BUTTON = 'shopping_cart_link'

    def __init__(self, driver):
        super().__init__(driver)
        # self.driver = driver
        # self.wait = WebDriverWait(driver, 10)
        # self.actions = ActionChains(driver)

    def assert_inventory_page(self):
        self.wait.until(EC.url_contains('inventory.html'))
        assert 'inventory.html' in self.driver.current_url, \
            'Wrong url'

    def add_many_cart_items(self):
        for id_ in (self.Locator.BACKPACK_BUTTON,
                    self.Locator.BOLT_SHIRT_BUTTON,
                    self.Locator.ONESIE_BUTTON):
            self.wait.until(EC.element_to_be_clickable((By.ID, id_))).click()

    def add_backpack_to_cart(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, self.Locator.BACKPACK_BUTTON))).click()

    def add_sauce_labs_bolt_t_shirt_to_cart(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, self.Locator.BOLT_SHIRT_BUTTON))).click()

    def click_cart_button(self):
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, self.Locator.CART_BUTTON))).click()



