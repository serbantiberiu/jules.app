from behave import *

@given("I am on the Jules login page")
def step_impl(context):
    context.login_page.open_login_page()

@when("I enter a correct email address and I leave the password field empty")
def step_impl(context):
    context.login_page.insert_email(context.login_page.valid_username)
    context.login_page.insert_password("asd")
    context.login_page.clear_pass_field()

@then('I should see an error message: "{error_message}"')
def step_impl(context, error_message):
    context.login_page.check_login_error_message(error_message)

@then("the Log in btn is disabled")
def step_impl(context):
    context.login_page.check_login_button_disabled()
