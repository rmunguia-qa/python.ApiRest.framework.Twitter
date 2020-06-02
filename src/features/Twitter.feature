# -*- coding: utf-8 -*-

@Twitter
# Created by MuNGuia10 at 27/04/2020
Feature: Test Twitter
  # Twitter with OAuth 2.0

  @Labs_v2_UserById
    Scenario: GET Single user by ID
      Given Conectamos con el endpoint Scenary:API_Labs2/users/Scenary:userbyId
      When Login en Twitter con credenciales OAuth 2.0

      When Realizamos un GET al endpoint
      Then Mostramos el RESPONSE por pantalla

      And Verificar que <Entity> tenga el valor <Value>
        | Entity        | Value               |
        | data.id       | 588227834           |
        | data.name     | Assassin's Creed ES |
        | data.username | assassinsspain      |


  @Labs_v2_UserByUsername
    Scenario: GET Single user by Username
      Given Conectamos con el endpoint Scenary:API_Labs2/users/Scenary:byUsername?Scenary:queryUsername
      When Login en Twitter con credenciales OAuth 2.0

      When Realizamos un GET al endpoint
      Then Mostramos el RESPONSE por pantalla

      And Verificar que <Entity> tenga el valor <Value>
        | Entity                                | Value               |
        | data.created_at                       | NOT NULL            |
        | data.description                      | NOT NULL            |
        | data.id                               | 588227834           |
        | data.location                         | España              |
        | data.name                             | Assassin's Creed ES |
        | data.public_metrics.followers_count   | NOT NULL            |
        | data.public_metrics.tweet_count       | NOT NULL            |
        | data.url                              | NOT NULL            |
        | data.username                         | assassinsspain      |
        | data.verified                         | True                |


  @Labs_v2_MultipleUsersByUsername
    Scenario: GET Multiple user by list of Usernames
      Given Conectamos con el endpoint Scenary:API_Labs2/users/Scenary:byUsernames=Scenary:username1,Scenary:username2,Buenafuente
      When Login en Twitter con credenciales OAuth 2.0

      When Realizamos un GET al endpoint
      Then Mostramos el RESPONSE por pantalla

      And Verificar que <Entity> tenga el valor <Value>
        | Entity        | Value    |
        | data.id       | 1253323820078780422,588227834,6809022 |
        | data.name     | Munguia,Assassin's Creed ES,Andreu Buenafuente |
        | data.username | Munguia12584444,assassinsspain,Buenafuente |


  @Labs_v2_SingleTweet
    Scenario: GET Single tweet by ID
      Given Conectamos con el endpoint Scenary:API_Labs2/tweets/Scenary:tweetbyId?Scenary:queryTweet
      When Login en Twitter con credenciales OAuth 2.0

      When Realizamos un GET al endpoint
      Then Mostramos el RESPONSE por pantalla

      And Verificar que <Entity> tenga el valor <Value>
        | Entity                              | Value               |
        | data.author_id                      | 588227834           |
        | data.created_at                     | NOT NULL            |
        | data.id                             | 1255874552187371525 |
        | data.lang                           | es                  |
        | data.public_metrics                 | NOT NULL            |
        | data.public_metrics.retweet_count   | NOT NULL            |
        | data.public_metrics.like_count      | NOT NULL            |
        | data.source                         | Twitter Ads         |
        | data.text                           | NOT NULL            |


  @Labs_v2_RecentSearch
  Scenario: GET Search Tweets from the last 7 days that match with a search query
    Given Conectamos con el endpoint Scenary:API_Labs2/tweets/Scenary:bySearch?query=Scenary:querySearch
    When Login en Twitter con credenciales OAuth 2.0

    When Realizamos un GET al endpoint
    Then Mostramos el RESPONSE por pantalla

    And Verificar que <Entity> tenga el valor <Value>
      | Entity             | Value    |
      | data[0].id         | NOT NULL |
      | data[1].id         | NOT NULL |
      | data[2].id         | NOT NULL |
      | data[3].id         | NOT NULL |
      | data[4].id         | NOT NULL |
      | data[5].id         | NOT NULL |
      | data[6].id         | NOT NULL |
      | data[7].id         | NOT NULL |
      | data[8].id         | NOT NULL |
      | data[9].id         | NOT NULL |
      | meta.result_count  | 10 |


  @Labs_v1_MetricsTweet
    # https://api.twitter.com/labs/1/tweets/metrics/private?ids=
    # OAuth 1.0 Pending

  @Labs_v1_ListRules
    # https://api.twitter.com/labs/1/tweets/stream/filter/rules
    # OAuth 2.0 Bearer OK - Pte estudiar cómo funciona

  @Labs_v1_Stream
    # https://api.twitter.com/labs/1/tweets/stream/filter?format=detailed
    # OAuth 2.0 Bearer OK - Pte estudiar cómo funciona

  @Labs_v1_Rule
    # https://api.twitter.com/labs/1/tweets/stream/filter/rules?ids=1
    # OAuth 2.0 Bearer OK - Pte estudiar cómo funciona

  @Labs_v1_SampledStream
    # https://api.twitter.com/labs/1/tweets/stream/filter?format=detailed
    # OAuth 1.0 Pending