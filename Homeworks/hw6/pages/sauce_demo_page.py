from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthPage:

    class Locator:
        PASSWORD = 'secret_sauce'
        USERNAME_FIELD = 'user-name'
        PASSWORD_FIELD = 'password'
        LOGIN_BUTTON = 'login-button'
        LOGOUT = 'logout_sidebar_link'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self):
        return self.wait.until(EC.presence_of_element_located((By.ID, self.Locator.USERNAME_FIELD)))

    def enter_password(self):
        return self.wait.until(EC.presence_of_element_located((By.ID, self.Locator.PASSWORD_FIELD)))

    def login_with_credentials(self, username):
        self.enter_username().send_keys(username)
        self.enter_password().send_keys(self.Locator.PASSWORD)
        self.click_login_button()
        assert "inventory.html" in self.driver.current_url,\
            'Wrong url'

    def click_login_button(self):
        self.find_element_by_id(self.Locator.LOGIN_BUTTON).click()

    def find_element_by_id(self, arg):
        return self.driver.find_element(By.ID, arg)

    def log_out(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, self.Locator.LOGOUT))).click()


