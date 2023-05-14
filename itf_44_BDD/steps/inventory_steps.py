import time

from behave import *


@given("I am logged into the app")
def step_impl(context):
    context.inventory_page.login()

@when('I click Add to chart button to the item "{item}"')
def step_impl(context, item):
    time.sleep(3)
    context.inventory_page.press_add_cart_item(item)

@then('The Remove button is displayed for the item "{item}"')
def step_impl(context, item):
    context.inventory_page.check_remove_button_is_present(item)