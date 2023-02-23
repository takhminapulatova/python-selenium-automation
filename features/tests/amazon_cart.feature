# Created by tahmina at 2/22/23
Feature: Amazon Cart page

  Scenario: User can check if the cart is empty
    Given Open Amazon page
    When  Click on the cart icon
    Then Verify that Amazon cart is empty

  Scenario: User can add any product into the cart
    Given Open Amazon page
    When Input text green tea mask stick
    And Click on search button
    And Click on the first product
    And Add the product to the cart
    Then Verify that Amazon cart is not empty