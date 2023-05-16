import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

from browser import Browser


class Signup_Page(Browser):
    valid_email_address = "tashaphotographer@gmail.com"
    LOGIN_BTN = (By.XPATH, '//button[@data-test-id="go-to-login-btn"]')
    PERSONAl_BTN = (By.XPATH, "//input[@type='radio' and @value='personal']")
    CONTINUE_BTN = (By.XPATH, "//button[@data-test-id='select-account-continue-btn']")
    FIRST_NAME_CONTINUE_BTN = (By.XPATH, "//button[@data-test-id='first-name-continue-btn']")
    LAST_NAME_CONTINUE_BTN = (By.XPATH, "//button[@data-test-id='last-name-continue-btn']")
    INPUT_FIELD = (By.XPATH, "//input[@type='text']")
    ERROR_MSG = (By.XPATH, "//*[@id='root']/div/div[4]/div[2]/div/div[2]/div/p")

    def open_signin_page(self):
        self.chrome.get("https://jules.app/sign-in")

    def click_login_button(self):
        self.chrome.find_element(*self.LOGIN_BTN).click()

    def click_personal_btn(self):
        self.chrome.find_element(*self.PERSONAl_BTN).click()

    def input_field(self, input_text):
        self.chrome.find_element(*self.INPUT_FIELD).send_keys(input_text)

    def click_continue_btn(self):
        try:
            self.chrome.find_element(*self.CONTINUE_BTN).click()
        except:
            try:
                self.chrome.find_element(*self.FIRST_NAME_CONTINUE_BTN).click()
            except:
                self.chrome.find_element(*self.LAST_NAME_CONTINUE_BTN).click()
        time.sleep(2)

    def check_error_message(self, expected_result):
        actual_result = self.chrome.find_element(*self.ERROR_MSG).text
        assert actual_result == expected_result, f"error: message is not as expected {expected_result}"

    def clear_email_input(self):
        self.chrome.find_element(*self.INPUT_FIELD).clear()

    def check_error_message_not_displayed(self):
        assert EC.invisibility_of_element_located(self.ERROR_MSG), "error: the message is still displayed"
