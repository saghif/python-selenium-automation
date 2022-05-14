# Created by bojanskaljak at 5/3/22
Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input Shoes into search field
    And Click on search icon
    Then Product results for Shoes are shown