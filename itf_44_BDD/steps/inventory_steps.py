from behave import *


@given("I am logged into the app")
def step_impl(context):
    context.inventory_page.login()


@when('I click Add to chart button to the item "{item}"')
def step_impl(context, item):
    context.inventory_page.click_add_cart_item(item)


@then('The Remove button is displayed for the item "{item}"')
def step_impl(context, item):
    context.inventory_page.check_remove_button_is_present(item)


@then('The cart icon shows there is one item in cart')
def step_impl(context):
    context.inventory_page.check_no_of_items_in_cart()


@when('I check the basket page')
def step_impl(context):
    context.inventory_page.click_shopping_cart_btn()


@then('The item "{item}" is displayed in basket')
def step_impl(context, item):
    context.inventory_page.check_item_in_cart(item)


@when('I remove the item "{item}" from the cart')
def step_impl(context, item):
    context.inventory_page.click_remove_item_from_cart(item)


@when('I go back to shopping list')
def step_impl(context):
    context.inventory_page.click_continue_shopping_btn()


@then('The Add to chart button is displayed for the item "{item}"')
def step_impl(context, item):
    context.inventory_page.check_add_cart_button_is_present(item)
