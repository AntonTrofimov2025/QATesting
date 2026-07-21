from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Common:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_by_id(self, arg):
        self.wait.until(EC.element_to_be_clickable((By.ID, arg))).click()

    def get_cart_link_n_click(self):
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_link"))).click()

    def assert_naming_of_container_item(self, containers_number):
        assert 'Sauce Labs Backpack' == self.get_text_of_container_item(containers_number), \
            'Actual and expected texts don\'t match.'

    def get_text_of_container_item(self, number):
        return self.driver.find_element(By.CSS_SELECTOR, f'#item_{number}_title_link > div').text

    def fetch_cart_elements_quantity(self):
        return self.wait.until(
            lambda dr: dr.find_element(By.CSS_SELECTOR, '#shopping_cart_container > a > span')
        ).text

    def assert_elements_quantity_by_number(self, your_number: int):
        assert str(your_number) == self.fetch_cart_elements_quantity(), \
            'Wrong elements quantity.'