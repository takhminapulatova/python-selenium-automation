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