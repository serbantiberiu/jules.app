import pdb
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from base_page import BasePage

class Login_page(BasePage):

    valid_username = "tashaphotographer@gmail.com"
    SIGN_UP_BTN = (By.XPATH, "//a[@href='/sign-up']")
    EMAIL = (By.CSS_SELECTOR, "input[placeholder='Enter your email']")
    PASSWORD = (By.CSS_SELECTOR, "input[placeholder='Enter your password']")
    LOGIN_BTN = (By.XPATH, "//button[@type='submit']")
    ERROR_MSG = (By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[2]/div/p')

    def open_login_page(self):
        self.chrome.get("https://jules.app/sign-in")

    def insert_email(self, email):
        self.chrome.find_element(*self.EMAIL).send_keys(email)

    def insert_password(self, password):
        self.chrome.find_element(*self.PASSWORD).send_keys(password)

    def clear_pass_field(self):
        self.chrome.find_element(*self.PASSWORD).send_keys(Keys.CONTROL+'a')
        self.chrome.find_element(*self.PASSWORD).send_keys(Keys.BACKSPACE)
        time.sleep(1)

    def click_signup_btn(self):
        self.chrome.find_element(*self.SIGN_UP_BTN).click()

    def check_login_error_message(self, expected_result):
        actual_result = self.chrome.find_element(*self.ERROR_MSG).text
        assert actual_result == expected_result, "error: message not displayed"

    def check_login_button_disabled(self):
        disabled_attribute = self.chrome.find_element(*self.LOGIN_BTN).get_attribute('disabled')
        assert disabled_attribute is not None, "error: Login button is not disabled"


