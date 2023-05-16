Feature: Login to Jules app

  Scenario: Unsuccessful login
    Given I am on the Jules login page
    When I enter a correct email address and I leave the password field empty
    Then I should see an error message: "Please enter your password!"
    Then the Log in btn is disabled
    




