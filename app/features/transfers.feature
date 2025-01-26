Feature: Transfers
    @transfers
    Scenario: Making outgoing transfers
        Given a personal account with a balance of 1000
        When an outgoing transfer of 200 is made
        Then the account balance is 800
        And the account history contains an outgoing transfer of 200

    @transfers
    Scenario: Making incoming transfers
        Given a personal account with a balance of 1000
        When an incoming transfer of 500 is made
        Then the account balance is 1500
        And the account history contains an incoming transfer of 500

    @transfers
    Scenario: Making express transfers
        Given a personal account with a balance of 1000
        When an express transfer of 300 is made
        Then the account balance is 699
        And the account history contains an outgoing transfer of 300
        And the account history contains an express transfer fee