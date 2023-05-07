Feature: Sign up to Jules app

  Scenario: Sign up with Persona
    Given I am on the Jules sign up page
    When I click the "Sign up" button
    And I click the "Personal" button
    And I click the "Continue" button
    And I input my correct first name
    And I click the "Continue" button
    And I input my correct last name
    And I click the "Continue" button
    And I input a wrong email
    Then I should see the message "Please enter a valid email address."
    When I clear the email input
    And I input my correct email
    Then I should not see the message "Please enter a valid email address."