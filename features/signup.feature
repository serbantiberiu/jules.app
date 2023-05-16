Feature: Sign up to Jules app

  Scenario: Sign up with Personal
    Given I am on the Jules sign up page
    When I click the Sign up button
    And I click the Personal button
    And I click the Continue button
    And I input "Tiberiu" in first name field
    And I click the Continue button
    And I input "Serban" in last name field
    And I click the Continue button
    And I input "wrong_email" as a wrong email
    Then I should see the message: "Please enter a valid email address."
    When I clear the email input
    And I input my correct email
    Then The error message is no longer displayed