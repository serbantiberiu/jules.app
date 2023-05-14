from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import Login_page


class Inventory_page(Login_page):
    username = "standard_user"
    password = "secret_sauce"
    items = ["sauce-labs-bike-light", "sauce-labs-bolt-t-shirt"]
    def login(self):
        self.open_login_page()
        self.insert_username(self.username)
        self.insert_password(self.password)
        self.click_login_btn()

    def getAddCartLocator(self, item):
        return self.chrome.find_element(By.XPATH, f"//button[@id='add-to-cart-{item}']")

    def getRemoveLocator(self, item):
        return self.chrome.find_element(By.XPATH, f"//button[@id='remove-{item}']")

    def press_add_cart_item(self, item):
        for i in self.items:
            if i == item:
                self.getAddCartLocator(i).click()

    def check_remove_button_is_present(self, item):
        for i in self.items:
            if i == item:
                assert EC.visibility_of_element_located(self.getRemoveLocator(i))
