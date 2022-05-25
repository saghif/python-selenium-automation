Feature: Tests for Best Seller page


  Scenario: User sees correct number of subheader links
    Given Open Amazon BestSellers page
    Then Verify there are 5 subheader links

  Scenario: Verify Best Sellers links opens correct page
    Given Open Amazon page
    Given Open Amazon BestSellers page
    Then Clicks on each top link and verify that correct page opens


