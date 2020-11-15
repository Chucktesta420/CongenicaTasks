Feature: Buy ticket


Scenario Outline: I can buy a ticket
  Given I go to "https://www.tiketa.lt/EN/search"
  And Login into my account
  When I search <caption>
  And Select <cityName> city
  And Choose dates from <dateFrom> to <dateTo>
  And Click search button
  And Click <event> buy button
  And Select <event> event name with <price> price
  And Select <sector> sector
  Then I have selected a sector
  Examples:
  | caption     | cityName    | dateFrom   | dateTo     | event                                         | price    | sector                                 |
  | Pasaulinė   | Internet    | 2020-09-01 | 2022-09-01 | Pasaulinė lyderystės konferencija online 2020 |  59,50   | 1 asmens bilietas (1 prisijungimas)    |
  | CIRQUE      | Vilnius     | 2020-09-01 | 2022-09-01 | CIRQUE DU SOLEIL - CORTEO                     |  33,80   | 112                                    |