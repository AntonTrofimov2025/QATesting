from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Homeworks.hw6.core.common import Common

class CheckoutPage(Common):

    class Locator(Common.Locator):
        FIRSTNAME = 'first-name'
        LASTNAME = 'last-name'
        ZIPCODE = 'postal-code'
        FINISH_BUTTON = 'finish'
        CONTINUE_BUTTON = 'continue'
        TOTAL_PRICE_VALUE = 'summary_total_label'
        BACK_HOME_BUTTON = 'back-to-products'
        CONFIRMATION_TEXT_VALUE = 'complete-header'
        CONTAINER_ITEM_TEMPLATE = '#item_{}_title_link > div'

    def __init__(self, driver):
        super().__init__(driver)
        # self.driver = driver
        # self.wait = WebDriverWait(driver, 10)
        # self.actions = ActionChains(driver)

    def send_keys_by_id(self, locator, value):
        self.wait.until(EC.element_to_be_clickable((By.ID, locator))).send_keys(value)

    def fill_form_and_continue(self):
        self.wait.until(EC.url_contains('checkout-step-one.html'))
        assert 'checkout-step-one.html' in self.driver.current_url,\
            'Wrong url'
        self.send_keys_by_id(self.Locator.FIRSTNAME, 'Tony')
        self.send_keys_by_id(self.Locator.LASTNAME, 'Kwark')
        self.send_keys_by_id(self.Locator.ZIPCODE, '19392')
        self.click_continue()

    def assert_text_in_order_confirmation(self):
        self.wait.until(EC.url_contains('checkout-complete.html'))
        assert 'checkout-complete.html' in self.driver.current_url,\
            'Wrong url'
        assert 'Thank you for your order!' == self.get_text_of_order_confirmation(), \
            'Actual and expected texts don\'t match.'

    def get_text_of_order_confirmation(self):
        return self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, self.Locator.CONFIRMATION_TEXT_VALUE))).text

    def back_home(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, self.Locator.BACK_HOME_BUTTON))).click()

    def assert_total_price(self, expected_price: str):
        assert expected_price in self.total_price_value(), 'Price values do not match.'

    def total_price_value(self):
        return self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, self.Locator.TOTAL_PRICE_VALUE))).text

    def click_continue(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, self.Locator.CONTINUE_BUTTON))).click()

    def click_finish(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, self.Locator.FINISH_BUTTON))).click()

    def assert_container_item_name(self, containers_number: int, expected_name: str = 'Sauce Labs Backpack'):
        assert expected_name == self.get_text_of_container_item(containers_number), \
            'Actual and expected texts don\'t match.'

    def get_text_of_container_item(self, number):
        return self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, self.Locator.CONTAINER_ITEM_TEMPLATE.format(number)))).text

