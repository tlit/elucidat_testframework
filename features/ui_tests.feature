Feature: Navigate to Case

  Background:
    Given I am on the course homepage

  Scenario: Navigate to the start page
    When I click the START button
    Then I see CardImage 1
    And I see CardImage 2

  Scenario: Current score
    When I click the START button
    Then the current score displays an integer

  Scenario Outline: Navigate to Case
    When I click the START button
    And I click CardImage <card_number>
    Then I see the "<landing_page>" page

    Examples:
      | card_number | landing_page         |
      | 1           | case1_landing_page   |
      | 2           | case2_landing_page   |

  Scenario Outline: Navigate through Case
    When I click the START button
    And I click CardImage <card_number>
    And I click the JUDGE THIS button
    Then I see the "<judgement_page>" page

    Examples:
      | card_number | judgement_page       |
      | 1           | case1_judgement_page |
      | 2           | case2_judgement_page |
