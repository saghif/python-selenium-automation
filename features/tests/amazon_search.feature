Feature: Tests for Amazon search

  Scenario Outline: Verify that user can search for products
    Given Open Amazon page
    When Search for <search_word>
    Then Verify search results for <search_result> are shown
    Examples:
    |search_word  |search_result  |
    |table        |"table"        |
    |dress        |"dress"        |
    |spoons       |"spoons"       |


  Scenario: Product gets added to the cart
    Given Open Amazon page
    When Search for lol surprise omg doll
    And Click on the first product
    And Click on Add to cart btn
    Then Verify cart has 1 item


  Scenario: User sees ham menu btn on the main page
    Given Open Amazon page
    Then Verify hamburger menu btn present


  Scenario: User sees correct amount of footer links
    Given Open Amazon page
    Then Verify there are 38 footer links


