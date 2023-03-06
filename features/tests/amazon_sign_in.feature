# Created by tahmina at 2/22/23
Feature: Amazon Sign In Page

  Scenario: User can see Sign In
    Given Open Amazon page
    When Click on orders
    Then Verify that Sign In page is opened


  Scenario: Sign in page can be opened from Sign In popup
    Given Open Amazon page
    When Click Sign In from popup
    Then Verify Sign In page opens