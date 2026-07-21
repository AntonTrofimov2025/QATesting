from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)

    def send_keys_by_id(self, arg, key):
        self.wait.until(EC.element_to_be_clickable((By.ID, arg))).send_keys(key)

    def fill_form(self):
        self.wait.until(EC.url_contains('checkout-step-one.html'))
        assert 'checkout-step-one.html' in self.driver.current_url,\
            'Wrong url'
        self.send_keys_by_id('first-name', 'Tony')
        self.send_keys_by_id('last-name', 'Kwark')
        self.send_keys_by_id('postal-code', '19392')

    def assert_text_in_order_confirmation(self):
        self.wait.until(EC.url_contains('checkout-complete.html'))
        assert 'checkout-complete.html' in self.driver.current_url,\
            'Wrong url'
        assert 'Thank you for your order!' == self.get_text_of_order_confirmation(), \
            'Actual and expected texts don\'t match.'

    def get_text_of_order_confirmation(self):
        return self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'complete-header'))).text

    def scroll_down_by(self, y):
        self.actions.scroll_by_amount(0, y).perform()

    def back_home(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, 'back-to-products'))).click()

    def assert_total_price(self, expected_price: str):
        assert expected_price in self.total_price_value(), 'Price values do not match.'

    def total_price_value(self):
        return self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'summary_total_label'))).text


