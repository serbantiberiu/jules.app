from behave import *


@given("I am logged into the app")
def step_impl(context):
    context.inventory_page.login()

@when('I click Add to chart button to an item')
def step_impl(context):
    context.inventory_page.press_add_char_item()

@then('The Remove button is displayed')
def step_impl(context):
    context.inventory_page.check_remove_button_is_present()