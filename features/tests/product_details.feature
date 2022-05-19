Feature: Tests for product page

  Scenario: User can select colors
    Given Open Amazon product B07MNHBRCJ page
    Then Verify user can click through colors

  Scenario: Verify correct color has been selected
    Given Open Amazon product B081YS2F7N page
    Then Verify correct color has been selected