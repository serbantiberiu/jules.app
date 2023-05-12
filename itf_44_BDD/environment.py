from browser import Browser
from pages.login_page import Login_page

def before_all(context):
    context.browser = Browser()
    context.login_page = Login_page()


def after_all(context):
    context.browser.close()
