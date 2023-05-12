Feature: Test add to cart functionality

  Scenario: add to cart Sauce Labs Bike Light
    Given I am logged into the app
    When I click Add to chart button to the item "Sauce Labs Bike Light"
    Then The Remove button is displayed
    When I click Remove Button for the item "Sauce Labs Bike Light"
    Then The Add to chart button is displayed