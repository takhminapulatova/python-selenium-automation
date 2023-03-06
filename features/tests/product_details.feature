Feature: Tests for product page

  Scenario: User can select colors
    Given Open Amazon product B081YS2F7N page
    Then Verify user can click through colors


  Scenario:  User can select any color for product: B07BJKRR25
    Given Open Amazon product B07BJKRR25 page
    Then Verify that user can click through all colors