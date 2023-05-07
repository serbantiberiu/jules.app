from selenium.webdriver.common.by import By

from browser import Browser

class Signup_Page(Browser):
    SIGN_UP_BTN = (By.XPATH, "//a[@href='/sign-up']")
    PERSONAl_BTN = (By.XPATH, "//input[@class='jss204']")
    CONTINUE_BTN = (By.XPATH, "//button[@type='button']")
    FIRST_NAME_INPUT = (By.XPATH, "//input[@type='text']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='Type your answer here...']")
    EMAIL_INPUT = (By.XPATH, "//input[@class='MuiInputBase-input MuiFilledInput-input']")
    ERROR_MSG = (By.XPATH, "//*[text()='Please enter a valid email address.']")

    def open_signin_page(self):
        self.chrome.get("")

    def click_signup_btn(self):
        self.chrome.find_element(*self.SIGN_UP_BTN).click()

    def click_personal_btn(self):
        self.chrome.find_element(*self.PERSONAl_BTN).click()

    def click_continue_btn(self):
        self.chrome.find_element(*self.CONTINUE_BTN).click()

    def input_correct_firstname(self, first_name):
        self.chrome.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)

    def input_correct_lastname(self, last_name):
        self.chrome.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)

    def input_wrong_email(self, email):
        self.chrome.find_element(*self.EMAIL_INPUT).send_keys(email)

    def verify_error_message(self):
        actual_result = self.chrome.find_element(*self.ERROR_MSG).text
        assert actual_result == expected_result, "Please enter a valid email address."

    def clear_email_input(self):
        self.chrome.find_element(*self.EMAIL_INPUT).clear()

    def input_correct_email(self, correct_email):
        self.chrome.find_element(*self.EMAIL_INPUT).send_keys(correct_email)

    def error_message_displayed(self):
        try:
            error = self.chrome.find_element(*self.ERROR_MSG)
            return error.is_displayed()
        except:
            return False