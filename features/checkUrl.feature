Feature: Check the links in the app

  Scenario: Check the links for sing-in and sign-up page
    Given I am on jules.app login page
    When I click Sign Up button
    Then I am redirected to the link "https://jules.app/sign-up"
    When I click Login button
    Then I am redirected to the link "https://jules.app/sign-in"