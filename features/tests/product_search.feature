# Created by Svetlana at 4/4/19
Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given open Google page
    When input Bags into search field
    And click on search icon
    Then product results for Bags are shown
    And first result contains Bags