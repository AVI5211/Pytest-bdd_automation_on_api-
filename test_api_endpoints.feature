# Created by avira at 19-01-2024
Feature: Test API endpoints

  Scenario Outline: Test API endpoints with different user actions
    Given I make a GET request with user "<UserId>", post "<PostId>", comment "<CommentDesc>", URL "<URL>", sentiment "<Sentiment>", and endpoint "<endpoint>"
    Then the response status code should be 200

    Examples:
      | UserId | PostId | CommentDesc     | URL                                           | Sentiment | endpoint           |
      | 2      | 22     | wow you r awsome| http://3.27.18.54/index.php/comment-on-post   | Positive  | comment-on-post    |
      | 4      | 22     | love you        | http://3.27.18.54/index.php/comment-on-post   | Positive  | get-comment-on-post|
      | 5      | 22     | amazing         | http://3.27.18.54/index.php/comment-on-post   |           | comment-on-post    |
      | 6      | 22     | well            | http://3.27.18.54/index.php/comment-on-post   |           | comment-on-post    |
