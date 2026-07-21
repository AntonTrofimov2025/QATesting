from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def get_username_input(self):
        return self.wait.until(EC.presence_of_element_located((By.ID, "user-name")))

    def get_password_input(self):
        return self.wait.until(EC.presence_of_element_located((By.ID, "password")))

    def input_username_password(self, username):
        self.get_username_input().send_keys(username)
        self.get_password_input().send_keys('secret_sauce')
        self.click_login_button()
        assert "inventory.html" in self.driver.current_url,\
            'Wrong url'

    def click_login_button(self):
        self.find_element_by_id('login-button').click()

    def find_element_by_id(self, arg):
        return self.driver.find_element(By.ID, arg)

    def log_out(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, 'logout_sidebar_link'))).click()


