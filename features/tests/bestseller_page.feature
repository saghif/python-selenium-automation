Feature: Tests for Best Seller page

  Scenario: User sees correct number of subheader links
    Given Open Amazon BestSellers page
    Then Verify there are 5 subheader links