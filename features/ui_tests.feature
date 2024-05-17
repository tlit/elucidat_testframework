Feature: Elucidat UI tests

# This feature file tests navigation from the course homepage, and functionality of the UI elements therein.
# The primary objective is to validate the presence and functionality of three "cases", as indicated by the text "Explore three cases..." found on the homepage.
# Due to an apparent absence of the third case, related tests currently fail.

  Background:
    Given I am on the course homepage

@test1
  Scenario: Navigate to the start page
    When I click the START button
    Then I see CardImage 1
    And I see CardImage 2
    And I see CardImage 3

@test2
  Scenario: Ensure the currrent score is an integer
    When I click the START button
    Then the current score displays an integer

@test3
  Scenario Outline: Navigate to a Case
    When I click the START button
    And I click CardImage <card_number>
    Then I see the "<landing_page>" page

    Examples:
      | card_number | landing_page         |
      | 1           | case1_landing_page   |
      | 2           | case2_landing_page   |
      | 3           | case3_landing_page   |

@test4
  Scenario Outline: Navigate through a Case
    When I click the START button
    And I click CardImage <card_number>
    And I click the JUDGE THIS button
    Then I see the "<judgement_page>" page

    Examples:
      | card_number | judgement_page       |
      | 1           | case1_judgement_page |
      | 2           | case2_judgement_page |
      | 3           | case3_judgement_page | 

@test5
  Scenario: Ensure vote cannot be cast without selecting a radiobutton
    When I click the START button
    And I click CardImage 1
    And I click the JUDGE THIS button
    Then the Vote button is locked