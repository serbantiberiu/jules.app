from browser import Browser
from pages.login_page import Login_page

def before_all(context):
    context.browser = Browser #initializare obiect browser
    context.login_page = Login_page() #initializare obiect pagina login

def after_all(context):
    context.browser.close()