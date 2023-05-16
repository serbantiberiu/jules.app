from browser import Browser
from base_page import BasePage
from pages.login_page import Login_page
from pages.signup_page import Signup_Page


def before_all(context):
    context.browser = Browser()  # initializare obiect browser
    context.base_page = BasePage()
    context.login_page = Login_page()  # initializare obiect pagina login
    context.signup_page = Signup_Page()


def after_all(context):
    context.browser.close()
