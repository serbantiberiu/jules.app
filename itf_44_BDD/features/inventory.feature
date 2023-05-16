Feature: Test add to cart and remove functionality

  Scenario Outline: Test add to cart and remove functionality for one item
    Given I am logged into the app
    When I click Add to chart button to the item "<item>"
    Then The Remove button is displayed for the item "<item>"
    Then The cart icon shows there is one item in cart
    When I check the basket page
    Then The item "<item>" is displayed in basket
    When I remove the item "<item>" from the cart
    When I go back to shopping list
    Then The Add to chart button is displayed for the item "<item>"

    Examples:
    |item                 |
    |Sauce Labs Backpack|
    |Sauce Labs Bike Light|
    |Sauce Labs Bolt T-Shirt|
    |Sauce Labs Fleece Jacket|
    |Sauce Labs Onesie|
    |Test.allTheThings() T-Shirt (Red)|