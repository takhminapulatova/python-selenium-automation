# Created by tahmina at 2/21/23
Feature: Amazon search tests

  Scenario Outline: User can search for coffee on Amazon
    Given Open Amazon page
    When Input text <search_word>
    And Click on search button
    Then Verify that text <search_result> is shown
    Examples:
    |search_word  |search_result   |
    |coffee       |"coffee"        |
    |table        |"table"         |

  Scenario: User can search for a table on Amazon
    Given Open Amazon page
    When Input text table
    When Click on search button
    Then Verify that text "table" is shown

  Scenario: Every product has a name and an image
    Given Open Amazon page
    When Input text coffee
    And Click on search button
    Then Verify that each product has a name and an image

  Scenario: User can select and search in a department
    Given Open Amazon page
    When Select department by alias audible
    And Input text Faust
    And Click on search button
    Then Verify audible department is selected

  Scenario: User can select any department and search for an item
    Given Open Amazon page
    When Select "Amazon Fresh" department
    And Input text Apples
    And Click on search button
    Then Verify that "Amazon Fresh" is selected
