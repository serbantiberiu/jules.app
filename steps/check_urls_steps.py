from behave import *

@given("I am on jules.app login page")
def step_impl(context):
    context.login_page.open_login_page()

@when("I click Sign Up button")
def step_impl(context):
    context.login_page.click_signup_btn()

@when("I click Login button")
def step_impl(context):
    context.signup_page.click_login_button()

@then('I am redirected to the link "{url}"')
def step_impl(context, url):
    context.base_page.verifyUrl(url)

