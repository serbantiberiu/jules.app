from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import Login_page


class Inventory_page(Login_page):
    username = "standard_user"
    password = "secret_sauce"
    items = {"Sauce Labs Backpack": "sauce-labs-backpack",
             "Sauce Labs Bike Light": "sauce-labs-bike-light",
             "Sauce Labs Bolt T-Shirt": "sauce-labs-bolt-t-shirt",
             "Sauce Labs Fleece Jacket": "sauce-labs-fleece-jacket",
             "Sauce Labs Onesie": "sauce-labs-onesie",
             "Test.allTheThings() T-Shirt (Red)": "test.allthethings()-t-shirt-(red)"}

    SHOPPING_CART_BTN = (By.CSS_SELECTOR, "a.shopping_cart_link")
    ITEMS_NUMBER_IN_CART = (By.CSS_SELECTOR, "span.shopping_cart_badge")
    ITEM_IN_CART = (By.CSS_SELECTOR, "div.inventory_item_name")
    CONTINUE_SHOPPING_BTN = (By.ID, "continue-shopping")

    def login(self):
        self.open_login_page()
        self.insert_username(self.username)
        self.insert_password(self.password)
        self.click_login_btn()

    def getAddCartLocator(self, item):
        return self.chrome.find_element(By.XPATH, f"//button[@id='add-to-cart-{item}']")

    def getRemoveLocator(self, item):
        return self.chrome.find_element(By.XPATH, f"//button[@id='remove-{item}']")

    def getItemInCart(self):
        return self.chrome.find_element(*self.ITEM_IN_CART)

    def click_add_cart_item(self, item):
        for i in self.items.keys():
            if i == item:
                self.getAddCartLocator(self.items.get(i)).click()

    def click_remove_item_from_cart(self, item):
        for i in self.items.keys():
            if i == item:
                self.getRemoveLocator(self.items.get(i)).click()

    def click_shopping_cart_btn(self):
        self.chrome.find_element(*self.SHOPPING_CART_BTN).click()

    def click_continue_shopping_btn(self):
        self.chrome.find_element(*self.CONTINUE_SHOPPING_BTN).click()

    def check_no_of_items_in_cart(self):
        no_of_items = self.chrome.find_element(*self.ITEMS_NUMBER_IN_CART).text
        assert no_of_items == "1", "Fail: There are more than one items in cart."

    def check_item_in_cart(self, item):
        item_in_cart_text = self.getItemInCart().text
        assert item == item_in_cart_text, f"Fail: The item {item} was not displayed in cart."

    def check_remove_button_is_present(self, item):
        for i in self.items.keys():
            if i == item:
                assert EC.visibility_of_element_located(self.getRemoveLocator(self.items.get(i))), \
                    f"Fail: The remove button for the item {item} is not displayed"

    def check_add_cart_button_is_present(self, item):
        for i in self.items.keys():
            if i == item:
                assert EC.visibility_of_element_located(self.getAddCartLocator(self.items.get(i))), \
                    f"Fail: The remove button for the item {item} is not displayed"
