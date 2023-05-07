from selenium.webdriver.common.by import By

from browser import Browser

class Login_page(Browser):

    EMAIL = (By.CSS_SELECTOR, "input[placeholder='Enter your email']")
    PASSWORD = (By.CSS_SELECTOR, "input[placeholder='Enter your password']")
    LOGIN_BTN = (By.XPATH, "//button[@type='submit']")
    ERROR_MSG = (By.XPATH, "//*[text()='Please enter your password!']")

    def open_login_page(self):
        self.chrome.get("")

    def insert_email(self, email):
        self.chrome.find_element(*self.EMAIL).send_keys(email)

    def empty_field_password(self, password):
        self.chrome.find_element(*self.PASSWORD).send_keys(password)

    def check_login_error_message(self, expected_result):
        actual_result = self.chrome.find_element(*self.ERROR_MSG).text
        assert actual_result == expected_result, "Please enter your password!"

    def login_button_disabled(self):
        return self.chrome.find_element(*self.LOGIN_BTN).is_disabled()

