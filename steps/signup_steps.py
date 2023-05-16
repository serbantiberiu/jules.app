import time

from behave import *


@given("I am on the Jules sign up page")
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


@when('I input "{firstname}" in first name field')
def step_impl(context, firstname):
    context.signup_page.input_field(firstname)


@when('I input "{lastname}" in last name field')
def step_impl(context, lastname):
    context.signup_page.input_field(lastname)


@when('I input "{wrong_email}" as a wrong email')
def step_impl(context, wrong_email):
    context.signup_page.input_field(wrong_email)
    time.sleep(5)


@then('I should see the message: "{error_message}"')
def step_impl(context, error_message):
    context.signup_page.check_error_message(error_message)


@when("I clear the email input")
def step_impl(context):
    context.signup_page.clear_email_input()


@when("I input my correct email")
def step_impl(context):
    context.signup_page.input_field(context.signup_page.valid_email_address)


@then("The error message is no longer displayed")
def step_impl(context):
    context.signup_page.check_error_message_not_displayed()
