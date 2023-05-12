from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import Login_page


class Inventory_page(Login_page):
    username = "standard_user"
    password = "secret_sauce"
    BIKE_LIGHT_ADD_CHART = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
    BIKE_LIGHT_REMOVE = (By.XPATH, "//button[@id='remove-sauce-labs-bike-light']")

    def login(self):
        self.open_login_page()
        self.insert_username(self.username)
        self.insert_password(self.password)
        self.click_login_btn()

    def press_add_char_item(self, item):
        self.chrome.find_element(*self.BIKE_LIGHT_ADD_CHART).click()

    def check_remove_button_is_present(self):
        assert EC.visibility_of_element_located(self.BIKE_LIGHT_REMOVE)
