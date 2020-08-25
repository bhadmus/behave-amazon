# Created by Ademola Bhadmus at 2020-05-04
Feature: A guest shopper on a shopping site
  The tests steps involved in simulating a guest user journey on a shopping website

  Scenario: Test steps as a guest shopper on amazon.com
    Given I open amazon website
    When I search for an item
    And I select the item
    And I add it to cart
    And I attempt to checkout
    Then I should be redirected to the Signup or Login page
