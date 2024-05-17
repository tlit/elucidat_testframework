Feature: Elucidat Projects and Releases API tests

# This feature file tests some basic functions of the 'Projects and Releases' API
# The steps herein are as-yet unimplemented due to time constraints.

  Background:
    Given I have a valid API key

  Scenario Outline: List projects
    When I send a GET request to "https://api.elucidat.com/v2/projects"
    Then the response status code should be 200
    And the response should contain a list of projects
    And the project at index <index> should have id "<project_id>" and name "<project_name>"

    Examples:
      | index | project_id  | project_name |
      | 0     | foo         | foo_project  |
      | 1     | bar         | bar_project  |

  Scenario Outline: Count Releases on a Project
    When I send a GET request to "https://api.elucidat.com/v2/projects/<project_id>/releases"
    Then the response status code should be 200
    And the response should contain a list of releases
    And the number of releases should be <release_count>

    Examples:
      | project_id | release_count |
      | foo        | 5             |
      | bar        | 10            |

  Scenario Outline: Get Release details
    When I send a GET request to "https://api.elucidat.com/v2/releases/<release_id>"
    Then the response status code should be 200
    And the response should contain the release with id "<release_id>"
    And the release should have a title "<release_title>"

    Examples:
      | release_id | release_title  |
      | 123        | foo_release    |
      | 456        | bar_release    |
