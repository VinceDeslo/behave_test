Feature: Testing out behave

  Scenario: Run an uppercase test
    Given The string gets uppercased
    When I input "upper"
    Then I get "UPPER"

  Scenario: Run a lowercase test
    Given The string gets lowercased
    When I input "LOWER"
    Then I get "lower"

  Scenario: Run a capitalization test
    Given The string gets capitalized
    When I input "capitalize"
    Then I get "Capitalize"




