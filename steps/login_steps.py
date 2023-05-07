from selenium import webdriver
from behave import *
import time

@given("I am on the Jules App login page")
def step_impl(context):
    context.login_page.open_login_page()

@when("I insert a correct email and leave the password field empty")
def step_impl(context):
    context.login_page.insert_email("tashaphotographer@gmail.com")
    context.login_page.insert_password("")

@then("I am not logged into the app")
def step_impl(context):
    assert context.chrome.current_url == "https://jules.app/sign-in", "Please enter your password!"

@then('I receive the error message "Please enter your password!"')
def step_impl(context, error_message):
    context.login_page.check_login_error_message(error_message)

