Feature: Amazon Best Seller tests

  Scenario: Header has 5 links
    Given Open Best Seller page
    Then Verify that header has 5 links

  Scenario: Header links are working properly
    Given Open Best Seller page
    Then Verify that each link opens correct page