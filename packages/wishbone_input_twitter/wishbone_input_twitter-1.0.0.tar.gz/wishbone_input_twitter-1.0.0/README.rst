::

              __       __    __
    .--.--.--|__.-----|  |--|  |--.-----.-----.-----.
    |  |  |  |  |__ --|     |  _  |  _  |     |  -__|
    |________|__|_____|__|__|_____|_____|__|__|_____|
                                       version 2.2.0

    Build composable event pipeline servers with minimal effort.



    ======================
    wishbone.input.twitter
    ======================

    Version: 1.0.0

    Reads Tweets from Twitter.
    --------------------------


        Reads tweets from Twitter.


        Parameters:

            - consumer_key(str)()
               |  The Twitter consumer_key value to authenticate.

            - consumer_secret(str)()
                | The Twitter consumer_secret value to authenticate.

            - access_token(str)()
                | The Twitter access_token value to authenticate.

            - access_token_secret(str)()
                | The Twitter access_token_secret value to authenticate.

            - timeline(bool)(False)
                | If True includes all events of the authenticated user's timeline

            - users(list)[]
                | A list of users to follow

            - track(list)["#wishbone"]
                | A list of expressions to follow

        Queues:

            - outbox
               |  Incoming Tweets


