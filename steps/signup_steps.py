from behave import *
from selenium.webdriver.common.keys import Keys

@given("I am on the Jules sign in page")
def step_impl(context):
    context.signup_page.open_signin_page()

@when("I click the Sign up button")
def step_impl(context):
    context.signup_page.click_signup_btn()

@when("I click the Personal button")
def step_impl(context):
    context.signup_page.click_personal_btn()

@when("I click the Continue button")
def step_impl(context):
    context.signup_page.click_continue_btn()

@when("I input my correct first name")
def step_impl(context):
    context.signup_page.input_correct_firstname("Tasha")

@when("I input my correct last name")
def step_impl(context):
    context.signup_page.input_correct_lastname("Andreea")

@when("I input a wrong email")
def step_impl(context):
    context.signup_page.input_wrong_email("tash@gmai.com")

@then("I should see the message {error_msg}")
def step_impl(context, error_message):
    context.signup_page.verify_error_message(error_message)

@when("I clear the email input")
def step_impl(context):
    context.signup_page.clear_email_input()

@when("I input my correct email")
def step_impl(context):
    context.signup_page.input_correct_email("photographertasha@gmail.com")

@then("I receive the error message 'Please enter a valid email address.'")
def step_impl(context):
      context.signup_page.error_message_displayed()